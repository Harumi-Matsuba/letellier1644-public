# Claude の書き起こしと、別の AI の書き起こし（second/codex_pass*.txt）を行ごとに並べて比べる
# 記号の並びを編集距離で対応させ、一致・食い違い・3回の多数を数える
# 使い方: python3 src/xcompare.py data/transcription_f50_before_xcheck.txt second/codex_pass1.txt second/codex_pass2.txt second/codex_pass3.txt > 出力.tsv
import sys, re
def norm(t):
    t = t.strip()
    return t
def load_mine(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        a = ln.split(); lid = a[0]
        lid = ('r_L' if lid[0]=='r' else 'v_L') + lid[1:]
        d[lid] = [t for t in a[1:] if t != 'cut']
    return d
def load_ai(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        ln = ln.strip()
        m = re.match(r'([rv]_L\d\d)\s+(.*)', ln)
        if not m: continue
        toks = re.findall(r'\?\{[^}]*\}|\S+', m.group(2))
        d[m.group(1)] = toks
    return d
def match(a, b):
    if a == b: return True
    return a in b.split('/')
def align(x, y):
    n, m = len(x), len(y)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1] + (0 if match(x[i-1], y[j-1]) else 1))
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (0 if match(x[i-1], y[j-1]) else 1):
            out.append((i-1, y[j-1])); i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1:
            out.append((i-1, '-')); i -= 1
        else:
            j -= 1
    return dict(out)
if __name__ == '__main__':
    mine = load_mine(sys.argv[1]); ais = [load_ai(p) for p in sys.argv[2:]]
    tot = 0; agree = [0]*len(ais); maj_dis = 0; allagree = 0
    print('line\tpos\tmine\t' + '\t'.join(f'ai{k+1}' for k in range(len(ais))) + '\tmajority_vs_mine')
    for lid in sorted(mine):
        x = mine[lid]; al = [align(x, a.get(lid, [])) for a in ais]
        for i, t in enumerate(x):
            tot += 1
            vs = [a.get(i, '-') for a in al]
            ok = [match(t, v) for v in vs]
            for k, o in enumerate(ok): agree[k] += o
            if all(ok): allagree += 1
            # 3回のうち2回以上が同じ別の読みなら「多数が違う」
            others = [v for v, o in zip(vs, ok) if not o]
            flag = ''
            if sum(ok) <= len(ais) // 2:
                from collections import Counter
                c = Counter(others).most_common(1)
                if c and c[0][1] >= 2: flag = 'MAJ:' + c[0][0]; maj_dis += 1
                else: flag = 'split'
            if not all(ok): print(f'{lid}\t{i+1}\t{t}\t' + '\t'.join(vs) + f'\t{flag}')
    print(f'# total {tot}  agree per pass {agree}  all-agree {allagree}  majority-differs {maj_dis}', file=sys.stderr)
