"""E18 production (README + amendment 1). Resumable: results.json."""
import sys, json, os, time, numpy as np
sys.path.insert(0, "experiments/E18_stim_addendum3")
import e18
from sim_util import wilson, per_round
OUT = "experiments/E18_stim_addendum3/results.json"
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
F_PREV = [float(x) for x in os.environ.get("F_PREV", "1e-6,2.9e-5").split(",")]; NONRES = float(os.environ.get("NONRES", "1.0"))
def save(): json.dump(res, open(OUT, "w"), indent=1)
def rec(key, d, fails, n, **meta):
    res[key] = dict(d=d, shots=n, fails=fails, **meta,
                    pL=[[per_round(x, d) for x in wilson(k, n)] for k in (fails if isinstance(fails, list) else [fails])])
    save(); print(key, n, fails, time.strftime("%H:%M:%S"), flush=True)
def std(key, d, p, mode, cap, min_fail_idx=0, **kw):
    if key in res: return
    n, k, seed = 0, None, 100 + 37 * len(res)
    while n < cap:
        step = 300_000 if n < 1_000_000 else min(cap - n, 2_000_000)
        kk = e18.run_std(d, p, 1, mode, step, seed0=seed, **kw); seed += 11
        k = kk if k is None else k + kk; n += step
        if k[min_fail_idx] >= 100 and n >= 1_000_000: break
    rec(key, d, [int(x) for x in k], n, p=p, mode=mode, kw={a: str(b) for a, b in kw.items()},
        decoders=["own", "marg", "cm"][:len(k)] if mode == "corr" else ["own"])
def era(key, d, mode, cap, etas=(0.0, 0.5, 0.8, 0.95, 1.0)):
    if key in res: return
    n, k, seed = 0, {e: 0 for e in etas}, 500 + 37 * len(res)
    while n < cap:
        step = 60_000 if n < 300_000 else 300_000
        kk = e18.run_erasure(d, 1e-3, 1, mode, step, list(etas), seed0=seed); seed += 11; n += step
        for e in etas: k[e] += kk[e]
        if min(k.values()) >= 100 or n >= 1_000_000: break
    rec(key, d, [k[e] for e in etas], n, mode=mode, etas=list(etas))
if __name__ == "__main__":
    # item 1b / re-decoding of E10 (m = 1)
    for p in (1e-3, 2e-3):
        for d in (3, 5, 7): std(f"A_corr_d{d}_p{p:g}", d, p, "corr", 10_000_000, min_fail_idx=1)
    # item 2
    for d in (9, 11):
        std(f"B_corr_d{d}", d, 1e-3, "corr", 40_000_000, min_fail_idx=1, use_cm=False)
        std(f"B_indep_d{d}", d, 1e-3, "indep", 120_000_000)
        std(f"B_base_d{d}", d, 1e-3, "base", 100_000_000 if d == 9 else 30_000_000)
    # item 4 (pitch 10.0 x 12.0)
    for d in (3, 5, 7):
        std(f"C_corr_d{d}", d, 1e-3, "corr", 10_000_000, min_fail_idx=1, pitch=(10.0, 12.0))
        std(f"C_indep_d{d}", d, 1e-3, "indep", 20_000_000, pitch=(10.0, 12.0))
    # item 1a (erasure)
    for d in (3, 5, 7):
        for mode in ("corr", "indep"): era(f"D_{mode}_d{d}", d, mode, 1_000_000)
    # item 3 (provisional unless env set): f_prev and non-resonant factor
    for d in (5, 7):
        for fp in F_PREV:
            for mode in ("corr", "indep"):
                std(f"E_{mode}_d{d}_fprev{fp:g}_nonres{NONRES:g}", d, 1e-3, mode, 10_000_000, min_fail_idx=1 if mode == "corr" else 0,
                    f_prev=fp, nonres=NONRES, use_cm=False)
            std(f"E_base_d{d}_fprev{fp:g}", d, 1e-3, "indep", 10_000_000, f_prev=fp, nonres=0.0) if False else None
    print("done", flush=True)
