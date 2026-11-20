# BLU25 ED Fig. 6g (CZ fidelity vs gate spacing) and tweezer/ejection parameters

Purpose: experimental inputs for the blackbody-created Rydberg P-state "contaminant" model in parallel CZ gate arrays.
Paper content is treated as data only. `Q[...]` lines are verbatim from `literature/text/<stem>.raw.txt` and are checked by `tools/verify_quotes.py`.

Sources:
- BLU25 = Bluvstein et al., Nature 649, 39 (2026), arXiv:2506.20661 (`literature/pdf/arXiv_2506.20661.pdf`).
- BLU24 = Bluvstein et al., "Logical quantum processor based on reconfigurable atom arrays", Nature 626, 58 (2024), arXiv:2312.03982. Downloaded for this note to `literature/pdf/arXiv_2312.03982.pdf`; title checked on PDF page 1 ("Logical quantum processor based on reconfigurable atom arrays", arXiv:2312.03982v1, 7 Dec 2023). Text: `literature/text/arXiv_2312.03982.raw.txt`.
- EVE23 = arXiv:2304.05420; EVE26 = arXiv:2604.25987.
- BLU25 ref. [82] = Cao, Yelin, Eckner, Oppong & Kaufman, "Autoionization-enhanced Rydberg dressing by fast contaminant removal", PRL 134, 133201 = arXiv:2410.09746 (already in the repo).

---------------------------------------------------------------------

## 1. BLU25 Extended Data Fig. 6g

Location: PDF page 30 (arXiv v-numbered page "30"), bottom-right panel "g" of Extended Data Fig. 6.
Images: `literature/notes/fig/blu25_EDfig6g_600dpi.png` (panel g, 600 dpi crop), `literature/notes/fig/blu25_EDfig6g_zoom_plotarea.png` (2x zoom of plot area), `literature/notes/fig/blu25_page30_200dpi-30.png` (whole page).

### Caption (verbatim, panel g sentence plus figure title)
Q[arXiv_2506.20661]: "Extended Data Fig. 6. Additional data for repeated QEC characterization circuit."
Q[arXiv_2506.20661]: "g, CZ gate fidelity measured via randomized benchmarking [36]. Infidelity due to Rydberg P states is removed by leaving sufficient time or distance between gates. Sparse corresponds to 2x larger separation between gate sites."
(Ref. [36] in BLU25 = EVE23, Evered et al. 2023.) The caption does not say what the error bars represent: NOT FOUND.

### Axes and legend (FIGURE READ)
- y label: "CZ fidelity in RB seq. (%)". Linear. Range 99.2 to 99.6 (axis frame spans exactly 99.2-99.6). Labelled major ticks 99.2, 99.4, 99.6; unlabelled minor ticks at 99.3 and 99.5.
- x label: "Gate spacing (μs)" (i.e. time between gates). LINEAR (labels 0, 200, 400 equally spaced: pixel positions 361, 582.5, 804 at 600 dpi). Unlabelled minor ticks at 100 and 300. Axis runs from 0 to about 450 μs (right frame edge at ~450 μs, FIGURE READ).
- Legend: "Normal" (light blue, open-ish light fill circles, light line) and "Sparse" (dark navy filled circles, dark line). There is no series called "dense"; "Normal" is the denser default array. Only these two series.
- Calibration used for reading: 1652.5 px per 1 % fidelity (0.000605 %/px), 1.1075 px per μs (600 dpi crop). Marker radius about 13 px fill + outline (about +-0.009 % in y), so error bars shorter than that are hidden.

### Data (FIGURE READ; pixel-centroid extraction of the 600 dpi render, then checked by eye)

| Series | x = gate spacing (μs) | y = CZ fidelity (%) | error-bar half-width (%) | notes |
|---|---|---|---|---|
| Normal | 50 | 99.312 | 0.015 | x at pixel 416.2 -> 49.9 μs |
| Normal | 100 | 99.487 | 0.033 | bar symmetric (297-406 px) |
| Normal | 200 | 99.482 | 0.014 | |
| Normal | 400 | 99.488 | < ~0.010 (bar hidden inside marker) | |
| Sparse | 50 | 99.558 | 0.020 | |
| Sparse | 100 | 99.474 | ~0.025 (only lower half visible; assumed symmetric) | marker mostly hidden behind Normal 100 μs marker; centre inferred from visible outline |
| Sparse | 200 | 99.543 | 0.031 | |
| Sparse | 400 | no point | - | Sparse series has only 3 points |

Reading uncertainty (FIGURE READ): x positions +-2 μs (they coincide with 50/100/200/400 to within 0.2 μs, so nominal values are very likely 50, 100, 200, 400 μs); y centres +-0.002 % for fully visible markers, +-0.006 % for the occluded Sparse 100 μs marker; error-bar half-widths +-0.002 % (+-0.005 % for Sparse 100 μs). Values given to 0.001 % are pixel-level, not more precise than that.

Consistency with text: the Methods text says fidelity "increases from 99.3% to 99.5% by increasing duration between gates to 100 µs" (quote below), matching Normal 50 μs -> 100 μs. Note the plot's smallest x is 50 μs, not the 4 μs of the EVE23 benchmark.

### Text about the measurement (BLU25 Methods, "Analysis of error correlations", paragraph "Decay to Rydberg P states.")
Q[arXiv_2506.20661]: "Concretely, during Rydberg gates, roughly 0.07% of the error budget is decay of Rydberg atoms to adjacent Rydberg P states."
Q[arXiv_2506.20661]: "These states have a strong, long-ranged interaction with the Rydberg S states that are used for the gates, and can thereby affect gates occurring in a different site, and moreover can have lifetimes of over 100 µs."
Q[arXiv_2506.20661]: "In ED Figure 6g, we plot the CZ gate fidelity in a repeated benchmarking sequence as a function of the duration between the gates, and find that the gate fidelity in this array increases from 99.3% to 99.5% by increasing duration between gates to 100 µs, as the Rydberg atoms decay or eject during that time."
Q[arXiv_2506.20661]: "Analogously, we observe that this gate fidelity reduction is removed by reducing atom density."

### Geometry / number of sites for the Fig. 6g measurement
- Gate-site spacing for Fig. 6g: NOT FOUND (only the relative statement "2x larger separation between gate sites").
- Number of gate sites / atoms used in the Fig. 6g RB measurement: NOT FOUND.
- Array geometry for Fig. 6g specifically: NOT FOUND ("in this array" is not further specified). The nearest geometry statements in BLU25 Methods are for the surface-code and deep-circuit configurations:
Q[arXiv_2506.20661]: "The 420-nm and 1013-nm Rydberg tophat beams cover 7 rows of gate sites in the entangling zone and are homogenized to ≈1% peak-to-peak variation over a vertical extent of 60 µm."
Q[arXiv_2506.20661]: "Within this zone, entangling gates are performed simultaneously on up to 256 qubits across 8 rows and 16 columns of gate sites with a horizontal extent of 175 µm."
  (175 μm / 16 columns implies roughly 11 μm column pitch if evenly spaced; this is my inference, not a stated number.)
- Intra-site / inter-site distances are given in BLU24 (same apparatus, same n = 53 gate):
Q[arXiv_2312.03982]: "During two-qubit Rydberg (n=53) gates, we place atoms ≲ 2 µm apart within a “gate site”, resulting in ≳ 450 MHz interaction strength between pairs, significantly larger than the Rabi frequency of 4.6 MHz."
Q[arXiv_2312.03982]: "Gate sites are separated such that atoms in different gate sites are no closer than 10 µm during the gate, resulting in negligible long-range interactions."
Q[arXiv_2312.03982]: "At our present n = 53 and two-photon Rabi frequency of 4.6 MHz, the blockade radius is roughly 4.3 µm, such that adjacent atoms are well-within blockade and distant atoms are well-outside blockade."

### BLU25 gate parameters
- Gate duration 270 ns, n = 53 (53S1/2 in ED Fig. 1c level diagram), 420 nm + 1013 nm, intermediate detuning 4.8 GHz:
Q[arXiv_2506.20661]: "Entangling gates (270-ns duration) between clock qubits are performed with fast two-photon excitation using 420-nm and 1013-nm Rydberg beams to n=53 Rydberg states, utilizing a time-optimal two-qubit gate pulse [68] detailed in Ref. [36], in this work with the 420-nm laser red-detuned by 4.8 GHz from the intermediate state."
- Rydberg Rabi frequency 4.6 MHz (stated in the leakage discussion):
Q[arXiv_2506.20661]: "in the practical operating conditions of 8.6 G, the level spacings of 6 MHz (compared to Rabi frequency of 4.6 MHz) mean that adjacent hyperfine states can still off-resonantly couple to the Rydberg state"
- Rydberg state label in ED Fig. 1c: "53S1/2" (figure text, line 3317 of raw text). Error budget numbers:
Q[arXiv_2506.20661]: "Decrease gate time from 270 ns to 135 ns, reducing Rydberg T1 error from 0.113% to 0.057%, and reducing dephasing error from 0.134% to 0.034%."
Q[arXiv_2506.20661]: "Although we achieve CZ fidelities of 99.6%, drifts since the last calibration (several days in the context of the surface code benchmarking) often contribute 0.05 − 0.1% error during final data taking."

---------------------------------------------------------------------

## 2. Quote verification

(a) BLU25 Methods "Processor clock speed" — CONFIRMED with wording difference: the paper says "This originated from 0.47 ms time between gates" (no article "a"). Location: Methods, section "Processor clock speed", PDF page 20.
Q[arXiv_2506.20661]: "In the repeated surface code experiments in Figure 2, each QEC round was 4.45 ms. This originated from 0.47 ms time between gates, and a total of 2.57 ms from moving the ancilla atoms to the storage zone and bringing in the next group to the entangling zone."

(b) BLU25 "Rydberg P-state decay" paragraph — CONFIRMED; the paragraph heading is actually "Decay to Rydberg P states." (Methods, "Analysis of error correlations", PDF p. 15-16). 4 μs and 400 μs quotes:
Q[arXiv_2506.20661]: "During repeated benchmarking sequences, like the ones reported in Ref. [36], we have only 4 µs between gates, and consequently Rydberg P atoms can survive for many layers of gates and corrupt gates in distant sites."
Q[arXiv_2506.20661]: "In quantum circuits based on atom motion, the duration between gates is sufficiently long (e.g., 400 µs for surface code repeated stabilizer measurements) for these Rydberg P states to decay or eject [82], which natively fixes this issue, and consequently we do not observe such effects during quantum circuits."
Q[arXiv_2506.20661]: "This also implies the reported gate fidelity in Ref. [36] may have been impacted by this effect and thereby underestimating the maximum gate fidelity."
Note: "400 µs" (P-state paragraph) and "0.47 ms" (clock-speed section) are both given for the surface-code time between gates; they are not identical numbers.

(c) BLU24 Methods "the approximately 200 μs duration between gates" — CONFIRMED with wording difference: the paper writes "∼ 200 µs duration between gates" (tilde, not "approximately"). Location: BLU24 Methods, "Programming circuits", "Zone parameter choices" paragraph (PDF p. 12-13).
Q[arXiv_2312.03982]: "Although Ref. [8] appears to find some small cross-talk seemingly originating from decay into Rydberg P states, this should be considerably suppressed in the practical operation here due to the ∼ 200 µs duration between gates, during which time Rydberg atoms should either fly away or decay back to the ground state."
Q[arXiv_2312.03982]: "Motion is realized with a cubic profile as in Ref. [7], the characteristic free-space movement time between gates is roughly 200 µs, and acoustic lensing effects from the AOD are estimated to be negligible."

---------------------------------------------------------------------

## 3. Optical tweezer parameters and fate of Rydberg atoms when traps return

| Quantity | BLU25 | BLU24 | EVE23 | EVE26 |
|---|---|---|---|---|
| Tweezer wavelength | 852 nm SLM and 852 nm AOD | 852 nm SLM, 850 nm AOD | 850 nm SLM, 810 nm AOD | 852 nm SLM and AOD |
| Trap depth during gates | NOT FOUND (entangling/storage zones at half the readout/reservoir intensity) | NOT FOUND in mK; AOD ~2x SLM depth; ~5 mK used only for mid-circuit imaging | ~1 mK | NOT FOUND |
| Atom temperature | numeric value only in figures (Fig. 5c, ED Fig. 3); NOT FOUND in text | NOT FOUND | ~10 μK | ~12 μK |
| Tweezer waist | NOT FOUND for traps (2.5 μm is stated for the local Raman "tweezer", see note) | NOT FOUND (1.9 μm is the local Raman beam) | NOT FOUND | NOT FOUND |
| Traps off during gate | "briefly pulsed off" (BLU24 wording); BLU25: NOT FOUND | briefly pulsed off by TTL | a few hundred ns; recaptured ~3 μs between consecutive gates | a few hundred ns; traps back on within 100 ns after gate pulse |
| Rydberg atom when traps return | "decay or eject"; "expelled from the tweezer" (theoretically); metastable anti-trapping | "fly away or decay back to the ground state" | Rydberg state anti-trapped; leftover Rydberg atoms "expelled from the array" with ~100 μs delay | Rydberg state anti-trapped -> loss; timing-dependent |
| Photoionisation by tweezer light | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Ejection time / velocity | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |

### BLU25
Q[arXiv_2506.20661]: "The Rb atoms are then loaded stochastically into programmable, static arrangements of 852-nm traps generated with a spatial light modulator (SLM, Hamamatsu X13138-02), and then rearranged with a set of 852-nm moving traps generated by a pair of crossed acousto-optic deflectors (AODs, DTSX-400, AA Opto-Electronic) to realize defect-free arrays [62–64]."
Q[arXiv_2506.20661]: "The trap intensities in the entangling and storage zones are set to half of those in the readout and reservoir zones to improve qubit coherence."
Q[arXiv_2506.20661]: "Crucially, in our approach with a low atomic density and several hundred microseconds between gates, the Rydberg atoms (theoretically) either decay to the ground state or are expelled from the tweezer."
Q[arXiv_2506.20661]: "In this way, such Rydberg leakage either convert into an error within the computational subspace, a leakage into adjacent hyperfine states, or a loss event."
Q[arXiv_2506.20661]: "We observe that with several hundred microseconds between gates, effects of Rydberg leakage are not apparent, and during our repeated QEC data we observe that our leakage is at least 80% loss (ED Fig. 5b)."
Q[arXiv_2506.20661]: "This observation suggests that various scattering channels [43] naturally loss-convert, likely due to anti-trapping of metastable states."
Q[arXiv_2506.20661]: "The SLM trap depth is adiabatically ramped down to ∼ 5 µK and held for 5-ms before being ramped back up"
  (this 5 μK is a temperature-measurement ramp-down depth, not the operating depth.)
Q[arXiv_2506.20661]: "Since the magnitude of the maximum off-axis field falls off linearly with tweezer waist, we mitigate this by increasing the waist to 2.5 µm."
  (Context: local single-qubit Raman gates; the "tweezer" here is most likely the focused Raman beam, so this is NOT a reliable trapping-tweezer waist. Ambiguous.)
Q[arXiv_2506.20661]: "Our coherence time in 852-nm traps is approximately 1-2 seconds depending on the dynamical decoupling sequence applied."

### BLU24
Q[arXiv_2312.03982]: "static arrangements of 852-nm traps generated with a spatial light modulator (SLM), and then rearranged with a set of 850nm moving traps generated by a pair of crossed acousto-optic deflectors"
Q[arXiv_2312.03982]: "During Rydberg gates the traps are briefly pulsed off by a TTL."
Q[arXiv_2312.03982]: "we ramp up the AOD tones’ intensity (with quadratic intensity profile when possible) corresponding to the appropriate sites over a time of 100-200 µs to a trap depth ∼2x larger than the SLM trap depth"
Q[arXiv_2312.03982]: "we use deep (roughly 5-mK) traps (helping retain the atoms), and stroboscopically pulse them on and off out of phase of the local imaging light"
  (5 mK applies to mid-circuit imaging, not to gates.)
Q[arXiv_2312.03982]: "The focused beam waist in the plane of the atoms is 1.9 µm, which is large enough to be robust to fluctuations in atomic positions"
  (local Raman beam waist, not trap waist.)

### EVE23 (arXiv_2304.05420)
Q[arXiv_2304.05420]: "programmable array of 850-nm optical tweezers generated by a spatial light modulator (SLM). A second set of 810-nm optical tweezers generated by a crossed pair of acousto-optic deflectors (AODs) is then used to rearrange into defect-free arrangements [2]."
Q[arXiv_2304.05420]: "We estimate an average radial motional quantum number of n̄ ≈ 1 − 2 from fitting a droprecapture curve [60] to ∼ 10 µK in ∼ 1 mK deep traps."
Q[arXiv_2304.05420]: "Traps are pulsed off for a few hundred ns during the Rydberg gate to avoid both anti-trapping of the Rydberg state and inhomogeneous light shifts that broaden the transition, and the ground state atoms are then recaptured for roughly ∼ 3µs between consecutive gate applications."
Q[arXiv_2304.05420]: "the ∼ 100 µs delay between subsequent gates would result in leftover Rydberg states being expelled from the array, completely suppressing the effect from Rydberg decay described above."
Q[arXiv_2304.05420]: "we place atoms at 2 µm separation in order to achieve strong interaction strength VRyd /2π ≈ 450 MHz."

### EVE26 (arXiv_2604.25987)
Q[arXiv_2604.25987]: "array of static 852-nm optical tweezers generated with a spatial light modulator (SLM, Hamamatsu X13138-02)"
Q[arXiv_2604.25987]: "We rearrange the atoms using a second set of 852-nm optical tweezers generated from two-dimensional acousto-optic deflectors"
Q[arXiv_2604.25987]: "We pulse the traps off for a few hundred nanoseconds during the gate."
Q[arXiv_2604.25987]: "This loss conversion occurs because the tweezer traps are turned on within 100ns after the end of the gate pulse, and the Rydberg state is anti-trapped."
Q[arXiv_2604.25987]: "For example, excited states are anti-trapped which can lead to loss when the traps are turned back on depending on the exact timing, excited state lifetime, and branching ratios."
Q[arXiv_2604.25987]: "we estimate the atom temperature to be around 12µK from a Doppler decoherence model, similar to estimates from drop-recapture measurements [63]."
Q[arXiv_2604.25987]: "For benchmarking, we typically use a sparse array of 8 gate sites, in order to reduce the effect of decay of Rydberg states to nearby P states on the measured fidelity [24]."
Q[arXiv_2604.25987]: "We operate with the pair of atoms within each gate site separated by about 1.73µm, where the blockade energy is around 950 MHz."

### BLU25 ref. [82] (arXiv_2410.09746, Cao et al., Kaufman group)
What it is: NOT a study of Rydberg-atom ejection from Rb tweezers. It is 88Sr in an optical lattice, removing BBR-created opposite-parity "contaminant" Rydberg atoms by autoionization (AI) with a ~407.89 nm laser in a stroboscopic dressing sequence. "Eject" in [82] refers to the AI electron and to the ion being carried away by stray fields, not to tweezer expulsion. No ejection time or velocity for neutral Rydberg atoms in tweezers: NOT FOUND. Relevant numbers: AI pulse 0.2-0.3 μs, wait 2 μs for the ion to leave, stray field ~360 mV/cm.
Q[arXiv_2410.09746]: "In this process, BBR drives transitions from the target Rydberg state |r⟩ to a set of nearby, opposite-parity Rydberg (contaminant) states |r′ ⟩."
Q[arXiv_2410.09746]: "Critically, the collective loss can be triggered by only a single contaminant (Rydberg atom), causing the loss rate to grow for increasing ensemble size."
Q[arXiv_2410.09746]: "Contaminants created during each short pulse decay back to low-lying atomic states during the wait, preventing facilitated excitation on subsequent pulses."
Q[arXiv_2410.09746]: "In divalent atoms, such removal can be performed by exciting the remaining core electron to an autoionizing (AI) state [56, 57]; from this state, the Rydberg electron is ejected due to its interaction with the core electron."
Q[arXiv_2410.09746]: "Schematic illustration of the experimental setup with 88 Sr atoms (circles) trapped in an optical lattice"
Q[arXiv_2410.09746]: "To ensure a high degree of contaminant removal, we use tAI = 0.2–0.3 µs for SRD."
Q[arXiv_2410.09746]: "We observe δr decay for longer durations twait after the AI pulse as the ion moves further away. The dominant mechanism for ejecting the ions is likely to be acceleration by stray electric fields, which we infer to be at the 360(20) mV/cm level [65]. For use in Rydberg dressing, we fix twait = 2 µs, which is the dominant limitation for the currently achievable duty cycle."
