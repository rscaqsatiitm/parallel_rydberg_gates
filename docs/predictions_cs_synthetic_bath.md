# Frozen predictions: synthetic-bath contaminant experiment in caesium (Addendum 2)

Frozen 2026-11-21, before any data exist, in the commit carrying tag `cs-predictions-v1`. Nothing below may be edited
after data are taken; later corrections go in a new, dated section or a new tag. Every number has a provenance:
COMPUTED (ARC 3.10.2), SIM (simulation in this repository), DERIVED (shown), ASSUMED (D011, laboratory parameters the
owner has not supplied), SOURCED (quote verified in literature/notes). Details, controls and failures: E11-E15 READMEs,
DV3, D011.

## Assumed laboratory parameters (D011; replace with the owner's values and re-run before comparing)
133Cs, probe state 60S1/2 mJ = +1/2; B = 5 G; gate exposure with the time-optimal pulse shape (I_r/T = 0.1925,
Omega T / 2pi = 1.215) at Omega/2pi = 1 MHz; atoms on a line perpendicular to B; spacing 5 or 10 um; contrast 0.90-0.95;
quench beam waist 20 or 100 um. Atomic data from a single route (ARC); no independent Cs quantum-defect check.

## 1. Contaminant creation, lifetimes, frequencies; choice of n (E11, COMPUTED)
- Resonant transfer (n-1)P + nP is 0.66-0.68 of all BBR transfer out of nS for n = 50-80 (300 K).
- n = 60, 300 K, per gate at Omega/2pi = 1 MHz: p_c = 1.61e-4 (59P1/2), 3.11e-4 (59P3/2), 1.45e-4 (60P1/2), 3.07e-4 (60P3/2);
  total 9.2e-4; at 5 MHz five times smaller. Per us of Rydberg time: 3.95e-3.
- Contaminant lifetimes at 300 K: 59P3/2 143 us, 60P3/2 149 us (P1/2: 147, 153 us); at 0 K 537-633 us.
- Lines a noise source must cover at n = 60: 60S1/2 -> 59P1/2 20.67 GHz, -> 59P3/2 19.41 GHz, -> 60P1/2 16.99 GHz,
  -> 60P3/2 18.18 GHz. (n = 52: 26.9-32.9 GHz; n = 70: 10.4-12.6 GHz.)
- **Recommendation: n = 60** if the noise source reaches ~20 GHz; n = 52-55 if it reaches ~35 GHz. Preference for low n
  is an opinion (blockade radius, stray-field sensitivity).
- Known limitation: per-state rates within n' = n +- 20 sum to 0.95-0.98 of the total (pre-registered 2 % check FAILED).

## 2. Error kernel of a deterministic n'P contaminant (E12, SIM)
- Blockade (resonant pi pulse on the probe): near-step kernel; at Omega/2pi = 1 MHz, E_B > 0.9 inside 12-15 um (theta = 0)
  or 8-12 um (theta = 90 deg), < 0.05 beyond 20 um; crossover radius ~ Omega^-1/3.
- Ramsey: oscillatory in t at the exchange frequency (exactly |cos(2 pi C3 t / R^3)| for 59P3/2 +3/2 at theta = 0,
  C3 = 3669 MHz um^3); maximised over t in 0.1-20 us, E_R = 0.68-0.98 at R = 5, 10, 20 um for every state and angle.
- Contrast needed (3 sigma, N shots per setting): blockade at 1 MHz, C_min = 0.07-0.08 (N = 1e3) at 5 and 10 um
  (0.18-0.19 for P1/2 at theta = 90 deg); at 20 um not resolvable with N = 1e4 unless Omega/2pi <= 0.5 MHz. Ramsey with a
  scanned free-evolution time: C_min <= 0.10 (N = 1e3) at all three R. A contrast of 0.90-0.95 is ample.

## 3. Band-limited bath, T_eff = 300 K - 1e6 K (E13, SIM; DV3, DERIVED and independently checked)
- Linear: every bath rate in nbar exactly and in T_eff to ~h nu / 2kT_eff. p_c within 10 % of linear up to ~3e4 K
  (narrow band 13.6-24.8 GHz, 1 MHz gate): 9.2e-4 (300 K), 3.0e-2 (1e4 K), 8.7e-2 (3e4 K).
- Saturates: p_c -> 0.25 (1e5 K), 0.52 (3e5 K), 0.66 (1e6 K) narrow; broad band 1-100 GHz falls back to 0.27 at 1e6 K.
- Spreads to non-resonant states: after one gate, above ~1e5 K (narrow 0.7 % at 1e5, 19 % at 1e6 K; broad 7 %, 65 %);
  a contaminant held under the bath leaves the resonant manifolds with tau_res = 124, 60, 12, 1.3 us (narrow) and
  85, 13, 1.3, 0.14 us (broad) at 1e3, 1e4, 1e5, 1e6 K, against 150 us with the bath off.
- Coherent kernels of item 2 remain valid while the probe's bath transfer in the sequence is < 0.1: T_eff <~ 7e3 K for
  a 1 us sequence.
- Equivalence: a band-limited, single-direction, polarised field with spectral energy density matched to Planck
  (nbar = c^2 I_nu / 8 pi h nu^3) gives exactly the blackbody creation rate out of nS1/2 for linear or unpolarised light
  (correction factor 1 for each final J); circular light gives 0 / 1.5 (sigma+) and 2 / 0.5 (sigma-) into P1/2 / P3/2,
  1 summed. It is not equivalent for the onward rates of P3/2 contaminants (factors 0-3 by m and polarisation;
  1 after m-averaging) nor for the m' distribution of contaminants; the latter changes the m'-weighted blockade kernel
  by -2 % to +1.4 % at R = 10 um, theta = 0.

## 4. Delay law and shots (E14, SIM + DERIVED)
- eps(t) = eps(0) S_res(t); tau_res = 150 us with the bath off during the wait at all T_eff; with it on, as in item 3.
- Shots for a 10 % two-point test (t = 0, tau_res), C = 0.90, independent [fully correlated] probes:
  2 atoms at 5 um: 2.2e8 [4.4e8] at 300 K; 2.2e6 [4.4e6] at 3e3 K; 2.1e5 [4.1e5] at 1e4 K.
  10 atoms at 5 um: 4.8e6 [4.8e7] at 300 K; 4.9e4 [4.9e5] at 3e3 K. C = 0.95 halves these (factor 2.1).
- Valid (single contaminant) only for N_a p_c <= 0.1: 2 atoms up to ~1.6e4 K, 10 atoms up to ~3e3 K.
- Suggested operating point (opinion): narrow-band bath at ~1e4 K, 2-3 atoms at 5 um; the bath-off and bath-on
  scenarios then predict 150 us and 60 us.

## 5. Quench transitions (E15, COMPUTED wavelengths and matrix elements; DERIVED powers; ASSUMED waist)
95 % removal of n'P in 1 us, strongest Zeeman component, 59P3/2 (60P within 0.1 %):
-> 7S1/2 779.1 nm, 0.31 mW (w = 20 um) / 7.8 mW (100 um); -> 6D5/2 1144.3 nm, 0.07 / 1.8 mW; -> 8S1/2 1417.7 nm, 0.04 / 1.1 mW;
-> 7D5/2 1886.1 nm, 0.01 / 0.26 mW; -> 9S1/2 2242.1 nm, 0.006 / 0.16 mW; -> 6S1/2 (stimulated emission, coherent pi,
m-selective) 318.8 nm, 0.34 / 8.4 mW; -> 5D fails (lifetime ~1 us). Four lines are needed for 59P and 60P, J = 1/2 and 3/2
(59P/60P lines 76-164 pm apart). The quench concept is SOURCED as a proposal (Boulier et al. 2017, arXiv:1709.02460);
every specific Cs transition and power here is UNSOURCED as a quench. Light shifts on probes and qubits not assessed.

## What would falsify these predictions
(i) A blockade kernel crossover at 1 MHz outside 8-15 um at n = 60; (ii) p_c not linear in the injected noise power below
~1e4 K; (iii) bath-off contaminant survival with 1/e time outside ~120-180 us (ARC 143-153 us plus room-BBR spreading);
(iv) a polarised-field creation rate out of nS1/2 that differs from the isotropic rate at equal energy density by more
than the measurement error.
