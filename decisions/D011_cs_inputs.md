# D011. Inputs for the caesium synthetic-bath predictions (Addendum 2)

Date: 2026-11-21. Tasks C1-C5 (experiments E11-E15). No published parameter of the owner's new Cs laboratory
exists; every laboratory parameter below is ASSUMED and enters only as a declared value or range. Atomic data:
ARC 3.10.2 `Caesium()` (quantum defects, radial matrix elements, lifetimes, Einstein coefficients), the only
route available (an independent Cs quantum-defect route would need Cs spectroscopic papers not yet read; flagged).

1. **States.** Probe / gate state nS1/2 mJ = +1/2 of 133Cs, n = 50-80. Hyperfine structure of Rydberg states neglected
   (as D004). Contaminant manifolds n' = n-1 and n (the two P manifolds nearest nS, as for Rb).
2. **Gate exposure.** Contaminant probability per gate p_c = Gamma_BBR x I_r with I_r/T = 0.1925 and
   Omega T/2pi = 1.215, i.e. the time-optimal pulse shape of Evered 2023 (E02) transferred to Cs. This is a property
   of the pulse shape, not of the species; the owner's gate may differ. Omega/2pi in {1, 5} MHz: ASSUMED.
3. **Field.** B = 5 G along z (quantization axis), ASSUMED; B = 20 G as a sensitivity for one kernel slice.
4. **Geometry.** Probe and contaminant separated by R at polar angle theta from B; kernel at
   theta in {0, 30, 54.74, 90} deg.
5. **Deterministic contaminant.** Prepared from nS1/2 mJ = +1/2 by a microwave pulse into
   n'P3/2 mJ = +3/2 (sigma+) or n'P1/2 mJ = +1/2 (pi); both n' = n-1 and n. The preparation pulse itself is not modelled.
6. **Bath.** Synthetic noise of effective temperature T_eff in a band [f_lo, f_hi] added to the 300 K blackbody:
   mean photon number per mode n(nu) = n_Planck(nu, T_eff) inside the band, n_Planck(nu, 300 K) outside.
   Two bands: "narrow" covering the four lines nS -> (n-1)P_J, nP_J with 20 % margin; "broad" 1-100 GHz.
   Isotropic and unpolarised unless stated (the polarised, single-direction case is item 3, DV3).
7. **Array for the delay-law test (item 4).** 2-10 atoms on a line with spacing a in {5, 10} um, ASSUMED; contrast
   C in {0.90, 0.95} (owner's numbers).
8. **Quench beams (item 5).** Gaussian waist w in {20, 100} um, ASSUMED, to give powers; required removal: 95 %
   of the n'P population in 1 us (rate >= 3.0 /us).
