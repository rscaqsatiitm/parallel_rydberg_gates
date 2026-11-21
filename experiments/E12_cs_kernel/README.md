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
(appended 2026-11-21; controls.py -> controls_output.txt, run.py -> output.txt + results.json, contrast.py ->
contrast_output.txt)

**Controls.** (1) Planted analytic (stretched pair, theta = 0, R = 10 um, C3 = 3668.5 MHz um^3): max deviation
1.5e-12, PASS. (2) Null at 1000 um: 1.1e-7, PASS. (3) Doubled dipole-dipole prefactor: deviation 0.88, caught, PASS.

**Results (SIM, n = 60, B = 5 G).** Full tables in output.txt and results.json (4 states x 11 R x 4 theta; Ramsey at
8 times, blockade at 4 Rabi frequencies, pi and 2pi).
(i) *Blockade (pi pulse)* is a monotonic, near-step kernel: E_B > 0.9 for R below a crossover that, at
Omega/2pi = 1 MHz, lies at 12-15 um for theta = 0 and 8-12 um for theta = 90 deg (state dependent), and E_B < 0.05
beyond 20 um. The crossover moves out as Omega^-1/3 (E_B at 15 um, 59P3/2: 0.975 / 0.466 / 0.002 at 0.5 / 1 / 5 MHz,
theta = 0). This matches the expectation (R_ex(1 MHz) = 15 um, E11).
(ii) *Ramsey* is oscillatory, not monotonic: the probe's Rydberg component is coherently exchanged with the
contaminant and returns, so E_R(t) oscillates at the exchange frequency C3_eff / R^3 (exactly |cos| for the stretched
pair at theta = 0, control 1) and at other angles beats between several Delta-m channels split by the Zeeman energy.
At fixed t, E_R is therefore not a monotonic function of R (e.g. 60P3/2 3/2, theta = 0, t = 1 us: 0.010 at 5 um, 0.305
at 10 um). Maximised over the t grid, E_R reaches 0.68-0.98 at R = 5, 10 and 20 um for every state and angle.
The expectation that Ramsey would be smooth away from theta = 0 was wrong.
(iii) *Field dependence.* At theta = 0 the kernel is field independent (M conserved, degenerate pair states); at
theta = 90 deg it changes with B (59P3/2 3/2, t = 1 us, R = 5 um: 0.86 at 5 G, 0.64 at 20 G).

**Contrast needed (pre-registered definition C_min = 2.12 / (E sqrt N)).** Blockade at Omega/2pi = 1 MHz:
C_min = 0.07-0.08 (N = 1e3) at R = 5 um and 10 um for all states (E_B 0.8-1.0 except the P1/2 states at
theta = 90 deg, 0.34-0.37, C_min 0.18-0.19); at R = 20 um not resolvable with N = 1e4 (E_B 0.001-0.04) unless
Omega/2pi <= 0.5 MHz (E_B 0.30-0.41 at theta = 0 for P3/2, C_min 0.16-0.23 at N = 1e3). Ramsey, with t chosen from
the grid (choice of t made after seeing the results; reported as the best attainable, not as a pre-registered
setting): E_R >= 0.68 at all three R, C_min <= 0.10 at N = 1e3. At a single fixed t = 1 us, 10 of 24 (state, R, theta)
cases need C > 0.2 or are unresolvable because they fall near a revival. **Hence a contrast of 0.90-0.95 is ample at
R = 5 and 10 um for either sequence; at R = 20 um only a Ramsey sequence with a scanned free-evolution time, or a
blockade pulse at Omega/2pi <~ 0.5 MHz, resolves the contaminant.**
