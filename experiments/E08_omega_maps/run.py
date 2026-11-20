import sys, json, time, itertools, numpy as np
from multiprocessing import Pool
sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E02_error_map")
import run as e2
from prg.model import Config, ThreeAtom, contaminant_increment
from prg.atomic import contaminant_weights
OM = float(sys.argv[1]); RS = [4, 6, 8, 10, 12, 14, 17, 20, 25, 30, 40]
_c = {}
def model(np_, bd):
    if (np_, bd) not in _c:
        m = ThreeAtom(Config(nprime=np_, bfield_dir=e2.BD[bd], Omega_MHz=OM))
        w, _ = contaminant_weights("Rb87", 53, 0.5, np_)
        c0s = [m.ryd.index(lv) for lv in w if w[lv] > 0]; ws = np.array([w[m.ryd[c]] for c in c0s])
        _c[(np_, bd)] = (m, c0s, ws, contaminant_increment(m, (1e4, 0, 0), c0s)[1])
    return _c[(np_, bd)]
def task(args):
    np_, bd, R, al, ton = args; m, c0s, ws, base = model(np_, bd)
    r = (R * np.cos(np.radians(al)), R * np.sin(np.radians(al)), 0.0)
    inc, _ = contaminant_increment(m, r, c0s, t_on=ton, baseline=base)
    return args, (ws[:, None] * np.array([inc[c] for c in c0s])).sum(0).tolist()
if __name__ == "__main__":
    t0 = time.time()
    # p_r(t) for this Omega: reuse E02's routine with a patched Config default
    e2.Config = lambda **k: Config(Omega_MHz=OM, **k)
    ts, pr, T = e2.rydberg_population(); Ir = np.trapezoid(pr, ts)
    rates = {n: sum(contaminant_weights("Rb87", 53, 0.5, n)[1].values()) for n in (52, 53)}
    edges = np.linspace(0, T, 7); tons = 0.5 * (edges[1:] + edges[:-1])
    wt = np.array([np.trapezoid(pr[(ts >= a) & (ts < b)], ts[(ts >= a) & (ts < b)]) for a, b in zip(edges[:-1], edges[1:])]); wt /= wt.sum()
    for k in itertools.product((52, 53), "xz"): model(*k)
    jobs = list(itertools.product((52, 53), "xz", RS, (0, 90), [0.0] + tons.tolist()))
    with Pool(4) as p:
        res = [(list(a), v) for a, v in p.imap_unordered(task, jobs, chunksize=4)]
    json.dump(dict(Omega=OM, T_us=T, I_r_us=Ir, I_r_over_T=Ir / T, p_c={n: rates[n] * Ir * 1e-6 for n in rates},
                   t_on=tons.tolist(), t_on_weight=wt.tolist(), res=res), open(f"experiments/E08_omega_maps/res_{OM:g}.json", "w"))
    print("done", OM, time.time() - t0, flush=True)
