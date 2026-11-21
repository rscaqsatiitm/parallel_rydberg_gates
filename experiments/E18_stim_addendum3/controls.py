# E18 pre-registered controls C1-C4.
import sys, json, numpy as np, pymatching
sys.path.insert(0, "experiments/E18_stim_addendum3")
import e18
from sim_util import wilson
out = {}
if __name__ == "__main__":
    # C1: flagged circuits sample the same physics as E10 circuits (same decoder: indep DEM)
    ci, _ = e18.m10.build(3, 1e-3, 1, "indep"); mi = pymatching.Matching.from_detector_error_model(e18.dem_of(ci))
    for mode in ("corr", "indep"):
        r = []
        for c in (e18.m10.build(3, 1e-3, 1, mode)[0], e18.build_flagged(3, 1e-3, 1, mode)[0]):
            if c.num_measurements > ci.num_measurements:       # flagged: sample measurements, convert
                meas = c.compile_sampler(seed=5).sample(1_000_000); det, obs = c.compile_m2d_converter().convert(measurements=meas, separate_observables=True)
            else:
                det, obs = c.compile_detector_sampler(seed=5).sample(1_000_000, separate_observables=True)
            k = int(np.any(mi.decode_batch(det) != obs, axis=1).sum()); r.append((k, wilson(k, 1_000_000)))
        ok = not (r[0][1][2] < r[1][1][0] or r[1][1][2] < r[0][1][0]); out[f"C1_{mode}"] = dict(E10=r[0][0], flagged=r[1][0], PASS=ok)
    # C2: flag fire rate equals marginal f per location (indep, m = 100, d = 3)
    c, locs = e18.build_flagged(3, 1e-3, 100, "indep")
    meas = c.compile_sampler(seed=9).sample(200_000); fl = meas[:, -len(locs):].mean(0)
    base = e18.stim.Circuit.generated("surface_code:rotated_memory_z", distance=3, rounds=3, after_clifford_depolarization=1e-3).flattened()
    coords = base.get_final_qubit_coordinates(); fexp = []
    for ins in base:
        if ins.name == "DEPOLARIZE2":
            t = [x.value for x in ins.targets_copy()]; pairs = list(zip(t[::2], t[1::2]))
            fexp += list(e18.layer_events(pairs, coords, 100, "indep", e18.m10.PITCH)[1])
    fexp = np.array(fexp); z = (fl - fexp) / np.sqrt(np.maximum(fexp * (1 - fexp), 1e-12) / 200_000)
    out["C2"] = dict(max_abs_z=float(np.abs(z).max()), mean_f=float(fexp.mean()), PASS=bool(np.abs(z).max() < 4.5))
    # C3: heralds carry information; shifted map loses it (corr, d = 3, m = 10, eta = 1 vs 0)
    good = e18.run_erasure(3, 1e-3, 10, "corr", 300_000, [0.0, 1.0], seed0=21)
    bad = e18.run_erasure(3, 1e-3, 10, "corr", 300_000, [0.0, 1.0], seed0=21, shift=1)
    sig = np.sqrt(good[0.0])
    out["C3"] = dict(no_herald=good[0.0], herald=good[1.0], herald_shifted=bad[1.0],
                     PASS=bool(good[1.0] < good[0.0] - 2 * sig and bad[1.0] >= good[0.0] - 2 * sig))
    # C4: correlated matching on base d = 5 vs standard
    cb, _ = e18.m10.build(5, 1e-3, 0, "base"); dem = e18.dem_of(cb)
    det, obs = cb.compile_detector_sampler(seed=4).sample(2_000_000, separate_observables=True)
    k0 = int(np.any(pymatching.Matching.from_detector_error_model(dem).decode_batch(det) != obs, axis=1).sum())
    mc = pymatching.Matching.from_detector_error_model(e18.clean_for_correlations(dem), enable_correlations=True)
    k1 = int(np.any(mc.decode_batch(det, enable_correlations=True) != obs, axis=1).sum())
    out["C4"] = dict(standard=k0, corrmatch=k1, note="agree within intervals, or small gain from Y-error correlations")
    json.dump(out, open("experiments/E18_stim_addendum3/controls.json", "w"), indent=1); print(json.dumps(out, indent=1))
