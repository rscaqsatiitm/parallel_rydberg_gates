# D012. Choices for E18 (Addendum 3, Stim variants)

Date: 2026-11-21. Task A3-S. Choices no source fixes, with reasons.

1. **Erasure (item 1a).** A contaminant-induced pair failure is a loss of both atoms of the pair (D010 item 5); with
   probability eta per failed pair it is heralded at the end of the round in which it occurred (loss detection by
   imaging). Encoding: each failure location (round, CX layer, pair) has its own flag qubit; every failure branch
   (the 16 Pauli branches of D010, identity included, since a lost atom is detected whatever its Pauli frame) also
   flips the flag. Herald efficiency eta is applied in post-processing: each fired flag is kept with probability eta
   (independent per location), so the same samples are decoded at every eta. Baseline (p) noise is never heralded.
   eta range {0, 0.5, 0.8, 0.95, 1.0}: BLU25 states leakage is "at least 80 % loss" (registry/notes, ED Fig. 5b) and
   loss detection efficiency in this architecture is not sourced; 0.5-1.0 brackets it, 0 reproduces E10.
2. **What the erasure decoder knows.** (i) A prior DEM built from the same model with contaminant strength
   m (1 - eta) (unheralded part; approximation for multi-pair events), decomposed as in E10. (ii) Per shot, the
   heralded locations; every graphlike edge produced by any Pauli on that pair at that location (from a probe DEM of
   the noiseless circuit with DEPOLARIZE2 at that location only) is set to error probability 1/2 (weight 0) for that
   shot. Same treatment for the indep model.
3. **Correlation-aware decoder (item 1b).** PyMatching 2.4.0 correlated matching (enable_correlations=True in
   from_detector_error_model and decode_batch) on the same decomposed DEM, which retains each hyperedge's
   decomposition. It uses pairwise correlations between edge components, not full hyperedge likelihoods; a BP+OSD or
   tensor-network decoder is not installed (checked: no ldpc, beliefmatching, tesseract, sinter).
4. **Large distance (item 2).** Same model as E10 at d = 9, 11 (rounds = d). Where >= 100 failures is computationally
   prohibitive (expected for base at d = 11), the point is reported with the shots used and a 95 % upper bound, and X is
   computed with the bound and labelled.
5. **Pitch (item 4).** Row pitch 10.0 um instead of 8.571 um, i.e. pitch = (10.0, 12.0) um in the E10 layout
   (D010 item 3: x = 8.571 replaced). Base model unchanged (no contaminant), reused from E10.
6. **Item 3 inputs** (earlier-layer failure per pair per layer f_prev; multiplicative factor for non-resonant BBR
   channels) come from the parent task (E16). Provisional values if not yet received: f_prev in [1e-6, 2.9e-5]
   (E07/E09 earlier-layer excess at 400 us), factor 1.0. f_prev is added as independent DEPOLARIZE2(15 f / 16) per pair
   per layer to both corr and indep (it is a different contaminant population, decorrelated by 400 us of motion and
   decay: approximation).
