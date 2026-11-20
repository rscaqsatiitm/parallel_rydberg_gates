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
