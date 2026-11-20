# E03. Independent check of the S-P dipole-dipole matrix (Rule 6)

Pre-registered 2026-11-20 before either side was run.

**Design.** Route 1 (in-house, `src/prg/atomic.py` + `ours.py`): ARC 3.10.2 radial matrix elements,
own Wigner-Eckart and dipole-dipole operator. Route 2 (`pi_reference.py`, written by a separate agent
that did not see route 1): `pairinteraction` 2.7.0. Same physical specification: Rb87, basis
{53S1/2 (x) 52P_J, 52P_J (x) 53S1/2}, J = 1/2, 3/2 (48 states), dipole-dipole only, B = 8.5 G along z,
theta in {0, 90} deg, R in {6, 10, 20} um; eigenvalues relative to |53S 1/2; 52P3/2 1/2>.
Shared layers: none in code. Both rest on quantum-defect data for Rb (ARC and pairinteraction use
their own databases and model potentials; both ultimately draw on the same spectroscopic
literature), so a common error in quantum defects would not be detected.

**Verdict rule.** PASS if every eigenvalue agrees within max(2 % of its distance from the nearest
asymptote, 5 kHz). A disagreement only in the overall scale of the coupling (all splittings in the
same ratio) is reported as a radial-matrix-element difference with its size.

## Result
(appended after the run)
