# E05. Contaminant creation rate and P-state lifetime vs temperature

2026-11-20, task S1. Pure evaluation of ARC 3.10.2 (getTransitionRate, getStateLifetime with
includeLevelsUpTo = n+40) at T = 300, 188 (JILA effective temperature, registry pending), 45, 4 K
(owner's addendum). No verdict rule (library evaluation). Known limitation: ARC treats BBR as an
ideal Planck spectrum at T; real cryostats leak room-temperature radiation through windows (JILA
measured T_eff = 188(8) K at a 45 K box), so the 45 K and 4 K numbers are ideal-shield limits.

## Result
300.0 4983.3 72.5 {'52P0.5': np.float64(97.7), '52P1.5': np.float64(95.8), '53P0.5': np.float64(102.2), '53P1.5': np.float64(100.1)}
188.0 3118.9 90.9 {'52P0.5': np.float64(133.2), '52P1.5': np.float64(129.4), '53P0.5': np.float64(139.6), '53P1.5': np.float64(135.6)}
45.0 738.5 133.8 {'52P0.5': np.float64(243.8), '52P1.5': np.float64(230.8), '53P0.5': np.float64(257.4), '53P1.5': np.float64(243.7)}
4.0 56.5 153.5 {'52P0.5': np.float64(312.7), '52P1.5': np.float64(291.0), '53P0.5': np.float64(331.8), '53P1.5': np.float64(308.8)}
T=0 radiative {'52P0.5': np.float64(318.3), '52P1.5': np.float64(295.8), '53P0.5': np.float64(338.0), '53P1.5': np.float64(314.1)}
