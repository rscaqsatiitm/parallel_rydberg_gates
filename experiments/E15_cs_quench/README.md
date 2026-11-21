# E15. Quench transitions that remove n'P contaminants within 1 us (Cs, n' = 59, 60; Addendum 2 item 5)

Pre-registered 2026-11-21 before the run. Task C5. Inputs D011 item 8. COMPUTED with ARC 3.10.2 (energies, radial
matrix elements, lifetimes); powers DERIVED with an ASSUMED beam waist.
**Candidates.** Optical coupling of n'P_J (n' = 59, 60) to a short-lived low-lying level k in {6S1/2 (ground),
7S1/2, 8S1/2, 9S1/2, 5D3/2, 5D5/2, 6D3/2, 6D5/2, 7D3/2, 7D5/2}, which decays to the ground manifold.
**Requirement.** Removal of 95 % of the n'P population within 1 us: rate Gamma_rem >= 3.0 /us. For a two-level
n'P - k system with k decaying at Gamma_k, the slow eigenvalue is Gamma_rem = Gamma_k / 2 - Re sqrt(Gamma_k^2 / 4 - Omega^2);
if Gamma_k / 2 < 3.0 /us the requirement cannot be met by that level alone (reported as such). The ground state 6S1/2
has no decay: quench by stimulated emission is a coherent pi pulse, m-selective, reported separately.
Omega uses the strongest Zeeman component (stretched, angular factor from atomic.py dipole_q).
Intensity I = c eps0 (hbar Omega / d)^2 / 2, peak power P = I pi w^2 / 2 for w in {20, 100} um.
**Reported for each candidate:** wavelength (vacuum, nm), radial and stretched dipole elements, Gamma_k, Omega required,
power at each waist; whether the use of that transition as a quench is reported in a source read in this project
(SOURCED with quote) or not (UNSOURCED); the separation between the n' = 59 and 60 lines (one laser or two).
**Expectation.** P -> nS / nD lines from n' ~ 60 to k = 7S, 6D, 7D lie in the visible / near-IR (~500-1200 nm) with
radial elements ~1e-2 a0, so Omega ~ 2pi x 1 MHz needs mW to W depending on waist; 5D (lifetime ~ 1 us) is expected to
fail the requirement alone; no candidate is expected to be SOURCED as a quench for Cs in the literature read so far.
**Verdict rule.** None (prediction).

## Result
(appended 2026-11-21; run.py -> output.txt, results.json; sources literature/notes/quench_sources.md, 5 quotes verified)

**Results (COMPUTED wavelengths, matrix elements and lifetimes; DERIVED Omega and powers; ASSUMED waists).**
Removal of 95 % of the n'P population in 1 us (rate 3.0 /us), strongest Zeeman component, n' = 59 (60 within 0.1 %):

| Quench (n'P3/2 -> k) | lambda (nm) | radial (a0) | Gamma_k (/us) | Omega/2pi needed (MHz) | P at w = 20 um | P at w = 100 um |
|---|---|---|---|---|---|---|
| -> 7S1/2 | 779.1 | 0.0081 | 20.7 | 1.16 | 0.31 mW | 7.8 mW |
| -> 6D5/2 | 1144.3 | 0.0136 | 16.5 | 1.01 | 0.07 mW | 1.8 mW |
| -> 6D3/2 | 1138.7 | 0.0131 | 16.4 | 1.01 | 0.76 mW | 19 mW |
| -> 7D5/2 | 1886.1 | 0.0271 | 10.9 | 0.77 | 0.01 mW | 0.26 mW |
| -> 8S1/2 | 1417.7 | 0.0149 | 11.1 | 0.79 | 0.04 mW | 1.1 mW |
| -> 9S1/2 | 2242.1 | 0.0239 | 6.2 | 0.49 | 0.006 mW | 0.16 mW |
| -> 5D3/2, 5D5/2 | 592.7, 596.2 | 0.004 | 1.04, 0.75 | not possible | | |
| -> 6S1/2 (stimulated emission) | 318.8 | 0.0034 | 0 | 0.50 (coherent pi, m-selective) | 0.34 mW | 8.4 mW |

n'P1/2 needs 1.5-10x more power for the same k (smaller stretched element, results.json). The 59P and 60P lines via a
given k are 76 pm (7S) to 164 pm (6D5/2) apart (~38 GHz at 779 nm): a single-frequency laser quenches one manifold;
both resonant manifolds and both J need four lines (cf. Boulier 2017: "at least four significant pollutant states").
5D fails because its lifetime (~1 us) caps the removal rate at Gamma_k/2 < 3 /us.
**Provenance status.** The technique (laser coupling of contaminants to lower-lying short-lived states) is SOURCED as a
proposal (Boulier et al. 2017, arXiv:1709.02460); a laser quench is cited by Zeiher et al. 2016 (arXiv:1602.06313) via a
reference not read here. Every specific Cs transition, wavelength and power above is UNSOURCED as a quench (computed
here, not reported in any source read). Laser availability at these wavelengths and the effect of the quench light on
probe atoms in 60S and on ground-state qubits (light shifts) are not assessed. The expectation (powers mW to W) was
pessimistic: with a 20 um waist all decaying candidates need <= 1 mW.
