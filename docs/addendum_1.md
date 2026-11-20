# Addendum 1 to the handover (received 2026-11-20): retarget to the thermal speed limit of the QEC cycle

Kept as received in substance; the owner's message is the source.

**Question.** What is the shortest interval between Rydberg gate layers, and hence the shortest QEC
cycle, that BBR allows at temperature T? Open problem 1 of the Stage 0 report is answered by clock
speed: it matters for every architecture wanting a shorter cycle than today's.

**Sourced facts quoted from the parent repository (params/params.yaml), to be re-read in the PDF:**
BLU25 Methods "Rydberg P-state decay": 400 us between gates for repeated surface-code stabilizer
measurement; 4 us in benchmarks. BLU25 Methods "Processor clock speed": rounds of 4.45 ms, from a
0.47 ms time between gates and 2.57 ms of ancilla exchange. BLU24 Methods: "the approximately 200 us
duration between gates". PEC26: P contaminants with ~100 us lifetimes (cited, approximate).
Parent result (not a source value): kinematic lower bound of BLU25's in-zone interval 92 us vs measured
470 us, margin 5.09 (plan/blocked/X1.2.md, docs/decisions/D007); geometry from a figure reading
(pitch 8.6 x 12.1 um) spot-checked by the owner. Schedules for reuse: experiments e39, e40, e41;
figure of merit atomclock/fom.py.

**Stage 1 (rescoped).** No fitted parameter: p_c(T, Omega, n) by manifold; tau_P(T, n) with radiative and
BBR parts and the contaminant's fate when traps return (anti-trapping, drift velocity, time to leave a
gate zone); E(R, theta, t) for a contaminant created a time t earlier at distance R; the excess error per
CZ against inter-layer delay t and spacing a for K layers. Derive t_wait = tau_P ln[K p_c n_R / eps] with
its domain of validity and test it against the numerics.

**Stage 2 (K3).** Pre-register against BLU25 ED Fig. 6g (fidelity vs time between gates and spacing),
tolerance from the figure's error bars stated before the run. Evered 2023 covariance is a weaker second test.

**Stage 3 (Gate 2).** T_c,min = L t_wait + readout, L = 4 (surface code) and L >= 10 (lifted product), at
300 K, 45 K, 4 K and vs Rabi frequency; compare with the kinematic floor; Gate 2 passes if the thermal
floor exceeds the kinematic one by >= 2 at 300 K for at least one schedule, stable under declared input
ranges. Translate to logical operations per second and audited runtimes. Circuit-level check that the
residual contaminant error at t_wait does not change the logical error beyond its statistical interval,
on a real gate-zone layout. State what removes the limit and its cost (cryogenic shielding, spacing,
faster gates, active P-state quench: sourced or marked unsourced).

**Kill tests.** K1 unchanged, search extended to derivations of a minimum inter-gate delay or cycle-time
limit from Rydberg contamination. K2 (replaces D003): fires if the delay needed for an excess error of
1e-4 per CZ is below the kinematic interval at 300 K in every published configuration. K3: fires if the
calculated curve disagrees with Fig. 6g beyond the pre-registered tolerance.

**Not to claim.** The effect, its measurement and the choice of 400 us are BLU25's.

**Not to pursue.** Superradiance on Rydberg microwave transitions (owner estimate: collective correction
< 1 % at 1e4 parallel excitations).
