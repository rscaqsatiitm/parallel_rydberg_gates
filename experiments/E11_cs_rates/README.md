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
