# Where the numbers come from / 数字の出どころ

Every number in README.md, README.en.md and docs/METHOD*.md, and where it is computed. Recompute with the command shown.
README・METHOD の数字ごとに、出どころと計算し直す方法を示す。

| number | meaning | source / command |
|---|---|---|
| 32 lines (20 + 12) | cipher lines of f. 50r–v | `data/transcription_f50.txt` (ids r01–r20, v01–v12) |
| 626 signs | signs of the final transcription | `python3 src/vote.py data/transcription_f50.txt second/codex_pass*.txt` (stderr: `signs 626`) |
| 581 / 613 / 11 / 2 | five passes all agree / majority agrees / majority differs / no majority | the same command (`all_agree`, `majority_agrees`, `majority_differs`, `no_majority`); per sign in `second/vote.tsv` |
| 15 → 4 corrected | majority disagreements before the last revision, and corrections | `second/VOTE.md`; the revision note in `data/transcription_f50.txt` |
| 633; 565 / 554 / 559; 546 | first transcription; agreement with Codex passes 1–3; all three agree | `python3 src/xcompare.py data/transcription_f50_before_xcheck.txt second/codex_pass1.txt second/codex_pass2.txt second/codex_pass3.txt` (stderr) |
| 10, 9, 2 corrections (σ, barred y, 24) | corrections after the first cross-check | `second/RESULT.md` (counted from the MAJ rows of `second/compare.tsv`) |
| −3.458, −4.942, 0/1000 (and the other rows of the control table) | real score, max of 1000 shuffles, shuffles ≥ real | `sh controls/run.sh` → `controls/results.txt` (seed 1) |
| 70 / 57 / 65 signs | signs in the full key / table-only / without inferred values | `table_only=... signs=...` lines of `src/control.py`; `controls/key_without_target.tsv` |
| f. 50v lines 7–12 | the last fifth (6 of 32 lines) | `controls/heldout_last_fifth.txt` |
| 0.924 (256/277), 0.874 (242/277) | sign accuracy on f. 171r lines 12–24 | `python3 src/score_signs.py data/key.tsv calib/f171r_tx.txt calib/f172r_ref.txt [--strict]` → `calib/signs_score*.txt` |
| 93.6% (337/360), 84.2% (303/360) | letter agreement of the reading / of the bare key | `python3 src/calib.py calib/f171r_reading.txt calib/f172r_ref.txt` and `calib/f171r_mech.txt` |
| 13 lines, 360 letters | size of the calibration | `calib/f172r_ref.txt` |
| 10 open items | signs or groups without a value | rows of the table in `docs/OPEN.md` |
| 451 of 630 | NoAutopilot's draft | header of their reading.txt (version f3dcded, 13 Oct 2026; not in this repository) |
| 18 lines | f. 230r aligned with f. 232r | `data/f230r_pairs.txt` (L01–L18) |
| views 111, 112, 366, 368, 486, 490, 402, 424, 487 | Gallica view numbers | `SOURCES.md` |
