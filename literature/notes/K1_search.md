# K1 prior-art search: BBR contaminant crosstalk between parallel Rydberg CZ gate pairs

Search date: 2026-11-20. Searcher: Claude Code subagent.

K1 fires if a paper (a) computes the error that a BBR contaminant Rydberg atom (nS transferred to n'P during a gate) causes on OTHER neighbouring gate pairs in a parallel CZ layer through resonant dipole exchange (1/R^3), or (b) simulates such spatially correlated, contaminant-induced multi-pair errors in a QEC code.

Already-known papers were excluded from re-reporting: 2611.06613, 2304.05420, 2604.25987, 2105.13501, 2411.04664, 2603.24237, 2604.21876, Bluvstein Nature 649, 39 (2026) (= arXiv 2506.20661, which appeared in results), Festa 2022 (2103.14383), Goldschmidt 2016, Boulier 2017, Zeiher 2016, and Cao 2025 PRL 134 133201 (= arXiv 2410.09746, which appeared in results). Other agents are reading those.

## 1. Queries run

All queries were run on 2026-11-20.

| # | Tool | Mode | Query |
|---|------|------|-------|
| 1 | WebSearch | extended | blackbody contaminant Rydberg atom parallel CZ gates crosstalk neighbouring pairs |
| 2 | WebSearch | extended | Rydberg leakage correlated errors surface code simulation neighbouring gates neutral atoms |
| 3 | WebSearch | extended | blackbody-induced transfer nP state resonant dipole exchange neighbouring qubits Rydberg gate error |
| 4 | WebSearch | extended | correlated errors Rydberg decay into adjacent Rydberg states neutral atom quantum error correction |
| 5 | WebSearch | extended | Rydberg gate array minimum site spacing limit blackbody radiation leakage parallel gates density |
| 6 | WebSearch | extended | spatially correlated errors neutral atom surface code Rydberg leakage spreading to neighbours |
| 7 | WebSearch | extended | "anomalous broadening" Rydberg blackbody contaminant atoms facilitation |
| 8 | WebSearch | extended | leakage-induced crosstalk between gate pairs Rydberg atom array residual Rydberg population neighbouring gate |
| 9 | WebSearch | extended | blackbody radiation Rydberg CZ gate error budget parallel gates contaminant neighbouring pair dipole-dipole 2025 |
| 10 | WebSearch | extended | Rydberg leakage to other Rydberg states blocks neighbouring atoms correlated errors qLDPC neutral atoms simulation |
| 11 | WebSearch | extended | "Rydberg leakage" spatially correlated "multi-qubit" errors decoder neutral atom 2026 |
| 12 | WebSearch | standard | long-lived Rydberg leakage blackbody nP state remains in Rydberg manifold subsequent gates blockade neighbouring qubits error |
| 13 | WebSearch | standard | thermal Rydberg state redistribution resonant exchange interaction spectator gate pair error neutral atom quantum computer |
| 14 | WebSearch | standard | Rydberg avalanche facilitation quantum processor gate array scaling limit blackbody contaminants |
| 15 | WebSearch | standard | cryogenic Rydberg atom array collective effects one Rydberg atom transitions different Rydberg state neighbours loss 2026 |
| 16 | WebSearch | standard | correlated Rydberg-induced loss neighbours gate zone neutral atom error correction spatial clustering errors simulation |
| 17 | WebSearch | extended | BBR contaminant Rydberg atom transversal entangling gate logical qubits correlated dephasing loss estimate |
| 18 | WebSearch | extended | leaked Rydberg atom spectator qubit resonant dipole-dipole interaction 1/R^3 gate infidelity neighbouring CZ gate |
| 19 | WebSearch | standard | burst errors blackbody radiation Rydberg neutral atom quantum error correction simulation clustered errors |
| 20 | WebSearch | standard | gate parallelism tradeoff correlated errors Rydberg contaminant spatial and temporal separation between gates neutral atom |
| 21 | WebSearch | standard | autoionization contaminant removal Rydberg entangling gates parallel array correlated errors strontium ytterbium |
| 22 | WebSearch | extended | "blackbody" "neighboring gate" OR "neighbouring gate" Rydberg hopping P state detuning shift parallel entangling gates error model |
| A1 | arXiv API | sortBy=submittedDate, max 50 | all:blackbody AND all:Rydberg AND all:gate |
| A2 | arXiv API | same | all:blackbody AND all:Rydberg AND all:correlated |
| A3 | arXiv API | same | abs:Rydberg AND abs:leakage AND abs:correlated |
| A4 | arXiv API | same | abs:black-body AND abs:Rydberg AND abs:qubit |
| A5 | arXiv API | same | abs:blackbody AND abs:Rydberg AND abs:error |
| A6 | arXiv API | same | abs:Rydberg AND abs:leakage AND abs:surface AND abs:code |
| A7 | arXiv API | same | abs:contaminant AND abs:Rydberg |
| A8 | arXiv API | same | abs:Rydberg AND abs:parallel AND abs:gates AND abs:crosstalk |
| A9 | arXiv API | same | abs:Rydberg AND abs:spatially AND abs:correlated AND abs:errors |
| A10 | arXiv API | max 30 | abs:Rydberg AND abs:avalanche |
| A11 | arXiv API | max 30 | abs:Rydberg AND abs:opposite AND abs:parity AND abs:gate (0 results) |
| A12 | arXiv API | max 30 | abs:Rydberg AND abs:leakage AND abs:neighboring |
| A13 | arXiv API | max 40 | abs:neutral AND abs:atom AND abs:correlated AND abs:errors AND abs:code |
| S1 | Semantic Scholar API | citations | arXiv:2103.14383 (Festa et al. PRA 105, 013109): 25 citing papers, all titles screened |
| S2 | Semantic Scholar API | citations | arXiv:2304.05420 (Evered et al. 2023): 747 citing papers, titles screened by keyword (blackbody, crosstalk, correlated, leakage, spacing, parallel, QEC/code/fault/decoder); about 30 downloaded and grepped |

For every downloaded PDF, the full text was grepped for `blackbody|black-body|black body|BBR|contaminant` (plus `neighbo|correlat|dipol|spacing` where relevant), and the matching sections were read.

## 2. Candidate table

The "How read" column says how much of each paper was read. "Full PDF (grep + sections)" means the whole PDF was downloaded and converted to text, every BBR and contaminant passage was found by grep, and those sections were read in context.

| arXiv / DOI | Authors | Year | Title | What it shows | What it does NOT show (vs. a, b) | Verdict | How read |
|---|---|---|---|---|---|---|---|
| 2405.16621 (PRResearch, doi 10.1103/2jk3-wdfz) | Jandura, Pecorari, Pupillo | 2024/2025 | Surface Code Stabilizer Measurements for Rydberg Atoms | Supp. S10 runs surface-code simulations with a BBR-populated extra Rydberg level r'. A spectator in r' blockades data-data CZs within the stabilizer, which breaks fault tolerance of the NH protocol (ceil(d/4) instead of ceil(d/2)). The NP protocol restores it. The paper also states that P states "can perturb neighboring atoms". | r' is modelled as an ordinary blockade only inside one stabilizer's atoms (all-to-all or data-ancilla blockade). There is no 1/R^3 resonant exchange, no effect on other gate pairs in a parallel layer, and no distance or spacing dependence. Contaminants are reset at the end of the round, so there is no inter-pair or inter-round spreading. This is the closest to (b), but only intra-stabilizer. | PARTIAL OVERLAP (b, intra-plaquette only) | Full PDF (grep + S10, S11, intro) |
| 2610.40329 | Jin, Seo, Shi, Lu, Thompson, Bakr | 2026 | High-Fidelity Universal Quantum Gates in a Cryogenic Atom Array | States qualitatively that BBR contaminants with long-range dipolar interactions cause errors correlated across space and time. It says that increasing gate separation costs parallelism and that cryogenics "may relax constraints on parallel" gates. It computes the vdW/P-P interpair shift (-1.6 kHz at 12 um) for its own 7-pair layer. | No calculation of the contaminant-induced error on other pairs, no 1/R^3 resonant-exchange error, no spacing bound and no QEC simulation. It cites Bluvstein 2026, Evered 2026 (Science 394, 197), Goldschmidt 2016 and Festa 2022 for the claim. | PARTIAL OVERLAP (qualitative motivation only) | Full PDF (grep + intro, Sec. on geometry, outlook) |
| 2602.05959 | Jin, Shi, Aziz Alaoui, Deng, Lu, Thompson, Bakr | 2026 | Extended Rydberg Lifetimes in a Cryogenic Atom Array | Observes collective non-exponential decay in a 7x7 array at 12 um spacing (but not at 24 um), which it attributes to one atom's BBR transition plus dipolar shifts of up to 1 MHz on neighbours. It argues that a transversal gate between logical qubits is vulnerable to this. | Lifetime-measurement protocol, not CZ gate pairs. No gate-error calculation for neighbouring pairs, no QEC simulation, and "left for future work". | PARTIAL OVERLAP (experimental observation, qualitative) | Full PDF (grep + main text end, Supp. S3) |
| 2602.18555 | Geim, Koylyoglu, Evered, ... Lukin | 2026 | Engineering quantum criticality and dynamics on an analog-digital simulator | Measures loss correlations in analog Rydberg dynamics (271 atoms). The two-point loss correlator decays as 1/r^3, attributed to BBR S to P transitions and avalanche. | Analog many-body evolution, not CZ gate layers. No gate-error model, no QEC. Used only for post-selection. | PARTIAL OVERLAP (empirical 1/r^3 signature, not gates) | Full PDF (grep + Methods "Loss in analog simulations", ED Fig. 2) |
| 2608.17331 | Li, Peng, Wang | 2026 | Beyond Legal Spacing: A Residual-Aware Characterization of Entangling-Zone Spacing in Neutral-Atom Compilation | Inter-pair crosstalk in parallel Rydberg stages as a function of spacing. Residual vdW C6/r^6 ZZ is Pauli-twirled into correlated faults, surface-code simulation (d=5,7) uses a matched correlated decoder, and the work recommends spacing slack beyond the 10 um floor. | Mechanism is coherent vdW 1/r^6 between intended pair members. No BBR, no contaminant, no leakage, no 1/R^3 (grep for blackbody/BBR/leak/dipol returns nothing). Methodologically analogous to (b) but a different mechanism. | PARTIAL OVERLAP (framework analogue of (b), different physics) | Full PDF (abstract, Secs. I-II, grep) |
| 2303.04798 | Pattison, Krishna, Preskill | 2023/2025 | Hierarchical memories: Simulating quantum LDPC codes with local gates | One sentence names BBR transitions to other Rydberg states (citing Festa 2022 and Zeiher 2016) as a source of "burst errors" that can wipe out patches, and argues that hierarchical codes are robust to them. | Does not model or simulate BBR bursts. Qualitative only. | PARTIAL OVERLAP (weak; qualitative mention as code-design motivation) | Full PDF (grep + discussion paragraph) |
| 2412.09780 | Zhang, Hsu, Tan, Slichter, Kaufman, Marinelli, Regal | 2024 | A high optical access cryogenic system for Rydberg atom arrays with a 3000-second trap lifetime | Qualitative statement that BBR opposite-parity populations "degrade gate fidelities in large arrays", citing Saffman 2016 and Evered 2023. | No calculation. | NO (qualitative only) | Full PDF (grep + intro) |
| 2410.09746 (= Cao et al. PRL 134 133201) | Cao, Yelin, Eckner, Darkwah Oppong, Kaufman | 2024/2025 | Autoionization-enhanced Rydberg dressing by fast contaminant removal | Removes BBR contaminants by autoionization during dressing. Collective loss is triggered by a single contaminant. | Dressing, not gates. No QEC. (Covered by another agent.) | NO for K1 (already assigned) | Full PDF (grep + intro) |
| 2409.04324 | (Geometrical approach authors) | 2024 | Geometrical Approach to Logical Qubit Fidelities of Neutral Atom CSS Codes | Treats BBR as independent erasure (Gamma_BBR) in a toric-code phase diagram. | Errors are uncorrelated per qubit. No neighbour or contaminant interaction. | NO | Full PDF (grep + Sec. on erasure) |
| 2507.06096 | Pecorari, Jandura, ... Pupillo | 2025 | Low-depth quantum error correction via three-qubit gates in Rydberg atom arrays | Mentions BBR only as a route back to the ground state and as a spoiler of Z bias. | No inter-pair contaminant effects. | NO | Full PDF (grep) |
| 2503.01649 (PRA 113, 042451) | (SWAP-LRC authors) | 2025/2026 | Locating Rydberg Decay Error in SWAP-Leakage Reduction Circuit Protocol | Correlated decay errors within the gate. BBR leaked state is not involved in subsequent gates. | Assumes the leaked state does not interact with others. No inter-pair effect. | NO | Full PDF (grep) |
| 2607.29603 | Nishio et al. | 2026 | Qubit Loss Inference with Stabilizer Codes without Leakage Detection Units | Mentions BBR as a loss source. | No spatial contaminant model. | NO | Full PDF (grep) |
| 2610.38283 | (anonymous in extraction) | 2026 | Maximally-Matched Mixture Decoding for Correlated Atom Loss in Quantum LDPC Codes | qLDPC decoding with correlated loss of both atoms of one gate. | Correlation only within a gate pair. No BBR or inter-pair. | NO | Full PDF (grep) |
| 2607.02804 | Bergonzoni, Pecorari, ... | 2026 | Fault-tolerant quantum computation with static atomic buses | Mentions that cryogenics suppresses BBR, and includes BBR in the lifetime scaling. | No contaminant crosstalk. | NO | Full PDF (grep) |
| 2604.07205 | Lim, Mamann, ... (Browaeys/Lahaye group) | 2026 | Defect-free arrays at the thousand-atom scale in a 4-K cryogenic environment | BBR shortens lifetimes. Motivation only. | Nothing on contaminant crosstalk. | NO | Full PDF (grep) |
| 2407.03249 | Manovitz, Li, Ebadi, ... Lukin | 2024/2025 | Quantum coarsening and collective dynamics on a programmable simulator | Discards shots with long chains of apparent blockade violations, attributed to BBR avalanches. | Analog simulator, no gates or QEC. | NO | Full PDF (grep) |
| 2210.03763 | (Tree-tensor-network digital-twin authors) | 2022 | Ab-initio tree-tensor-network digital twin for quantum computer benchmarking in 2D | Crosstalk vs. parallelization trade-off for Rydberg gates (vdW). | No BBR (grep empty). | NO | Full PDF (grep) |
| 2610.38604, 2611.15104, 2610.26471, 2609.10079, 2608.27568, 2607.08767, 2512.00843, 2406.18897, 2609.29018, 2601.01990, 2606.04079, 2611.12098, 2504.15282, 2611.24078 | various | 2024-2026 | (Evered-citers on QEC/parallel gates/crosstalk; titles in S2 list) | Downloaded and grepped. | Zero or only bibliographic hits for blackbody/BBR/contaminant. 2610.38604 is about transmon crosstalk. 2406.18897 covers generic error bursts with no Rydberg mechanism. | NO | Full PDF (grep only) |
| 2507.10356 (Quantum 2026) | (Suppressing crosstalk authors) | 2025 | Suppressing crosstalk for Rydberg quantum gates | Crosstalk on a spectator from addressing-laser leakage. | Laser crosstalk, not BBR or contaminant. | NO | Abstract/search snippet only |
| 1510.08710 / PRL 116 113001 | Goldschmidt et al. | 2016 | Anomalous broadening in driven dissipative Rydberg systems | (Assigned to another agent.) | Lattice gas, no gates. | not re-assessed | search snippet only |

No candidate FIRES K1.

## 3. Verbatim quotes (PARTIAL entries)

### arXiv_2405.16621 (Jandura, Pecorari, Pupillo)
Q[arXiv_2405.16621]: "A Rydberg leakage error on a single qubit can prevent the execution of two-qubit gates on all of its neighbors, via the Rydberg blockade mechanism"
Q[arXiv_2405.16621]: "Moreover, through stimulated absorption or emission of black body radiation (BBR) it is also possible to cause the excitation of a different Rydberg state. While not directly captured in our model"
Q[arXiv_2405.16621]: "Experimentally, BBR can populate higher-lying or nearby P states with longer-range or anisotropic interactions that can perturb neighboring atoms."
Q[arXiv_2405.16621]: "By contrast, the NP protocol is immune by design to these types of errors and restores the favorable logical-error scaling in the presence of BBR processes."
Q[arXiv_2405.16621]: "Hence, BBR-induced decays within a stabilizer round can be absorbed into our noise model by increasing the effective decay probability to"

### arXiv_2610.40329 (Jin, Seo, Shi, Lu, Thompson, Bakr)
Q[arXiv_2610.40329]: "Rydberg states whose strong, long-range dipolar interactions perturb subsequent operations, introducing errors correlated across space and time [10, 24, 25]."
Q[arXiv_2610.40329]: "Such errors can be reduced by increasing the spatial and temporal separation between gates [10, 21], but at the cost of reduced gate parallelism and a lower effective clock rate."
Q[arXiv_2610.40329]: "At this spacing, the interaction shift between atoms in neighboring pairs is approximately −1.6 kHz, making interpair crosstalk negligible."
Q[arXiv_2610.40329]: "More broadly, suppressing BBR-induced contaminant Rydberg states may reduce correlated errors and relax constraints on parallel and repeated gate operations."

### arXiv_2602.05959 (Jin, Shi, Aziz Alaoui, Deng, Lu, Thompson, Bakr)
Q[arXiv_2602.05959]: "Consider, for example, a transversal entangling gate between logical qubits, as demonstrated in [5]."
Q[arXiv_2602.05959]: "A BBR transition transfers an atom to a different Rydberg state that couples to the rest of the excited atoms via long-range dipoledipole interactions, inducing correlated dephasing and loss [9, 37–39]."
Q[arXiv_2602.05959]: "We attribute this to collective effects induced by the transition of one Rydberg atom into a different Rydberg state."
Q[arXiv_2602.05959]: "A more detailed investigation of the collective effects is left for future work."

### arXiv_2602.18555 (Geim et al., Lukin group)
Q[arXiv_2602.18555]: "Furthermore, the two-point loss correlations decay as 1/r3 for radial separation r (ED Fig. 2b), consistent with dipolar S-P interactions that can tune otherwise unpopulated blockade-violating states into resonance."

### arXiv_2608.17331 (Li, Peng, Wang)
Q[arXiv_2608.17331]: "Legal spacings just above the device floor can still induce correlated ZZ-like faults."
Q[arXiv_2608.17331]: "The results show that near-floor spacing can produce structured correlated exposure that is visible both at the physical layer and, in the tightest case, after quantum error correction (QEC)."

### arXiv_2303.04798 (Pattison, Krishna, Preskill)
Q[arXiv_2303.04798]: "or blackbody radiation mediated transitions to other Rydberg states in neutral atom platforms [Fes+22; Zei+16]."

### arXiv_2412.09780 (Zhang ... Regal), NO but noted
Q[arXiv_2412.09780]: "These unwanted interactions cause rapid many-body loss effects that impair the study of spin models [45, 46], and also degrade gate fidelities in large arrays and when operating with high gate depth [21, 23]."

## 4. Limits of this search

- Semantic Scholar citation lists were reachable for Festa 2022 and Evered 2023 (after rate-limit retries). For Evered (747 citers), only titles were screened by keyword, and about 30 papers were downloaded. A paper with an uninformative title could be missed.
- Google Scholar was not used, and APS/Nature full texts behind paywalls were not checked. Only arXiv versions were read.
- Conference proceedings and theses (e.g. DAMOP abstracts, PhD theses from the Lukin, Saffman, Gross or Bakr groups) were not searched systematically. The DAMOP 2026 "Rydberg atom arrays in a cryogenic environment" abstracts were seen only as search hits.
- Not finding a paper in these searches does not show that none exists. Within the reachable literature, though, no paper computes contaminant-induced errors on other parallel gate pairs via 1/R^3 exchange, and none simulates such inter-pair contaminant errors in a QEC code. Up to 2026-11 the literature names the mechanism qualitatively, observes it experimentally (2602.05959, 2602.18555, plus the known 2611.06613 and Evered papers), or models BBR leakage only inside one stabilizer (2405.16621).
