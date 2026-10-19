# A reading of Le Tellier's cipher letter to Marca (26 April 1644)

[日本語 README](README.md)

A reading of the cipher in BnF Baluze 103 f. 50, a letter from Michel Le Tellier, Secretary of State for War, to Pierre de Marca in Catalonia, using the table of the "Le Tellier-Marca Cipher (1644)" reconstructed by Satoshi Tomokiyo.

- Source: BnF Baluze 103 (Affaires de Catalogne — Correspondance de Marca), Gallica ark:/12148/btv1b9001389d, view 111 (f. 50r, dated in clear "Du 26e avril 1644", 20 cipher lines) and view 112 (f. 50v, 12 cipher lines).
- Prior work: Tomokiyo lists f. 50 as the one "undeciphered" letter in this cipher ([Cryptiana](https://cryptiana.web.fc2.com/code/louisxiv0.htm)). NoAutopilot/cipher-lab has a partial draft reading of f. 50 with the same table (version of 13 Oct 2026, "Status: partial"). How this work relates to it is in [docs/METHOD.md](docs/METHOD.md) (Japanese).

## Status (v0.1)
- All 32 lines of f. 50r–v read as French ([docs/READING.en.md](docs/READING.en.md)). Nine signs or code groups remain unknown ([docs/OPEN.md](docs/OPEN.md), Japanese).
- Shuffled-key control (1000 shuffles): none scored as high as the real key (also with table signs only). The same key applied to three independent transcriptions made by another AI: none in each.
- **Calibration**: 13 lines of f. 171r, which has a period decipherment, read blind with the same key: 93.6% letter agreement (337/360) with the period decipherment; 84.2% from the bare key. Expect errors in detail.
- **The transcription has not been checked by a person.** It was made by an AI (Claude) and corrected against three independent transcriptions by another AI (Codex). Agreement between AIs is not a substitute for human checking.

## Content (gist)
The Barcelona councillors chose, as Marca's lodgings, the house of a friend of Marshal de La Motte, who expected thereby to learn everything Marca does and writes; Marca is warned to be on his guard. Barcelona's agent at Court complains that packets sent to him by the Catalans are being opened; the Queen wishes Marca to watch this, report, and stop it.

## AI use
Transcription, key additions, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5). Cross-check of the transcription: OpenAI Codex. Choice of target, instructions and the decision to publish: a person.

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f50.txt
python3 src/control.py data/key.tsv data/transcription_f50.txt 1000   # needs wordfreq
python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt
python3 -m unittest discover -s tests
```
