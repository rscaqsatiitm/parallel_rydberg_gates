# Prior work and K1 verdict (Stage 0, 2026-11-20)

K1 fires if a paper (a) computes the inter-pair error from a blackbody (BBR) contaminant in parallel
CZ gates, or (b) simulates its effect on a code. Verbatim support for every entry is in
`literature/notes/*.md` (392 quotes, all passing `tools/verify_quotes.py` on 2026-11-20). Text was read
from arXiv PDFs (decision D001); journal versions not checked.

## Verdict: K1 does not fire.
No paper found computes (a) or simulates (b). The mechanism itself is not new: it is named,
measured and judged harmless for motion-based circuits by Bluvstein et al. (2026). The open part is
narrower than the handover assumed (see "Consequence for the project").

## Table

| Work | What it showed | What it did not show | K1 | Read |
|---|---|---|---|---|
| Bluvstein et al., Nature 649, 39 (2026), arXiv:2506.20661 | Methods: decay to adjacent P states is ~0.07 % of the gate error budget; P atoms live >100 us and "corrupt gates in distant sites" with 4 us between gates. ED Fig. 6g: CZ RB fidelity 99.3 % -> 99.5 % when inter-gate time is raised to 100 us; removed also by 2x site separation ("sparse") or lower density. 400 us between gates in QEC circuits; code simulations with uncorrelated errors only; no correlated-error excess in error-per-shot distributions | No error per contaminant, no R or theta dependence, no model of ED Fig. 6g, no code simulation with contaminant faults, no statement for architectures with short inter-gate times | Partial (strong) | Main, Methods, ED captions, ancillary error model; SI not on arXiv |
| Evered et al., Nature 622, 268 (2023), arXiv:2304.05420 | Neighbour covariance grows with number of CZ gates (ED Fig. 9b,d), attributed to P-state decay (1/R^3 shifts, hopping between sites) or detuning noise; ~100 us between gates in transport circuits would expel P atoms; crosstalk ~10 kHz negligible; no shot of 5053 with >=18 errors on 30 sites | Covariance not modelled; fit coefficients not given ("guide to the eye") | No (qualitative) | Full |
| Evered et al., arXiv:2604.25987 (2026) | 53S, ~2pi x 17 MHz peak, loss 0.054(2) % per atom per CZ; RB on sparse 8 of 17 sites "to reduce the effect of decay of Rydberg states to nearby P states" | No correlation analysis | No | Full incl. supplement |
| Zhang et al. (JILA), arXiv:2611.06613 | Dressing avalanches; Gamma_ava = N(P_Ryd+P_PN) Gamma_BBR^trig + ...; branching into (n-1)P+nP 0.686 (50S), 0.677 (60S) at 300 K; xi0 ~10-13 um; outlook: contaminants "could induce both erasure errors ... and correlated Pauli errors" in parallel-gate architectures | No gates, no code | Partial (outlook sentence) | Full |
| Cong et al., PRX 12, 021049 (2022), arXiv:2105.13501 | BBR-transferred atom blockades later Rydberg operations "within the interaction range", giving correlated Z errors; FT protocols that detect it | Contaminant = perfect blockader in one logical operation; no parallel layer, no 1/R^3 model, no spacing dependence, no threshold simulation | Partial (qualitative) | Full |
| Jandura, Pecorari, Pupillo, arXiv:2405.16621 (PRResearch) | Supp. S10: surface-code simulation with a BBR-populated extra level that blockades CZs inside one stabilizer; NH protocol loses FT, NP restores it | Intra-stabilizer only, no exchange, no other gate pairs, no spacing, reset every round | Partial on (b), intra-plaquette | Full PDF (sections) |
| Jin et al., arXiv:2610.40329 (cryogenic gates) | States contaminants give errors "correlated across space and time"; separation costs parallelism; cryogenics "may relax constraints on parallel" gates | No calculation | No (motivation) | Sections |
| Jin et al., arXiv:2602.05959 | Collective lifetime reduction at 12 um spacing attributed to one atom's BBR transition; names transversal gates as vulnerable | Lifetime study; "left for future work" | No | Sections |
| Geim et al., arXiv:2602.18555 | Loss correlations ~1/r^3 attributed to S-P interactions (analog simulation) | No gates | No | Sections |
| Li, Peng, Wang, arXiv:2608.17331 | Surface-code effect of inter-pair crosstalk vs spacing | vdW 1/r^6 only; no BBR, no leakage | No (different mechanism; method template) | Sections |
| Pecorari et al., arXiv:2604.21876 | Rydberg hopping within a CZ pair, temporal correlation in one 5-atom plaquette; cites BBR P-decay as dominant in experiments | Interactions zero or infinite; no inter-pair, no spacing | No | Full |
| Perrin, Roger, Pupillo, arXiv:2603.24237 | Correlated loss of CZ partners as a QEC resource | Partner-only, phenomenological | No | Full |
| Yu et al., arXiv:2411.04664 | MBQC with Rydberg decay; one remark on decay breaking blockade within a CZ | Not simulated; leaked atoms excluded from later gates | No | Full |
| Pattison, Krishna, Preskill, arXiv:2303.04798 | Mentions BBR transitions as a source of burst errors | No model | No | Sentence |
| Festa 2022 (arXiv:2103.14383), Goldschmidt 2016 (1510.08710), Boulier 2017 (1709.02460), Zeiher 2016 (1602.06313), Cao 2025 (2410.09746) | Facilitation, anomalous broadening, avalanche dephasing, dressing loss, contaminant removal by autoionization | No gates, no codes | No | Full |

Search record: `literature/notes/K1_search.md` (22 web searches, 13 arXiv API queries, Semantic Scholar
citers of Festa 2022 (25, all screened) and Evered 2023 (747, title-screened)). Not covered: Google
Scholar, paywalled versions, theses, conference abstracts; Evered citers with uninformative titles.

## Consequence for the project
1. "A contaminant causes inter-pair errors" is established experimentally (Bluvstein ED Fig. 6g,
   Evered 2023 ED Fig. 9). It cannot be a thesis.
2. The leading architecture avoids it by 400 us between gates; a logical-level penalty therefore
   exists only for architectures whose CZ layers are closer in time than the contaminant survival
   time (benchmarks, in-place or dual-species syndrome extraction, fast QEC cycles, dense gate
   zones). Whether such architectures are a realistic near-term target must be argued from sources,
   not assumed.
3. Remaining open, quantitative content: (i) E(R, theta, t) per contaminant from the published pulse;
   (ii) a zero-parameter account of Bluvstein ED Fig. 6g (inter-gate time and sparse/dense) and Evered
   2023 ED Fig. 9 (covariance vs gate number and neighbour class); (iii) a minimum inter-layer delay
   or spacing as a function of T, n and gate speed, and its cost in QEC cycle time or laser power.
   Item (ii) is a stronger K3 test than the handover planned: ED Fig. 6g is a controlled
   experiment that varies exactly our parameters.
