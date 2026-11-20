# Pre-registered E08 control: at 4.6 MHz, 6-point vs E02's 12-point t_on grid for E_same (B z, alpha 0, R 10 and 20 um).
import sys, json, numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E02_error_map")
import run as e2
from prg.model import contaminant_increment
r02 = json.load(open("experiments/E02_error_map/results.json")); T = r02["T_us"]
ts, pr, _ = e2.rydberg_population()
edges = np.linspace(0, T, 7); tons = 0.5 * (edges[1:] + edges[:-1])
wt = np.array([np.trapezoid(pr[(ts >= a) & (ts < b)], ts[(ts >= a) & (ts < b)]) for a, b in zip(edges[:-1], edges[1:])]); wt /= wt.sum()
pc = r02["p_c"]; pct = sum(pc.values())
S12 = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]
for R in (10, 20):
    v6 = 0.0
    for npr in (52, 53):
        m, c0s, ws, base = e2.model(npr, "z")
        for ton, w in zip(tons, wt):
            inc, _ = contaminant_increment(m, (R, 0, 0), c0s, t_on=ton, baseline=base)
            v6 += w * pc[str(npr)] / pct * (ws * np.array([inc[c][0] for c in c0s])).sum()
    v12 = S12[str(("z", R, 0))][0]
    print(f"R={R}: E_same 6-point {v6:.4e}  12-point {v12:.4e}  rel diff {abs(v6 - v12) / v12:.3f}  {'PASS' if abs(v6 - v12) / v12 < 0.10 else 'FAIL'}")
