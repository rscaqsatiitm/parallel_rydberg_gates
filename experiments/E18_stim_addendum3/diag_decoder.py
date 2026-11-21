# Diagnostic (run before the E18 amendment; exploratory): E10 corr samples (seed 0 table, as E10) decoded with
# (a) own corr DEM (E10), (b) indep DEM, (c) own corr DEM + PyMatching correlated matching. m = 1, p = 1e-3.
import sys, numpy as np, pymatching
from multiprocessing import Pool
sys.path.insert(0, "experiments/E18_stim_addendum3")
import e18
def work(args):
    d, shots, seed = args
    c, _ = e18.m10.build(d, 1e-3, 1, "corr"); ci, _ = e18.m10.build(d, 1e-3, 1, "indep")
    mo = pymatching.Matching.from_detector_error_model(e18.dem_of(c))
    mi = pymatching.Matching.from_detector_error_model(e18.dem_of(ci))
    mc = pymatching.Matching.from_detector_error_model(e18.clean_for_correlations(e18.dem_of(c)), enable_correlations=True)
    s = c.compile_detector_sampler(seed=seed); k = np.zeros(3, int)
    for b in range(0, shots, 100_000):
        det, obs = s.sample(min(100_000, shots - b), separate_observables=True)
        k += [int(np.any(mo.decode_batch(det) != obs, axis=1).sum()), int(np.any(mi.decode_batch(det) != obs, axis=1).sum()),
              int(np.any(mc.decode_batch(det, enable_correlations=True) != obs, axis=1).sum())]
    return k
if __name__ == "__main__":
    for d, shots in ((3, 1_000_000), (5, 1_500_000), (7, 3_000_000)):
        with Pool(3) as p: k = sum(p.map(work, [(d, shots // 3, 11 + i) for i in range(3)]))
        print(f"d={d} shots={shots} fails own/indepDEM/own+corrmatch = {k.tolist()}", flush=True)
