# 出典

## 一次資料（リポジトリには含めていない）
- **BnF, Baluze 103**（Affaires de Catalogne — Correspondance de Marca）、Gallica ark:/12148/btv1b9001389d
  - 111コマ：f. 50r（暗号20行）。https://gallica.bnf.fr/ark:/12148/btv1b9001389d/f111.item
  - 112コマ：f. 50v（暗号12行）
  - 366・368コマ：f. 171r（暗号）と f. 172r（当時の解読文）。較正に使った
  - 486・490コマ：f. 230r（暗号）と f. 232r（当時の解読文）。鍵の確かめに使った
  - 402・424・487コマ：f. 189r、f. 200r、f. 230v。語の符号の確かめに使った

画像は再配布していません。コマ番号で参照してください。Source gallica.bnf.fr / BnF.

## 鍵
- 友清理士（Satoshi Tomokiyo）, Cryptiana, code/louisxiv0.htm「Le Tellier-Marca Cipher (1644)」（Last-Modified 2025-12-06）。« Le Tellier's letters use the following cipher in April to October 1644 (f.50 (undeciphered), f.171, f.189, f.200, f.230 (deciphered on separate pages)) »。表の画像 louisxiv_0marca1644.png は含めていない。`data/key.tsv` の source に T を含む値は、この表を記号名に置き換えたもの。

## 照らした研究
- NoAutopilot/cipher-lab, `ciphers/baluze103-letellier-marca-1644/`（https://github.com/NoAutopilot/cipher-lab 、最後のコミット f3dcded6、2026-10-13）。NOTES.md（コマ番号の対応、openapi.bnf.fr の IIIF、f. 200r の照合の記録）、b189/f190r_decipherment.txt、b200/f205r_decipherment.txt（当時の解読文の書き起こし）を読んで使った。ファイルはこのリポジトリに含めていない。

## 先行の確かめ（2026-10-20）
見つからないことは、手を付けた人がいないことの証明にはなりません。

| 調べた先 | 結果 |
|---|---|
| GitHub コード検索「Baluze 103 f.50」「"Baluze 103"」 | NoAutopilot/cipher-lab だけ（上記、部分的な下書き） |
| GitHub リポジトリ・issue 検索（Marca、Tellier、Baluze の組み合わせ） | 関係するものなし |
| D. Bourdeau, cyphersolver（origin/main 0258b8ab、2026-10-18。全文検索と issue 100件） | 該当なし |
| Cryptiana（louisxiv0.htm 2025-12-06、unsolved.htm 2026-10-13、GL.htm 2026-10-15） | louisxiv0.htm で « undeciphered »。ほかに言及なし |
| Cryptoole（idx.json、854件） | 該当なし |
| BravoBravoIX の公開リポジトリ8件（ファイル名） | 該当なし |
| ウェブ検索（英語1回） | 該当なし |
| DECODE（de-crypt.org）R2742 | ログインが要るため見ていない。NoAutopilot は「画像と友清氏の表だけ」と記録 |
| 刊本（Sanabre ほか） | 見ていない |
