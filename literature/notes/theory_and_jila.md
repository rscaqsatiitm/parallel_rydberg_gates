# Prior-work reading: JILA cryogenic avalanche paper + four QEC/theory papers

Project question: a BBR-produced n'P contaminant (from a gate's nS Rydberg atom) talks to Rydberg atoms of
OTHER gate pairs by resonant dipole exchange (1/R^3). What is the correlated inter-pair error in a dense parallel
CZ layer vs gate speed, pair spacing, n, T, and what does it do to a code's logical error?

Kill test K1 fires if a paper already computes that inter-pair error in parallel CZ gates, or simulates its effect on a code.

All quotes below are verbatim from `literature/text/<id>.raw.txt` (checked with `tools/verify_quotes.py`).
Read in full: main text, appendices, supplements and reference lists of all five papers.

## Summary table

| Paper | Contaminant hits a different gate pair? | Parallel gates? | 1/R^3 exchange? | Spacing dependence? | Code simulation with spatially correlated multi-pair errors? | K1 |
|---|---|---|---|---|---|---|
| 2611.06613 (Zhang...Regal, JILA) | Only as a one-sentence outlook; physics measured in a dressed array, not gates | Mentioned in outlook only | Yes (Eq. 3, J_ij = C3(θ)/R^3), for dressing facilitation | Yes for avalanches (ξ0, r_c, g2(d)); none for gates | No | PARTIAL OVERLAP (physics input, no gate/code calculation) |
| 2105.13501 (Cong et al., PRX 2022) | Qualitatively: a BBR-transferred atom blockades later Rydberg operations "within the interaction range" | No (sequential gates in a stabilizer circuit) | No (contaminant treated as a blockader) | No | No (resource counting, no simulation) | PARTIAL OVERLAP (qualitative statement only) |
| 2411.04664 (Yu et al., MBQC) | No; correlated leakage only within one CZ, and ignored in simulation | No | No | No | Code sim, but leakage propagates only through CZ-gate connectivity | NO |
| 2603.24237 (Perrin, Roger, Pupillo) | No; correlation only between the two atoms of the same CZ | No | No | No | Surface-code sim with gate-partner-correlated loss | NO |
| 2604.21876 (Pecorari et al.) | No; hopping is between the two atoms of a CZ, correlations are temporal across sequential gates | No (one 5-atom plaquette, B_ij = 0 or infinity) | No | No | Surface-code sim, but correlated errors are hook-like within one plaquette | NO |

Overall: K1 does NOT fire on any of the five. The closest prior statements are (i) the Cong et al. qualitative remark that a
BBR-transferred Rydberg atom blockades remaining Rydberg operations within the interaction range, and (ii) the JILA outlook
sentence that BBR contaminants in parallel-gate architectures could cause erasures and correlated Pauli errors. Neither
computes an inter-pair error rate, a spacing/speed/n/T dependence, or a code-level effect.

---

## 1. arXiv:2611.06613 — Zhang, Marsh, Tan, Manning, Slichter, Kaufman, Regal, "Cryogenic suppression of correlated loss in Rydberg atom arrays" (JILA/NIST, Nov 2026)

### (a) What it shows (with numbers)

Experimental paper: a 45 K radiation shield ("cold box") around a 87Rb tweezer array; measures nS lifetimes (50 <= n <= 75) and
avalanche (correlated loss) rates in Rydberg-DRESSED arrays (not gates), at 300 K and cryogenic operation.

Main claims:
Q[arXiv_2611.06613]: "Here, we suppress avalanche decay and establish BBR as its dominant trigger using a Rydberg atom array that operates either cryogenically or at room temperature."
Q[arXiv_2611.06613]: "Rydberg lifetimes are cryogenically extended up to 45(11) %, corresponding to suppression of BBR-induced decay rates ΓBBR by up to 53(8) %."
Q[arXiv_2611.06613]: "Cryogenic operation reduces Γava by 22(2) % for n = 50 and 18(2) % for n = 60."

Definition of contaminant and the mechanism (this is exactly our "contaminant" concept, but for dressing):
Q[arXiv_2611.06613]: "BBR transfers atoms into nearby opposite-parity Rydberg states, termed “contaminant” states, whose strong dipolar interactions can shift Rydberg levels closer to or into resonance with the dressing laser [34]."

Temperatures / effective temperature:
Q[arXiv_2611.06613]: "Our apparatus, details of which are provided in Ref. [36], operates at either 45 K or 300 K."
Q[arXiv_2611.06613]: "Approximating the MW environment using a single effective temperature, we find that Teff = 188(8) K matches the data well for n ≤ 60, corresponding to 44(3) % shielding from room-temperature BBR."
Q[arXiv_2611.06613]: "The cold windows subtend approximately 50 % of the solid angle to the atom array, providing a simplified estimate of 50 % shielding from room-temperature BBR under cryogenic operation."
Cryogenic BBR is NOT thermal at one temperature (important if we scale with T):
Q[arXiv_2611.06613]: "The cryogenic BBR environment therefore cannot be fully described by a single effective BBR temperature Teff for the current apparatus."
Future projection:
Q[arXiv_2611.06613]: "Employing a conductive coating on optical apertures in the current apparatus should yield equilibration to a uniform MW effective temperature Teff ≈ 45 K and this modification alone is expected to suppress ΓBBR and Γava by about 85 % compared to room-temperature operation."

BBR rate model used (Eq. 1 with Purcell factor), and n̄ ≈ kT/ħω scaling:
Q[arXiv_2611.06613]: "For the dominant BBR-induced Rydberg transitions we study, n̄(ω, T ) ≈ kB T /(ℏω) for T ≫ ℏω/kB ≈ 1 K."
Q[arXiv_2611.06613]: "The BBR-induced component accounts for over 50 % of the total decay rate for 87 Rb nS states with n ≥ 48, and accounts for even more for states with orbital angular momentum L > 0 [48]."
Purcell effects (cold box):
Q[arXiv_2611.06613]: "Finite-element simulations in Appendix C suggest the cold box hosts MW resonances with quality factors up to 50, particularly in the 3 to 15 GHz band, leading to Purcell factors FP ≲ 5 [Fig. 2(c)]."

Lifetimes: individual nS lifetimes are given only in Fig. 2(a) (plot). Numerical lifetime values in text: NOT FOUND except n = 80:
Q[arXiv_2611.06613]: "The lifetime of the 80S1/2 state is found to be 26(2) µs, substantially shorter than the predicted roomtemperature lifetime of 204 µs."
Contaminant (n'P) lifetimes: NOT FOUND.

Geometry, field, dressing parameters:
Q[arXiv_2611.06613]: "We perform Rydberg dressing in square-lattice arrays of up to 5×14 atoms with 5 µm spacing."
Q[arXiv_2611.06613]: "The long axis of the array is aligned with the Rydberg-beam propagation and quantization-field directions [Fig. 3(a)]."
Q[arXiv_2611.06613]: "All reported measurements use a 3.5 G magnetic field during Rydberg excitation, applied parallel to"
Q[arXiv_2611.06613]: "For single-atom lifetime measurements, atoms are instead loaded stochastically into a 1 × 4 array with 33 µm spacing, which is large enough to ensure that atom-atom interaction effects can be neglected."
Q[arXiv_2611.06613]: "This large separation suppresses resonant dipole-exchange interactions between atoms transferred to nearby P contaminant states and atoms remaining in the target nS state."
Q[arXiv_2611.06613]: "The 420 nm Rydberg beams are reddetuned from the excited state 6P3/2 , F = 3, mF = +3 with ∆ = −2π × 1.5 GHz."
Q[arXiv_2611.06613]: "The two-photon Rydberg coupling strength is Ω ≤ 2π ×3 MHz."
Q[arXiv_2611.06613]: "δ = −2π × 2 MHz is the detuning from the Rydberg state."
Q[arXiv_2611.06613]: "Our maximum Rabi frequency Ω = 2π × 1.25 MHz puts the system near the strong-dressing regime and yields a nominal Rydberg dressing fraction PRyd ≈ 0.08 before considering interaction effects."
Q[arXiv_2611.06613]: "The Rydberg coupling is ramped on over tramp = 6 µs using a cosine profile to a maximum Rabi frequency Ω, held static for a variable amount of time ∆t, then ramped back down to zero in a time-reversed fashion [Fig. 3(b)]."
Q[arXiv_2611.06613]: "Rydberg-Rydberg interactions are described by Vij = −2πC6 /|ri − rj |6 , where ri are the positions of the atoms and the dispersion coefficients are C6 ≈ −15 GHz µm6 for 50S1/2 and C6 ≈ −139 GHz µm6 for 60S1/2 ."
Lifetime-measurement Rabi frequency (closer to gate-like π pulses):
Q[arXiv_2611.06613]: "The two-photon Rabi frequency is Ω/2π ≈ 2.5 MHz, with approximately matched single-photon Rabi frequencies to minimize scattering from the 6P3/2 state during the pulse."

Dipole-exchange (1/R^3) Hamiltonian, C3, V_dd:
Q[arXiv_2611.06613]: "BBR-induced decay to an n′ P contaminant state |r′ ⟩ triggers spin-exchange interactions described by the dipole-dipole Hamiltonian"
Q[arXiv_2611.06613]: "where Jij = C3 (θ)/|ri − rj |3 depends on the angle θ between the quantization axis and the interatomic separation vector."
Q[arXiv_2611.06613]: "Nearest-neighbor spin-exchange rates are estimated to reach up to tens of MHz at our 5 µm spacing."
Q[arXiv_2611.06613]: "Dipolar interactions between nS1/2 and contaminant (n + ∆n)PJ states are evaluated as Vdd = C3 /R3 at the nearest-neighbor separation R = 5 µm."
Q[arXiv_2611.06613]: "The C3 coefficients are calculated using the PairInteraction package [61] at a bias field of 3.5 G, for n = 50, 60 and J = 1/2, 3/2."
Q[arXiv_2611.06613]: "The mean strength V dd is obtained by averaging over the four nearest-neighbor interactions, two along the biasfield axis and two perpendicular to it."
Numerical C3 or V_dd values: NOT FOUND in text (only plotted as bars in Fig. 4(e)). We must recompute C3 ourselves (PairInteraction/ARC).

Which contaminants matter ("strongly interacting" = V_dd(5 µm) >= |δ|):
Q[arXiv_2611.06613]: "Only when nS1/2 dressed atoms decay to nP or (n − 1)P states do the dipole-dipole interaction strengths at our 5 µm lattice spacing become comparable to or exceed |δ|, as required for resonant facilitation and triggering avalanches [Fig. 4(e)]."
Q[arXiv_2611.06613]: "Comparing V dd to the dressing-detuning magnitude |δ|/2π = 2 MHz indicates that the (n − 1)P and nP manifolds are the only contaminant channels that are estimated to be strongly interacting enough to trigger avalanches [Fig. 4(e)]."

Branching fraction into (n−1)P + nP (CONFIRMED: 0.686 at 50S, 0.677 at 60S, 300 K; also 45 K values):
Q[arXiv_2611.06613]: "TABLE I. BBR branching fractions fn into the (n − 1)P and nP manifolds in thermal equilibrium at 300 K and 45 K."
Q[arXiv_2611.06613]: "50S1/2 0.686 0.729"
Q[arXiv_2611.06613]: "60S1/2 0.677 0.711"
Q[arXiv_2611.06613]: "Their mean is approximately 0.70, motivating the estimate Γtrig.BBR ≈ 0.7ΓBBR used in the main text for room temperature."
Q[arXiv_2611.06613]: "Under cryogenic conditions, Γtrig.BBR depends on the degree to which room-temperature BBR is suppressed at the specific nP and (n − 1)P transition frequencies, which is not known."
Q[arXiv_2611.06613]: "Purcell enhancement is omitted from these transition-rate calculations; Purcell effects do not significantly affect the n = 50 and n = 60 decay rates [Fig. 2]."
(Columns are fn(300 K), fn(45 K); "Initial state fn (300 K) fn (45 K)" header. Values computed with ARC.)

Γ_ava formula and definitions:
Q[arXiv_2611.06613]: "Even a single decayed atom can set off a chain reaction of correlated atom loss, resulting in a predicted avalanche rate Γava ∝ N ΓBBR , where N is the total number of atoms in the ensemble."
Q[arXiv_2611.06613]: "We define the total BBR-induced decay rate to these avalanchetriggering states as Γtrig.BBR , corresponding to Eq. (1) but with the sum over states limited to the nP and (n − 1)P states [Fig. 4(f)]."
Q[arXiv_2611.06613]: "Γava = N (PRyd + PPN )Γtrig.BBR + N PE Γion ."
Q[arXiv_2611.06613]: "This gives Γ⋆ava = N PRyd Γtrig.BBR as a testable hypothesis that links our measured avalanche rates in dressed atom arrays to the measured Rydberg lifetimes."
Terms:
Q[arXiv_2611.06613]: "We estimate PRyd in large atom arrays through exact diagonalization of Ĥ in a simplified geometry (Appendix H 1), which predicts PRyd = 0.063 for 50S1/2 dressing and PRyd = 0.044 for 60S1/2 dressing, reduced from the PRyd = 0.076 predicted for a single dressed atom [Fig. 4(d)]."
Q[arXiv_2611.06613]: "Extrapolating back to zero phase noise provides an estimation of the phase-noise contribution PPN ≈ 0.01, typically accounting for 15 %–20 % of Γava ."
Q[arXiv_2611.06613]: "The difference in Γava between the rate at our nominal 9 µK operating depth and the extrapolated zero-depth value gives an estimated PE Γion = 12(1) s−1 ."
Q[arXiv_2611.06613]: "This accounts for about 5.1(6) % of the total avalanche rate and is close to that predicted from theoretical estimates (Appendix H 5)."
Q[arXiv_2611.06613]: "At Vop = 8.8 µK, this yields bVop = 0.83(8) ms−1 , corresponding to 5.1(6) % of the fitted avalanche rate."
Q[arXiv_2611.06613]: "For 5 × 14 arrays (N = 70) dressed with the 50S1/2 state, this gives ΓPN = 4.1(9) ms−1 under cryogenic operation and 4.3(4) ms−1 at room temperature, corresponding to 18(3) % and 15(1) % of the respective avalanche rates."
Q[arXiv_2611.06613]: "RT ΓCryo BBR /ΓBBR = 0.67(8)."
Agreement:
Q[arXiv_2611.06613]: "Figure 5(b) shows that the measured Γava at room temperature are in agreement with the rate predicted by Eq. (5)."
Q[arXiv_2611.06613]: "The measured Γava under cryogenic operation are consistent with the bound Γtrig.BBR < ΓBBR ."

Measured Γ_ava vs N and P_Ryd with uncertainties: tabulated values NOT FOUND in the text; Γ_ava(N) is only plotted
(Fig. 3(h), linear zero-offset fits) and Γ*_ava vs P_Ryd only plotted (Fig. 5(a),(b)). Data said to be on Harvard Dataverse (below).
Numbers that are in the text:
Q[arXiv_2611.06613]: "In all cases, Γava is reduced under cryogenic operation and we observe the expected linear dependence of Γava on N ."
Q[arXiv_2611.06613]: "A leastsquares fit yields Γ0 = 11.5(2) ms−1 and rc = 17.5(1) µm with reduced chi-squared χ2ν = 0.70."
(Γ0 = avalanche rate of an isolated 5 × 5 array, i.e. N = 25.)
Q[arXiv_2611.06613]: "Linear fits to the early-time growth yield slopes of 10.3(6) ms−1 (cryo) and 12.6(5) ms−1 (RT), corresponding to a suppression of 19(6) %."
Q[arXiv_2611.06613]: "The fitted slopes are 4.3(1) ms−1 (cryo) and 5.4(2) ms−1 (RT), corresponding to a suppression of 21(4) %."
(These two are g2_NN growth slopes for 50S and 60S respectively, Fig. S8.)
Dressed-state spontaneous decay (dressing-weighted, not bare):
Q[arXiv_2611.06613]: "In addition to intermediate-state scattering, spontaneous decay from the Rydberg state occurs during dressing at rates of approximately 0.58 ms−1 for n = 50 and 0.33 ms−1 for n = 60 at the nominal Rydberg dressing strength."

Facilitation range ξ0 (Appendix E) and how it is computed:
Q[arXiv_2611.06613]: "For each contaminant state |Pi ⟩, the two-atom dipoledipole Hamiltonian is diagonalized at every interatomic separation R to yield eigenstates |ψαi (R)⟩ with energies Eαi (R), where α indexes the eigenstates."
Q[arXiv_2611.06613]: "The calculations take the internuclear axis to be parallel to the quantization axis."
Q[arXiv_2611.06613]: "Resonant facilitation occurs when ∆Eαi = ℏδ. The R at which this condition is met determines ξ0 , as shown in Fig. 3."
Q[arXiv_2611.06613]: "For δ = −2π × 2 MHz used in this work, ξ0 ≃ 13 µm for n = 60 and ξ0 ≃ 10 µm for n = 50."
Q[arXiv_2611.06613]: "Because several pair eigenstates and contaminant states contribute, ξ0 represents an approximate facilitation range rather than a uniquely defined radius."
Q[arXiv_2611.06613]: "Thus, pair eigenstates are visible in Fig. 3 ... only when dipolar interactions admix |S, Pi ⟩ character; the other pair eigenstates are not coupled by the dressing laser."
Fig. 3(c) pair potentials include n' = 59, 60, 61 and all fine-structure states:
Q[arXiv_2611.06613]: "Dipolar potentials for 60S1/2 |n′ PJ ⟩ pair states, including n′ = 59, 60, 61 and all fine structure states, shaded by their overlap with the non-interacting pair state at infinite separation."

Avalanche dynamics and the golden-rule facilitation rate (a ready-made formula for contaminant-induced excitation of a neighbour):
Q[arXiv_2611.06613]: "ξ(∆t) is consistent with ξ0 at early dressing times but then increases, growing at a rate of approximately 3 m/s for our nominal operating conditions."
Q[arXiv_2611.06613]: "This suggests that the facilitation rate scales as Ω2 /(δ 2 + Ω2 )."
Q[arXiv_2611.06613]: "where ρ is the spectral density of states at the final-state energy."
Q[arXiv_2611.06613]: "Fermi’s golden rule thus predicts that the facilitation rate scales as Ω2 /(δ 2 +Ω2 ), in agreement with the collapse of the measured data."
(Eq. 10: Γ_fac = 2πρ J_ij^2 cos^2φ sin^2φ = (π/2) ρ J_ij^2 Ω^2/(δ^2+Ω^2); Eq. 9 matrix element −ħJ_ij cosφ sinφ.)
Gaps stop propagation:
Q[arXiv_2611.06613]: "The gNN remains near 0.5 while g (2) (dc ) decays to zero over roughly 30 µm."
Q[arXiv_2611.06613]: "Neglecting the small contribution from photoionization, we find that a simple phenomenological model based on a 1/d3sep dipolar separation dependence captures the decay of Γ̄ava well."
Q[arXiv_2611.06613]: "At present, the lack of correlated loss observed between 50 µm-separated 5 × 5 atom arrays [Fig. 7] provides no evidence for a superradiant burst, but it may become a formidable source of correlated loss in larger arrays."

Sentence on contaminants perturbing gates, and ref [13]:
Q[arXiv_2611.06613]: "Contaminants can also perturb Rydberg gates, introducing correlated faults that compromise quantum error correction [13]."
Q[arXiv_2611.06613]: "[13] D. Bluvstein et al., A fault-tolerant neutral-atom architecture for universal quantum computation, Nature 649, 39 (2026)."
Ref [19] (gate errors from BBR) is Evered et al. 2026 (arXiv:2604.25987, also in our text folder):
Q[arXiv_2611.06613]: "BBR-induced stimulated emission and absorption are major Rydberg decay channels at room temperature [18], contributing to errors in state-of-the-art two-qubit gates [19–21]."

Whole Discussion/Outlook on gates/QEC (verbatim, the only gate/QEC content in the paper):
Q[arXiv_2611.06613]: "Our work has clear implications for error mitigation in neutral-atom quantum computing architectures."
Q[arXiv_2611.06613]: "We demonstrate cryogenic lifetime enhancement of the n ≥ 50 Rydberg nS states commonly used in leading platforms. This should directly reduce error rates in entangling gates [19]."
Q[arXiv_2611.06613]: "Practical quantum processor architectures execute large numbers of entangling gates in parallel, with atoms closely packed in interaction zones and with sequential gates occurring in rapid succession [13]."
Q[arXiv_2611.06613]: "In this context, BBR-induced contaminants could induce both erasure errors, lowering the error correction threshold, and correlated Pauli errors, reducing the effectiveness of quantum error correction [56] and increasing logical failure rates."
Q[arXiv_2611.06613]: "Cryogenic operation should passively reduce these errors by inhibiting BBR-driven decay to contaminant states, while active removal techniques [51] could be intermittently applied between gates to eliminate residual contaminants."
(Ref [56] = Cong et al. PRX 12, 021049 = arXiv 2105.13501; ref [51] = Cao et al. PRL 134, 133201, autoionization contaminant removal.)
Q[arXiv_2611.06613]: "[56] I. Cong, H. Levine, A. Keesling, D. Bluvstein, S.-T. Wang, and M. D. Lukin, Hardware-efficient, fault-tolerant quantum computation with Rydberg atoms, Physical Review X 12, 021049 (2022)."
Other outlook points (collective/superradiant BBR decay; shallow traps):
Q[arXiv_2611.06613]: "Thus, BBR photons may couple collectively to all atoms in the Rydberg state, and induce collective decay."
Q[arXiv_2611.06613]: "Once full cryogenic shielding is attained, previously sub-dominant trigger channels like trap photoionization become more relevant."

Harvard Dataverse (ref [57]): only the availability statement and the DOI; contents/format NOT described in the text.
Q[arXiv_2611.06613]: "Data availability: The data supporting these findings are publicly available [57]."
Q[arXiv_2611.06613]: "Data pertaining to “Cryogenic suppression of correlated loss in Rydberg atom arrays”, Harvard Dataverse, https://doi.org/10.7910/ DVN/AQHLGF, 2026."

### (b) What it does NOT show (relative to the project)
- No quantum gates at all: every correlated-loss measurement is in a continuously, off-resonantly DRESSED array (δ = −2π×2 MHz,
  Ω = 2π×1.25 MHz, tens of µs). No CZ gates, no resonant π/2π pulses, no gate fidelity, no parallel gate layer.
- The contaminant's effect on neighbours is computed only as dressing-laser FACILITATION (resonance condition ΔE(R) = ħδ
  giving ξ0), not as a phase/blockade/exchange error on a gate pair driven resonantly for ~0.1–1 µs.
- No error per neighbouring gate pair, no dependence on gate speed, no explicit n'P lifetime, no T scaling of an
  inter-pair error. Spacing dependence exists only for avalanches (ξ0 ≈ 10–13 µm, r_c = 17.5 µm, g2 decay over ~30 µm).
- No code-level simulation; the QEC statement is a single qualitative outlook sentence citing [13] and [56].
- C3/V_dd values are not tabulated (bar chart only).

### (c) K1 verdict: PARTIAL OVERLAP (does not fire)
It explicitly names our concern ("BBR-induced contaminants could induce both erasure errors ... and correlated Pauli errors"
in architectures that "execute large numbers of entangling gates in parallel") but computes nothing for gates or codes.
It is the strongest motivation reference and the main source of physical inputs; it also raises the novelty bar (the idea
is now stated in print by a leading group, Nov 2026), so our contribution must be the quantitative inter-pair model + code sim.

### (d) Models/numbers to reuse or compare to
- Branching to strongly interacting (n−1)P + nP: f = 0.686 (50S), 0.677 (60S) at 300 K; 0.729, 0.711 at 45 K (ARC). Use Γ_trig = f·Γ_BBR.
- Eq. (3) exchange Hamiltonian J_ij = C3(θ)/R^3 (angle dependent, field 3.5 G); "tens of MHz" at 5 µm (n = 50–60).
- ξ0 construction (pair-potential resonance with a detuning) — the analogous gate criterion would be V_dd(R) vs Ω or gate bandwidth.
- Golden-rule facilitation rate Γ_fac = (π/2)ρ J^2 Ω^2/(δ^2+Ω^2) (Eq. 10) — compare our inter-pair excitation probability.
- Γ_ava = N(P_Ryd + P_PN)Γ_trig + N P_E Γ_ion: the "seed rate per Rydberg-population" logic maps to our per-layer contaminant production N_pairs × P_Ryd(t) × Γ_trig × t_gate.
- T_eff = 188(8) K (44(3)% shielding), lifetime gain up to 45(11)%, Γ_BBR suppression up to 53(8)%; projected ~85% at 45 K.
- Correlated-loss spatial range: r_c = 17.5(1) µm (5×5 subarrays, 1/d^3 model), cross-correlation vanishing by ~30 µm; no correlation at 50 µm.
- Phase noise contributes P_PN ≈ 0.01 (15–20% of Γ_ava): incoherent Rydberg population also seeds contaminants.
- Dataverse DOI 10.7910/DVN/AQHLGF for raw Γ_ava(N) if we need to fit.

---

## 2. arXiv:2105.13501 — Cong, Levine, Keesling, Bluvstein, Wang, Lukin, "Hardware-Efficient, Fault-Tolerant Quantum Computation with Rydberg Atoms", PRX 12, 021049 (2022)

### (a) What it shows
Error-model + FTQC-protocol paper (Ryd-7 Steane-code and Ryd-3 repetition-code schemes). Converts all leading-order Rydberg
errors (BBR, RD, intermediate-state scattering) to Pauli-Z using ancilla blockade detection, optical pumping, selection rules.

BBR error treatment (Kraus jump |r'><1| plus no-jump Z):
Q[arXiv_2105.13501]: "First, interactions with blackbody photons can induce transitions from the nS state to nearby Rydberg n0 P states of higher or lower energy; such errors are subsequently referred to as blackbody radiation-induced (BBR) errors."
Q[arXiv_2105.13501]: "BBR errors give rise to quantum jumps from the qubit |1i state to Rydberg P states (corresponding to a leakage error), as well as Pauli-Z errors within the qubit manifold"

The key "nearby Rydberg population" statement (a BBR-transferred atom affects OTHER Rydberg operations within interaction range):
Q[arXiv_2105.13501]: "Due to the relatively long lifetimes of Rydberg states, we may assume that the atom will not decay again within the timescale of several Rydberg gate operations, as these would be higher-order processes."
Q[arXiv_2105.13501]: "In this case, because the states |r0 i are not de-excited in the ensuing operations, one serious consequence of BBR quantum jumps is that the remaining Rydberg operations on atoms within the interaction range will be affected by blockade, potentially resulting in multiple, correlated Pauli-Z type errors."
Q[arXiv_2105.13501]: "Rydberg-atom QEC seems to face a daunting chal-"
Q[arXiv_2105.13501]: "Rydberg states could decay into multiple other states, which not only results in leakage errors out of the computational space, but could also give rise to high-weight correlated errors from ensuing undesired blockade effects."
Q[arXiv_2105.13501]: "the possibility for Rydberg leakage errors to influence many future operations, resulting in high-weight correlated errors."
Within-gate correlations:
Q[arXiv_2105.13501]: "Thus, for the Ca Zb gates shown in Figure 2, the possible correlated errors may involve one of the Kraus maps Mr0 or M0 occurring on one of the qubits, together with Z-type errors on some or all of the remaining qubits involved in that gate."
FT definition forbids residual Rydberg population because it blockades future gates:
Q[arXiv_2105.13501]: "The final requirement is important because any remnant Rydberg population could blockade future Rydberg gates."
Detection via ancilla blockade, then ejection:
Q[arXiv_2105.13501]: "Specifically, we prepare a nearby ancilla qubit in the state |+i = √12 (|0i + |1i) and apply a 2π Rydberg pulse to detect whether there is another Rydberg atom within the blockade radius."
Q[arXiv_2105.13501]: "To convert the error to an atom loss error, we notice that the Rydberg atom naturally expels itself due to the anti-trapping potential of the tweezer [18], and can also be directly ejected in ∼ 100 ns by pulsing a weak, ionizing electric field (∼ 10 V/cm [54, 56, 57]) which removes the ion and electron."
Postponed detection gives correlated errors on the later-gated data atoms of the SAME stabilizer circuit:
Q[arXiv_2105.13501]: "the only possible correlated errors that can arise are Xβ Xγ Xδ , Xγ Xδ , or Xδ , corresponding to BBR transitions on data atoms β, γ, or δ, respectively."
Contaminant explicitly treated as a blockader for nearby atoms in the bias-preserving CNOT:
Q[arXiv_2105.13501]: "This is achieved because the Rydberg pulses from the qubit states to |d± i are resonant if and only if there are no neighboring atoms in |r± i or nearby Rydberg states."

BBR rate and branching:
Q[arXiv_2105.13501]: "For 87 Rb atoms excited to the 70S Rydberg state, there are four dominant final states associated to these BBR errors (see Appendix A); these are illustrated in Figure 1c as red arrows."
Q[arXiv_2105.13501]: "We note that the overall rate of BBR transitions can be suppressed by operating at higher neff or operating at cryogenic temperatures."
(Eq. 3: Γ_BBR = 4 k_B T / (3 c^3 n_eff^2) [atomic units].)
Q[arXiv_2105.13501]: "Comparing this with the scaling for the BBR decay rate, we see that while both error rates decrease for larger n, BBR processes dominate for large n, and RD processes dominate for smaller n or very low T ."
Appendix A / Fig. 12 (branching ratios only plotted, no numerical table for BBR):
Q[arXiv_2105.13501]: "Figure 12: Branching ratios for BBR transitions between Rydberg states of 87 Rb, from the stretched 70S1/2 state with mJ = 1/2, mI = 3/2 to different P states with mJ = 3/2 (empty orange circles) or mJ = 1/2 (filled blue diamonds)."
Q[arXiv_2105.13501]: "Indeed, we find that the atom decays primarily to the 69P and 70P states as illustrated in Figure 1c."
Numerical BBR branching values: NOT FOUND (figure only). RD branching ratios ARE tabulated (Table 4: 0.534, 0.177, 0.055, 0.168, 0.059, ...):
Q[arXiv_2105.13501]: "Table 4: Branching ratios for transition to each ground state of 87 Rb for radiative decay processes from the 70S1/2 , mJ = 1/2, mI = 3/2 stretched Rydberg state, accounting for transitions involving up to four-photon emission processes."

Crosstalk: the only "cross-talk" discussed is optical (photon reabsorption during readout), not Rydberg/BBR:
Q[arXiv_2105.13501]: "At lattice spacings of a few microns, this detection scheme could be limited by atom heating and cross-talk from the reabsorption of scattered photons by neighboring atoms [61]."
Q[arXiv_2105.13501]: "Between moving and light-shifting the ancillary atoms, cross-talk errors on the data qubits can be suppressed by five or more orders of magnitude, to negligible levels."
Threshold not computed (no numerical simulation):
Q[arXiv_2105.13501]: "One may estimate the error thresholds for two- and three-qubit gates directly by using the numbers presented in Tables 1 and 2 and requiring each logical operation or stabilizer measurement step to have at most a single error, but it can be more useful to obtain the precise numbers for these thresholds via numerical simulation."

### (b) What it does NOT show
- The contaminant is modelled as a perfect BLOCKADER of later Rydberg pulses in the same logical operation (sequential gates
  sharing atoms/ancillas), not as a resonant dipole-exchange (1/R^3) partner. No C3, no exchange dynamics, no partial shifts.
- No parallel CZ layer; no "other gate pair" separated by a spacing; no dependence on spacing, gate speed, n, or T beyond the
  total Γ_BBR ∝ T/n_eff^2 scaling.
- No error probability for neighbours; no code-level simulation at all (resource counting only; thresholds explicitly left to
  future numerical work). Mitigation = detect-and-eject after every gate (or postpone within a stabilizer), which
  assumes the leaked atom's influence is confined to its own logical operation.

### (c) K1 verdict: PARTIAL OVERLAP (does not fire)
It is the earliest clear qualitative statement that a BBR-transferred Rydberg atom corrupts subsequent Rydberg operations on
atoms "within the interaction range", producing correlated Z errors. But it computes no inter-pair error, has no parallel
layer, no 1/R^3 exchange, and no simulation. Must be cited as the qualitative precursor.

### (d) Reuse/compare
- Kraus model: M_r' ∝ |r'><1| per final state, no-jump M0 = sqrt(1−P)|1><1| + ... (Eqs. 1–2): reuse as the per-gate source event.
- "Blockade by contaminant ⇒ Z errors on gated neighbours" as the strong-interaction limit of our model (our model should reduce to it when V_dd ≫ Ω).
- Γ_BBR = 4k_BT/(3c^3 n_eff^2) scaling (compare to ARC numbers).
- 70S → mainly 69P and 70P (consistent with JILA f ≈ 0.68–0.70 into (n−1)P + nP).
- Ejection by ∼10 V/cm field in ∼100 ns — a mitigation timescale to compare with the layer duration.

---

## 3. arXiv:2411.04664 — Yu, Chen, Deng, Lu, Chen, Pan, "Taming Rydberg decay with measurement-based quantum computation" (v5, Apr 2026)

### (a) What it shows
RHG cluster-state MBQC with only final three-outcome (|0>,|1>,|L>) measurement; leaked atoms do not interact further;
"located decoder" reweights matching edges.
Q[arXiv_2411.04664]: "We demonstrate a high error threshold of 3.65% per CZ gate for pure Rydberg decay and achieve a favorable error distance de ≈ d."
Q[arXiv_2411.04664]: "The BBR branch takes the atom to other Rydberg states and is converted to atom loss with an anti-trapping potential or a microwave-assisted process."
Q[arXiv_2411.04664]: "A critical advantage of converting population to atom loss is that lost atoms no longer participate in Rydberg interactions."
Error model per CZ (only within the gate pair):
Q[arXiv_2411.04664]: "When neither of the two qubits is leaked before the CZ gate, the CZ errors are represented by p4e {L ⊗ I, L ⊗ Z, I ⊗ L, Z ⊗ L}."
Propagation only via the circuit's CZ connectivity:
Q[arXiv_2411.04664]: "Otherwise, the jump operator K1L propagates to a correlated Z error Zi Zj Zk ."
Q[arXiv_2411.04664]: "If a leakage is finally detected in a dual qubit, it happens at four error sites with approximately equal probability 25% (Li represents that the dual qubit leaks at the i-th CZ gate)."

The requested passage ("triggers another BBR error with O(1) probability") — correlated leakage within ONE CZ, ignored:
Q[arXiv_2411.04664]: "We have noticed that there is correlated leakage in Rydberg decay [8]. But we have ignored its effect in our simulation."
Q[arXiv_2411.04664]: "When implementing the two-qubit gate with neutral atoms, an RD error during the CZ gate leads to failure of Rydberg blockade, so it triggers another BBR error with O(1) probability."
Q[arXiv_2411.04664]: "Therefore, there is O(p) probability error that the interacting two qubits are leaked in a single CZ gate, instead of O(p2 ), although the probability is small."
Q[arXiv_2411.04664]: "For simplicity and clarity, we don’t consider this complex but indeed less harmful error in the simulation."
(Ref [8] = Chiu et al., Nature 2025.) Supplementary comparison section also frames it as partner dephasing within the gate:
Q[arXiv_2411.04664]: "The second difference is that the Rydberg decay happens during the two-qubit gate, so a leakage during the gate time may dephase another atom [1, 8]."
Q[arXiv_2411.04664]: "Recent experiments have reported Re ≈ 0.55 [1] and Re ≈ 0.56 [4], and the ratio increases when other noises, such as Doppler shifts and laser noise, are further suppressed in future scenarios [49]."

### (b) What it does NOT show
- Leakage does NOT spread to spatial neighbours: the leaked state is assumed inert ("not involved in subsequent gates"), BBR
  population converted to loss. Correlated leakage is only the two atoms of the same CZ (and is dropped from simulations).
- No parallel-gate crosstalk, no contaminant–Rydberg dipole interaction, no 1/R^3, no spacing/speed/n/T dependence.
- Code simulation exists (RHG, d up to 13), but errors are i.i.d. per CZ plus deterministic propagation through CZ edges.

### (c) K1 verdict: NO
The "O(1) probability" passage concerns the gate partner within a single CZ (RD breaks blockade), not a contaminant acting
on other pairs; it is explicitly excluded from the simulation.

### (d) Reuse/compare
- Threshold 3.65% (pure Rydberg decay, RHG + located decoder); R_e ≈ 0.55–0.56 in experiments; BE comparison η ≈ 1.5 at p = 0.1%, d = 7.
- Their assumption "leaked atoms do not interact" is precisely what our effect violates if the BBR contaminant is not removed
  within the layer — our result could be phrased as a correction to that assumption.
- Open code (github.com/yuchengcheng720/Located-decoder-for-Rydberg-decay) usable as a baseline harness.

---

## 4. arXiv:2603.24237 — Perrin, Roger, Pupillo, "Correlated Atom Loss as a Resource for Quantum Error Correction" (v2, Apr 2026)

### (a) What it shows
Surface code with teleportation-based loss-detection units (LDUs), circuit-level partially correlated atom loss + depolarizing;
loss-graph decoder.
Q[arXiv_2603.24237]: "Compared to a decoder that assumes independent loss events, our approach achieves up to an order-of-magnitude reduction in logical error probability and increases the loss threshold from 3.2% to 4%."
Mechanism (gate-partner re-excitation, not BBR dipole exchange):
Q[arXiv_2603.24237]: "Here we consider that the loss of the first atom during the two-qubit Rydberg gate can increase the loss probability of the second atom, giving rise to correlated-loss events [35, 48]"
Q[arXiv_2603.24237]: "After the first atom loss and while the gate laser pulse is still being applied, there exists a finite probability that the atom in |1⟩ is subsequently excited to its Rydberg state."
Q[arXiv_2603.24237]: "The probability of losing the second atom is enhanced with respect to the first atom due to the longer effective occupation of the Rydberg state."
Model:
Q[arXiv_2603.24237]: "We denote by pl the probability that an atom is lost during the implementation of a CZ gate."
Q[arXiv_2603.24237]: "When both atoms are initially present, we introduce a second parameter, pc , which quantifies the conditional probability of losing the second atom given that the first atom has already been lost during the same CZ gate."
Q[arXiv_2603.24237]: "the effective noise channel acting on the remaining atom can be described as a Pauli channel with error probabilities 1/8 for both X and Y errors, and 3/8 for Z errors."
Spatial structure = only CZ-connected pairs:
Q[arXiv_2603.24237]: "applied every cycle and correlated losses occur only during CZ gates — each edge between two nodes uniquely identifies a correlated loss channel."
Q[arXiv_2603.24237]: "To capture these correlations systematically, we construct a loss graph, with nodes representing lost atoms and edges connecting atoms that could be lost together via a CZ gate (see Fig. 2)."
BBR is mentioned only as a leakage source:
Q[arXiv_2603.24237]: "they may also decay out of the computational subspace due to, e.g. spontaneous emission or coupling to nearby Rydberg states due to black-body radiation."
Q[arXiv_2603.24237]: "Interestingly, although fully correlated losses double the number of lost atoms relative to the uncorrelated model, the threshold remains unchanged at 3.2%, and the logical performance is slightly improved in the fully correlated regime."
Q[arXiv_2603.24237]: "In this regime, loss graph construction is highly efficient: timings are predominantly below 50µs, with a mean of 18µs."

### (b) What it does NOT show
- Correlations are strictly between the two partners of a CZ gate (same gate); no inter-pair or spatial-range correlation; no
  parallel-gate crosstalk; mechanism is laser re-excitation after partner loss, not a BBR contaminant's 1/R^3 exchange.
- No physical rate model vs spacing, gate speed, n or T; p_l and p_c are free parameters.
- State dependence of loss is not simulated (Appendix B notes it).

### (c) K1 verdict: NO

### (d) Reuse/compare
- Decoder idea: a loss graph whose edges are physical correlated-loss mechanisms — directly extensible to our inter-pair
  edges (edges between atoms of DIFFERENT pairs within distance ~R_c). Eq. (6) local posterior p̃_e is a cheap baseline.
- Thresholds: 3.2% (independent decoder), 4% (correlated decoder, p_c = 1); rescaled per-atom 1.6%.
- Remaining-atom Pauli channel (1/8, 1/8, 3/8) for a partially excited survivor — reusable for our "neighbour got excited but not lost" branch.

---

## 5. arXiv:2604.21876 — Pecorari, Brennen, Kondov, Pupillo, "Loss-biased fault-tolerant quantum error correction" (Apr 2026)

### (a) What it shows
Fast QEC cycles let residual Rydberg population survive into the next gate; with time-optimal pulses the excitation "hops"
between the two atoms of a CZ, producing temporally correlated (non-Markovian) hook errors; mid-circuit ionization ("loss biasing") restores FT scaling.
Q[arXiv_2604.21876]: "We show that shorter QEC cycles amplify platformspecific errors, notably Rydberg excitation hopping, and hinder decay of residual Rydberg population, leading to non-Markovian correlated errors that degrade logical performance."
Q[arXiv_2604.21876]: "in neutralatom systems, this is primarily Rydberg hopping, i.e., the transfer of a Rydberg excitation during two-qubit gates [15]."
Q[arXiv_2604.21876]: "revealing that the time-optimal pulse mediates Rydberg excitation hopping between the two atoms involved in the CZ gate."
Interaction model: only data–ancilla blockade, B = 0 or infinity (no 1/R^3, no spacing):
Q[arXiv_2604.21876]: "assume only data-ancilla blockade with either Bij = 0 (perfect absence of interaction) or Bij = ∞ (infinitely strong interaction)."
Simulation scope: one 5-atom plaquette, effective Pauli channel, then Stim:
Q[arXiv_2604.21876]: "We simulate the open dynamics of the 5-atom surface code plaquette by generating trajectories from microscopic gate unitaries interleaved with decay events."
Q[arXiv_2604.21876]: "Backto-back gate schedules produce a non-fault-tolerant scaling ⌈d/4⌉, while perfect inter-gate ionization restores the faulttolerant Pauli scaling of ⌈d/2⌉ for Pauli errors."
Q[arXiv_2604.21876]: "Remarkably, we find that ionizing only the ancilla after each gate — assuming data–ancilla blockade — is already sufficient to preserve fault tolerance, whereas all other schedules fail to do so."
Q[arXiv_2604.21876]: "νall = 1.96, νancilla = 1.98, νtwice = 1.31, νhalfway = 1.23, νdata = 1.14, and νnone = 1.08."
BBR mentioned (P-state contaminants, ~100 µs lifetime, problematic at 4 µs gate spacing):
Q[arXiv_2604.21876]: "Recent experiments [9] identify black body–induced decay to nearby Rydberg P states (∼ 100µs lifetimes) as dominant error source."
Q[arXiv_2604.21876]: "Gate sequences with 4µs spacing are therefore prone to these errors, whereas circuits implemented via atom rearrangement are not, as they allow time for decay or for ejection when traps are pulsed on [9]."
Q[arXiv_2604.21876]: "Imperfections in the gate trajectory — both coherent (e.g. rotation errors, phase noise, crosstalk) and incoherent (e.g., blackbody transitions, spontaneous decay) — may leave residual population in Rydberg states."
Partner-correlated loss:
Q[arXiv_2604.21876]: "Specifically, if one atom decays during a gate, its interacting partner acquires a residual Rydberg population, increasing its probability of subsequent decay or of remaining in a Rydberg state susceptible to ionization."
Q[arXiv_2604.21876]: "Two-qubit CZ gates based on the Rydberg-blockade mechanism [8] now reach infidelities at the 10−3 level on sub-µs timescales, with a significant fraction of errors arising from leakage outside the computational subspace (∼40%) [9]."
Q[arXiv_2604.21876]: "Because autoionization is fundamentally unsuited for alkali atoms, we identify pulsed field ionization [35] as a highly efficient alternative loss-biasing strategy."

### (b) What it does NOT show
- Residual Rydberg population (including BBR P-state population) is assumed to act only on the SAME atom's later gates and its
  CZ partner (hopping); no interaction with other gate pairs; B_ij is 0 or infinity, so no 1/R^3 exchange or spacing dependence.
- Decay is modelled as amplitude damping back to |0>/|1>; the BBR contaminant is not a separate state with its own dipole couplings.
- Correlations are temporal/hook-like within one plaquette; no spatially correlated multi-pair errors in a parallel layer;
  no n or T dependence (only γ/Ω_max).

### (c) K1 verdict: NO
Closest in spirit (residual Rydberg population, including BBR P states, causing correlated errors in fast back-to-back cycles,
and ionization as the cure), but intra-pair/intra-plaquette only.

### (d) Reuse/compare
- Scaling exponents ν (d = 3): ⌈d/4⌉ without ionization vs ⌈d/2⌉ with; ν_all 1.96, ν_ancilla 1.98, ν_none 1.08 — benchmark format for showing FT degradation.
- Their cited ∼100 µs P-state lifetimes and 4 µs gate spacing give the contaminant persistence window relevant to our multi-layer estimate.
- Loss-biasing (ionize after each gate; ancilla-only suffices) is the natural mitigation baseline for our inter-pair errors.
- Note ref [9] (Bluvstein et al., Nature 649, 39) is the same architecture paper JILA cites as [13].
