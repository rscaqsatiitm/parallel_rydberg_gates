# E12 pre-registered controls.
import sys, numpy as np
sys.path.insert(0, "src")
import prg.probe as pb
from prg.atomic import Level, dipole_q, K_DD
m = pb.ProbePair("Cs133", 60, 59, 5.0); c = Level(59, 1, 1.5, 1.5)
C3 = K_DD * dipole_q("Cs133", c, Level(60, 0, 0.5, 0.5), 1) ** 2
ts = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]; R = 10.0
base = [abs(m.ramsey(None, 0, c, t)) for t in ts]
dev = max(abs(abs(m.ramsey(R, 0.0, c, t)) / b - abs(np.cos(2 * np.pi * C3 * t / R ** 3))) for t, b in zip(ts, base))
print(f"C3 = {C3:.2f} MHz um^3; (1) planted max dev {dev:.2e} {'PASS' if dev < 1e-8 else 'FAIL'}")
nul = max([1 - abs(m.ramsey(1000.0, th, c, t)) / b for th in (0, 0.5, 1.2) for t, b in zip(ts, base)] +
          [abs(m.pulse(1000.0, th, c, 1.0, np.pi) - m.pulse(None, th, c, 1.0, np.pi)) for th in (0, 1.2)])
print(f"(2) null max {nul:.2e} {'PASS' if nul < 1e-6 else 'FAIL'}")
K0 = pb.K_DD; pb.K_DD = 2 * K0
dev2 = max(abs(abs(m.ramsey(R, 0.0, c, t)) / b - abs(np.cos(2 * np.pi * C3 * t / R ** 3))) for t, b in zip(ts, base))
pb.K_DD = K0
print(f"(3) corrupted (K doubled) dev {dev2:.2e} {'caught: PASS' if dev2 > 1e-3 else 'NOT caught: FAIL'}")
