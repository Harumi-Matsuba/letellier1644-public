# Method, figures, AI use and limits

[日本語](METHOD.md)

## Images
- BnF Baluze 103 (Gallica ark:/12148/btv1b9001389d): f. 50r = view 111, f. 50v = view 112, fetched at full size (4864×6996) from the BnF IIIF server (openapi.bnf.fr). The images are not in this repository.
- Sister letters used to check the key: f. 230r (view 486) and its period decipherment f. 232r (view 490). For the code groups: f. 171r (366), f. 189r (402), f. 200r (424), f. 230v (487).

## Key (`data/key.tsv`)
1. Base: Satoshi Tomokiyo's table (Cryptiana, louisxiv0.htm, "Le Tellier-Marca Cipher (1644)"), rewritten with our sign names.
2. 18 lines of f. 230r aligned sign by sign with the period decipherment f. 232r (`data/f230r_pairs.txt`, `data/f232r_decipherment.txt`); this confirmed table values and added signs the table lacks (R = c, ʒc/ʒx = r, ꝺ = r, ℒ = M, Ꝺ = h, k = u). Uncertain pairs carry "?".
3. Code groups: =9 pour, =11 que, =12 qui, =26 vous, =32 Barcelone, 81 faire, 39 Catalogne, =y Monsieur le Mareschal, =3 de La Motte, =11 =o la Reyne, =l =m du Roi. =3 was checked on f. 230r and f. 200r; =11 =o at three places of f. 189r against f. 190r.
4. Column source: T = Tomokiyo's table; S = checked on f. 230r/f. 232r; X = split after the AI cross-check; C = inferred from f. 50 alone.
- We first took 6 to stand for t and l, and y for n and g. The AI cross-check showed that l is a separate σ-shaped sign and n is a y with a bar, as Tomokiyo's table separates them. The f. 230r alignment was made before this split and has not been redone.

## Transcription (`data/transcription_f50.txt`)
- Claude transcribed the full-size line images once, by sign name (`data/transcription_f50_before_xcheck.txt`).
- Second transcription: OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2 bundled with the ChatGPT app, default model) was given only the images and the list of sign names (shape descriptions only; no values, no first transcription, no key, no decipherment) and transcribed the page five times independently: passes 1–3 one image per line (`second/PROMPT.md`), passes 4–5 each line cut into two overlapping halves (`second/PROMPT_halves.md`). No pass ran a command or read a file (execution logs).
- First transcription vs Codex passes 1–3: 565, 554, 559 of 633 signs agree; all three agree on 546. Disagreements were checked on the full-size image; we corrected the σ sign (10 places), the barred y (9), and "2 4" read as one number 24 (2), among others (`second/RESULT.md`).
- Five-pass vote: of the final 626 signs, all five agree on 581, the majority agrees on 613, the majority gives another name on 11, no majority on 2. The 15 majority disagreements before the last revision were checked on the image and 4 corrected (`second/VOTE.md`).
- **Agreement between AIs is not a substitute for checking by a person. No person has checked the transcription.**

## Controls (`src/control.py`, `controls/run.sh` → `controls/results.txt`)
Real key vs 1000 shuffles of its values, scored by French letter-trigram likelihood (built from the top 50,000 French words of wordfreq).

| transcription | key | real | max of shuffles | shuffles ≥ real |
|---|---|---|---|---|
| final (32 lines) | all signs (70) | −3.458 | −4.942 | 0/1000 |
| final | Tomokiyo's table signs only (57) | −3.370 | −4.867 | 0/1000 |
| final | without values inferred from f. 50 (source C only) (65) | −3.421 | −4.726 | 0/1000 |
| last fifth (f. 50v lines 7–12) | all signs | −3.182 | −4.510 | 0/1000 |
| last fifth | without inferred values | −3.182 | −4.545 | 0/1000 |
| Codex passes 1–5 | all signs | −3.682 / −3.670 / −3.619 / −3.647 / −3.627 | −4.934 / −4.880 / −4.873 / −4.890 / −4.962 | 0/1000 each |

## Calibration (`calib/`)
Lines 12–24 of f. 171r were read with the same key and the reading frozen (SHA-256 in `calib/hashes_before_answer.txt`) before the period decipherment f. 172r was opened.

| measure | result |
|---|---|
| sign accuracy, main and other values (`src/score_signs.py`) | 0.924 (256/277) |
| sign accuracy, main value only | 0.874 (242/277) |
| letter agreement of our reading (`src/calib.py`) | 93.6% (337/360) |
| letter agreement of the bare key | 84.2% (303/360) |

Only 13 lines; not fully blind (we had earlier read seven lines of f. 172r, the start of the page, in NoAutopilot's transcription, so lines 1–11 were not used). Two findings came after seeing the answer and were not added to the key: an unbarred "12 19" = qu'il, and a 9 with a small g above = Sr.

## Relation to earlier work
- Satoshi Tomokiyo: the table, and the listing of f. 50 as undeciphered.
- NoAutopilot/cipher-lab (`ciphers/baluze103-letellier-marca-1644/`, last commit f3dcded, 13 Oct 2026, Status: partial / Verdict: parked): a partial draft of f. 50 with Tomokiyo's table (451 of 630 signs valued). We used: the Gallica view numbers, the fact that openapi.bnf.fr serves the images, their note that 6 also stands for l on f. 200r, and their transcriptions of the period decipherments f. 190r and f. 205r (for the checks on f. 189r and f. 200r). Our transcription and reading of f. 50, the f. 230 alignment and the calibration were made without their files. Words their draft already shows are reproduced, not new (README).

## AI use
Transcription, key additions, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5). Second transcription: OpenAI Codex. Choice of target, instructions and the decision to publish: a person.
