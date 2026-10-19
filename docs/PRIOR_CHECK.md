# 「新しい」の判定（RULES §2.2 の5）

[English](PRIOR_CHECK.en.md)

この判定は2つの探索からなる。
1. **別のセッションによる反証の探索**（RULES §2.2 の5が求めるもの）：解いたのとは別の会話が、先行を否定するつもりで探した（2026-10-20、作業用の報告 reports/2026-10-20_prior_check_vulcob_letellier_dodieu.md。下の「別のセッションの探索」）。
2. **解いたセッション自身の探索**（ユーザーの指示で、同じ日に先に行った。下の「調べた先」）。独立した確かめではないので、1を補うものとして扱う。

調べた日時：2026-10-20（日本時間）、UTC では 2026-10-19 15時〜17時台。

## 判定
| 対象 | 区分 | 根拠 |
|---|---|---|
| f. 50 の平文（つなげた読み）全体 | **見つからない** | 当時の解読文は同じ巻にない（NoAutopilot の記録：f. 49v・f. 51・f. 52 は宛名と貼り紙だけ。こちらでは見ていない）。刊本・論文・リポジトリにも、この書簡の平文は見つからなかった（下の表） |
| 一部の語（conseil、que ledit、descouvert、surtou[t] など） | **既に読まれている（部分的）** | NoAutopilot/cipher-lab の reading.txt（コミット f3dcded、2026-10-13）に、友清氏の表を当てた文字列として出ている。通った文にはなっていない（同 NOTES.md の「Status: partial」「Verdict: parked」） |
| 平文はあるが対応はない | 該当なし | この書簡の平文は見つかっていない |

見つからないことは、読まれていないことの証明にはならない。README では「初めて」とは書かない。

## 別のセッションの探索（2026-10-20）
| 先 | 結果 |
|---|---|
| DECODE R2742（記録の公開ページ） | 「Status: Decrypted」「Inline Plaintext: No」「Available Documents: Key, Paper」、作成者 tomokiyo。文書はログインが要る。NoAutopilot はログインして、画像と友清氏の表だけと記録している（2026-10-05） |
| NoAutopilot/cipher-lab の baluze103-letellier-marca-1644 | 最後のコミット f3dcded（2026-10-13 07:56 UTC）、Verdict: parked。それより後のコミットはない |
| GitHub コード検索「"Baluze 103"」（18件） | すべて NoAutopilot のファイル |
| Cyphersolver（origin/main 0258b8ab）の全文検索、issue・PR 全47件（最新 #49） | f. 50 の読みはない |
| Cryptiana（unsolved.htm 2026-10-13、GL.htm 2026-10-15、ai.htm 2026-10-19、verification.htm 2026-10-15） | f. 50 の記述は louisxiv0.htm の « undeciphered » だけ |
| Cryptoole API（854件） | 項目なし |
| DECODE の目録の写し（aaymeloglu/unsolved-ciphers、c2436b0、2026-09-18、10,106件） | R2742 のほかに該当なし |
| BravoBravoIX（6リポジトリ）、pangoleen/cipher-readings、el-descifrador/cabinet-noir | ファイル名に Baluze・Marca・Tellier なし |
| ウェブ検索（仏）「conseillers de la ville de Barcelone」・Marca・La Motte | 該当なし |
| 調べられなかった先 | Gallica・Google Books・HathiTrust の全文検索（その時点）、DECODE の文書、Sanabre など西語の刊本 |

## 解いたセッションの探索：調べた先
| 先 | 調べ方 | 結果 |
|---|---|---|
| ウェブ検索（仏・西・英、5回） | 「"Le Tellier" Marca 1644 lettre "La Motte" Barcelone conseillers logis」、「Marca visitador general Cataluña 1644 casa amigo mariscal La Motte consellers Barcelona alojamiento cartas abiertas」、「Pierre de Marca 1644 Barcelona letters opened "La Mothe" Le Tellier cipher」、Torreilles・Sanabre・Aznar の名で各1回 | この書簡の内容（宿、包みが開けられる件）に触れたものはない |
| T. Issartel「Pierre de Marca (1594-1662), l'absolutisme et la frontière」（ddd.uab.cat、2010） | PDF を取得して全文を検索 | Marca の訪問官としての経緯と、Le Tellier との往復の研究（Dubarat 1901・1927–28、Torreilles 1901、Sanabre 1956）を挙げるが、f. 50 の内容はない |
| HistoCrypt の論文（ecp.ep.liu.se、検索で出たもの） | PDF を取得 | ブラジルのポルトガル人スパイ（1646）の論文で、関係ない |
| GitHub コード検索 | 「"paquets que les Catalans"」「"conseillers de la ville de Barcelonne"」「Marca "La Motte" "Le Tellier" 1644」「baluze103 letellier marca」 | 前の2つは 0件。3つ目は関係のない文章のデータだけ。4つ目は NoAutopilot/cipher-lab だけ |
| NoAutopilot/cipher-lab | `ciphers/baluze103-letellier-marca-1644/` の最後のコミットと reading.txt | 最後のコミットは f3dcded（2026-10-13）のまま。reading.txt に paquet・catalan・motte・maison の語はない |
| D. Bourdeau, cyphersolver | ledger を fetch、origin/main 0258b8ab（2026-10-18）を全文検索、issue の最新5件（#45〜#49） | 該当なし |
| Cryptiana | louisxiv0.htm（2025-12-06）、unsolved.htm（2026-10-13） | louisxiv0.htm で « f.50 (undeciphered) » のまま |
| Cryptoole | 同日の先行調査（idx.json、854件） | 該当なし |
| HathiTrust の全文検索（語句検索、全件） | ユーザーが Chrome で確認を押したあと、同じタブから4秒間隔で12語句：「paquets que les Catalans」「ouvre tous les paquets」「conseillers de la ville de Barcelonne」「conseillers de la ville de Barcelone」「maison d'un amy de M. le Mareschal」「amy de M. le Mareschal de la Motte」「Marca ait l'oeil」「desire passionnement que M. Marca」「ponctuellement de tout ce que ledit sieur Marca」「preparer un logis」「Le Tellier a Marca」「paquets qui sont envoyes de la ville de Barcelone」 | f. 50 に固有の語句7つは0件。「conseillers de la ville de Barcelonne」の当たりは Sourdis の書簡集と、1641年の条約の文面（Collection de documents inédits、uc1.c2811166 の p. 492・564 を見た）で関係ない。一般的な語句（ouvre tous les paquets、preparer un logis、Le Tellier a Marca）は関係のない本が多数（題名を見ただけで、中身は見ていない）。f. 189 の当時の解読文の語句（paquets qui sont envoyes…）も0件で、兄弟書簡の平文も刊本には見当たらない |

## 解いたセッションの探索：調べられなかった先
| 先 | 理由 |
|---|---|
| Google Books の全文検索（API） | 7回とも 429（アクセス制限）。そこで止めた |
| Gallica の全文検索（SRU） | curl は 403。Chrome でもセキュリティ検証の画面が出た。2回目（ユーザーが HathiTrust の確認を押した後）も Gallica は検証の画面のままで、押さずに止めた |
| DECODE（de-crypt.org）R2742 | ログインが要る。NoAutopilot は「画像と友清氏の表だけ」と記録 |
| 刊本：Sanabre『La acción de Francia en Cataluña』（1956）、Dubarat「Marca (1644-1651) et sa famille en Catalogne」（1927–28）、Torreilles（Revue des Questions historiques, 1901）、Chéruel 編 Mazarin 書簡集 | 全文を読めていない（Chéruel 第1巻は NoAutopilot が「Marca」で全文を検索し、この書簡はないと記録） |
| Persée・Cairn・Dialnet | 個別には検索していない（ウェブ検索の範囲だけ） |
