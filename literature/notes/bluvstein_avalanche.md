# Prior work: BBR contaminants, avalanche facilitation, and correlated Rydberg-gate errors

Project question: a BBR transition nS -> n'P during a gate pulse creates a contaminant that
interacts with other Rydberg atoms via resonant dipole exchange (1/R^3). What is the correlated
error one contaminant causes on OTHER gate pairs in a dense parallel CZ layer, and what is its
logical consequence for a code?

Kill test K1 fires if a paper already computes that inter-pair error in parallel CZ gates, or
simulates its effect on a code.

Prepared 2026-11-20. Quotes below are copied from `literature/text/arXiv_<id>.raw.txt`
(pdftotext output) and checked with `python3 tools/verify_quotes.py`.

## Sources

| paper | arXiv ID | how verified | read extent |
|---|---|---|---|
| Bluvstein et al., "A fault-tolerant neutral-atom architecture for universal quantum computation", Nature 649, 39 (2026) | 2506.20661 (arXiv title: "Architectural mechanisms of a universal fault-tolerant quantum computer") | arXiv API lists DOI 10.1038/s41586-025-09848-5; Crossref for that DOI returns the Nature title, vol. 649, pp. 39-46, first author Bluvstein; PDF first line and author list match | Full arXiv PDF (main text, Methods, Extended Data captions). The Supplementary Information is not in the arXiv PDF. The arXiv ancillary `Error_model.docx` was downloaded and its text saved as `text/arXiv_2506.20661.anc_Error_model.txt`. I did not read the other ancillary files (movies, raw command strings). |
| Cao, Yelin, Eckner, Oppong, Kaufman, "Autoionization-enhanced Rydberg dressing by fast contaminant removal", PRL 134, 133201 (2025) | 2410.09746 | Exact title and authors match on PDF page 1 (v2, 4 Mar 2025) | Full (main text and Supplementary Material, both in the arXiv PDF) |
| Festa et al., "Blackbody-radiation-induced facilitated excitation of Rydberg atoms in optical tweezers", PRA 105, 013109 (2022) | 2103.14383 | arXiv API gives DOI 10.1103/PhysRevA.105.013109; PDF title "Black-body radiation induced facilitated excitation of Rydberg atoms in optical tweezers"; authors match | Full (main text and Supplemental Information) |
| Goldschmidt et al., "Anomalous broadening in driven dissipative Rydberg systems", PRL 116, 113001 (2016) | 1510.08710 | Exact title and authors match on PDF page 1 (v3) | Full (main text and supplementary material) |
| Boulier et al., "Spontaneous avalanche dephasing in large Rydberg ensembles", PRA 96, 053409 (2017) | 1709.02460 | Exact title and authors match on PDF page 1 (v1) | Full (main text and appendix) |
| Zeiher et al., "Many-body interferometry of a Rydberg-dressed spin lattice", Nat. Phys. 12, 1095 (2016) | 1602.06313 | Exact title and authors match on PDF page 1 (v3) | Main text in full. In the Supplementary Information I read the BBR, correlated-loss and post-selection sections in full and skimmed the rest. |
| (extra, already in repo) Evered et al., "High-fidelity parallel entangling gates on a neutral atom quantum computer", Nature 622, 268 (2023) | 2304.05420 | Ref. [36] of Bluvstein 2026; PDF title matches | Targeted read only: gate-site correlation Methods section and ED Fig. 3 caption |

Note on the Bluvstein citation: arXiv:2611.06613 (Zhang, Marsh, Tan, ... Kaufman, Regal) cites
Bluvstein et al. as its ref. [13] for this sentence:
Q[arXiv_2611.06613]: "Contaminants can also perturb Rydberg gates, introducing correlated faults that compromise quantum error correction [13]."

---

## 1. Bluvstein et al. 2026 (arXiv:2506.20661): the most important paper

### What it shows

**Contaminant mechanism during gates.** In Methods ("Analysis of error correlations"), the paper
names the project's mechanism and puts a number on it:
Q[arXiv_2506.20661]: "Concretely, during Rydberg gates, roughly 0.07% of the error budget is decay of Rydberg atoms to adjacent Rydberg P states."
Q[arXiv_2506.20661]: "These states have a strong, long-ranged interaction with the Rydberg S states that are used for the gates, and can thereby affect gates occurring in a different site, and moreover can have lifetimes of over 100 µs."
Q[arXiv_2506.20661]: "During repeated benchmarking sequences, like the ones reported in Ref. [36], we have only 4 µs between gates, and consequently Rydberg P atoms can survive for many layers of gates and corrupt gates in distant sites."
- The text is ambiguous about whether "0.07% of the error budget" means 0.07% absolute probability
  per gate or 0.07% of the total error. The value is not derived anywhere in the arXiv PDF.

**Measured effect of gate spacing (time) and site separation (distance) on CZ fidelity.** This
is ED Fig. 6g:
Q[arXiv_2506.20661]: "In ED Figure 6g, we plot the CZ gate fidelity in a repeated benchmarking sequence as a function of the duration between the gates, and find that the gate fidelity in this array increases from 99.3% to 99.5% by increasing duration between gates to 100 µs, as the Rydberg atoms decay or eject during that time."
Q[arXiv_2506.20661]: "g, CZ gate fidelity measured via randomized benchmarking [36]. Infidelity due to Rydberg P states is removed by leaving sufficient time or distance between gates. Sparse corresponds to 2x larger separation between gate sites."
Q[arXiv_2506.20661]: "This also implies the reported gate fidelity in Ref. [36] may have been impacted by this effect and thereby underestimating the maximum gate fidelity."
Q[arXiv_2506.20661]: "Analogously, we observe that this gate fidelity reduction is removed by reducing atom density."
- The x-axis of ED Fig. 6g is "Gate spacing (μs)" and runs from 0 to 400. There are two curves,
  "Normal" and "Sparse". I read the 99.3% to 99.5% values from the text, not from the plot.

**Why the authors say it does not affect their QEC.** Long times between gates, passive decay and ejection, and low density:
Q[arXiv_2506.20661]: "In quantum circuits based on atom motion, the duration between gates is sufficiently long (e.g., 400 µs for surface code repeated stabilizer measurements) for these Rydberg P states to decay or eject [82], which natively fixes this issue, and consequently we do not observe such effects during quantum circuits."
Q[arXiv_2506.20661]: "Leakage to Rydberg states. Population left in the Rydberg manifold can affect subsequent gates, and can lead to large error correlations. For example, manybody Rydberg evolution in dense systems observes socalled avalanche errors where a macroscopic fraction of the system has an error [83]."
Q[arXiv_2506.20661]: "Crucially, in our approach with a low atomic density and several hundred microseconds between gates, the Rydberg atoms (theoretically) either decay to the ground state or are expelled from the tweezer."
Q[arXiv_2506.20661]: "We observe that with several hundred microseconds between gates, effects of Rydberg leakage are not apparent, and during our repeated QEC data we observe that our leakage is at least 80% loss (ED Fig. 5b)."
- Ref. [82] is Cao et al. 2025 and ref. [83] is Festa et al. 2022, the papers covered in sections 2 and 3.
- The paper does not describe an active ejection, autoionization or "push-out" pulse between gates.
  Removal is passive, through decay or expulsion during the inter-gate time. The word
  "eject" is used, but no protocol is given.

**Code-level evidence is empirical only.** The paper finds no excess correlated errors in the surface-code data:
Q[arXiv_2506.20661]: "Crucially, we find these are closely consistent with the expected distribution as seen by Clifford simulations that assume uncorrelated one- and two-qubit errors."
Q[arXiv_2506.20661]: "We further note that our observed distribution of errors-per-shot is closely consistent with these simple simulations with uncorrelated Pauli-type and loss-type errors, suggesting the absence of large-scale correlated errors in the system."
- The circuit-level error model in the ancillary file uses only independent channels. These are a two-qubit depolarizing
  channel per gate pair, single-qubit depolarizing on idle qubits in the entangling zone, loss, SPAM and idle errors. It has no
  term for P-state contaminants or for inter-pair correlation:
Q[arXiv_2506.20661]: "For each pair of qubits doing an entangling gate: Apply two-qubit depolarizing channel after gate with probabilities entangling_gate_error_rate"
Q[arXiv_2506.20661]: "entangling_gate_loss_rate 0.00183"

**Geometry (deep-circuit configuration).**
Q[arXiv_2506.20661]: "Within this zone, entangling gates are performed simultaneously on up to 256 qubits across 8 rows and 16 columns of gate sites with a horizontal extent of 175 µm."
- The paper gives no gate-site pitch or intra-pair distance in the arXiv PDF. A column pitch of
  about 175/16 ≈ 11 µm is my own inference, not a number from the paper.
- Gate parameters for the error budget:
Q[arXiv_2506.20661]: "Decrease gate time from 270 ns to 135 ns, reducing Rydberg T1 error from 0.113% to 0.057%, and reducing dephasing error from 0.134% to 0.034%."

**Rydberg state.** The PDF mentions 53S1/2 in a level-diagram figure. Evered 2023 (see 1b) gives the n = 53 lifetimes.

### 1b. Supporting detail from Ref. [36], Evered et al. 2023 (arXiv:2304.05420, targeted read)
Q[arXiv_2304.05420]: "Careful analysis reveals small growth in the covariance between neighboring gate sites (Extended Data Fig. 9), which can result either from correlated detuning fluctuations (corresponding to our T2∗ ) or from long-range interactions caused by a Rydberg atom decaying into an adjacent Rydberg state"
Q[arXiv_2304.05420]: "For example, decay of Rydberg atoms to nearby P states during the gate can cause detuning shifts due to strong long-range interactions between S and P Rydberg states (decaying as 1/R3 ), as well as hopping of the P state to nearby gate sites."
Q[arXiv_2304.05420]: "Classical Monte Carlo simulations of these two phenomena (not plotted here) reveal that both error sources can result in nonzero covariance, which appears to be described by quadratic growth for a small number of gates but linear asymptotically."
Q[arXiv_2304.05420]: "The Rydberg lifetime has both radiative decay (170 µs) and black-body decay (128 µs) components, which we obtain by re-scaling the values in Ref. [96] to n = 53."

### What it does NOT show (relative to the project question)
- **Pulsed gates.** Yes, these are real pulsed CZ gates in global randomized benchmarking. But there is
  no model of the contaminant-induced error per gate pulse: no detuning shift vs. R, no
  dependence on gate protocol, no exchange/hopping amplitude.
- **Parallel gate pairs and inter-pair error.** The inter-pair effect is acknowledged ("affect
  gates occurring in a different site") and seen only in aggregate: average RB fidelity vs.
  gate spacing and for 2x sparser sites. It is never isolated or computed per contaminant. There is no
  inter-pair error probability as a function of distance, n, or contaminant state. Evered 2023
  mentions Monte Carlo covariance simulations but does not plot them and gives no numbers.
- **Spacing dependence.** There are only two geometries (Normal and Sparse = 2x). There is no functional
  R-dependence and no 1/R^3 or 1/R^6 error law.
- **Code-level consequence.** No simulation includes the effect. The error model is uncorrelated.
  The paper argues the effect is absent in its own QEC circuits because 400 µs separate the gates, and it does not
  analyse fast-cycle or short inter-gate-time architectures.
- **Removal pulses.** Removal is passive only (decay or ejection). No active ejection or autoionization step is part of the architecture.

### K1 verdict: PARTIAL OVERLAP (strong; closest prior art; does not fire)
Justification: the paper explicitly identifies the mechanism. P-state contaminants from decay
during gates corrupt gates at other, distant sites. It measures the aggregate fidelity cost
(99.3% -> 99.5% CZ RB fidelity at 4 µs vs. 100 µs gate spacing, which is removed by 2x site separation
or lower density). That observation is prior art, and the project must cite it and not
claim discovery of the effect. But the paper does not compute the inter-pair error, either per
contaminant or as a function of distance. Its code simulation uses uncorrelated errors and does not include the
effect. So neither K1 clause is met. Our novelty must be the quantitative, distance-resolved
inter-pair error model and its code-level consequence, especially for short inter-gate times
(< about 100 µs), where Bluvstein's "decay or eject" argument fails.

### Numbers to reuse
- About 0.07% (of error budget; ambiguous) per gate from Rydberg decay to adjacent P states.
- P-state lifetimes "over 100 µs". n = 53 Rydberg lifetime components: radiative 170 µs, BBR 128 µs (Evered 2023).
- CZ RB fidelity 99.3% at short (4 µs) spacing, 99.5% at 100 µs. The effect is removed at 2x site separation.
- QEC cycle has 400 µs between gates. Gate time 270 ns. Rydberg T1 error 0.113% per gate.
- Up to 256 qubits in 8 x 16 gate sites over 175 µm.
- Error-model entangling-gate Pauli rates (ancillary): IZ = ZI = 5e-4, ZZ = 1e-3, others 5e-5. Gate loss 0.00183.

---

## 2. Cao et al. 2025 (arXiv:2410.09746): autoionization (AI) contaminant removal

### What it shows
Q[arXiv_2410.09746]: "In this process, BBR drives transitions from the target Rydberg state |r⟩ to a set of nearby, opposite-parity Rydberg (contaminant) states |r′ ⟩. The resonant dipolar exchange interaction of |r′ ⟩ with |r⟩ [47, 48] can shift the dressing laser into resonance, facilitating a proliferation of Rydberg excitations."
Q[arXiv_2410.09746]: "Critically, the collective loss can be triggered by only a single contaminant (Rydberg atom), causing the loss rate to grow for increasing ensemble size."
- Platform: 88Sr clock qubits in a 575 nm lattice, 2a_lat or 3a_lat spacing. Target state 5s47s 3S1. Contaminants are in the 5snp 3P0,1,2 series.
Q[arXiv_2410.09746]: "The data show a 1/e timescale of τAI = 31(2) ns, which is three orders of magnitude faster than the relevant Rydberg state lifetimes [19]."
Q[arXiv_2410.09746]: "For SRD, we apply a variable number M of dressing pulses, each with a fixed tp ≈ 0.23 µs [65]; in between dressing pulses, AI pulses of duration tAI = 0.3 µs are applied, followed by a wait time of twait = 2 µs."
Q[arXiv_2410.09746]: "By incorporating AI pulses into a stroboscopic Rydberg dressing (SRD) sequence, we enhance lifetimes by an order of magnitude for system sizes of up to 144 atoms, while maintaining an order of magnitude larger duty cycle than previously achieved."
- AI leaves an ion. The resulting Stark shift on neighbours sets the wait time:
Q[arXiv_2410.09746]: "For use in Rydberg dressing, we fix twait = 2 µs, which is the dominant limitation for the currently achievable duty cycle."
- AI does not harm clock-qubit coherence:
Q[arXiv_2410.09746]: "The fitted fringe contrast is C = 0.977(4) [0.970(4)] with [without] applying the AI pulses"
- Target-state lifetimes (Supplement):
Q[arXiv_2410.09746]: "In Ref. [18], 1/e exponential timescales to occupy states bright and dark to our detection protocol from the target 5s47s 3S1 Rydberg state were measured to be τrdark = 51(2) µs and τrbright = 86(3)µs."

### What it does NOT show
- Rydberg dressing only. There are no CZ gates, no gate pairs, no parallel gate layer, and no inter-pair gate error.
- No spacing dependence of the contaminant interaction and no C3 values. The quantity reported is the ensemble lifetime τ1/e vs. system size and density.
- No QEC or code-level consequence. Erasure conversion is mentioned only as a future idea:
Q[arXiv_2410.09746]: "Alternatively, direct detection of the ionized contaminants could be a useful tool in erasure conversion schemes [5, 13, 76]."
- AI needs a divalent (alkaline-earth-like) atom. It does not apply directly to Rb or Cs as used in Bluvstein 2026.

### K1 verdict: NO
It demonstrates a mitigation, contaminant removal between pulses, in a dressing context. It computes no gate-pair error and has no code analysis.

### Numbers to reuse
- τ_AI = 31(2) ns (measured). Theory gives τ_AI ≈ 34 ns. AI pulses last 0.2–0.3 µs. Ion-clearing wait t_wait = 2 µs, set by a stray field of 360(20) mV/cm.
- Duty cycle about 8 to 10% with AI vs. < 1% without.
- Sr 47 3S1 lifetimes: τ_dark = 51 µs, τ_bright = 86 µs.

---

## 3. Festa et al. 2022 (arXiv:2103.14383): BBR-induced facilitation in tweezers

### What it shows
Q[arXiv_2103.14383]: "Here we report on a single atom resolved study of this state contamination and the emerging pairwise interactions in optical tweezers. For near-resonant laser detuning we observe characteristic correlations with a length scale set by the dipolar interaction."
- Platform: 39K in tweezers with spacing 5 to 40 µm. Single-photon excitation to 62P1/2. The strongest-coupled contaminants are 61D3/2,5/2, about 13 GHz away.
Q[arXiv_2103.14383]: "The dipole-dipole potentials between |r0 i and magnetic substates of the 13 GHz higher lying, strongest coupled states 61D3/2 and 61D5/2 are shown in gray."
- **Facilitation-range method.** The correlation length is fitted to an exponential and compared with the dipolar pair potentials. The potentials are weighted by pair-state overlap times BBR rate and calculated with Pairinteraction and ARC:
Q[arXiv_2103.14383]: "To extract a typical correlation length scale dc (∆) we fit the data exponentially with g (2) (d, ∆) ∝ exp(−d/dc (∆))."
Q[arXiv_2103.14383]: "The pair-potentials are shaded according to the relative predicted facilitation strength."
Q[arXiv_2103.14383]: "For the calculations the Pairinteraction [53] and ARC [54] software packages have been used."
- **Rate formula (static positions, low excitation, Supplement):**
Q[arXiv_2103.14383]: "The resonant rate of dipolar facilitation γi due to the i-th pair-potential can be readily calculated in the low excitation fraction regime. It follows from γi = Γeff p0 Ω2 τr2"
Q[arXiv_2103.14383]: "with an effective rate Γeff = hΨ2 |r0 , r̄i i Γ0,i , taking into account the pair-state overlap hΨ2 |r0 , r̄i i and the black-body coupling rate Γ0,i ."
Q[arXiv_2103.14383]: "Additionally, it includes a convolution with a Gaussian of standard deviation σ = 0.58 µm to include the thermal extend of the spatial wavefunction in the individual tweezers."
- **Motion dominates at short range.** Rydberg atoms are ejected and fly, so the static picture fails:
Q[arXiv_2103.14383]: "The decay to low lying states takes several hundred microseconds, in which the Rydberg atoms move by tens of micrometers, clearly invalidating a static picture [32]."
Q[arXiv_2103.14383]: "Including black-body radiation, none of the states live for more than about 150 µs. When assuming a lifetime of 150 µs to roughly estimate the time in which facilitation can take place, the atoms move about 13 µm."
- **Avalanche (Fig. 4).** With stronger driving the correlations reach across the whole array:
Q[arXiv_2103.14383]: "For the strongest driving, the amplitude of correlation between the two ends of the array (almost 80 µm apart) is of comparable strength to the nearest-neighbor correlation for the weakest drive."
- The proposed mitigation is a repulsive light sheet that traps ground-state atoms and repels contaminants.

### What it does NOT show
- Near-resonant cw excitation (dressing-like regime, Ω/2π ≤ 0.4 MHz, Δ/2π a few MHz, ms-scale illumination). There are no pulsed gates, no CZ, no qubits and no gate pairs.
- It measures correlated *loss*, not a gate-error probability. It has no QEC or code consequence.
- **No explicit C3 values are given.** The pair potentials appear only in plots (Fig. 1b, 2), and the
  correlation lengths dc(Δ) are shown in Fig. 2 without being tabulated in the text. The spacing dependence is measured, but
  at nearest-neighbour range it is dominated by motion: gnn(a) is "indistinguishable" for two detunings.

### K1 verdict: NO
Its physics is the same mechanism, but in a cw near-resonant drive regime. It has no gate-pair error and no code.

### Numbers / models to reuse
- γ_i = Γ_eff p0 Ω² τ_r², with Γ_eff = |⟨Ψ2|r0,r̄_i⟩|² Γ_0,i and p0 = α(Δ)Ω²/4Δ². Then sum over pair potentials and convolve with σ = 0.58 µm. This is the facilitation-range method.
- K 62P: lifetimes for all states ≤ about 150 µs including BBR. 0 K lifetimes near n = 60 are about 250 µs (s), 800 µs (p) and 500 µs (d).
- Velocities: recoil 36 µm/ms, ponderomotive 40 µm/ms, so flight is about 13 µm over 150 µs.
- Correlations spanned about 80 µm in avalanche conditions (5 µm-spaced 3x16 array).

---

## 4. Goldschmidt et al. 2016 (arXiv:1510.08710): anomalous broadening

### What it shows
Q[arXiv_1510.08710]: "We attribute the increased linewidth to resonant dipole-dipole interactions of 18s atoms with blackbody induced population in nearby np states."
Q[arXiv_1510.08710]: "∝ C3 /r3 , whose angular dependence allows it to be positive or negative [26, 27] and, for 18s interacting with 17p or 18p, equals the 18s linewidth at 16 µm separation."
Q[arXiv_1510.08710]: "Blackbody-induced transitions to other Rydberg levels constitute & 20 % of the decay."
- Platform: 87Rb 18s, 3D lattice with 406 nm spacing, Γ0 = 2π × 45 kHz, 1/Γ0 = 3.5 µs. The width reaches about 200 Γ0, up to 8 MHz.
- Scaling law with the interaction volume β3:
Q[arXiv_1510.08710]: "bnp /Γnp = 116 µm3 (including the root-mean-squared average of the angular dependence of C3 )."
Q[arXiv_1510.08710]: "Γ ≈ Ω ρ g β3 ,"
- Time to the first contaminant (the trigger estimate):
Q[arXiv_1510.08710]: "The time until the creation of the first contaminant atom is τ = τs /bN0 , where b & 20 % is the branching to contaminant states and N0 is the total number of atoms."
- Scaling with n (Supplement):
Q[arXiv_1510.08710]: "Additionally, this effect remains at higher principal quantum number: β3 ∝ n∗7 where n∗ = n − δqd is the effective principal quantum number and δqd is the quantum defect [30]."
- Mean-field fails because exchange needs s–p coherences:
Q[arXiv_1510.08710]: "Mean-field approaches fail because the off-diagonal interaction requires single-atom coherences between the driven state and contaminant states, which do not develop under blackbody induced population of the contaminant states [29]."
- The paper flags relevance to gates but does not analyse it:
Q[arXiv_1510.08710]: "The expected non-interacting excitation rates, both on and off resonance, are central to the feasibility of both dressed Rydberg proposals and Rydberg quantum gate implementations."

### What it does NOT show
Bulk 3D BEC with cw excitation and ensemble-averaged spectroscopy. It has no pulsed gates, no gate pairs, no per-contaminant
inter-pair error, and no code. It states the configuration is irrelevant ("insensitivity to nearest-neighbor
spacing"), so there is no spacing law beyond the C3 scale.

### K1 verdict: NO

### Numbers to reuse
- Rb 18s–17p/18p: the C3/r^3 shift equals 2π × 45 kHz at 16 µm. β3 = Σ C3 b_np/Γ_np = 116 µm^3 (rms angular average, 17p and 18p only).
- BBR branching ≳ 20%. The vdW blockade shift at the highest density is 1.9 MHz, against an observed 8 MHz width.
- Trigger time τ = τs/(b N0), with τs = 4δ²/(Γ0 Ω²).

---

## 5. Boulier et al. 2017 (arXiv:1709.02460): spontaneous avalanche dephasing

### What it shows
Q[arXiv_1709.02460]: "The dephasing arises as a runaway process where the production of the first contaminant atoms facilitates the creation of more contaminant atoms."
Q[arXiv_1709.02460]: "These results support earlier works and confirm that the time scale for the onset of dephasing is reduced by a factor which scales as the inverse of the atom number."
- Pump–probe cross-broadening: contaminants from one Rydberg transition broaden a different transition, and only when the pulses overlap in time:
Q[arXiv_1709.02460]: "As expected, the cross-broadening and cross-saturation are absent when the probe and pump pulses are out of phase."
- **Avalanche or trigger model (homogeneous mean-field rate equations):**
Q[arXiv_1709.02460]: "Ṅg = (N18S − Ng )R + Γ0 b1 N18S + ΓnP b3 NnP ,"
Q[arXiv_1709.02460]: "ṄnP = b2 Γ0 N18S − ΓnP NnP ,"
Q[arXiv_1709.02460]: "Γ(t) = Γ0 + C3 ρ0 NnP (t),"
Q[arXiv_1709.02460]: "where ρ0 is the density of atoms (in any state), NnP is the fraction of these atoms in the pollutant state, and C3 ≃ ... 2π × 35 MHz µm3 is the average of the C3"
- (The `...` stands for a "(nP)" superscript that pdftotext places between the lines.)
Q[arXiv_1709.02460]: "It correctly predicts the overall time dependence with only one free parameter, C3cross , for which the extracted value is C3cross ≃ C3 /10 = 2π × 3.5 MHz µm3 ."
- The model is too slow. The dynamics are clustered and correlated:
Q[arXiv_1709.02460]: "A single atom in an nP state can shift some fraction of surrounding atoms into resonance, leading to fast excitation in an anti-blockade, clustered dynamic [29, 30]."
- Stroboscopic mitigation and the first-contaminant time τc. The formula itself is lost in text extraction; the threshold is N_c = 4δ²/(Ω² b_nL):
Q[arXiv_1709.02460]: "The average time τc until the first contaminantstate atom appears provides an estimate of the actual coherent time available before the avalanche excitation is triggered."
Q[arXiv_1709.02460]: "For experimentally reasonable parameters of δ/Ω ≃ 10 and bnL ≃ 0.2, Nc ≃ 2000."
- Contaminant set for nS:
Q[arXiv_1709.02460]: "Indeed, for a nS initial Rydberg state, there are at least four signiﬁcant pollutant states: nP1/2 , nP3/2 , (n− 1)P1/2 and (n− 1)P3/2 , plus all their hyperﬁne levels (if they are spectrally resolved)."
- Cryogenics:
Q[arXiv_1709.02460]: "would need an ambient temperature near 10 K to make up for the avalanche dephasing eﬀect."
- The paper says the mechanism applies to QIP but does not analyse it:
Q[arXiv_1709.02460]: "This decoherence mechanism is important to consider, as it should be present in any experiment with steady-state Rydberg population, such as oﬀ-resonantly dressed Rydberg systems or Rydberg-based quantum information processing."

### What it does NOT show
Bulk Rb 18S BEC with cw or stroboscopic excitation on 2 to 30 µs pulses. There are no gates, no gate pairs, no inter-pair gate error, no
spacing dependence (homogeneous density model), and no code consequence.

### K1 verdict: NO

### Numbers / models to reuse
- Effective C3 ≈ 2π × 35 MHz µm^3 for Rb 18S–nP (rms-averaged). Cross-state C3 ≈ 2π × 3.5 MHz µm^3.
- Branching ratios: b1 = 0.49 (18S -> g), b3 = 0.55 (pollutant -> g). The value of b2 was lost in extraction; do not use it without checking the PDF.
- Lifetimes of the s and p populations are 3–10 µs (n = 18). Onset of broadening takes a few hundred ns. Steady state is reached in about 10 µs.
- Mean-field three-level rate model plus Γ(t) = Γ0 + C3 ρ0 N_nP(t). This is the avalanche trigger model, and it is known to underestimate speed by about 2x or more.
- Four dominant pollutant states for nS: nP1/2, nP3/2, (n−1)P1/2, (n−1)P3/2.

---

## 6. Zeiher et al. 2016 (arXiv:1602.06313): Rydberg-dressed spin lattice

### What it shows
Q[arXiv_1602.06313]: "From this we conclude that stimulated Rydberg-Rydberg state transitions, recently observed as anomalous broadening [24], act collectively in a manybody system, implying that rare one-body decay events can globally affect the entire spin lattice."
- Platform: about 190 87Rb atoms in a 532 nm lattice dressed to 31P (τr ≈ 27 µs).
- **Trigger model:** one BBR event causes instantaneous loss of all dressed-state atoms:
Q[arXiv_1602.06313]: "We can incorporate this picture into our theoretical description by assuming a stochastically triggered instantaneous loss of all |↑i-state atoms as a simplification, still permitting an analytical solution of the many-body dynamics (Supplementary Information)."
Q[arXiv_1602.06313]: "We extract a value of γBB /2π = 1.6 kHz, approximately half the literature value for 31P1/2 -states [35]."
Q[arXiv_1602.06313]: "Due to the dependence on system size via N (0), the extracted value of 130(20) µs is significantly lower than the anticipated value of τr /β 2 = 2.2 ms in the absence of additional loss processes, however it surpasses the bare Rydberg state lifetime by a factor of five."
Q[arXiv_1602.06313]: "The observed long tail for short times or the bimodality for later times are not expected from the coherent theory without dissipation and support the hypothesis of a loss process which is correlated in the sense that a single trigger event leads to a significant loss of atoms in the whole ensemble."
- Mitigation suggestions: fewer spins, adjusted detuning, and stroboscopic dressing with decay or laser quenching.

### What it does NOT show
Dressing, not gates. There are no gate pairs and no inter-pair error. The loss is modelled as global with no spatial or spacing dependence and no
C3. There is no code-level consequence, and post-selection is used to remove triggered shots.

### K1 verdict: NO

### Numbers to reuse
- γ_BB/2π = 1.6 kHz fitted for 31P (about half the literature value). Loss model N(t) = N(0) exp(−(N(0)/4) β² γ_BB t).
- Collective lifetime 130(20) µs vs. ideal 2.2 ms for about 190 atoms.

---

## Overall K1 assessment
- **K1 does not fire** on any of the six papers.
- **Bluvstein 2026 is a strong PARTIAL OVERLAP.** It names the exact mechanism (gate-time decay to
  adjacent P states corrupts gates at other sites, with lifetimes > 100 µs) and measures its
  aggregate cost: CZ RB fidelity of 99.3% at 4 µs gate spacing vs. 99.5% at 100 µs, with the effect gone at 2x site separation
  or lower density. It does not compute the per-contaminant inter-pair error or its distance law, and
  it does not put the effect into its (uncorrelated) code simulation. Its argument that the effect is harmless
  relies on several hundred µs between gates and low density. Evered 2023 (its ref. [36]) adds
  that unpublished classical Monte Carlo sims of P-state shifts and hopping give nonzero gate-site
  covariance, but it shows no numbers.
- Project framing: do not claim discovery of the effect. Claim (i) a quantitative inter-pair error
  model vs. R, n and gate protocol, (ii) its correlated-fault structure in a parallel CZ layer, and (iii)
  code-level consequences, especially for short inter-gate times or dense layouts where passive
  decay or ejection does not apply.
- The dressing and avalanche papers (Festa, Goldschmidt, Boulier, Zeiher, Cao) give the C3 scales,
  trigger-time estimates, facilitation-rate formula and mitigation ideas (AI removal, repulsive light sheets,
  stroboscopy, cryogenics). None of them treats gate pairs or codes.
