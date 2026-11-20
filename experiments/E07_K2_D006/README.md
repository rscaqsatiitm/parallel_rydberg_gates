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
(appended 2026-11-20; run.py, results.json. Implementation note: the sum over earlier layers is
truncated at 600 us for gaps whose multiples beyond 600 us were not stored; S(600 us) < 3e-3 of the
leading term. E06 numbers were re-generated after this change and are identical.)

**Verdict: K2 (D006) does NOT fire.** In all 108 variants the same-layer floor p_c n_same exceeds 1e-4
(min 6.9e-4, median 1.05e-3, max 1.08e-3 per CZ), so no delay brings the excess to 1e-4: t_wait(1e-4) is
infinite, not below 92 us. The expectation (t_wait > 100 us, finite) was wrong in kind: the floor,
not the delay, binds at 300 K in the BLU25-like dense zone.

**Additional, not pre-registered (reported for Stage 3 design):** delay at which the excess from
earlier layers alone falls to 1e-4: 235-251 us (median 246) over the declared range; to 1e-5:
347-431 us. Kinematic interval 92 us. Motion and decay-only variants differ little because, in an
array much larger than the contaminant's flight distance per lifetime (0.18 um/us x 100 us = 18 um vs
a ~150 um zone), ejection from the tweezer redistributes contaminants over the array instead of
removing them: the earlier-layer excess is decay-limited, t_wait ~ tau_P ln(1 + p_c n_full / eps*).

**Post-hoc consistency check (NOT pre-registered; data seen before the calculation):**
floor_sparse.py. Floor, Sparse geometry: 1.7e-5 to 6.9e-5. Predicted Normal - Sparse difference at long
gaps (floor x f, f in 0.8..1): 5.0e-4 to 1.06e-3, plus 0.4-1.4e-4 from earlier layers at 200 us.
Measured (ED Fig. 6g, 200 us, figure read): 99.543(31) - 99.482(14) % = 6.1(3.4)e-4. Consistent.
