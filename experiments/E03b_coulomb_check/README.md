# E03b. Independent route for the radial dipole matrix elements (substitute for blocked E03)

2026-11-20. Not pre-registered as a separate experiment: it substitutes the blocked E03, and the
comparison uses the E03 tolerance (2 %) transferred to the matrix elements. Written by a separate
agent without ARC and without access to src/ (NOTES.md: sources, 16 verified quotes, controls).

Route 2: Coulomb approximation, Numerov on a sqrt grid, quantum defects nS1/2 from Mack et al. 2011
(arXiv:1103.6221, 87Rb, Table I) and nP from Li et al. PRA 67, 052502 (2003) (85Rb, Table VI, table
read from the rendered page). Controls: hydrogen vs Gordon's formula, max relative error 5e-11; inner
cutoff 0.5-8 a0 changes results < 2.5e-5.

| | route 2 (a0) | ARC 3.10.2 (a0) | rel. diff | nu route 2 (GHz) | nu ARC (GHz) |
|---|---|---|---|---|---|
| 53S1/2-52P1/2 | 2612.23 | 2612.29 | 2.3e-5 | -28.2308 | -28.2310 |
| 53S1/2-52P3/2 | 2660.31 | 2660.38 | 2.6e-5 | -27.5078 | -27.5080 |
| 53S1/2-53P1/2 | 2884.35 | 2884.43 | 2.8e-5 | 24.9095 | 24.9096 |
| 53S1/2-53P3/2 | 2839.34 | 2839.42 | 2.8e-5 | 25.5903 | 25.5905 |

**Verdict: PASS** (agreement 3e-5, tolerance 2e-2). Shared layer: spectroscopic quantum defects
(ARC also uses the Li 2003 / Mack 2011 data, to be confirmed in ARC's source), so a common error in
those data would not be detected; the radial integration and core treatment are independent
(Coulomb approximation vs ARC's model potential). Together with E01-[5] (independent assembly of the
dipole-dipole operator), every layer of the S-P coupling except the quantum-defect data now has two routes.
