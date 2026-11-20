# Status (updated 2026-11-20, autonomous run)

Scope: Addendum 1 (thermal speed limit of the QEC cycle). K1 not fired (docs/prior_work.md,
literature/notes/K1_cycle_search.md). K2 per D006; K3 per E06 pre-registration.

| Item | State |
|---|---|
| E00 handover estimate | reproduced (not a result) |
| E01 model controls | pass, one recorded FAIL (high-blockade pulse fidelity 6e-6 short; immaterial) |
| E02 error map (2023 config) | whole-gate part done, same-layer part running |
| E03 pairinteraction check | BLOCKED (database download impossible here); substitute E03b running |
| E04 K2 under D003 | pre-registered, waits for E02 |
| E05 rates vs T | done |
| E06 K3 vs BLU25 ED Fig. 6g | pre-registered; stage A (trajectories) running; stage B coded |
| DV1 delay law, DV2 motion | written; independent check running |
| Stage 3 | not started (needs E06 verdict and maps at other Omega) |

Key numbers so far (provenance in experiment READMEs): p_c = 2.53e-4 per atom per CZ (Rb 53S,
4.6 MHz, 300 K, inputs-averaged Rydberg time I_r/T = 0.192); tau_P(300 K) = 96-102 us; P-state hill
0.164 U_g at 852 nm; v_inf = 0.177 um/us at U_g = 1 mK; median contaminant distance from its site
8.1 / 16.7 / 33.8 um at 50 / 100 / 200 us (U_g 1 mK, w 1 um, 8.571 x 12.0 um lattice).
Open human checks: figure-read values (Fig. 6g, pitches), journal vs arXiv versions.
