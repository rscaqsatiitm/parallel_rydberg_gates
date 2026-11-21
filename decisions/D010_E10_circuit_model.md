# D010. Circuit-level model for E10 (correlated same-layer contaminant errors)

Date: 2026-11-21. Task S4. Choices that no source fixes, with reasons.

1. **Code and circuit.** Rotated surface-code memory (Z basis), stim `surface_code:rotated_memory_z`, rounds = d,
   d in {3, 5, 7}. Stim's circuit uses CX with Hadamards on the X-type ancillas; a CZ-native circuit has the same
   four entangling layers with the same pairs, so the layer structure (which pairs act simultaneously) is the same.
   Reason: standard, reproducible, decodable with PyMatching.
2. **Baseline noise (UNSOURCED, swept).** after_clifford_depolarization = after_reset_flip = before_measure_flip = p,
   p in {1e-3, 2e-3}. These are not hardware values; they set a reference against which the contaminant term is seen.
3. **Layout.** Every (control, target) pair of a CX layer is one gate site of two atoms. Site centre = midpoint of the
   two qubits' stim coordinates; sites of one layer lie on a square grid of spacing 2 coordinate units, mapped to the
   BLU25-like pitch 8.571 um (x) by 12.0 um (y) (D008). The two atoms of a site are +-1 um along x (d_pair = 2 um,
   pair axis x). Only sites active in that layer are sources or targets. Approximation: BLU25 interleaves the code
   differently in its zone; the real neighbour structure is not published.
4. **Contaminant physics (from E02, no new input).** Each atom of each active site becomes a contaminant with
   probability p_c x m per layer, p_c = 2.533e-4 (E02, 300 K, 4.6 MHz), m in {1, 3, 10} (m = 1 physical; 3 and 10 to
   resolve the effect and to emulate higher temperature or density). A contaminant at source s makes target pair j
   fail with probability E_same(R_sj, alpha_sj) from E02 summary.json same_weighted, comp 0 (total incl. leakage),
   B along z (main; x as variant), interpolated linearly in (ln R, ln E) and in alpha, R^-6 beyond 40 um.
   Intra-pair effects (the source's own partner) are part of the ordinary gate error and are not added.
   Earlier layers are not included (BLU25 uses ~400-470 us between gates; E07/E09 earlier-layer excess at 400 us is
   ~1e-5 or less per CZ).
5. **Failure = unheralded loss -> full depolarisation** of both qubits of the pair (each of the 16 two-qubit Paulis
   with probability 1/16). Reason: at long range the error is ~100 % leakage (E02) and BLU25 reports leakage is at least
   80 % loss; without loss detection a lost atom acts as a maximally mixed qubit. Heralded erasure (loss detection) is
   a variant NOT run here (see E10 README, cut list).
6. **Correlated encoding (model "corr").** Per source, target pairs with E_same >= 0.05 form the cluster (in this
   geometry: the x and y nearest neighbours, up to 4 sites); all 2^k - 1 failure subsets are enumerated exactly with
   probability p_c m prod(E or 1-E), as mutually exclusive branches of one E / ELSE_CORRELATED_ERROR chain. Within a
   subset, 16 Pauli strings of equal weight are used; pair j receives two-qubit Pauli index (i XOR c_j), i = 0..15,
   c_j random: each pair's Pauli distribution is exactly uniform, but the Paulis of different pairs in one event are
   deterministically coupled (approximation; variant V1 uses independent random strings instead). Pairs with
   E_same < 0.05 receive independent DEPOLARIZE2 with the same marginal (correlation among weak tail errors dropped:
   second order in E < 0.05).
7. **Independent model ("indep").** Each pair fails independently with the same marginal as in "corr":
   f_j = 1 - prod_s (1 - p_c m E_sj) over all sources, as DEPOLARIZE2(15 f_j / 16). The per-pair marginals of the two
   models are identical by construction (checked by sampling, E10 control C2).
8. **Decoder.** PyMatching 2.4.0 on stim's detector error model with decompose_errors, approximate_disjoint_errors and
   ignore_decomposition_failures; each model is decoded with its own error model (the decoder knows the noise).
   A matching decoder cannot exploit hyperedge correlations; a correlation-aware decoder could do better (not run).
