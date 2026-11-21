"""E10 circuit model (D010): rotated surface-code memory with same-layer contaminant errors.

Physical layout: in each CX layer of stim's rotated_memory_z circuit, every (control, target) pair is one gate site
(two atoms). Site centres are midpoints of the two qubits' coordinates; one coordinate unit = PITCH/2 (sites of one
layer form a square grid of spacing 2 units -> 8.571 um along x, 12.0 um along y, D008). Source atoms sit +-1 um
along x about their site centre (d_pair = 2 um, pair axis x). Error per target pair from a contaminant at source s:
E_same(R, alpha) from E02 (summary.json same_weighted, B along BDIR, comp 0 = total incl. leakage), interpolated
linearly in (log R, log E) and in alpha in [0, 90] deg, R^-6 beyond 40 um, clipped below 4 um.
A failed pair is fully depolarised (each of the 16 two-qubit Paulis with probability 1/16): unheralded loss.
"""
import json, itertools, numpy as np, stim

PITCH = (8.571, 12.0); D_PAIR = 2.0; P_C = 2.533e-4
_S = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]

def emap(bdir="z"):
    RS = sorted({eval(k)[1] for k in _S if eval(k)[0] == bdir})
    Z = np.array([[_S[str((bdir, R, al))][0] for al in (0, 90)] for R in RS])
    return np.array(RS, float), Z

def E_same(rel, RS, Z):
    """rel: (N, 2) vectors from source atom to target site centre (um)."""
    R = np.hypot(rel[:, 0], rel[:, 1]); al = np.degrees(np.arctan2(np.abs(rel[:, 1]), np.abs(rel[:, 0]))) / 90.0
    lR = np.log(np.clip(R, RS[0], RS[-1])); lE = np.log(np.maximum(Z, 1e-300))
    e0 = np.interp(lR, np.log(RS), lE[:, 0]); e1 = np.interp(lR, np.log(RS), lE[:, 1])
    E = np.exp(e0 * (1 - al) + e1 * al)
    return E * np.where(R > RS[-1], (RS[-1] / np.maximum(R, 1e-9)) ** 6, 1.0)

PAULI = "IXYZ"

def layer_noise(pairs, coords, mult, mode, cluster_min=0.05, rng=None, bdir="z", pitch=PITCH, scale_check=1.0, coupling="xor"):
    """Noise instructions (stim.Circuit) for one CX layer.
    pairs: list of (q1, q2); coords: dict q -> (x, y). mode: 'corr' or 'indep'. Returns (circuit, marginal f per pair)."""
    RS, Z = emap(bdir); p = mult * P_C
    cen = np.array([[(coords[a][0] + coords[b][0]) / 2 * pitch[0] / 2, (coords[a][1] + coords[b][1]) / 2 * pitch[1] / 2]
                    for a, b in pairs])
    n = len(pairs); out = stim.Circuit(); f_miss = np.ones(n)        # prod(1 - p E) over sources, per target
    events = []                                                      # per source: list of (cluster targets, E values)
    tail = np.zeros(n)                                               # prod(1 - p E) for tail contributions
    tail_miss = np.ones(n)
    for s in range(n):
        for sgn in (-1, 1):
            src = cen[s] + np.array([sgn * D_PAIR / 2, 0.0])
            others = [j for j in range(n) if j != s]
            E = E_same(cen[others] - src, RS, Z) * scale_check
            f_miss[others] *= 1 - p * E
            if mode == "corr":
                cl = [(j, e) for j, e in zip(others, E) if e >= cluster_min]
                for j, e in zip(others, E):
                    if e < cluster_min: tail_miss[j] *= 1 - p * e
                events.append(cl)
    f = 1 - f_miss
    if mode == "indep":
        for j in range(n):
            if f[j] > 0: out.append("DEPOLARIZE2", [pairs[j][0], pairs[j][1]], min(f[j] * 15 / 16, 15 / 16))
        return out, f
    rng = rng or np.random.default_rng(0)
    for cl in events:
        if not cl: continue
        k = len(cl); chain = []
        for bits in itertools.product((0, 1), repeat=k):
            if not any(bits): continue
            q = p * np.prod([e if b else 1 - e for (j, e), b in zip(cl, bits)])
            sub = [cl[i][0] for i in range(k) if bits[i]]
            offs = rng.integers(0, 16, size=len(sub))
            rnd = rng.integers(0, 16, size=(16, len(sub)))           # variant V1: independent random strings
            for i in range(16):                                      # xor: per pair exactly uniform over 16 Paulis
                tg = []
                for jj, (j, c) in enumerate(zip(sub, offs)):
                    idx = (i ^ int(c)) if coupling == "xor" else int(rnd[i, jj])
                    for qb, pi in ((pairs[j][0], idx & 3), (pairs[j][1], idx >> 2)):
                        if pi: tg.append(getattr(stim, "target_" + PAULI[pi].lower())(qb))
                if tg: chain.append((q / 16, tg))
        used = 0.0
        for i, (q, tg) in enumerate(chain):
            out.append("E" if i == 0 else "ELSE_CORRELATED_ERROR", tg, min(q / (1 - used), 1.0)); used += q
    for j in range(n):
        tf = 1 - tail_miss[j]
        if tf > 0: out.append("DEPOLARIZE2", [pairs[j][0], pairs[j][1]], tf * 15 / 16)
    return out, f

def build(d, p, mult, mode, rounds=None, seed=0, bdir="z", pitch=PITCH, scale_check=1.0, cluster_min=0.05, coupling="xor"):
    """Rotated memory-Z circuit with baseline p (after Clifford, reset, measure) plus contaminant noise after each CX layer."""
    base = stim.Circuit.generated("surface_code:rotated_memory_z", distance=d, rounds=rounds or d,
                                  after_clifford_depolarization=p, after_reset_flip_probability=p,
                                  before_measure_flip_probability=p).flattened()
    if mode == "base" or mult == 0:
        return base, []
    coords = {q: c for q, c in base.get_final_qubit_coordinates().items()}
    rng = np.random.default_rng(seed); out = stim.Circuit(); margs = []; cache = {}
    for ins in base:
        out.append(ins)
        if ins.name == "DEPOLARIZE2" or (ins.name == "CX" and p == 0):
            t = [x.value for x in ins.targets_copy()]; pairs = tuple(zip(t[::2], t[1::2]))
            if pairs not in cache:
                cache[pairs] = layer_noise(list(pairs), coords, mult, mode, cluster_min, rng, bdir, pitch, scale_check, coupling)
            c, f = cache[pairs]; out += c; margs.append(f)
    return out, margs
