"""E10 analysis: per-round rates table, excess ratio X with conservative bounds, verdicts as pre-registered."""
import json
R = json.load(open("experiments/E10_stim_correlated/results.json")); g = lambda k: R[k]["pL_round"]
def ov(a, b): return max(a[0], b[0]) <= min(a[2], b[2])
lines = ["p      d  m  | base                 | corr                          | indep                         | X [lo, hi]"]
X = {}
for p in ("0.001", "0.002"):
    for d in (3, 5, 7):
        b = g(f"base_d{d}_p{p}")
        for m in (1, 3, 10):
            c, i = g(f"corr_d{d}_p{p}_m{m}"), g(f"indep_d{d}_p{p}_m{m}")
            x = (c[1] - b[1]) / (i[1] - b[1]); xl = (c[0] - b[2]) / (i[2] - b[0]); xh = (c[2] - b[0]) / max(i[0] - b[2], 1e-30)
            if i[0] - b[2] <= 0: xh = float("inf")
            X[(p, d, m)] = (xl, x, xh)
            lines.append(f"{p}  {d}  {m:2d} | {b[1]:.2e} [{b[0]:.2e},{b[2]:.2e}] | {c[1]:.3e} [{c[0]:.3e},{c[2]:.3e}] | "
                         f"{i[1]:.3e} [{i[0]:.3e},{i[2]:.3e}] | {x:.2f} [{xl:.2f}, {xh:.2f}]" + ("  OVERLAP" if ov(c, i) else ""))
v1 = all(not ov(g(f"corr_d{d}_p0.001_m1"), g(f"indep_d{d}_p0.001_m1")) and g(f"corr_d{d}_p0.001_m1")[0] > g(f"indep_d{d}_p0.001_m1")[2] for d in (5, 7))
v2 = any(all(g(f"corr_d{d}_p0.001_m{m}")[0] > g(f"indep_d{d}_p0.001_m{m}")[2] for d in (5, 7)) for m in (3, 10))
v3 = {p: X[(p, 3, 10)][1] < X[(p, 5, 10)][1] < X[(p, 7, 10)][1] for p in ("0.001", "0.002")}
lines += ["", f"Verdict 1 (correlation matters at m = 1, p = 1e-3, d = 5 and 7): {'YES' if v1 else 'NO'}",
          f"Verdict 2 (correlation matters at m = 3 or 10): {'YES' if v2 else 'NO'}",
          f"Verdict 3 (distance penalty: X monotonic increasing d = 3 -> 7 at m = 10): {v3} -> {'YES' if all(v3.values()) else 'NO'}",
          "", "Suppression factors Lambda = pL(d)/pL(d+2), p = 1e-3:"]
for mode in ("base", "corr", "indep"):
    for m in ((0,) if mode == "base" else (1, 3, 10)):
        k = (lambda d: f"base_d{d}_p0.001") if mode == "base" else (lambda d, m=m: f"{mode}_d{d}_p0.001_m{m}")
        lines.append(f"  {mode:5s} m={m:2d}: d3/d5 {g(k(3))[1]/g(k(5))[1]:.1f}  d5/d7 {g(k(5))[1]/g(k(7))[1]:.1f}")
lines += ["", "Variants (p = 1e-3, m = 10), pL/round:"] + [f"  {k}: {g(k)[1]:.3e} [{g(k)[0]:.3e}, {g(k)[2]:.3e}]" for k in R if k[:2] in ("V1", "V2", "V3", "D1")]
open("experiments/E10_stim_correlated/analysis_output.txt", "w").write("\n".join(lines) + "\n"); print("\n".join(lines))
