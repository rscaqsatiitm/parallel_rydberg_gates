# Working rules (adopted from the handover, Section 4)

1. **Provenance.** Every number entering a computation is a keyed entry in `params/registry.yaml`
   with value, unit, source and a verbatim quote from the primary PDF (see D001 for the source
   used). Nothing is quoted from memory. A value read from a figure is a range flagged
   `figure_read: true` for human check. Atomic quantities from ARC or `pairinteraction` record the
   library version and the call.
2. **No fabrication.** A number no source contains is a range with sourced bounds, or the task is blocked.
3. **Pre-registration.** Each `experiments/<id>/README.md` states design, expectation and verdict rule
   in a commit made before the run. Results are appended; text above them is not edited.
4. **No fitted parameter** in any comparison with an experiment.
5. **Controls before real runs**: planted answer recovered through the full path; corrupted input caught; a null checked.
6. **Independent route**: each key number from two solvers, with shared layers named.
7. **Derivations** carry a header (assumptions, conventions, domain of validity, dependencies) and
   are checked by a fresh agent given only the assumptions and neutrally worded questions.
8. **Statistics**: a logical error rate needs >= 100 failures or 1e6 shots, with a 95 % interval.
   Zero failures is an upper bound.
9. **Decision records** (`decisions/Dnnn_*.md`) for every design choice no source fixes. Commit
   messages start with the task ID (S0, S1, ...).
10. **Priority**: state what each prior work showed and exactly what it did not.

Kill tests: K1 (prior art), K2 (correlated error < 1e-5 per atom per gate at published spacing for
every published configuration), K3 (disagreement with measured covariance). Gate 1 = K1, K2, K3 not
fired. Gate 2 = a design-changing quantitative statement stable under doubled shots and a second decoder.
