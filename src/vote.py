# EN: Vote: for every sign of the final transcription, the names given by each AI pass at the aligned place.
#     Names that carry the same value in the key (9/g, x/ae, zx/zc, k/hb) count as one.
# 投票：最終の書き起こしの記号ごとに、各 AI の回が対応する位置で付けた名前を集め、多数を数える。
# 鍵で同じ値になる名前（9 と g、x と ae、zx と zc、k と hb）は同じとみなす。
# 使い方: python3 src/vote.py data/transcription_f50.txt second/codex_pass*.txt > second/vote.tsv
import sys, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from xcompare import load_mine, load_ai, align
SAME = {'g': '9', 'ae': 'x', 'zc': 'zx', 'hb': 'k', '=g': '=9', 'mi': 'mz'}  # mi は Codex に渡した名前の一覧になかった
def canon(t):
    t = t.split('/')[0].strip('[]')
    return SAME.get(t, t)
mine = load_mine(sys.argv[1]); ais = [load_ai(p) for p in sys.argv[2:]]
N = len(ais); stats = collections.Counter()
print('line\tpos\tfinal\t' + '\t'.join(f'ai{k+1}' for k in range(N)) + '\tagree\tmajority')
for lid in sorted(mine):
    x = mine[lid]
    al = [align(x, a.get(lid, [])) for a in ais]
    for i, t in enumerate(x):
        vs = [a.get(i, '-') for a in al]
        agree = sum(canon(v) == canon(t) or canon(t) in [canon(w) for w in v.split('/')] for v in vs)
        c = collections.Counter(canon(v) for v in vs).most_common(1)[0]
        maj = c[0] if c[1] > N // 2 else 'none'
        stats['signs'] += 1
        if agree > N // 2: stats['majority_agrees'] += 1
        elif maj != 'none': stats['majority_differs'] += 1
        else: stats['no_majority'] += 1
        if agree == N: stats['all_agree'] += 1
        print(f'{lid}\t{i+1}\t{t}\t' + '\t'.join(vs) + f'\t{agree}/{N}\t{maj}')
print('# ' + '  '.join(f'{k} {v}' for k, v in stats.items()), file=sys.stderr)
