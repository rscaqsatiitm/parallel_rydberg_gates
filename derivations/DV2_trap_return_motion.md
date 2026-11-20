# DV2. Motion of a contaminant when the tweezers return

**Header (Rule 7).**
- Assumptions: (B1) tweezers at lambda = 852 nm (BLU25, EVE26; registry pending), linear polarisation,
  Gaussian beams of waist w (not sourced; range in D007) and ground-state depth U_g (EVE23: ~1 mK;
  BLU25 not given; D007); (B2) the Rydberg (n'P) atom's light shift is that of a free electron plus the
  Rb+ core: U_R(r) = -(alpha_e + alpha_core)/alpha_g * U_g(r) with U_g(r) < 0 the ground-state trap
  potential; alpha_e = -e^2/(m_e omega^2) (ponderomotive; n-independent when the
  Rydberg orbit (~0.3 um at n = 53) is small compared with the waist; the orbit-averaging correction
  is O((r_orbit/w)^2) ~ 0.1 and is neglected, flagged); (B3) classical motion; atom starts with the
  ground-state thermal distribution of the trap (EVE23 ~10 uK) at the moment the traps return
  (free flight during the few-hundred-ns gate neglected); (B4) photoionisation by tweezer light and
  BBR transfer to other states are not included (both only shorten the harmful lifetime; omission is
  conservative for the size of the effect).
- Conventions: atomic units for polarisabilities; U > 0 repulsive.
- Domain: n'P with n' ~ 52-53, 852 nm, depths 0.3-3 mK.
- Dependencies: ARC 3.10.2 DynamicPolarizability(Rubidium87, 5S1/2), basis n <= 30.

**Numbers (COMPUTED / DERIVED, 2026-11-20).** ARC: alpha_g(5S1/2, 852 nm) = 2071.5 a.u. (scalar),
alpha_core = 9.08 a.u. Free electron at 852 nm: omega = 0.053478 a.u., alpha_e = -1/omega^2 = -349.7 a.u.
Ratio U_R / |U_g| = (349.7 - 9.1) / 2071.5 = 0.164: the contaminant sits on a repulsive hill of height
0.164 U_g, i.e. 164 uK x k_B for U_g = 1 mK.
Asymptotic speed after rolling off its own hill (energy conservation, independent of w):
v_inf = sqrt(2 * 0.164 U_g / m) = 0.177 m/s = 0.177 um/us at U_g = 1 mK (scales as sqrt(U_g)).
Escape time from the hill top for an inverted harmonic potential, curvature kappa^2 = 4 * 0.164 U_g /(m w^2):
t_esc ~ kappa^-1 ln(w / rho0), rho0 the initial thermal displacement. For w = 1 um, U_g = 1 mK:
kappa^-1 = 4.6 us; rho0 = sqrt(kT / (m omega_r^2)) with omega_r^2 = 4 U_g/(m w^2): rho0 = w sqrt(kT/4U_g)
= 0.05 um at 10 uK, so t_esc ~ 4.6 us x ln(20) ~ 14 us.
Order of magnitude: a contaminant is ~ v_inf (t - t_esc) ~ 6 um from its site at t = 50 us and ~ 15 um at
100 us. This is the same window over which BLU25 ED Fig. 6g recovers, so motion, not decay
(tau_P ~ 100 us), may set the recovery. The full calculation (trajectories through the tweezer array,
whose other sites are repulsive hills of the same height) is E06.

## Questions for the independent check (neutral wording)
1. For a free electron in a linearly polarised field of angular frequency omega, what is the
dynamic polarisability, and what is its value at 852 nm in atomic units? 2. Given a Gaussian repulsive
potential of height U and waist w, what is the speed at infinity of a particle released at rest near
the top, and the e-folding time of its displacement near the top? 3. Is the orbit-averaging correction
for an n = 53 P state in a 1 um waist beam small?
