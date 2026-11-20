# D004. Microscopic model of a gate pair perturbed by one contaminant

Date: 2026-11-20. Task: S1. Choices that no source fixes, with reasons.

1. **Atoms.** Gate atoms A, B (sites separated by d, sourced), contaminant C at vector r_C. Atom basis:
   A, B: {|0>, |1>, nS1/2 mJ = +-1/2, n'P_J mJ (J = 1/2, 3/2; 6 states)}; C: {nS1/2 (2), n'P_J (6)}.
   One contaminant manifold n' per run (n' = n-1 or n). Reason: an exchange with C in n'P is resonant
   only for final P states in the same n' manifold; other manifolds are detuned by >= several GHz
   while the couplings at R >= 1.7 um are <~ 1 GHz at most for the intra-pair pair and <~ 10 MHz for
   R >= 6 um, so their second-order effect is < 1e-3 of the resonant one at R >= 6 um. The intra-pair
   S-P coupling (~ GHz at 1.7-2 um) is resonant within the manifold and kept exactly.
2. **Interactions.** First-order electric dipole-dipole between every S-P atom pair (A-B, A-C, B-C),
   full Zeeman and fine structure, field along a chosen quantization axis, arbitrary geometry. S-S
   pairs: diagonal van der Waals shift C6/R^6 with C6 fixed by the sourced blockade (450 MHz at 2 um for
   2023; 950 MHz at 1.73 um for 2026), applied to all S-S pairs including C after an exchange. P-P and
   S-P second-order (vdW) terms neglected (first-order term dominates for S-P; P-P first order is zero
   and the second order is <~ the S-S value). Ground-Rydberg interactions neglected.
3. **Contaminant states.** Created by BBR from nS1/2 mJ_r into n'P_J mJ' with weights from ARC
   rates (300 K) per (n', J) split over mJ' by squared Clebsch-Gordan coefficients (isotropic BBR).
   BBR transitions into manifolds other than (n-1)P and nP are not modelled (they have smaller
   transition dipoles to nS; consequence: epsilon is a lower bound in that respect, by at most the
   untreated branching fraction, 0.32 at 53S, if those contaminants were as harmful).
4. **Laser.** Couples |1> to nS1/2 mJ_r only, with the published phase/amplitude profile. Spurious
   coupling to the other mJ, scattering, Doppler and noise are omitted: they are part of the
   uncorrelated budget and cancel in the difference we compute (the error is always reported as
   the contaminant-induced increment over the same model without contaminant).
5. **Error measure.** For each contaminant initial state, Kraus operators K_e = P_comp <e|U|c0> on the
   pair's computational space; F_e = (1/16) sum_e |Tr(U_CZ^dag K_e)|^2 with U_CZ the ideal CZ times the
   single-qubit Z phases that maximise fidelity without contaminant (fixed once per pulse). Leakage
   L = 1 - (1/4) sum_e Tr(K_e^dag K_e) (pair population left outside {|0>,|1>}: Rydberg S or P, which the
   traps convert to loss, per Evered 2023/2026). Pauli-type part = 1 - F_e - L. Contaminant mJ' and
   field orientation averaged or reported as a range as stated in each experiment README.
6. **Field orientation.** Not given relative to the array in either Evered paper. Three cases are run:
   B along the row axis, B in-plane perpendicular to the rows, B normal to the plane. Reported as a range.
7. **Motion.** Atoms frozen during a gate (traps off for a few hundred ns; thermal motion ~0.1 um/us
   at tens of uK gives < 0.03 um per gate). Between layers motion is a Stage 2 question.
