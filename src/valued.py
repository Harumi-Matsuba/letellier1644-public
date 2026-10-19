# EN: Share of cipher signs that have a value (key value or a known code group), with and without inferred values.
# 値の付いた記号の割合（推定込み・推定なし）。[ ] の平文の語と [消] は数えない
# 使い方: python3 src/valued.py data/key.tsv data/transcription_f50.txt
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode import load_key, load_lines, CODES, PAIRS
key, src = load_key(sys.argv[1])
tot = val = val_noC = 0; unk = []
for lid, toks in load_lines(sys.argv[2]):
    i = 0
    while i < len(toks):
        t = toks[i]
        if t.startswith('['): i += 1; continue
        if i + 1 < len(toks) and (t, toks[i + 1]) in PAIRS:
            tot += 2; val += 2; val_noC += 2; i += 2; continue
        tot += 1
        ok = (t in CODES and CODES[t] != '(=o)') or (t in key and key[t] not in ('?', ''))
        if ok:
            val += 1
            if t in CODES or src.get(t) != 'C': val_noC += 1
        else: unk.append(f'{lid}:{t}')
        i += 1
print(f'signs {tot}  valued {val} ({val/tot:.1%})  without inferred (source C only) {val_noC} ({val_noC/tot:.1%})')
print('no value: ' + ' '.join(unk))
