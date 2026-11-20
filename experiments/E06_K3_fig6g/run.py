"""E06 driver (see README). Stage A: trajectories (no E02 needed). Stage B: predictions (needs E02 map)."""
import sys, json, itertools, time, numpy as np
from multiprocessing import Pool
sys.path.insert(0, "src")
from prg.motion import Landscape, lattice_sites, atom_positions, initial_thermal, trajectories
D = "experiments/E06_K3_fig6g/"
PITCHES = {"rows8.571": (12.0, 8.571), "rows12.0": (8.571, 12.0)}   # (ax, ay): pitch along x, along y
GAPS = [50.0, 100.0, 200.0, 400.0]
TIMES = sorted({g * j for g in GAPS for j in range(1, 13) if g * j <= 1200})
NTRAJ, D_PAIR, T_UK = 100, 2.0, 10.0      # per source atom (two source atoms -> 200)

def stage_a(args):
    Ug, w0, pax, pkey, sparse = args
    ax, ay = PITCHES[pkey]; s = 2.0 if sparse else 1.0
    sites = lattice_sites(15, 15, ax * s, ay * s)                 # bulk patch, source at centre
    atoms = atom_positions(sites, D_PAIR, pax)
    land = Landscape(atoms, Ug, w0)
    rng = np.random.default_rng(12345)
    centre = np.argmin(np.linalg.norm(sites, axis=1)); nS = len(sites)
    out = []
    for idx in (centre, centre + nS):                             # the two atoms of the centre site
        p, v = initial_thermal(NTRAJ, Ug, w0, T_UK, rng)
        r0 = p + np.array([atoms[idx, 0], atoms[idx, 1], 0.0])
        tr = trajectories(land, r0, v, TIMES, dt=0.1)
        out.append(tr - np.array([sites[centre, 0], sites[centre, 1], 0.0]))   # relative to source site centre
    return args, np.concatenate(out, axis=1)                       # (len(TIMES), 2*NTRAJ, 3)

if __name__ == "__main__" and sys.argv[1] == "A":
    jobs = list(itertools.product((0.5, 1.0, 2.0), (0.8, 1.0, 1.2), ("x", "y"), PITCHES, (False, True)))
    t0 = time.time(); res = {}
    with Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 1) as p:
        for a, tr in p.imap_unordered(stage_a, jobs):
            res[str(a)] = tr
    np.savez_compressed(D + "trajectories.npz", times=np.array(TIMES), **res)
    print("stage A done", len(jobs), time.time() - t0)


# ------------------------------- Stage B: predictions ---------------------------------------------
def load_map():
    e02 = json.load(open("experiments/E02_error_map/results.json"))
    pc = {int(k): v for k, v in e02["p_c"].items()}; pct = sum(pc.values())
    RS = sorted({a[2] for a, _ in e02["full"]}); ALS = sorted({a[3] for a, _ in e02["full"]})
    M = {bd: np.zeros((len(RS), len(ALS), 3)) for bd in "xyz"}
    for (npr, bd, R, al), v in e02["full"]:
        M[bd][RS.index(R), ALS.index(al)] += np.array(v) * pc[npr] / pct
    return np.array(RS, float), np.array(ALS, float), M, pct

def E_interp(Rg, Ag, Mbd, comp, rel):
    """E at relative positions rel (..., 3) in the pair frame. comp: 0 = error incl. leakage, 2 = Pauli only."""
    R = np.linalg.norm(rel, axis=-1)
    al = np.degrees(np.arctan2(np.abs(rel[..., 1]), np.abs(rel[..., 0])))
    lR = np.log(np.clip(R, Rg[0], Rg[-1])); lg = np.log(Rg)
    i = np.clip(np.searchsorted(lg, lR) - 1, 0, len(Rg) - 2); fr = (lR - lg[i]) / (lg[i + 1] - lg[i])
    j = np.clip(np.searchsorted(Ag, al) - 1, 0, len(Ag) - 2); fa = (al - Ag[j]) / (Ag[j + 1] - Ag[j])
    Z = Mbd[:, :, comp]
    v = (Z[i, j] * (1 - fr) * (1 - fa) + Z[i + 1, j] * fr * (1 - fa) + Z[i, j + 1] * (1 - fr) * fa + Z[i + 1, j + 1] * fr * fa)
    tail = np.where(R > Rg[-1], (Rg[-1] / np.maximum(R, 1e-9)) ** 6, 1.0)
    return np.clip(v, 0, None) * tail

_SURV = {}
def survival(t):
    if t in _SURV:
        return _SURV[t]
    e05 = json.load(open("experiments/E05_rates_vs_T/results.json"))["300.0"]["tau_P_us"]
    # J weights within each n' from E02 contaminant weights (52: J=1/2 0.337, J=3/2 0.663; recomputed below)
    from prg.atomic import contaminant_weights
    s = 0.0
    for npr in (52, 53):
        w, _ = contaminant_weights("Rb87", 53, 0.5, npr)
        for J in (0.5, 1.5):
            wJ = sum(v for k, v in w.items() if k.j == J)
            s = s + 0.5 * wJ * np.exp(-t / e05[f"{npr}P{J}"])
    _SURV[t] = s
    return s

def predict(trajs, times, Rg, Ag, M, pct, pkey, pax, sparse, bd_lab, comp, static=False):
    ax_, ay_ = PITCHES[pkey]; s = 2.0 if sparse else 1.0
    sites = lattice_sites(15, 15, ax_ * s, ay_ * s)
    tgt = np.argmin(np.linalg.norm(sites, axis=1))
    srcs = np.delete(sites, tgt, axis=0)
    bmap = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}[pax]
    Mbd = M[bmap[bd_lab]]
    eps = {}
    for g in GAPS:
        tot = 0.0
        for jj in range(1, 13):
            tj = g * jj
            if tj > 1200: break
            k = times.index(tj)
            if static:   # decay-only variant: contaminant stays on its tweezer (atom offsets +-d/2 along the pair axis)
                off = np.array([D_PAIR / 2, 0, 0]) if pax == "x" else np.array([0, D_PAIR / 2, 0])
                dr = np.concatenate([np.tile(-off, (NTRAJ, 1)), np.tile(off, (NTRAJ, 1))])
            else:
                dr = trajs[k]
            pos = srcs[:, None, :2] + dr[None, :, :2]                     # (nsrc, ntraj, 2)
            rel = np.concatenate([pos, np.broadcast_to(dr[None, :, 2:3], pos.shape[:2] + (1,))], axis=-1)
            if pax == "y":
                rel = np.stack([rel[..., 1], -rel[..., 0], rel[..., 2]], axis=-1)
            # each source site has two atoms; trajectories array holds both atoms' trajectories (NTRAJ each)
            Em = E_interp(Rg, Ag, Mbd, comp, rel).mean(axis=1)            # mean over both atoms' trajectories
            tot += survival(tj) * 2 * pct * Em.sum()                      # 2 atoms per source site
        eps[g] = tot
    return eps

if __name__ == "__main__" and sys.argv[1] == "B":
    Rg, Ag, M, pct = load_map()
    Z = np.load(D + "trajectories.npz"); times = [float(x) for x in Z["times"]]
    rows = []
    for Ug, w0, pax, pkey, sparse in itertools.product((0.5, 1.0, 2.0), (0.8, 1.0, 1.2), ("x", "y"), PITCHES, (False, True)):
        tr = Z[str((Ug, w0, pax, pkey, sparse))]
        for bd in "xyz":
            for comp in (0, 2):
                for static in (False, True):
                    e = predict(tr, times, Rg, Ag, M, pct, pkey, pax, sparse, bd, comp, static)
                    rows.append(dict(Ug=Ug, w0=w0, pax=pax, pkey=pkey, sparse=sparse, bd=bd,
                                     leak="counted" if comp == 0 else "not", static=static, eps=e))
    json.dump(rows, open(D + "predictions.json", "w"))
    print(len(rows), "predictions written")
