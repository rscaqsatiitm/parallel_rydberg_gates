# E07. K2 under D006: delay for an excess error of 1e-4 per CZ vs the kinematic interval (300 K)

Pre-registered 2026-11-20 before the run (E06 absolute numbers at 50/100/200/400 us are known).

**Design.** Same model, geometry, trajectories and declared input range as E06 (Normal lattice).
eps_tot(t) = p_c n_same + eps_prev(t): eps_prev from E06's stage-B code evaluated at gaps
t = 50, 100, ..., 600 us (multiples of 50 us available in the trajectories); same-layer floor
p_c n_same = sum over other sites, 2 atoms each, p_c E_same(r) with the contaminant at its tweezer
(created during the gate; E02 same-layer map, B along x or z, alpha in {0, 90} interpolated; B along y
mapped to x for the in-plane-perpendicular case: approximation, both B maps' extremes reported).
t_wait(1e-4) = smallest t on the grid, linearly interpolated in log eps, with eps_tot(t) <= 1e-4
(f = 1, leakage counted: the conservative convention for this budget); infinite if the floor >= 1e-4.
Kinematic interval: 92 us (parent repository, BLU25 in-zone mean CZ-layer spacing; docs/parent_extract.md).

**Rule (D006).** K2 fires if t_wait(1e-4) < 92 us for every variant in the declared range. Reported:
min/median/max of t_wait over the range, and the floor.
**Expectation.** From E06: eps_prev(100 us) = 2.2e-4 to 8.6e-4, so t_wait > 100 us for every variant
unless the floor alone exceeds 1e-4 (then t_wait is infinite); K2 not expected to fire.

## Result
