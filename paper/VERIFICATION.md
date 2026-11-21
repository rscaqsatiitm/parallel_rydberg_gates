# Verification notes for paper/main.tex (PRA draft, 2026-11-21)

Build: `python3 paper/make_figures.py` (repo root), then `pdflatex main; bibtex main; pdflatex main; pdflatex main`
(revtex4-2, apsrev4-2). 7 pages; abstract ~270 words, body ~4900 words (approximate script count, math tokens
included). No em dashes.

## Provenance ledger
Types: SOURCE (verified quote in literature/notes or params/registry.yaml), FIGURE (figure reading, human
check pending), COMPUTED (ARC 3.10.2 call), SIM (simulation in this repo, review before submission),
DERIVED (calculation shown).

| Value | Location | Type | Pointer |
|---|---|---|---|
| Rb87 53S1/2 mJ=+1/2, Omega/2pi 4.6 MHz, A, omega, phi0, delta0, Omega T/2pi 1.215, B 8.5 G, d 2 um, 450 MHz | Sec. II A | SOURCE | registry evered23.* (arXiv:2304.05420 Methods, ED Fig. 1) |
| T = 0.264 us | Sec. II A | DERIVED | 2pi x 1.215 / (2pi x 4.6 MHz) |
| 270-275 ns gate incl. rise | fn. | SOURCE | BLU25 "270-ns duration"; 275 ns EVE23 (registry note E02) |
| I_r/T = 0.1925; 0.387 for atom in |1> | Sec. II A, fn. | SIM | E02 README (c) |
| Gamma 2525, 2458 /s; p_c 2.53e-4 | Sec. II A | COMPUTED | E02 README, E05 |
| Branching 0.686 / 0.677 | Sec. II A | SOURCE | literature/notes/theory_and_jila.md:93 (arXiv:2611.06613) |
| Table I (Gamma, p_c, tau_P at 300/188/45/4 K) | Table I | COMPUTED/DERIVED | E05 output; p_c scaled by Gamma ratio |
| T_eff 188(8) K | Table I, Sec. V | SOURCE | theory_and_jila.md:46 |
| Leakage >= 80 % loss | Sec. II C | SOURCE | blu25_fig6g_traps.md:111 |
| Controls 0.999984, 0.9999936, 3.6e-6, 2e-6, 1.3e-8, 0.33, 1.2e-13 | Sec. II D | SIM | E01 README |
| Matrix-element agreement 3e-5, 0.2 MHz | Sec. II D | SIM | E03b README |
| E_full 0.6-0.9 (<=8 um), R_1/2 10-12 um, 0.62/0.22 at 12 um, 0.59/0.013, slopes -5.97..-6.04, leakage fractions, E_same/E_full 0.39, 0.5-1.3 | Sec. III, Fig. 1 | SIM | E02 README, summary.json |
| alpha_e -349.7, core 9.08, alpha_g 2071.5, 0.164, v_inf 0.177, 3.99 us, 14-16 us, 4-7 %, 2-4 % | Sec. IV B | COMPUTED/DERIVED | DV2 + independent check |
| U_g 1 mK, 10 uK | Sec. IV B | SOURCE | blu25_fig6g_traps.md:130 (EVE23) |
| U_g {0.5,1,2} mK, w {0.8,1.0,1.2} um | Sec. IV B | ASSUMED range | D007 (not sourced) |
| 852 nm; entangling-zone intensity half | Sec. IV B, fn. | SOURCE | blu25_fig6g_traps.md:107-108 |
| 18 um per 100 us; zone ~150 um | Sec. IV B | DERIVED / SOURCE | 0.177 x 100; 175 um horizontal extent (registry bluvstein26.gate_zone) |
| Fig. 6g data points | Sec. IV C, Fig. 2 | FIGURE | E06 README; human check pending |
| Row pitch 8.571 um | Sec. IV C | DERIVED from SOURCE | 60 um / 7 (blu25_fig6g_traps.md:57); interpretation flagged |
| Column pitch 12.0 um | Sec. IV C | FIGURE | parent readings (owner spot-check 2026-09-27) |
| Table II bands, medians | Table II | SIM | E06 verdict_output.txt |
| Floors 6.9e-4..1.08e-3, median 1.05e-3; sparse 1.7-6.9e-5; difference 5.0e-4..1.06e-3; 0.4-1.4e-4 | Sec. IV C, V A | SIM | E07 README |
| Measured difference 6.1(3.4)e-4 | Sec. IV C | DERIVED from FIGURE | E07 README |
| t_wait 235-300 us (1e-4), ~500/760/300 us (1e-5) | Sec. V, VI | SIM | E07, E09 |
| s_min 1.5-2.0, 1.1-1.2, 1.0; floors 45 K, 4 K | Sec. V B, Fig. 3b | SIM | E09 |
| E08 numbers (p_c Omega const 0.2 %, slopes, 58.7-59.2 vs 64, R_1/2 12.8/6.8, 1.88, floors, exponents) | Sec. V C, Fig. 3a | SIM | E08 README, analysis_output.txt, floor_output.txt |
| Omega 10-16 MHz for 1e-4 | Sec. V C | DERIVED | log interpolation, E08 README (v) |
| ~17 MHz peak at 53S | Sec. V C | SOURCE | registry evered26.Omega_peak_over_2pi |
| Table III rows 188/45/4 K | Table III | DERIVED | 300 K row x Gamma(T)/Gamma(300 K) |
| (8 p_c)^2 ~ 4e-6 | Sec. VI | DERIVED | 8 atoms within R_1/2 at 8.571 x 12 um pitch |
| 92 us kinematic bound; cycle ratios 0.3-2.2 and < 1.5 | Sec. VI | SIM (owner's parent repo + E09) | docs/parent_extract.md; E09; citation missing |
| 0.07 %, 4 us, 99.3 -> 99.5 %, 400 us, 256 qubits 8 x 16 | Sec. I | SOURCE | registry bluvstein26.* |

All SIM entries: review before submission.

## Open placeholders
1. [CONFIRM?] author list, affiliations, acknowledgments and funding.
2. [CONFIRM?] gate-site pitch: "7 rows over 60 um" reads as 60/7 = 8.57 um or 60/6 = 10.0 um; column pitch 12.0 um is a
   figure reading. Best settled by the authors (docs/questions_for_authors.md).
3. [REF?] the owner's wall-clock model (source of the 92 us kinematic bound and the lifted-product schedules).
4. [REF?] ARC citation: not read this session. Recalled, unverified: Sibalic et al., Comput. Phys. Commun. 220, 319
   (2017); Robertson et al., Comput. Phys. Commun. 261, 107814 (2021). Verify before use.
5. Journal references for arXiv entries not verified (recalled, unverified: Evered 2023 Nature 622, 268; Bluvstein
   Nature 649, 39 (2026); Cong PRX 12, 021049 (2022)). Currently cited by arXiv ID only. Bluvstein author list
   truncated ("others") in the bib.
6. PRA length and abstract limits not checked against the current APS author guide [CONFIRM?].

## Sourcing gaps and things the draft deliberately does not claim
- The mechanism, its measurement and the 400 us choice are credited to Bluvstein et al.; the draft does not claim the
  effect as new.
- The motion model is not supported as necessary by the data (stated in Sec. IV C).
- No logical error rate is reported (no circuit-level simulation was run).
- pairinteraction cross-check not run (container); the substitute shares quantum-defect data with ARC.
- Fig. 6g comparison: band ~4x wide; the post-hoc normal-sparse check is labelled as post hoc.
- Gate-speed scaling excludes scattering, finite blockade and pulse-distortion errors.

## Update 2026-11-21: logical consequence (Sec. V D, Table IV, abstract, discussion, conclusion)
| Value | Location | Type | Pointer |
|---|---|---|---|
| Logical error per round, base / corr / indep, d = 3, 5, 7, p = 1e-3, m = 1; X = 7.8, 9.8, 6.3 with intervals | Sec. V D, Table IV | SIM | experiments/E10_stim_correlated/README.md, analysis_output.txt |
| X = 3.7-5.6 at p = 2e-3; 2.0-7.7 at m = 3, 10 | Sec. V D | SIM | analysis_output.txt |
| "four to ten times" (abstract, conclusion) | abstract, Sec. VII | SIM summary | X range 3.7-9.8 at m = 1 over both p |
| sensitivity ~1 %; decoding with indep model gives same rates | Sec. V D | SIM | E10 README (sensitivity, D1) |
Assumptions to state to referees: code-qubit placement in the zone (D010 item 3, unsourced), baseline p unsourced,
failure = undetected loss (no erasure), matching decoder. Review before submission.
