import sys, time, numpy as np
sys.path.insert(0, "src")
from prg.model import Config, ThreeAtom, run_gate, cz_fidelity, error_components
from prg.atomic import Level
def c0_of(m, lev): return 2 + m.ryd.index(lev) - m.nS   # C basis: ryd list (S first) -> index
cfg = Config()
m = ThreeAtom(cfg)
cP = m.ryd.index(Level(52, 1, 1.5, 1.5))     # index in C basis (C basis == ryd list)
t = time.time()
U0 = run_gate(m, None, [cP])[cP][cP]
F, th = cz_fidelity(U0)
print(f"[1] blockade 450 MHz: CZ fidelity {F:.6f}, theta {th:.4f}, |diag| {np.round(np.abs(np.diag(U0)),6)}, {time.time()-t:.1f}s")
# (1e5 MHz blockade run is in run_hiblock.py)


# [2] convergence and [3] null: contaminant in 52P3/2 mJ=3/2, R along x (row axis), B along z (normal)
def contaminant_error(model, rC, cP, U_ref):
    K = run_gate(model, rC, [cP])[cP]
    return error_components(K, U_ref)
for ns in (600, 1200):
    mm = ThreeAtom(Config(nsteps=ns)); Ur = run_gate(mm, None, [cP])[cP][cP]
    print(f"[2] nsteps {ns}: R=8 um along row, err/leak/pauli =", np.round(contaminant_error(mm, (8.0, 0, 0), cP, Ur), 8))
Ur = U0
print("[3] R=200 um:", contaminant_error(m, (200.0, 0, 0), cP, Ur))
# [4] corrupted inputs
import prg.atomic as pa
orig = pa.dipole_cartesian
try:
    def bad(species, levels):
        dx, dy, dz = orig(species, levels); dyb = dy.copy(); dyb[np.triu_indices_from(dyb, 1)] *= -1
        for M in (dyb,):
            assert np.allclose(M, M.conj().T), "dipole not Hermitian"
        return dx, dyb, dz
    bad("Rb87", pa.manifold(53, 0) + pa.manifold(52, 1)); print("[4] corrupted dy NOT caught")
except AssertionError as e:
    print("[4] corrupted dy caught:", e)
import prg.model as pm
op = pm.pulse_phase
pm.pulse_phase = lambda cfg: (op(cfg)[0], op(cfg)[1], (lambda t: 0.0))
print("[4] zero phase modulation: CZ fidelity", cz_fidelity(run_gate(ThreeAtom(cfg), None, [cP])[cP][cP])[0])
pm.pulse_phase = op
