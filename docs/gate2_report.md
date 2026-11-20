# Gate 2 report (2026-11-20, autonomous run)

**Verdict: Gate 2 is not passed** under the pre-registered definitions (D009, E09). At 300 K no schedule
has a thermal cycle floor at least twice its kinematic floor over the declared input range. Per the
handover, no letter draft is started. The calculation does, however, yield a different design-relevant
statement (a density floor) which the owner may choose to pursue; see "Recommendation".

## What was shown (zero fitted parameters; provenance in each experiment README)
1. **Microscopic error per contaminant** (E02; model E01, matrix elements cross-checked E03b): a
   neighbouring CZ pair within ~8 um of a P-state contaminant fails with probability 0.6-0.9 per gate;
   half-error radius 10-12 um at Omega/2pi = 4.6 MHz; R^-6 tail; the long-range part is leakage
   (P-state hopping, then loss). Contaminant probability 2.53e-4 per atom per CZ at 300 K.
2. **Confrontation with experiment** (E06, K3 not fired): the model reproduces BLU25 ED Fig. 6g within
   its 2-sigma error bars at all four pre-registered points (excess 0.06-0.22 % predicted vs 0.176(18) %
   measured at 50 us; recovery by 100-200 us; no effect at 2x spacing). The test is not discriminating
   (a decay-only model also passes; band ~4x wide).
3. **Density floor** (E07, E09): a contaminant created during a layer degrades the neighbouring gates
   of that same layer; no delay removes it. In a BLU25-like zone (8.571 x 12.0 um) this floor is
   0.7-1.1e-3 per CZ at 300 K, 1.0-1.6e-4 at 45 K and ~1e-5 at 4 K (ideal shielding). A 1e-4 budget
   needs 1.5-2.0x larger pitch at 300 K, 1.1-1.2x at 45 K, none at 4 K. Post-hoc (data seen first):
   the predicted Normal-Sparse difference at long gaps, 5-12e-4, matches the measured 6.1(3.4)e-4.
4. **Delay law** (DV1, independently checked; E07, E09): earlier-layer excess
   eps(t) = p_c n_full / (exp(t/tau_P) - 1); in arrays larger than the contaminant's flight distance per
   lifetime it is decay-limited because ejection from the tweezer only moves the contaminant to other
   sites. t_wait for 1e-4: 250-300 us at 300 K, 200-300 us at 45 K, 50-60 us at 4 K; for 1e-5: ~500,
   ~760, ~300 us.
5. **Cycle floor** (E09): at 300 K, T_th / T_kin = 0.7-1.4 (BLU25 surface, reading E 1e-4) and < 1.5
   for the parent's lifted-product schedules. BBR does not set the cycle time of current schedules.
6. **Gate speed** (E08, both pre-registered verdicts PASS): at fixed pulse shape, p_c ~ Omega^-1 exactly,
   E_full(R) ~ Omega^-2 in the tail (to 8 %), half-error radius ~ Omega^-0.3. The BLU25-zone floor at
   300 K is 2.8-4.1e-3, 0.7-1.1e-3, 1.4-3.1e-4 and 2.3-7.6e-5 per CZ at Omega/2pi = 2.3, 4.6, 9.2,
   18.4 MHz (exponent -2 to -2.6). Faster gates remove the floor about as effectively as cooling:
   1e-4 is reached near 10-16 MHz (DERIVED, interpolation) at the published pitch and 300 K. This
   excludes the other error channels that grow with Omega (outside the model).

## What failed, including wrong expectations
- Gate 2 (cycle-time thesis of Addendum 1): not passed; the expectation registered in E09 (ratio ~1)
  was correct, so this is a confirmed negative, not a surprise.
- K2 under D006: my expectation of a finite t_wait > 100 us was wrong in kind (floor binds).
- My pre-run inference that ED Fig. 6g "shows motion" was not supported (E06).
- E03 (pairinteraction) blocked by container GitHub access; substitute E03b shares quantum defects with ARC.
- E01 control 1 missed its high-blockade threshold by 3.6e-6 (immaterial).
- Inputs that are figure readings or sensitivities, not sourced values: Fig. 6g data, all gate-site
  pitches, trap depth in BLU25, trap waist, field direction, pair orientation, the RB fidelity convention.

## Most important open problems
1. **Is the density floor real at the 1e-3 level?** It rests on figure-read pitches and an RB convention
   the paper does not state. The cleanest test is a measurement the model predicts with no parameter:
   CZ infidelity vs gate-site pitch at long inter-gate delay (floor ~ pitch^-6 in the tail regime).
   Draft questions for the authors: docs/questions_for_authors.md.
2. **Logical consequence.** The floor is spatially correlated (one contaminant hits several neighbours
   in the same layer) and mostly loss-type at long range. Whether it matters beyond its marginal rate
   needs the circuit-level (Stim) simulation, not yet run.
3. **Which knob is cheapest.** Pitch (x1.5-2), temperature (45 K, if the field is truly cold) and
   Rabi frequency (x2-3.5) each bring the floor to ~1e-4 in this model; their costs are set by error
   channels the model does not contain (atom number per area, cryostat, laser power and scattering).
4. **Cryostat reality.** The 45 K and 4 K numbers assume an ideal Planck field; JILA measured
   T_eff = 188(8) K behind a 45 K box. With T_eff the floor reduction is ~1.6x, not ~7x.

## Recommendation
**Retarget.** The cycle-time thesis of Addendum 1 fails its own gate. A defensible paper is a
zero-parameter account of the BLU25 inter-gate-delay and spacing data plus the density floor and its
temperature and gate-speed dependence (floor ~ Omega^-2 to Omega^-2.6, E08): suitable for Physical Review A or PRX Quantum, not a letter.
A letter would require a design-changing result that the current data cannot yet support; the
strongest candidate is the density limit, if (i) the authors' actual pitch and RB convention confirm
the ~1e-3 floor and (ii) the circuit-level simulation shows a logical penalty beyond the marginal rate.
Decision for the owner: retarget to PRA/PRX Quantum, or fund the two checks above first.
