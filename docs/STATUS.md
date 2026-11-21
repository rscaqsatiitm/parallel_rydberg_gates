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
| E10 Stim (S4) | 4-10x penalty WITHDRAWN: decoder artefact (E18) |
| Addendum 2 (Cs) | E11-E15 done; DV3 checked; predictions frozen in docs/predictions_cs_synthetic_bath.md, tag cs-predictions-v1 |
| Addendum 3 | E16 (extra channels < 3e-4 rel.; earlier layers +3-4 %; pitch 10.0 lowers floor 21-34 %); E17 (Cs 3-atom floor, vdW window); E18 (X_best 1.5-3.3, flat to d = 11, heralding eta >= 0.8 removes 85-97 % of excess; V1a partial, V1b not recovered at d = 7, V2 flat); E19 (Cs defects confirmed); E03 still BLOCKED; predictions v2 (854427e, tag cs-predictions-v2 local only) |
| Journal | docs/journal_recommendation.md: PRA |
| Paper (PRA draft) | paper/main.tex, 9 pages, Table IV from E18 |

Key numbers (provenance in experiment READMEs): p_c = 2.53e-4 per atom per CZ (Rb 53S, 4.6 MHz,
300 K), p_c ~ Omega^-1; tau_P(300 K) = 96-102 us; half-error radius 10-12 um at 4.6 MHz; BLU25-zone
same-layer floor 0.7-1.1e-3 per CZ at 300 K and 4.6 MHz, 1.4-3.1e-4 at 9.2 MHz, 2.3-7.6e-5 at 18.4 MHz.
Open human checks: figure-read values (Fig. 6g, pitches), journal vs arXiv versions, RB convention;
questions for authors in docs/questions_for_authors.md (owner sends, not us).

Note (2026-11-21): the predictions were frozen in commit c4d0393 on branch ccr-825341ea-tdqiim (pushed). The annotated
tag cs-predictions-v1 exists only in the session's local clone: pushing tags was refused by the session's git access
(HTTP 403); the owner should create and push it on c4d0393 (`git tag -a cs-predictions-v1 c4d0393 -m "..."`).

Note (2026-11-21, Addendum 3): tag cs-predictions-v2 on 854427e is likewise local only; the owner should create and push both tags.
