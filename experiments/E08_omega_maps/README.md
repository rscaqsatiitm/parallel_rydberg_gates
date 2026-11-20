# E08. Gate-speed dependence of the contaminant error maps

Pre-registered 2026-11-20 before the run. Task S3.

**Design.** As E02 (Rb 53S, B = 8.5 G, d = 2 um, blockade 450 MHz, the Evered 2023 time-optimal
phase profile with Omega T/2pi = 1.215 held fixed) at Omega/2pi in {2.3, 9.2, 18.4} MHz (0.5x, 2x, 4x
the published 4.6 MHz). B along x and z; alpha in {0, 90} deg; R in {4, 6, 8, 10, 12, 14, 17, 20, 25,
30, 40} um; n' = 52, 53. E_full and E_same (t_on grid of 6 points weighted by p_r(t) of that pulse);
I_r and p_c per Omega. Control: at 4.6 MHz, the 6-point E_same agrees with E02's 12-point value within
10 % at R = 10 and 20 um (B along z, alpha = 0).
**Expectation (scaling, DERIVED in DV3 to be written):** in the perturbative tail E ~ (2 pi V T)^2 with
V = C3/R^3, so at fixed R, E_full ~ Omega^-2; the half-error radius scales as Omega^-1/3; p_c ~ Omega^-1.
Hence, if the floor is tail-dominated, eps_floor ~ Omega^-3; if dominated by atoms inside the
half-error radius, ~ Omega^-1 x (number of atoms inside R_1/2(Omega)).
**Verdict rule.** Tail exponent check as E02 (slope -6.0 +- 0.3 on [25, 40] um) at each Omega; the
Omega^-2 scaling of E_full at R = 30 um holds within 20 % between 2.3 and 18.4 MHz: PASS/FAIL each.

## Result
(appended 2026-11-20; raw res_<Omega>.json committed; analysis analyse.py -> analysis_output.txt,
floor floor_omega.py -> floor_output.txt; runtimes 560 s, 1437 s, 2297 s for 18.4, 9.2, 2.3 MHz)

**Control** (pre-registered, 6-point vs 12-point t_on grid at 4.6 MHz): running at time of this commit; result appended below.

**Verdict 1, tail exponent** (slope of ln E_full vs ln R on [25, 40] um, B x/z, alpha 0/90): PASS at all
four Omega; slopes -5.96 to -6.04.
**Verdict 2, Omega^-2 at R = 30 um**: E_full(2.3 MHz)/E_full(18.4 MHz) = 58.7-59.2 against 64, i.e.
q/64 = 0.92; PASS (within 20 %) for all four (B, alpha) combinations. The 8 % shortfall is not
diagnosed; a candidate is the residual R-dependence beyond lowest order at 2.3 MHz (E_full(20 um) =
0.19 for B x, alpha 0, not yet perturbative).

**Further results (SIM, 300 K, BBR rates of E02; not verdicts):**
(i) p_c = 5.07e-4, 2.53e-4, 1.27e-4, 6.35e-5 per atom per CZ at 2.3, 4.6, 9.2, 18.4 MHz;
p_c x Omega constant to 0.2 % (I_r/T = 0.1925 is fixed by the pulse shape), so p_c ~ Omega^-1 exactly.
(ii) Half-error radius (B z, alpha 0, log-interpolated): 12.8, 10.4, 8.5, 6.8 um; over a factor 8 in
Omega it shrinks by 1.88 (Omega^-1/3 would give 2.0).
(iii) E_same/E_full at 30 um: 0.39 (2.3 MHz) to 0.42-0.45 (18.4 MHz).
(iv) Same-layer floor in the BLU25 zone (D008 normal spacing, E07 procedure unchanged, ranges over
pitch assignment, pair axis and field direction): 2.8-4.1e-3 (2.3 MHz), 6.9e-4-1.08e-3 (4.6 MHz;
identical to E07, method check), 1.35-3.07e-4 (9.2 MHz), 2.3-7.6e-5 (18.4 MHz). Local exponent
d ln eps / d ln Omega from -1.8/-2.0 at low Omega to -2.0/-2.6 between 9.2 and 18.4 MHz, i.e. moving
from the "atoms inside R_1/2" regime (-1 x number inside, here about -2) towards the tail regime (-3)
as expected in the pre-registration.
(v) DERIVED (log interpolation between 9.2 and 18.4 MHz): the floor reaches 1e-4 per CZ at
Omega/2pi ~ 10-16 MHz in the BLU25 geometry at 300 K, versus the published 4.6 MHz.

**What this does not include.** Faster gates at fixed n change other error budgets (laser scattering
from the intermediate state, finite blockade 450 MHz / Omega, pulse distortion); these are outside the
model and would need sourced numbers before any "required Omega" is quoted as a design target.
