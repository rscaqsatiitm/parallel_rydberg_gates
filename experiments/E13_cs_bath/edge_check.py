# E13 window check (pre-registered "checked in the run", added after the first run): population on the window-edge
# levels (n'' = 45-46 or 74-75), whose bath-driven lines out of the window are not modelled.
import sys, numpy as np; sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E13_cs_bath")
from prg.bath import Bath
b = Bath(cache="experiments/E13_cs_bath/levels_A.npz"); N = len(b.levels)
edge = [i for i, lv in enumerate(b.levels) if lv[0] in (45, 46, 74, 75)]
P59 = b.idx[(59, 1, 1.5)]; S60 = b.idx[(60, 0, 0.5)]
for bn, band in {"narrow": (13.6e9, 24.8e9), "broad": (1e9, 100e9)}.items():
    for T in (1e4, 1e5, 1e6):
        M = b.generator(T, band); w, V = np.linalg.eig(M)
        for start, t in ((P59, 100e-6), (S60, 0.234e-6)):
            P0 = np.zeros(N); P0[start] = 1; P = np.real(V @ (np.exp(w * t) * np.linalg.solve(V, P0)))
            print(f"{bn:6} T_eff {T:8.0f} start {b.levels[start]} t {t*1e6:g} us: edge population {P[edge].sum():.2e} of remaining {P.sum():.3f}")
