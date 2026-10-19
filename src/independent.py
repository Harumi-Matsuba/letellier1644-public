# EN: Agreement between the final transcription and the independent Codex pass made after all corrections.
# 直した後の最終の書き起こしと、そのあと新しく1回読ませた Codex（独立の2回目）との一致を数える
# 使い方: python3 src/independent.py data/transcription_f50.txt second/codex_independent.txt > second/independent_compare.tsv
import sys, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from xcompare import load_mine, load_ai, align
SAME = {'g': '9', 'zc': 'zx', 'hb': 'k', '=g': '=9', 'ae': 'x'}   # 鍵で同じ値になる名前（ae は横線のない曲がった x）
def canon(t): t = t.split('/')[0]; return SAME.get(t, t)
mine = load_mine(sys.argv[1]); ai = load_ai(sys.argv[2])
tot = exact = same = 0; kinds = collections.Counter()
print('line\tpos\tfinal\tcodex\tsame_value')
for lid in sorted(mine):
    x = mine[lid]; al = align(x, ai.get(lid, []))
    for i, t in enumerate(x):
        v = al.get(i, '-'); tot += 1
        e = v == t or t in v.split('/'); s = e or canon(v) == canon(t)
        exact += e; same += s
        if not e: print(f'{lid}\t{i+1}\t{t}\t{v}\t{"yes" if s else "no"}')
        if not s: kinds[(t, v)] += 1
print(f'# signs {tot}  same name {exact} ({exact/tot:.3f})  same value class {same} ({same/tot:.3f})', file=sys.stderr)
print('# differing (final, codex): ' + ', '.join(f'{a}/{b} {n}' for (a, b), n in kinds.most_common()), file=sys.stderr)
