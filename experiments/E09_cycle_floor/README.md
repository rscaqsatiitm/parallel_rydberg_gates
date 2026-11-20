# E09. Thermal floor of the QEC cycle vs the kinematic floor (Gate 2, readings P and E of D009)

Pre-registered 2026-11-20 before the run. Task S3. Omega/2pi = 4.6 MHz only (E08 adds gate speed later).
**Design.** E07 machinery (trajectories, E02 maps) with p_c(T) = p_c(300 K) x Gamma(T)/Gamma(300 K)
and tau_P(T) from E05 (T in {300, 45, 4} K). Gap grid 50-600 us (step 50); interpolation in log excess.
Scale factor grid for the density limit s in {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.7, 2.0} (floor only, static
contaminants, E02 same-layer map) to find s_min(T); earlier-layer excess at s_min from the decay-only
model (the motion model's trajectories exist only for s = 1, 2; E07 showed the two agree within the
declared band).
**Outputs.** For each T: floor (min/max), s_min, t_wait (readings P and E), T_th for L = 4, 10 and both
t_ro, ratio to each kinematic floor; Gate 2 verdict at 300 K under each reading.
**Expectation.** From E07 (300 K): reading P infinite at s = 1 (density limit; s_min between 1 and 2);
reading E t_wait(1e-4) ~ 246 us so T_th(L=4) = 1.03-1.48 ms vs BLU25 kinematic 1.17-1.53 ms: ratio ~1,
Gate 2 not passed for BLU25 under reading E; for e40 schedules T_th(L=10) = 2.5-3.0 ms vs 3.9-35 ms:
ratio < 1, not passed. At 45 K the floor falls ~7x and tau_P rises ~2.5x.
**Verdict rule.** As D009. Not changed after the run.

## Result
(appended 2026-11-20; run.py, output.txt, results.json. Declared range: 108 contaminant-physics variants
x t_ro in {45, 500} us x kinematic lo/hi. The static earlier-layer model uses a 21 x 21 site patch and the
exact geometric survival sum; the motion model is on the 50-us grid only.)

| T | p_c | floor at s = 1 | s_min (floor < 1e-4) | t_wait E(1e-4) | t_wait E(1e-5) | t_wait P at s_min |
|---|---|---|---|---|---|---|
| 300 K | 2.53e-4 | 6.9e-4 - 1.08e-3 | 1.5 - 2.0 | 260-290 us (motion 250-300) | 490-510 us | 120-370 us |
| 45 K | 3.75e-5 | 1.0e-4 - 1.6e-4 | 1.1 - 1.2 | 260-300 us (motion 200-250) | 730-790 us | 410-1190 us |
| 4 K | 2.87e-6 | 7.9e-6 - 1.2e-5 | 1.0 | 50-60 us | 280-330 us | 50-60 us |

Ratio T_th / T_kin at 300 K (min-max over the declared range): BLU25 surface (L = 4): reading E(1e-4)
0.71-1.42, E(1e-5) 1.31-2.17, P(s_min) 0.34-1.69. e40 lifted-product (L = 10): A <= 0.22, B <= 0.76,
C 0.22-1.44, D <= 0.26 under any reading.

**Verdict (D009): Gate 2 NOT passed at 300 K under either reading** (no schedule has min ratio >= 2).
The expectation (ratio ~1 for BLU25 under E; < 1 for e40) was correct.
**What the numbers say instead.** (i) At 300 K the contaminant wait is of the same order as the BLU25
kinematic in-zone interval, and well below the move-dominated e40 schedules: BBR does not set the
cycle time of current or parent-proposed schedules. (ii) The binding thermal constraint is density:
the same-layer floor at the BLU25 zone pitch is 0.7-1.1e-3 per CZ at 300 K; a 1e-4 budget needs
1.5-2.0x larger pitch at 300 K, 1.1-1.2x at 45 K (ideal shield) and none at 4 K. (iii) Lower T lengthens
tau_P (t_wait E(1e-5) rises from ~500 us at 300 K to ~760 us at 45 K) while cutting p_c: cooling helps
density, not necessarily delay.
