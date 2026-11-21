# E14. Delay law against T_eff and shots needed to test it (Cs n = 60, Addendum 2 item 4)

Pre-registered 2026-11-21 before the run. Task C4. Inputs D011 (items 2, 6, 7), E12 model, E13 rate model.

**Protocol modelled (ASSUMED; the owner's sequence may differ).** N_a in {2, 3, 5, 10} atoms on a line, spacing
a in {5, 10} um, line perpendicular to B (theta = 90 deg). (1) Creation: every atom receives one gate-like Rydberg
exposure (Omega/2pi = 1 MHz, I_r = 0.234 us) under the bath at T_eff; it becomes a resonant contaminant with
probability p_c(T_eff) (E13 (a), narrow band). (2) Wait t, with the bath OFF (scenario A, 300 K) or ON (scenario B).
(3) Probe: resonant blockade pi pulse at Omega/2pi = 1 MHz on all atoms; an atom that is not itself a contaminant
counts as a probe.
**Delay law.** Excess probe error eps(t) = sum_{j != i} p_c S_res(t) <E_B(|i - j| a)>_m', averaged over probe atoms i,
where S_res is the resonant survival from E13 (b) for the scenario, and <E_B>_m' the E12-type blockade kernel averaged
over all 12 m' states of 59P and 60P with the isotropic BBR weights (contaminant_weights, 300 K; for a narrow isotropic
bath the J and m' weights are unchanged, DV3). First order in p_c (single contaminant per shot); validity reported as
N_a p_c. Fitted parameters: none.
**Shots (definition fixed now).** The measured probe quantity is the excitation probability q ~ C (contrast C in
{0.90, 0.95}). eps is the difference between runs with and without the creation exposure (equal shots). With N_p
independent probe atoms per shot, sigma_eps = sqrt(2 q (1 - q) / (N_s N_p)) / C. The delay law is "tested at 10 %"
when the ratio eps(tau_pred) / eps(0) is measured to 10 % relative: each of the two points to 7.1 %, hence
N_s = 2 q (1 - q) / (N_p C^2 (0.071 eps)^2) per point, summed over the two points (reported as total shots).
Bounds: N_p = number of non-contaminant atoms (independent probes, optimistic) and N_p = 1 (fully correlated probes,
pessimistic). T_eff in {300, 1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6} K.
**Expectation.** At 300 K p_c ~ 9e-4 (E11, 1 MHz) gives eps(0) ~ 1e-3 for 2 atoms at 5 um and N_s ~ 1e6-1e7; N_s falling
as T_eff^-2 while p_c is linear, flattening when p_c saturates (E13); in scenario B tau_res shortens as 1/T_eff, so the
test becomes a test of the bath-induced lifetime rather than of radiative decay.
**Verdict rule.** None (prediction).

## Result
(appended 2026-11-21; run.py -> output.txt (a = 5 um table), results.json (all rows))

**Inputs computed in the run.** m'-averaged blockade kernel (60S probe, theta = 90 deg, Omega/2pi = 1 MHz, isotropic
300 K weights over 59P and 60P): E_B = 0.996 (5 um), 0.689 (10 um), 0.068 (15 um), 0.003 (20 um), < 3e-4 beyond.
Hence only nearest neighbours at a = 5 um (and next-nearest weakly) contribute; at a = 10 um only nearest neighbours.

**Delay law (prediction).** eps(t) = eps(0) S_res(t), with eps(0) = p_c(T_eff) x (m'-averaged kernel sum) and S_res from E13:
scenario A (bath off during the wait): tau_res = 150 us at every T_eff (radiative decay plus room BBR);
scenario B (bath on, narrow band): tau_res = 150, 124, 93, 60, 33, 12, 4.3, 1.3 us at T_eff = 300, 1e3, 3e3, 1e4, 3e4, 1e5,
3e5, 1e6 K. S_res(t) is not a single exponential (population returns from 60S and from non-resonant states; full curves
in E13 results.json); the 10 % test is defined at t = tau_res as pre-registered.

**Shots for a 10 % test (two points, t = 0 and t = tau_res; contrast C = 0.90; independent-probe bound, fully
correlated bound in brackets).**
| T_eff (K) | p_c | 2 atoms, a = 5 um | 10 atoms, a = 5 um | 2 atoms, a = 10 um | 10 atoms, a = 10 um |
|---|---|---|---|---|---|
| 300 | 9.2e-4 | 2.2e8 [4.4e8] | 4.8e6 [4.8e7] | 4.6e8 [9.1e8] | 2.8e7 [2.8e8] |
| 1e3 | 3.1e-3 | 2.0e7 [3.9e7] | 4.4e5 [4.4e6] | 4.1e7 [8.2e7] | 2.5e6 [2.5e7] |
| 3e3 | 9.2e-3 | 2.2e6 [4.4e6] | 4.9e4 [4.9e5] | 4.7e6 [9.2e6] | 2.9e5 [2.8e6] |
| 1e4 | 3.0e-2 | 2.1e5 [4.1e5] | (4.7e3)* | 4.4e5 [8.5e5] | (2.7e4)* |
| 3e4 | 8.7e-2 | (2.7e4)* | (6.0e2)* | (5.6e4)* | (3.5e3)* |
C = 0.95 reduces every entry by a factor 2.1 (output.txt). (*) Outside the first-order validity condition
N_a p_c <= 0.1 (2 atoms: T_eff <~ 1.6e4 K; 10 atoms: T_eff <~ 3e3 K); there multi-contaminant events and saturation
(E13) make the formula invalid, and the entries are shown only to indicate scale.
Scenario B in addition requires the probe pulse (0.5 us) to be short compared with the bath-induced probe transfer:
Gamma_probe x 0.5 us <= 0.1 holds for T_eff <~ 1.4e4 K (narrow band, E13 (d)).
**Reading.** At room temperature a 10 % test of the delay law needs 5e6-5e8 shots: impractical with 2 atoms. A narrow-band
synthetic bath at T_eff ~ 1e4 K with 2 atoms at 5 um brings it to 2-4e5 shots (1-2e5 at C = 0.95) while staying in the
first-order regime and below the probe-validity limit; at that T_eff the two scenarios predict distinguishable
lifetimes (150 us bath off vs 60 us bath on). 10 atoms help only up to ~3e3 K (5e4-5e5 shots), because the
single-contaminant condition fails sooner. Expectation (N_s ~ T_eff^-2 while p_c is linear): correct within the valid range.
Model dependence: the probe protocol, spacing, contrast definition and the first-order treatment are ASSUMED (D011);
shot noise only (no drifts, no SPAM asymmetry); correlated-probe bound brackets the effect of one contaminant
affecting several probes.
