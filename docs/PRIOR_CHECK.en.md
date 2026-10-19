# Is the reading new? (RULES §2.2, item 5)

[日本語](PRIOR_CHECK.md)

**Note: this check was made by the same session that made the reading** (at the user's instruction). It is not the search by a separate session, made in order to refute, that the rules ask for, so it is weak as an independent check.

Date: 20 Oct 2026 (Japan time); 19 Oct 2026, 15:00–17:59 UTC.

## Verdict
| object | class | evidence |
|---|---|---|
| the plaintext of f. 50 as a whole (the joined reading) | **not found** | no period decipherment in the volume (NoAutopilot: f. 49v, f. 51, f. 52 carry only the address and slips; we have not looked at them). No plaintext of this letter found in print, papers or repositories (table below) |
| some words (conseil, que ledit, descouvert, surtou[t] …) | **already read (partly)** | in NoAutopilot/cipher-lab reading.txt (commit f3dcded, 13 Oct 2026) as strings from Tomokiyo's table, not as connected text ("Status: partial", "Verdict: parked") |
| plaintext exists but no alignment | none | no plaintext of this letter has been found |

Not finding a reading does not prove that none exists. The README does not call this reading the first.

## Searched
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

## Not searched or blocked
| where | why |
|---|---|
| Google Books full-text (API) | HTTP 429 on all seven queries; stopped |
| Gallica full-text (SRU) | 403 with curl; a security check page in Chrome; stopped |
| HathiTrust full-text | Cloudflare bot check; not tried |
| DECODE (de-crypt.org) R2742 | login needed; NoAutopilot records "images and Tomokiyo's table only" |
| printed works: Sanabre (1956), Dubarat (1927–28), Torreilles (1901), Chéruel's Mazarin letters | not read in full (NoAutopilot searched Chéruel vol. 1 for "Marca" and found no such letter) |
| Persée, Cairn, Dialnet | not searched separately (only through web search) |
