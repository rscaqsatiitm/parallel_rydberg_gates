# Handover (received 2026-11-20, kept as the project charter)

This file records the owner's handover. Its claims carry the status labels given in its Section 1;
none is established by being written here. Section 3 numbers are not results (Section 7).

## 0. Task
Determine, by theory and simulation only, whether the following is a PRL-level result:
room-temperature blackbody radiation transfers a Rydberg nS atom to a neighbouring P state during a
gate pulse; that contaminant interacts with every Rydberg atom nearby through resonant dipole
exchange (1/R^3). What correlated error does one contaminant cause in a dense parallel CZ layer, as a
function of gate speed, pair spacing, principal quantum number and temperature, and what does this do
to the logical error of a code whose gate-zone neighbours are also code neighbours?
Staged with kill tests; stop at the first that fires and report. A clean negative result is
acceptable. No paper draft before Gate 2.

## 1. Status of the starting claims (as handed over)
Read partly (fetch tool, not PDF) on 2026-11-20: arXiv:2611.06613 (Zhang et al., JILA; 87Rb, up to
5 x 14 atoms at 5 um, dressing, 50S and 60S; Gamma_ava ~ N P_Ryd Gamma_BBR^trig; fraction of BBR
decays into (n-1)P and nP 0.686 (50S) and 0.677 (60S) at 300 K; facilitation range ~13 um for 60S);
arXiv:2304.05420 (Evered 2023: 53S, 2pi x 4.6 MHz, CZ 99.5 %, small growth of neighbour covariance);
arXiv:2604.25987 (Evered 2026: 53S, ~2pi x 17 MHz peak, loss 0.054(2) % per atom per CZ, no
large-scale correlated events).
Unverified (model-generated summary): sparse 8-site array in 2604.25987 to reduce P-state decay
effect; ~80 us lifetime; 2304.05420 Methods covariance vs gates and neighbour class; no shot of 5053
with >= 18 errors on 30 sites; the Discussion and references of 2611.06613.
Literature: two web searches only, no prior computation found; not evidence of absence.

## 2. Lessons from the parent repository (rscaqsatiitm/Neutral-atom-QC)
(1) Literature check first. (2) No estimate quoted as a result until both the microscopic calculation
and the circuit-level simulation exist.

## 3. Exploratory estimate (crude, upper-biased, unreviewed; reproduce, then distrust)
ARC 3.10.2, 300 K. Rb 53S: lifetime 73 us, BBR rate to nearest P manifolds 5.0e3 /s (0.68 of BBR);
contaminant per atom per gate 5.1e-4 (4.6 MHz), 1.4e-4 (17 MHz); R_c 13 um, 8.5 um.
Cs 60S: 94 us, 4.0e3 /s (0.67); 9.3e-4 (2 MHz), 3.7e-4 (5 MHz); R_c 20 um, 15 um.
Assumptions: Omega T = 7.612, integrated Rydberg population 2.947/Omega per atom (recalled,
unverified); C3 = (radial m.e.)^2/3 with largest S-P channel; R_c from exchange phase 1 rad in half a
gate; neighbour error sin^2(phase), neighbour in Rydberg state for the whole half gate.
Correlated error per atom per gate (pitch 8.6x12.1 / 5x5 / 20x20 um): Rb 4.6 MHz 3.2e-3 / 1.5e-2 /
1.8e-4; Rb 17 MHz 2.4e-4 / 1.6e-3 / 3.7e-6; Cs 2 MHz 1.5e-2 / 6.7e-2 / 3.5e-3; Cs 5 MHz 3.3e-3 /
1.4e-2 / 2.9e-4. Known defect: 3.2e-3 exceeds what the 2023 experiment could have missed; likely
over-estimate by 3 to 10. The 8.6 x 12.1 um pitch is a figure reading, not a printed value.
Suggested scaling (to be derived, not assumed): error ~ Gamma_BBR(T) C3^(2/3) tau^(5/3) / a^2.
The reproduction script is in `experiments/E00_reproduce_handover_estimate/`.

## 4. Rules: see docs/RULES.md.

## 5. Stages
S0 Literature (K1: fires if a paper computes the inter-pair contaminant error in parallel CZ gates or
simulates its effect on a code). Deliverables: prior-work table; registered parameter file.
S1 Microscopic calculation (K2: fires if correlated error per atom per gate at published spacing is
< 1e-5 for every published configuration). One gate pair with the published pulse plus one contaminant
in n'P at (R, theta) appearing at a random time; full Zeeman and fine structure; outputs E(R, theta)
(Pauli, leakage, loss separately), contaminant probability per atom per gate; scaling law with domain.
S2 Confrontation with experiment (K3, Gate 1): pre-registered, no fitted parameter: neighbour
covariance vs number of CZ gates and neighbour class (2304.05420); bound on large correlated events
(2604.25987, sparse and dense); N and P_Ryd scaling of the avalanche trigger (2611.06613, trigger only).
S3 Logical consequence (Gate 2): Stim, surface code and one qLDPC code, correlated multi-pair events
on a real gate-zone layout vs independent model with equal marginals; suppression vs spacing, gate
time, temperature; non-neighbour layouts; laser-power cost. Reuse with attribution
`atomclock/qec/repetition.py::extra_z_flips` and `atomclock/noise/correlated_loss.py` from the parent.
S4 Letter draft only after Gate 2.

## 6. Report at each gate: what was shown (numbers, intervals, provenance); what failed; three open
problems; recommendation (continue / retarget with journal / stop).

## 7. Do not: claim the mechanism is new; extend dressing avalanche results to pulsed gates without
calculation; tune inputs or widen tolerances after a run; use Section 3 numbers as results; contact
authors (draft questions for the owner instead).
