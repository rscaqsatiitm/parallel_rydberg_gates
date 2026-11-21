# E10. Circuit-level cost of correlated same-layer contaminant errors (Stim)

Pre-registered 2026-11-21 before the production run. Task S4. Model and choices: D010; code: model.py, sim.py.
Disclosure: a timing pilot (20 000 shots per point, p = 1e-3, m = 10, d = 3, 5, 7) was run before this text was
written. Failures seen (base / corr / indep): d = 3: 10 / 370 / 103; d = 5: 1 / 480 / 146; d = 7: 0 / 313 / 135.
These pilot numbers are not results and are not reused.

**Question.** Does a same-layer contaminant error (one contaminant fails several neighbouring pairs of the same CZ
layer) cost more logically than independent pair failures with the same marginal rate per CZ?

**Design.** Rotated surface-code memory, rounds = d, d in {3, 5, 7}; baseline p in {1e-3, 2e-3} (unsourced);
contaminant multiplier m in {1, 3, 10}; models base (no contaminant), corr, indep (D010). Logical error per round
p_L = 1 - (1 - P_fail)^(1/d). Shots per point: batches of 2e5 until >= 100 failures, at least 1e6 shots, at most
2e7 shots; 95 % Wilson interval; zero failures reported as an upper bound.
Derived quantity: excess ratio X = (p_L,corr - p_L,base) / (p_L,indep - p_L,base), the logical cost of the
contaminant term relative to an independent term with the same marginal.
Sensitivity variants (d = 5 and 7, p = 1e-3, m = 10 only): V1 independent random Pauli strings per pair inside an
event (instead of XOR-coupled), V2 E_same map with B along x, V3 cluster threshold 0.2 instead of 0.05 (more of the
correlation dropped into the independent tail). Diagnostic D1: corr samples decoded with the indep error model.

**Controls (run first; production proceeds only if C1-C4 pass).**
C1 planted zero: with E_same scaled by 0, the corr and indep detector error models equal the base model exactly.
C2 marginal: single-layer noise-only circuit (d = 7 layer 1, m = 100 to make f ~ 0.05), reset in Z, noise, measure Z:
   per-qubit flip rate equals f_j / 2 for corr and indep within 4 sigma (2e6 shots); corr shows positive excess joint
   flip rate between cluster neighbours, indep shows none (within 4 sigma).
C3 corrupted input caught: corr with E_same doubled (scale 2) must FAIL the C2 marginal test.
C4 null: pitch x 10 (contaminant marginals < 1e-8): corr and indep logical rates at d = 3, p = 1e-3, m = 10 agree with
   base within the 95 % intervals (1e6 shots each).

**Expectation.** One contaminant fails a cluster of up to 4 pairs (8 qubits) in one step, so a single fault can
produce an error that the independent model needs two or more faults to produce; corr should then have a smaller
effective distance: X > 1 and X increasing with d, most visible at m = 10, possibly unresolved at m = 1 against the
baseline.

**Verdict rule (fixed now).** "Correlation matters" if, at m = 1 and p = 1e-3, p_L,corr exceeds p_L,indep with
non-overlapping 95 % intervals at both d = 5 and d = 7. "Correlation matters at elevated strength" if the same holds at
m = 3 or m = 10. "Distance penalty" if X increases monotonically from d = 3 to d = 7 at m = 10 (both p values).
Otherwise: correlation does not measurably change the logical cost in this model, and the marginal rate suffices.

## Result
(appended 2026-11-21; results.json, run_log.txt, analysis_output.txt (analyse.py), controls.json/controls_output.txt)

**Controls.** C1 PASS (corr and indep detector error models with E_same x 0 identical to base). C2 PASS: per-qubit
flip rates match f/2 for corr and indep (max |z| 2.35, 2.38; mean f = 0.052 at m = 100); joint flip excess between
co-cluster pairs: corr mean z = +90 (max 361), indep mean z = +0.02. C3 PASS (caught: doubled p_c gives max |z| = 251).
C4 PASS (pitch x 10: base / corr / indep failures 461 / 472 / 472 in 1e6 shots, intervals overlap).
Amendments to the control text above, made after a first control run and before any production point: (i) the first
C2 implementation tested ADJACENT pairs; these share no source in this geometry (a source's cluster is its two
x-neighbours, which are second neighbours of each other), so it measured nothing; the test was corrected to pairs
4 coordinate units apart (both x-neighbours of the site between), which is what "cluster neighbours" means.
(ii) C3 "E_same doubled" is impossible (E_same x 2 exceeds 1 near 8 um); implemented as doubled p_c.
Further checks: all corr error-model errors decomposed into graphlike components (0 decomposition failures at
d = 3, 5). One production attempt was killed by the out-of-memory killer at base d = 7 (worker arrays too large); the
sampler was changed to 1e5-shot batches and the run resumed from the stored points (no point recomputed or discarded).

**Results** (logical error per round, 95 % Wilson interval; >= 100 failures or >= 1e6 shots at every point;
X = (corr - base)/(indep - base), conservative bounds):

| p | d | m | base | corr | indep | X |
|---|---|---|---|---|---|---|
| 1e-3 | 3 | 1 | 1.50e-4 | 7.86e-4 [7.55, 8.18] | 2.32e-4 [2.16, 2.50] | 7.8 [5.2, 13.4] |
| 1e-3 | 5 | 1 | 1.26e-5 | 2.37e-4 [2.24, 2.51] | 3.56e-5 [3.07, 4.12] | 9.8 [6.8, 15.3] |
| 1e-3 | 7 | 1 | 9.3e-7 [7.6e-7, 1.13e-6] | 2.47e-5 [2.13, 2.87] | 4.73e-6 [4.01, 5.59] | 6.3 [4.2, 9.7] |
| 1e-3 | 5 | 3 | | 9.02e-4 | 1.28e-4 | 7.7 [6.8, 8.9] |
| 1e-3 | 7 | 3 | | 1.78e-4 | 3.39e-5 | 5.4 [4.4, 6.5] |
| 1e-3 | 3/5/7 | 10 | | 4.24e-3 / 5.65e-3 / 2.61e-3 | 1.84e-3 / 1.50e-3 / 1.02e-3 | 2.4 / 3.8 / 2.6 |
| 2e-3 | 3/5/7 | 1 | 6.0e-4 / 1.02e-4 / 1.83e-5 | 1.51e-3 / 4.51e-4 / 7.17e-5 | 7.65e-4 / 1.71e-4 / 3.27e-5 | 5.6 / 5.1 / 3.7 |
| 2e-3 | 3/5/7 | 10 | | 5.36e-3 / 6.88e-3 / 3.69e-3 | 3.02e-3 / 2.52e-3 / 1.89e-3 | 2.0 / 2.8 / 2.0 |
(Brackets in units of the central value's exponent; full table with all intervals in analysis_output.txt.)

**Verdicts (as pre-registered).**
1. Correlation matters at physical strength (m = 1, p = 1e-3, d = 5 and 7): **YES.** corr exceeds indep by 6.7x
   (d = 5) and 5.2x (d = 7) with non-overlapping intervals; the contaminant's logical cost is X = 6-10 times that of
   independent pair failures with the same marginal rate.
2. Correlation matters at elevated strength (m = 3, 10): **YES** at every d and p.
3. Distance penalty (X increasing monotonically with d at m = 10): **NO** (X = 2.4, 3.8, 2.6 at p = 1e-3; 2.0, 2.8, 2.0
   at p = 2e-3). The expectation (X growing with d) was wrong in kind for d <= 7: the penalty is a large prefactor,
   not a reduced effective distance. At m = 1, p = 1e-3 the corr suppression factor from d = 5 to 7 is 9.6 (indep 7.5,
   base 13.6); from d = 3 to 5 it is 3.3 (indep 6.5).
Sensitivity: V1 (independent random Pauli strings) 5.63e-3 / 2.60e-3 vs main 5.65e-3 / 2.61e-3 (d = 5 / 7, m = 10);
V2 (B along x) corr 5.59e-3 / 2.58e-3, indep 1.53e-3 / 1.04e-3; V3 (cluster threshold 0.2) 5.58e-3 / 2.59e-3; all
within ~1 % of main: the result does not depend on the Pauli-string construction, the field direction or the
cluster threshold. Diagnostic D1: decoding corr samples with the indep error model gives 5.64e-3 / 2.58e-3, the same
as with the corr model: a matching decoder gains nothing from knowing the correlations.

**What it shows.** In this model (BLU25-like pitch, 300 K, 4.6 MHz, unheralded loss as depolarisation, matching
decoder), one same-layer contaminant fails the two x-neighbour gate sites of its source with joint probability
~0.2, a weight-up-to-4 data-plus-ancilla fault. At p = 1e-3 and d = 7 this term alone raises the logical error per
round from 9.3e-7 to 2.5e-5 (27x), versus 4.7e-6 (5x) for independent errors of the same marginal: using the
marginal rate underestimates the logical cost by a factor of 5-10.
**What it does not include (cut or not done).** Heralded-erasure variant (loss detection) not run; correlation-aware
decoding not run; earlier-layer contaminants not included; the real BLU25 placement of code qubits in the zone is not
published (D010 item 3); baseline p unsourced; only memory-Z experiments; d <= 7.
