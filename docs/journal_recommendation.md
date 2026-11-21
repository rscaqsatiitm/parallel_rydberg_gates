# Journal recommendation (Addendum 3, final item)

Date: 2026-11-21. Based on the Addendum 3 results (E16, E17, E18, E19) as committed on branch ccr-825341ea-tdqiim.

## Recommendation: Physical Review A

Submit the present draft (paper/main.tex, revtex4-2, PRA style) to Physical Review A. Do not submit to PRL or
PRX Quantum now. Reconsider a letter or PRX Quantum only if an experiment tests the same-layer floor.

## Reasons

**1. The physical effect is not ours, and the one comparison with data does not discriminate.** Bluvstein et al.
(arXiv:2506.20661) observed the contaminant effect and removed it with a 400 µs delay. They report the CZ fidelity
rising from 99.3 % to 99.5 % at 100 µs between gates (registry `bluvstein26.RB_vs_gap`, verified quote). Our model
agrees with their ED Fig. 6g within the error bars. However, its prediction band spans a factor of four, and a model
without contaminant motion agrees equally well (E06, K3 not fired). So the paper contains no experimental result that
confirms the model rather than merely being consistent with it. A letter normally rests on such a result.

**2. The new content is quantitative, and it is useful at the level of hardware design.** Three things are new.
(i) The error that one contaminant causes, as a function of distance, orientation and gate speed (half-error radius
10–12 µm at 4.6 MHz). (ii) The delay law. (iii) A same-layer floor that no delay removes: 0.7–1.1e-3 per CZ for a
row pitch of 8.57 µm, or 0.46–0.85e-3 for 10.0 µm, at 300 K and 4.6 MHz. That is 9 % to 22 % of the 5e-3 infidelity at
the 99.5 % benchmark (DERIVED). The floor's dependence on Ω, pitch and temperature is computed with no fitted
parameter. These are the results of a careful model paper. They set a design rule for dense parallel layers, but
they do not by themselves change how the field operates.

**3. Addendum 3 removed the strongest argument for a high-impact journal.** The surface-code result was the
candidate for broad interest: a correlated floor costing 4–10 times the logical error of independent noise. E18 showed
that this factor came mostly from the decoder (E10's own-model decoder depends on an arbitrary Pauli table, by a
factor of about 4.6). With the best decoder tested, the factor is 1.5–3.3 and shows no growth with distance up to
d = 11. Loss heralding with efficiency ≥ 0.8 removes 85–97 % of the excess. The honest logical conclusion is
therefore modest: the floor matters mainly through its marginal size, not through its correlation. In addition, the
logical layout is assumed and no likelihood-based decoder was available, so even this factor is decoder-bounded.

**4. The main limitations are input uncertainties that only the experimenters can close.** The published geometry
admits two readings of the row pitch, which change the floor by 21–34 %, the largest single input uncertainty. The
fidelity convention is not published either. Questions for the authors are drafted in docs/questions_for_authors.md
for the owner to send. PRA referees accept a stated, quantified input uncertainty. PRL and PRX Quantum referees will
ask why the comparison was not made against data that resolve it.

**5. The caesium synthetic-bath proposal is a prediction, not a result.** It is frozen before data (tag
cs-predictions-v1 on c4d0393 and cs-predictions-v2 on 854427e, both still to be pushed by the owner). Its best valid
operating points (3e3 K at 1 MHz with 12–15 µm spacing, or 1e4 K at 2 MHz with 10–12 µm, both with a floor of
1–3e-2) need 1–5e4 shots per point (E17). It strengthens the paper as a falsifiable test, but it does not raise the
present evidence to letter level.

## When to change the target

- **PRL or PRX Quantum** becomes appropriate if either of two experiments confirms the floor. The first is a measured
  CZ infidelity versus gate-site pitch at long inter-gate delay, which the model predicts with no parameter. The
  second is the caesium synthetic-bath experiment, which must reproduce the frozen predictions. The paper would then
  be co-authored with, or follow, the group that takes the data.
- **PRX Quantum** also becomes reasonable if a likelihood-based decoder (BP+OSD or tensor network) shows a correlation
  penalty that survives realistic heralding. On present evidence that outcome is not expected.

## Verification notes

- All numbers above come from the committed experiment READMEs and paper/VERIFICATION.md (types SIM, SOURCE, DERIVED).
  The 9–22 % figure is (0.46e-3 to 1.1e-3)/5e-3. Most of that span is the uncertainty in the row-pitch reading,
  not a measured range.
- Confidence labels:
  - Reasons 1, 3 and 4: Well-supported (they follow from our own pre-registered results).
  - The judgment about journal thresholds: Provisional. The scope statements of PRL, PRX Quantum and PRA were not
    re-read in this session, so the characterisation of their criteria is from general knowledge and is unverified.
- The decoder finding rests on one circuit builder (E18/e18.py on the E10 model). It should be reproduced with an
  independently written builder before submission.
