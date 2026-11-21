# E13. Cs n = 60 under a band-limited synthetic bath, T_eff = 300 K to 1e6 K (Addendum 2, item 3)

Pre-registered 2026-11-21 before the run. Task C3. Inputs D011 (item 6), DV3. Model src/prg/bath.py (to be written):
rate equations over Cs Rydberg levels n'' in [45, 75], l <= 3 (S1/2, P1/2, P3/2, D3/2, D5/2, F5/2, F7/2), Einstein A from
ARC getTransitionRate(T = 0) for each downward pair, stimulated rates A (1 + nbar) down and A (g_u / g_l) nbar up, nbar
from D011 item 6; every level also decays into a sink at its ARC 300 K out-of-window rate (total 300 K rate from ARC
lifetimes minus the in-window 300 K rates): spontaneous decay to low-lying states and BBR to n'' outside [45, 75].
The sink is not driven by the synthetic band (out-of-window lines are above 100 GHz; checked in the run).
Bands: narrow = [0.8 x 16.99, 1.2 x 20.67] GHz = [13.6, 24.8] GHz (the four 60S lines, E11); broad = [1, 100] GHz.
**Quantities.** (a) Gate exposure: start in 60S1/2, evolve for the exposure I_r = 0.1925 x 1.215 / (Omega/2pi) us
(Omega/2pi = 1 MHz: 0.234 us); report p_c = population of 59P + 60P (resonant), population left in 60S, other Rydberg,
sink; compare p_c with the linear value Gamma(T_eff) I_r. (b) Contaminant survival: start in 59P3/2, evolve with the
bath on and with it off (300 K) for 0-1000 us; report S_res(t) (population in 59P + 60P), its 1/e time tau_res(T_eff),
and the fractions in 60S, in other Rydberg states and in the sink. (c) Polarisation (DV3): correction factors
polarised / isotropic for linear pi, sigma+ and sigma- and an unpolarised beam along x or z, for 60S1/2 m = +1/2 and
59P3/2 m = -3/2..3/2 into each final level; and the m'-distribution of 59P3/2 contaminants with the resulting change of
the E12 blockade kernel (R = 10 um, theta = 0, Omega/2pi = 1 MHz; E computed for all six 59P m' states).
(d) Validity of the coherent kernel under the bath: T_eff at which the probe's bath transfer probability during
t = 1 us reaches 0.1.
**Controls.** (1) Planted: at T_eff = 300 K the model's upward rate 60S1/2 -> 60P3/2 equals ARC's getTransitionRate at
300 K to 1e-6 relative (independent use of nbar and degeneracy factors), and the 59P3/2 total out-rate equals 1/tau_ARC.
(2) Population conservation to 1e-10. (3) Corrupted input: degeneracy ratio inverted must fail (1).
**Expectations.** p_c linear in T_eff (Rayleigh-Jeans) up to Gamma I_r ~ 0.1, i.e. T_eff ~ 3e4 K for the narrow band at
1 MHz; beyond that saturation towards a quasi-equilibrium among 60S and the resonant P levels (~ degeneracy-weighted
fractions), and for the broad band rapid spreading to n'' S, D. tau_res falling as 1/T_eff with the bath on.
Polarisation: factor exactly 1 for linear pi and unpolarised beams from S1/2 (DV3 R1, R4); not 1 for circular from
|+1/2>; m-dependent for P3/2.
**Verdict rule.** None (prediction); controls PASS/FAIL.

## Result
(appended 2026-11-21; build.py (217 levels, 677 s), run.py -> output.txt, results.json; edge_check.py -> edge_output.txt)

**Controls.** (1) Upward 60S1/2 -> 60P3/2 rate at 300 K vs ARC getTransitionRate: 2.4e-15 relative, PASS; 59P3/2 total
out-rate vs 1/tau_ARC: 1.000 (by construction of the sink; not an independent test). (2) Conservation 1.6e-15, PASS.
(3) Inverted degeneracy ratio: 0.75 relative deviation, caught, PASS. The pre-registered check that the sink is not
driven by the synthetic band was not in the first run; edge_check.py (added after) shows the population on the
window-edge levels n'' = 45, 46, 74, 75 is <= 5e-3 of the remaining population (narrow band, 100 us) and <= 5e-2 (broad
band, 1e5-1e6 K, 100 us), and <= 2e-5 after a gate exposure; the unmodelled out-of-window driving therefore affects
only the "other Rydberg" fraction at broad band and high T_eff, not the resonant quantities.

**(a) Contaminant creation per gate exposure (Omega/2pi = 1 MHz, I_r = 0.234 us), narrow band** (broad in output.txt):
| T_eff (K) | p_c | linear Gamma I_r | p_c / linear | left in 60S | other Rydberg | Gamma_probe (/us) |
|---|---|---|---|---|---|---|
| 300 | 9.24e-4 | 9.26e-4 | 0.998 | 0.998 | 3.9e-4 | 0.011 |
| 1e3 | 3.08e-3 | 3.09e-3 | 0.997 | 0.995 | 3.9e-4 | 0.020 |
| 1e4 | 3.02e-2 | 3.09e-2 | 0.978 | 0.968 | 4.7e-4 | 0.139 |
| 3e4 | 8.69e-2 | 9.26e-2 | 0.939 | 0.911 | 1.1e-3 | 0.40 |
| 1e5 | 0.252 | 0.309 | 0.818 | 0.740 | 7.0e-3 | 1.33 |
| 3e5 | 0.525 | 0.926 | 0.567 | 0.431 | 0.043 | 3.96 |
| 1e6 | 0.664 | 3.09 | 0.215 | 0.147 | 0.188 | 13.2 |
**What scales linearly:** p_c and every bath-driven rate, in nbar (exactly) and in T_eff (to h nu / 2 k T_eff ~ 2e-3,
DV3 check). p_c is within 10 % of linear up to T_eff ~ 3e4 K. **What saturates:** p_c, towards ~0.5-0.7 for the narrow
band (population shared between 60S and the four resonant P levels) and falls again for the broad band (0.27 at 1e6 K)
because population is driven onward. **Where population spreads:** after one gate exposure, to non-resonant Rydberg
states only above ~1e5 K (narrow: 0.7 % at 1e5, 19 % at 1e6 K; broad: 7 % at 1e5, 65 % at 1e6 K).

**(b) Contaminant survival (start 59P3/2).** Bath off (300 K): resonant 1/e time tau_res = 150 us; after 100 us,
51 % resonant, 18 % other Rydberg (room BBR already spreads), 28 % sink. Bath ON, narrow / broad band:
tau_res = 124 / 85 us (1e3 K), 60 / 13 us (1e4 K), 12 / 1.3 us (1e5 K), 1.3 / 0.14 us (1e6 K). With the bath on, the
contaminant's harmful lifetime is set by bath-driven transfer to non-resonant states, not by radiative decay; a
narrow band preserves it ~5-10x longer than a broad one at the same T_eff.

**(c) Polarisation (DV3).** Numerical factors equal the independent checker's analytic values exactly: from
60S1/2 +1/2, pi and any unpolarised beam (axial or perpendicular) give 1.000 for each final J; sigma+ gives 0 (P1/2)
and 1.5 (P3/2), sigma- 2 and 0.5, and 1 for the J-summed rate. From 59P3/2 +3/2 -> 60S1/2: pi 0, sigma+ 0, sigma- 3,
axial beam 1.5, perpendicular beam 0.75; into 58D5/2: 0.8, 2.0, 0.2, 1.1, 0.95 (m = +1/2 values in output.txt); m-averaged
all 1. **Answer:** a band-limited, single-direction, polarised field is equivalent to a blackbody of the same spectral
energy density (T_eff from nbar = c^2 I_nu / (8 pi h nu^3)) for the creation rate out of nS1/2 (factor exactly 1 for
linear or unpolarised light; for circular light only after summing over P1/2 + P3/2), but NOT for the onward rates of
the P3/2 contaminants, whose correction factors range from 0 to 3 depending on m and polarisation, and NOT for the
m'-distribution of the contaminants (pi light from +1/2 populates only m' = +1/2). The effect on the harmful fraction is
small at the one kernel point computed: E_B at R = 10 um, theta = 0, 1 MHz is 0.96-0.99 for m' = -1/2, +1/2, +3/2 and
0.36 for m' = -3/2; the m'-weighted kernel changes by -2 % (pi), +0.9 % (sigma+) and +1.4 % (sigma-) relative to isotropic.
**(d) Validity of the coherent kernel (E12) under the bath:** the probe's own bath transfer during 1 us reaches 0.1 at
T_eff ~ 7e3 K (narrow) and ~ 6e3 K (broad); above that, kernels must be measured with sequences shorter than
0.1 / Gamma_probe.
**Expectations.** Linear-to-3e4 K: correct. tau_res falling as 1/T_eff: only asymptotically (150 -> 124 us at 1e3 K,
because radiative decay and room BBR dominate at low T_eff). Polarisation: correct for S1/2; circular result refined
(J-summed equality) by the independent check.
