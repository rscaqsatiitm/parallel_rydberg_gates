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
