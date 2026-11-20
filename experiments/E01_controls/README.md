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
(appended 2026-11-20; scripts run.py, run_exchange.py, run_null.py in this directory)

1. Planted pulse. Blockade 450 MHz: CZ fidelity 0.999984 (PASS, >= 0.999). Blockade 1e5 MHz: 0.9999936,
   **FAIL** against the pre-registered >= 0.99999 by 3.6e-6. Not discretisation (600 vs 2400 steps:
   0.99999359 vs 0.99999363). Re-optimising Omega T/2pi on [1.2145, 1.2155] gives at most 0.9999944
   (at 1.2153), so the residual is not the 3-digit rounding of Omega T alone. Untested hypothesis:
   4-digit rounding of A, omega, phi0, or a convention difference. Impact: none on the reported
   quantities, which are increments over the same pulse without contaminant (D004 item 4).
2. Convergence. Increment at R = 8 um (contaminant 52P3/2 mJ=3/2, along the row, B normal):
   (err, leak, Pauli) = (0.99931661, 0.54130106, 0.45801555) at 600 steps, (0.99931664, 0.54130038,
   0.45801625) at 1200. Relative change < 2e-6. PASS.
3. Null. R = 200 um: increments (1.3e-8, 1.3e-8, 0). PASS (< 1e-6). Note: the first version of the
   metric reported the gate's own baseline leakage (1.6e-5); the incremental definition required by
   D004 item 4 was then implemented in `contaminant_increment` before any production run.
4. Corrupted input. Sign-flipped dy: Hermiticity assertion fired. Phase modulation removed: CZ
   fidelity 0.327. PASS.
5. Exchange. Population of |53S1/2 1/2; 52P3/2 1/2> at R = 10 um along B over 0-0.5 us, model vs
   independent dense diagonalisation of the two-atom S(x)P + P(x)S dipole-dipole matrix: max
   difference 1.2e-13. PASS. (A first attempt disagreed because the control script placed the
   contaminant 12 um from A instead of 10 um; the script, not the model, was corrected.)
   Shared layers of the two routes: `dipole_q` (ARC radial elements + Wigner-Eckart) and level
   energies. Independent: embedding in the 3-atom space, B-frame rotation, Cartesian vs spherical
   form of the dipole-dipole operator, propagator. An independent check of `dipole_q` itself against
   `pairinteraction` is still required (Rule 6) and is scheduled as E03.
