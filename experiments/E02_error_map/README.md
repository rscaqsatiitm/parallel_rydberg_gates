# E02. Error map of a gate pair perturbed by one contaminant, Evered 2023 configuration

Pre-registered 2026-11-20 before the run. Task S1. Model: src/prg/model.py (D004), controls E01.

**Configuration.** Rb87, |r> = 53S1/2 mJ = +1/2, Omega/2pi = 4.6 MHz, time-optimal pulse (registry
`evered23.*`), B = 8.5 G, pair distance 2 um, blockade 450 MHz. Pair axis along x (row axis).
Contaminant in 52P_J or 53P_J (all mJ', weighted by `contaminant_weights`, 300 K ARC rates).

**Design.**
(a) E_full(R, alpha, Bdir): contaminant present for the whole gate (created in an earlier layer).
    Positions in the array plane at distance R from the pair centre and in-plane angle alpha from the
    pair axis; R in {4, 5, 6, 7, 8, 10, 12, 14, 17, 20, 25, 30, 40} um, alpha in {0, 30, 60, 90} deg,
    Bdir in {x, y, z}. Output: increments of (error, leakage, Pauli part) over the no-contaminant gate,
    averaged over contaminant states; for each n' separately and BBR-rate-weighted over n' = 52, 53.
(b) E_same(R): contaminant switched on at t_on, averaged over t_on with weight p_r(t_on), the
    time-dependent Rydberg population of one atom of a neighbouring pair averaged over the four
    computational inputs (computed with the same pulse). t_on on a 12-point grid. Same R grid, alpha in
    {0, 90}, Bdir in {x, z}.
(c) Integrated Rydberg population per atom per gate, I_r = int p_r dt (inputs averaged), and contaminant
    probability per atom per gate p_c(n') = Gamma_BBR(53S -> n'P, 300 K) * I_r.

**Expectations (stated before the run).** From control E01-[2]: E_full ~ 1 at R ~ 8 um. Expect E_full
of order 1 for R <~ 9 um, a crossover near R_c where 2 pi C3/R^3 * T ~ 1 (handover estimate 13 um),
and E_full proportional to R^-6 beyond, from second-order perturbation theory in V T. Expect E_same
smaller than E_full by roughly the mean remaining fraction of the pulse squared, of order 0.3. Expect
I_r near 0.4 T (handover's recalled 2.947/Omega corresponds to I_r/T = 0.387).

**Verdict rule.** None (measurement of a model quantity). The tail exponent is checked: PASS if a
fit of log E_full vs log R over R in [25, 40] um gives slope -6.0 +- 0.3.

## Result

(appended 2026-11-20; results.json raw, summary.json p_c-weighted over n' = 52, 53; runtime 5216 s)

(c) T = 0.2641 us (= 2 pi x 1.215 / Omega; the 275 ns of the paper includes rise times not modelled),
I_r/T = 0.1925 (inputs-averaged; the handover's 2.947/Omega = 0.387 T is the value for an atom in |1>),
BBR rates 53S -> 52P 2525 /s, -> 53P 2458 /s, p_c = 1.284e-4 + 1.250e-4 = 2.533e-4 per atom per CZ.
(a) E_full (error increment, all contaminant states weighted), selected (B along x, alpha = 0 / 90 deg):
R = 4 um 0.63 / 0.69; 8 um 0.87 / 0.78; 10 um 0.87 / 0.49; 12 um 0.62 / 0.22; 14 um 0.36 / 0.10;
20 um 0.053 / 0.013; 30 um 4.7e-3 / 1.1e-3; 40 um 8.3e-4 / 2.0e-4. B along z (normal): nearly
isotropic in plane, 0.59 at 10 um, 0.013 at 20 um. Full tables: summary.json.
Leakage fraction of the error: 0.2-0.5 for R <= 8 um, > 0.9 for R >= 14 um, 1.00 for R >= 20 um:
the long-range error is excitation hopping into the gate atom (P-state leakage, converted to loss),
not a Pauli error.
Angular structure: suppression near alpha = 60 deg when B lies along the row (1 - 3 cos^2 theta node).
Tail exponent check (pre-registered): slopes of log E_full vs log R on [25, 40] um between -5.97 and
-6.04 for all B and alpha in {0, 90}: **PASS**.
(b) E_same / E_full = 0.39 for R >= 17 um (expectation ~0.3); 0.5-1.3 at R <= 12 um (a contaminant
appearing mid-gate is more harmful than one present throughout at short range).
