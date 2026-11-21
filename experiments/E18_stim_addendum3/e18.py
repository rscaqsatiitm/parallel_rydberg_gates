"""E18 model and sampler (D012). Reuses E10 model (emap, E_same, build, constants)."""
import sys, itertools, numpy as np, stim, pymatching
from multiprocessing import Pool
sys.path.insert(0, "experiments/E10_stim_correlated")
import model as m10
from model import emap, E_same, D_PAIR, P_C, PAULI

def _tg(q, pi):
    return getattr(stim, "target_" + PAULI[pi].lower())(q)

def layer_events(pairs, coords, mult, mode, pitch, nonres=1.0, cluster_min=0.05, seed=0):
    """Event structure for one layer: list of chains; chain = list of (prob, [(pair, pauli_idx)]) mutually exclusive."""
    RS, Z = emap("z"); p = mult * P_C
    cen = np.array([[(coords[a][0] + coords[b][0]) / 2 * pitch[0] / 2, (coords[a][1] + coords[b][1]) / 2 * pitch[1] / 2] for a, b in pairs])
    n = len(pairs); f_miss = np.ones(n); tail_miss = np.ones(n); events = []
    rng = np.random.default_rng(seed)
    for s in range(n):
        for sgn in (-1, 1):
            src = cen[s] + np.array([sgn * D_PAIR / 2, 0.0]); others = [j for j in range(n) if j != s]
            E = np.minimum(E_same(cen[others] - src, RS, Z) * nonres, 1.0)
            f_miss[others] *= 1 - p * E
            if mode == "corr":
                events.append([(j, e) for j, e in zip(others, E) if e >= cluster_min])
                for j, e in zip(others, E):
                    if e < cluster_min: tail_miss[j] *= 1 - p * e
    chains = []
    def pair_chain(j, f):
        return ("pair", j, f)
    if mode == "indep":
        for j in range(n):
            if f_miss[j] < 1: chains.append(pair_chain(j, 1 - f_miss[j]))
        return chains, 1 - f_miss
    for cl in events:
        if not cl: continue
        k = len(cl); ch = []
        for bits in itertools.product((0, 1), repeat=k):
            if not any(bits): continue
            q = p * np.prod([e if b else 1 - e for (j, e), b in zip(cl, bits)])
            sub = [cl[i][0] for i in range(k) if bits[i]]; offs = rng.integers(0, 16, size=len(sub))
            for i in range(16): ch.append((q / 16, [(j, i ^ int(c)) for j, c in zip(sub, offs)]))
        chains.append(ch)
    for j in range(n):
        if tail_miss[j] < 1: chains.append(pair_chain(j, 1 - tail_miss[j]))
    return chains, 1 - f_miss

def build_flagged(d, p, mult, mode, pitch=m10.PITCH, nonres=1.0, f_prev=0.0, flags=True, seed=0):
    """Returns (circuit, locations) ; locations[k] = (cx_layer_index, pair) for flag k. Flags measured at the end."""
    base = stim.Circuit.generated("surface_code:rotated_memory_z", distance=d, rounds=d, after_clifford_depolarization=p,
                                  after_reset_flip_probability=p, before_measure_flip_probability=p).flattened()
    coords = base.get_final_qubit_coordinates(); nq = base.num_qubits
    out = stim.Circuit(); locs = []; cache = {}; layer = -1
    for ins in base:
        out.append(ins)
        if ins.name == "DEPOLARIZE2":
            layer += 1
            t = [x.value for x in ins.targets_copy()]; pairs = tuple(zip(t[::2], t[1::2]))
            if mult > 0:
                if pairs not in cache: cache[pairs] = layer_events(list(pairs), coords, mult, mode, pitch, nonres, seed=seed)
                chains, _ = cache[pairs]
                fl = {}
                for j in range(len(pairs)):
                    fl[j] = nq + len(locs); locs.append((layer, pairs[j]))
                for ch in chains:
                    if isinstance(ch, tuple):                     # single-pair failure (indep or tail)
                        _, j, f = ch
                        if not flags:
                            out.append("DEPOLARIZE2", [pairs[j][0], pairs[j][1]], min(f * 15 / 16, 15 / 16)); continue
                        ch = [(f / 16, [(j, i)]) for i in range(16)]
                    used = 0.0; started = False
                    for i, (q, items) in enumerate(ch):
                        tg = []
                        for j, pi in items:
                            for qb, pp in ((pairs[j][0], pi & 3), (pairs[j][1], pi >> 2)):
                                if pp: tg.append(_tg(qb, pp))
                            if flags: tg.append(stim.target_x(fl[j]))
                        if not tg: tg = [stim.target_x(fl[items[0][0]])] if flags else []
                        if tg:
                            out.append("ELSE_CORRELATED_ERROR" if started else "E", tg, min(q / (1 - used), 1.0)); started = True
                            used += q
            if f_prev > 0:
                for a, b in pairs: out.append("DEPOLARIZE2", [a, b], f_prev * 15 / 16)
    if flags and locs:
        out.append("M", list(range(nq, nq + len(locs))))
    return out, locs

def dem_of(c):
    return c.detector_error_model(decompose_errors=True, approximate_disjoint_errors=True, ignore_decomposition_failures=True)

def herald_edges(d, locs):
    """For each location, the set of graphlike edges (u, v) (v = -1 for boundary) any Pauli on that pair produces."""
    clean = stim.Circuit.generated("surface_code:rotated_memory_z", distance=d, rounds=d).flattened()
    cx_pos = [i for i, ins in enumerate(clean) if ins.name == "CX"]
    out = []; cache = {}
    for layer, (a, b) in locs:
        key = (layer, a, b)
        if key not in cache:
            c = clean[:cx_pos[layer] + 1] + stim.Circuit(f"DEPOLARIZE2(0.01) {a} {b}") + clean[cx_pos[layer] + 1:]
            edges = set()
            for e in dem_of(c).flattened():
                if e.type != "error": continue
                comp = []
                for t in e.targets_copy():
                    if t.is_separator():
                        edges.add(tuple(sorted(comp)) if len(comp) == 2 else (comp[0], -1) if comp else None); comp = []
                    elif t.is_relative_detector_id(): comp.append(t.val)
                if comp: edges.add(tuple(sorted(comp)) if len(comp) == 2 else (comp[0], -1))
            edges.discard(None); cache[key] = edges
        out.append(cache[key])
    return out

def decode_heralded(m, det, obs, fired, edges_of):
    """Per-shot erasure decoding; fired: bool (shots, nloc). Returns number of failures."""
    fails = 0; base_pred = m.decode_batch(det)
    for s in range(det.shape[0]):
        idx = np.flatnonzero(fired[s])
        if idx.size == 0:
            fails += int(np.any(base_pred[s] != obs[s])); continue
        es = set().union(*(edges_of[i] for i in idx)); saved = []
        for u, v in es:
            if v == -1:
                if m.has_boundary_edge(u):
                    dd = m.get_boundary_edge_data(u); saved.append((u, v, dd))
                    m.add_boundary_edge(u, fault_ids=dd["fault_ids"], weight=0.0, error_probability=0.5, merge_strategy="replace")
            elif m.has_edge(u, v):
                dd = m.get_edge_data(u, v); saved.append((u, v, dd))
                m.add_edge(u, v, fault_ids=dd["fault_ids"], weight=0.0, error_probability=0.5, merge_strategy="replace")
        pred = m.decode(det[s])
        for u, v, dd in saved:
            if v == -1: m.add_boundary_edge(u, fault_ids=dd["fault_ids"], weight=dd["weight"], error_probability=dd["error_probability"], merge_strategy="replace")
            else: m.add_edge(u, v, fault_ids=dd["fault_ids"], weight=dd["weight"], error_probability=dd["error_probability"], merge_strategy="replace")
        fails += int(np.any(pred != obs[s]))
    return fails

def _work_erasure(args):
    d, p, mult, mode, shots, seed, etas, pitch, shift = args
    c, locs = build_flagged(d, p, mult, mode, pitch)
    edges = herald_edges(d, locs)
    if shift: edges = edges[shift:] + edges[:shift]            # corrupted map (control C3)
    nloc = len(locs); conv = c.compile_m2d_converter(); smp = c.compile_sampler(seed=seed)
    rng = np.random.default_rng(seed + 7)
    mats = {}
    for eta in etas:
        cd, _ = m10.build(d, p, mult * (1 - eta), mode, pitch=pitch) if eta < 1 else m10.build(d, p, 0, "base")
        mats[eta] = pymatching.Matching.from_detector_error_model(dem_of(cd))
    fails = {eta: 0 for eta in etas}; done = 0
    while done < shots:
        b = min(20_000, shots - done)
        meas = smp.sample(b); flags = meas[:, -nloc:]
        det, obs = conv.convert(measurements=meas, separate_observables=True)
        u = rng.random(flags.shape)
        for eta in etas:
            fired = flags & (u < eta)
            fails[eta] += decode_heralded(mats[eta], det, obs, fired, edges) if eta > 0 else int(np.any(mats[eta].decode_batch(det) != obs, axis=1).sum())
        done += b
    return fails

def run_erasure(d, p, mult, mode, shots, etas, pitch=m10.PITCH, nproc=3, seed0=1, shift=0):
    ch = -(-shots // nproc)
    jobs = [(d, p, mult, mode, min(ch, shots - i), seed0 + k, etas, pitch, shift) for k, i in enumerate(range(0, shots, ch))]
    with Pool(nproc) as pool: rs = pool.map(_work_erasure, jobs)
    return {eta: sum(r[eta] for r in rs) for eta in etas}

def _work_std(args):
    d, p, mult, mode, shots, seed, kw = args
    corrdec = kw.pop("corrdec", False)
    if mode == "base": c, _ = m10.build(d, p, 0, "base")
    else: c, _ = build_flagged(d, p, mult, mode, flags=False, **kw)
    m = pymatching.Matching.from_detector_error_model(dem_of(c), enable_correlations=corrdec)
    s = c.compile_detector_sampler(seed=seed); k = 0
    for b in range(0, shots, 100_000):
        det, obs = s.sample(min(100_000, shots - b), separate_observables=True)
        k += int(np.any(m.decode_batch(det, enable_correlations=corrdec) != obs, axis=1).sum())
    return k

def run_std(d, p, mult, mode, shots, nproc=3, seed0=1, **kw):
    ch = -(-shots // nproc)
    jobs = [(d, p, mult, mode, min(ch, shots - i), seed0 + k, dict(kw)) for k, i in enumerate(range(0, shots, ch))]
    with Pool(nproc) as pool: return sum(pool.map(_work_std, jobs))

def clean_for_correlations(dem):
    """PyMatching correlated matching rejects decomposed components with no detector; fold such a component's
    observables into the first component that has detectors (same flip set overall; decomposition only)."""
    out = stim.DetectorErrorModel()
    for e in dem.flattened():
        if e.type != "error":
            out.append(e); continue
        comps, cur = [], []
        for t in e.targets_copy():
            if t.is_separator(): comps.append(cur); cur = []
            else: cur.append(t)
        comps.append(cur)
        good = [c for c in comps if any(t.is_relative_detector_id() for t in c)]
        if not good:
            continue                                    # undetectable error: no decoder can see it
        extra = [t for c in comps if not any(t.is_relative_detector_id() for t in c) for t in c]
        if extra:
            obs = {}
            for t in good[0] + extra:
                if t.is_logical_observable_id(): obs[t.val] = obs.get(t.val, 0) ^ 1
            good[0] = [t for t in good[0] if t.is_relative_detector_id()] + [stim.target_logical_observable_id(k) for k, v in obs.items() if v]
        split = []
        for c in good:                                  # undecomposed components (> 2 detectors): split greedily
            dets = [t for t in c if t.is_relative_detector_id()]; obs_t = [t for t in c if not t.is_relative_detector_id()]
            if len(dets) <= 2: split.append(c); continue
            chunks = [dets[i:i + 2] for i in range(0, len(dets), 2)]; chunks[0] = chunks[0] + obs_t; split += chunks
        good = split
        tg = []
        for i, c in enumerate(good):
            if i: tg.append(stim.target_separator())
            tg += c
        out.append("error", e.args_copy(), tg)
    return out
