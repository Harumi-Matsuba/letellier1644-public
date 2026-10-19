# EN: Build docs/index.html (check by hand): for every line, the IIIF image from BnF (linked, not stored),
#     the sign names and their main values, and the decoded line; then the key.
# 手で確かめるページ docs/index.html を作る。画像は BnF の IIIF から読み込むだけで、リポジトリには入れない
# 使い方: python3 src/make_page.py > docs/index.html
import sys, html
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode import load_key, load_lines, decode
key, src = load_key('data/key.tsv'); lines = load_lines('data/transcription_f50.txt')
W, H = 4864, 6996
REC = dict(x=int(W * 0.33), y0=int(H * 0.165), w=int(W * 0.51), gap=229, canvas=111,
           peaks=[216, 460, 690, 903, 1143, 1339, 1573, 1784, 2013, 2222, 2443, 2674, 2914, 3149, 3364, 3573, 3808, 4025, 4268, 4494])
VER = dict(x=int(W * 0.22), y0=int(H * 0.125), w=int(W * 0.64), gap=226, canvas=112,
           peaks=[220, 434, 657, 893, 1098, 1358, 1580, 1827, 2053, 2297, 2502, 2735])
def url(d, k):
    y = d['y0'] + d['peaks'][k] - int(d['gap'] * 0.62); h = int(d['gap'] * 1.17)
    return f"https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9001389d/f{d['canvas']}/{d['x']},{y},{d['w']},{h}/1600,/0/default.jpg"
rows = []
for lid, toks in lines:
    d = REC if lid[0] == 'r' else VER; k = int(lid[1:]) - 1
    cells = ''.join(f'<td><code>{html.escape(t)}</code><br><b>{html.escape(decode([t], key))}</b></td>' for t in toks)
    rows.append(f'<section><h3>{"f. 50r" if lid[0] == "r" else "f. 50v"} line {k + 1}</h3><img loading="lazy" src="{url(d, k)}" alt="{lid}"><div class="t"><table><tr>{cells}</tr></table></div><p>{html.escape(decode(toks, key))}</p></section>')
keyrows = ''.join('<tr>' + ''.join(f'<td>{html.escape(c)}</td>' for c in (l.rstrip("\n").split("\t") + ["", "", ""])[:4]) + '</tr>'
                  for l in open('data/key.tsv', encoding='utf-8') if l.strip() and not l.startswith('#'))
print(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Le Tellier to Marca, 1644: check by hand</title>
<style>:root{{--bg:#fff;--fg:#1a1a1a;--mute:#666;--line:#ddd}}@media (prefers-color-scheme:dark){{:root{{--bg:#151515;--fg:#eee;--mute:#aaa;--line:#333}}}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif;max-width:1100px;margin:0 auto;padding:16px}}
img{{max-width:100%;border:1px solid var(--line);background:#fff}}.t{{overflow-x:auto}}td{{border:1px solid var(--line);padding:2px 4px;text-align:center;font-size:13px;white-space:nowrap}}
p{{font-family:ui-monospace,monospace}}.m{{color:var(--mute)}}</style></head><body>
<h1>BnF Baluze 103 f. 50: Le Tellier to Marca, 26 April 1644 — check by hand</h1>
<p class="m">Each line: the manuscript image (loaded from the BnF IIIF server, not stored in this repository; Source gallica.bnf.fr / BnF), the sign names of our transcription with the main value of each sign, and the decoded line. Code groups are shown expanded. The transcription was made by an AI (Claude) and cross-checked against five independent AI transcriptions (Codex); it has <b>not</b> been checked by a person. The joined reading is in <a href="READING.en.md">READING.en.md</a>; sign shapes are named in <a href="../data/SIGNS.md">data/SIGNS.md</a>.</p>
{''.join(rows)}
<h2>Key</h2><p class="m">sign, main value, other values, source (T = Tomokiyo's table, S = checked on f. 230r against the period decipherment f. 232r, X = split after the AI cross-check, C = inferred from f. 50 only).</p>
<div class="t"><table>{keyrows}</table></div>
</body></html>''')
