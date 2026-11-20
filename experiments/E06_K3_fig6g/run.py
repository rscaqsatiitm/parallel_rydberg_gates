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
