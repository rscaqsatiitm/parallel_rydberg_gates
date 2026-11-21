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
(appended 2026-11-21; run.py -> output.txt, results.json. Implementation change before the reported run, not a design
change: the first run was killed at the 30-min limit; propagation was switched from per-step expm to one
eigendecomposition per piecewise-constant Hamiltonian (mathematically identical). A display bug (shot counts at 300 K,
where eps - eps(300 K) = 0 by definition) was fixed; 300 K has no shot entry.)

**Kernel E_same(R) (60S probe, 2pi pulse, theta = 90 deg, m'-averaged over 59P and 60P):** saturates at 0.75 at short range
(the contaminant blocks the probe's return in three quarters of the creation times); falls to 0.5 at R ~ 20 um
(0.5 MHz), 16 um (1 MHz), 13 um (2 MHz), 10 um (5 MHz); 0.02-0.09 at 30 um for 0.5-1 MHz. The expectation
(0.3-0.5 x the blockade kernel) was wrong: E_same is comparable to the pi-pulse kernel at short range.
**V1 (vdW crosstalk, |C6| / a^6 <= 0.1 Omega/2pi) excludes a <= 10 um at 0.5-1 MHz, a <= 8 um at 2 MHz, a <= 6 um at 5 MHz.**
**Floor per atom (3 atoms on a line), 300 K, valid spacings:** Omega/2pi = 1 MHz: 1.8e-3 (12 um), 1.4e-3 (15), 5.7e-4 (20),
1.7e-4 (25), 6.1e-5 (30); 5 MHz: 3.7e-4 (8 um), 2.4e-4 (10), 1.1e-4 (12), 3.5e-5 (15), 6.5e-6 (20).
**Under the synthetic bath (narrow band), with shots for a 10 % measurement of eps - eps(300 K) at C = 0.90
(independent-probe bound; x3 for fully correlated):**
| T_eff | Omega/2pi | a = 12 um | a = 15 um | a = 20 um | validity |
|---|---|---|---|---|---|
| 1e3 K | 1 MHz | 6.0e-3 [4e5] | 4.8e-3 [7e5] | 1.9e-3 [4e6] | V1-V3 ok |
| 3e3 K | 1 MHz | 1.8e-2 [3e4] | 1.4e-2 [5e4] | 5.6e-3 [3e5] | ok |
| 3e3 K | 2 MHz | 7.2e-3 [2e5] (10 um: 8.9e-3 [1e5]) | 3.7e-3 [7e5] | 8.4e-4 [1e7] | ok |
| 1e4 K | 2 MHz | 2.4e-2 [2e4] (10 um: 2.9e-2 [1e4]) | 1.2e-2 [6e4] | 2.8e-3 [1e6] | ok |
| 1e4 K | 5 MHz | 3.8e-3 [6e5] (8 um: 1.2e-2 [6e4]) | 1.2e-3 [6e6] | 2.1e-4 [2e8] | ok |
| 1e4 K | 1 MHz | 5.8e-2 [3e3] | 4.6e-2 [5e3] | 1.8e-2 [3e4] | V2, V3 violated |
Full grid (a = 3-30 um, Omega/2pi = 0.5-5 MHz, T_eff = 300 K-1e4 K) in output.txt. **Best valid operating points:**
T_eff ~ 3e3 K at 1 MHz and a = 12-15 um, or T_eff ~ 1e4 K at 2 MHz and a = 10-12 um: floor 1-3e-2 per atom, 1-5e4 shots.
The floor falls with Omega at fixed a (e.g. 1e4 K, a = 12 um: 5.8e-2, 2.4e-2, 3.8e-3 at 1, 2, 5 MHz) and with a as the kernel
tail; at 5 MHz and a >= 15 um it is below 1e-3 even at 1e4 K.
