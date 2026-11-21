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

**Amendment (2026-11-20, before route 2 reported):** the basis has 2 x 6 x 2 = 24 states, not 48; the
agent brief carried the same error. Verdict rule unchanged.

## Result
(appended 2026-11-20)
**BLOCKED.** Route 2 could not be run: pairinteraction 2.7.0 needs its Rb database tables, which it
downloads from GitHub. In this container the download failed (session GITHUB_TOKEN rejected with 401
by api.github.com; anonymous rate limit exhausted at three reset times; attaching the data repository
pairinteraction/database-sqdt was refused by the session's permission system). The route-2 script
`pi_reference.py` is syntax-checked but never run. No route-2 numbers exist. Route 1 output: `ours.json`.
Unblock: provide the Rb tables in /root/.cache/pairinteraction/database/tables, or GitHub access to
that repository, then run `python pi_reference.py` here and compare under the rule above.
Substitute independent route: E03b (Coulomb-approximation radial integrals without ARC).

**Re-attempt (2026-11-21, Addendum 3 item 5): still BLOCKED.** `pairinteraction database download Rb` fails with
"Failed obtaining the rate limit: status code 401. The download of database tables is disabled."; the GitHub API
returns 403 for the data repository's releases. No route-2 numbers exist; E03b remains the independent route.
