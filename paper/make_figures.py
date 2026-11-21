"""Regenerate the paper figures from committed results (no new computation). Run from the repository root."""
import json, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use("Agg"); import matplotlib.pyplot as plt
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]; INK = "#0b0b0b"; MUTED = "#52514e"
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "axes.edgecolor": MUTED, "xtick.color": MUTED,
                     "ytick.color": MUTED, "axes.labelcolor": INK, "legend.frameon": False, "lines.linewidth": 1.5,
                     "lines.markersize": 4, "savefig.bbox": "tight", "font.family": "serif"})
OUT = "paper/figures/"

# Fig. 1: error per contaminant, Omega/2pi = 4.6 MHz (E02)
S = json.load(open("experiments/E02_error_map/summary.json"))
def series(kind, bd, al, comp=0):
    d = {eval(k)[1]: v for k, v in S[kind].items() if eval(k)[0] == bd and eval(k)[2] == al}
    R = np.array(sorted(d)); return R, np.array([d[r][comp] for r in R]), np.array([d[r][1] for r in R])
fig, ax = plt.subplots(1, 2, figsize=(6.8, 2.5))
for (bd, al, c, m, lab) in [("x", 0, C[0], "o", r"$\mathbf{B}\parallel\hat x$, $\alpha=0^\circ$"),
                            ("x", 90, C[1], "s", r"$\mathbf{B}\parallel\hat x$, $\alpha=90^\circ$"),
                            ("z", 0, C[2], "^", r"$\mathbf{B}\parallel\hat z$, $\alpha=0^\circ$")]:
    R, E, L = series("full_weighted", bd, al); ax[0].loglog(R, E, m + "-", color=c, label=lab)
    ax[1].semilogx(R, L / E, m + "-", color=c)
R, E, _ = series("same_weighted", "z", 0); ax[0].loglog(R, E, "^--", color=C[2], mfc="white", label=r"$E_{\rm same}$, $\mathbf{B}\parallel\hat z$, $\alpha=0^\circ$")
ax[0].set(xlabel=r"$R$ ($\mu$m)", ylabel=r"error increment $E$", ylim=(1e-4, 1.5)); ax[0].legend(fontsize=6.5, loc="lower left")
ax[1].set(xlabel=r"$R$ ($\mu$m)", ylabel=r"leakage fraction $L/E_{\rm full}$", ylim=(0, 1.05))
from matplotlib.ticker import NullFormatter
for a in ax: a.set_xticks([4, 6, 10, 20, 40]); a.set_xticklabels(["4", "6", "10", "20", "40"]); a.xaxis.set_minor_formatter(NullFormatter())
ax[0].text(0.97, 0.97, "(a)", transform=ax[0].transAxes, va="top", ha="right", color=INK)
ax[1].text(0.97, 0.03, "(b)", transform=ax[1].transAxes, va="bottom", ha="right", color=INK)
fig.savefig(OUT + "fig1_error_map.pdf"); fig.savefig(OUT + "fig1_error_map.png", dpi=200); plt.close(fig)

# Fig. 2: excess error vs time between gates, prediction band vs BLU25 ED Fig. 6g (E06)
P = json.load(open("experiments/E06_K3_fig6g/predictions.json")); G = [50.0, 100.0, 200.0, 400.0]
fig, ax = plt.subplots(figsize=(3.4, 2.5))
for sparse, c, lab in [(False, C[0], "normal spacing"), (True, C[1], r"sparse ($2\times$)")]:
    for static, ls in [(False, "-"), (True, ":")]:
        rows = [p for p in P if p["sparse"] == sparse and p["static"] == static]
        ref = 400.0 if not sparse else 200.0; gs = [g for g in G if g <= ref]
        D = np.array([[f * 100 * (p["eps"][str(g)] - p["eps"][str(ref)]) for g in gs] for p in rows for f in (0.8, 1.0)])
        if not static: ax.fill_between(gs, D.min(0), D.max(0), color=c, alpha=0.2, lw=0)
        ax.plot(gs, np.median(D, 0), ls, color=c, label=lab + (" (decay only, median)" if static else " (model median, band)"))
ax.errorbar([50, 100, 200], [0.176, 0.001, 0.006], yerr=[0.018, 0.034, 0.017], fmt="o", color=INK, ms=4, capsize=2, label="BLU25 normal (figure read)")
ax.errorbar([50], [-0.015], yerr=[0.037], fmt="s", color=INK, mfc="white", ms=4, capsize=2, label="BLU25 sparse (figure read)")
ax.axhline(0, color=MUTED, lw=0.5); ax.set(xscale="log", xlabel=r"time between gates $t$ ($\mu$s)", ylabel=r"excess infidelity $D(t)$ (%)")
ax.set_xticks(G); ax.set_xticklabels([str(int(g)) for g in G]); ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_ylim(-0.06, 0.36); ax.legend(fontsize=5.5, loc="upper right", ncol=1)
fig.savefig(OUT + "fig2_fig6g.pdf"); fig.savefig(OUT + "fig2_fig6g.png", dpi=200); plt.close(fig)

# Fig. 3: same-layer floor vs Rabi frequency (E08) and vs lattice scale factor and temperature (E09)
F = json.load(open("experiments/E08_omega_maps/floor_omega.json")); Om = sorted(float(k) for k in F)
R9 = json.load(open("experiments/E09_cycle_floor/results.json"))
fig, ax = plt.subplots(1, 2, figsize=(6.8, 2.5))
lo = [F[f"{o:g}"][0] for o in Om]; hi = [F[f"{o:g}"][1] for o in Om]
ax[0].fill_between(Om, lo, hi, color=C[0], alpha=0.25, lw=0); ax[0].loglog(Om, np.sqrt(np.array(lo) * np.array(hi)), "o-", color=C[0])
ax[0].axhline(1e-4, color=MUTED, lw=0.6, ls="--"); ax[0].axvline(4.6, color=MUTED, lw=0.6, ls=":")
ax[0].text(4.8, 4e-5, "published\n4.6 MHz", color=MUTED, fontsize=6.5)
ax[0].set(xlabel=r"$\Omega/2\pi$ (MHz)", ylabel=r"same-layer floor $\epsilon_{\rm same}$ per CZ"); ax[0].set_xticks(Om); ax[0].set_xticklabels([f"{o:g}" for o in Om]); ax[0].xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
for T, c, m in [("300.0", C[0], "o"), ("45.0", C[1], "s"), ("4.0", C[2], "^")]:
    rows = R9[T]["rows"]; s = sorted(float(k) for k in rows[0]["floors"])
    V = np.array([[r["floors"][f"{x:g}" if f"{x:g}" in r["floors"] else str(x)] for x in s] for r in rows])
    ax[1].fill_between(s, V.min(0), V.max(0), color=c, alpha=0.25, lw=0); ax[1].semilogy(s, np.sqrt(V.min(0) * V.max(0)), m + "-", color=c, label=f"{float(T):g} K")
ax[1].axhline(1e-4, color=MUTED, lw=0.6, ls="--"); ax[1].set(xlabel=r"lattice scale factor $s$", ylabel=r"$\epsilon_{\rm same}$ per CZ"); ax[1].legend(fontsize=6.5)
for a, t in zip(ax, "ab"): a.text(0.5, 0.97, f"({t})", transform=a.transAxes, va="top", ha="center", color=INK)
fig.savefig(OUT + "fig3_floor.pdf"); fig.savefig(OUT + "fig3_floor.png", dpi=200); plt.close(fig)
print("figures written")
