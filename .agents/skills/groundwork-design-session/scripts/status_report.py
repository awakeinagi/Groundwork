#!/usr/bin/env python3
"""Groundwork project state assessment.

Usage: python3 status_report.py [project_root]   (default: cwd)

Prints an artifact census, open items, the refinement frontier, and a
recommended mode for the groundwork-design-session skill:
  Mode 1 (bootstrap) | Mode 2 (begin design) | Mode 3 (continue design)
"""

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("status_report.py requires PyYAML: pip install pyyaml")
    sys.exit(2)

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
DERIVABLE = {"business-goal": "epics", "epic": "stories/spikes"}


def as_list(v):
    return [] if v is None else (v if isinstance(v, list) else [v])


def load(root):
    arts = {}
    for path in sorted((root / "docs").rglob("*.md")):
        if path.parent.name == "specs":
            continue
        m = FM_RE.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and fm.get("id"):
            fm["_path"] = path.relative_to(root)
            arts[str(fm["id"])] = fm
    return arts


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    agents_md = root / "AGENTS.md"
    has_marker = agents_md.exists() and \
        "groundwork" in agents_md.read_text(encoding="utf-8").lower()
    has_docs = (root / "docs").is_dir()

    if not has_docs:
        print(f"Project root: {root}")
        print("No docs/ tree found."
              + (" AGENTS.md has a Groundwork marker." if has_marker else ""))
        print("\nRECOMMENDED MODE: 1 (bootstrap), then 2 (begin design)")
        return 0

    arts = load(root)
    print(f"Project root: {root}")
    print(f"Groundwork AGENTS.md marker: {'yes' if has_marker else 'NO'}")
    print(f"Artifacts: {len(arts)}\n")

    # Census
    census = defaultdict(Counter)
    for fm in arts.values():
        census[fm.get("type", "?")][fm.get("status", "?")] += 1
    for t in sorted(census):
        parts = ", ".join(f"{s}: {n}" for s, n in sorted(census[t].items()))
        print(f"  {t:<16} {sum(census[t].values()):>3}   ({parts})")

    # Open items
    def by(pred):
        return sorted(a for a, fm in arts.items() if pred(fm))

    gated = by(lambda f: f.get("status") == "gated")
    stale = by(lambda f: f.get("status") == "stale")
    wip = by(lambda f: f.get("status") in ("draft", "in-refinement")
             and f.get("type") not in ("session", "decision"))
    open_cfl = by(lambda f: f.get("type") == "conflict"
                  and f.get("status") != "resolved")
    pending_cp = by(lambda f: f.get("type") == "change-proposal"
                    and f.get("triage", "pending") == "pending")

    print("\nOpen items:")
    for label, items in [("gated (awaiting approval)", gated),
                         ("stale (awaiting re-affirmation)", stale),
                         ("draft/in-refinement", wip),
                         ("open conflicts (BLOCKING)", open_cfl),
                         ("untriaged change proposals", pending_cp)]:
        print(f"  {label:<32} {', '.join(items) if items else '-'}")

    # Frontier: approved parents with no derived children
    children = defaultdict(list)
    for aid, fm in arts.items():
        for p in as_list((fm.get("links") or {}).get("derives-from")):
            children[p].append(aid)
    frontier = []
    for aid, fm in arts.items():
        if fm.get("status") == "approved" and fm.get("type") in DERIVABLE:
            kids = [k for k in children[aid]
                    if arts[k].get("type") not in ("session", "decision")]
            if not kids:
                frontier.append(f"{aid} (approved, no {DERIVABLE[fm['type']]}"
                                f" derived yet)")
    print(f"\nFrontier: {'; '.join(frontier) if frontier else '-'}")

    # Components readiness
    comps = {a: f for a, f in arts.items() if f.get("type") == "component"}
    if comps:
        done = [a for a, f in comps.items() if f.get("status") == "approved"]
        print(f"Component docs approved: {len(done)}/{len(comps)}")

    # Mode recommendation
    approved_goals = by(lambda f: f.get("type") == "business-goal"
                        and f.get("status") == "approved")
    if not any(f.get("type") == "business-goal" for f in arts.values()):
        mode = "2 (begin design — structure exists, no business goal yet)"
    elif not approved_goals:
        mode = ("2/3 (a business goal exists but none approved — "
                "finish goal refinement and gate it)")
    else:
        mode = "3 (continue design)"
    print(f"\nRECOMMENDED MODE: {mode}")

    # Next-ID helper
    maxn = defaultdict(int)
    for aid in arts:
        p, n = aid.split("-")
        maxn[p] = max(maxn[p], int(n))
    nxt = ", ".join(f"{p}-{maxn[p] + 1:04d}" for p in sorted(maxn))
    if nxt:
        print(f"Next IDs: {nxt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
