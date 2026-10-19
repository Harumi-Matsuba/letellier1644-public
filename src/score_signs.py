# EN: Sign-level accuracy on a page with a known answer: align each transcribed sign (with its possible values)
#     to the letters of the period decipherment, and count the signs whose value matches.
# 答えのある書簡で、書き起こした記号ごとの精度を測る。記号の値（主な値と別の値）を、当時の解読文の文字に動的計画法で
# 対応させ、値が合った記号の割合を出す。[ ] の平文の語は対応に使うが、数には入れない。
# 使い方: python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt [--strict]
#   --strict : 主な値だけを使う（別の値を許さない）
import sys, re
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode import load_lines, CODES, PAIRS

def norm(s):
    return re.sub(r'[^a-z]', '', s.lower()).translate(str.maketrans('jvy', 'iui'))

def load_vals(p, strict):
    d = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        s, main, other, _ = (ln.rstrip('\n').split('\t') + ['', '', ''])[:4]
        vs = [main] + ([] if strict else [o for o in other.split(',') if o])
        d[s] = [norm(v) for v in vs if norm(v)]
    return d

def signs(toks, vals):
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if i + 1 < len(toks) and (t, toks[i + 1]) in PAIRS:
            out.append((t + ' ' + toks[i + 1], [norm(PAIRS[(t, toks[i + 1])])], True)); i += 2; continue
        if t.startswith('['): out.append((t, [norm(t)], False))
        elif t in CODES: out.append((t, [norm(CODES[t])], True))
        else: out.append((t, vals.get(t, []), True))
        i += 1
    return out

def align(sg, ref):
    INF = 10**9; n, m = len(sg), len(ref)
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = D[i][j]
            if c == INF: continue
            if j < m and c + 1 < D[i][j + 1]: D[i][j + 1] = c + 1; B[i][j + 1] = ('ins', i, j)
            if i < n:
                if c + 1 < D[i + 1][j]: D[i + 1][j] = c + 1; B[i + 1][j] = ('del', i, j)
                for v in sg[i][1] or ['?']:
                    k = j + len(v)
                    if k <= m:
                        cost = 0 if ref[j:k] == v else 1
                        if c + cost < D[i + 1][k]: D[i + 1][k] = c + cost; B[i + 1][k] = ('ok' if cost == 0 else 'sub', i, j)
    i, j, res = n, m, {}
    while (i, j) != (0, 0):
        op, pi, pj = B[i][j]
        if op in ('ok', 'sub', 'del'): res[pi] = (op, ref[pj:j] if op != 'del' else '')
        i, j = pi, pj
    return res

if __name__ == '__main__':
    strict = '--strict' in sys.argv
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    vals = load_vals(a[0], strict); tx = dict(load_lines(a[1])); rf = dict(load_lines(a[2]))
    tot = ok = 0
    for lid in sorted(rf):
        ref = norm(''.join(rf[lid])); sg = signs(tx.get(lid, []), vals); res = align(sg, ref)
        bad = []
        for i, (t, vs, counted) in enumerate(sg):
            if not counted: continue
            tot += 1; op, got = res.get(i, ('del', ''))
            if op == 'ok': ok += 1
            else: bad.append(f'{t}:{"/".join(vs) or "?"}→{got or "-"}')
        print(f'{lid}\t' + ' '.join(bad))
    print(f'# signs {tot}  matched {ok}  accuracy {ok/tot:.3f}  strict={strict}')
