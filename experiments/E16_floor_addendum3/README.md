# E16. Same-layer floor: extra BBR channels, earlier layers at 400 us, row pitch 10.0 um (Addendum 3, items 3-4)

Pre-registered 2026-11-21 before the run. Task A3-F. Rb 53S, Omega/2pi = 4.6 MHz, 300 K, E02 maps, E07 floor procedure.

**(A) Extra BBR channels.** BBR transfer from 53S1/2 into n'P_J with n' not in {52, 53} (n' in [33, 73], ARC rates,
as E05). For each n' the same-layer map is obtained by rescaling the E02 (52P + 53P) map in distance,
E_n'(R) = E_res(R (C3_res / C3_n')^(1/3)), with C3 proportional to |<53S1/2|r|n'P3/2>|^2 (the kernel depends on the
exchange through C3 / R^3 at fixed pulse; Zeeman and fine-structure detail ignored: approximation). Control of the
approximation: direct three-atom calculation (model.py, nprime = 51 and 54, B along z, alpha = 0, R = 8.571, 12, 17 um,
6-point t_on grid as E08) compared with the rescaled map; reported, and the direct values replace the rescaled ones
if they differ by more than a factor 2 (then the rescaling is declared failed for the floor).
Floor_extra = sum over n' of p_c(n') n_same(n'), p_c(n') = Gamma(53S -> n'P) I_r.
**(B) Earlier layers at 400 us.** Static (decay-only) model, Eq. (2) of the paper: p_c n_full / (exp(t / tau_P) - 1)
at t = 400 us, tau_P = 96-102 us, resonant channels (and extra channels with rescaled E_full, tau taken equal).
(The motion model's 400 us values from E06/E07, 1e-6 to 1.5e-5, are reported alongside.)
**(C) Row pitch 10.0 um.** Floor and earlier-layer term with pitches (10.0, 12.0) um, both assignments to the lattice
axes, everything else as E07 (declared range: pair axis, B direction).
**Outputs.** Floor (min, max over the declared range) for: resonant only (reproduces E07: 6.9e-4 to 1.08e-3, control),
+ extra channels, + earlier layers, all; at pitch 8.571 and 10.0; relative change. Also the factor
(floor_resonant + floor_extra) / floor_resonant and the earlier-layer per-CZ value, passed to E18 (Stim).
**Expectation.** Extra channels: C3 for |n' - 53| >= 2 is ~10-50x smaller, so R_1/2 shrinks by ~2-4x and the extra
floor is a few % of the resonant one (+1 to +10 %). Earlier layers at 400 us: e^-4 ~ 2 % of p_c n_full ~ 1e-3 ->
~2e-5 (+2 %). Pitch 10.0: floor falls by ~1.5x (from E09 scale-factor curve, s = 1.17 on one axis only, so less).
**Verdict rule.** None (measurement of model quantities); the control (A) is PASS/FAIL as stated.

## Result
(appended 2026-11-21; run.py -> output.txt, results.json)

**Control (A).** Rescaled vs direct three-atom E_same for n' = 51 and 54 at 8.571, 12, 17 um: ratio 0.92-1.09, PASS
(within the factor-2 rule); the rescaled maps are used.
**(A) Extra channels.** BBR transfer outside 52P + 53P is 2156 /s of 7342 /s (29 %), but their exchange strength is
small: C3 ratio 0.017 for 51P and 54P, 0.003 for 50P and 55P, <= 0.001 beyond. Extra same-layer floor 5.8e-8 to 2.4e-7 per
CZ, i.e. +2e-4 relative at most. **The pre-registered expectation (+1 to +10 %) was wrong: the extra channels are
negligible** (the same-layer factor is 1.000 to three decimals). The lower-bound caveat in the paper (Sec. II A) is
therefore resolved: omitting them changes the floor by < 0.03 %.
**(B) Earlier layers at 400 us (static model, all channels).** 2.0e-5 to 3.2e-5 per CZ at pitch 8.571 um; 1.6e-5 to 2.5e-5
at 10.0 um (motion model, E06/E07: 1e-6 to 1.5e-5). Adds +2.5 % to +3.8 % to the floor.
**(C) Floor per CZ (min-max over pair axis, B direction, pitch assignment):**
| row pitch | resonant same-layer | + extra channels + earlier layers (400 us) | change |
|---|---|---|---|
| 8.571 um | 6.92e-4 - 1.08e-3 (reproduces E07: control PASS) | 7.18e-4 - 1.11e-3 | +2.5 to +3.8 % |
| 10.0 um | 4.57e-4 - 8.50e-4 | 4.77e-4 - 8.74e-4 | +2.8 to +4.4 % |
Pitch 10.0 um lowers the resonant floor by 21-34 % relative to 8.571 um (expectation "~1.5x less, smaller because one
axis only": about right at the low end, the effect is 1.27-1.51x). **How much the floor moves:** all additions together
move it by +3 to +4 %; the row-pitch reading moves it by -21 to -34 %; the pitch question dominates.
