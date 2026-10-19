# Le Tellier から Marca への暗号書簡（1644年4月26日）の読み

[English README](README.en.md)

フランス国立図書館 BnF Baluze 103 f. 50 にある、陸軍卿 Michel Le Tellier からカタルーニャの Pierre de Marca への書簡の暗号部分を、友清理士氏が復元した「Le Tellier-Marca Cipher (1644)」の表で読んだ記録です。

- 資料：BnF Baluze 103（Affaires de Catalogne — Correspondance de Marca）、Gallica ark:/12148/btv1b9001389d の111コマ（f. 50r、冒頭に平文の日付「Du 26e avril 1644」、暗号20行）と112コマ（f. 50v、暗号12行）。
- 先行：友清理士氏は、同じ暗号の書簡のうち f. 50 だけを「undeciphered」としている（[Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)）。NoAutopilot/cipher-lab に、f. 50 を同じ表で部分的に読んだ下書きがある（2026-10-13 の版、「Status: partial」）。こちらの作業との関係は [docs/METHOD.md](docs/METHOD.md)。

## 現状（v0.1）
- f. 50r・v の32行を通して、フランス語の文として読めた（[docs/READING.md](docs/READING.md)）。値の分からない記号が9か所ある（[docs/OPEN.md](docs/OPEN.md)）。
- 鍵の値をかき混ぜた対照（1000回）：本物以上は0回（表の記号だけでも0回）。別の AI が独立に作った3つの書き起こしに同じ鍵を当てても、各0回。
- **較正**：当時の解読文がある f. 171r の13行を、答えを見ずに同じ鍵で読むと、当時の解読文との文字の一致率は 93.6%（337/360）。鍵を機械的に当てただけでは 84.2%。この読みも、細部に誤りを含みうる前提で使ってください。
- **書き起こしは人が確かめていません。** AI（Claude）が書き起こし、別の AI（Codex）の独立の書き起こし3回と照らして直しました。AI どうしの比較は、人による確認の代わりにはなりません。

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
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt           # 較正
python3 -m unittest discover -s tests
```

## AI の使用
書き起こし・鍵の補い・解読・スクリプト・文書は、Anthropic の Claude（Claude Code、Claude Opus 5.5）が行いました。書き起こしの照合に OpenAI の Codex を使いました。対象の選定、作業の指示、公開の判断は人が行いました。詳しくは [docs/METHOD.md](docs/METHOD.md)。

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f50.txt | f. 50 の記号名での書き起こし（照合後）。照合前は transcription_f50_before_xcheck.txt |
| data/SIGNS.md | 記号名と形 |
| data/key.tsv | 記号名→値。source 列で出典（友清氏の表・兄弟書簡の照合・推定）を区別 |
| data/decoded_f50.txt | `src/decode.py` の出力 |
| data/f230r_pairs.txt、data/f232r_decipherment.txt | 兄弟書簡 f. 230r と当時の解読文の対応 |
| docs/READING.md、READING.en.md | 読み（行ごとの確かさの印つき）と要約 |
| docs/METHOD.md | 方法、数字、先行研究との関係、AI の使用 |
| docs/OPEN.md | 値の分からない記号、確かめていないこと |
| calib/ | 較正（f. 171r／f. 172r） |
| xcheck/ | 別の AI（Codex）による独立の書き起こし3回と、照合の結果 |
| SOURCES.md | 出典と、先行の確かめ |
