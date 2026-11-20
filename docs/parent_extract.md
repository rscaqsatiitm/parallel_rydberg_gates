# Parent-repository extract: kinematic floor, cycle budgets, P-state material

Read-only extraction from the parent repository `rscaqsatiitm/Neutral-atom-QC`, cloned at
`/home/user/neutral-atom-qc`, commit `7eb6b2e` ("Merge pull request #24 ..."). Nothing in the parent was modified.
All paths below are relative to the parent root. `file:N` means line N, and `file:N-M` means lines N to M.
NOT FOUND means the item was searched for and is not in the parent. No number here is estimated.

Extracted 2026-11-20 for the question: what minimum time between Rydberg gate layers, and hence what minimum QEC
cycle, do blackbody-created Rydberg P-state contaminants impose, compared with the kinematic (atom-motion) floor of
the same schedules?

---

## 1. Kinematic lower bound of the BLU25 in-zone interval: 92 us against a measured 470 us, margin 5.09

### 1.1 Where it is stated
| What | Where |
|---|---|
| Blocked-task record, resolution under D007 (table: in-zone interval 92.2 us, measured 470 us, margin 5.09x) | `plan/blocked/X1.2.md:56-74` (table at `:62-66`) |
| Decision record D007 (approved 2026-09-26): outcome on promotion, context, decision | `docs/decisions/D007-blu25-move-model.md:9-16` (outcome), `:37-50` (context), `:58-66` (decision items 2-3), `:103-104` (anchor edit) |
| Anchor `timing.blu25_gap_kinematic_lower_bound` | `plan/anchors.yaml:98-106` |
| Config that computes it | `configs/blu25_surface.yaml:66-85` (`let:`), `:94` (prediction), `:100-108` (outputs) |
| Experiment that runs it | `experiments/e10_blu25_round/run.py` (whole file, 62 lines); acceptance `experiments/e10_blu25_round/check.py` |
| Result file | `experiments/e10_blu25_round/results.json`, keys `configs.blu25_surface.outputs.*` and `predictions.timing.blu25_gap_kinematic_lower_bound` (git_commit `23335b0063982cca1662129ab78f1a56b2074654`, 2026-09-28T04:46:24Z) |
| Gate report | `reports/G1a.md:166-172` ("in-zone interval's kinematic lower bound 92.2 us against 470 us (speed margin 5.09x)") |
| Manuscript | `papers/g1_atomclock/manuscript/main.tex:102` ("a lower bound of 92 us on each in-zone interval against the measured 470 us") |

Verbatim from `plan/blocked/X1.2.md:62-66`:

    | Quantity | Kinematic (mid) | lo / hi variants | Measured | Speed margin |
    |---|---|---|---|---|
    | in-zone interval (move + CZ) | 92.2 us | - | 470 us | 5.09x |
    | block swap (2 moves + 2 transfers) | 0.922 ms | 0.662 ms / 1.164 ms | 2.57 ms | 2.79x |
    | round | 1.291 ms | - | 4.45 ms | 3.45x |

**Stale numbers in that table.** The swap and round rows (0.922 ms, 2.79x, 1.291 ms, 3.45x) predate the
2026-09-26 correction of reading A2 (swap distance; `plan/human_readings/readings.yaml:69`). The committed
`results.json` gives the following. The in-zone interval is unchanged.

| Output (`results.json`, `configs.blu25_surface.outputs`) | Value |
|---|---|
| `t_inzone_move_kin` | 9.197851377485513e-05 s |
| `t_gap_kin` | 9.224851377485513e-05 s (92.25 us) |
| `speed_margin_gap` | 5.094933032168931 |
| `t_swap_move_kin` | 2.625031267819067e-04 s |
| `t_transfer` | 2.25e-04 s |
| `t_swap_kin` | 9.750062535638134e-04 s (lo 8.018639968978295e-04, hi 1.1584048786263787e-03) |
| `speed_margin_swap` | 2.6358805295927215 (lo 3.205, hi 2.219) |
| `t_round_kinematic` | 1.344000308663234e-03 s (lo 1.1709e-03, hi 1.5274e-03) |
| `speed_margin_round` | 3.3110111443546075 |

The current numbers (92 us, 0.975 ms, 1.34 ms, 3.3x) are the ones in `papers/g1_atomclock/manuscript/main.tex:102`
and in e41 row 3 (1.344 ms).

### 1.2 What "kinematic interval" means exactly
- **The interval.** It is the time between two consecutive CZ gate layers of one QEC round in BLU25's d = 5
  surface-code memory (Fig. 2). In that time the ancilla block, held in the AOD, moves rigidly to its next data
  neighbour and then the next CZ fires. The 470 us it is compared with is BLU25's "0.47 ms time between gates".
- **Per round.** One round has 4 CZ layers and 3 drawn in-zone moves, so 3 intervals lie between gate layers 1-2,
  2-3 and 3-4. The Methods arithmetic (4.45 - 2.57)/0.47 = 4 gives a fourth interval. D007 item 1 takes it, as a
  declared inference, to be "the incoming block's entry onto its first gate position" (`configs/blu25_surface.yaml:36-40`,
  `D007:53-57`).
- **The kinematic value is a mean.** The number is the *mean* in-zone move time, averaged over the 3 moves and over
  the N and Z round patterns, plus one CZ duration (`configs/blu25_surface.yaml:82-83`). It is not the time of any
  one interval and not the maximum. Per-move values are computed below.
- **What "kinematic" means.** The time the drawn moves would take under the corpus's fastest sourced move law,
  ZHOU25 Eq. 1 `t = 2 sqrt(L/a)` at a = 5500 m/s^2. Nothing else is counted: no settling, no AOD tone change, no
  single-qubit gates, no trap transfer. D007 item 3 (`:64-66`) names the ratio measured/kinematic the "speed
  margin". It is a reported result, not an anchor.
- **The round floor.** `t_round_kinematic = 4 * t_gap_kin + t_swap_kin` (`configs/blu25_surface.yaml:107`) assigns
  the same mean `t_gap_kin` to the undrawn fourth (entry) interval.

### 1.3 Formula (verbatim, `configs/blu25_surface.yaml:70-85`)

      p_y: "blu25_ez_vertical_extent_m / n_ez_gate_rows"
      p_x: "p_y * blu25_data_pitch_aspect_x_over_y"
      p_d: "sqrt(p_x ** 2 + p_y ** 2)"
      ...
      a: zhou25_acceleration_m_per_s2
      t_n_path: "2 * (2 * sqrt(p_y / a)) + 2 * sqrt(p_d / a)"
      t_z_path: "2 * (2 * sqrt(p_x / a)) + 2 * sqrt(p_d / a)"
      t_inzone_move_kin: "(t_n_path + t_z_path) / 2 / n_inzone_moves_per_round"
      t_gap_kin: "t_inzone_move_kin + blu25_cz_duration_s"

In closed form:

    t_gap_kin = [ (2 t(p_y) + t(p_d)) + (2 t(p_x) + t(p_d)) ] / (2 * 3) + t_CZ,   with t(L) = 2 sqrt(L / a)

The N path (rounds 1 and 4) is edge (vertical) + diagonal + edge. The Z path (rounds 2 and 3) is edge
(horizontal) + diagonal + edge (reading A1).

### 1.4 Inputs
| Symbol | Value | Unit | Key / location | Provenance class | Verbatim quote or basis |
|---|---|---|---|---|---|
| Vertical extent of the gate rows | 6.0e-05 | m | `blu25_ez_vertical_extent_m`, `params/params.yaml:579` | Sourced quote (BLU25 Methods, Surface code layout) | "cover 7 rows of gate sites in the entangling zone and are homogenized to about 1% peak-to-peak variation over a vertical extent of 60 um." |
| Gate rows | 7 | count | `n_ez_gate_rows`, `configs/blu25_surface.yaml:61-65` | Sourced quote (same sentence) | same |
| p_y = 60 um / 7 | 8.5714e-06 (reading A1 rounds it to 8.6 um) | m | derived in config | Derived from print | - |
| x:y pitch aspect | 1.40 (point value; note says about +-10 %) | dimensionless | `blu25_data_pitch_aspect_x_over_y`, `params/params.yaml:141` | **Figure reading A1** (Ext. Data Fig. 6a atom image), DERIVED; human spot check done | caption quote "The data qubits and one ancilla block are located in the entangling zone (top) and four additional ancilla blocks are in storage (bottom)"; note "Data-grid x:y pitch ratio 118:84 px ... DERIVED ... about +-10 % ... human spot check by RS on 2026-09-27, confirmed: the D009 flag is lifted." |
| p_x = p_y x 1.40 | 1.2000e-05 in the model (reading A1 states 12.1 um, from 118/84 = 1.405) | m | derived | Derived (reading x print) | `readings.yaml:48`: "Taking the y pitch as the gate-site row pitch 60 um / 7 rows = 8.6 um (Methods) gives x pitch 12.1 um." |
| p_d = sqrt(p_x^2 + p_y^2) | 1.4747e-05 (reading A1: 14.8 um) | m | derived | Derived | - |
| Moves per round in-zone | 3 | count | `n_inzone_moves_per_round`, `configs/blu25_surface.yaml:31-35` | **Figure reading A1** (Ext. Data Fig. 6d) | caption "d, Stabilizer gate ordering. The same pattern is used globally in each round." |
| CZ layers per round | 4 | count | `n_gate_layers_per_round`, `configs/blu25_surface.yaml:26-30` | Sourced quote + arithmetic (20 gate layers / 5 rounds) | "apply up to five rounds of stabilizer measurement ... A global Z(θ) rotation is applied to the data qubits at every gate layer (20 time steps in total)." |
| Between-gate intervals per round | 4 | count | `n_between_gate_intervals_per_round`, `configs/blu25_surface.yaml:36-40` | Sourced quote + arithmetic + declared inference (D007 item 1) | "each QEC round was 4.45 ms. This originated from a 0.47 ms time between gates, and a total of 2.57 ms from moving ..." |
| Acceleration a | 5500 | m/s^2 | `zhou25_acceleration_m_per_s2`, `params/params.yaml:721` | Sourced quote (ZHOU25 Table 1, p3) | "Site spacing l Acceleration a Gate time 12 um 5500 m/s2 1 us Measure time Decoding time 500 us 500 us" |
| Origin of a | 55 um in 200 us | m, s | `zhou25_accel_derivation_distance_m` / `_time_s`, `params/params.yaml:725-726` | Sourced quote (ZHOU25 Table 1 caption) | "The accel- eration is calculated from moving 55 um in 200 us [[13]](#13)." Check: 2 sqrt(55e-6/5500) = 200 us. ZHAO26 cites the same 5500 m/s^2 to Bluvstein 2022 (`params/params.yaml:678`). |
| CZ duration | 2.7e-07 | s | `blu25_cz_duration_s`, `params/params.yaml:140` | Sourced quote (BLU25 Methods, System overview; reading F2) | "(270-ns duration) between clock qubits are performed with fast two-photon excitation" |
| Measured interval | 4.7e-04 | s | `blu25_time_between_gates_s`, `params/params.yaml:570` (also `:125`) | Sourced quote (BLU25 Methods, "Processor clock speed") | "This originated from a 0.47 ms time between gates" |

**Move law.** ZHOU25 Eq. 1, `t = 2 sqrt(L/a)`, is constant acceleration over the first half of the move and
constant deceleration over the second (bang-bang). It is cited as "ZHOU25 Eq. 1" in
`configs/zhou25_transversal.yaml:9`, `docs/decisions/D008-blu25-move-law.md:30,38` and `plan/anchors.yaml:105`.
A verbatim quote of Eq. 1 itself is NOT FOUND in `params/params.yaml` or `params/quotes.yaml`.
`params/params.yaml:725` refers to "derived.zhou25_accel_check", which is NOT FOUND in `params/params.yaml` or
`plan/anchors.yaml`.

**Velocity limit.** The model has no velocity cap: NOT FOUND in the model. The law implies a peak velocity
v_max = sqrt(a L):

| Move | v_max |
|---|---|
| vertical edge, 8.57 um | 0.217 m/s |
| horizontal edge, 12.0 um | 0.257 m/s |
| diagonal, 14.75 um | 0.285 m/s |

The only velocity param, `gyg24_peak_move_velocity` (0.054 m/s, `params/params.yaml:172`), is a lattice value. The
anchor note says "Not a tweezer-array bound" (`plan/anchors.yaml:583-590`). It is not used.

**Jerk-limited profiles** are not modelled. BLU24 uses a cubic profile ("Motion is realized with a cubic profile as
in ref. 7", `params/params.yaml:548`), so its moves do not follow this law.

### 1.5 Worked numbers
These are recomputed from the formula above. They match `results.json` to all printed digits.

| Move | L (um) | t = 2 sqrt(L/a) (us) |
|---|---|---|
| vertical edge (N rounds) | 8.5714 | 78.954 |
| horizontal edge (Z rounds) | 12.000 | 93.420 |
| diagonal (both) | 14.747 | 103.561 |

- N path: 2 x 78.954 + 103.561 = 261.470 us.
- Z path: 2 x 93.420 + 103.561 = 290.401 us.
- Mean move: (261.470 + 290.401)/6 = 91.979 us. Adding the CZ (0.270 us) gives **t_gap_kin = 92.249 us**.
- Margin: 470 / 92.249 = **5.0949**.
- **Per-interval floors (not reported by the parent).** From 79.22 us (vertical edge + CZ) to 103.83 us
  (diagonal + CZ).
- **Pitch sensitivity.** With pitch ratio 1.0 the bound falls to "about 80 us; verdict unchanged"
  (`plan/human_readings/SPOT_CHECK_A1_A2_A4_D2.md:34-36`).
- **Acceleration sensitivity** (not scored, requested by the 2026-09-28 review; `experiments/e10_blu25_round/run.py:32-41`).
  At XU24's 2e4 m/s^2 (`params/params.yaml:665`, "ap = 0.02 um us−2"):
  - t_gap_kin = 48.50 us, margin 9.69;
  - kinematic round 0.919 ms (`results.json` `xu24_acceleration_sensitivity`).

### 1.6 Swap part, for completeness (`configs/blu25_surface.yaml:74-77, 84-85`)
- Formula: t_swap_kin = 2 x 2 sqrt(L_swap/a) + 2 x t_transfer.
- L_swap = sqrt(v^2 + h^2), at the range midpoints:
  - v in [86, 92] um (`blu25_swap_vertical_m`, `params/params.yaml:142`, reading A2);
  - h in [10, 55] um (`blu25_swap_horizontal_m`, `:143`, reading A2).
- t_transfer = mid(100-200 us ramp) + mid(50-100 us pull-away) = 225 us:
  - BLU24 Methods (`params/params.yaml:549-560`): "we ramp up the intensity of the AOD tones ... over a time of
    100–200 us ... and then move the AOD trap 1–2 um away over a time of 50–100 us."
  - The transfer happens at the storage end only (reading A2).

### 1.7 Domain of validity, as stated or implied in the parent
1. **Lower bound only, and one-sided.** The anchor tolerance is `{range: [0, 0.47e-3]}` (`plan/anchors.yaml:101`).
   The test is falsifiable only in one direction: a geometry that implied a longer interval than measured would
   fail it (`D007:61`).
2. **The ancilla block stays in the AOD at the entangling end.** There is no in-zone transfer (reading A2,
   `readings.yaml:76-78`). Every move is a single rigid block move (reading A1, `readings.yaml:45-46`).
3. **Excluded from the bound:** settling, AOD retuning, the per-layer global Z(θ) rotation, and any wait for
   Rydberg decay. The global Raman rotation is about 5 us (`blu25_global_rotation_s`, `params/params.yaml:581`); it
   is not in the bound.
4. **What the 0.47 ms contains is not stated by BLU25.** Reading A5 (`readings.yaml:113-127`):
   `gap_includes_move_gate_settling: null`, "Record as not_stated for both booleans".
5. **The bound depends on the acceleration chosen.**
   - 5500 m/s^2 is a measured value for a 55 um move. D007 calls it "the corpus's fastest sourced law"
     (`configs/blu25_surface.yaml:8-9`).
   - XU24's 2e4 m/s^2 halves the bound.
   - D008 notes the BLU25 operating point (a_eff = 116-192 m/s^2) "is a measured operating point of this machine,
     not a kinematic limit" (`plan/blocked/X1.2.md:26-29`).
6. **The geometry is DERIVED** from atom images, about +-10 %, with scale A against scale B differing by 7 %
   (`readings.yaml:16`).
   - The anchor note (`plan/anchors.yaml:106`) still says "needs_human_spot_check". The readings file records the
     check as done (Section 6 below).
   - The swap anchor's `inputs` text (`plan/anchors.yaml:114`) still quotes the withdrawn "45-105 um vertical and
     0-30 um horizontal".
7. **The fourth interval** is assumed equal to the mean drawn interval. No entry move is drawn: "no entry drawn"
   (spot check, `readings.yaml:27`).
8. **The authors say the machine is not speed-optimised.** `params/quotes.yaml:4-7`: "In the present work, we do
   not optimize for clock speed, and often choose slower speeds for our components so that they can function
   reliably without detailed characterization on exist- ing infrastructure."

### 1.8 Code path
- `experiments/e10_blu25_round/run.py:44-52` calls `experiment.run([CFG], ...)`, which calls
  `atomclock/config.py:288` `fit_and_run(cfg)`.
- The `let:` expressions are evaluated by `atomclock/config.py:63` `evaluate()`. The functions allowed are listed
  at `atomclock/config.py:51` (`sqrt`, `min`, `max`, `ceil`, `floor`, `log2`). `lo`/`hi`/`mid` for range params are
  defined at `atomclock/config.py:127-135`.
- Variants: `run.py:22-29` (`variant("lo"/"hi")`) and `:32-41` (XU24 acceleration).
- Acceptance: `python experiments/e10_blu25_round/check.py`, which also runs `scripts/check_anchor.py` on the 4
  anchors.
- No unit test in `tests/` targets the bound directly. `tests/test_cli.py` uses `configs/blu25_surface.yaml` for
  the report path only.

---

## 2. `params/params.yaml` entries relevant to the new project

Format: line, key, value, unit, source, then the verbatim quote and location. Where a quote is long, the part that
carries the number is given.

### 2.1 Time between gates, inter-gate delays
| Line | Key | Value | Quote (verbatim) | Location |
|---|---|---|---|---|
| 570 | `blu25_time_between_gates_s` | 4.7e-4 s, BLU25 | "This originated from a 0.47 ms time between gates" (note: "Methods elsewhere quotes "400 us" between gates for surface code.") | Methods, "Processor clock speed" |
| 125 | `blu25_time_between_gates` | 4.7e-4 s, BLU25 | "This originated from a 0.47 ms time between gates, and a total of 2.57 ms from moving the ancilla atoms to the storage zone and bringing in the next group to the entangling zone." | same |
| 576 | `blu25_gap_between_gates_sc_s` | 4.0e-4 s, BLU25 | "In quantum circuits based on atom motion, the duration between gates is sufficiently long (for example, 400 us for surface code repeated stabilizer measurements)" | **Methods (Rydberg P-state decay)**; note "Differs from 0.47 ms in the clock-speed section." |
| 583 | `blu25_benchmark_gap_s` | 4.0e-6 s, BLU25 | "we have only 4 us between gates" | **Methods (Rydberg P-state decay)**; note "Repeated randomized-benchmarking sequence of ref. 36, not a QEC circuit." |
| 98 | `blu24_duration_between_gates` | 2.0e-4 s, BLU24 | "owing to the approximately 200 μs duration between gates" | Methods (Rydberg gates / crosstalk paragraph) |
| 97 / 548 | `blu24_free_space_move_time` / `blu24_move_between_gates_s` | 2.0e-4 s, BLU24 | "Motion is realized with a cubic profile as in ref. 7, the characteristic free-space movement time between gates is roughly 200 μs" | Methods, "Shuttling and transfers" |
| 382 | `eve23_inter_gate_recapture_time` | 3.0e-6 s, EVE23 | "the ground state atoms are then recaptured for roughly ∼ 3µs between consecutive gate applications." (note: traps "pulsed off for a few hundred ns during the Rydberg gate") | Extended Data figure caption |
| 383 | `eve23_transport_inter_gate_delay` | 1.0e-4 s, EVE23 | "Moreover, when running quantum circuits using atom transport ... the ∼ 100 us delay between subsequent gates would result in leftover Rydberg states being expelled from the array" (note "Approximate.") | Methods, correlated errors |
| 474 | `pec26_gate_spacing` | 4.0e-6 s, PEC26 | "Gate se- quences with 4µs spacing are therefore prone to these errors" | Supplementary / discussion |
| 472 | `pec26_trap_off_per_gate` | 5.0e-7 s, PEC26 | "Optical traps are switched off for 500ns during each gate to avoid anti-trapping of the Rydberg state [1]." (note "Cited value.") | Supplementary / discussion |

### 2.2 Round durations and clock speed
| Line | Key | Value | Quote (verbatim) | Location |
|---|---|---|---|---|
| 119 / 569 | `blu25_qec_round_time` / `blu25_qec_round_s` | 4.45e-3 s | "In the repeated surface code experiments in Fig. 2, each QEC round was 4.45 ms." | BLU25 Methods, "Processor clock speed" |
| 126 / 571 | `blu25_qec_round_moving_time` / `blu25_ancilla_block_swap_s` | 2.57e-3 s | "a total of 2.57 ms from moving the ancilla atoms to the storage zone and bringing in the next group to the entangling zone." | same |
| 127-129, 572-573 | `blu25_transversal_cnot_circuit_time`, `..._max_count`, `blu25_time_per_transversal_cnot` | 17.7 ms, 27, 0.655 ms | "we fix the overall circuit duration (independent of the number of CNOTs) at 17.7 ms, corresponding to the time of the longest circuit of 27 total transversal CNOTs. This corre- sponds to 0.655 ms per transversal CNOT on average." | same |
| 130 / 574 | `blu25_teleportation_layer_time` | 41.9e-3 s | "For this reason, each logical teleportation layer was 41.9 ms." | same |
| 131-136 | `blu25_teleport_layer_circuit_time` (13.5 ms), `blu25_spin_to_position_time` (4 ms), `blu25_imaging_time_deep_circuit` (10 ms), `blu25_cool_resort_time` (13.3 ms), `blu25_midcircuit_processing_latency` (7 ms), `blu25_reinitialization_time` (1.1 ms) | | "The circuit is 13.5-ms long. Including idle times, the spin-to-position conversion takes 4-ms, imaging takes 10-ms, cooling and re-sorting takes 13.3-ms (≈ 7-ms latency for mid-circuit data processing), and re-initialization takes 1.1-ms." | BLU25 Ext. Data Fig. 3d caption |
| 137 / 575 | `blu25_fast_calibration_cycle` / `blu25_rabi_calibration_cycle_s` | 4e-3 s | "In the repeated Rabi calibration in Fig. 5b, we optimized for speed and achieved a cycle time of 4 ms." | BLU25 Methods, "Processor clock speed" |
| 138 | `blu25_background_vacuum_loss_per_qec_seq` | 0.006 | "Our repeated QEC sequence also experienced 0.6% background loss from vacuum that can be readily reduced to <0.01% using improved vacuum lifetime and a shorter sequence (for example, about 4 ms cycle times in Fig. 5b)." | BLU25 Discussion |
| 727 | `zhou25_qec_cycle_gates_s` | 4.0e-4 s | "Our estimates directly account for the movement times, resulting in the gates in a QEC cycle taking around 400 us." | ZHOU25 p10, Sec. 4.2 |
| 722-724 | `zhou25_gate_time_s` (1 us), `zhou25_measure_time_s` (500 us), `zhou25_decoding_time_s` (500 us) | | Table 1 flattened quote (as in Section 1.4) | ZHOU25 p3 |
| 730 | `zhou25_lattice_surgery_qec_cycle_s` | 9e-4 s | "... so we assume a 900 us QEC cycle time." | ZHOU25 p11 |
| 731-732 | `zhou25_local_gadget_move_s` (1.5 ms), `zhou25_local_gadget_qec_cycle_s` (3 ms) | | "... would involve a movement time of 1.5 ms and result in a QEC cycle time close to 3 ms." | ZHOU25 p12 |
| 740 | `cain26_assumed_cycle_s` | 1e-3 s | "Here we assume a 1 ms stabilizer measurement cycle. ..." | CAIN26 |
| 233 | `ueno26_esm_cycle_time` | 2.37e-4 s | "For the ESM duration, we assume 237 µs and 1 µs for NA and superconducting platforms, respectively." | UENO26 p.12 |
| 672 | `xu24_se_round_s` | 24e-3 s | "resulting in a total time overhead of 3 ms per rearrangement layer and 24 ms for a full round of syndrome extraction" | XU24 p10 |
| 682-683 | `zhao26_se_round_2aod_p192_s` (16.91 ms), `zhao26_se_round_4aod_p96_s` (8.317 ms) | | "SE round (2 crossed-AODs) 13,267us 16,910us"; "SE round (4 crossed-AODs) 8,317us 9,935us" | ZHAO26 App. D.4, Table D2 |
| 698 | `zhao26_projected_se_round_s` | [2e-3, 4e-3] s (range) | see file | ZHAO26 |
| 394 / 396 | `lee26_mcm_feedforward_cycle_time` (45 us), `..._upper_bound` (100 us) | | "... together, these define a measurement-and-feedforward cycle time of 45 us."; "Our approach reduces the measurement-and-feedforward cycle time to below 100 us" | LEE26 |
| 545-547 | `blu24_local_imaging_s` (500 us), `blu24_camera_readout_s` (200 us), `blu24_readout_feedforward_cycle_s` (1 ms, upper) | | Ext. Data Fig. 3d caption / Methods quotes in file | BLU24 |

### 2.3 Rydberg lifetimes and P-state contaminants
| Line | Key | Value | Quote (verbatim) | Location / note |
|---|---|---|---|---|
| 380 | `eve23_rydberg_t1` | 8.8e-5 s, EVE23 | "We assume a 88 us Rydberg state lifetime (based on measured T1 with 1013-nm scattering lifetime subtracted)" | Ext. Data Fig. 3 caption; note: "n = 53; radiative 170 us, blackbody 128 us components." |
| 473 | `pec26_rydberg_p_state_lifetime` | 1.0e-4 s, PEC26 | "Recent experiments [9] identify black body–induced decay to nearby Rydberg P states (∼ 100µs lifetimes) as dominant error source." | Supplementary / discussion; note "Approximate, cited." |
| 500 | `zhang25_rydberg_lifetime_calc_300k` | 1.47e-4 s, ZHANG25 | "The calculated 70S1/2 Ryd- berg state lifetime is 147 us at 300 K and 306 us at 45 K." | App. E; "CALCULATED, not measured" |
| 501 | `zhang25_rydberg_lifetime_calc_45k` | 3.06e-4 s | same | App. E |
| 502 | `zhang25_rydberg_lifetime_sim` | 1.0e-4 s | "we conservatively set the cryogenic lifetime to be 100 us in the simulation." | App. E; "Assumption." |
| 381 | `eve23_ground_rydberg_t2star` | 3.0e-6 s | "our measured ground-Rydberg T∗ 2 = 3 us which is dominated by laser light shift fluctuations and finite atomic tempera- ture." | EVE23 main text |
| 379 | `eve23_gate_induced_loss` | 0.0017 | "Specifically, there is a 0.35(5)% probability that an atom is lost during the sequence, and the gate itself causes 0.17% additional loss on top of this baseline loss." | EVE23 Methods |

BLU25's own P-state sentence is not in `params.yaml` as a number. It is in reading A5 (Section 5).

### 2.4 Gate-zone geometry
| Line | Key | Value | Quote / note |
|---|---|---|---|
| 579 | `blu25_ez_vertical_extent_m` | 60 um | Section 1.4 |
| 577 | `blu25_ez_storage_separation_m` | 40 um | "The entangling zone is separated by 40 um from the storage and readout zone (over- lapping in these measurements)" |
| 578 | `blu25_readout_zone_height_m` | 55 um | "The readout zone is 12 rows tall (55 um) with two rows of traps per atom for the lattice readout" |
| 580 | `blu25_array_width_m` | 165 um | "resulting in a total array width of 165 um." |
| 141 | `blu25_data_pitch_aspect_x_over_y` | 1.40 | reading A1 (Section 1.4) |
| 142 | `blu25_swap_vertical_m` | [86, 92] um | reading A2, DERIVED, spot-checked |
| 143 | `blu25_swap_horizontal_m` | [10, 55] um | reading A2, DERIVED, spot-checked |
| 144 | `blu25_transversal_cnot_block_offset_m` | [65, 80] um | reading A4: "6.0 data column pitches x 12.1 um = 72 um" |
| 720 | `zhou25_site_spacing_m` | 12 um | ZHOU25 Table 1 |
| 676 | `zhao26_data_spacing_m` | 12 um | "Data atoms are spaced 12um apart both verti- cally and horizontally; ancilla atoms are placed 2um from the corresponding data atom for each gate [24, 41]." |

- **Not in `params.yaml`.** The BLU25 within-pair CZ distance (Rydberg pair spacing) is NOT FOUND. A pitch
  printed for the surface-code layout is also NOT FOUND (reading A3, `readings.yaml:83-91`: "Not printed as a
  spacing for the surface-code layout").
- **Deep-circuit layout labels** are in reading A3 and are for comparison only: storage column pitch 11 um, gap
  52 um, "8 rows and 16 columns of gate sites with a horizontal extent of 175 um".

### 2.5 Rabi frequencies
| Line | Key | Value | Quote |
|---|---|---|---|
| 377 | `eve23_two_photon_rabi_over_2pi` | 4.6e6 Hz | "maintaining a high two-photon Rabi fre- quency (Ω/2π =4.6 MHz)" |
| 378 | `eve23_time_optimal_gate_dimensionless_duration` | 1.215 | "which constitutes an exact gate with time (ΩT/2π)=1.215, i.e., slightly longer than a reso- nant single-atom 2π pulse." |
| 581 | `blu25_global_rotation_s` | 5e-6 s | "A global Raman path illuminating the entire array is used for global rotations (Rabi frequency of about 0.5 MHz, resulting in around 5 us rotations with composite pulse techniques35)" |
| 815 | `wang26_data_2pi_rabi_hz` | 918e3 Hz | "The data atom 2pi pulse is driven resonantly (Delta = 0) at Omega_data = 918 kHz." |
| 823 / 824 | `lib26_three_photon_rabi_hz` (40 kHz), `lib26_fs_rabi_hz` (120 kHz) | | as in file |

The BLU25 Rydberg Rabi frequency is NOT FOUND. Only the 270 ns CZ duration is present.

### 2.6 Trap depth and trap wavelength
- **BLU25 trap depth and wavelength: NOT FOUND** in `params.yaml`.
- **Present, but in other contexts:**
  - `man25_t2_dd` note "At reduced trap depth kB x 55 uK" (`params/params.yaml:419`);
  - YOK26 "532 nm tweezer light" (`:496`);
  - NOR24 459 nm and 423 nm tweezers (`:454-455`);
  - EVE23 "1013-nm scattering lifetime" (`:380`);
  - BLU24 AOD trap "about two times larger than the SLM trap depth" (`:553`, quote of `blu24_slm_to_aod_ramp_s`);
  - KUM26 "we estimate the average trap depth of the tweezers to be around 220 µK" (`params/quotes.yaml`,
    `kum26_statement_2`, not a computational param).

---

## 3. Experiments e39, e40, e41 and `atomclock/fom.py`

### 3.1 e39 / T4.0: the measured budgets (`experiments/e39_budget_decomposition/`)
**Design** (`README.md:10-58`, pre-registered 2026-09-26). Three measured budgets are each run through the timing
kernel. Then each component is replaced by a demonstrated primitive, one at a time and all together. The
substitution table is at `README.md:23-32`. The intrinsic components are at `:34-38`.

| Budget | CZ/gate layers per round | Per-round time budget (measured) | Code |
|---|---|---|---|
| B1 BLU25 memory round, 4.45 ms | 4 CZ layers. 4 intervals between gates (3 drawn moves + entry) | 4 x 0.47 ms = 1.88 ms in-zone (moves + CZ) + 2.57 ms swap (2 moves, 2 storage transfers). **Readout, cooling, reload and decoding are not in the round**: "The ancilla blocks are measured at the end of the experiment" (`README.md:11-13`; `run.py:78-81`). CZ is 4 x 270 ns, inside the intervals. | `run.py:64-81`, through `run_config()` `:26-37` on `configs/blu25_surface.yaml` |
| B2 BLU25 teleportation layer, 41.9 ms | Not a QEC round. Layer counts not given in e39 | circuit 13.5 + spin-to-position 4 + imaging 10 + cool/re-sort 13.3 (incl. ~7 ms processing) + re-init 1.1 = 41.9 ms (echo) | `run.py:83-106`, `serial()` `:40-45` |
| B3 AC26 det8 toric cycle, full reload, 232.1 ms | "the four gate layers", whose per-layer durations are not printed (`configs/ac26_toric.yaml:9-10`) | SE circuit 80 ms + move to MZ 2.9 + LAC 22.6 + MCM 33.7 + move back 2.9 + refill ~90; MOT/transport 60 in parallel | `run.py:108-130` on `configs/ac26_toric.yaml` |

**Result** (`README.md:66-81`, `table.md`):

| Budget | Measured | All substitutions | Remaining floor |
|---|---|---|---|
| B1 | 4.45 ms | 1.50-1.80 ms | BLU24 moves |
| B2 | 41.9 ms | 18.64 ms | circuit, cooling loop, re-init |
| B3 | 232.1 ms | 80.75-81.05 ms | 80 ms SE circuit |

- In B1, intervals alone 4 x 200 us = 0.8 ms gives 3.37 ms. The swap alone 2 x (200 + 100..200 + 50..100 us) =
  0.7-1.0 ms gives 2.58-2.88 ms.
- **Projected 2027-2030 range: 1.50-3.00 ms** (`run.py:132-150`).
  - Low: B1 all substitutions at the lo ends. LEE26's 45 us and BLU25's 1.1 ms re-init are pipelined on the stored
    block.
  - High: B1 at the hi ends, plus LEE26's 100 us and the 1.1 ms re-init in series.
- "No demonstrated substitution brings any measured budget to 1 ms" (`README.md:78`).
- **Caveat** (`README.md:44-45`): BLU24's 200 us move is assumed to hold at BLU25's 86-92 um swap distance.
- **Entry points:** `python experiments/e39_budget_decomposition/run.py`, which writes `results.json` and
  `table.md`. `check.py` verifies them.

### 3.2 e40 / T4.1: lifted-product schedules A to D (`experiments/e40_lp_schedule/`)
**Design** (`README.md:18-73`). The codes are CAIN26 LP(A, A†):
- lp20 [[4350,1224,≤20]], ℓ = 75;
- lp24 [[5278,1480,≤24]], ℓ = 91;
- lp16 [[2610,744,≤16]], ℓ = 45, for D only.

The seed matrix is 3 x 7, so the stabilizer weight is 10.

Layers per round, verbatim from `README.md:28-31`:
> **Layers per round:** D = r_A + n_A = 10. X and Z checks are measured at the same time on separate ancillas, as in
> ZHAO26's timing layout. A weight-10 check needs at least 10 CNOT layers, so D = 10 is a lower bound on depth.

The phrase "at least ten CNOT layers" is verbatim in `papers/g1b_audit/manuscript/main.tex:110` and
`papers/p1_which_lever/manuscript/main.tex:154`.

**Per-round composition, applied to every schedule.** The round is a serial kernel program
(`configs/cain26_lp.yaml:51-54`):

    layer_moves: (n_layers * moves_per_layer + n_return_moves) * t_move
    cz_layers:   n_layers * t_cz          (t_cz = blu25_cz_duration_s = 270 ns)
    measure:     t_mcm                     (lee26_mcm_feedforward_cycle_time = 45 us, not pipelined)

- τ = t_move = BLU24 200 us + ramp (100-200 us) + pull-away (50-100 us), which is 350 or 500 us
  (`cain26_lp.yaml:40-41`).
- No decoding time is included.

| Schedule | CNOT layers | Moves/layer m | Moves/round D·m+1 | T_c at τ = 350 / 500 us | Moves / CZ / readout share at τ = 350 us | τ for 1 ms |
|---|---|---|---|---|---|---|
| A, XU24 binary ladder, m = ⌈log2 ℓ⌉ | 10 | 7 | 71 | 24.8977 / 35.5477 ms | 24.85 ms / 2.7 us / 45 us | 13.4 us |
| B, ZHAO26 2-3 moves per step (`zhao26_moves_per_step`) | 10 | 2-3 | 21-31 | 7.3977 / 15.5477 ms | 7.35-10.85 ms / 2.7 us / 45 us | 45.3 / 30.7 us |
| **C, minimal, one parallel move per layer** | 10 | 1 | 11 | **3.8977** / 5.5477 ms | 3.85 ms / 2.7 us / 45 us | **86.6 us** |
| D, ONEX compiled lp16 (LIU26X Table 3, published, not modelled) | NOT FOUND (not modelled in e40) | - | - | 23.731 ms (ONEX), 21.405 ms (ONEX-Z) | - | - |

- lp20 and lp24 give identical numbers.
- Sensitivity with 8 layers (XU24's count) for A: 19.997-28.547 ms.
- **Distance-aware sensitivity for C** (`run.py:76-91`). The model is ZHOU25/ZHAO26 `t = 2 sqrt(L/a)` per layer
  with L = ⌈ℓ/2⌉ x 12 um, and a transfer only on the return move:

  | Code | L | a = 5500 m/s^2 | a = 2e4 m/s^2 |
  |---|---|---|---|
  | lp20 | 456 um | move 575.9 us, T_c 6.532 ms | 302.0 us, 3.520 ms |
  | lp24 | 552 um | move 633.6 us, T_c 7.167 ms | 332.3 us, 3.853 ms |

- **H2 verdict:** REFUTED under the pre-registered rule. The deciding case is C_lp20 at τ = 350 us, 3.8977 ms < 5 ms.
  No schedule reaches 1 ms.
- The closing note (`README.md:102-111`) says the verdict rests on a distance-independent move model that D007 had
  already superseded. Under distance-aware kinematics, C takes 6.5-7.2 ms.
- **Code entry points:**
  - `experiments/e40_lp_schedule/run.py`: `round_time(cfg, names, **over)` at `:26-29` gives the makespan of
    `configs/cain26_lp.yaml` with overrides (`moves_per_layer`, `t_move`, `n_layers`). Loops over schedules
    `:46-63`, H2 `:93-100`.
  - Runtimes: `runtimes_days = runtime(1 ms) x T_c / 1 ms` at `:56`.
  - Per-move time for 1 ms: `(1 ms - D t_CZ - t_MCM)/(D m + 1)` at `:57`.
- **Results:** `results.json` (git_commit `38502254...`, 2026-09-26).

### 3.3 e41 / T4.2: runtimes against cycle time (`experiments/e41_cain_audit/`)
**Design** (`README.md:5-48`). Runtime laws:
- **CAIN26:** runtime(T) = runtime(1 ms) x T / 1 ms, with ECC-256 10 d and RSA-2048 97 d at 1 ms.
- **XUE26 single module:** t0(T) = 164.5 d x (T + 10d us)/(1 ms + 10d us), with d = 25.
- **XUE26 6-QPU:** single-module law times XUE26's modular/single ratio, interpolated between its two printed
  points (`README.md:70-72`).

e41 composes no rounds. It takes T_c values from params and from the e10, e39 and e40 results. It defines no
layer count of its own: the layers are those of the upstream schedules.

**Result** (`table.md`, 12 audit rows plus schedules plus range). Rows nearest the new project:

| # | Kind | T_c | CAIN26 ECC-256 | CAIN26 RSA-2048 |
|---|---|---|---|---|
| 1 | assumed, UENO26 | 0.237 ms | 2.37 d | 23 d |
| 2 | assumed, CAIN26/XUE26 | 1 ms | 10 d | 97 d |
| **3** | **kinematic limit of the measured BLU25 schedule, e10 (D007)** | **1.344 ms** | 13.4 d | 130 d |
| 4 | projected, ZHAO26 | 2-4 ms | 20-40 d | 194-388 d |
| 5 | measured, BLU25 | 4.45 ms | 44.5 d | 432 d |
| - | schedule C (lp20) | 3.898-5.548 ms | 39-55.5 d | 378-538 d |
| - | T4.0 range | 1.5-3 ms | 15-30 d | 146-291 d |

- Anchors: 5 ECHO after the review correction (`README.md:62-69`).
- **Code entry points** (`experiments/e41_cain_audit/run.py`):
  - `class Laws` `:23-52`, with `cain(t)`, `xue_single(t)`, `xue_modular(t)` and `all(t)`;
  - audit rows `:71-94`. The kinematic row reads `experiments/e10_blu25_round/results.json` at
    `configs/blu25_surface/outputs/t_round_kinematic` (`:71`).

### 3.4 `atomclock/fom.py`: the R and C figure of merit
Definitions, verbatim from the module docstring (`atomclock/fom.py:1-13`):

    tau_c  wall-clock time of one syndrome-extraction cycle (readout, reset, amortized reload; decoding only where
           it sits on the critical path)
    r      syndrome-extraction rounds per logical operation: d for lattice surgery, 1 for transversal gates
    k      logical operations per layer (n_logical)

    R = k / (r tau_c)            logical operation rate, per second
    C = 1 / p_L                  capacity: logical operations before failure (the Quop count of MEN26)
    feasible(Q, T)  iff  C >= Q and R T >= Q

API (pure Python; imports only `math`, `re`, `dataclasses` and `atomclock.si`):

| Function | Line | What it does |
|---|---|---|
| `seconds(t)` | 31 | Parses 4.45e-3, (4.45, "ms") or "4.45 ms" |
| `rounds_per_op(mode, d)` | 56 | mode "lattice_surgery" gives d; "transversal" gives 1 |
| `logical_rate(n_logical, rounds, t_cycle)` | 65 | R |
| `capacity(p_logical)` | 77 | C = 1/p_L (inf at 0) |
| `error_per_op(p_round, rounds)` | 85 | 1 - (1 - p)^r |
| `operating_point(d, p_round, t_cycle, n_logical, mode, label=None)` | 106 | Returns a `Point(rate, capacity, ...)` |
| `feasible(rate, capacity, q_ops, t_budget)` | 123 | Returns a `Feasibility` (bool) |
| `pareto(points)` | 132 | Pareto frontier |
| `frontier_over_d(ds, p_round, t_cycle, n_logical, mode)` | 139 | Frontier over code distance |

How to call it:

    from atomclock import fom
    pt = fom.operating_point(d=5, p_round=0.0062, t_cycle="4.45 ms", n_logical=1, mode="transversal")
    pt.rate, pt.capacity                      # R in 1/s, C
    bool(fom.feasible(pt.rate, pt.capacity, q_ops=1e8, t_budget=(30, "s")))  # hypothetical Q and T

- The values in the first line are BLU25's operating point, from `configs/blu25_surface.yaml:113-118`. Q and T in
  the last line are hypothetical.
- **CLI:** `atomclock report --config configs/blu25_surface.yaml [--json]` (`atomclock/cli.py:1,54`). It goes
  through `atomclock/report.py:69` `build()` and `:55` `fom.operating_point(...)`.
- **Tests:** `tests/test_fom.py`, `tests/test_cli.py:25-27`.

---

## 4. `extra_z_flips` and `correlated_loss`: signatures, tests, vendoring

### 4.1 `atomclock/qec/repetition.py::extra_z_flips` (`:172-192`)
Signature:

    def extra_z_flips(d: int, rounds: int, data_z: np.ndarray, anc_z: np.ndarray | None) -> np.ndarray:

Docstring (verbatim):
> Measurement-record flips, shape (shots, n_records), of extra Z faults. data_z[s, r, q]: a Z on data qubit q at the
> end of cycle r. anc_z[s, r, a]: a Z on ancilla a before its measurement in cycle r (None: no such fault). A data Z
> stays until the end, so it flips the two neighbouring checks in every later cycle and the final result of its
> qubit; an ancilla Z flips its own result once.

**What it does.** It maps caller-sampled Z faults, which may be correlated across qubits (for example common-mode,
WP11), onto the bit flips of the measurement record of the X-basis repetition-code memory built by
`build_circuit`. The map is exact for Pauli faults in a Clifford circuit (module docstring `:14-19`):
- `data_z` has shape (shots, rounds, d); `anc_z` has shape (shots, rounds, d-1). Both are checked; a wrong shape
  raises ValueError.
- The cumulative parity `state` is computed by `np.logical_xor.accumulate`.
- Each check flips from the next cycle on.
- The final data results take the last parity.

**Consumer.** It is used by `logical_error_rate(..., extra_z=(data_z, anc_z))` at `:235-277`, which XORs the flips
into the Stim sample before detector conversion and decodes with PyMatching.

**Dependencies:**
- the function itself needs only `numpy` and `measurement_records(d, rounds)` (`:162-169`, numpy only);
- its record layout is that of `build_circuit` (`:87-159`, needs `stim`), with `RepetitionNoise` (`:35-69`),
  `Herald` (`:71-77`) and the constants `HALF`, `MIXED` (`:30-31`);
- the module imports `numpy`, `pymatching`, `stim` and `scipy.optimize.curve_fit` (`:21-29`; the last for
  `fit_lifetime`);
- the samplers used with it are in `atomclock/noise/common_mode.py` (`independent_flips` `:109`,
  `flips_from_phases` `:103`, `sample_phases` `:96`).

**Tests** (`tests/test_common_mode.py`):
- `test_record_layout_and_extra_z_flips_match_a_deterministic_circuit` (`:110-133`). It compares every single Z
  against a Stim circuit with that Z injected (`force_z`).
- `test_two_extra_z_on_one_qubit_cancel` (`:136-144`).
- `test_extra_z_route_agrees_with_the_circuit_channel` (`:147-161`).
- `test_extra_z_route_reproduces_the_exact_majority_formula` (`:164-177`).
- `test_extra_z_shape_is_checked` (`:180-185`).
- The circuit and records are also tested in `tests/test_qec_repetition.py` (13 tests, `:17-106`).

### 4.2 `atomclock/noise/correlated_loss.py` (76 lines)
The model is correlated two-atom loss in a CZ (PER26 Sec. II-B, Eq. 2, App. A; docstring `:1-8`):
- with probability p_l one atom, chosen uniformly, is lost;
- the partner is then also lost with probability p_c;
- otherwise the survivor gets the twirled channel Z 3/8, X 1/8, Y 1/8, I 3/8;
- if a partner was lost before the gate, the other atom is lost with probability 1.

| Signature | Line | Purpose |
|---|---|---|
| `per26_survivor_channel(store: provenance.ParamStore \| None = None) -> PauliChannel` | 22 | Reads `per26_twirled_survivor_xy` (0.125) and `per26_twirled_survivor_z` (0.375) from `params/params.yaml:186-187` (quote "error probabilities 1/8 for both X and Y errors, and 3/8 for Z errors") |
| `pc_from_marginal(p_marg: float, p_l: float) -> float` | 29 | Inverts Eq. 2: p_c = 2 p_marg/p_l - 1 |
| `@dataclass(frozen=True) class CorrelatedCZLoss(p_l: float, p_c: float, survivor: PauliChannel = per26_survivor_channel())` | 38-42 | The channel |
| `.marginal_loss() -> float` | 48 | p_l/2 (1 + p_c) |
| `.outcome_probabilities() -> dict[str, float]` | 52 | none_lost, a_lost, b_lost, both_lost |
| `.sample(rng: np.random.Generator, n: int, prelost: tuple[bool, bool] = (False, False)) -> dict` | 57 | Returns {"lost": bool (n,2), "pauli": str (n,2)} |

**Dependencies:**
- `numpy`;
- `atomclock.provenance` (`ParamStore`, `default_store()`). This is needed only for the default survivor channel:
  pass `survivor=` explicitly to avoid it;
- `atomclock.noise.channels`: `PauliChannel` (`:41-61` and following; `p_error`, `then`) and `_check_prob`
  (`:30-32`). `channels.py` imports only `math` and `dataclasses`.

**Tests:**
- `tests/test_noise_channels.py:190-268`: survivor channel = PER26 A4; exact outcomes; closed form; empirical
  marginal within 3 sigma; survivor twirled Pauli; prelost partner; invalid input; the EVE26 → p_c = 0.24 anchor
  `derived.eve26_pc_from_per26_eq2`.
- `tests/test_qec_layer2.py:13-44`.
- `tests/test_qec_erasure.py:7-58`.

### 4.3 Vendoring requirements
- **Licence.** `LICENSE` is MIT, "Copyright (c) 2026 rscaqsatiitm". A vendored copy must carry the copyright and
  permission notice.
- **NOTICE.** It lists one third-party item: the BootLoops skills under `.claude/skills/` (CC BY 4.0). It does not
  touch these modules, so no further terms apply to them.
- **Pinned versions** (`environment.lock`): `numpy==2.4.6`, `scipy==1.17.1`, `stim==1.16.0`, `pymatching==2.4.0`.
  `pyproject.toml:12-18` lists numpy, scipy, stim and pymatching.
- **Minimal file set:**
  - for `extra_z_flips` with its exact record semantics: `atomclock/qec/repetition.py` whole, or `extra_z_flips` +
    `measurement_records` + `build_circuit` + `RepetitionNoise` + `Herald` + `HALF`/`MIXED`, plus
    `atomclock/noise/common_mode.py` if its samplers are wanted;
  - for `correlated_loss`: `correlated_loss.py` + `channels.py` (`PauliChannel`, `_check_prob`), with
    `per26_survivor_channel` rewired to the new `params/registry.yaml` keys or `survivor=` passed explicitly.
- **Parent conventions that travel with the code:**
  - no numeric literal other than 0, 1, 2 in model code (`tests/test_provenance.py`; CLAUDE.md:10-12);
  - a vendored-file record with the upstream commit and hashes, as the parent does in `.claude/skills/VENDORED.json`;
  - copying the tests above. `test_pc_from_eve26_reproduces_derived_anchor` needs the parent's anchors and params.
- **Upstream commit for the record:** `7eb6b2e`.

---

## 5. Existing parent material on Rydberg P states, BBR, contaminants, and minimum inter-gate delays

1. **BLU25's own P-state statement.** Reading A5, verbatim (`plan/human_readings/readings.yaml:117-120`):
   > In quantum circuits based on atom motion, the duration between gates is sufficiently long (for example, 400 us
   > for surface code repeated stabilizer measurements) for these Rydberg P states to decay or eject

   The params location tag is "Methods (Rydberg P-state decay)" (`params/params.yaml:576, 583`). That subsection
   also gives "we have only 4 us between gates" for the randomized-benchmarking sequence (`:583`). The surrounding
   BLU25 sentences (P-state lifetime, ejection mechanism, error caused) are NOT FOUND in the parent.
2. **EVE23**, `params/quotes.yaml:92-95` (`eve23_statement_1`), full sentence:
   > Moreover, when running quantum circuits using atom transport ... the ∼ 100 us delay between subsequent gates
   > would result in leftover Rydberg states being expelled from the array, completely suppressing the effect from
   > Rydberg decay described above.

   EVE23 also gives the 88 us lifetime at n = 53, with radiative 170 us and blackbody 128 us
   (`params/params.yaml:380`).
3. **PEC26** ("Loss-biased fault-tolerant quantum error correction", source [25], `plan/anchors.yaml:43`):
   - `params/quotes.yaml:60-91` (`pec26_statement_1` to `_8`), including:
     - "shorter QEC cycles amplify platform- specific errors, notably Rydberg excitation hopping, and hinder decay
       of residual Rydberg popula- tion, leading to non-Markovian correlated errors";
     - "Given sufficient time (typically 100’s of us), residual Rydberg population generated by gate errors is
       likely to convert into qubit loss";
     - "Gate se- quences with 4µs spacing are therefore prone to these errors, whereas circuits implemented via
       atom rearrange- ment are not, as they allow time for decay or for ejection when traps are pulsed on [9]";
     - "Upon Pauli twirling, this non-Markovianity is revealed as spa- tially correlated (hook-like) multi-qubit
       error strings".
   - Params: `pec26_rydberg_p_state_lifetime` 100 us (`:473`), `pec26_gate_spacing` 4 us (`:474`),
     `pec26_trap_off_per_gate` 500 ns (`:472`).
   - `reports/librarian_pass2_findings.md:54-56`: "No threshold value, Rydberg decay rate in s^-1, or QEC cycle time
     is printed as a PEC26 result. The only decay parameter is dimensionless: "γ = 5×10−5Ωmax". The time scales in
     the PDF are cited from other work: 200−400 us per ancilla transfer, 500 ns trap-off, ∼100 us Rydberg P
     lifetimes, 4 us gate spacing ..."
4. **Cryogenic BBR suppression.**
   - ZHANG25: 147 us at 300 K and 306 us at 45 K for 70S (calculated); `params/quotes.yaml:128-131`: "The overall
     calculated Rydberg lifetime increases to 310μs ... compared to the total room-temperature radiative lifetime
     of 150 μs and the zero-temperature radiative lifetime of 370μs".
   - KUM26: "One important caveat of our design is that it does not shield the atoms from exposure to
     room-temperature blackbody radiation." (`params/quotes.yaml:120-123`).
5. **ARC-computed Rydberg lifetimes at 0 K and 300 K, for 133Cs, not 87Rb**:
   - files: `reports/cs_laser_power/research/model_rydberg_atomic.md:135-147` (table for n = 40-100: nS, nP1/2,
     nP3/2, nD3/2, nD5/2);
   - code: `reports/cs_laser_power/cs_laser/rydberg_atomic.py`, ARC 3.10.2, `getStateLifetime`, BBR sum to
     n + 30 (`:72-75`), convergence note at `:74-75`;
   - example values at n = 70 (0 K / 300 K): nS 344.0 / 139.3 us, nP3/2 922.0 / 212.1 us;
   - these are a different species from BLU25/EVE23 (Rb) and are not in `params/params.yaml`.
6. **Contaminant-P-state dipole exchange, P-state-induced correlated errors in parallel CZ layers, BBR transfer
   fractions, and any minimum inter-gate delay derived from P-state decay: NOT FOUND.** No experiment, config,
   derivation or decision record in the parent computes a P-state-limited gate spacing. The parent's only "minimum
   inter-gate delay" is the kinematic one of Section 1. The 400 us, 100 us and 4 us figures above are quoted
   statements, not model outputs. Searches covered `p-state`, `p state`, `blackbody`, `black body`, `bbr`,
   `contaminant`, `leftover`, `expelled`, `rydberg` over `*.md`, `*.tex`, `*.py`, `*.yaml`, `*.json`.

---

## 6. Parent provenance rules, and the spot-check record for the 8.6 x 12.1 um pitch

### 6.1 Rules
- **`CLAUDE.md:10-17`** (R1, with D009 and D014):
  - every numeric constant is a key of `params/params.yaml` with `value`, `unit`, `source`, and a verbatim `quote`;
  - no literal other than 0, 1, 2 in `atomclock/`;
  - "A value read from a figure carries `reading: <id>` ... with a location and a note on who read it and how
    (D009)";
  - assumed values carry `assumed: true`, `basis` and `replace_by`, are scored ASSUMED and are kept out of tallies
    (D014).
- **`docs/ACTION_PLAN.md:19-41`.** The full rules are R1 to R12. R3 (`:23`): "If a number is needed and no source
  ... contains it, the agent (a) records it as a parameter *range* with the bounds and their sources ... If no
  bounds exist either, the task is BLOCKED. Under no circumstances is a plausible value invented. The phrase
  "typical value" is banned unless followed by a source ID."
- **`docs/decisions/D009-figure-readings.md:12-25`.** A figure reading:
  - carries `reading: <id>`;
  - its quote is the caption with no digits;
  - its note states who read it, how, and whether it is DERIVED;
  - an uncertain reading is entered as `[lo, hi]` "never as a point picked inside it";
  - it is class D;
  - "Every value read by an agent rather than a person stays flagged for a human spot check until one is recorded
    in the reading's notes";
  - "A figure reading can be a model input, never a validation target."
- **Observation.** `blu25_data_pitch_aspect_x_over_y` is entered as a point value 1.40 with "+-10 %" in its note
  (`params/params.yaml:141`), not as a `[lo, hi]` range. This departs from D009 item 3.
- **`docs/decisions/D014-assumed-inputs.md:12-36`**: the ASSUMED class.
- **Enforcement:** `tests/test_provenance.py` (pinned in `plan/checker_pins.json`); `scripts/check_anchor.py`.

### 6.2 Spot-check record for the pitch (readings A1 and A3)
- `plan/human_readings/readings.yaml:6-7`: `needs_human_spot_check: []` and
  `human_spot_check_done: {by: RS, date: '2026-09-27', entries: [A1, A2, A4, D2], result: all confirmed}`.
- `readings.yaml:10`: "A1, A2, A4 and D2 spot-checked by RS on 2026-09-27, all confirmed; D009 flag lifted."
- A1 entry, `readings.yaml:26-28`:

      spot_check: {by: RS, date: '2026-09-27', result: confirmed, d009_flag: lifted,
        note: 'Checked against the PDF (ED6d, 6c, 6a): 4 CZ layers, 3 displacements, diagonal in the middle, no entry drawn; grid visibly wider than tall; gap and storage-pitch cross-checks hold.',
        prior_agent_crosscheck: 'Claude local session, 2026-09-26, automated spot detection'}

- A1 values, `readings.yaml:38-41`: `vertical_edge: 8.6`, `horizontal_edge: 12.1`, `diagonal: 14.8` (um).
- **How they were measured.** `readings.yaml:47-51`: x:y = 1.40 (118:84 px on a 3x upsample); automated re-measure
  39.5:28.0 px = 1.41 (ED6a) and 61.2:43.1 px = 1.42 (Fig. 3a). Cross-checks:
  - gap 43.0 um against the printed 40 um;
  - storage pitch 4.0 um against 165/38 = 4.3 um.

  Scale B (55 um / 6) makes every distance 7 % larger (x pitch 12.9 um).
- **A3**, `readings.yaml:84`: `value_ez_um: '8.6 (rows) x 12.1 (columns) data-lattice pitch, DERIVED'`. Status
  `done_derived`. A3 itself carries no `spot_check` mapping; the check is recorded on A1.
- **Owner's instruction sheet:** `plan/human_readings/SPOT_CHECK_A1_A2_A4_D2.md` (written 2026-09-27).
  - `:21-36` (A1): "The vertical pitch is tied to print (60 µm over 7 gate rows = 8.6 µm), so only the ratio is a
    reading. Agent value 1.40 to 1.42."
  - Where it states what would change a result, it says "a pitch ratio near 1.0 (the in-zone bound falls from
    92 µs to about 80 µs; verdict unchanged)".
- **Params notes** (`params/params.yaml:141-144`) end "human spot check by RS on 2026-09-27, confirmed: the D009
  flag is lifted."
- **Inconsistency to note.** `plan/anchors.yaml:106,115` and `plan/blocked/X1.2.md:70-72` still say "flagged for a
  human spot check" / "needs_human_spot_check". The readings file and params record the check as done.
