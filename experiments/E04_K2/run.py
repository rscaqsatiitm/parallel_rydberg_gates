"""E04: K2 evaluation (see README). Usage: python run.py <pitch_um>"""
import sys, json, time, itertools, numpy as np
from multiprocessing import Pool
sys.path.insert(0, "src")
from prg.model import Config, ThreeAtom, contaminant_increment
from prg.atomic import contaminant_weights, get_atom
PITCH = float(sys.argv[1]); NSITES = 10
E02 = json.load(open("experiments/E02_error_map/results.json"))
TONS, TW = np.array(E02["t_on"]), np.array(E02["t_on_weight"]); T = E02["T_us"]
PC = {int(k): v for k, v in E02["p_c"].items()}
# lab B labels -> pair-frame vectors, per orientation (pair axis is the model's x axis)
BFRAME = {"along": {"row": (1, 0, 0), "inplane_perp": (0, 1, 0), "normal": (0, 0, 1)},
          "perp": {"row": (0, 1, 0), "inplane_perp": (1, 0, 0), "normal": (0, 0, 1)}}
def positions(orient, j):
    a = PITCH * j
    return [(a + 1, 0, 0), (a - 1, 0, 0)] if orient == "along" else [(1, a, 0), (-1, a, 0)]
_c = {}
def model(np_, bvec):
    k = (np_, bvec)
    if k not in _c:
        m = ThreeAtom(Config(nprime=np_, bfield_dir=bvec))
        w, _ = contaminant_weights("Rb87", 53, 0.5, np_)
        c0s = [m.ryd.index(lv) for lv in w if w[lv] > 0]
        ws = np.array([w[m.ryd[c]] for c in c0s])
        base = contaminant_increment(m, (1e4, 0, 0), c0s)[1]
        _c[k] = (m, c0s, ws, base)
    return _c[k]
def task(args):
    np_, bvec, r, ton = args
    m, c0s, ws, base = model(np_, bvec)
    inc, _ = contaminant_increment(m, r, c0s, t_on=ton, baseline=base)
    per = np.array([inc[c] for c in c0s])           # (n_c0, 3)
    return args, per.tolist()
if __name__ == "__main__":
    t0 = time.time()
    bvecs = sorted({v for o in BFRAME.values() for v in o.values()})
    for np_ in (52, 53):
        for b in bvecs: model(np_, b)
    jobs = []
    for orient in BFRAME:
        for j in range(1, NSITES):
            for r in positions(orient, j):
                for np_ in (52, 53):
                    for b in bvecs:
                        for ton in [0.0] + TONS.tolist():
                            jobs.append((np_, b, r, ton))
    jobs = sorted(set(jobs))
    print(len(jobs), "jobs", flush=True)
    with Pool(4) as p:
        res = [(list(a), v) for a, v in p.imap_unordered(task, jobs, chunksize=4)]
    json.dump({"pitch": PITCH, "res": res}, open(f"experiments/E04_K2/raw_pitch{PITCH:g}.json", "w"))
    print("done", time.time() - t0, flush=True)
