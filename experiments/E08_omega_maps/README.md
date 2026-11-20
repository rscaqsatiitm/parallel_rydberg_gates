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
