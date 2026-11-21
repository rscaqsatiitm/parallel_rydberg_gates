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
