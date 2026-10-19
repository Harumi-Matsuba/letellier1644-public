# Le Tellier から Marca への暗号書簡（1644年4月26日）の読み（v0.1）

[English README](README.en.md)

フランス国立図書館 BnF Baluze 103 f. 50 にある、陸軍卿 Michel Le Tellier からカタルーニャの Pierre de Marca への書簡の暗号部分を、友清理士氏が復元した「Le Tellier-Marca Cipher (1644)」の表で読んだ記録です。

- **状態：全文の読み（v0.1）。** f. 50r・v の暗号32行を通して読んだ。値の分からない記号・語が10か所ある（[docs/OPEN.md](docs/OPEN.md)）。
- **先行との関係：** 友清理士氏は、同じ暗号の書簡のうち f. 50 だけを「undeciphered」としている（[Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)）。NoAutopilot/cipher-lab に、f. 50 を同じ表で部分的に読んだ下書きがある（2026-10-13 の版、「Status: partial」、630記号中451に値）。その下書きにすでに出ている語（「conseil」「que ledit」「descouvert」「surtou[t]」など、reading.txt の f50r L01・L09、f50v L09・L10）は、この読みでは **再現（reproduced）** であって新しくない。新しいのは、通した読み・鍵の補い・語の符号の確かめ・内容（下の「この読みで加えたこと」）。
- **人は書き起こしを確かめていません。** 書き起こしは AI（Claude）が作り、別の AI（OpenAI Codex）が画像だけから独立に作った5回の書き起こしと照らして直しました。AI どうしの一致は、人による確認の代わりにはなりません。
- **数字：**
  - 2回目の書き起こし：Codex 5回。最終の書き起こし626記号のうち、5回とも同じ 581、多数が一致 613（[second/VOTE.md](second/VOTE.md)）。照合前の書き起こしとの一致は、Codex 1〜3回目で 565・554・559／633（[second/RESULT.md](second/RESULT.md)）。
  - 対照：鍵の値をかき混ぜた鍵1000通りで、本物以上は0回。表の記号だけ、f. 50 の文脈から推定した値を外した鍵、最後の5分の1だけ、Codex の5つの書き起こし、のどれでも0回（[controls/results.txt](controls/results.txt)）。
  - 較正：当時の解読文がある f. 171r の13行を、答えを見ずに同じ鍵で読むと、記号ごとの精度 0.924（256/277。主な値だけなら 0.874）、読みの文字の一致 93.6%（337/360）（[calib/RESULT.md](calib/RESULT.md)）。
  - 数字の出どころは [NUMBERS.md](NUMBERS.md)。
- **手で確かめる：** [docs/index.html](docs/index.html) に、行ごとの画像（BnF の IIIF から読み込む）と、記号名・値を並べた。
- **AI の使用：** 書き起こし・鍵の補い・解読・スクリプト・文書は Anthropic の Claude（Claude Code、Claude Opus 5.5）。2回目の書き起こしは OpenAI の Codex。対象の選定、作業の指示、公開の判断は人。

（v0.1 が最初の版。版を上げたら、ここに変更点を書く。）

## 内容（要約）
- バルセロナの参事たちは Marca の宿を用意するにあたり、La Motte 元帥の友人の家を選んだ。その友人は、Marca の言動や宮廷との書簡の中身を逐一知るつもりでいる。Marca は用心し、言いくるめられないように。
- 宮廷でバルセロナの用を務める者が、カタルーニャ人から自分に宛てた包みが開けられていると何度も訴えている。王妃は Marca がこれを見張り、分かったことを知らせることを強く望んでいる。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- 鍵の表：友清理士氏の復元（[louisxiv_0marca1644.png](https://cryptiana.web.fc2.com/code/louisxiv_0marca1644.png)）。表の画像はこのリポジトリに含めていません。
- コマ番号の対応と、f. 190r・f. 205r の当時の解読文の書き起こし：NoAutopilot/cipher-lab。

**この読みで加えたこと**
1. f. 50r・v の記号を、記号名で行ごとに書き起こした（`data/transcription_f50.txt`）。
2. 兄弟書簡 f. 230r と当時の解読文 f. 232r を記号ごとに対応させ、表の値を確かめ、表にない記号の値を足した（`data/f230r_pairs.txt`）。
3. 語の符号 =y（Monsieur le Mareschal）、=3（de La Motte）、=11 =o（la Reyne）を兄弟書簡で確かめた。
4. 書簡の内容。対照・較正・別の AI との照合。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f50.txt               # 鍵の全記号
python3 src/decode.py data/key.tsv data/transcription_f50.txt --table-only  # 友清氏の表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f50.txt 1000         # 対照（wordfreq が必要）
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt           # 較正（読みの文字）
python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt  # 較正（記号ごと）
sh controls/run.sh                                                         # 対照をすべて計算し直す
python3 -m unittest discover -s tests
```

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f50.txt | f. 50 の記号名での書き起こし（照合後）。照合前は transcription_f50_before_second.txt |
| data/SIGNS.md | 記号名と形 |
| data/key.tsv | 記号名→値。source 列で出典（友清氏の表・兄弟書簡の照合・推定）を区別 |
| data/decoded_f50.txt | `src/decode.py` の出力 |
| data/f230r_pairs.txt、data/f232r_decipherment.txt | 兄弟書簡 f. 230r と当時の解読文の対応 |
| docs/READING.md、READING.en.md | 読み（行ごとの確かさの印つき）と要約 |
| docs/METHOD.md、METHOD.en.md | 方法、数字、先行研究との関係、AI の使用 |
| docs/OPEN.md、OPEN.en.md | 値の分からない記号、確かめていないこと |
| calib/ | 較正（f. 171r／f. 172r） |
| second/ | 2回目の書き起こし：Codex 5回の出力、照合（RESULT.md）と投票（VOTE.md） |
| controls/ | 対照の入力と結果（results.txt）、計算し直すスクリプト（run.sh） |
| docs/index.html | 手で確かめるためのページ（行ごとに Gallica の画像と記号名・値。GitHub Pages 用、まだ有効にしていない） |
| NUMBERS.md | README の数字の出どころ |
| CITATION.cff、.zenodo.json | 引用情報（DOI は付けていない） |
| SOURCES.md、SOURCES.en.md | 出典と、先行の確かめ |
