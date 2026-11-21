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
