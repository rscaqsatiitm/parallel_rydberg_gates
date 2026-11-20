# E01. Controls for the three-atom gate model (Rule 5)

Pre-registered 2026-11-20 before the run. Task S1.

**Design and verdict rules.**
1. *Planted answer (pulse).* Evered 2023 time-optimal pulse (registry `evered23.pulse_params`,
   `evered23.OmegaT_over_2pi`), Omega/2pi = 4.6 MHz, blockade 450 MHz at 2 um, contaminant decoupled.
   Expectation: CZ fidelity (max over single-qubit Z phase) >= 0.999 (finite blockade and the extra
   Rydberg levels allow a small deviation; the paper calls the pulse exact for perfect blockade).
   Also with blockade 1e5 MHz: >= 0.99999. PASS if both hold.
2. *Convergence.* nsteps 600 vs 1200 changes the contaminant-induced error at R = 8 um by < 2 %. PASS/FAIL.
3. *Null.* Contaminant at R = 200 um: contaminant-induced error < 1e-6. PASS/FAIL.
4. *Corrupted input caught.* Dipole operator with a deliberately wrong sign on dy: Hermiticity
   assertion must fire. Single-qubit fidelity check with the pulse phase amplitude set to 0: CZ
   fidelity must drop below 0.9. PASS if both are caught.
5. *Planted answer (exchange).* Two isolated atoms (gate atom held in nS mJ_r, no laser), contaminant
   in n'P at distance R along B: population transfer must oscillate at the frequency given by the
   eigenvalues of the 2-atom dipole-dipole matrix computed independently with dense diagonalisation.
   PASS if the propagated and eigen-decomposed populations agree to 1e-8.

## Result
(appended after the run)
