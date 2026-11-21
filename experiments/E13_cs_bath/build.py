import sys, time; sys.path.insert(0, "src")
from prg.bath import Bath
t0 = time.time(); b = Bath(cache="experiments/E13_cs_bath/levels_A.npz"); print("levels", len(b.levels), "built in", round(time.time() - t0), "s; min sink", b.sink.min())
