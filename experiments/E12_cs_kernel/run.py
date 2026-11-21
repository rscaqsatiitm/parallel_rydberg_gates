# E12 production run (pre-registered README).
import sys, json, itertools, numpy as np
sys.path.insert(0, "src")
from prg.probe import ProbePair
from prg.atomic import Level
RS = [3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30]; THS = [0, 30, 54.74, 90]
TS = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]; OMS = [0.5, 1, 2, 5]
STATES = [(59, 1.5, 1.5), (59, 0.5, 0.5), (60, 1.5, 1.5), (60, 0.5, 0.5)]
out = []
def run(B, states, ths, rs):
    for (n2, j, mj) in states:
        m = ProbePair("Cs133", 60, n2, B); c = Level(n2, 1, j, mj)
        r0 = {t: m.ramsey(None, 0, c, t) for t in TS}
        g0 = {(om, a): m.pulse(None, 0, c, om, a) for om in OMS for a in (np.pi, 2 * np.pi)}
        for R, th in itertools.product(rs, ths):
            T = np.radians(th); rec = dict(B=B, state=f"{n2}P{j} {mj}", R=R, theta=th, ramsey={}, block={}, block2pi={})
            for t in TS:
                r = m.ramsey(R, T, c, t); rec["ramsey"][t] = [1 - abs(r) / abs(r0[t]), float(np.angle(r / r0[t]))]
            for om in OMS:
                pe0 = 1 - g0[(om, np.pi)]; pe = 1 - m.pulse(R, T, c, om, np.pi)
                rec["block"][om] = 1 - pe / pe0
                rec["block2pi"][om] = g0[(om, 2 * np.pi)] - m.pulse(R, T, c, om, 2 * np.pi)
            out.append(rec)
run(5.0, STATES, THS, RS)
run(20.0, [STATES[0]], [0, 90], RS)
json.dump(out, open("experiments/E12_cs_kernel/results.json", "w"))
# summary tables
def get(B, st, R, th): return next(o for o in out if o["B"] == B and o["state"] == st and o["R"] == R and o["theta"] == th)
for st in [f"{a}P{b} {c}" for a, b, c in STATES]:
    print(f"\n== {st}, B 5 G. Ramsey E_R at t = 0.2 / 1 / 5 us ; blockade E_B at Omega/2pi = 0.5 / 1 / 5 MHz")
    for R in RS:
        print(f"R {R:4} " + "  ".join(f"th{th:>5}: R {get(5.0, st, R, th)['ramsey'][0.2][0]:.3f} {get(5.0, st, R, th)['ramsey'][1][0]:.3f} {get(5.0, st, R, th)['ramsey'][5][0]:.3f}"
                                     f" B {get(5.0, st, R, th)['block'][0.5]:.3f} {get(5.0, st, R, th)['block'][1]:.3f} {get(5.0, st, R, th)['block'][5]:.3f}" for th in (0, 90)))
print("\nB-field sensitivity (59P3/2 3/2, Ramsey E_R at t = 1 us): R, theta, 5 G, 20 G")
for R in (5, 10, 20):
    for th in (0, 90): print(R, th, round(get(5.0, "59P1.5 1.5", R, th)["ramsey"][1][0], 4), round(get(20.0, "59P1.5 1.5", R, th)["ramsey"][1][0], 4))
