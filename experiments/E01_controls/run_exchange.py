# [5] exchange planted answer: A held in nS mJ_r (no laser), B in |0>, C in n'P at R along B axis.
import sys, numpy as np, scipy.linalg as la
sys.path.insert(0, "src")
from prg.model import Config, ThreeAtom
from prg.atomic import Level, manifold, dipole_q, level_energy_MHz, K_DD
from scipy.sparse.linalg import expm_multiply
cfg = Config(); m = ThreeAtom(cfg)
R = 10.0
H, L = m.hamiltonian_static((R, 0, 0))   # contaminant along x; set field along x to make it "along B"
m = ThreeAtom(Config(bfield_dir=(1.0, 0, 0))); H, L = m.hamiltonian_static((R - cfg.d_pair / 2, 0, 0))   # A at -d/2 => |r_C - r_A| = R
# initial: A in S(mj_r), B in |0>, C in 52P3/2 mJ=+1/2
a0 = 2 + m.ir; c0 = m.ryd.index(Level(52, 1, 1.5, 0.5))
N = m.dG ** 2 * m.dC; psi = np.zeros(N, complex); psi[m.basis_index(a0, 0, c0)] = 1
ts = np.linspace(0, 0.5, 11)
pops_model = [abs(expm_multiply(-2j * np.pi * t * H, psi)[m.basis_index(a0, 0, c0)]) ** 2 for t in ts]
# independent: 2-atom space S (x) P  +  P (x) S, along quantization axis: V = K (dA.dC - 3 dAz dCz)/R^3
S = manifold(53, 0); P = manifold(52, 1)
basis = [(s, p) for s in S for p in P] + [(p, s) for p in P for s in S]
def E(lv):
    ref = level_energy_MHz("Rb87", Level(53, 0, 0.5, 0.5), 8.5) if lv.l == 0 else level_energy_MHz("Rb87", Level(52, 1, 1.5, 0.0), 0.0)
    return level_energy_MHz("Rb87", lv, 8.5) - ref
Hd = np.zeros((len(basis),) * 2, complex)
for i, (x1, y1) in enumerate(basis):
    Hd[i, i] = E(x1) + E(y1)
    for k, (x2, y2) in enumerate(basis):
        # d_A . d_C - 3 d_Az d_Cz in spherical components: sum_q (-1)^q dA_q dC_-q - 3 dA_0 dC_0
        v = sum((-1) ** q * dipole_q("Rb87", x1, x2, q) * dipole_q("Rb87", y1, y2, -q) for q in (-1, 0, 1)) \
            - 3 * dipole_q("Rb87", x1, x2, 0) * dipole_q("Rb87", y1, y2, 0)
        Hd[i, k] += K_DD * v / R ** 3
i0 = basis.index((Level(53, 0, 0.5, 0.5), Level(52, 1, 1.5, 0.5)))
w, V = la.eigh(Hd)
pops_ind = [abs((V @ (np.exp(-2j * np.pi * w * t) * V.conj()[i0])))[i0] ** 2 for t in ts]
print("[5] model     :", np.round(pops_model, 6))
print("[5] independent:", np.round(pops_ind, 6))
print("[5] max |diff| =", np.max(np.abs(np.array(pops_model) - np.array(pops_ind))))
