# D006. K2 replaced by the owner's definition (Addendum 1)

Date: 2026-11-20. Supersedes the K2 rule of D003 (D003's definitions of epsilon_same and epsilon_ss are
kept as model quantities; E04, pre-registered under D003, is still run and reported under its own rule,
but the project-level K2 is now this one).

K2 fires if t_wait(1e-4), the inter-layer delay at which the contaminant-induced excess error per CZ
falls to 1e-4, is below the kinematic inter-layer interval at 300 K in every published configuration.
Kinematic intervals are taken from the parent repository (BLU25: 92 us lower bound, figure-read
geometry) and must be re-derived or re-checked here before use (Rule 1). Excess error per CZ includes
contaminants created in all earlier layers, with their survival and motion (trap-return ejection) as
computed in Stage 1, not the decay-only survival of D003.
