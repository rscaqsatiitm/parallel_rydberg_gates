# E17. Same-layer floor for 3 Cs atoms under the synthetic bath: spacing 3-30 um, Rabi frequency 0.5-5 MHz (Addendum 3 item 7)

Pre-registered 2026-11-21 before the run. Task A3-7. Inputs D011 (Cs 60S, B = 5 G), E12 model (probe.py), E13 bath model.
**Protocol (ASSUMED).** Three atoms on a line perpendicular to B (theta = 90 deg), spacing a in
{3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30} um. All three are driven simultaneously by a resonant square 2pi pulse
g -> 60S1/2 +1/2 -> g at Omega/2pi in {0.5, 1, 2, 5} MHz (the simplest "layer": every atom should return to g).
A BBR (or bath) transfer of atom j during the pulse creates a contaminant in 59P or 60P (isotropic m' weights,
contaminant_weights) at time t_on with probability density proportional to p_r(t_on) = sin^2(Omega t_on / 2).
**Kernel.** E_same(R, Omega) = probability that a neighbouring atom i does not return to g, given a contaminant appearing
at t_on (averaged over t_on with weight p_r on a 12-point grid and over m'), minus the same without contaminant:
the probe evolves under the laser alone until t_on, then with the contaminant (probe.py Hamiltonian) to the end.
**Floor.** eps(a, Omega, T_eff) = mean over the three atoms of sum_{j != i} p_c E_same(|i - j| a), with
p_c(T_eff, Omega) from the E13 rate model (narrow band) for an exposure I_r = T/2, T = 2 pi / Omega.
T_eff in {300, 1e3, 3e3, 1e4} K.
**Validity conditions (reported, not applied silently).** (V1) van der Waals crosstalk between the simultaneously driven
atoms is outside the model: the ideal sequence is undisturbed only if |C6| / a^6 <= 0.1 Omega/2pi, with
C6(60S, 60S) = -101.6 GHz um^6 (ARC getC6perturbatively); points violating V1 are flagged. (V2) single contaminant:
3 p_c <= 0.1. (V3) bath transfer of the probe during the pulse Gamma_probe T <= 0.1 (E13).
**Shots (definition fixed now).** Measured: fraction of atoms not returned to g, with baseline q0 = 1 - C (C = 0.90, 0.95).
eps is measured as the difference between bath-on and bath-off runs (equal shots); a 10 % measurement needs
N_s = 2 q (1 - q) / (3 C^2 (0.1 eps')^2), q = q0 + eps, eps' = eps(T_eff) - eps(300 K); fully correlated bound x3.
**Expectation.** E_same ~ 0.3-0.5 x the blockade kernel of E14 at the same R (contaminant present for part of the pulse);
at 1 MHz significant out to ~12-15 um; V1 excludes a <~ 10 um at 1 MHz (R_vdW ~ 6.8 um) and <~ 7 um at 5 MHz; the floor
per atom at 1e4 K and a = 10-12 um of order 1e-3-1e-2, shots ~1e4-1e5.
**Verdict rule.** None (prediction).

## Result
