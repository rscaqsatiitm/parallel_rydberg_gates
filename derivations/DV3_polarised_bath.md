# DV3. Is a band-limited, single-direction, polarised noise field equivalent to a blackbody for BBR transfer rates?

**Header (Rule 7).**
- Assumptions: (C1) electric-dipole transitions between fine-structure levels |n l J m>, hyperfine structure
  neglected; (C2) the noise field is classical, stationary and broadband compared with every linewidth and Rabi
  frequency it produces (rate-equation regime: transition rate = (pi / (3 eps0 hbar^2)) |d|^2-weighted spectral energy
  density at the line, Fermi golden rule); (C3) the blackbody is isotropic and unpolarised with spectral energy
  density u_BB(nu, T) = (8 pi h nu^3 / c^3) nbar(nu, T), nbar = 1 / (exp(h nu / k T) - 1); (C4) the synthetic field has
  spectral energy density u_s(nu) inside a band and a fixed polarisation unit vector e (linear or circular) or a
  fixed propagation direction k with both transverse polarisations equally populated (unpolarised beam).
- Conventions: rates for absorption and stimulated emission i -> f; isotropic rate
  W_iso = (u / (3 eps0 hbar^2)) (pi) sum_q |<f| d_q |i>|^2 ... written below up to the common constant kappa.
- Domain: rate-equation regime; T_eff defined by u_s(nu) = u_BB(nu, T_eff) at each in-band line.
- Dependencies: Wigner-Eckart theorem; atomic.py dipole_q for numbers.

## Derivation
For a field with polarisation e and spectral energy density u at the line frequency, the golden-rule rate is
W_e(i -> f) = kappa u |<f| e* . d |i>|^2. For isotropic unpolarised radiation of the same u, averaging over directions
and polarisations gives W_iso(i -> f) = kappa u (1/3) sum_q |<f| d_q |i>|^2 (each Cartesian component weight 1/3).
Summing over the final Zeeman sublevels m_f of a level (n_f l_f J_f):
  sum_{m_f} |<f| e*.d |i>|^2 = sum_K (tensor of rank K = 0, 1, 2 built from e e*) x (rank-K multipole of state i).
The rank-0 part equals (1/3) |<J_f||d||J_i>|^2 / (2 J_i + 1) for any e, which is also the isotropic value. The rank-1
part (orientation) exists only for circular components and requires J_i >= 1/2; the rank-2 part (alignment) requires
J_i >= 1. Hence:
(R1) for an initial J_i = 1/2 state (nS1/2, nP1/2) in a pure m state, the total rate into a level J_f is the same for
     every polarisation e as for isotropic radiation of equal u, EXCEPT for the rank-1 term, which is nonzero for
     circular e when the initial state is oriented (|m = +1/2> is oriented). For linear e the rank-1 term vanishes and
     the correction factor is exactly 1. For circular e the factor differs from 1 and is computed numerically (E13).
(R2) for J_i = 3/2 (n'P3/2), both orientation and alignment contribute; correction factors depend on m_i and e and are
     computed numerically (E13); averaged over a uniform m_i distribution they are 1 (the rank > 0 terms average out).
(R3) the distribution over final m_f is never the isotropic one for a polarised field (e.g. linear e along B from
     |S1/2, +1/2> populates only m_f = +1/2).
(R4) a single-direction beam with both transverse polarisations equal (unpolarised beam along k) has
     e e* averaged = (1 - k k)/2, a rank-0 part 2/3 x 1/2 ... i.e. the same rank-0 weight as isotropic radiation for
     equal u plus a rank-2 part proportional to (1/3 - k k); for J_i = 1/2 the factor is exactly 1.
(R5) band limitation: lines outside the band see only the room-temperature field; the correction is the indicator of
     the band.
(R6) energy-density matching: a beam of spectral intensity I_nu has u = I_nu / c; T_eff follows from
     nbar_eff(nu) = c^3 u / (8 pi h nu^3), so h nu nbar = k T_eff in the Rayleigh-Jeans limit: rates are linear in T_eff
     while k T_eff >> h nu (always the case here: h nu / k = 1 K at 20 GHz).

## Questions for the independent check (neutral wording)
1. For an atom in |J = 1/2, m = +1/2> driven on a J = 1/2 -> J' transition by a field of fixed polarisation e, under
what conditions does the total rate summed over m' equal the rate for isotropic unpolarised radiation of the same
spectral energy density? 2. Same question for J = 3/2 initial states. 3. How is the effective temperature of a
directed, unpolarised beam of spectral intensity I_nu defined so that rates match a blackbody?
