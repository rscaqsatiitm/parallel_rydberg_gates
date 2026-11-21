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
