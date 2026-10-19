# Le Tellier から Marca への暗号書簡（1644年4月26日）の読み

[English README](README.en.md)

フランス国立図書館 BnF Baluze 103 f. 50 にある、陸軍卿 Michel Le Tellier からカタルーニャの Pierre de Marca への書簡の暗号部分を、友清理士氏が復元した「Le Tellier-Marca Cipher (1644)」の表で読んだ記録です。

- **状態：全文の読み（RULES §2.2a の段階 C：対照 0/1000、独立の2回目 90.7%、値の付いた割合 99.5%、較正 記号 91.3%・文字 93.6%）。** f. 50r・v の暗号32行を通して読んだ。値の分からない記号・語が9か所ある（[docs/OPEN.md](docs/OPEN.md)）。
- **先行との関係：** 友清理士氏は、同じ暗号の書簡のうち f. 50 だけを「undeciphered」としている（[Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)）。NoAutopilot/cipher-lab に、f. 50 を同じ表で部分的に読んだ下書きがある（2026-10-13 の版、「Status: partial」、630記号中451に値）。その下書きにすでに出ている語（「conseil」「que ledit」「descouvert」「surtou[t]」など、reading.txt の f50r L01・L09、f50v L09・L10）は、この読みでは **再現（reproduced）** である。こちらで加えたのは、通した読み・鍵の補い・語の符号の確かめ・内容（下の「この読みで加えたこと」）。先行の判定（[docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)、2026-10-20）では、この書簡の平文は刊本・論文・リポジトリに見つからなかった（区分「見つからない」。Google Books・Gallica・HathiTrust の全文検索と刊本は調べられていない）。判定は解いたのと同じセッションが行ったので、独立した確かめではない。「初めて」とは書かない。
- **人は書き起こしを確かめていません。** 書き起こしは AI（Claude）が作り、別の AI（OpenAI Codex）が画像だけから独立に作った5回の書き起こしと照らして直しました。AI どうしの一致は、人による確認の代わりにはなりません。
- **数字：**
  - 独立の2回目：書き起こしを最後に直した後、Codex に新しく1回読ませた。626記号のうち同じ名前 568（90.7%）、鍵で同じ値になる名前を同じとみなすと 590（94.2%）（[second/INDEPENDENT.md](second/INDEPENDENT.md)）。この比較では書き起こしを直していない。
  - 照合の記録（直すのに使った比較）：Codex 5回。照合前の書き起こしとの一致は Codex 1〜3回目で 565・554・559／633（[second/RESULT.md](second/RESULT.md)）、最終の書き起こしとの投票は5回とも同じ 572、多数が一致 604（[second/VOTE.md](second/VOTE.md)）。
  - 対照：鍵の値をかき混ぜた鍵1000通りで、本物以上は0回。表の記号だけ、f. 50 の文脈から推定した値を外した鍵、最後の5分の1だけ、Codex の5つの書き起こし、のどれでも0回（[controls/results.txt](controls/results.txt)）。
  - 値の付いた割合：書き起こしの暗号の記号620のうち、鍵の値か意味の分かる語の符号があるもの 617（99.5%）、f. 50 の文脈から推定した値を除くと 613（98.9%）。値のないのは r06 の 23̂、r10 の綴じ目で切れた記号、v05 の =18（`src/valued.py`）。値があっても文脈で読めない記号は [docs/OPEN.md](docs/OPEN.md)。
  - 較正：当時の解読文がある f. 171r の13行を、答えを見ずに同じ鍵で読むと、記号ごとの精度 0.913（253/277。主な値だけなら 0.874。読みを固定した時点の鍵では 0.924）、読みの文字の一致 93.6%（337/360）（[calib/RESULT.md](calib/RESULT.md)）。
  - 数字の出どころは [NUMBERS.md](NUMBERS.md)。
- **手で確かめる：** [docs/index.html](docs/index.html) に、行ごとの画像（BnF の IIIF から読み込む）と、記号名・値を並べた。
- **AI の使用：** 書き起こし・鍵の補い・解読・スクリプト・文書は Anthropic の Claude（Claude Code、Claude Opus 5.5）。2回目の書き起こしは OpenAI の Codex。対象の選定、作業の指示、公開の判断は人。

## 更新履歴
- 2026-10-20：最初の版を作った。同じ日の公開前の点検で、次を直した。
  - 鍵：y の主な値を n から g に（友清氏の表どおり）。mz を、尾に横線のある mz（s）と横線のない mi（i）に分けた（f. 50 の11か所を mi に）。横線つきの曲がった x（xx＝c）を分けた。
  - 兄弟書簡 f. 230r（1〜21行）を、形を分けて書き起こし直し（`data/f230r_tx.txt`）、当時の解読文と機械的に対応させた（`src/align_sister.py`）。記号の当てはまりは 406/424（直す前の鍵）→ 412/424（直した後の鍵）。ff＝d、小さな o＝z、ℓ＝x、小さな ʒ＝s、=83＝le Gouverneur を足した。
  - 2026-10-20（同日、ルールの追加に合わせて）：書き起こしの修正をすべて画像で見直した（`second/CORRECTIONS.md`）。σ に直した10か所のうち8つを 6 に戻した。書き起こしを最後に直した後で、Codex にもう1回読ませた（独立の2回目、`second/INDEPENDENT.md`）。
  - 対照の本物の値：−3.458 → −3.446 → −3.286 → −3.302（どれも 0/1000）。較正の記号ごとの精度：0.924 → 0.913（較正用の f. 171r の書き起こしは mz と mi を分ける前に固定したため。下の「数字」）。

## 内容（要約）
- バルセロナの参事たちは Marca の宿を用意するにあたり、La Motte 元帥の友人の家を選んだ。その友人は、Marca の言動や宮廷との書簡の中身を逐一知るつもりでいる。Marca は用心し、言いくるめられないように。
- 宮廷でバルセロナの用を務める者が、カタルーニャ人から自分に宛てた包みが開けられていると何度も訴えている。王妃は Marca がこれを見張り、分かったことを知らせることを強く望んでいる。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- 鍵の表：友清理士氏の復元（[louisxiv_0marca1644.png](https://cryptiana.web.fc2.com/code/louisxiv_0marca1644.png)）。表の画像はこのリポジトリに含めていません。
- コマ番号の対応と、f. 190r・f. 205r の当時の解読文の書き起こし：NoAutopilot/cipher-lab。

**この読みで加えたこと**
1. f. 50r・v の記号を、記号名で行ごとに書き起こした（`data/transcription_f50.txt`）。
2. 兄弟書簡 f. 230r の21行を書き起こし、当時の解読文 f. 232r と機械的に対応させて、表の値を確かめ、表にない記号の値を足した（`data/f230r_tx.txt`、`data/f230r_sign_counts.tsv`）。
3. 語の符号 =y（Monsieur le Mareschal）、=3（de La Motte）、=11 =o（la Reyne）を兄弟書簡で確かめた。
4. 書簡の内容。対照・較正・別の AI との照合。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f50.txt               # 鍵の全記号
python3 src/decode.py data/key.tsv data/transcription_f50.txt --table-only  # 友清氏の表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f50.txt 1000         # 対照（wordfreq が必要）
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt           # 較正（読みの文字）
python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt  # 較正（記号ごと）
python3 src/align_sister.py data/key.tsv data/f230r_tx.txt data/f232r_ref_l1-21.txt  # 兄弟書簡との対応
sh controls/run.sh                                                         # 対照をすべて計算し直す
python3 -m unittest discover -s tests
```

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f50.txt | f. 50 の記号名での書き起こし（照合後）。照合前は transcription_f50_before_xcheck.txt |
| data/SIGNS.md | 記号名と形 |
| data/key.tsv | 記号名→値。source 列で出典（友清氏の表・兄弟書簡の照合・推定）を区別 |
| data/decoded_f50.txt | `src/decode.py` の出力 |
| data/f230r_tx.txt、data/f232r_ref_l1-21.txt、data/f230r_aligned.tsv、data/f230r_sign_counts.tsv、data/f232r_decipherment.txt | 兄弟書簡 f. 230r の書き起こし、当時の解読文、記号ごとの対応と数 |
| data/tomokiyo_table_signs.tsv | 友清氏の表の各列にある記号を、記号名で書き写したもの（鍵の T の行の照合に使った） |
| docs/READING.md、READING.en.md | 読み（行ごとの確かさの印つき）と要約 |
| docs/METHOD.md、METHOD.en.md | 方法、数字、先行研究との関係、AI の使用 |
| docs/OPEN.md、OPEN.en.md | 値の分からない記号、確かめていないこと |
| calib/ | 較正（f. 171r／f. 172r） |
| second/ | 2回目の書き起こし：Codex 5回の出力、照合（RESULT.md）と投票（VOTE.md） |
| controls/ | 対照の入力と結果（results.txt）、計算し直すスクリプト（run.sh） |
| docs/index.html | 手で確かめるためのページ（行ごとに Gallica の画像と記号名・値。GitHub Pages 用、まだ有効にしていない） |
| NUMBERS.md | README の数字の出どころ |
| SOURCES.md、SOURCES.en.md | 出典と、先行の確かめ |
