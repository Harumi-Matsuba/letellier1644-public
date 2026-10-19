# EN: Align a sister letter's transcription with its period decipherment, line by line, and count which letter
#     each sign stands for. Each cipher sign takes one letter (or none, at a cost); code groups and clear words
#     take their words. A sign costs 0 where the letter is one of its key values, 0.6 where it is not.
# 兄弟書簡の書き起こしを当時の解読文と行ごとに対応させ、記号ごとに当たった字を数える。
# 使い方: python3 src/align_sister.py data/key.tsv data/f230r_tx.txt data/f232r_ref_l1-21.txt [詳細.tsv]
import sys, re, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode import load_lines
CODEW = {'=9': ['pour'], '=11': ['que'], '=12': ['qui', 'quil'], '=26': ['vous'], '=32': ['barcelone'], '81': ['faire'],
         '=81': ['faire'], '39': ['catalogne'], '=39': ['catalogne'], '=y': ['monsieurlemareschal', 'mlemareschal'],
         '=3': ['delamotte'], '=5': ['ordres', 'ordre'], '=83': ['legouuerneur', 'legouverneur']}
def norm(s): return re.sub(r'[^a-z]', '', s.lower()).translate(str.maketrans('jvy', 'iui'))
def load_vals(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        s, main, other, _ = (ln.rstrip('\n').split('\t') + ['', '', ''])[:4]
        d[s] = {norm(v) for v in [main] + other.split(',') if norm(v)}
    return d
def options(t, vals):
    if t.startswith('['): return [norm(t)] if t != '[消]' else ['']
    if t in CODEW: return [norm(w) for w in CODEW[t]]
    return None
def align(toks, ref, vals):
    n, m = len(toks), len(ref); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = D[i][j]
            if c >= INF: continue
            if j < m and c + 1 < D[i][j + 1]: D[i][j + 1] = c + 1; B[i][j + 1] = (i, j, None)   # 解読文の字が余る
            if i == n: continue
            t = toks[i]; opts = options(t, vals)
            if opts is not None:
                for w in opts:
                    k = j + len(w)
                    if k <= m and ref[j:k] == w and c < D[i + 1][k]: D[i + 1][k] = c; B[i + 1][k] = (i, j, w)
                if c + 2 < D[i + 1][j]: D[i + 1][j] = c + 2; B[i + 1][j] = (i, j, '')
                continue
            if c + 1 < D[i + 1][j]: D[i + 1][j] = c + 1; B[i + 1][j] = (i, j, '')                  # 記号が余る
            if j < m:
                cost = 0 if ref[j] in vals.get(t, set()) else 0.6
                if c + cost < D[i + 1][j + 1]: D[i + 1][j + 1] = c + cost; B[i + 1][j + 1] = (i, j, ref[j])
    i, j, out = n, m, {}
    while (i, j) != (0, 0):
        pi, pj, w = B[i][j]
        if pi != i: out[pi] = w
        i, j = pi, pj
    return out
if __name__ == '__main__':
    vals = load_vals(sys.argv[1]); tx = dict(load_lines(sys.argv[2])); rf = dict(load_lines(sys.argv[3]))
    det = open(sys.argv[4], 'w', encoding='utf-8') if len(sys.argv) > 4 else None
    tally = collections.defaultdict(collections.Counter)
    for lid in sorted(rf):
        toks = tx.get(lid, []); ref = norm(''.join(rf[lid])); res = align(toks, ref, vals)
        for i, t in enumerate(toks):
            w = res.get(i, '')
            if options(t, vals) is None:
                tally[t][w or '-'] += 1
            if det: det.write(f'{lid}\t{i+1}\t{t}\t{w or "-"}\n')
    print('sign\tkey_values\taligned_letters')
    for s in sorted(tally, key=lambda x: (-sum(tally[x].values()), x)):
        c = tally[s]; kv = ','.join(sorted(vals.get(s, []))) or '(none)'
        print(f'{s}\t{kv}\t' + ' '.join(f'{k}:{v}' for k, v in c.most_common()))
