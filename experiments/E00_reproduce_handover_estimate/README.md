# E00. Reproduce the handover's exploratory estimate (Section 3)

Pre-registered 2026-11-20, before the run. Task S1 (run only after the K1 verdict).

**Purpose.** Check that the Section 3 tables follow from the Section 3 script with ARC 3.10.2. This
is a reproduction of a crude estimate, not a result. No number from it enters any later computation.

**Design.** Run `handover_estimate.py` (verbatim copy of the handover script, only a `__main__`
guard and print formatting unchanged) with ARC-Alkali-Rydberg-Calculator 3.10.2, Python 3.13.

**Expectation.** 300 K lifetimes 73 us (Rb 53S) and 94 us (Cs 60S); BBR rate to the nearest P
manifolds 5.0e3 /s and 4.0e3 /s with fractions 0.68 and 0.67; the 12 correlated-error entries of
the second table to the two significant figures printed.

**Verdict rule.** REPRODUCED if every printed quantity agrees with the handover to the printed
precision (rounding of the last digit allowed). Otherwise NOT REPRODUCED, and each discrepancy is
listed. Either outcome is recorded; the estimate remains untrusted in both cases.

## Result
(appended after the run)
