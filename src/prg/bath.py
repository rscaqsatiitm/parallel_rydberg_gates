"""Rate equations for Rydberg populations under a band-limited synthetic bath (E13, D011 item 6, DV3).

Levels (n, l, j), n in [nmin, nmax], l <= lmax. A[i, k]: spontaneous rate i -> k (1/s) for E_i > E_k (ARC, T = 0).
nbar(nu) = Planck(nu, T_eff) inside [f_lo, f_hi], Planck(nu, 300 K) outside. Stimulated: down A (1 + nbar), up
A g_u / g_l nbar. Sink: ARC 300 K total out-rate minus in-window 300 K rates (not driven by the synthetic band).
"""
from __future__ import annotations
import numpy as np, os
from scipy.linalg import expm
from .atomic import get_atom

H, KB = 6.62607015e-34, 1.380649e-23


def nbar(nu_Hz, T):
    x = H * nu_Hz / (KB * T)
    return 1.0 / np.expm1(x)


class Bath:
    def __init__(self, species="Cs133", nmin=45, nmax=75, lmax=3, cache=None):
        a = get_atom(species)
        self.levels = [(n, l, j) for n in range(nmin, nmax + 1) for l in range(0, lmax + 1)
                       for j in ([0.5] if l == 0 else [l - 0.5, l + 0.5]) if n > l]
        N = len(self.levels); self.idx = {lv: i for i, lv in enumerate(self.levels)}
        if cache and os.path.exists(cache):
            z = np.load(cache); self.E, self.A, self.sink = z["E"], z["A"], z["sink"]; return
        self.E = np.array([a.getEnergy(*lv) for lv in self.levels]) * 1.602176634e-19 / H   # Hz
        self.A = np.zeros((N, N))
        for i, (n1, l1, j1) in enumerate(self.levels):
            for k, (n2, l2, j2) in enumerate(self.levels):
                if abs(l1 - l2) == 1 and abs(j1 - j2) <= 1 and self.E[i] > self.E[k]:
                    self.A[i, k] = a.getTransitionRate(n1, l1, j1, n2, l2, j2, temperature=0)
        tot300 = np.array([1 / a.getStateLifetime(*lv, temperature=300.0, includeLevelsUpTo=lv[0] + 40) for lv in self.levels])
        self.sink = tot300 - self.rates(300.0, (0, 0)).sum(1)
        if cache: np.savez(cache, E=self.E, A=self.A, sink=self.sink)

    def g(self):
        return np.array([2 * lv[2] + 1 for lv in self.levels])

    def rates(self, T_eff, band):
        """W[i, k]: rate i -> k (1/s), within the window."""
        nu = np.abs(self.E[:, None] - self.E[None, :])
        inband = (nu >= band[0]) & (nu <= band[1])
        with np.errstate(divide="ignore", invalid="ignore"):
            nb = np.where(inband, nbar(nu, T_eff), nbar(nu, 300.0))
        nb = np.nan_to_num(nb)
        g = self.g(); W = self.A * (1 + nb)                      # downward i -> k (A nonzero only for E_i > E_k)
        W = W + (self.A.T * (g[None, :] / g[:, None])) * nb     # upward: from lower i to upper k: A[k, i] g_k / g_i nbar
        return W

    def generator(self, T_eff, band):
        W = self.rates(T_eff, band); N = len(self.levels)
        M = W.T - np.diag(W.sum(1) + self.sink)                  # dP/dt = M P (sink leaves the system)
        return M

    def evolve(self, P0, T_eff, band, times_s):
        M = self.generator(T_eff, band)
        w, V = np.linalg.eig(M); Vi = np.linalg.inv(V); c = Vi @ P0
        return np.array([np.real(V @ (np.exp(w * t) * c)) for t in times_s])
