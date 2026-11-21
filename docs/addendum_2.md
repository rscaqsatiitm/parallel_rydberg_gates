# Addendum 2 (owner, 2026-11-21): predictions for a synthetic-bath experiment in caesium

The owner plans an experiment in a new Cs tweezer laboratory. Produce, pre-registered and with provenance:
1. For Cs nS, n = 50 to 80: contaminant probability per atom per gate, by final state, at 300 K; contaminant
   lifetimes; the transition frequencies a noise source must cover. Recommend n.
2. The error kernel E(R, theta, t) on a blockade sequence and on a Rydberg Ramsey sequence, for a contaminant
   prepared deterministically in n'P. State the contrast needed to resolve it at R = 5, 10, 20 um.
3. The same quantities under a band-limited bath of effective temperature T_eff from 300 K to 1e6 K: what scales
   linearly, what saturates, where population spreads to states that no longer exchange resonantly. Is a
   band-limited, single-direction, polarised noise field equivalent to a blackbody for these rates? Give the
   correction factors.
4. The delay law against T_eff, and the number of shots needed to test it at 10 % at each T_eff with 2 to 10
   atoms and 90 to 95 % contrast.
5. Candidate quench transitions that remove n'P contaminants within 1 us, with wavelengths and powers, each
   sourced or marked unsourced.
Freeze these predictions in a tagged commit before any data exist.

Also requested in the same message: the circuit-level (Stim) simulation (open problem 2 of docs/gate2_report.md),
task S4, experiment E10.
