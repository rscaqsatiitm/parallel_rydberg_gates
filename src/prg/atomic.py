"""Single-atom Rydberg data for the contaminant model (D004).

Conventions
-----------
Spherical tensor components of the dipole operator d_q (q = -1, 0, +1) with the Wigner-Eckart
theorem in the Condon-Shortley convention:
    <j m | d_q | j' m'> = (-1)^(j-m) (j 1 j'; -m q m') <j || d || j'>,
    <l s j || d || l' s j'> = (-1)^(l+s+j'+1) sqrt((2j+1)(2j'+1)) {l j s; j' l' 1} <l || d || l'>,
    <l || d || l'> = (-1)^l sqrt((2l+1)(2l'+1)) (l 1 l'; 0 0 0) R(n l j; n' l' j'),
with R the radial matrix element from ARC (e a0). Energies from ARC (eV), Zeeman shifts linear in B
with g_J from the Lande formula (g_s = 2.0023). Hyperfine structure of Rydberg states is neglected.
"""
from __future__ import annotations
import warnings
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
from sympy.physics.wigner import wigner_3j, wigner_6j

warnings.filterwarnings("ignore")

MU_B_MHZ_PER_G = 1.39962449361   # Bohr magneton / h, MHz/G (CODATA 2018)
EV_TO_MHZ = 2.417989242e8        # 1 eV / h in MHz (CODATA 2018)
_E, _A0, _EPS0, _H = 1.602176634e-19, 5.29177210903e-11, 8.8541878128e-12, 6.62607015e-34
K_DD = _E**2 * _A0**2 / (4 * np.pi * _EPS0 * _H) * 1e18 * 1e-6   # MHz um^3 per (e a0)^2 (= 9.755e-4)


def get_atom(species: str):
    from arc import Rubidium87, Caesium
    return {"Rb87": Rubidium87, "Cs133": Caesium}[species]()


def lande_gj(l, j, s=0.5, gs=2.0023193):
    return 1 + (gs - 1) * (j * (j + 1) + s * (s + 1) - l * (l + 1)) / (2 * j * (j + 1)) if j > 0 else 0.0


@dataclass(frozen=True)
class Level:
    n: int
    l: int
    j: float
    m: float


def manifold(n, l):
    """All |n l j m> states with j = l +- 1/2."""
    out = []
    for j in ([0.5] if l == 0 else [l - 0.5, l + 0.5]):
        for m in np.arange(-j, j + 1):
            out.append(Level(n, l, j, float(m)))
    return out


@lru_cache(maxsize=None)
def _radial(species, n1, l1, j1, n2, l2, j2):
    return float(get_atom(species).getRadialMatrixElement(n1, l1, j1, n2, l2, j2))


def dipole_q(species, a: Level, b: Level, q: int) -> float:
    """<a| d_q |b> in e a0 (real in this convention)."""
    if abs(a.l - b.l) != 1 or a.m != b.m + q:
        return 0.0
    R = _radial(species, a.n, a.l, a.j, b.n, b.l, b.j)
    red_l = (-1) ** a.l * np.sqrt((2 * a.l + 1) * (2 * b.l + 1)) * float(wigner_3j(a.l, 1, b.l, 0, 0, 0)) * R
    s = 0.5
    red_j = ((-1) ** int(round(a.l + s + b.j + 1)) * np.sqrt((2 * a.j + 1) * (2 * b.j + 1))
             * float(wigner_6j(a.l, a.j, s, b.j, b.l, 1)) * red_l)
    return (-1) ** int(round(a.j - a.m)) * float(wigner_3j(a.j, 1, b.j, -a.m, q, b.m)) * red_j


def dipole_cartesian(species, levels):
    """Cartesian dipole matrices (dx, dy, dz) on the given level list, in e a0."""
    N = len(levels)
    dq = {q: np.zeros((N, N)) for q in (-1, 0, 1)}
    for i, a in enumerate(levels):
        for k, b in enumerate(levels):
            for q in (-1, 0, 1):
                dq[q][i, k] = dipole_q(species, a, b, q)
    # d_{+1} = -(dx + i dy)/sqrt2, d_{-1} = (dx - i dy)/sqrt2
    dx = (dq[-1] - dq[1]) / np.sqrt(2)
    dy = 1j * (dq[-1] + dq[1]) / np.sqrt(2)
    dz = dq[0].astype(complex)
    for M in (dx, dy, dz):
        assert np.allclose(M, M.conj().T, atol=1e-9 * max(1, np.abs(M).max())), "dipole not Hermitian"
    return dx.astype(complex), dy, dz


def level_energy_MHz(species, lev: Level, B_G: float) -> float:
    E = get_atom(species).getEnergy(lev.n, lev.l, lev.j) * EV_TO_MHZ
    return E + lande_gj(lev.l, lev.j) * MU_B_MHZ_PER_G * B_G * lev.m


def bbr_rates(species, n, T, nprime=None):
    """BBR-stimulated rates (1/s) from nS1/2 to n'P_J, J = 1/2, 3/2 (ARC getTransitionRate minus T=0 part)."""
    atom = get_atom(species)
    out = {}
    for n2 in (nprime if nprime is not None else (n - 1, n)):
        for j2 in (0.5, 1.5):
            rT = atom.getTransitionRate(n, 0, 0.5, n2, 1, j2, temperature=T)
            lower = atom.getEnergy(n2, 1, j2) < atom.getEnergy(n, 0, 0.5)
            r0 = atom.getTransitionRate(n, 0, 0.5, n2, 1, j2, temperature=0) if lower else 0.0
            out[(n2, j2)] = rT - r0
    return out


def contaminant_weights(species, n, mj_r, nprime, T=300.0):
    """Probabilities of n'P_J mJ' given a BBR transition from |nS1/2 mj_r> into the n' manifold.

    Isotropic radiation: within (n', J) the m' distribution is proportional to sum_q |<P m'|d_q|S m>|^2.
    Between J the ARC rates set the weights.
    """
    rates = bbr_rates(species, n, T, nprime=(nprime,))
    S = Level(n, 0, 0.5, mj_r)
    w = {}
    for J in (0.5, 1.5):
        levs = [lv for lv in manifold(nprime, 1) if lv.j == J]
        cg = np.array([sum(dipole_q(species, lv, S, q) ** 2 for q in (-1, 0, 1)) for lv in levs])
        cg = cg / cg.sum()
        for lv, c in zip(levs, cg):
            w[lv] = rates[(nprime, J)] * c
    tot = sum(w.values())
    return {k: v / tot for k, v in w.items()}, rates
