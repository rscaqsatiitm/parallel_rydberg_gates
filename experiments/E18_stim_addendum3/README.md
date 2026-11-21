# E18. Addendum 3 Stim checks: erasure, correlation-aware decoding, d = 9-11, item-3 additions, pitch 10.0 um

Pre-registered 2026-11-21 before any production run. Task A3-S. Model: E10 (D010) plus D012. Code: e18.py.
All points at m = 1 (p_c = 2.53e-4, 300 K), baseline p = 1e-3 unless stated. Statistics as E10 (>= 100 failures or
>= 1e6 shots, 95 % Wilson intervals, zero failures as upper bound). X = (corr - base) / (indep - base) with conservative
interval bounds, as E10.

**Item 1a (erasure).** corr and indep with flagged failures (D012 items 1-2), eta in {0, 0.5, 0.8, 0.95, 1.0}, decoded
per D012 item 2; base unchanged (no contaminant, nothing heralded). d = 3, 5, 7.
**Item 1b (correlated matching).** corr decoded with PyMatching correlated matching; X_1b uses base and indep decoded
the same way (correlated matching on a DEM without contaminant hyperedges). d = 3, 5, 7.
**Item 2.** base, corr, indep at d = 9, 11.
**Item 3.** corr and indep with (i) f_prev added, (ii) non-resonant factor applied, (iii) both; d = 5, 7; values from
the parent (E16) or provisional (D012 item 6), stated in the result.
**Item 4.** corr and indep at pitch (10.0, 12.0) um, d = 3, 5, 7, p = 1e-3 (p = 2e-3 if budget allows).

**Controls (before production).**
C1 eta = 0 equivalence: flagged corr and indep at d = 3 decoded without heralds reproduce E10's corr and indep logical
   rates within the 95 % intervals (1e6 shots). C2 herald marginal: flagged indep at d = 3, m = 100, one round: the fire
   rate of each flag equals that location's marginal f within 4 sigma. C3 erasure decoding, planted and corrupted:
   flagged corr at d = 3, m = 10, eta = 1: decoding with heralds must give fewer failures than without (planted: the
   heralds carry information); with the herald-to-location map shifted by one location (corrupted input) the benefit
   must disappear (failures not below the no-herald value minus 2 sigma). C4 correlated matching: on base (no
   contaminant) d = 5, correlated and standard matching agree within intervals (no correlated contaminant structure to
   exploit; baseline Y errors may give a small gain, reported).
**Expectations.** 1a: X falls with eta because heralded failures cost little; at eta = 1, both corr and indep excess
should drop by an order of magnitude or more, and X may approach 1 if the remaining unheralded part is small. 1b:
correlated matching reduces corr's rate modestly (E10 D1 showed a matching decoder does not use the correlation);
X_1b expected 3-8. 2: X(d = 9, 11) within the d = 7 interval (flat). 4: larger row pitch lowers both excesses; X similar.
**Verdict rules (fixed now).**
V1a "erasure removes the penalty": X(eta = 0.95) upper bound < 2 at both d = 5 and 7; "penalty survives erasure": X
lower bound > 2 at d = 5 and 7 for eta >= 0.8; otherwise "partially reduced".
V1b "decoder recovers": X_1b upper bound < X_E10 lower bound at d = 5 and 7; otherwise "not recovered".
V2 "X flat": X(d = 11) interval overlaps the E10 d = 7 interval [4.2, 9.7]; "grows" if its lower bound > 9.7; "shrinks"
if its upper bound < 4.2. Same statement for d = 9.
Items 3 and 4: no verdict; report shifts of the logical rates and of X relative to E10.

## Result
**Amendment 1 (2026-11-21, before any production run; after exploratory diagnostics, which are disclosed).**
While validating the E18 builder, two exploratory diagnostics (diag_decoder.py -> diag_decoder_output.txt, and an
inline seed scan) showed: (i) E10's corr logical rate, decoded with the corr model's own decomposed DEM, varies by a
factor ~4.6 with the random Pauli table of the correlated events (d = 3: 336-1544 failures per 2e5 shots over 5 table
seeds), whereas decoding the same samples with the indep model's DEM gives 195-231 for all seeds: the physics is stable,
the own-DEM decoder is not. (ii) At the E10 points (m = 1, p = 1e-3, table seed 0), the own-DEM decoder fails 2.1-3.5x more
often than the indep-DEM decoder on the same corr samples (d = 3 / 5 / 7: 2379 / 1740 / 543 vs 1112 / 493 / 233 failures in
1.0 / 1.5 / 3.0 e6 shots). E10's X (6.3-9.8 at m = 1) is therefore largely a decoder artefact. Changes, fixed now:
(a) Every E18 corr point is decoded three ways and all are reported: "own" (E10 convention), "marg" (decoder built from
the indep model's DEM, i.e. correct per-pair marginals without hyperedges), "cm" (own DEM with PyMatching correlated
matching, item 1b; undecomposable hyperedges split greedily, undetectable components folded, e18.clean_for_correlations).
The best decoder per point is the primary result: X_best = (corr_best - base) / (indep - base).
(b) Item 1b's verdict V1b is evaluated with X_best against E10's X.
(c) Re-decoding E10 (item 1b) is run as production: d = 3, 5, 7, p = 1e-3 and 2e-3, m = 1, fresh seeds.
(d) Erasure (1a): the decoder prior for both models is built from the indep DEM at strength m (1 - eta).
(e) Statistics: per-shot herald decoding is slow; at d = 7 erasure points stop at >= 1e6 shots if 100 failures are not
reached (allowed by the E10 rule), reported as such.
(appended 2026-11-21; results.json, run_log.txt, analysis.json / analysis_output.txt (analyse.py), controls.json /
controls_output.txt, diag_decoder_output.txt)

**Controls.** C1 PASS (flagged vs E10 circuits, same decoder: corr 1087 vs 1121, indep 725 vs 720 failures in 1e6).
C2 PASS (flag fire rate vs marginal, max |z| 2.4). C3 PASS (corr d = 3, m = 10: no herald 2030, heralds 516, heralds with
the location map shifted by one 10658 failures in 3e5: caught). C4: base d = 5, standard 140 vs correlated matching 128
in 2e6 (agree within intervals).

**Item 1b and the decoder artefact (the main result of E18; it weakens E10 / paper Table IV).** Same corr samples,
three decoders (amendment 1); base and indep from E10. X with conservative 95 % bounds:
| p | d | X own DEM (E10 convention) | X marg (indep-model DEM) | X cm (correlated matching) | best |
|---|---|---|---|---|---|
| 1e-3 | 3 | 20.8 [14.6, 34.7] | 2.49 [1.51, 4.67] | 23.7 [16.6, 39.3] | marg |
| 1e-3 | 5 | 8.45 [5.90, 13.2] | 2.22 [1.39, 3.80] | 6.02 [4.13, 9.57] | marg |
| 1e-3 | 7 | 6.80 [4.64, 10.4] | 3.29 [2.08, 5.36] | 4.33 [2.83, 6.84] | marg |
| 2e-3 | 3 | 18.7 [13.2, 30.3] | 1.53 [0.86, 2.99] | 21.2 [15.1, 34.4] | marg |
| 2e-3 | 5 | 4.42 [3.13, 6.78] | 1.63 [1.03, 2.74] | 3.38 [2.34, 5.27] | marg |
| 2e-3 | 7 | 4.29 [2.41, 10.2] | 2.52 [1.29, 6.35] | 1.87 [0.88, 4.95] | cm |
The own-DEM decoder used in E10 is the worst of the three: stim's decomposition of the correlated events into graphlike
pieces mis-weights the matching graph, and its result depends on the arbitrary Pauli table (d = 3 own: 1.86e-3 here
vs 2.36e-3 in E10 with a different table; marg is table-independent, diagnostic). With the best decoder found the
correlated floor costs X = 1.5-3.3 (point estimates) times an independent error of the same marginal, not 6-10.
PyMatching correlated matching (the decoder given the hyperedge model) does not beat the marginal decoder except at
p = 2e-3, d = 7, and is far worse at d = 3. **V1b (pre-registered, X_best upper bound below the E10 X lower bound):
satisfied at d = 5 (3.80 < 6.8), not at d = 7 (5.36 > 4.2): formally "not recovered" at d = 7**, although every point
estimate falls by 2-3x.

**Item 2 (d = 9, 11; m = 1, p = 1e-3; X with the marg decoder).**
| d | base (per round) | indep | corr marg | X_best | X own |
|---|---|---|---|---|---|
| 7 | 9.3e-7 (E10) | 4.73e-6 (E10) | 1.35e-5 [1.12, 1.62] | 3.29 [2.08, 5.36] | 6.80 |
| 9 | 6.56e-8 [5.08, 8.46] (59 fails / 1e8) | 6.65e-7 [5.49, 8.07] (103 / 1.7e7) | 1.70e-6 [1.41, 2.05] (110 / 7.2e6) | 2.72 [1.75, 4.30] | 6.8 |
| 11 | 6.1e-9 [1.7e-9, 2.2e-8] (2 / 3e7) | 7.42e-8 [6.09, 9.05] (98 / 1.2e8) | 2.30e-7 [1.89, 2.79] (101 / 4e7) | 3.28 [1.88, 7.14] | 7.7 |
Base at d = 9 (59 failures) and d = 11 (2 failures, cap cut to 3e7) and indep at d = 11 (98) are below 100 failures; their
Wilson intervals are used in the conservative X bounds. **V2: X flat.** X(d = 11) overlaps the pre-registered E10 d = 7
interval [4.2, 9.7] and the E18 d = 7 interval; X(d = 9) likewise. No growth with distance up to d = 11 under either decoder.
Suppression per d + 2 (marg): 7.9 (7 -> 9), 7.4 (9 -> 11); indep 7.1, 9.0; base 14, 11.

**Item 4 (row pitch 10.0 um; base from E10).** corr marg 3.07e-4 / 4.38e-5 / 6.74e-6 and indep 2.29e-4 / 2.95e-5 / 3.30e-6 per
round at d = 3 / 5 / 7 (pitch 8.571: 3.55e-4 / 6.37e-5 / 1.35e-5 and 2.32e-4 / 3.56e-5 / 4.73e-6). X marg 2.00 [1.16, 3.88],
1.85 [1.01, 3.72], 2.46 [1.45, 4.39]; X own 19.3, 6.13, 4.57. The contaminant excess at d = 7 (marg) falls from 1.26e-5 to
5.8e-6 per round (2.2x) for the 17 % larger row pitch. p = 2e-3 not run (budget).

**Item 1a (erasure at the end of each round; marg-type prior, per-shot herald reweighting).** X(eta), d = 3 / 5 / 7:
| eta | d = 3 | d = 5 | d = 7 |
|---|---|---|---|
| 0 | 3.44 [1.44, 14.0] | 1.80 [1.17, 2.88] | 2.63 [1.43, 5.09] |
| 0.5 | 3.01 [0.74, inf] | 1.44 [0.70, 3.23] | 1.63 [0.58, 5.18] |
| 0.8 | 2.62 [0.28, inf] | 0.85 [0.12, 4.53] | 1.22 [0.13, 20.8] |
| 0.95 | 3.25 [-0.07, inf] | 0.62 [-0.06, 5.93] | 1.00 [-0.07, inf] |
| 1.0 | 3.12 [-0.10, inf] | 0.48 [-0.16, 7.83] | 0.52 [-0.20, inf] |
Absolute (d = 7, per round): corr 1.23e-5 (eta 0), 2.26e-6 (0.8), 1.31e-6 (1.0) against base 9.3e-7 and indep 5.2e-6, 2.0e-6,
1.7e-6: heralding at eta >= 0.8 removes ~85-97 % of the contaminant excess of both models, after which corr and indep are
indistinguishable at these statistics (d = 7 points: 11-103 failures in 1.2e6 shots, allowed by the >= 1e6-shot rule; d = 3
points stopped at >= 100 failures, 1.8-2.4e5 shots). **V1a: formally "partially reduced"** (neither pre-registered
condition met: the X(0.95) upper bounds are not < 2, and the lower bounds are not > 2); the point estimates at d = 5, 7 are
consistent with no correlation penalty once losses are heralded with eta >= 0.8.

**Item 3 (final inputs from E16: f_prev = 3.2e-5 per pair per layer (upper end; 2.0e-5 low end not run, budget);
non-resonant factor 1.0003, i.e. negligible; only the combined variant was run).** d = 5: corr marg 6.50e-5, indep 3.55e-5,
X 2.29 [1.46, 3.81]; d = 7: 1.15e-5, 5.49e-6, X 2.31 [1.56, 3.51]. Compared with item 1b (no additions; 6.37e-5, 1.35e-5) the
corr rates do not change measurably (intervals overlap), and X stays in the same range. Earlier-layer contaminants at
400 us and the non-resonant channels do not move the logical results.

**Expectations vs outcome.** 1a: correct (X falls with eta; excess largely removed). 1b: wrong in kind: the E10 decoder was
the problem, not a missing correlation-aware decoder; correlated matching did not help. 2: correct (flat). 4: correct.
**Cut or not done:** correlated matching at d >= 9 (slow, and worse than marg at d = 11 in the pilot: 18 vs 1 failures in
3e5); base d = 11 capped at 3e7 shots (2 failures); f_prev low end and the separate f_prev-only / nonres-only variants;
pitch 10.0 at p = 2e-3; a BP+OSD or tensor-network decoder (not installed). The erasure decoder's prior for multi-pair
events is approximate (D012 item 2).
