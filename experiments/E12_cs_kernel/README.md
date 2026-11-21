# E12. Error kernel of a deterministic n'P contaminant on a blockade and a Ramsey sequence (Cs, Addendum 2 item 2)

Pre-registered 2026-11-21 before the run. Task C2. Inputs D011; n = 60 (E11 recommendation), n' = 59 and 60.
Model: src/prg/probe.py (probe + contaminant, first-order S-P dipole-dipole exchange with full Zeeman and fine
structure, B = 5 G along z; no decay, no motion, no laser on the contaminant). Written separately from model.py; shares
atomic.py (ARC matrix elements, Wigner-Eckart).

**Contaminant states.** 59P3/2 mJ=+3/2, 59P1/2 mJ=+1/2, 60P3/2 mJ=+3/2, 60P1/2 mJ=+1/2 (D011 item 5).
**Geometry.** R in {3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30} um; theta in {0, 30, 54.74, 90} deg from B.
**Sequences and kernels.**
(a) Ramsey: instantaneous pi/2 on g -> 60S1/2 mJ=+1/2, free evolution t, coherence rho_gr. Kernel
E_R(R, theta, t) = 1 - |rho_gr| / |rho_gr(no contaminant)| (contrast loss) and the phase shift; t in
{0.1, 0.2, 0.5, 1, 2, 5, 10, 20} us.
(b) Blockade: resonant square pi pulse g -> r of Rabi frequency Omega (duration t = pi / Omega);
E_B = 1 - P_exc / P_exc(no contaminant), P_exc = 1 - P_g. Omega/2pi in {0.5, 1, 2, 5} MHz (t = 1, 0.5, 0.25, 0.1 us).
Also the 2pi pulse: E_2pi = P_g(no contaminant) - P_g.
Probe and contaminant decay are omitted (t <= 20 us vs tau ~ 150 us at 300 K; both cancel to first order in the
ratio; flagged). B = 20 G sensitivity: Ramsey at theta = 0, 90 deg, 59P3/2 3/2 only.
**Contrast needed (definition fixed now).** A kernel value E is resolved at 3 sigma with N shots per setting (with
and without contaminant) when C E >= 3 sqrt(2 x 0.25 / N); hence C_min = 2.12 / (E sqrt(N)). Reported at R = 5, 10,
20 um for N = 1e3 and 1e4; C_min > 1 means not resolvable at that N.

**Controls (before the production run).** (1) Planted analytic: theta = 0, contaminant 59P3/2 mJ=+3/2. The pair
subspace with M = 2 is exactly two-dimensional, {|r, P 3/2>, |P 3/2, r>}, coupled by C3/R^3 with
C3 = K |<P3/2 3/2| d_+1 |S1/2 1/2>|^2 (E11 value 3669 MHz um^3), so |rho_gr| / |rho_gr,0| = |cos(2 pi C3 t / R^3)|.
PASS if the model agrees to 1e-8 at R = 10 um for all t. (2) Null: R = 1000 um, all kernels < 1e-6.
(3) Corrupted input caught: dipole-dipole prefactor doubled must fail control (1).
**Expectation.** Ramsey: E_R ~ 1 for C3 t / R^3 >~ 0.25 (R <~ 15 um at t = 1 us for 59P3/2); oscillatory at theta = 0
for the stretched state, smoother elsewhere; small angle dependence near the magic angle different from 1-3cos^2.
Blockade: E_B ~ 1 (full blockade) for C3 / R^3 >> Omega; crossover near R_ex(Omega) (15 um at 1 MHz).
**Verdict rule.** None (prediction); controls PASS/FAIL as stated.

## Result
