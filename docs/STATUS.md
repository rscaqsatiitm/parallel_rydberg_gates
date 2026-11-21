# Status (updated 2026-11-20, end of autonomous run)

Scope: Addendum 1 (thermal speed limit of the QEC cycle). **Gate 2 not passed**; report and
recommendation in docs/gate2_report.md. No letter draft started. Circuit-level stage done (E10).

| Item | State |
|---|---|
| K1 prior work | not fired (docs/prior_work.md, K1_cycle_search.md) |
| E00 handover estimate | reproduced (not a result) |
| E01 model controls | pass, one recorded FAIL (high-blockade pulse fidelity 6e-6 short; immaterial) |
| E02 error map (4.6 MHz) | done; tail slope -6.0 PASS |
| E03 pairinteraction check | BLOCKED (database download impossible here); substitute E03b PASS (3e-5) |
| E04 K2 under D003 | superseded by D006 (not run) |
| E05 rates vs T | done |
| E06 K3 vs BLU25 ED Fig. 6g | K3 NOT fired (all 4 points within band; not discriminating) |
| E07 K2 under D006 | K2 NOT fired (same-layer floor 0.7-1.1e-3 > 1e-4) |
| E08 maps vs Omega | both verdicts PASS; floor ~ Omega^-2 to -2.6 |
| E09 cycle floor (Gate 2) | NOT passed at 300 K (thermal/kinematic 0.3-2.2, below 2 over declared range) |
| DV1, DV2 | written; independently checked (DV2 arithmetic slip corrected) |
| E10 Stim (S4) | correlated floor costs 4-10x the equal-marginal independent model (d = 3-7); no distance penalty |
| Addendum 2 (Cs) | E11-E15 done; DV3 checked; predictions frozen in docs/predictions_cs_synthetic_bath.md, tag cs-predictions-v1 |
| Paper (PRA draft) | paper/main.tex, 8 pages, includes E10 |

Key numbers (provenance in experiment READMEs): p_c = 2.53e-4 per atom per CZ (Rb 53S, 4.6 MHz,
300 K), p_c ~ Omega^-1; tau_P(300 K) = 96-102 us; half-error radius 10-12 um at 4.6 MHz; BLU25-zone
same-layer floor 0.7-1.1e-3 per CZ at 300 K and 4.6 MHz, 1.4-3.1e-4 at 9.2 MHz, 2.3-7.6e-5 at 18.4 MHz.
Open human checks: figure-read values (Fig. 6g, pitches), journal vs arXiv versions, RB convention;
questions for authors in docs/questions_for_authors.md (owner sends, not us).
