"""Gate pair (A, B) executing a CZ pulse, perturbed by one contaminant C in an n'P state (D004).

Units: MHz (frequencies, as ordinary not angular: H/h), us (time), um (length). The Schroedinger
equation is d psi/dt = -2 pi i H psi with H in MHz.

Rotating frame: |1> at 0; the laser-target Rydberg level nS mJ_r at 0 (resonant drive); every other
Rydberg level at its energy relative to its own reference (S levels relative to nS mJ_r, P levels
relative to n'P3/2 at zero field). A constant per P excitation is dropped; this is exact because the
number of P excitations is conserved (the laser couples only |1> <-> S, and first-order dipole terms
only exchange S <-> P between two atoms).
"""
from __future__ import annotations
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
from dataclasses import dataclass, field
from .atomic import Level, manifold, dipole_cartesian, level_energy_MHz, K_DD


@dataclass
class Config:
    species: str = "Rb87"
    n: int = 53
    mj_r: float = 0.5
    nprime: int = 52
    B_G: float = 8.5
    bfield_dir: tuple = (0.0, 0.0, 1.0)     # lab-frame unit vector of B (quantization axis)
    d_pair: float = 2.0                     # um, A-B distance (A at -d/2 x, B at +d/2 x)
    blockade_MHz: float = 450.0             # S-S shift at d_pair, fixes C6 = V d^6
    Omega_MHz: float = 4.6                  # Omega / 2 pi
    pulse: str = "evered23_TO"
    nsteps: int = 600


def pulse_phase(cfg: Config):
    """Returns (T_us, amp(t) in MHz (Omega/2pi), phi(t))."""
    if cfg.pulse == "evered23_TO":
        Om = 2 * np.pi * cfg.Omega_MHz           # rad/us
        A, w, phi0, d0 = 2 * np.pi * 0.1122, 1.0431 * Om, -0.7318, 0.0
        T = 2 * np.pi * 1.215 / Om
        return T, (lambda t: cfg.Omega_MHz), (lambda t: A * np.cos(w * t - phi0) + d0 * t)
    if cfg.pulse == "evered23_TO_cal":
        Om = 2 * np.pi * cfg.Omega_MHz
        A, w, phi0, d0 = 2 * np.pi * 0.0988, 1.3629 * Om, -2.6082, -0.0187 * Om
        T = 2 * np.pi * 1.215 / Om
        return T, (lambda t: cfg.Omega_MHz), (lambda t: A * np.cos(w * t - phi0) + d0 * t)
    raise ValueError(cfg.pulse)


def _rot_to_B(bdir):
    """Rotation matrix taking lab vectors to the frame whose z axis is along B."""
    z = np.asarray(bdir, float); z /= np.linalg.norm(z)
    t = np.array([1.0, 0, 0]) if abs(z[0]) < 0.9 else np.array([0, 1.0, 0])
    x = t - z * (t @ z); x /= np.linalg.norm(x); y = np.cross(z, x)
    return np.vstack([x, y, z])


class ThreeAtom:
    """Hilbert space A (x) B (x) C. A, B: [0, 1, S(-1/2), S(+1/2), P(n') x6]; C: [S x2, P x6]."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        S = manifold(cfg.n, 0)
        P = manifold(cfg.nprime, 1)
        self.ryd = S + P
        self.nS, self.nP = len(S), len(P)
        dx, dy, dz = dipole_cartesian(cfg.species, self.ryd)
        self.d_ryd = [dx, dy, dz]
        # energies (MHz) in the rotating frame
        Eref_S = level_energy_MHz(cfg.species, Level(cfg.n, 0, 0.5, cfg.mj_r), cfg.B_G)
        Eref_P = level_energy_MHz(cfg.species, Level(cfg.nprime, 1, 1.5, 0.0), 0.0)
        self.E_ryd = np.array([level_energy_MHz(cfg.species, lv, cfg.B_G) - (Eref_S if lv.l == 0 else Eref_P)
                               for lv in self.ryd])
        self.iS = list(range(self.nS)); self.iP = list(range(self.nS, self.nS + self.nP))
        self.ir = [i for i, lv in enumerate(self.ryd) if lv.l == 0 and lv.m == cfg.mj_r][0]
        self.dG, self.dC = 2 + len(self.ryd), len(self.ryd)
        self.C6 = cfg.blockade_MHz * cfg.d_pair ** 6
        self.R_B = _rot_to_B(cfg.bfield_dir)
        self._static_pair = self._build_pair_static()

    # ---- single-atom embeddings -------------------------------------------------------------
    def _gate_op(self, M_ryd):
        """Embed a Rydberg-space operator into a gate atom (ground states untouched)."""
        M = np.zeros((self.dG, self.dG), complex); M[2:, 2:] = M_ryd; return M

    def _dd(self, MA, MB, rvec):
        """First-order dipole-dipole operator between two atoms with Rydberg-space dipoles MA, MB.

        V = K [dA.dB - 3 (dA.n)(dB.n)] / R^3, with vectors expressed in the B-field frame.
        """
        rb = self.R_B @ np.asarray(rvec, float)
        R = np.linalg.norm(rb); nvec = rb / R
        out = 0
        for a in range(3):
            for b in range(3):
                coef = (1.0 if a == b else 0.0) - 3 * nvec[a] * nvec[b]
                if coef != 0:
                    out = out + coef * sp.kron(sp.csr_matrix(MA[a]), sp.csr_matrix(MB[b]))
        return K_DD / R ** 3 * out

    def _isS(self, d, gate):
        v = np.zeros(d); off = 2 if gate else 0
        v[off:off + self.nS] = 1; return v

    def _build_pair_static(self):
        """Static H of A (x) B: Rydberg energies, A-B dipole-dipole, A-B S-S vdW."""
        cfg = self.cfg; IG = sp.identity(self.dG, format="csr")
        hG = np.zeros(self.dG); hG[2:] = self.E_ryd
        H = sp.kron(sp.diags(hG), IG) + sp.kron(IG, sp.diags(hG))
        dA = [self._gate_op(M) for M in self.d_ryd]
        H = H + self._dd(dA, dA, (cfg.d_pair, 0, 0))
        sG = self._isS(self.dG, True)
        H = H + self.C6 / cfg.d_pair ** 6 * sp.diags(np.kron(sG, sG))
        L = np.zeros((self.dG, self.dG), complex); L[2 + self.ir, 1] = 1.0   # |r><1|
        self.Lpair = sp.kron(sp.csr_matrix(L), IG) + sp.kron(IG, sp.csr_matrix(L))
        return H.tocsr()

    def hamiltonian_static(self, rC):
        """Static H on A (x) B (x) C for contaminant position rC (lab frame, um; pair centre at origin).

        rC=None: contaminant decoupled (its own energies still present).
        """
        cfg = self.cfg; IC = sp.identity(self.dC, format="csr"); IG = sp.identity(self.dG, format="csr")
        H = sp.kron(self._static_pair, IC) + sp.kron(sp.identity(self.dG ** 2), sp.diags(self.E_ryd))
        if rC is not None:
            rA = np.array([-cfg.d_pair / 2, 0, 0]); rB = -rA
            dG = [self._gate_op(M) for M in self.d_ryd]
            dC = self.d_ryd
            sG, sC = self._isS(self.dG, True), self._isS(self.dC, False)
            for which, r0 in (("A", rA), ("B", rB)):
                rv = np.asarray(rC, float) - r0
                VAC = self._dd(dG, dC, rv)                      # on (gate atom) x C
                vdw = self.C6 / np.linalg.norm(rv) ** 6 * sp.diags(np.kron(sG, sC))
                op = (VAC + vdw).tocsr()
                if which == "A":
                    # A x C with B identity in the middle: permute via explicit construction
                    H = H + _embed_AC(op, self.dG, self.dG, self.dC)
                else:
                    H = H + sp.kron(IG, op)
        L = sp.kron(self.Lpair, IC)
        return H.tocsr(), L.tocsr()

    # ---- states ------------------------------------------------------------------------------
    def basis_index(self, a, b, c):
        return (a * self.dG + b) * self.dC + c

    def comp_indices(self, c):
        return [self.basis_index(a, b, c) for a in (0, 1) for b in (0, 1)]

    def P_index_C(self, lev: Level):
        return self.ryd.index(lev)


def _embed_AC(op, dA, dB, dC):
    """Embed an operator on A (x) C into A (x) B (x) C."""
    op = op.tocoo()
    a1, c1 = np.divmod(op.row, dC); a2, c2 = np.divmod(op.col, dC)
    rows, cols, vals = [], [], []
    for b in range(dB):
        rows.append((a1 * dB + b) * dC + c1); cols.append((a2 * dB + b) * dC + c2); vals.append(op.data)
    N = dA * dB * dC
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))


def evolve(model: ThreeAtom, psi0, rC, t_on=0.0):
    """Evolve columns of psi0 through the pulse. Contaminant coupling active for t >= t_on."""
    cfg = model.cfg
    T, amp, phi = pulse_phase(cfg)
    H_off, L = model.hamiltonian_static(None)
    H_on = model.hamiltonian_static(rC)[0] if rC is not None else H_off
    dt = T / cfg.nsteps; psi = psi0.astype(complex)
    for k in range(cfg.nsteps):
        tm = (k + 0.5) * dt
        Hs = H_on if tm >= t_on else H_off
        Hl = 0.5 * amp(tm) * (np.exp(1j * phi(tm)) * L + np.exp(-1j * phi(tm)) * L.getH())
        psi = expm_multiply(-2j * np.pi * dt * (Hs + Hl), psi)
    return psi


COMP = [(0, 0), (0, 1), (1, 0), (1, 1)]


def run_gate(model: ThreeAtom, rC, c0_list, t_on=0.0):
    """Return K[c0] = array (dC, 4, 4) of Kraus blocks K_e[j, k] = <j, e| U |k, c0>."""
    N = model.dG ** 2 * model.dC
    cols = []
    for c0 in c0_list:
        for (a, b) in COMP:
            v = np.zeros(N, complex); v[model.basis_index(a, b, c0)] = 1; cols.append(v)
    psi = evolve(model, np.array(cols).T, rC, t_on)
    out = {}
    for i, c0 in enumerate(c0_list):
        K = np.zeros((model.dC, 4, 4), complex)
        for k in range(4):
            col = psi[:, 4 * i + k]
            for e in range(model.dC):
                for j, (a, b) in enumerate(COMP):
                    K[e, j, k] = col[model.basis_index(a, b, e)]
        out[c0] = K
    return out


def reference_unitary(model: ThreeAtom, c0):
    """Computational block of the gate without contaminant coupling (diagonal phases kept)."""
    K = run_gate(model, None, [c0])[c0]
    U0 = K[c0]
    return U0


def cz_fidelity(U0):
    """Max over a symmetric single-qubit Z phase theta of |Tr(U_CZ(theta)^dag U0)|^2 / 16."""
    th = np.linspace(-np.pi, np.pi, 20001)
    d = np.diag(U0)
    tr = np.conj(1) * d[0] + np.exp(-1j * th) * (d[1] + d[2]) - np.exp(-2j * th) * d[3]
    k = np.argmax(np.abs(tr) ** 2)
    return np.abs(tr[k]) ** 2 / 16, th[k]


def error_components(K, U_ref):
    """Entanglement infidelity, leakage and Pauli-type part relative to the diagonal unitary U_ref."""
    Uh = np.diag(np.exp(1j * np.angle(np.diag(U_ref))))
    Fe = sum(abs(np.trace(Uh.conj().T @ K[e])) ** 2 for e in range(K.shape[0])) / 16
    leak = 1 - sum(np.linalg.norm(K[e]) ** 2 for e in range(K.shape[0])) / 4
    return 1 - Fe, leak, 1 - Fe - leak
