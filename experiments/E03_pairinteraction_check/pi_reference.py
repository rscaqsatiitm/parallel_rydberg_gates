"""Reference pair-state energies for 87Rb 53S1/2 + 52P_J with pairinteraction 2.7.0.

Basis: |53S1/2 m1>|52P_J m2> and |52P_J m1>|53S1/2 m2>, J = 1/2, 3/2, all m (48 states).
Interaction: electric dipole-dipole only (interaction order 3), exact diagonalisation in this basis.
B = 8.5 G along z, E = 0. Interatomic axis at angle theta to z (pairinteraction: set_distance(..., angle_degree)
is the angle between the distance vector and the z axis; 90 deg = x axis).
Energies in MHz (E/h), relative to the uncoupled |53S1/2,+1/2>|52P3/2,+1/2> at the same B.
"""

import json
import warnings
from pathlib import Path

import numpy as np
import pairinteraction as pi
from sympy import Rational
from sympy.physics.wigner import wigner_3j, wigner_6j

OUT = Path(__file__).with_name("pi_reference.json")
SPECIES = "Rb"  # pairinteraction's SQDT Rb table (87Rb, no hyperfine structure)
B_GAUSS = 8.5
THETAS = [0.0, 90.0]
DISTANCES_UM = [6.0, 10.0, 20.0]

caught = []
warnings.simplefilter("always")
with warnings.catch_warnings(record=True) as wlist:
    # --- reference kets -------------------------------------------------------------
    ket_s = pi.KetAtom(SPECIES, n=53, l=0, j=0.5, m=0.5)
    ket_p32 = pi.KetAtom(SPECIES, n=52, l=1, j=1.5, m=0.5)
    ket_p12 = pi.KetAtom(SPECIES, n=52, l=1, j=0.5, m=0.5)

    # --- single-atom basis: exactly 53S1/2 (2 kets) + 52P1/2 (2) + 52P3/2 (4) ----------
    e_s = ket_s.get_energy(unit="GHz")
    e_p12 = ket_p12.get_energy(unit="GHz")
    e_p32 = ket_p32.get_energy(unit="GHz")
    lo, hi = min(e_s, e_p12, e_p32) - 1.0, max(e_s, e_p12, e_p32) + 1.0
    basis_atom = pi.BasisAtom(SPECIES, n=(52, 53), l=(0, 1), energy=(lo, hi), energy_unit="GHz")
    labels_atom = [str(k) for k in basis_atom.kets]
    assert basis_atom.number_of_kets == 8, labels_atom

    system_atom = pi.SystemAtom(basis_atom)
    system_atom.set_magnetic_field([0, 0, B_GAUSS], unit="gauss")
    system_atom.diagonalize()

    # asymptotic reference energy (same B) of |53S1/2,+1/2>|52P3/2,+1/2>
    e_ref_mhz = system_atom.get_corresponding_energy(ket_s, unit="MHz") + system_atom.get_corresponding_energy(
        ket_p32, unit="MHz"
    )

    # --- pair basis: all product states with pair energy near E(53S)+E(52P_J) --------
    # (excludes SS and PP products, which are ~28 GHz away)
    e_sp_lo = (e_s + e_p12) * 1e3 - 2000.0
    e_sp_hi = (e_s + e_p32) * 1e3 + 2000.0
    if e_sp_lo > e_sp_hi:
        e_sp_lo, e_sp_hi = e_sp_hi - 4000.0, e_sp_lo + 4000.0

    def make_pair_basis(m=None):
        return pi.BasisPair([system_atom, system_atom], m=m, energy=(e_sp_lo, e_sp_hi), energy_unit="MHz")

    basis_pair = make_pair_basis()
    n_pair = basis_pair.number_of_states
    assert n_pair == 48, n_pair

    results = {}
    for theta in THETAS:
        for r in DISTANCES_UM:
            sp = pi.SystemPair(basis_pair).set_interaction_order(3).set_distance(r, angle_degree=theta, unit="micrometer")
            sp.diagonalize(diagonalizer="eigen", sort_by_energy=True)
            ev = np.sort(np.asarray(sp.get_eigenenergies(unit="MHz")) - e_ref_mhz)
            results[f"theta={theta:g}deg,R={r:g}um"] = ev.tolist()

    # uncoupled energies (R -> inf) for reference
    sp_inf = pi.SystemPair(basis_pair).set_interaction_order(3)  # no distance set -> no interaction
    h0 = sp_inf.get_hamiltonian(unit="MHz").toarray()
    asym = np.sort(np.real(np.linalg.eigvalsh(h0)) - e_ref_mhz)

    # --- total M = 1 block at theta = 0, R = 10 um ------------------------------------
    basis_m1 = make_pair_basis(m=(1, 1))
    sp_m1 = pi.SystemPair(basis_m1).set_interaction_order(3).set_distance(10.0, angle_degree=0.0, unit="micrometer")
    sp_m1.diagonalize(diagonalizer="eigen", sort_by_energy=True)
    ev_m1 = np.sort(np.asarray(sp_m1.get_eigenenergies(unit="MHz")) - e_ref_mhz)

    # cross-check: same block by projecting the full 48-dim Hamiltonian onto M = 1 kets
    sp_full = pi.SystemPair(basis_pair).set_interaction_order(3).set_distance(10.0, angle_degree=0.0, unit="micrometer")
    h = sp_full.get_hamiltonian(unit="MHz").toarray()
    kets_pair = basis_pair.kets
    coeff = basis_pair.get_coefficients().toarray()  # (n_kets x n_states)
    m_of_ket = np.array([k.ket_atoms[0].m + k.ket_atoms[1].m if hasattr(k, "ket_atoms") else np.nan for k in kets_pair])
    m_of_state = np.array([m_of_ket[np.argmax(np.abs(coeff[:, i]))] for i in range(n_pair)])
    idx = np.where(np.isclose(m_of_state, 1.0))[0]
    ev_m1_check = np.sort(np.linalg.eigvalsh(h[np.ix_(idx, idx)]) - e_ref_mhz)
    assert len(ev_m1_check) == len(ev_m1) and np.allclose(ev_m1_check, ev_m1, atol=1e-6), (ev_m1_check, ev_m1)

    # --- dipole matrix elements 53S1/2 <-> 52P3/2 ------------------------------------
    # q-resolved <53S1/2,m=1/2| d_q |52P3/2,m'> from the library (e*a0), then Wigner-Eckart.
    def half(x):
        return Rational(int(round(2 * x)), 2)

    d_q = {}
    for mp in (-1.5, -0.5, 0.5, 1.5):
        kp = pi.KetAtom(SPECIES, n=52, l=1, j=1.5, m=mp)
        for q in (-1, 0, 1):
            val = ket_s.get_matrix_element(kp, "electric_dipole", q, unit="bohr * elementary_charge")
            d_q[f"m'={mp:+g},q={q:+d}"] = float(np.real(val))
    # <j m| d_q |j' m'> = (-1)^(j-m) (j 1 j'; -m q m') <j||d||j'>; use m=1/2, m'=1/2, q=0
    j, m, jp, mp, q = 0.5, 0.5, 1.5, 0.5, 0
    tj = float(wigner_3j(half(j), 1, half(jp), half(-m), q, half(mp)))
    me = d_q["m'=+0.5,q=+0"]
    reduced_j = me / ((-1) ** (j - m) * tj)
    # <(l s) j || d || (l' s) j'> = (-1)^(l+s+j'+1) sqrt((2j+1)(2j'+1)) {l j s; j' l' 1} <l||d||l'>
    # <l||d||l'> = (-1)^l sqrt((2l+1)(2l'+1)) (l 1 l'; 0 0 0) * <r>   (radial integral)
    l, s, lp = 0, 0.5, 1
    six = float(wigner_6j(l, half(j), half(s), half(jp), lp, 1))
    reduced_l = reduced_j / ((-1) ** (l + s + jp + 1) * np.sqrt((2 * j + 1) * (2 * jp + 1)) * six)
    ang = (-1) ** l * np.sqrt((2 * l + 1) * (2 * lp + 1)) * float(wigner_3j(l, 1, lp, 0, 0, 0))
    radial = reduced_l / ang

    caught = [f"{w.category.__name__}: {w.message}" for w in wlist]

out = {
    "library": f"pairinteraction {pi.__version__}",
    "species": SPECIES,
    "single_atom_basis_kets": labels_atom,
    "pair_basis_dimension": int(n_pair),
    "B_gauss_along_z": B_GAUSS,
    "interaction_order": 3,
    "angle_convention": "theta = angle between interatomic vector and z (quantization/B axis); 90 deg = along x",
    "energy_unit": "MHz (E/h)",
    "reference": "uncoupled |53S1/2,+1/2>|52P3/2,+1/2> at B=8.5 G (single-atom eigenstate energies)",
    "reference_absolute_MHz": float(e_ref_mhz),
    "asymptotic_energies_R_inf": asym.tolist(),
    "eigenenergies": results,
    "theta=0,R=10um,M=1_block": ev_m1.tolist(),
    "dipole_53S1/2_52P3/2": {
        "q_resolved_<53S1/2,+1/2|d_q|52P3/2,m'>_e_a0": d_q,
        "reduced_<53S1/2||d||52P3/2>_e_a0 (Wigner-Eckart, Edmonds/Condon-Shortley (-1)^(j-m) 3j convention)": reduced_j,
        "radial_integral_<53S|r|52P>_a0 (derived, fine-structure-resolved radial wavefunctions of the j=3/2 state)": radial,
    },
    "warnings": caught,
}
OUT.write_text(json.dumps(out, indent=2))
print(json.dumps({k: v for k, v in out.items() if k != "eigenenergies"}, indent=2))
for k, v in results.items():
    print(k, np.round(v, 4).tolist())
