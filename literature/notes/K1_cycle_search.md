# K1 (extended) prior-art search: minimum inter-gate delay / QEC cycle time set by BBR Rydberg P-state contaminants

Search date: 2026-11-20. Searcher: Claude Code subagent. This builds on `K1_search.md` and `docs/prior_work.md` and does not repeat their queries.

Retargeted claim under test: "the minimum time between Rydberg gate layers, and hence the minimum QEC cycle time, set by BBR-created Rydberg P-state contaminants (lifetime ~100 us), as a function of temperature T, Rabi frequency Omega, n and gate-site spacing R".

K1 (extended) FIRES if a paper does one of the following:
- (i) derives a minimum inter-gate delay, wait time or cycle-time limit from Rydberg contamination, leakage, residual Rydberg population or BBR P states;
- (ii) analyses the QEC clock speed or cycle time of a neutral-atom processor including a Rydberg-contamination term;
- (iii) proposes or demonstrates active removal of Rydberg P-state or residual Rydberg atoms between gates *for speed*;
- (iv) computes the anti-trapping or ejection time of Rydberg atoms from optical tweezers.

For (iii) and (iv), "fires" means the paper does this in the context of the gate-delay or cycle-time question. Generic removal or ejection data are logged as PARTIAL, with their numbers, because they are inputs to our model.

## 1. Queries run (2026-11-20)

| # | Tool | Mode | Query |
|---|------|------|-------|
| W1 | WebSearch | extended | minimum time between Rydberg gates residual Rydberg population blackbody P states delay neutral atom |
| W2 | WebSearch | extended | neutral atom quantum error correction cycle time limit Rydberg leakage wait time between gate layers |
| W3 | WebSearch | extended | removal of residual Rydberg atoms between gates ionization pulse field ionization neutral atom quantum computer |
| W4 | WebSearch | extended | Rydberg atom ejection from optical tweezer ponderomotive anti-trapping time trap turned back on |
| W5 | WebSearch | extended | "Rydberg quench" OR "de-excitation pulse" residual Rydberg population return to ground state between gates leakage reduction |
| W6 | WebSearch | extended | QEC cycle time neutral atom processor clock speed analysis Rydberg gate time transport measurement time budget |
| W7 | WebSearch | extended | blackbody contaminant Rydberg atoms ejection tweezer between entangling gates delay 100 microseconds fidelity recovery |
| W8 | WebSearch | extended | autoionization removal Rydberg population alkaline-earth ytterbium strontium gate leakage conversion to erasure between gates |
| W9 | WebSearch | extended | microwave pulse remove Rydberg P state population neutral atom array leakage "P state" clean-up |
| W10 | WebSearch | extended | Rydberg leakage reduction unit neutral atoms pump residual Rydberg population ground state fast |
| W11 | WebSearch | extended | microwave pulse converts Rydberg state 70S rubidium to atom loss 98.6% fidelity 100 ns |
| W12 | WebSearch | extended | Rydberg atoms anti-trapped by tweezer light expelled time scale microseconds heating loss recapture probability Rydberg excitation detection |
| W13 | WebSearch | extended | fast quantum error correction cycle neutral atoms sub-millisecond syndrome extraction in-place gates Rydberg decay correlated errors repeated gates |
| W14 | WebSearch | extended | temperature dependence blackbody Rydberg contaminant gate repetition rate cryogenic clock rate parallel gates neutral atoms |
| W15 | WebSearch | extended | CZ gate fidelity versus time between gates Rydberg decay nearby P states randomized benchmarking delay dependence |
| W16 | WebSearch | extended | state-selective field ionization Rydberg atoms tweezer array electrodes remove Rydberg atoms microseconds quantum processor |
| W17 | WebSearch | standard | Rydberg atom ponderomotive force tweezer ejection velocity escape time calculation alkali 1064 nm 852 nm trap depth |
| W18 | WebSearch | standard | residual Rydberg population converted to loss tweezer turned on after gate "Rydberg" "loss detection" entangling gate fidelity 2025 |
| W19 | WebSearch | standard | lifetime of Rydberg contaminant atoms in array blackbody P state survives 100 microseconds corrupts subsequent gates distant sites |
| W20 | WebSearch | standard | photoionization of Rydberg atoms optical tweezer light ionization rate removal residual Rydberg neutral atom gate |
| W21 | WebSearch | extended | pulsed field ionization alkali Rydberg leakage erasure conversion neutral atom quantum computer kV/cm electrodes fast switching |
| W22 | WebSearch | extended | "inter-gate" delay Rydberg decay "P states" neutral atom logical circuit speed tradeoff 2026 |
| W23 | WebSearch | standard | dual-species in-place syndrome extraction Rydberg residual excitation ancilla ionization between gates Rb Cs microwave ionization |
| W24 | WebSearch | standard | Rydberg atom lifetime in optical tweezer trap on anti-trapping measured microseconds 852 nm 1064 nm cesium rubidium ejection |
| W25 | WebSearch | standard | stroboscopic Rydberg excitation wait time contaminant decay duty cycle blackbody facilitation repetition |
| W26 | WebSearch | standard | Rydberg ion removal small electric field after autoionization correlated errors ions stray field neighbouring Rydberg gates |
| A1 | arXiv API | max 50, sortBy=submittedDate | abs:Rydberg AND abs:residual AND abs:population AND abs:gate |
| A2 | arXiv API | same | abs:Rydberg AND abs:leakage AND abs:ionization (0 hits) |
| A3 | arXiv API | same | abs:Rydberg AND abs:contaminant |
| A4 | arXiv API | same | abs:Rydberg AND abs:cycle AND abs:time AND abs:error AND abs:correction |
| A5 | arXiv API | same | abs:Rydberg AND abs:antitrapping (0 hits) |
| A6 | arXiv API | same | abs:Rydberg AND abs:anti-trapped |
| A7 | arXiv API | same | abs:Rydberg AND abs:ponderomotive AND abs:tweezer |
| A8 | arXiv API | same | abs:Rydberg AND abs:recapture AND abs:tweezer |
| A9 | arXiv API | same | abs:Rydberg AND abs:autoionization AND abs:gate |
| A10 | arXiv API | same | abs:Rydberg AND abs:blackbody AND abs:delay (0 hits) |
| A11 | arXiv API | same | abs:Rydberg AND abs:leakage AND abs:loss AND abs:conversion |
| A12 | arXiv API | same | abs:neutral AND abs:atom AND abs:clock AND abs:speed AND abs:error AND abs:correction |
| A13 | arXiv API | same | abs:Rydberg AND abs:microwave AND abs:ionization AND abs:array (0 hits) |
| S1 | Semantic Scholar API | citations, limit 1000 | arXiv:2506.20661 (Bluvstein et al. 2026): 264 citing records returned, all titles screened by eye. Plausible ones were downloaded: 2603.01612, 2604.21876, 2608.16815, 2604.19735, 2605.03951, 2603.15561, 2605.10924, 2603.13492, 2606.08453, 2506.13724, 2608.06242, 2606.24869, 2608.05010, 2608.27426, 2603.21643. 2611.15104, 2609.10079, 2607.02804, 2611.06613 and 2604.25987 already had text in the repo. |

Every downloaded PDF was converted to `literature/text/arXiv_<id>.raw.txt` and grepped for `blackbody|black-body|BBR|contaminant|residual Rydberg|Rydberg population|eject|expel|anti-trap|ioniz|between gates|cycle time|clock|wait`. Each hit was then read in context.

## 2. Candidate table

| arXiv / DOI | Authors | Year | Title | What it shows | What it does NOT show (vs. i-iv) | Verdict | Read extent |
|---|---|---|---|---|---|---|---|
| 2604.21876 | Pecorari, Brennen, Kondov, Pupillo | 2026 | Loss-biased fault-tolerant quantum error correction | States that shorter QEC cycles leave less time for residual Rydberg population (from gate errors, BBR or decay) to decay, which gives correlated error clusters. Surface-code simulations (d=3-9) compare back-to-back gates with ideal inter-gate ionization ("relaxation"), and partial ionization efficiency (100/90/75/50/0 %), and ionization only at selected locations. Proposes autoionization (AEL atoms) or pulsed field ionization (~1 kV/cm, alkali) between gates to enable sub-ms cycles. Supp. S6 cites Bluvstein's ~100 us P-state lifetime and 4 us spacing. | Does not derive a minimum delay or a delay law. Relaxation is either ideal or absent, with no time dependence; no T, Omega, n or R dependence; and no inter-pair dipolar (1/R^3) contaminant: residual Rydberg acts only through hopping and blockade inside a stabilizer. No removal time or efficiency for alkali atoms is computed. | PARTIAL (strong: closest to (ii) and (iii)) | Full text: main, Supp. S5, S6 |
| 2410.09746 (PRL 134, 133201) | Cao, ..., Kaufman | 2024/2025 | Autoionization-enhanced Rydberg dressing by fast contaminant removal | Explicitly frames waiting for BBR contaminants to decay as a duty-cycle limit (stroboscopic dressing), and replaces the wait with AI pulses: tau_AI = 31(2) ns, 0.3 us AI pulses, 2 us wait, duty cycle ~10 % vs <1 % without AI. Sr 5s47s 3S1. | Dressing, not gate layers. No QEC cycle time, no delay law in T, Omega, n or R. Applies only to divalent atoms. | PARTIAL on (iii) (removal for speed, analogous context) | Intro, Fig. 1-2 text |
| 2201.03540 (Nat. Commun. 13, 4657) | Wu, Kolkowitz, Puri, Thompson | 2022 | Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays | Proposes autoionizing residual Rydberg population after each gate (Yb, 369 nm) and removing ions with a small field, which "eliminates correlated errors from leakage to long-lived Rydberg states". Supp. S7 gives a cycle-time estimate with an erasure-detection step te ~10 us after each set of parallel gates (cycle ~100 us), 61 % of n=75 decays are BBR, and the alternative of waiting ~1 ms for decay. | Does not derive the cycle time from contaminant physics: te is the imaging time. No inter-pair contaminant error, no T, R or Omega law. | PARTIAL on (ii) and (iii) | Main Sec. on erasure, Supp. S3, S7 sections |
| 2506.13632 | Senoo et al. | 2025 | High-fidelity entanglement and coherent multi-qubit mapping in an atom array | Experiment (Yb): "we also apply an ionization pulse after each CZ gate to convert residual Rydberg population" to loss. Auto-ionization time constant 0.03 us (369.5 nm, 1 mW, 40 um waist). gRB raw fidelity 99.37(7) %, loss-detected 99.78(4) %. | Purpose is erasure or loss detection, not speed or delay. No contaminant-delay analysis, no cycle-time model. | PARTIAL on (iii) (demonstrated per-gate removal) | Sections on gRB and ionization, ED Fig. 5 caption |
| 2405.10434 | Chow, Buchemmavari, Omanakuttan, Little, Pandey, Deutsch, Jau | 2024 | Circuit-based leakage-to-erasure conversion in a neutral atom quantum processor | Measures the ejection of Cs 64P3/2 Rydberg atoms from a 937 nm tweezer with the trap on: survival drops 1/e in ~23 us vs ~170 us Rydberg lifetime. Notes that the anti-trapping speed is system-specific and that ionization is faster. Notes that a BBR-populated r' gives only phase error in LP gates. | No ponderomotive calculation. No delay-law or cycle-time analysis; the trap depth is not stated in the text read. | PARTIAL on (iv) (measured ejection time) | Sec. on Rydberg leakage, App. A1, Fig. 5 |
| 2303.06126 | Guttridge, Ruttley, ..., Adams, Cornish | 2023 | Observation of Rydberg blockade due to the charge-dipole interaction between an atom and a polar molecule | Rb 52S1/2 in an 817 nm tweezer left on: Rydberg trap lifetime 8.5(1.1) us at 35 kW/cm^2, mapping fidelity 94(1) % (146 us calculated lifetime). | Not about gates, delays or contaminants. Measured only, no model. | PARTIAL on (iv) (number only) | Supp. "Rydberg detection", Fig. S7 |
| 2303.08783 (PRA 108, 023122) | de Keijzer, Tse, Kokkelmans | 2023 | Recapture probability for anti-trapped Rydberg states in optical tweezers | Quantum-mechanical calculation (inverted Gaussian / inverted harmonic potential) of wavefunction escape from a tweezer for 88Sr, U0 = 50 uK, omega = 25 kHz: ~30 us needed to expand out of the trap, recapture ~100 % for gate-relevant times, recapture times similar with traps on or off. | Treats a short excursion to the Rydberg state (recapture), not the ejection of a long-lived contaminant. Sr only, no alkali ponderomotive scaling with n or lambda. Does not connect to inter-gate delay or BBR. | PARTIAL on (iv) (theory of anti-trapping escape time) | Abstract, Secs. II-III, Fig. 5-7 captions |
| 2603.24789 | Patenotte, Kim, Gebretsadkan, Ni | 2026 | Absence of Far-Detuned Attractive Optical Traps for Alkali Rydberg Atoms | Polarizability of Cs Rydberg levels in a 1064 nm tweezer. Protocol: "tweezer is turned back on for 100 us to eject the Rydberg atom population". Proves that no far-detuned attractive trap exists for alkali Rydberg atoms. | No measured ejection time and no gate or delay context. | PARTIAL on (iv) (protocol number, theory of anti-trapping) | Abstract, methods paragraph, grep |
| 2012.12281 (Nature 595, 227) | Ebadi et al. | 2021 | Quantum phases of matter on a 256-atom programmable quantum simulator | Rb |r> = 70S: 100 ns MW pulse (6.9 GHz plus harmonics, 3 W horn) converts Rydberg atoms to loss, 98.6(4) % (99.1(4) % with a second pi pulse). Transfer out of r on a timescale of several ns. | Detection, not removal between gates. Not BBR P states. No delay context. | PARTIAL on (iii) (removal number, alkali) | Methods paragraph, ED Fig. 5 caption |
| 2611.06613 | Zhang et al. (JILA) | 2026 | Cryogenic suppression of correlated loss in Rydberg atom arrays | Cs contaminants are removed by a 9 us MW-ionization pulse ("ionization typically occurs in less than 1 us") in the lifetime protocol. After dressing, contaminants are photoionized by a MW pulse. | Measurement step, not inter-gate removal for speed. No cycle time. | PARTIAL on (iii) (removal number, alkali) | Appendix lifetime protocol, grep (known paper) |
| 2603.13492 | Miles et al. (Infleqtion) | 2026 | Qubit syndrome measurements with a high fidelity Rb-Cs Rydberg gate | A background microwave pulse ionizes Cs Rydberg population before measurement. | No timing given for this step, no delay analysis. | NO (mention only) | grep + paragraph |
| 2603.01612 | Lin, Li, ... | 2026 | Sustaining high-fidelity quantum logic in neutral-atom circuits via mid-circuit operations | Attributes much of the CZ infidelity (99.60(1) %) to residual Rydberg population from imperfect gates or BBR, which the tweezers then expel (loss). | No ejection time, no delay or cycle analysis (only ~25 kB of text extracted). | NO (qualitative) | Full extracted text, grep |
| 2506.20661 (Nature 649, 39) | Bluvstein et al. | 2026 | Architectural mechanisms of a universal fault-tolerant quantum computer | Context, already known: fidelity 99.3 % to 99.5 % at 100 us between gates; 400 us between gates lets P states "decay or eject"; Rydberg leakage either decays or is expelled. | No delay law. | (known; PARTIAL in prior_work) | Quoted only |
| 2304.05420 (Nature 622, 268) | Evered et al. | 2023 | High-fidelity parallel entangling gates on a neutral-atom quantum computer | Context, already known: a ~100 us delay with transport would expel leftover Rydberg states. | No delay law. | (known) | Quoted only |
| 2404.18809 | Poole, Graham, Perlin, Saffman et al. | 2024 | Architecture for fast implementation of qLDPC codes with optimized Rydberg gates | QEC cycle-time model (~1.28 ms for [[144,12,12]]) built from gate, scanning and measurement times. | No Rydberg contamination, BBR or inter-gate delay term (grep for blackbody/BBR/contaminant/residual is empty apart from integrated Rydberg population in the gate error). | NO for (ii) | Cycle-time section, grep |
| 2505.11218 | Saffman | 2025 | Quantum computing with atomic qubit arrays: confronting the cost of connectivity | Cycle-time comparisons and a discussion of heating, leakage and loss. | No contamination term in the cycle time; no BBR hits. | NO | grep + cycle-time paragraphs |
| 2406.07356 | Petrosyan, Norrell, Poole, Saffman | 2024 | Fast measurements and multiqubit gates in dual species atomic arrays | Dual-species cycle budget dominated by readout. | No contaminant term. | NO | grep |
| 2607.21554 | Menssen et al. | 2026 | Strategic Plan for Neutral Atom Quantum Computation | Says imaging dominates QEC cycle time; mentions cryogenic BBR suppression. | No contaminant or delay term. | NO | grep |
| 2608.30783 | Saffman | 2026 | Neutral atom quantum computing (review) | BBR lifetimes and cycle-time remarks. | No contaminant-delay analysis. | NO | grep |
| 2608.16815, 2604.19735, 2605.03951, 2603.15561, 2611.15104, 2608.06242, 2606.24869, 2608.05010 | various | 2026 | (Bluvstein citers on cycle rate, architecture, resource estimates, real-time QEC, fast MCM, reviews) | Cycle-time or clock-rate discussions. | Zero BBR, contaminant or residual-Rydberg hits relevant to delay (grep). | NO | grep only |
| 2305.05493 | Ma et al. | 2023 | High-fidelity gates with mid-circuit erasure conversion in a metastable neutral atom qubit | Recovers Rydberg leakage (including BBR-populated states) by waiting for it to decay, and suggests ionizing instead. | No delay law, no inter-pair term. | NO (qualitative) | grep + paragraph |
| 2407.20184, 2608.27426, 2608.26446, 2506.13724, 2606.08453, 2605.10924, 2608.04812, 2110.06902 | various | 2021-2026 | (gate benchmarking, robust gates, Yb logical qubits, dual-species readout, trap-off motional refocusing, ion-core light shifts) | Residual Rydberg converted to loss or erasure, anti-trapping mentioned. | No removal time for contaminants between gates, no delay or cycle analysis, no ejection-time calculation. | NO | grep only |

### Verdict
No candidate FIRES. None derives a minimum inter-gate delay or QEC cycle-time limit from BBR P-state contaminants as a function of T, Omega, n or R. The closest is 2604.21876 (PARTIAL, strong). It shows by simulation that fast cycles plus residual Rydberg population break fault tolerance and that ideal inter-gate ionization restores it, and it proposes ionization (autoionization; pulsed field ionization for alkali atoms) for sub-ms cycles. It treats relaxation as on/off, ignores inter-pair dipolar contaminants and gives no delay law.

For (iii), active removal is established. Autoionization works in ~30 ns (Sr, Yb) and has been demonstrated after every CZ in Yb (2506.13632). Cao et al. explicitly motivate it as replacing a contaminant wait (duty cycle). For alkali atoms only MW ionization or detection pulses (100 ns, 9 us) exist, outside a gate context.

For (iv), ejection times are measured (~8.5 us for Rb 52S at 817 nm and 35 kW/cm^2; ~23 us for Cs 64P at 937 nm) and computed for Sr (~30 us), but nobody turns them into an inter-gate delay bound.

## 3. Verbatim quotes

### arXiv_2604.21876 (Pecorari et al.), (i)/(ii)/(iii)
Q[arXiv_2604.21876]: "Given sufficient time (typically 100’s of µs), residual Rydberg population generated by gate errors is likely to convert into qubit loss"
Q[arXiv_2604.21876]: "Second, shorter cycles reduce the time available for residual Rydberg excitations to decay, leading to correlated error clusters that degrade logical performance and fault tolerance."
Q[arXiv_2604.21876]: "These unwanted excitations are removed via rapid ionization and subsequent removal of the remaining electron-ion pair using a small electric field"
Q[arXiv_2604.21876]: "The speed of Rydberg population removal is therefore determined by the Rabi rate of the coupling laser"
Q[arXiv_2604.21876]: "AI has been demonstrated with near-unity fidelity for reading out Rydberg excitation in Sr on µs scale [27]"
Q[arXiv_2604.21876]: "Remarkably, we find that ionizing only the ancilla after each gate — assuming data–ancilla blockade — is already sufficient to preserve fault tolerance"
Q[arXiv_2604.21876]: "Recent experiments [9] identify black body–induced decay to nearby Rydberg P states (∼ 100µs lifetimes) as dominant error source."
Q[arXiv_2604.21876]: "we identify pulsed field ionization [35] as a highly efficient alternative loss-biasing strategy."
Q[arXiv_2604.21876]: "challenging due to the necessity of rapidly switching large electric fields (∼ 1 kV/cm)."

### arXiv_2410.09746 (Cao et al.), (iii)
Q[arXiv_2410.09746]: "this SRD strategy suffers from a low duty cycle [55] as a result of waiting for the contaminants to decay. A fast contaminant removal procedure can be used to overcome this limitation."
Q[arXiv_2410.09746]: "a single AI laser is capable of removing all dominantly populated contaminant states"
Q[arXiv_2410.09746]: "AI pulses of duration tAI = 0.3 µs are applied, followed by a wait time of twait = 2 µs."
Q[arXiv_2410.09746]: "The data show a 1/e timescale of τAI = 31(2) ns, which is three orders of magnitude faster than the relevant Rydberg state lifetimes [19]."
Q[arXiv_2410.09746]: "a Rydberg duty cycle near the 10% level is maintained, compared to < 1% realized previously without AI [18]."

### arXiv_2201.03540 (Wu et al.), (ii)/(iii)
Q[arXiv_2201.03540]: "we estimate that 61% of decays are BBR, 34% are RD"
Q[arXiv_2201.03540]: "Population remaining in Rydberg states at the end of a gate can be converted into Yb+ ions by autoionization on the 6s → 6p1/2 Yb+ transition at 369 nm [48]."
Q[arXiv_2201.03540]: "As the ions can be removed after each erasure detection round with a small electric field, this approach also eliminates correlated errors from leakage to longlived Rydberg states [50]."
Q[arXiv_2201.03540]: "The erasure detection step must occur after each set of parallel gates, and takes a time te ≈ 10 µs"
Q[arXiv_2201.03540]: "This increases the cycle time to (tg + te )/fp ≈ 100 µs."
Q[arXiv_2201.03540]: "To ensure more than 99.9% of the ions have decayed, it would be necessary to wait approximately τ > 7/Γ ≈ 1 ms"
Q[arXiv_2201.03540]: "corresponding to a velocity v0 = pe /m ≈ 3.5 m/s."

### arXiv_2506.13632 (Senoo et al.), (iii)
Q[arXiv_2506.13632]: "Importantly, we also apply an ionization pulse after each CZ gate to convert residual Rydberg population after the gate to (detectable) loss."
Q[arXiv_2506.13632]: "A beam of power 1 mW is focused to a 40 µm Gaussian waist"
Q[arXiv_2506.13632]: "an ionization decay time constant of 0.03 µs, fast enough to suppress Rydberg decay prior to ionization [28]."
Q[arXiv_2506.13632]: "we extract a raw gate fidelity of 99.37(7)%"
Q[arXiv_2506.13632]: "observing 99.78(4)% two-qubit gate fidelity"

### arXiv_2012.12281 (Ebadi et al.), (iii) alkali MW removal
Q[arXiv_2012.12281]: "The MW source (Stanford Research Systems SG384) is frequency-tripled to 6.9 GHz and amplified to 3 W"
Q[arXiv_2012.12281]: "is applied on the atoms using a microwave horn for 100 ns. When applying a Rydberg π-pulse immediately followed by the MW pulse, we observe loss probabilities of 98.6(4)%."
Q[arXiv_2012.12281]: "99.1(4)% loss probability, which is our best estimate for our Rydberg detection fidelity"
Q[arXiv_2012.12281]: "there is a rapid transfer out of the Rydberg state on the timescale of several nanoseconds."

### arXiv_2611.06613 (Zhang et al., JILA), (iii) alkali MW ionization
Q[arXiv_2611.06613]: "These contaminants are removed immediately after the second π pulse using a 9 µs MW-ionization pulse applied through an antenna inside the cold box [36]. Although the applied pulse lasts 9 µs, ionization typically occurs in less than 1 µs"
Q[arXiv_2611.06613]: "both weakly anti-trapped by the tweezer and are photoionized by a MW pulse directly after dressing"

### arXiv_2603.13492 (Miles et al.), (iii) mention
Q[arXiv_2603.13492]: "microwave pulse ionizes the Cs Rydberg population, resulting in atom loss before measurement of the Cs atom."

### arXiv_2405.10434 (Chow et al.), (iv)
Q[arXiv_2405.10434]: "Since the Rydberg 64P3/2 state used in this work is anti-trapped for our trap wavelength (937 nm)"
Q[arXiv_2405.10434]: "In our system, the survival drops by 1/e in ≈ 23 µs, which is short compared to the Rydberg lifetime of ≈ 170 µs for the 64P state at room temperature [40, 56]."
Q[arXiv_2405.10434]: "Trap wavelength, strength, geometry, and chosen Rydberg level all make the anti-trapping speed system-specific [57]."
Q[arXiv_2405.10434]: "Other, typically faster, methods of converting Rydberg population to atom loss utilize laser- or field-induced ionization"
Q[arXiv_2405.10434]: "where |r′ ⟩ is a different nearby Rydberg state populated due to blackbody-radiation, then only a coherent phase error is added on the second atom"

### arXiv_2303.06126 (Guttridge et al.), (iv)
Q[arXiv_2303.06126]: "We achieve this by merging a 817 nm tweezer containing a Rb atom"
Q[arXiv_2303.06126]: "state |r⟩ = |522 S1/2 , mj = −1/2⟩"
Q[arXiv_2303.06126]: "the trap lifetime is measured to be 8.5(1.1) µs in an atom tweezer of intensity 35 kWcm−2 ."
Q[arXiv_2303.06126]: "We calculate the zero-temperature lifetime of the state |r⟩ with arc [17] to be 146 µs. We therefore expect to map excitation to loss with a fidelity of 94(1)%"

### arXiv_2303.08783 (de Keijzer, Tse, Kokkelmans), (iv) theory
Q[arXiv_2303.08783]: "We find that there is ample time (≈ 30 µs, in a Strontium-88 system) needed for the wave functions to expand out off the trap."
Q[arXiv_2303.08783]: "Therefore, even with traps on, ≈ 100% recapture probabilities can be expected for times in which significant entanglement operations between atoms can be performed."
Q[arXiv_2303.08783]: "U0 = 50 µK and ω = 25 kHz"
Q[arXiv_2303.08783]: "it is more beneficial to keep the traps on, thus heating up only a single atom, than to heat up the entire array when switching the traps off."

### arXiv_2603.24789 (Patenotte et al.), (iv) protocol
Q[arXiv_2603.24789]: "The optical tweezer is turned back on for 100 µs to eject the Rydberg atom population."
Q[arXiv_2603.24789]: "due to the 1064 nm tweezer light"
Q[arXiv_2603.24789]: "We attribute this to site-by-site trap depth inhomogeneity and the anti-trapping of the Rydberg states"

### arXiv_2603.01612 (Lin et al.)
Q[arXiv_2603.01612]: "residual Rydberg population due to imperfect gate evolution or black-body radiation induced transitions, which is subsequently expelled by the tweezers."

### Context (known papers)
Q[arXiv_2506.20661]: "the gate fidelity in this array increases from 99.3% to 99.5% by increasing duration between gates to 100 µs, as the Rydberg atoms decay or eject during that time."
Q[arXiv_2506.20661]: "400 µs for surface code repeated stabilizer measurements) for these Rydberg P states to decay or eject [82]"
Q[arXiv_2506.20661]: "the Rydberg atoms (theoretically) either decay to the ground state or are expelled from the tweezer."
Q[arXiv_2304.05420]: "∼ 100 µs delay between subsequent gates would result in leftover Rydberg states being expelled from the array"

## 4. Quantitative inputs harvested for (iii) and (iv)

| Quantity | Value | Species / state | Conditions | Source |
|---|---|---|---|---|
| Autoionization 1/e time | 31(2) ns | Sr 5s47s 3S1 | AI pulses 0.3 us + 2 us wait | 2410.09746 |
| Autoionization decay constant | 0.03 us | Yb Rydberg | 369.5 nm, 1 mW, 40 um waist; applied after each CZ | 2506.13632 |
| Erasure-detection step per gate layer | ~10 us (cycle ~100 us with f_p = 1/10) | Yb (proposal) | autoionization + ion imaging | 2201.03540 |
| Ion recoil velocity after AI | ~3.5 m/s | Yb+ | | 2201.03540 |
| MW-enhanced loss | 100 ns pulse, 98.6(4) % (99.1(4) %) | Rb 70S | 6.9 GHz + harmonics, 3 W horn | 2012.12281 |
| MW ionization | 9 us pulse, ionization < 1 us | Cs contaminants | cryogenic antenna | 2611.06613 |
| Pulsed field ionization requirement | ~1 kV/cm switched fields | alkali (proposal) | | 2604.21876 |
| Ejection 1/e (trap on) | ~23 us (lifetime ~170 us) | Cs 64P3/2 | 937 nm tweezer, depth not stated | 2405.10434 |
| Ejection trap lifetime | 8.5(1.1) us; 94(1) % map-to-loss | Rb 52S1/2 | 817 nm tweezer, 35 kW/cm^2 | 2303.06126 |
| Wavefunction escape time (theory) | ~30 us | 88Sr | U0 = 50 uK, omega = 25 kHz | 2303.08783 |
| Ejection hold (protocol) | 100 us tweezer on | Cs | 1064 nm tweezer | 2603.24789 |

## 5. Limits
- Google Scholar, paywalled journal versions, theses and conference abstracts were not searched. Semantic Scholar returned 264 citers of 2506.20661, which may be incomplete for very recent preprints.
- The citers were screened by title, so a paper with an uninformative title could be missed.
- 2603.01612 yielded only ~25 kB of text; its supplement may hold ejection numbers that were not seen.
- Not finding a paper does not show that none exists. Within the reachable literature up to 2026-11-20, no paper derives the inter-gate delay or cycle-time floor from BBR P-state contaminants as a function of T, Omega, n or R.
