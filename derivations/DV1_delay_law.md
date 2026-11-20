# DV1. Delay law for contaminant-limited gate layers

**Header (Rule 7).**
- Assumptions: (A1) contaminants are rare: at most one contaminant interacts with a given gate pair
  at a time (p_c N_R << 1, N_R the number of atoms within the interaction range); (A2) each contaminant
  is created independently with probability p_c per atom per gate (BBR, Poisson); (A3) a contaminant
  harms a gate executed a time t after its creation with probability S(t) E_full(r(t)), where S(t) is the
  probability that it is still in the modelled n'P manifold and r(t) its position relative to the
  gate pair; (A4) layers are identical and separated by a fixed delay t (gate duration T << t);
  (A5) errors from different contaminants add (first order in p_c).
- Conventions: epsilon = excess error per CZ (1 - entanglement fidelity, leakage included), averaged
  over gate sites; E_same, E_full, p_c as in D003/D004; tau_P the n'P lifetime.
- Domain of validity: p_c N_R K << 1 (no multi-contaminant events); t >> T; contaminant motion either
  negligible (case 1) or described by the drift law r(t) (case 2).
- Dependencies: E02 (E_full, E_same), E04/E05 (lattice sums), trap-return motion model (DV2, pending).

## Derivation
Sum over sources (atoms i at positions r_i, all sites including the target's own partner) and over
earlier layers j = 1, 2, ... (created a time j t earlier):

  epsilon(t) = sum_i p_c [ E_same(r_i) + sum_{j>=1} S(j t) E_full(r_i(j t)) ].           (1)

**Case 1: static contaminants, exponential survival** S(t) = exp(-t / tau_P), r_i(t) = r_i:

  epsilon(t) = p_c [ n_same + n_full / (exp(t / tau_P) - 1) ],   n_full = sum_i E_full(r_i),
                                                                 n_same = sum_i E_same(r_i).   (2)

For t >> tau_P the second term is p_c n_full exp(-t/tau_P). Setting the excess from earlier layers
equal to a budget eps* (per CZ):

  t_wait = tau_P ln[ p_c n_full / eps* ]  (t_wait >> tau_P; requires p_c n_full > eps*).         (3)

The owner's form t_wait = tau_P ln[K p_c n_R / eps] follows from (3) when the budget eps is per QEC
round of K CZ layers per qubit (eps = K eps*), with n_R := n_full, the error-weighted number of atoms
in range. Note: (3) needs eps* < p_c n_same + p_c n_full exp(-t/tau_P): the same-layer term
p_c n_same is a floor that no delay removes; if p_c n_same > eps* no t_wait exists (only spacing,
temperature or gate speed help).

**Case 2: drift out of range.** If after the traps return the contaminant leaves its site with speed
v and the error is negligible beyond R_c, a static array gives S(t) E_full(r(t)) ~ 0 for t > t_esc
~ R_c / v (deterministic, not exponential): t_wait ~ min(t_esc, tau_P ln[...]). Whether v is large
enough to matter is computed in DV2 from sourced trap parameters, not assumed.

**Order of magnitude (DERIVED, illustrative only, not a result):** with p_c = 2.5e-4 (E02, 2023
configuration) and n_full ~ 4 (E_full ~ 1 within ~9 um, a 9-10 um pitch row with pair partners),
p_c n_full ~ 1e-3; for eps* = 1e-4, t_wait = tau_P ln 10 = 2.3 tau_P ~ 230 us at tau_P = 100 us.
This is below the 400 us used by BLU25 and above the parent repository's 92 us kinematic bound;
whether it survives the full calculation (motion, angular structure, same-layer floor) is the Stage 1
result.

## Questions for the independent check (neutral wording)
1. Given (A1)-(A5) and S(t) = exp(-t/tau), what is sum_{j>=1} S(j t)? 2. Under what condition on t is
the leading-order form of (3) accurate to 10 % in t_wait? 3. Does the same-layer term depend on t?
