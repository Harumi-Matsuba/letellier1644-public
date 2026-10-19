# EN: Apply the key (main values) to a sign-name transcription, line by line.
# 書き起こし（記号名）に鍵の主な値を当てて、1行ずつ文字列にする
# 使い方 / usage: python3 src/decode.py data/key.tsv data/transcription_f50.txt [--table-only]
import sys

CODES = {'=9': 'pour', '=11': 'que', '=12': 'qui', '=26': 'vous', '=32': 'Barcelone',
         '=81': 'faire', '81': 'faire', '39': 'Catalogne', '=39': 'Catalogne',
         '=y': 'Monsieur le Mareschal', '=3': 'de La Motte', '=83': 'le Gouverneur', '=5': 'ordres', '=o': '(=o)'}
# 2語で1つの符号：=11 =o = la Reyne、=l =m = du Roi
PAIRS = {('=11', '=o'): 'la Reyne', ('=l', '=m'): 'du Roi'}


def load_key(p, table_only=False):
    key, src = {}, {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        s, main, other, so = (ln.rstrip('\n').split('\t') + ['', '', ''])[:4]
        if table_only and 'T' not in so:
            continue
        key[s], src[s] = main, so
    return key, src


def load_lines(p):
    out = []
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        a = ln.split()
        out.append((a[0], a[1:]))
    return out


def decode(toks, key):
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if i + 1 < len(toks) and (t, toks[i + 1]) in PAIRS:
            out.append(' ' + PAIRS[(t, toks[i + 1])] + ' '); i += 2; continue
        if t.startswith('['):
            out.append(' ' + t.strip('[]') + ' ')
        elif t in CODES:
            out.append(' ' + CODES[t] + ' ')
        elif t.startswith('='):
            out.append(' <' + t + '> ')
        elif t == 'cut':
            out.append('…')
        else:
            out.append(key.get(t, '?'))
        i += 1
    return ' '.join(''.join(out).split())


if __name__ == '__main__':
    key, _ = load_key(sys.argv[1], '--table-only' in sys.argv)
    for lid, toks in load_lines(sys.argv[2]):
        print(lid, decode(toks, key))
