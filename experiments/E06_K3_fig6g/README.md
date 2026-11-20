# E06. K3: zero-parameter prediction of BLU25 ED Fig. 6g (CZ fidelity vs time between gates)

Pre-registered 2026-11-20 before the run and before any E02 map value was seen (only the E01 control
value at 8 um and the E02 header line, I_r and p_c, are known). Task S2. Rule: Addendum 1 (K3).

## Data (FIGURE READ, literature/notes/blu25_fig6g_traps.md; human check pending)
Normal: 50 us 99.312(15) %, 100 us 99.487(33) %, 200 us 99.482(14) %, 400 us 99.488(<~10) %.
Sparse (2x site separation): 50 us 99.558(20) %, 100 us 99.474(~25) %, 200 us 99.543(31) %.
Measured excess error relative to the Normal 400 us point, D(t) = F(400) - F(t):
Normal: D(50) = 0.176, D(100) = 0.001, D(200) = 0.006 (%); sigma = quadrature of the two error bars,
taking 0.010 % for the 400 us bar: sigma(50) = 0.018, sigma(100) = 0.034, sigma(200) = 0.017 (%).
Sparse: compared with its own 200 us point (no 400 us point): D_s(50) = -0.015 +- 0.037 %.

## Model (no fitted parameter)
Excess error per CZ, averaged over gate sites, eq. (1) of DV1, evaluated at gap t (layers of gate
duration T = 0.264 us every t):
  eps(t) = sum_i p_c [ E_same(r_i) + sum_{j>=1} S(j t) < E_full(r_i(j t) - r_target) >_traj ],
p_c = 2.53e-4 per atom per CZ (E02, 52P + 53P weighted), E_full and E_same from E02 (2023 pulse,
Omega/2pi = 4.6 MHz, 53S; BLU25 states the same n = 53, 4.6 MHz and 270 ns), interpolated in
(log R, in-plane angle); for out-of-plane positions R = |r| and the angle of the in-plane projection.
S(t) = exp(-t/tau_P) with ARC 300 K tau_P (E05), weighted by J. Trajectories r_i(t): classical motion
in the repulsive tweezer landscape of DV2 (all sites' tweezers, both atoms per site), initial thermal
state at 10 uK in the ground trap, U_g = 1 mK, w = 1.0 um, 852 nm (D007), 200 trajectories per source atom.
Geometry (D008): BLU25 gate zone, 8 rows x 16 columns of sites (sourced), pitch 8.571 um x 12.0 um
(parent repository; 8.571 printed, 12.0 figure-read), pair axis along either lattice direction, B
along x, y or z. Sparse: both pitches doubled. Fidelity convention: excess infidelity = eps x f with
f in {0.8, 1.0} (average-gate vs entanglement fidelity; BLU25 RB convention not stated) and leakage
counted fully or not at all (loss handling in the RB fit not stated).

**Declared input range (the prediction band).** All combinations of: U_g in {0.5, 1, 2} mK;
w in {0.8, 1.0, 1.2} um; pair axis in {x, y}; B in {x, y, z}; f in {0.8, 1.0}; leakage in {counted, not};
geometry pitch swap (8.571 along rows or along columns). The band is [min, max] over these.

## Verdict rule (fixed now; not changed after the run)
K3 FIRES if at any of the four tests the prediction band does not overlap the 2-sigma data interval:
(i) Normal D(50) in [0.140, 0.212] %; (ii) Normal D(100) in [-0.067, 0.069] %; (iii) Normal D(200) in
[-0.028, 0.040] %; (iv) Sparse D_s(50) in [-0.089, 0.059] % (prediction: eps_sparse(50) - eps_sparse(200)).
Model prediction for D(t) is eps(t) - eps(400 us).
In addition (not part of the kill rule, reported): the "decay-only" variant (no motion) is evaluated
with the same rule, to test whether motion is required.

## Result
(appended after the run)
(appended 2026-11-20; predictions.json, verdict.py, verdict_output.txt. 432 model variants per
motion/static case x f in {0.8, 1.0}.)

**Verdict: K3 does NOT fire.** Prediction band (min..max over the declared range) vs 2-sigma data:
| test | data (%) | motion model band (%) | median | decay-only band (%) |
|---|---|---|---|---|
| Normal D(50) | [0.140, 0.212] | [0.056, 0.218] | 0.122 | [0.042, 0.247] |
| Normal D(100) | [-0.067, 0.069] | [0.022, 0.085] | 0.046 | [0.016, 0.091] |
| Normal D(200) | [-0.028, 0.040] | [0.004, 0.018] | 0.010 | [0.004, 0.022] |
| Sparse D_s(50) | [-0.089, 0.059] | [0.005, 0.046] | 0.018 | [0.000, 0.022] |
Absolute excess from earlier layers, Normal, motion model: 0.056-0.220 % at 50 us, 0.022-0.086 % at
100 us, 0.0045-0.020 % at 200 us, 0.0001-0.0015 % at 400 us.

**What failed or is weak.** (i) The test does not discriminate: the decay-only variant also passes, so
ED Fig. 6g does not show that motion is needed (an inference made before the run, in conversation,
is not supported). (ii) The band spans a factor ~4 at 50 us, dominated by U_g, B direction and the
fidelity convention f; it is wide enough that agreement is a weak confirmation. (iii) The median
prediction at 100 us (0.046 %) is above the measured central value (0.001 %) but within 2 sigma.
(iv) Same-layer errors cancel in D(t) and are untested here.
**What it shows.** With no fitted parameter, the model gives the size of the 50 us excess within the
band containing the measurement (median 0.7 x measured) and its disappearance by 100-200 us, and a
small or zero effect for 2x spacing, as observed.
