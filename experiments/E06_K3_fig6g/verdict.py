import json, numpy as np
rows = json.load(open("experiments/E06_K3_fig6g/predictions.json"))
DATA = {"N50": (0.140, 0.212), "N100": (-0.067, 0.069), "N200": (-0.028, 0.040), "S50": (-0.089, 0.059)}
def band(static):
    out = {k: [] for k in DATA}; eps = {"normal": [], "sparse": []}
    for r in rows:
        if r["static"] != static: continue
        e = {float(k): v for k, v in r["eps"].items()}
        for f in (0.8, 1.0):
            if not r["sparse"]:
                out["N50"].append(100 * f * (e[50] - e[400])); out["N100"].append(100 * f * (e[100] - e[400]))
                out["N200"].append(100 * f * (e[200] - e[400])); eps["normal"].append([100 * f * e[g] for g in (50, 100, 200, 400)])
            else:
                out["S50"].append(100 * f * (e[50] - e[200])); eps["sparse"].append([100 * f * e[g] for g in (50, 100, 200, 400)])
    return out, eps
for static in (False, True):
    out, eps = band(static)
    print("MOTION" if not static else "DECAY-ONLY (static)", "variant; predicted excess D in % (band min..max) vs 2-sigma data interval")
    fire = False
    for k, (lo, hi) in DATA.items():
        a, b = min(out[k]), max(out[k]); ov = not (b < lo or a > hi); fire |= not ov
        print(f"  {k}: [{a:.4f}, {b:.4f}]   data [{lo}, {hi}]   overlap={ov}   median {np.median(out[k]):.4f}")
    for g in ("normal", "sparse"):
        E = np.array(eps[g]); print(f"  absolute eps(t) % {g}: 50/100/200/400 us min", np.round(E.min(0), 4), "max", np.round(E.max(0), 4))
    print("  K3", "FIRES" if fire else "does NOT fire", "\n")
