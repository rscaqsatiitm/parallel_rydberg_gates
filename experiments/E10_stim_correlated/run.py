"""E10 production run (grid and stopping rule as pre-registered in README)."""
import sys, json, time, os, numpy as np
sys.path.insert(0, "experiments/E10_stim_correlated")
from sim import run, wilson, per_round
OUT = "experiments/E10_stim_correlated/results.json"
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
def point(key, d, p, m, mode, **kw):
    if key in res: return
    t0 = time.time(); n = 0; k = 0; seed = 1000 * (len(res) + 1)
    while (k < 100 or n < 1_000_000) and n < 20_000_000:
        step = 1_000_000 if n < 1_000_000 else min(20_000_000 - n, max(1_000_000, int(n * (100 - k) / max(k, 1)) if k else 4_000_000))
        k += run(d, p, m, mode, step, seed0=seed); n += step; seed += 17
    lo, ph, hi = wilson(k, n)
    res[key] = dict(d=d, p=p, m=m, mode=mode, kw={a: str(b) for a, b in kw.items()}, shots=n, fails=k,
                    P=[lo, ph, hi], pL_round=[per_round(lo, d), per_round(ph, d), per_round(hi, d)], wall_s=time.time() - t0)
    json.dump(res, open(OUT, "w"), indent=1)
    print(key, n, k, "pL/round %.3e [%.3e, %.3e]" % tuple(res[key]["pL_round"][i] for i in (1, 0, 2)), "%.0fs" % res[key]["wall_s"], flush=True)
for p in (1e-3, 2e-3):
    for d in (3, 5, 7):
        point(f"base_d{d}_p{p:g}", d, p, 0, "base")
        for m in (1, 3, 10):
            for mode in ("corr", "indep"):
                point(f"{mode}_d{d}_p{p:g}_m{m}", d, p, m, mode)
for d in (5, 7):
    point(f"V1_d{d}", d, 1e-3, 10, "corr", coupling="random")
    point(f"V2corr_d{d}", d, 1e-3, 10, "corr", bdir="x"); point(f"V2indep_d{d}", d, 1e-3, 10, "indep", bdir="x")
    point(f"V3_d{d}", d, 1e-3, 10, "corr", cluster_min=0.2)
    point(f"D1_d{d}", d, 1e-3, 10, "corr", decode_with="indep")
print("done")
