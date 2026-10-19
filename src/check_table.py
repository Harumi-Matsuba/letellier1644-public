# EN: Check the key rows whose source includes T against the table transcription: is each value in a column
#     that holds the sign? Prints only rows that are not "ok".
# 鍵のうち source に T を含む行を、友清氏の表の書き写し（data/tomokiyo_table_signs.tsv）と突き合わせる
# 使い方: python3 src/check_table.py data/key.tsv data/tomokiyo_table_signs.tsv
import sys
tab = {}
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    col, signs = l.rstrip('\n').split('\t')
    for s in signs.split(): tab.setdefault(s.rstrip('?'), set()).add(col)
n = bad_main = 0
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    s, main, other, src = (l.rstrip('\n').split('\t') + ['', '', ''])[:4]
    if 'T' not in src: continue
    n += 1; cols = tab.get(s, set())
    others = [o for o in other.split(',') if o and o.lower() not in cols]
    if main.lower() not in cols:
        bad_main += 1; print(f'{s}\tmain {main} not in table columns {sorted(cols)}')
    elif others:
        print(f'{s}\tother {",".join(others)} not in the table (from S or X)')
print(f'# T rows {n}  main value not in table {bad_main}')
