# E11. Cs nS, n = 50-80: contaminant creation by final state, lifetimes, transition frequencies (Addendum 2, item 1)

Pre-registered 2026-11-21 before the run. Task C1. Inputs D011. Library evaluation (ARC 3.10.2), no fitted parameter.

**Design.** For each n in 50..80: (a) BBR-stimulated rate at 300 K from nS1/2 into every n'P_J with
n' in [n-8, n+8] (ARC getTransitionRate(T) minus its T = 0 part for downward lines), and the total BBR rate out of nS
(difference of ARC lifetimes at 300 K and 0 K); fraction into the resonant manifolds (n-1)P + nP; (b) p_c per gate by
final state for Omega/2pi = 1 and 5 MHz (D011 item 2) and per us of Rydberg time; (c) lifetimes of (n-1)P_J and nP_J
at 300 K and 0 K; (d) transition frequencies nS1/2 -> n'P_J and the frequency band containing 90 % of the BBR rate;
(e) the S-P exchange strength C3 = K |<nS1/2 1/2| d_+1 | n'P3/2 3/2>|^2 (stretched pair along B, MHz um^3) and the
exchange radius R_ex(Omega) = (C3 / (Omega/2pi))^(1/3).
Controls: (i) planted: the same code at Rb 53S reproduces E05 (2525, 2458 /s; tau 95.8-102.2 us) to 1e-3;
(ii) the per-final-state rates sum to the lifetime-difference total within 2 % (else the n' window is too small).
**Expectation.** Resonant fraction ~0.6-0.7 (JILA value for Rb 0.68); total BBR rate decreasing slowly with n;
P lifetimes rising roughly as n*^3 at 0 K but less steeply at 300 K; resonant line frequencies falling as n*^-3
(~10-30 GHz near n = 60-70); C3 rising as n*^4.
**Recommendation rule (fixed now).** Recommend the n range that satisfies all of: (1) both resonant lines below a
band ceiling f_max, reported for f_max = 20 and 40 GHz (the owner's noise-source ceiling is unknown); (2) resonant
P lifetime at 300 K >= 100 us (delays long compared with sequence times); (3) R_ex at Omega/2pi = 1 MHz between 10
and 25 um (so the kernel changes across the owner's R = 5, 10, 20 um). Within that range, prefer lower n (smaller
blockade radius relative to trap spacing, less sensitivity to stray fields; opinion, not computed).

## Result
(appended 2026-11-21; run.py, output.txt (table for every n), results.json)

**Controls.** (i) Planted Rb 53S: 2525 and 2458 /s, identical to E05: PASS. (ii) Sum of per-state rates vs the
lifetime-difference total within 2 %: **FAIL**. With the pre-registered window n' = n +- 8 the sum is 0.895-0.922 of the
total; widened to n +- 20 (a diagnostic step the rule anticipates) it is 0.949-0.977, falling with n. The remainder is
BBR transfer to n'P outside n +- 20 (the far tail of the Planck spectrum). Consequence: all fractions below are quoted
relative to the lifetime-difference total, which does not depend on the window; the "90 % band" column in output.txt
is relative to the in-window sum and is therefore only indicative.

**Results (COMPUTED, ARC 3.10.2, 300 K, ideal Planck field).** Selected n (all n in output.txt):

| n | Gamma(nS -> (n-1)P + nP) /s | fraction of total BBR | (n-1)P3/2, nP3/2 line (GHz) | tau (n-1)P3/2, nP3/2 at 300 K (us) | same at 0 K (us) | C3 stretched (n-1)P3/2 (MHz um^3) | R_ex at 1 MHz (um) |
|---|---|---|---|---|---|---|---|
| 52 | 5373 | 0.68 | -30.92, 28.81 | 102.4, 107.1 | 336.9, 358.6 | 1967 | 12.5 |
| 55 | 4762 | 0.68 | -25.74, 24.04 | 116.9, 122.0 | 404.6, 429.0 | 2514 | 13.6 |
| 60 | 3952 | 0.67 | -19.41, 18.18 | 143.3, 148.9 | 536.6, 566.1 | 3669 | 15.4 |
| 65 | 3331 | 0.67 | -15.00, 14.08 | 172.4, 178.6 | 694.7, 729.6 | 5182 | 17.3 |
| 70 | 2846 | 0.67 | -11.83, 11.12 | 204.2, 210.9 | 881.1, 922.0 | 7120 | 19.2 |
| 80 | 2147 | 0.66 | -7.73, 7.29 | 276.0, 283.8 | (results.json) | 12574 | 23.3 |

By final state at n = 60 (300 K, /s): 59P1/2 689, 59P3/2 1331, 60P1/2 619, 60P3/2 1313; next manifolds 58P3/2 222,
61P3/2 183; P1/2 lines at -20.67 and +16.99 GHz. p_c per gate (I_r = 0.1925 T, Omega T/2pi = 1.215) at n = 60:
59P1/2 1.61e-4, 59P3/2 3.11e-4, 60P1/2 1.45e-4, 60P3/2 3.07e-4 at Omega/2pi = 1 MHz (total resonant 9.2e-4);
five times smaller at 5 MHz (1.85e-4). Per us of Rydberg time: 3.95e-3 at n = 60.
The resonant fraction is 0.66-0.68 for all n (cf. 0.68 for Rb 50S-60S, JILA); the n = 60 lifetimes at 300 K are
a quarter of the 0 K values, i.e. BBR dominates the contaminant lifetime, which matters for item 3.

**Recommendation (rule above).** Lifetime >= 100 us: n >= 52. R_ex(1 MHz) in 10-25 um: all n. Band ceiling 40 GHz:
n >= 50; ceiling 20 GHz: n >= 60. **Recommended n = 60** if the noise source reaches only ~20 GHz (lines at
16.99-20.67 GHz; tau_P ~ 143-153 us; R_ex = 15 um, central in the owner's 5-20 um range); n = 52-55 if it reaches
~35 GHz. The preference for the lowest admissible n is an opinion (blockade radius vs trap spacing, stray-field
sensitivity rising steeply with n), not a computed criterion.
