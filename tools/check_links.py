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
  7. Component design elements use the closed type enum (entity, value,
     service, event, protocol) — both `component-type:` frontmatter and
     `### <Name> (<type>)` headings in Design Elements sections — and
     element names are unique within a doc.
  8. Body cross-references are clickable and resolve: relative links in
     bodies point at existing files; a link whose text begins with an
     artifact ID targets that artifact's file; bare artifact IDs in body
     prose (outside code spans/fenced blocks, excluding the artifact's
     own ID) are violations.
  9. In component docs, every design-element heading is directly
     followed by an `Implements:` line naming >=1 story via resolvable
     markdown links; each referenced story's body links the component
     doc back (reciprocity with its Component Impact).
 10. (audit, non-blocking) Approved stories with no referencing design
     element are reported as design-coverage warnings.
 11. `deferred` status and `release:` fields appear only on stories,
     epics, and spikes; a `release:` value is the reserved `backlog` or a
     SemVer prefix (`1`, `1.2`, `1.2.3` — no leading zeroes, no v prefix)
     and must exactly match a release declared in a business goal's
     `**Releases:**` list.
 12. Deferred/release consistency: a deferred artifact has an effective
     release (own field, or its parent epic's) that is not a current
     release; an artifact whose effective release is non-current is
     deferred.
 13. (audit, non-blocking) A design element whose Implements line
     references only deferred stories is reported as a warning.
 14. The trigger registry (docs/TRIGGERS.md), when present, is
     well-formed: headings `## TRG-nnnn (armed|fired|retired)`, unique
     IDs, required fields per status (Condition/Consequence/Cites; plus
     Fired/Retired with a decision link), and resolvable relative links.

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
ELEMENT_TYPES = {"entity", "value", "service", "event", "protocol"}
ELEMENT_HEADING_RE = re.compile(r"^###\s+(\S+)\s+\(([^)]*)\)\s*$",
                                re.MULTILINE)
DESIGN_ELEMENTS_RE = re.compile(r"^## Design Elements\s*$(.*?)(?=^## |\Z)",
                                re.MULTILINE | re.DOTALL)
FENCED_CODE_RE = re.compile(r"```.*?(?:```|\Z)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BARE_ID_RE = re.compile(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP)-\d{4}\b")
EXTERNAL_TARGET = ("http://", "https://", "mailto:", "#")
RELEASE_SCOPED_TYPES = {"story", "epic", "spike"}
RELEASE_RE = re.compile(r"^(0|[1-9]\d*)(\.(0|[1-9]\d*)){0,2}$")
RELEASES_HEADER_RE = re.compile(r"^\*\*Releases:\*\*\s*$", re.MULTILINE)
RELEASE_ITEM_RE = re.compile(r"^-\s+`([^`]+)`(\s*\(current\))?")
TRIGGER_HEAD_RE = re.compile(r"^## (TRG-\d{4}) \((armed|fired|retired)\)\s*$")
TRIGGER_ANY_HEAD_RE = re.compile(r"^## .*TRG", re.IGNORECASE)


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, None, "missing YAML frontmatter"
    try:
        return yaml.safe_load(m.group(1)), text[m.end():], None
    except yaml.YAMLError as e:
        return None, None, f"unparseable frontmatter: {e}"


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
        if path.parent.name in SKIP_DIRS or path.name == "TRIGGERS.md":
            continue
        fm, body, err = parse_frontmatter(path)
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
        fm["_body"] = body
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

    # Rule 7: component design elements use the closed type enum
    for aid, fm in artifacts.items():
        if fm.get("type") != "component":
            continue
        ctype = fm.get("component-type")
        if ctype is not None and ctype not in ELEMENT_TYPES:
            errors.append(f"{fm['_path']}: component-type {ctype!r} not one "
                          f"of {sorted(ELEMENT_TYPES)}")
        section = DESIGN_ELEMENTS_RE.search(fm.get("_body") or "")
        if not section:
            continue  # drafts may not have the section yet
        seen = set()
        for name, etype in ELEMENT_HEADING_RE.findall(section.group(1)):
            if etype not in ELEMENT_TYPES:
                errors.append(f"{fm['_path']}: element {name} has unknown "
                              f"type {etype!r} (closed enum: "
                              f"{sorted(ELEMENT_TYPES)})")
            if name in seen:
                errors.append(f"{fm['_path']}: duplicate element name "
                              f"{name}")
            seen.add(name)

    # Rules 11-12: release scoping and deferred consistency
    declared, current = set(), set()
    for aid, fm in artifacts.items():
        if fm.get("type") != "business-goal":
            continue
        body = fm.get("_body") or ""
        header = RELEASES_HEADER_RE.search(body)
        if not header:
            continue
        for line in body[header.end():].lstrip("\n").splitlines():
            item = RELEASE_ITEM_RE.match(line)
            if item is None:
                if line.strip() and not line.startswith(" "):
                    break  # end of the Releases list
                continue
            value = item.group(1)
            declared.add(value)
            if item.group(2):
                current.add(value)
            if not RELEASE_RE.match(value):
                errors.append(f"{fm['_path']}: declared release {value!r} "
                              f"is not a SemVer prefix")

    def own_release(fm):
        return None if fm.get("release") is None else fm.get("release")

    def effective_release(fm):
        if fm.get("release") is not None:
            return fm.get("release")
        for p in as_list((fm.get("links") or {}).get("derives-from")):
            parent = artifacts.get(p, {})
            if parent.get("type") == "epic" and \
                    parent.get("release") is not None:
                return parent.get("release")
        return None

    for aid, fm in artifacts.items():
        atype = fm.get("type")
        rel = own_release(fm)
        if fm.get("status") == "deferred" and \
                atype not in RELEASE_SCOPED_TYPES:
            errors.append(f"{fm['_path']}: status deferred is only valid "
                          f"on stories and epics")
        if rel is not None:
            if atype not in RELEASE_SCOPED_TYPES:
                errors.append(f"{fm['_path']}: release: is only valid on "
                              f"stories and epics")
                continue
            if not isinstance(rel, str):
                errors.append(f"{fm['_path']}: release: {rel!r} must be a "
                              f"quoted string (YAML parsed it as "
                              f"{type(rel).__name__})")
                continue
            if rel != "backlog" and not RELEASE_RE.match(rel):
                errors.append(f"{fm['_path']}: release: {rel!r} is not "
                              f"'backlog' or a SemVer prefix")
                continue
            if rel != "backlog" and rel not in declared:
                errors.append(f"{fm['_path']}: release: {rel!r} matches no "
                              f"release declared in a business goal "
                              f"(declared: {sorted(declared) or 'none'})")
        if atype in RELEASE_SCOPED_TYPES:
            eff = effective_release(fm)
            eff_current = eff is None or eff in current
            if fm.get("status") == "deferred" and eff is None:
                errors.append(f"{fm['_path']}: deferred {aid} has no "
                              f"release: (own or parent epic's)")
            elif fm.get("status") == "deferred" and eff_current:
                errors.append(f"{fm['_path']}: deferred {aid} targets "
                              f"current release {eff!r}")
            elif fm.get("status") != "deferred" and not eff_current \
                    and isinstance(eff, str):
                errors.append(f"{fm['_path']}: {aid} targets non-current "
                              f"release {eff!r} but is not deferred")

    # Rule 9: element Implements lines — presence, stories, reciprocity
    warnings = []
    story_covered = set()
    for aid, fm in artifacts.items():
        if fm.get("type") != "component":
            continue
        section = DESIGN_ELEMENTS_RE.search(fm.get("_body") or "")
        if not section:
            continue
        sec_text = section.group(1)
        cmp_path = (root / fm["_path"]).resolve()
        heads = list(ELEMENT_HEADING_RE.finditer(sec_text))
        for i, h in enumerate(heads):
            name = h.group(1)
            end = heads[i + 1].start() if i + 1 < len(heads) else len(sec_text)
            block = sec_text[h.end():end].lstrip("\n")
            if not block.startswith("Implements:"):
                errors.append(f"{fm['_path']}: element {name} lacks an "
                              f"Implements: line directly under its heading")
                continue
            para = block.split("\n\n", 1)[0]
            story_ids = [text for text, _ in MD_LINK_RE.findall(para)
                         if ID_RE.match(text) and text.startswith("ST-")]
            if not story_ids:
                errors.append(f"{fm['_path']}: element {name} Implements "
                              f"line names no stories")
                continue
            for sid in story_ids:
                st = artifacts.get(sid)
                if st is None or st.get("type") != "story":
                    errors.append(f"{fm['_path']}: element {name} "
                                  f"implements {sid}, which is not a story")
                    continue
                st_base = (root / st["_path"]).parent
                back = any(
                    (st_base / tgt.split("#")[0]).resolve() == cmp_path
                    for _, tgt in MD_LINK_RE.findall(st["_body"] or "")
                    if not tgt.startswith(EXTERNAL_TARGET))
                if not back:
                    errors.append(f"{fm['_path']}: element {name} "
                                  f"implements {sid}, but {sid}'s Component "
                                  f"Impact does not link {aid}")
                story_covered.add(sid)
            # Rule 13 (audit): element motivated only by deferred stories
            statuses = [artifacts.get(sid, {}).get("status")
                        for sid in story_ids if sid in artifacts]
            if statuses and all(s == "deferred" for s in statuses):
                warnings.append(f"{fm['_path']}: element {name} implements "
                                f"only deferred stories")

    # Rule 10 (audit): approved stories uncovered by any element
    for aid, fm in artifacts.items():
        if fm.get("type") == "story" and fm.get("status") == "approved" \
                and aid not in story_covered:
            warnings.append(f"{fm['_path']}: approved story {aid} has no "
                            f"referencing design element (coverage gap)")

    # Rule 8: body cross-references are clickable and resolve
    for aid, fm in artifacts.items():
        prose = INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("",
                                                          fm["_body"] or ""))
        base = (root / fm["_path"]).parent
        for text, target in MD_LINK_RE.findall(prose):
            if target.startswith(EXTERNAL_TARGET):
                continue
            dest = (base / target.split("#")[0]).resolve()
            tid = BARE_ID_RE.match(text)
            if not dest.exists():
                errors.append(f"{fm['_path']}: link [{text}]({target}) "
                              f"does not resolve")
            elif tid and not dest.name.startswith(tid.group(0) + "-"):
                errors.append(f"{fm['_path']}: link [{text}]({target}) "
                              f"targets a different artifact")
        bare = {b for b in BARE_ID_RE.findall(MD_LINK_RE.sub("", prose))
                if b != aid}
        for b in sorted(bare):
            errors.append(f"{fm['_path']}: bare cross-reference {b} in "
                          f"prose — must be a markdown link")

    # Rule 14: trigger registry well-formedness
    reg = docs / "TRIGGERS.md"
    if reg.exists():
        text = reg.read_text(encoding="utf-8")
        seen_trg, status_of = set(), {}
        blocks = {}
        current = None
        for line in text.splitlines():
            m = TRIGGER_HEAD_RE.match(line)
            if m:
                tid, tstatus = m.group(1), m.group(2)
                if tid in seen_trg:
                    errors.append(f"docs/TRIGGERS.md: duplicate id {tid}")
                seen_trg.add(tid)
                status_of[tid] = tstatus
                blocks[tid] = []
                current = tid
                continue
            if TRIGGER_ANY_HEAD_RE.match(line):
                errors.append(f"docs/TRIGGERS.md: malformed trigger "
                              f"heading {line.strip()!r}")
                current = None
                continue
            if line.startswith("## "):
                current = None
                continue
            if current is not None:
                blocks[current].append(line)
        for tid, lines in blocks.items():
            block = "\n".join(lines)
            fields = {f for f in ("Condition", "Consequence", "Cites")
                      if f"**{f}:**" in block}
            for f in ("Condition", "Consequence", "Cites"):
                if f not in fields:
                    errors.append(f"docs/TRIGGERS.md: {tid} lacks "
                                  f"**{f}:** field")
            tstatus = status_of[tid]
            if tstatus in ("fired", "retired"):
                marker = tstatus.capitalize()
                seg = block.split(f"**{marker}:**", 1)
                if len(seg) < 2:
                    errors.append(f"docs/TRIGGERS.md: {tid} is {tstatus} "
                                  f"but lacks **{marker}:** field")
                elif not MD_LINK_RE.search(seg[1].split("**", 1)[0]):
                    errors.append(f"docs/TRIGGERS.md: {tid} **{marker}:** "
                                  f"lacks a decision link")
        for text_, target in MD_LINK_RE.findall(text):
            if target.startswith(EXTERNAL_TARGET):
                continue
            if not (docs / target.split("#")[0]).resolve().exists():
                errors.append(f"docs/TRIGGERS.md: link [{text_}]({target}) "
                              f"does not resolve")

    if warnings:
        print(f"WARN: {len(warnings)} audit warning(s)\n")
        for w in warnings:
            print(f"  {w}")
        print()
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
