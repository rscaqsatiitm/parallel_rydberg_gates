import numpy as np
def wilson(k, n, z=1.96):
    ph = k / n; den = 1 + z * z / n; c = (ph + z * z / (2 * n)) / den; h = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return max(c - h, 0.0), ph, c + h
def per_round(x, r): return 1 - (1 - x) ** (1 / r)
