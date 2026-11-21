"""Sampling + PyMatching decoding loop (no sinter). Wilson 95 % intervals."""
import sys, time, numpy as np, stim, pymatching
from multiprocessing import Pool
sys.path.insert(0, "experiments/E10_stim_correlated")
from model import build

def dem_of(c):
    return c.detector_error_model(decompose_errors=True, approximate_disjoint_errors=True,
                                  ignore_decomposition_failures=True)

def _work(args):
    d, p, mult, mode, shots, seed, kw = args
    c, _ = build(d, p, mult, mode, **kw)
    m = pymatching.Matching.from_detector_error_model(dem_of(c))
    s = c.compile_detector_sampler(seed=seed)
    det, obs = s.sample(shots, separate_observables=True)
    pred = m.decode_batch(det)
    return int(np.any(pred != obs, axis=1).sum())

def run(d, p, mult, mode, shots, nproc=4, chunk=None, seed0=1, **kw):
    chunk = chunk or max(1, shots // nproc)
    jobs = [(d, p, mult, mode, min(chunk, shots - i), seed0 + k, kw) for k, i in enumerate(range(0, shots, chunk))]
    with Pool(nproc) as pool:
        fails = sum(pool.map(_work, jobs))
    return fails

def wilson(k, n, z=1.96):
    ph = k / n; den = 1 + z * z / n; c = (ph + z * z / (2 * n)) / den; h = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return c - h, ph, c + h

def per_round(x, r):
    return 1 - (1 - x) ** (1 / r)
