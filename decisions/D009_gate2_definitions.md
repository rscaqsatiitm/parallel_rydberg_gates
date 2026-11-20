# D009. Operational definitions for Gate 2 (fixed before E09 is run)

Date: 2026-11-20, autonomous run (owner asleep). Addendum 1 defines Gate 2 as: thermal floor
T_c,min = L t_wait + readout exceeds the kinematic floor of the same schedule by >= 2 at 300 K for at least
one schedule, stable under the declared input ranges. E07 found a same-layer floor (0.7-1.1e-3 per CZ in
a BLU25-like dense zone at 300 K) that no delay removes, which makes "t_wait for a total excess of 1e-4
per CZ" infinite at that density. To avoid choosing the definition after seeing results, BOTH readings
are fixed now and reported; the owner chooses which one carries the thesis.

- **Reading P (primary, owner's K2 wording):** t_wait = delay at which the TOTAL contaminant excess
  (same-layer floor + earlier layers) per CZ <= eps* = 1e-4. If the floor >= eps*, t_wait = infinity and
  the statement becomes a density limit: report s_min, the smallest lattice scale factor (both pitches
  multiplied by s) at which the floor < eps*, and t_wait at s_min (earlier layers recomputed at s_min).
- **Reading E (earlier layers only):** t_wait = delay at which the excess from EARLIER layers <= eps*,
  eps* in {1e-4, 1e-5}; the same-layer floor reported separately as a density floor.
- **Thermal floor:** T_th = L t_wait + t_ro (owner's formula), L = 4 (BLU25 surface-code round),
  L = 10 (lifted-product schedules of parent e40); t_ro in {45 us (LEE26 via parent e40), 500 us (BLU24
  mid-circuit image)}.
- **Kinematic floor (parent repository, docs/parent_extract.md):** BLU25 surface round 1.344 ms
  (lo 1.171, hi 1.527 ms; includes the 0.975 ms ancilla swap); e40 lifted-product schedules A-D:
  A 24.9-35.5 ms, B 7.40-15.5 ms, C 3.90-5.55 ms, D 21.4-23.7 ms. Ratio = T_th / T_kin; Gate 2 needs
  ratio >= 2 at 300 K for at least one schedule over the whole declared range (min over the range >= 2).
- **Density:** the contaminant physics uses the BLU25 gate-zone lattice (8.571 x 12.0 um, D008) for all
  schedules; the e40 schedules' own zone pitches are not used (not checked here; flagged).
- **Declared range:** as E06/E07 (U_g, w, pair axis, B direction, pitch assignment), f = 1, leakage
  counted; t_ro and kinematic lo/hi as above; temperature 300 K (also 45 K, 4 K reported, ideal-shield
  ARC rates, E05).
