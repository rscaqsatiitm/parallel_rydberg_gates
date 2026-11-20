"""Verify that every SOURCE entry of params/registry.yaml has a quote found in its source text."""
import sys, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from verify_quotes import corpus, norm
reg = yaml.safe_load(open(pathlib.Path(__file__).resolve().parents[1] / "params" / "registry.yaml"))
bad = 0
for k, e in reg.items():
    if e.get("type") == "SOURCE":
        ok = all(any(norm(p) in c for c in corpus(e["src"])) for p in e["quote"].split("...") if p.strip())
        if not ok:
            bad += 1; print("MISSING", k)
print(f"{len(reg)} entries, {bad} SOURCE quotes not found"); sys.exit(1 if bad else 0)
