# 対照実験：鍵の値をかき混ぜた鍵と、本物の鍵とで、f.50 の平文のフランス語らしさを比べる
# フランス語らしさ＝文字3連の対数尤度の平均（wordfreq の仏語上位5万語を頻度で重み付け。Harumi-Matsuba/matignon1586-public の src/control.py と同じ作り）
# 語の符号（=N）と平文の語（[..]）、鍵にない記号で区切り、1文字の記号の並びだけを採点する
# 使い方: python3 src/control.py data/key.tsv data/transcription_f50.txt [試行回数] [--table-only]
import sys, math, random, collections
from wordfreq import top_n_list, word_frequency
from decode import load_key, load_lines
def build_model():
    tri = collections.Counter(); bi = collections.Counter()
    for w in top_n_list('fr', 50000):
        w2 = ''.join(c for c in w.lower() if c.isalpha())
        w2 = w2.replace('œ', 'oe').translate(str.maketrans('éèêëàâäîïôöùûüç', 'eeeeaaaiioouuuc'))
        w2 = w2.replace('j', 'i').replace('v', 'u')
        if not w2: continue
        f = word_frequency(w, 'fr'); s = '^' + w2 + '$'
        for i in range(len(s) - 2):
            tri[s[i:i+3]] += f; bi[s[i:i+2]] += f
    alpha = 27
    return lambda a, b, c: math.log((tri[a+b+c] + 1e-7) / (bi[a+b] + 1e-7 * alpha))
def runs(lines, key):
    out = []
    for _, toks in lines:
        cur = []
        for t in toks:
            if t not in key:
                if cur: out.append(cur); cur = []
                continue
            cur.append(t)
        if cur: out.append(cur)
    return out
def score(rs, key, lp):
    tot = n = 0
    for r in rs:
        s = ''.join(key[k] for k in r).replace('v', 'u')
        for i in range(len(s) - 2):
            tot += lp(s[i], s[i+1], s[i+2]); n += 1
    return tot / n, n
if __name__ == '__main__':
    to = '--table-only' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    key, _ = load_key(args[0], to); lines = load_lines(args[1])
    N = int(args[2]) if len(args) > 2 else 1000
    lp = build_model(); rs = runs(lines, key)
    real, n = score(rs, key, lp)
    signs = sorted(key); vals = [key[s] for s in signs]
    random.seed(1); sh = []
    for _ in range(N):
        v = vals[:]; random.shuffle(v)
        sh.append(score(rs, dict(zip(signs, v)), lp)[0])
    sh.sort()
    print(f'table_only={to} signs={len(key)} trigrams={n}')
    print(f'real {real:.3f}  shuffled median {sh[N//2]:.3f}  p99 {sh[int(N*0.99)]:.3f}  max {sh[-1]:.3f}  shuffled>=real {sum(s>=real for s in sh)}/{N}')
