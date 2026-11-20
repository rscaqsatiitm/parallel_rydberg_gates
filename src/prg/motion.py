"""Classical motion of an anti-trapped contaminant in a tweezer array (DV2).

Units: um, us. Potential energies are given per unit mass (um^2/us^2 = m^2/s^2).
Tweezer k at in-plane position (x_k, y_k), axis along z, Gaussian beam of waist w0 at z = 0:
    U(r) = U_h * sum_k (w0/w(z))^2 exp(-2 rho_k^2 / w(z)^2),  w(z) = w0 sqrt(1 + (z/zR)^2),
U_h > 0 the repulsive hill height for the contaminant (0.164 U_g, DV2).
"""
from __future__ import annotations
import numpy as np

KB = 1.380649e-23
M_RB87 = 86.909180527 * 1.66053906660e-27      # kg
RATIO_HILL = (349.66 - 9.08) / 2071.49          # DV2: U_R/|U_g| at 852 nm


def lattice_sites(nx, ny, ax, ay):
    """Site centres of an nx x ny lattice centred at the origin (um)."""
    xs = (np.arange(nx) - (nx - 1) / 2) * ax
    ys = (np.arange(ny) - (ny - 1) / 2) * ay
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    return np.stack([X.ravel(), Y.ravel()], axis=1)


def atom_positions(sites, d_pair, pair_axis):
    """Two atoms per site separated by d_pair along pair_axis ('x' or 'y')."""
    off = np.array([d_pair / 2, 0.0]) if pair_axis == "x" else np.array([0.0, d_pair / 2])
    return np.concatenate([sites - off, sites + off])


class Landscape:
    def __init__(self, tweezers_xy, Ug_mK, w0_um, lam_um=0.852):
        self.tw = np.asarray(tweezers_xy, float)
        self.w0, self.zR = w0_um, np.pi * w0_um ** 2 / lam_um
        Ug = Ug_mK * 1e-3 * KB / M_RB87                    # m^2/s^2 = um^2/us^2
        self.Ug, self.Uh = Ug, RATIO_HILL * Ug

    def force(self, r):
        """Acceleration (um/us^2) on contaminants at positions r (N, 3)."""
        x, y, z = r[:, 0:1], r[:, 1:2], r[:, 2:3]
        dx = x - self.tw[None, :, 0]; dy = y - self.tw[None, :, 1]
        w2 = self.w0 ** 2 * (1 + (z / self.zR) ** 2)
        g = (self.w0 ** 2 / w2) * np.exp(-2 * (dx ** 2 + dy ** 2) / w2)
        U = self.Uh * g
        ax = (4 * dx / w2 * U).sum(1)
        ay = (4 * dy / w2 * U).sum(1)
        # d/dz of (w0^2/w2) exp(-2 rho^2/w2): dw2/dz = 2 w0^2 z / zR^2
        dw2 = 2 * self.w0 ** 2 * z / self.zR ** 2
        dUdz = U * (-dw2 / w2 + 2 * (dx ** 2 + dy ** 2) * dw2 / w2 ** 2)
        az = (-dUdz).sum(1)
        return np.stack([ax, ay, az], axis=1)


def initial_thermal(n, Ug_mK, w0_um, T_uK, rng, lam_um=0.852):
    """Thermal state of the ground-state harmonic trap (depth Ug, waist w0)."""
    Ug = Ug_mK * 1e-3 * KB / M_RB87
    zR = np.pi * w0_um ** 2 / lam_um
    wr2, wz2 = 4 * Ug / w0_um ** 2, 2 * Ug / zR ** 2     # (1/us)^2
    kT = T_uK * 1e-6 * KB / M_RB87
    pos = rng.normal(size=(n, 3)) * np.sqrt(kT / np.array([wr2, wr2, wz2]))
    vel = rng.normal(size=(n, 3)) * np.sqrt(kT)
    return pos, vel


def trajectories(land, r0, v0, t_out, dt=0.05):
    """Velocity-Verlet integration; returns positions at the requested times (len(t_out), N, 3)."""
    t_out = np.sort(np.asarray(t_out, float))
    r, v = r0.copy(), v0.copy(); a = land.force(r)
    out = np.empty((len(t_out),) + r.shape); k = 0; t = 0.0
    while k < len(t_out):
        while k < len(t_out) and t_out[k] <= t + 1e-12:
            out[k] = r; k += 1
        if k == len(t_out):
            break
        h = min(dt, t_out[k] - t) if t_out[k] - t > 1e-12 else dt
        v_half = v + 0.5 * h * a
        r = r + h * v_half
        a = land.force(r)
        v = v_half + 0.5 * h * a
        t += h
    return out
