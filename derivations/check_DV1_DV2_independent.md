# Independent check: defect-rate model (Part A) and Rydberg light shifts (Part B)

Worked out from the problem statement alone. No repository files were read. Numbers come from Python with scipy.constants (CODATA).

## Part A

**A1.** A defect made k >= 1 layers ago (time k t) is still present with probability e^{-k t/tau}. Summed over sources and ages:
excess = sum_i p E_i sum_{k>=1} e^{-k t/tau} = p n / (e^{t/tau} - 1).
For large t this is approximately p n e^{-t/tau}.

**A2.** Setting p n/(e^{t/tau}-1) = eps gives the exact solution t = tau ln(1 + p n/eps).
For large t (p n >> eps), t ~ tau ln(p n/eps).
The relative error in t is 1 - ln(e^T - 1)/T, with T = t/tau. It equals 10 % at T = 1.80, which is p n/eps = 5.06.
- The approximation is within 10 % for t/tau >~ 1.8.
- The error is 7.3 % at T = 2, 1.7 % at T = 3 and 0.14 % at T = 5.
- At T = 1 the error is 46 %.
- The approximation always underestimates t.

**A3.** Per block of K layers, K p n/(e^{t/tau}-1) = eps_block. The exact solution is t = tau ln(1 + K p n/eps_block). For large t it becomes tau ln(K p n/eps_block). This is the same as using a per-layer target eps = eps_block/K.

**A4.** The same-layer term p m does not depend on t, so no choice of t removes it.
The condition is p m + p n/(e^{t/tau}-1) = eps, which gives t = tau ln(1 + p n/(eps - p m)).
The target is unreachable if p m >= eps. As p m approaches eps from below, t diverges.

## Part B

**B1.** For a free electron, m x'' = -e E0 cos(wt), so alpha = -e^2/(m_e w^2). In atomic units this is alpha = -1/w^2.
At 852 nm, hbar w = 0.053478 Eh, which gives alpha_e = -349.66 a.u. (-5.765e-39 C m^2/V).

**B2.** alpha_Ryd = -349.66 + 9.08 = -340.58 a.u. Light shifts scale with alpha, so the ratio is U_r/U_g = -340.58/2071.5 = -0.1644.
With the ground-state shift equal to -1 mK (attractive), the Rydberg shift at the intensity maximum is +164.4 uK. It is repulsive and equal to 16.4 % of U_g.

**B3.** With U0 = 164.4 uK k_B and m = 86.909 u:
- **Speed far away:** v = sqrt(2 U0/m) = 0.177 m/s = 0.177 um/us.
- **Behaviour near the top:** U ~ U0 (1 - 2 rho^2/w^2), so rho'' = gamma^2 rho with gamma = 2 sqrt(U0/m)/w. The e-folding time is 1/gamma = 3.99 us.
- **Starting displacement:** the ground-state trap has omega = sqrt(4 U_g/(m w^2)) = 2 pi x 98.5 kHz. The rms spread per axis is sigma = (w/2) sqrt(T/U_g) = 0.050 um. The 2D radial rms is sqrt(2) sigma = 0.0707 um.
- **Time to reach rho = w, starting at rest (exact Gaussian, energy-conservation integral):**
  - 15.8 us starting from sigma
  - 14.4 us starting from the radial rms
- **Harmonic estimate (1/gamma) arccosh(w/rho0):** 14.7 us and 13.3 us. Using (1/gamma) ln(w/rho0) gives about 11.9 us and 10.6 us.
- In short, the time is about 3 to 4 e-folding times, or roughly 14 to 16 us.
- The initial thermal velocity (about 0.03 um/us per axis) is neglected. It would shorten these times somewhat.

**B4.** The point-electron picture is a fair first approximation, with a correction of a few percent.
- **Orbit size:** for Rb nP the quantum defect is about 2.65, so n* = 50.35. Then <r> = (3n*^2 - l(l+1))/2 a0 = 0.20 um, and the rms radius is sqrt(<r^2>) = 0.21 um, where <r^2> = n*^2 (5n*^2 + 1 - 3l(l+1))/2 a0^2. The diameter is about 0.4 um, which is not negligible compared with w = 1 um.
- **Size of the correction:** the ponderomotive shift should be averaged over the electron density. At the beam centre, <I>/I0 ~ 1 - 2<rho^2>/w^2, so the peak shift is reduced by:

| State | Reduction of the peak shift |
|---|---|
| m_l = 0 | 3.6 % |
| isotropic average | 6.0 % |
| \|m_l\| = 1 | 7.2 % |

- The effective potential is also slightly broadened. The w^2/r^2 expansion is not fully converged, since r/w ~ 0.2.
