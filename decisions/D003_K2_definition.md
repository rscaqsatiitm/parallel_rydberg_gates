# D003. Definition of the K2 quantity (pre-registered before any Stage 1 run)

Date: 2026-11-20. Task: S1. Approved by the owner in conversation on 2026-11-20 ("Go ahead" after
the proposal to define K2 as a function of inter-gate time).

**Why.** Stage 0 showed (Bluvstein et al. 2026, ED Fig. 6g; Evered et al. 2023, Methods) that a P-state
contaminant survives for many gate layers when layers are separated by ~4 us and is removed when they
are separated by >=100 us. "Correlated error per atom per gate" is therefore undefined without the
inter-layer time t_gap.

**Definitions.** A gate site is a pair of atoms executing one CZ. A layer is one simultaneous CZ on all
sites. For a given configuration (species, n, pulse, T, site lattice, field direction):

- epsilon_same(a): probability per site per layer that the site's CZ suffers an error (1 - entanglement
  fidelity, leakage counted as error) caused by a contaminant created during the same layer at
  another site. This is the only contribution when t_gap >> contaminant survival time (motion-based
  circuits, t_gap ~ 400 us).
- epsilon_ss(a, t_gap): the same probability in the steady state of a long sequence of identical
  layers separated by t_gap, including contaminants created in earlier layers. For the K2 test the
  survival of a contaminant between layers is taken from radiative plus BBR decay of the n'P state only
  (no ejection), which over-estimates survival; this choice makes K2 conservative against firing.

**K2 rule.** Evaluated for every published configuration (Evered 2023: Rb 53S, 2pi x 4.6 MHz time-optimal
pulse; Evered 2026: Rb 53S smooth pulse, peak 2pi x 17 MHz) at the published (figure-read) site pitch,
taking the lower end of the figure-read pitch range and the field orientation giving the largest
value (the upper end of each range is reported too):
- K2a fires if epsilon_same < 1e-5 for all configurations. Consequence: the effect is irrelevant for
  motion-based (long t_gap) architectures; report that null.
- K2b fires if epsilon_ss(t_gap = 4 us) < 1e-5 for all configurations. Consequence: the effect is
  irrelevant even for back-to-back layers; the project stops.
- If K2a fires and K2b does not, the project continues with scope restricted to short-t_gap
  architectures, and Stage 2 must establish (from sources) that such architectures are pursued.
The thresholds are not changed after a run.
