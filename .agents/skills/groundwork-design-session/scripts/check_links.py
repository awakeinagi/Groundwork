#!/usr/bin/env python3
"""Validate a Groundwork artifact graph.

Usage: python3 check_links.py [project_root]   (default: cwd)

Rules enforced:
  1. IDs unique; frontmatter `id` matches filename prefix and type.
  2. Every linked or cited ID resolves to an existing artifact.
  3. Every epic|story|spike|component traces to a business goal via
     derives-from/satisfies chains.
  4. Every decision derives from a session or spike.
  5. No approved artifact links conflicts-with an unresolved conflict.
  6. Impact links (impacts/impacted-by) are reciprocal and same-type.

Exit code 0 = graph is sound; 1 = violations; 2 = setup problem.

This file is installed into Groundwork projects as tools/check_links.py.
It requires PyYAML (`pip install pyyaml`).
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("check_links.py requires PyYAML: pip install pyyaml")
    sys.exit(2)

LINK_TYPES = {"derives-from", "satisfies", "depends-on", "conflicts-with",
              "supersedes", "relates-to", "impacts", "impacted-by"}
ID_RE = re.compile(r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP)-\d{4}$")
PREFIX_FOR_TYPE = {
    "business-goal": "BG", "epic": "EP", "story": "ST", "spike": "SP",
    "component": "CMP", "session": "SES", "decision": "DEC",
    "conflict": "CFL", "consolidation": "CON", "change-proposal": "CP",
}
MUST_TRACE_TO_GOAL = {"epic", "story", "spike", "component"}
SKIP_DIRS = {"specs"}  # non-artifact doc directories


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, "missing YAML frontmatter"
    try:
        return yaml.safe_load(m.group(1)), None
    except yaml.YAMLError as e:
        return None, f"unparseable frontmatter: {e}"


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    docs = root / "docs"
    if not docs.is_dir():
        print(f"No docs/ directory under {root} — not a Groundwork project "
              f"(or wrong root).")
        return 2

    errors = []
    artifacts = {}

    for path in sorted(docs.rglob("*.md")):
        if path.parent.name in SKIP_DIRS:
            continue
        fm, err = parse_frontmatter(path)
        rel = path.relative_to(root)
        if err:
            errors.append(f"{rel}: {err}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: empty or non-mapping frontmatter")
            continue
        aid = str(fm.get("id", ""))
        if not ID_RE.match(aid):
            errors.append(f"{rel}: bad or missing id {aid!r}")
            continue
        if not path.name.startswith(f"{aid}-"):
            errors.append(f"{rel}: filename does not start with id {aid}")
        if aid in artifacts:
            errors.append(f"{rel}: duplicate id {aid}")
            continue
        expected_prefix = PREFIX_FOR_TYPE.get(str(fm.get("type")))
        if expected_prefix is None:
            errors.append(f"{rel}: unknown type {fm.get('type')!r}")
        elif not aid.startswith(expected_prefix + "-"):
            errors.append(f"{rel}: id {aid} does not match type "
                          f"{fm['type']} (expected {expected_prefix}-)")
        fm["_path"] = rel
        artifacts[aid] = fm

    def refs(fm):
        links = fm.get("links") or {}
        for ltype, targets in links.items():
            if ltype not in LINK_TYPES:
                errors.append(f"{fm['_path']}: unknown link type {ltype!r}")
                continue
            for t in as_list(targets):
                yield ltype, t
        for t in as_list(fm.get("cites")):
            yield "cites", t

    # Rule 2: all references resolve
    for aid, fm in artifacts.items():
        for ltype, target in refs(fm):
            if target not in artifacts:
                errors.append(f"{fm['_path']}: {ltype} -> {target} "
                              f"does not resolve")

    # Rule 3: work artifacts trace to a goal
    def traces_to_goal(aid, seen):
        if aid in seen or aid not in artifacts:
            return False
        seen.add(aid)
        fm = artifacts[aid]
        if fm.get("type") == "business-goal":
            return True
        links = fm.get("links") or {}
        parents = as_list(links.get("derives-from")) + \
            as_list(links.get("satisfies"))
        return any(traces_to_goal(p, seen) for p in parents)

    for aid, fm in artifacts.items():
        if fm.get("type") in MUST_TRACE_TO_GOAL:
            if not traces_to_goal(aid, set()):
                errors.append(f"{fm['_path']}: {aid} does not trace to any "
                              f"business goal")

    # Rule 4: decisions derive from a session or spike
    for aid, fm in artifacts.items():
        if fm.get("type") != "decision":
            continue
        parents = as_list((fm.get("links") or {}).get("derives-from"))
        ok = any(artifacts.get(p, {}).get("type") in ("session", "spike")
                 for p in parents)
        if not ok:
            errors.append(f"{fm['_path']}: {aid} must derive from a "
                          f"session or spike")

    # Rule 6: impact links reciprocal and same-type
    INVERSE = {"impacts": "impacted-by", "impacted-by": "impacts"}
    for aid, fm in artifacts.items():
        links = fm.get("links") or {}
        for ltype, inverse in INVERSE.items():
            for target in as_list(links.get(ltype)):
                other = artifacts.get(target)
                if other is None:
                    continue  # already reported by rule 2
                if other.get("type") != fm.get("type"):
                    errors.append(f"{fm['_path']}: {ltype} -> {target} "
                                  f"crosses artifact types")
                back = as_list((other.get("links") or {}).get(inverse))
                if aid not in back:
                    errors.append(f"{fm['_path']}: {aid} {ltype} {target}, "
                                  f"but {target} lacks {inverse}: {aid}")

    # Rule 5: approved artifacts have no open conflicts
    for aid, fm in artifacts.items():
        if fm.get("status") != "approved":
            continue
        for cfl in as_list((fm.get("links") or {}).get("conflicts-with")):
            if artifacts.get(cfl, {}).get("status") != "resolved":
                errors.append(f"{fm['_path']}: approved {aid} links "
                              f"unresolved conflict {cfl}")

    if errors:
        print(f"FAIL: {len(errors)} violation(s) across "
              f"{len(artifacts)} artifacts\n")
        for e in errors:
            print(f"  {e}")
        return 1
    print(f"OK: {len(artifacts)} artifacts, graph is sound")
    return 0


if __name__ == "__main__":
    sys.exit(main())
