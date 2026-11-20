import sys, numpy as np
sys.path.insert(0, "src")
from prg.model import Config, ThreeAtom, contaminant_increment
from prg.atomic import Level
m = ThreeAtom(Config()); cP = m.ryd.index(Level(52, 1, 1.5, 1.5))
for R in (200.0, 8.0):
    inc, base = contaminant_increment(m, (R, 0, 0), [cP])
    print(f"[3/2] R={R}: d_err, d_leak, d_pauli =", np.round(inc[cP], 9))
m2 = ThreeAtom(Config(nsteps=1200)); inc2, _ = contaminant_increment(m2, (8.0, 0, 0), [cP])
print("[2] nsteps 1200, R=8:", np.round(inc2[cP], 9))
