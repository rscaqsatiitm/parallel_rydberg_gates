# Gate 1 report (2026-11-20, autonomous run; owner asleep)

**Gate 1 passes: K1, K2 (D006) and K3 have not fired.** Stage 3 may start under Addendum 1.

## What was shown (provenance in the experiment READMEs; no fitted parameter anywhere)
1. Contaminant probability (Rb 53S, 2pi x 4.6 MHz time-optimal pulse, 300 K): p_c = 2.53e-4 per atom per
   CZ (52P 1.28e-4, 53P 1.25e-4), from ARC BBR rates and the modelled Rydberg time I_r = 0.192 T (E02).
2. Error map of a gate pair with one contaminant (E02, three-atom model, full fine and Zeeman structure,
   controls E01, matrix elements checked by an independent route E03b to 3e-5): error ~0.6-0.9 for
   R <= 8 um, half-error radius 10-12 um, R^-6 tail (slope -6.0 +- 0.04), long-range error is leakage
   (P-state hopping, converted to loss). Same-layer (created mid-gate) / whole-gate ratio 0.39 at long range.
3. P-state lifetime 96-102 us (300 K), 231-257 us (45 K), 291-332 us (4 K); creation rate falls 88x
   from 300 K to 4 K (E05). Anti-trapping hill 0.164 U_g at 852 nm, escape speed 0.177 um/us at 1 mK
   (DV2, independently checked).
4. K3 (E06): the zero-parameter prediction of BLU25 ED Fig. 6g overlaps the 2-sigma data at all four
   pre-registered points (Normal 50/100/200 us, Sparse 50 us). Median predicted excess at 50 us
   0.12 % vs measured 0.176(18) %.
5. K2 (E07): the same-layer floor in a BLU25-like dense zone (8.571 x 12.0 um) is 0.7-1.1e-3 per CZ at
   300 K, so a 1e-4 budget is unreachable by waiting; for 2x spacing it is 2-7e-5. A post-hoc check
   matches the measured Normal-Sparse difference (6.1(3.4)e-4 vs predicted 5-12e-4).

## What failed or is weak
- K3 is not discriminating: a decay-only model also passes; the prediction band spans ~4x.
- E03 (pairinteraction) blocked by the container's GitHub access; replaced by E03b, which shares the
  quantum-defect data with ARC.
- E01 control 1 failed its high-blockade threshold by 3.6e-6 (immaterial for increments).
- My expectation for K2 (finite t_wait > 100 us) was wrong in kind: the floor binds.
- Geometry of the Fig. 6g benchmark and the trap depth/waist are not published; values are figure
  readings or sensitivity ranges (D007, D008). Fig. 6g values are figure readings, human check pending.

## Consequence for Stage 3 (my reading; the owner may redirect)
The thermal limit has two parts with different remedies: (a) a same-layer density floor
eps_floor = p_c sum E_same(r), set by T (p_c), gate speed and spacing, which no delay removes; (b) an
earlier-layer excess, decay-limited in large arrays, t_wait = tau_P ln(1 + p_c n_full / eps*), 235-251 us
for eps* = 1e-4 at 300 K vs a 92 us kinematic interval. Both are design-relevant. Stage 3 as written
(cycle floor vs kinematic floor) addresses (b); (a) is the "density limit" thesis of the original handover.

## Three most important open problems
1. Omega and spacing dependence of both parts (needs maps at other Rabi frequencies; E08 planned).
2. Whether the 1e-3 floor is consistent with published error budgets of dense arrays (Evered 2023 model
   total 99.53-99.62 % vs measured 99.52-99.54 % leaves <~1e-3 unexplained; a row of sites has fewer
   neighbours than the BLU25 zone): a further zero-parameter test.
3. Logical consequence: the floor is spatially correlated (one contaminant hits ~4 neighbours at once)
   and mostly leakage/loss at long range: needs the circuit-level simulation.

## Recommendation
Continue to Stage 3. Target remains a letter only if Stage 3 yields a design-changing statement that is
stable over the declared ranges; otherwise PRA / PRX Quantum.
