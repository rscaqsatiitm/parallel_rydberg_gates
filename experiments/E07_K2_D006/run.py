import sys, json, itertools, numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E06_K3_fig6g")
import run as e6
e6.GAPS = [50.0 * k for k in range(1, 13)]
Rg, Ag, M, pct = e6.load_map()
# same-layer map (E02 summary): keys "(bd, R, al)"; bd in x,z; al in 0,90
S = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]
def same_map(bd):
    RS = sorted({float(eval(k)[1]) for k in S}); A = [0.0, 90.0]
    Z = np.zeros((len(RS), 2, 3))
    for k, v in S.items():
        b, R, al = eval(k)
        if b == bd: Z[RS.index(float(R)), A.index(float(al))] = v
    return np.array(RS), np.array(A), Z
Z = np.load(e6.D + "trajectories.npz"); times = [float(x) for x in Z["times"]]
rows = []
for Ug, w0, pax, pkey in itertools.product((0.5, 1.0, 2.0), (0.8, 1.0, 1.2), ("x", "y"), e6.PITCHES):
    tr = Z[str((Ug, w0, pax, pkey, False))]
    ax_, ay_ = e6.PITCHES[pkey]; sites = e6.lattice_sites(15, 15, ax_, ay_)
    tgt = np.argmin(np.linalg.norm(sites, axis=1)); srcs = np.delete(sites, tgt, axis=0)
    off = np.array([1.0, 0]) if pax == "x" else np.array([0, 1.0])
    atoms = np.concatenate([srcs - off, srcs + off]); rel = np.concatenate([atoms, np.zeros((len(atoms), 1))], 1)
    if pax == "y": rel = np.stack([rel[:, 1], -rel[:, 0], rel[:, 2]], 1)
    for bd in "xyz":
        bmodel = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}[pax][bd]
        sR, sA, sZ = same_map("z" if bmodel == "z" else "x")
        floor = pct * e6.E_interp(sR, sA, sZ, 0, rel).sum()
        e = e6.predict(tr, times, Rg, Ag, M, pct, pkey, pax, False, bd, 0, False)
        ts = np.array(sorted(e)); tot = floor + np.array([e[t] for t in ts])
        if floor >= 1e-4: tw = np.inf
        elif tot[0] <= 1e-4: tw = float(ts[0])          # at or below the first grid point (upper bound)
        else:
            k = np.argmax(tot <= 1e-4)
            if tot[k] > 1e-4: tw = np.inf if tot[-1] > 1e-4 else float(ts[-1])
            else:
                l0, l1 = np.log(tot[k - 1] - floor), np.log(tot[k] - floor); lt = np.log(1e-4 - floor)
                tw = float(ts[k - 1] + (ts[k] - ts[k - 1]) * (l0 - lt) / (l0 - l1))
        rows.append(dict(Ug=Ug, w0=w0, pax=pax, pkey=pkey, bd=bd, floor=floor, t_wait=tw,
                         eps=dict(zip(ts.tolist(), tot.tolist()))))
json.dump(rows, open("experiments/E07_K2_D006/results.json", "w"))
tw = np.array([r["t_wait"] for r in rows]); fl = np.array([r["floor"] for r in rows])
print("floor p_c n_same: min %.2e median %.2e max %.2e" % (fl.min(), np.median(fl), fl.max()))
print("t_wait(1e-4) us: min %.1f median %.1f max %.1f ; n_inf %d of %d" % (tw[np.isfinite(tw)].min(), np.median(tw), tw[np.isfinite(tw)].max(), np.sum(~np.isfinite(tw)), len(tw)))
print("K2 (D006)", "FIRES" if np.all(tw < 92) else "does NOT fire")
