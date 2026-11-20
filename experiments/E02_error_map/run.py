import sys, json, time, itertools, numpy as np
from multiprocessing import Pool
sys.path.insert(0, "src")
from prg.model import Config, ThreeAtom, contaminant_increment, run_gate, evolve, pulse_phase, COMP
from prg.atomic import Level, contaminant_weights
BD = {"x": (1.0, 0, 0), "y": (0, 1.0, 0), "z": (0, 0, 1.0)}
RS = [4, 5, 6, 7, 8, 10, 12, 14, 17, 20, 25, 30, 40]
_cache = {}
def model(np_, bd):
    k = (np_, bd)
    if k not in _cache:
        m = ThreeAtom(Config(nprime=np_, bfield_dir=BD[bd]))
        w, _ = contaminant_weights("Rb87", 53, 0.5, np_)
        c0s = [m.ryd.index(lv) for lv in w if w[lv] > 0]
        ws = np.array([w[m.ryd[c]] for c in c0s])
        base = contaminant_increment(m, (1e4, 0, 0), c0s)[1]
        _cache[k] = (m, c0s, ws, base)
    return _cache[k]
def task_full(args):
    np_, bd, R, al = args
    m, c0s, ws, base = model(np_, bd)
    r = (R * np.cos(np.radians(al)), R * np.sin(np.radians(al)), 0.0)
    inc, _ = contaminant_increment(m, r, c0s, baseline=base)
    return args, (ws[:, None] * np.array([inc[c] for c in c0s])).sum(0).tolist()
def task_same(args):
    np_, bd, R, al, ton = args
    m, c0s, ws, base = model(np_, bd)
    r = (R * np.cos(np.radians(al)), R * np.sin(np.radians(al)), 0.0)
    inc, _ = contaminant_increment(m, r, c0s, t_on=ton, baseline=base)
    return args, (ws[:, None] * np.array([inc[c] for c in c0s])).sum(0).tolist()
def rydberg_population():
    """p_r(t) of atom A, averaged over 4 comp inputs; returns times, p_r, T."""
    m = ThreeAtom(Config()); cfg = m.cfg
    T, amp, phi = pulse_phase(cfg)
    H, L = m.hamiltonian_static(None)
    from scipy.sparse.linalg import expm_multiply
    c0 = m.ryd.index(Level(52, 1, 1.5, 1.5))
    N = m.dG ** 2 * m.dC; cols = []
    for (a, b) in COMP:
        v = np.zeros(N, complex); v[m.basis_index(a, b, c0)] = 1; cols.append(v)
    psi = np.array(cols).T; dt = T / cfg.nsteps
    # projector on A Rydberg (any S or P state of A)
    idx = np.array([i for i in range(N) if (i // m.dC) // m.dG >= 2])
    ts, pr = [], []
    for k in range(cfg.nsteps):
        tm = (k + 0.5) * dt
        Hl = 0.5 * amp(tm) * (np.exp(1j * phi(tm)) * L + np.exp(-1j * phi(tm)) * L.getH())
        psi = expm_multiply(-2j * np.pi * dt * (H + Hl), psi)
        ts.append((k + 1) * dt); pr.append(np.mean(np.sum(np.abs(psi[idx]) ** 2, axis=0)))
    return np.array(ts), np.array(pr), T
if __name__ == "__main__":
    t0 = time.time(); out = {}
    ts, pr, T = rydberg_population()
    Ir = np.trapezoid(pr, ts)
    out["T_us"] = T; out["I_r_us"] = Ir; out["I_r_over_T"] = Ir / T
    rates = {}
    for np_ in (52, 53):
        _, r = contaminant_weights("Rb87", 53, 0.5, np_); rates[np_] = sum(r.values())
    out["rate_to_nP"] = rates; out["p_c"] = {k: v * Ir * 1e-6 for k, v in rates.items()}
    print("T", T, "I_r", Ir, "I_r/T", Ir / T, "rates", rates, "p_c", out["p_c"], flush=True)
    # t_on grid and weights
    edges = np.linspace(0, T, 13); tons = 0.5 * (edges[1:] + edges[:-1])
    wt = np.array([np.trapezoid(pr[(ts >= a) & (ts < b)], ts[(ts >= a) & (ts < b)]) for a, b in zip(edges[:-1], edges[1:])])
    wt = wt / wt.sum(); out["t_on"] = tons.tolist(); out["t_on_weight"] = wt.tolist()
    full = list(itertools.product((52, 53), "xyz", RS, (0, 30, 60, 90)))
    same = list(itertools.product((52, 53), "xz", RS, (0, 90), tons.tolist()))
    for k in itertools.product((52, 53), "xyz"):
        model(*k)                       # build in parent (ARC sqlite is not fork/concurrency safe)
    with Pool(4) as p:
        out["full"] = [(list(a), v) for a, v in p.imap_unordered(task_full, full, chunksize=4)]
        print("full done", time.time() - t0, flush=True)
        out["same_raw"] = [(list(a), v) for a, v in p.imap_unordered(task_same, same, chunksize=8)]
    print("same done", time.time() - t0, flush=True)
    json.dump(out, open("experiments/E02_error_map/results.json", "w"))
