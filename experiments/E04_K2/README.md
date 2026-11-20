# E04. K2 evaluation for the Evered 2023 configuration (rule: decisions/D003)

Pre-registered 2026-11-20 before the run (E02 running, no E02 numbers seen beyond I_r and p_c,
which are printed at its start and stated below).

**Inputs already known.** From E02 (c): gate time T = 0.2641 us; I_r/T = 0.1925 (Rydberg population of
one atom, averaged over the four computational inputs); BBR rates 53S -> 52P = 2525 /s, -> 53P = 2458 /s
(ARC 3.10.2, 300 K); p_c = 1.28e-4 (52P) + 1.25e-4 (53P) = 2.53e-4 per atom per gate. n'P lifetimes at
300 K (ARC getStateLifetime, includeLevelsUpTo n+40): 52P1/2 97.7, 52P3/2 95.8, 53P1/2 102.2, 53P3/2 100.1 us.

**Geometry (D005).** One row of 10 gate sites (the 20-atom data of Evered 2023), pitch a = 9 um (lower end
of the figure-read range [9, 11]; 11 um also reported), pair distance 2 um, pair axis either along the
row or perpendicular to it (not stated in the paper; both reported). B along x, y or z (D004 item 6).
Per-site error averaged over the 10 sites (edge sites have fewer neighbours).

**Quantities (D003).** For each contaminant position r (an atom of another site):
E_full(r) from the model with the contaminant on for the whole gate; E_same(r) averaged over t_on with
weight p_r(t_on) (12-point grid). Then
  epsilon_same = (1/10) sum_sites sum_{other atoms} p_c * E_same(r),
  epsilon_ss(t_gap) = (1/10) sum_sites sum_{other atoms} p_c * [E_same(r) + sum_{j>=1} S(j (T + t_gap)) E_full(r)],
S(t) = exp(-t / tau_P) with tau_P the 300 K lifetime of the contaminant's J level (weighted by the same
weights as the contaminant state). Contaminants of each n' weighted by their own p_c. Contaminants are
assumed not to move between layers (no ejection): conservative against K2 firing per D003. Not
conservative in one respect: BBR transfer out of n'P into other Rydberg states (still interacting) ends
survival in this model; the radiative-only lifetime (~300 us) is also reported as an upper variant.
The largest value over (Bdir, pair orientation) at a = 9 um is the K2 number.

**Expectation.** From control E01-[2] (E_full ~ 1 at 8 um), epsilon_ss(4 us) of order p_c x (number
of layers survived ~ 100/4.3 ~ 23) x (number of atoms within ~10 um ~ 4) ~ 2e-2 per site, i.e. far above
1e-5: K2b not expected to fire. epsilon_same expected ~ p_c x 4 x 0.3 ~ 3e-4: K2a not expected to fire.
This epsilon_ss would exceed the experiment's total CZ error (~5e-3) by a factor ~4 and would therefore
already contradict Evered 2023 / Bluvstein 2026 unless contaminants move away between layers: that is
the Stage 2 question (K3), not decided here.

**Verdict.** K2a / K2b fire or not per D003, thresholds 1e-5. Not changed after the run.

## Result
(appended after the run)
