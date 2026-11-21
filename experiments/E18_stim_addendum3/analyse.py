"""E18 analysis: X with conservative 95 % bounds; verdicts V1a, V1b, V2 as pre-registered (amendment 1)."""
import sys, json, numpy as np
sys.path.insert(0, "experiments/E18_stim_addendum3")
from sim_util import wilson, per_round
R = json.load(open("experiments/E18_stim_addendum3/results.json")); E10 = json.load(open("experiments/E10_stim_correlated/results.json"))
def iv(k, n, d): return [per_round(x, d) for x in wilson(k, n)]
def e10(key): v = E10[key]; return iv(v["fails"], v["shots"], v["d"])
def X(c, i, b):
    num_lo, num_c, num_hi = c[0] - b[2], c[1] - b[1], c[2] - b[0]; den_lo, den_c, den_hi = i[0] - b[2], i[1] - b[1], i[2] - b[0]
    return [num_lo / den_hi if den_hi > 0 else np.nan, num_c / den_c, num_hi / den_lo if den_lo > 0 else np.inf]
f = lambda x: f"{x[1]:.2f} [{x[0]:.2f}, {x[2]:.2f}]"; g = lambda x: f"{x[1]:.2e} [{x[0]:.2e}, {x[2]:.2e}]"
out = {}
print("== Item 1b: E10 model re-decoded (m = 1). corr decoders own / marg / cm; base and indep from E10")
for p in (1e-3, 2e-3):
    for d in (3, 5, 7):
        k = f"A_corr_d{d}_p{p:g}"
        if k not in R: continue
        r = R[k]; b = e10(f"base_d{d}_p{p:g}"); i = e10(f"indep_d{d}_p{p:g}_m1")
        cs = [iv(x, r["shots"], d) for x in r["fails"]]; xs = [X(c, i, b) for c in cs]
        best = int(np.argmin([c[1] for c in cs])); out[k] = dict(X=xs, best=r["decoders"][best], X_E10=None)
        print(f"p {p:g} d {d}: shots {r['shots']:.1e} fails {r['fails']} | corr own {g(cs[0])} marg {g(cs[1])} cm {g(cs[2])} | indep {g(i)} base {g(b)}")
        print(f"      X own {f(xs[0])}  X marg {f(xs[1])}  X cm {f(xs[2])}  best = {r['decoders'][best]}")
print("\n== Item 2: d = 9, 11 (m = 1, p = 1e-3); corr decoders own / marg")
for d in (7, 9, 11):
    if d == 7:
        b = e10("base_d7_p0.001"); i = e10("indep_d7_p0.001_m1"); c = iv(R["A_corr_d7_p0.001"]["fails"][1], R["A_corr_d7_p0.001"]["shots"], 7) if "A_corr_d7_p0.001" in R else None
    else:
        if f"B_base_d{d}" not in R: continue
        rb, ri, rc = R[f"B_base_d{d}"], R[f"B_indep_d{d}"], R[f"B_corr_d{d}"]
        b = iv(rb["fails"][0], rb["shots"], d); i = iv(ri["fails"][0], ri["shots"], d); c = iv(rc["fails"][1], rc["shots"], d)
        print(f"d {d}: base {rb['fails']}/{rb['shots']:.1e} {g(b)} | indep {ri['fails']}/{ri['shots']:.1e} {g(i)} | corr {rc['fails']}/{rc['shots']:.1e} marg {g(c)} own {g(iv(rc['fails'][0], rc['shots'], d))}")
    if c: x = X(c, i, b); out[f"X2_d{d}"] = x; print(f"   X_best(d={d}) {f(x)}")
print("\n== Item 4: pitch (10.0, 12.0) um, p = 1e-3, m = 1 (base from E10)")
for d in (3, 5, 7):
    if f"C_corr_d{d}" not in R: continue
    rc, ri = R[f"C_corr_d{d}"], R[f"C_indep_d{d}"]; b = e10(f"base_d{d}_p0.001")
    cs = [iv(x, rc["shots"], d) for x in rc["fails"]]; i = iv(ri["fails"][0], ri["shots"], d)
    print(f"d {d}: corr own {g(cs[0])} marg {g(cs[1])} cm {g(cs[2])} | indep {g(i)} | base {g(b)} | X own {f(X(cs[0], i, b))} X marg {f(X(cs[1], i, b))}")
    out[f"X4_d{d}"] = dict(own=X(cs[0], i, b), marg=X(cs[1], i, b))
print("\n== Item 1a: erasure, X(eta) (base from E10, decoders per D012/amendment)")
for d in (3, 5, 7):
    if f"D_corr_d{d}" not in R: continue
    rc, ri = R[f"D_corr_d{d}"], R[f"D_indep_d{d}"]; b = e10(f"base_d{d}_p0.001")
    for j, eta in enumerate(rc["etas"]):
        c = iv(rc["fails"][j], rc["shots"], d); i = iv(ri["fails"][j], ri["shots"], d); x = X(c, i, b)
        out[f"X1a_d{d}_eta{eta}"] = x
        print(f"d {d} eta {eta:4}: corr {rc['fails'][j]}/{rc['shots']:.1e} {g(c)} | indep {ri['fails'][j]}/{ri['shots']:.1e} {g(i)} | X {f(x)}")
print("\n== Item 3 (f_prev, non-resonant factor), corr decoders own / marg")
for k in sorted(R):
    if not k.startswith("E_corr"): continue
    d = R[k]["d"]; ki = k.replace("E_corr", "E_indep"); b = e10(f"base_d{d}_p0.001")
    c = iv(R[k]["fails"][1], R[k]["shots"], d); i = iv(R[ki]["fails"][0], R[ki]["shots"], d)
    out[k] = X(c, i, b); print(f"{k}: corr marg {g(c)} | indep {g(i)} | X {f(out[k])}")
json.dump(out, open("experiments/E18_stim_addendum3/analysis.json", "w"), indent=1, default=float)
