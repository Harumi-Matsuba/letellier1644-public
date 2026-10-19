# A reading of Le Tellier's cipher letter to Marca (26 April 1644), v0.1

[日本語 README](README.md)

A reading of the cipher in BnF Baluze 103 f. 50, a letter from Michel Le Tellier, Secretary of State for War, to Pierre de Marca in Catalonia, using the table of the "Le Tellier-Marca Cipher (1644)" reconstructed by Satoshi Tomokiyo.

- Source: BnF Baluze 103 (Affaires de Catalogne — Correspondance de Marca), Gallica ark:/12148/btv1b9001389d, view 111 (f. 50r, dated in clear "Du 26e avril 1644", 20 cipher lines) and view 112 (f. 50v, 12 cipher lines).
- **State: full reading (v0.1).** All 32 cipher lines of f. 50r–v read through; ten signs or code groups have no value ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Relation to earlier work:** Tomokiyo lists f. 50 as the one "undeciphered" letter in this cipher ([Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)). NoAutopilot/cipher-lab has a partial draft of f. 50 with the same table (version of 13 Oct 2026, "Status: partial", 451 of 630 signs valued). Words already in that draft ("conseil", "que ledit", "descouvert", "surtou[t]", among others; reading.txt f50r L01, L09, f50v L09, L10) are **reproduced** here, not new. New: the connected reading, key additions, the checks of the code groups, the content ([docs/METHOD.en.md](docs/METHOD.en.md)).
- **No person has checked the transcription.** It was made by an AI (Claude) and corrected against five transcriptions made independently from the images by another AI (OpenAI Codex). Agreement between AIs is not a substitute for human checking.
- **Figures:**
  - Second transcription: five Codex passes; of the final 626 signs, all five agree on 581, the majority agrees on 613 ([second/VOTE.md](second/VOTE.md)).
  - Controls: 0 of 1000 shuffled keys score as high as the real key; also with Tomokiyo's table signs only, without the values inferred from f. 50, on the last fifth alone, and on each of the five Codex transcriptions ([controls/results.txt](controls/results.txt)).
  - Calibration: 13 lines of f. 171r, which has a period decipherment, read blind with the same key: sign accuracy 0.924 (256/277; 0.874 with main values only), letter agreement 93.6% (337/360) ([calib/RESULT.md](calib/RESULT.md)).
  - Where each number comes from: [NUMBERS.md](NUMBERS.md).
- **AI use:** transcription, key additions, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5). Second transcription: OpenAI Codex. Choice of target, instructions and the decision to publish: a person.
- **Check by hand:** [docs/index.html](docs/index.html) shows each line's image (from the BnF IIIF server) with our sign names and values.

(v0.1 is the first version; changes will be listed here.)

## Content (gist)
The Barcelona councillors chose, as Marca's lodgings, the house of a friend of Marshal de La Motte, who expected thereby to learn everything Marca does and writes; Marca is warned to be on his guard. Barcelona's agent at Court complains that packets sent to him by the Catalans are being opened; the Queen wishes Marca to watch this, report, and stop it.

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f50.txt
python3 src/control.py data/key.tsv data/transcription_f50.txt 1000   # needs wordfreq
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt
python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt
sh controls/run.sh
python3 -m unittest discover -s tests
```
