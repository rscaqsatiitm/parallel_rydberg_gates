# E18. Addendum 3 Stim checks: erasure, correlation-aware decoding, d = 9-11, item-3 additions, pitch 10.0 um

Pre-registered 2026-11-21 before any production run. Task A3-S. Model: E10 (D010) plus D012. Code: e18.py.
All points at m = 1 (p_c = 2.53e-4, 300 K), baseline p = 1e-3 unless stated. Statistics as E10 (>= 100 failures or
>= 1e6 shots, 95 % Wilson intervals, zero failures as upper bound). X = (corr - base) / (indep - base) with conservative
interval bounds, as E10.

**Item 1a (erasure).** corr and indep with flagged failures (D012 items 1-2), eta in {0, 0.5, 0.8, 0.95, 1.0}, decoded
per D012 item 2; base unchanged (no contaminant, nothing heralded). d = 3, 5, 7.
**Item 1b (correlated matching).** corr decoded with PyMatching correlated matching; X_1b uses base and indep decoded
the same way (correlated matching on a DEM without contaminant hyperedges). d = 3, 5, 7.
**Item 2.** base, corr, indep at d = 9, 11.
**Item 3.** corr and indep with (i) f_prev added, (ii) non-resonant factor applied, (iii) both; d = 5, 7; values from
the parent (E16) or provisional (D012 item 6), stated in the result.
**Item 4.** corr and indep at pitch (10.0, 12.0) um, d = 3, 5, 7, p = 1e-3 (p = 2e-3 if budget allows).

**Controls (before production).**
C1 eta = 0 equivalence: flagged corr and indep at d = 3 decoded without heralds reproduce E10's corr and indep logical
   rates within the 95 % intervals (1e6 shots). C2 herald marginal: flagged indep at d = 3, m = 100, one round: the fire
   rate of each flag equals that location's marginal f within 4 sigma. C3 erasure decoding, planted and corrupted:
   flagged corr at d = 3, m = 10, eta = 1: decoding with heralds must give fewer failures than without (planted: the
   heralds carry information); with the herald-to-location map shifted by one location (corrupted input) the benefit
   must disappear (failures not below the no-herald value minus 2 sigma). C4 correlated matching: on base (no
   contaminant) d = 5, correlated and standard matching agree within intervals (no correlated contaminant structure to
   exploit; baseline Y errors may give a small gain, reported).
**Expectations.** 1a: X falls with eta because heralded failures cost little; at eta = 1, both corr and indep excess
should drop by an order of magnitude or more, and X may approach 1 if the remaining unheralded part is small. 1b:
correlated matching reduces corr's rate modestly (E10 D1 showed a matching decoder does not use the correlation);
X_1b expected 3-8. 2: X(d = 9, 11) within the d = 7 interval (flat). 4: larger row pitch lowers both excesses; X similar.
**Verdict rules (fixed now).**
V1a "erasure removes the penalty": X(eta = 0.95) upper bound < 2 at both d = 5 and 7; "penalty survives erasure": X
lower bound > 2 at d = 5 and 7 for eta >= 0.8; otherwise "partially reduced".
V1b "decoder recovers": X_1b upper bound < X_E10 lower bound at d = 5 and 7; otherwise "not recovered".
V2 "X flat": X(d = 11) interval overlaps the E10 d = 7 interval [4.2, 9.7]; "grows" if its lower bound > 9.7; "shrinks"
if its upper bound < 4.2. Same statement for d = 9.
Items 3 and 4: no verdict; report shifts of the logical rates and of X relative to E10.

## Result
