# Is the reading new? (RULES §2.2, item 5)

[日本語](PRIOR_CHECK.md)

This check has two parts.
1. **A search by a separate session, made in order to refute** (what RULES §2.2 item 5 asks for): another conversation, not the one that made the reading, looked for earlier work (20 Oct 2026; working report reports/2026-10-20_prior_check_vulcob_letellier_dodieu.md; "Separate session" below).
2. **The solving session's own search** (made earlier the same day at the user's instruction; "Searched" below). It is not independent and only supplements part 1.

Date: 20 Oct 2026 (Japan time); 19 Oct 2026, 15:00–17:59 UTC.

## Verdict
| object | class | evidence |
|---|---|---|
| the plaintext of f. 50 as a whole (the joined reading) | **not found** | no period decipherment in the volume (NoAutopilot: f. 49v, f. 51, f. 52 carry only the address and slips; we have not looked at them). No plaintext of this letter found in print, papers or repositories (table below) |
| some words (conseil, que ledit, descouvert, surtou[t] …) | **already read (partly)** | in NoAutopilot/cipher-lab reading.txt (commit f3dcded, 13 Oct 2026) as strings from Tomokiyo's table, not as connected text ("Status: partial", "Verdict: parked") |
| plaintext exists but no alignment | none | no plaintext of this letter has been found |

Not finding a reading does not prove that none exists. The README does not call this reading the first.

## Separate session (20 Oct 2026)
| where | result |
|---|---|
| DECODE R2742 (public record page) | "Status: Decrypted", "Inline Plaintext: No", "Available Documents: Key, Paper", by tomokiyo; documents need a login; NoAutopilot logged in and records only the images and Tomokiyo's table (5 Oct 2026) |
| NoAutopilot/cipher-lab baluze103-letellier-marca-1644 | last commit f3dcded (13 Oct 2026 07:56 UTC), Verdict: parked; no later commit |
| GitHub code search "\"Baluze 103\"" (18 hits) | all NoAutopilot files |
| cyphersolver (origin/main 0258b8ab) full text; all 47 issues and PRs (latest #49) | no reading of f. 50 |
| Cryptiana (unsolved 2026-10-13, GL 2026-10-15, ai 2026-10-19, verification 2026-10-15) | only louisxiv0.htm's « undeciphered » |
| Cryptoole API (854 entries) | nothing |
| DECODE catalogue copy (aaymeloglu/unsolved-ciphers, c2436b0, 18 Sep 2026, 10,106 records) | nothing beyond R2742 |
| BravoBravoIX (6 repositories), pangoleen/cipher-readings, el-descifrador/cabinet-noir | no file names with Baluze, Marca, Tellier |
| web search (French): "conseillers de la ville de Barcelone", Marca, La Motte | nothing |
| not searched | Gallica, Google Books, HathiTrust full text (at that time); DECODE documents; Spanish printed works such as Sanabre |

## Solving session: searched
| where | how | result |
|---|---|---|
| web search (French, Spanish, English; 5 queries) | the letter's subjects (lodging, opened packets) with Le Tellier, Marca, La Motte, Barcelona, 1644; and the names Torreilles, Sanabre, Aznar | nothing on this letter's content |
| T. Issartel, "Pierre de Marca (1594-1662), l'absolutisme et la frontière" (ddd.uab.cat, 2010) | full text of the PDF | cites the studies of the Le Tellier–Marca correspondence (Dubarat 1901, 1927–28; Torreilles 1901; Sanabre 1956); nothing on f. 50 |
| a HistoCrypt paper found by the search (ecp.ep.liu.se) | PDF | about a Portuguese spy in Dutch Brazil (1646); unrelated |
| GitHub code search | "\"paquets que les Catalans\"", "\"conseillers de la ville de Barcelonne\"", "Marca \"La Motte\" \"Le Tellier\" 1644", "baluze103 letellier marca" | 0, 0, unrelated text data, only NoAutopilot/cipher-lab |
| NoAutopilot/cipher-lab | last commit of the folder and reading.txt | still f3dcded (13 Oct 2026); reading.txt has none of the words paquet, catalan, motte, maison |
| D. Bourdeau, cyphersolver | origin/main 0258b8ab (18 Oct 2026), full-text search; latest issues #45–#49 | nothing |
| Cryptiana | louisxiv0.htm (2025-12-06), unsolved.htm (2026-10-13) | louisxiv0.htm still says « f.50 (undeciphered) » |
| Cryptoole | same-day search (idx.json, 854 entries) | nothing |
| HathiTrust full-text (phrase search, all items) | after the user passed the check in Chrome, 12 phrases from the same tab, 4 s apart (the letter's own phrases; general ones such as "ouvre tous les paquets", "preparer un logis", "Le Tellier a Marca"; and a phrase of the f. 189 period decipherment) | the seven phrases specific to f. 50: 0 hits. "conseillers de la ville de Barcelonne" hits Sourdis's correspondence and the 1641 treaty text (Collection de documents inédits, uc1.c2811166, pp. 492, 564 seen): unrelated. General phrases: many unrelated books (titles only). The f. 189 phrase: 0, so the sister letters' plaintext is not in print either, as far as this search goes |

## Solving session: not searched or blocked
| where | why |
|---|---|
| Google Books full-text (API) | HTTP 429 on all seven queries; stopped |
| Gallica full-text (SRU) | 403 with curl; a security check page in Chrome, twice (also after the user passed the HathiTrust check); not pressed, stopped |
| DECODE (de-crypt.org) R2742 | login needed; NoAutopilot records "images and Tomokiyo's table only" |
| printed works: Sanabre (1956), Dubarat (1927–28), Torreilles (1901), Chéruel's Mazarin letters | not read in full (NoAutopilot searched Chéruel vol. 1 for "Marca" and found no such letter) |
| Persée, Cairn, Dialnet | not searched separately (only through web search) |
