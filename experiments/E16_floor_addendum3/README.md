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
