"""Probe atom + one contaminant (Addendum 2, item 2; D011). Units MHz (H/h), us, um.

Probe basis: [g, nS1/2 m=-1/2, nS1/2 m=+1/2, n'P_J m (6)]; contaminant: [nS (2), n'P (6)].
Rotating frame: probe |g> and |r> = nS1/2 m=+1/2 at 0; other S levels at their Zeeman offset from |r>;
P levels relative to n'P3/2 at zero field (a constant per P excitation is dropped; exact because the
number of P excitations is conserved by the first-order S-P exchange and the laser couples only g-r).
Quantization axis z = B; probe at origin, contaminant at R (sin th, 0, cos th).
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm
from .atomic import Level, manifold, dipole_cartesian, level_energy_MHz, K_DD


class ProbePair:
    def __init__(self, species="Cs133", n=60, nprime=59, B_G=5.0):
        self.sp, self.n, self.np_ = species, n, nprime
        S, P = manifold(n, 0), manifold(nprime, 1)
        self.ryd = S + P
        self.ir = [i for i, lv in enumerate(self.ryd) if lv.l == 0 and lv.m == 0.5][0]
        d = dipole_cartesian(species, self.ryd)
        Er = level_energy_MHz(species, Level(n, 0, 0.5, 0.5), B_G)
        Ep = level_energy_MHz(species, Level(nprime, 1, 1.5, 0.0), 0.0)
        E = np.array([level_energy_MHz(species, lv, B_G) - (Er if lv.l == 0 else Ep) for lv in self.ryd])
        nr = len(self.ryd); self.dPr, self.dC = 1 + nr, nr
        self.dP = [np.zeros((self.dPr, self.dPr), complex) for _ in range(3)]
        for k in range(3): self.dP[k][1:, 1:] = d[k]
        self.dCop = d
        self.hP = np.diag(np.concatenate([[0.0], E])); self.hC = np.diag(E)
        self.H0 = np.kron(self.hP, np.eye(self.dC)) + np.kron(np.eye(self.dPr), self.hC)
        L = np.zeros((self.dPr, self.dPr), complex); L[1 + self.ir, 0] = 1.0
        self.Ldrive = np.kron(L + L.conj().T, np.eye(self.dC)) / 2      # Omega/2 (|r><g| + h.c.) per unit Omega

    def Vdd(self, R, th):
        if R is None: return np.zeros_like(self.H0)
        nv = np.array([np.sin(th), 0.0, np.cos(th)]); out = 0
        for a in range(3):
            for b in range(3):
                c = (1.0 if a == b else 0.0) - 3 * nv[a] * nv[b]
                if c: out = out + c * np.kron(self.dP[a], self.dCop[b])
        return K_DD / R ** 3 * out

    def state(self, probe, c_level):
        """probe: vector on probe space; c_level: Level of the contaminant."""
        c = np.zeros(self.dC, complex); c[self.ryd.index(c_level)] = 1
        return np.kron(probe, c)

    def probe_rho(self, psi):
        M = psi.reshape(self.dPr, self.dC); return M @ M.conj().T

    # ---- sequences ------------------------------------------------------------------------------
    def ramsey(self, R, th, c_level, t):
        """Instantaneous pi/2 on g-r, free evolution t, returns rho_gr (coherence)."""
        p = np.zeros(self.dPr, complex); p[0] = p[1 + self.ir] = 1 / np.sqrt(2)
        psi = expm(-2j * np.pi * (self.H0 + self.Vdd(R, th)) * t) @ self.state(p, c_level)
        return self.probe_rho(psi)[0, 1 + self.ir]

    def pulse(self, R, th, c_level, Omega_MHz, area):
        """Square resonant pulse of area 'area' (rad); returns probe population left in g."""
        p = np.zeros(self.dPr, complex); p[0] = 1
        t = area / (2 * np.pi * Omega_MHz)
        psi = expm(-2j * np.pi * (self.H0 + self.Vdd(R, th) + Omega_MHz * self.Ldrive) * t) @ self.state(p, c_level)
        return float(np.real(self.probe_rho(psi)[0, 0]))
