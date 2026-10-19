# 較正：私の読み（または鍵の機械的な当てはめ）と、当時の解読文を、行ごとに文字の編集距離で比べる
# 文字だけを残し（小文字、j→i、v→u、y→i）、一致率＝一致した文字数／答えの文字数
# 使い方: python3 src/calib.py 読み.txt 答え.txt
import sys, re
def load(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        lid, _, rest = ln.partition(' ')
        rest = re.sub(r'\([^)]*\)', '', rest)
        s = re.sub(r'[^a-z]', '', rest.lower()).translate(str.maketrans('jvy', 'iui'))
        d[lid] = s
    return d
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            m[i][j] = m[i-1][j-1]+1 if a[i-1] == b[j-1] else max(m[i-1][j], m[i][j-1])
    return m[-1][-1]
r, a = load(sys.argv[1]), load(sys.argv[2])
tot = hit = 0
for lid in sorted(a):
    x = r.get(lid, ''); y = a[lid]; h = lcs(x, y)
    tot += len(y); hit += h
    print(f'{lid}\t{h}/{len(y)}\t{x}\t{y}')
print(f'# matched {hit}/{tot} = {hit/tot:.1%}')
