#!/usr/bin/env python3
"""Validate a Groundwork artifact graph.

Usage: python3 check_links.py [--uses-advisory] [project_root]
(default root: cwd)

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
  8. Body cross-references are bare artifact IDs and resolve
     (DEC-0242): every bare artifact ID in body prose (outside code
     spans/fenced blocks) resolves to an existing artifact; an inline
     markdown link targeting an artifact file is a violation — use the
     bare ID; remaining relative links (non-artifact files) must
     resolve.
  9. In component docs, every design-element heading is directly
     followed by an `Implements:` line naming >=1 story by bare ID;
     each referenced story's body references the component doc back
     (reciprocity with its Component Impact).
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
     IDs, required fields per status (Condition/Subscribers/Cites; plus
     Fired/Retired naming a decision), resolvable IDs and relative
     links, and subscriber lines each carrying an artifact-ID target
     plus a `(per DEC)` citation. On armed entries every subscribed
     artifact is `deferred` and there is at least one subscriber
     (DEC-0109, DEC-0110).
 15. Derived-work completeness (DEC-0246): every artifact whose
     `derives-from` names a business goal or epic is referenced by
     bare ID in that parent's body prose.
 16. Cites/prose synchronization (DEC-0247), on goals, epics, stories,
     spikes, and components: every `cites:` DEC appears in body prose
     (no dead cites), and every DEC referenced in body prose appears
     in `cites:` or a frontmatter link (no missing cites).
 17. Impactor-side impact prose (DEC-0249): an artifact carrying an
     `impacts` edge references each impact target in its body prose.
 18. Session mention completeness (DEC-0250): every artifact in a
     session's `relates-to` is referenced in the session's body prose
     (for closed sessions, appended as Post-Close Enrichment per
     DEC-0248).
 19. Overview presence, cap, and resolution (DEC-0284, DEC-0286,
     DEC-0287): every artifact's frontmatter contains a non-empty
     `overview:` field of at most 250 words, and every bare artifact
     ID inside it resolves (DEC-0242 extended to the overview
     surface). Faithfulness to the body is a process obligation
     (DEC-0288), not checked here.
 20. Typed element dependencies (DEC-0299, DEC-0306, DEC-0309;
     SPEC-design-elements): every design element carries a `Uses:`
     line before its contract items — `Uses: none`, or comma-separated
     `Target.K-n (interface|implementation|test)` entries (omitted
     qualifier means interface; a bare element name without an item is
     valid, e.g. a test double). Every target resolves to an element
     defined in some component's Design Elements section and, when
     item-qualified, to an item that element defines (`..` ranges
     expanded). A component's cross-component Uses: edges must project
     exactly onto its frontmatter depends-on, both directions
     (DEC-0309). Docs with no Design Elements section are skipped.
     With --uses-advisory, rule-20 findings are demoted to warnings
     (exit 0) — an authoring-time aid only; all other rules keep their
     normal severity.
 21. Duplicate sibling headings (SES-0072, from IDEA-0041/IDEA-0028):
     no artifact body repeats a same-level heading text under the same
     parent heading (outside code) — the edit-section phantom-heading
     signature. Applies to every artifact, drafts included.
 22. Placeholder text in ratified artifacts (SES-0072): an artifact
     whose status is approved, accepted, or closed contains no
     standalone TBD/TODO/FIXME line and no unallocated ID placeholder
     (e.g. `SES-XXXX`) outside code. Drafts may stub freely; quote
     placeholders in backticks to mention them legitimately.
 23. Produced-decision back-links (SES-0072): every decision whose
     derives-from names a session appears in that session's
     links.relates-to; deriving from a spike, in the spike's cites.
 24. Body H1 identity (SES-0072): a body H1, when present, must not
     carry an unallocated ID placeholder, and when it leads with an
     artifact ID that ID is the artifact's own.

Ideas (IDEA-*, docs/ideas/, DEC-0258) are pre-classification captures:
they are exempt from goal tracing (rule 3) and never carry release
fields; their statuses are captured | taken-up | declined.

Exit code 0 = graph is sound; 1 = violations; 2 = setup problem.

This file is installed into Groundwork projects as tools/check_links.py.
It requires PyYAML (`pip install pyyaml`).
"""

import re
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("check_links.py requires PyYAML: pip install pyyaml")
    sys.exit(2)

LINK_TYPES = {"derives-from", "satisfies", "depends-on", "conflicts-with",
              "supersedes", "relates-to", "impacts", "impacted-by"}
ID_RE = re.compile(r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}$")
PREFIX_FOR_TYPE = {
    "business-goal": "BG", "epic": "EP", "story": "ST", "spike": "SP",
    "component": "CMP", "session": "SES", "decision": "DEC",
    "conflict": "CFL", "consolidation": "CON", "change-proposal": "CP",
    "idea": "IDEA",
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
BARE_ID_RE = re.compile(
    r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}\b")
EXTERNAL_TARGET = ("http://", "https://", "mailto:", "#")
RELEASE_SCOPED_TYPES = {"story", "epic", "spike"}
RELEASE_RE = re.compile(r"^(0|[1-9]\d*)(\.(0|[1-9]\d*)){0,2}$")
RELEASES_HEADER_RE = re.compile(r"^\*\*Releases:\*\*\s*$", re.MULTILINE)
RELEASE_ITEM_RE = re.compile(r"^-\s+`([^`]+)`(\s*\(current\))?")
TRIGGER_HEAD_RE = re.compile(r"^## (TRG-\d{4}) \((armed|fired|retired)\)\s*$")
TRIGGER_ANY_HEAD_RE = re.compile(r"^## .*TRG", re.IGNORECASE)
ARTIFACT_FILE_RE = re.compile(
    r"(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}-[^/\s]*\.md$")
USES_QUALIFIERS = {"interface", "implementation", "test"}
ITEM_DEF_RE = re.compile(
    r"^[ \t]*-[ \t]+`(?P<el>[A-Za-z]\w*)\.(?P<a>[A-Z]{1,3}-\d+)"
    r"(?:\.\.(?P<b>[A-Z]{1,3}-\d+))?`", re.MULTILINE)
USES_ENTRY_RE = re.compile(
    r"^(?P<el>[A-Za-z]\w*)(?:\.(?P<item>[A-Z]{1,3}-\d+))?"
    r"(?:\s*\((?P<qual>[^)]*)\))?$")
ANY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
PLACEHOLDER_LINE_RE = re.compile(r"^(?:TBD|TODO|FIXME)\s*[.!:]?$",
                                 re.IGNORECASE)
ID_PLACEHOLDER_RE = re.compile(
    r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-XXXX\b")
BODY_H1_ID_RE = re.compile(
    r"^#\s+((?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4})\b")
RATIFIED_STATUSES = {"approved", "accepted", "closed"}

# Rule 25 (SES-0077, DEC-0402): typed frontmatter field schema — a hand
# copy of gw_write.py's FIELD_SCHEMA (keep in sync; `release` is omitted
# here because rule 10 validates it more strongly against the declared
# release list). WARN severity until the DEC-0402 promotion decision.
# Rule 26 (SES-0077): required-section skeleton per type — a hand copy
# of gw_write.py's REQUIRED_SECTIONS (keep in sync).
REQUIRED_SECTIONS = {
    "business-goal": ["Problem", "Intent", "Outcomes & Success Criteria",
                      "Scope", "Constraints", "Stakeholders & Roles",
                      "Conflicts & Tensions", "Derived Work"],
    "epic": ["Summary", "Why (Goal Alignment)", "Scope", "Domain Context",
             "Interfaces & Contracts to Define", "Risks & Open Questions",
             "Derived Work"],
    "story": ["Summary", "Acceptance Criteria", "Component Impact",
              "Out of Scope", "Notes for Implementers"],
    "spike": ["Question", "Why It Blocks", "Method", "Findings",
              "Resulting Decisions"],
    "component": ["Purpose", "Ubiquitous Language", "Design Elements",
                  "Component Invariants", "Implementation Guidance",
                  "Dependencies", "Acceptance & Test Expectations",
                  "Out of Scope"],
    "session": ["Purpose", "Transcript", "Decisions Produced",
                "Conflicts Raised"],
    "decision": ["Context", "Decision", "Rationale",
                 "Alternatives Considered", "Implications"],
    "conflict": ["The Tension", "Party Intents", "Mediation Record",
                 "Resolution"],
    "change-proposal": ["Proposed Change", "Context", "Triage Outcome"],
    "idea": ["The Idea", "Spark Context", "Disposition"],
    "consolidation": ["Path Covered", "Consolidated Content", "Omissions"],
}

# Sections the SPEC marks optional — exempt from the skeleton guard
# (SES-0077 item 9: stories' Notes for Implementers is "optional
# context", per the system reference).
OPTIONAL_SECTIONS = {"story": {"Notes for Implementers"}}

DATE_VALUE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FIELD_SCHEMA = {
    "transcript-fidelity": ({"session"}, "enum",
                            {"verbatim", "reconstructed"}),
    "participant": ({"session"}, "scalar", None),
    "participant-role": ({"session"}, "scalar", None),
    "facilitator": ({"session"}, "scalar", None),
    "decided-by": ({"decision"}, "scalar", None),
    "decided-on": ({"decision"}, "date", None),
    "accepted-in": ({"decision"}, "scalar", None),
    "source-span": ({"decision"}, "scalar", None),
    "timebox": ({"spike"}, "scalar", None),
    "sponsor": ({"business-goal"}, "scalar", None),
    "approved-by": (None, "scalar", None),
    "approved-on": (None, "date", None),
    "created": (None, "date", None),
}


def validate_field(atype, key, value):
    """One frontmatter field against FIELD_SCHEMA (DEC-0402); error
    string or None (unknown fields stay open for extension)."""
    spec = FIELD_SCHEMA.get(key)
    if spec is None:
        return None
    types, kind, enum = spec
    if types is not None and atype not in types:
        return (f"field {key!r} applies to {sorted(types)}, not "
                f"{atype!r} (rule 25, DEC-0402)")
    if isinstance(value, (list, dict)):
        return (f"field {key!r} must be a single scalar value, got a "
                f"{type(value).__name__} (rule 25, DEC-0402)")
    v = str(value).strip().strip("\"'")
    if kind == "scalar" and v.startswith("["):
        return (f"field {key!r} must be a single scalar value, got a "
                f"list (rule 25, DEC-0402)")
    if kind == "enum" and v not in enum:
        return (f"field {key!r} must be one of {sorted(enum)}, got "
                f"{v!r} (rule 25, DEC-0402)")
    if kind == "date" and not DATE_VALUE_RE.match(v):
        return (f"field {key!r} must be an absolute date YYYY-MM-DD, "
                f"got {v!r} (rule 25, DEC-0402)")
    return None


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
    argv = [a for a in sys.argv[1:] if a != "--uses-advisory"]
    uses_advisory = "--uses-advisory" in sys.argv[1:]
    root = Path(argv[0]).resolve() if argv else Path.cwd()
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

    # Rule 19: overview presence and word cap (DEC-0284, DEC-0286,
    # DEC-0287).
    for aid, fm in artifacts.items():
        overview = fm.get("overview")
        if not isinstance(overview, str) or not overview.strip():
            errors.append(f"{fm['_path']}: {aid} has no non-empty "
                          f"overview: frontmatter field (DEC-0284)")
        elif len(overview.split()) > 250:
            errors.append(f"{fm['_path']}: {aid} overview is "
                          f"{len(overview.split())} words (max 250, "
                          f"DEC-0286)")
        else:
            for ref in BARE_ID_RE.findall(overview):
                if ref not in artifacts:
                    errors.append(f"{fm['_path']}: {aid} overview "
                                  f"references unknown artifact {ref} "
                                  f"(DEC-0242, DEC-0287)")

    # Rules 21-22 body walker: lines outside fenced code, inline code
    # blanked — quoting placeholders/headings in backticks is legitimate.
    def body_prose_lines(body):
        in_code = False
        for n, line in enumerate((body or "").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if not in_code:
                yield n, INLINE_CODE_RE.sub("", line)

    # Rule 21: duplicate sibling headings (SES-0072)
    for aid, fm in artifacts.items():
        stack, seen = [], {}
        for _, line in body_prose_lines(fm["_body"]):
            m = ANY_HEADING_RE.match(line.rstrip())
            if not m:
                continue
            level, text = len(m.group(1)), m.group(2)
            while stack and stack[-1][0] >= level:
                stack.pop()
            key = (tuple(t for _, t in stack), level, text)
            seen[key] = seen.get(key, 0) + 1
            stack.append((level, text))
        for (_, level, text), n in sorted(seen.items()):
            if n > 1:
                errors.append(f"{fm['_path']}: duplicate sibling heading "
                              f"{'#' * level} {text!r} x{n} — phantom-"
                              f"heading signature (rule 21)")

    # Rule 22: placeholder text in ratified artifacts (SES-0072)
    for aid, fm in artifacts.items():
        if fm.get("status") not in RATIFIED_STATUSES:
            continue
        for n, line in body_prose_lines(fm["_body"]):
            s = line.strip()
            if PLACEHOLDER_LINE_RE.match(s):
                errors.append(f"{fm['_path']}: ratified {aid} line {n} is "
                              f"placeholder text {s!r} (rule 22)")
            for tok in ID_PLACEHOLDER_RE.findall(line):
                errors.append(f"{fm['_path']}: ratified {aid} line {n} "
                              f"carries unallocated ID placeholder {tok} "
                              f"(rule 22)")

    # Rule 23: produced-decision back-links (SES-0072)
    for aid, fm in artifacts.items():
        if fm.get("type") != "decision":
            continue
        for p in as_list((fm.get("links") or {}).get("derives-from")):
            parent = artifacts.get(p)
            if parent is None:
                continue  # unresolved target: rule 2
            if parent.get("type") == "session":
                back = as_list((parent.get("links") or {}).get("relates-to"))
                if aid not in back:
                    errors.append(f"{parent['_path']}: session produced "
                                  f"{aid} (its derives-from) but "
                                  f"relates-to omits it (rule 23)")
            elif parent.get("type") == "spike":
                if aid not in as_list(parent.get("cites")):
                    errors.append(f"{parent['_path']}: spike produced "
                                  f"{aid} but cites: omits it (rule 23)")

    # Rule 24: body H1 identity (SES-0072)
    for aid, fm in artifacts.items():
        first = (fm["_body"] or "").lstrip("\n").split("\n", 1)[0]
        if not first.startswith("# "):
            continue
        if ID_PLACEHOLDER_RE.search(first):
            errors.append(f"{fm['_path']}: body H1 carries an unallocated "
                          f"ID placeholder (rule 24)")
            continue
        m = BODY_H1_ID_RE.match(first)
        if m and m.group(1) != aid:
            errors.append(f"{fm['_path']}: body H1 names {m.group(1)}, "
                          f"not {aid} (rule 24)")

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

    # Rule 25 (DEC-0402): typed frontmatter fields match the schema.
    # Promoted WARN -> FAIL at SES-0077: the rollout sweep found zero
    # legacy violations, so the rule blocks from day one.
    for aid, fm in artifacts.items():
        atype = str(fm.get("type"))
        for k, v in fm.items():
            if k.startswith("_"):
                continue
            err = validate_field(atype, k, v)
            if err:
                errors.append(f"{fm['_path']}: {aid} {err}")

    # Rule 26 (SES-0077): required-section presence per type — WARN
    # until the rollout sweep decides promotion.
    for aid, fm in artifacts.items():
        req = REQUIRED_SECTIONS.get(str(fm.get("type")), [])
        if not req:
            continue
        have = set()
        for _, ln in body_prose_lines(fm.get("_body") or ""):
            m = ANY_HEADING_RE.match(ln.rstrip())
            if m and len(m.group(1)) == 2:
                have.add(m.group(2))
        optional = OPTIONAL_SECTIONS.get(str(fm.get("type")), set())
        missing = [s for s in req if s not in have and s not in optional]
        if missing:
            warnings.append(f"{fm['_path']}: {aid} missing required "
                            f"section(s) {missing} (rule 26)")
    story_covered = set()
    for aid, fm in artifacts.items():
        if fm.get("type") != "component":
            continue
        section = DESIGN_ELEMENTS_RE.search(fm.get("_body") or "")
        if not section:
            continue
        sec_text = section.group(1)
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
            story_ids = [s for s in dict.fromkeys(BARE_ID_RE.findall(para))
                         if s.startswith("ST-")]
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
                st_prose = INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub(
                    "", st["_body"] or ""))
                back = aid in BARE_ID_RE.findall(st_prose)
                if not back:
                    errors.append(f"{fm['_path']}: element {name} "
                                  f"implements {sid}, but {sid}'s Component "
                                  f"Impact does not reference {aid}")
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

    # Rule 20: typed Uses: lines and depends-on projection (DEC-0299,
    # DEC-0306, DEC-0309; SPEC-design-elements). Findings are demoted
    # to warnings under --uses-advisory (authoring aid; error is the
    # default so the rule cannot ship unarmed).
    uses_findings = warnings if uses_advisory else errors
    element_owner = {}    # element name -> [owning CMP ids]
    element_items = {}    # (cmp, name) -> set of item ids (ranges expanded)
    element_blocks = {}   # (cmp, name) -> block text
    for aid, fm in artifacts.items():
        if fm.get("type") != "component":
            continue
        section = DESIGN_ELEMENTS_RE.search(fm.get("_body") or "")
        if not section:
            continue
        sec_text = section.group(1)
        heads = list(ELEMENT_HEADING_RE.finditer(sec_text))
        for i, h in enumerate(heads):
            name = h.group(1)
            end = heads[i + 1].start() if i + 1 < len(heads) else len(sec_text)
            block = sec_text[h.end():end]
            element_owner.setdefault(name, []).append(aid)
            items = set()
            for m in ITEM_DEF_RE.finditer(block):
                if m.group("el") != name:
                    continue
                a, b = m.group("a"), m.group("b")
                if b is None:
                    items.add(a)
                    continue
                pa, na = a.rsplit("-", 1)
                pb, nb = b.rsplit("-", 1)
                if pa == pb and int(na) <= int(nb):
                    items.update(f"{pa}-{n}"
                                 for n in range(int(na), int(nb) + 1))
                else:
                    items.update((a, b))
            element_items[(aid, name)] = items
            element_blocks[(aid, name)] = block
    cross_targets = {}    # cmp id -> set of provider cmp ids
    for (aid, name), block in sorted(element_blocks.items()):
        fmp = artifacts[aid]["_path"]
        lines = block.splitlines()
        uses_idx = [i for i, ln in enumerate(lines)
                    if ln.strip().startswith("Uses:")]
        if not uses_idx:
            uses_findings.append(f"{fmp}: element {name} lacks a Uses: "
                                 f"line (per DEC-0299)")
            continue
        if len(uses_idx) > 1:
            uses_findings.append(f"{fmp}: element {name} has multiple "
                                 f"Uses: lines")
            continue
        i0 = uses_idx[0]
        first_bullet = next(
            (i for i, ln in enumerate(lines)
             if ln.lstrip().startswith("- `")), len(lines))
        if i0 > first_bullet:
            uses_findings.append(f"{fmp}: element {name} Uses: line must "
                                 f"precede its contract items")
        content_lines = [lines[i0].split("Uses:", 1)[1]]
        for ln in lines[i0 + 1:]:
            if not ln.strip() or ln.lstrip().startswith(("- ", "#")):
                break
            content_lines.append(ln)
        content = " ".join(p.strip() for p in content_lines).strip()
        if content == "none":
            continue
        if not content:
            uses_findings.append(f"{fmp}: element {name} Uses: line is "
                                 f"empty (write 'Uses: none')")
            continue
        for raw in content.split(","):
            entry = raw.strip().strip("`").strip()
            m = USES_ENTRY_RE.match(entry)
            if not m:
                uses_findings.append(f"{fmp}: element {name} Uses: entry "
                                     f"{raw.strip()!r} is malformed")
                continue
            qual = m.group("qual")
            if qual is not None and qual not in USES_QUALIFIERS:
                uses_findings.append(
                    f"{fmp}: element {name} Uses: entry {entry!r} has "
                    f"unknown qualifier {qual!r} (closed set: "
                    f"{sorted(USES_QUALIFIERS)})")
            tgt = m.group("el")
            owners = element_owner.get(tgt, [])
            if not owners:
                uses_findings.append(f"{fmp}: element {name} Uses: target "
                                     f"{tgt!r} resolves to no element")
                continue
            if len(owners) > 1:
                uses_findings.append(
                    f"{fmp}: element {name} Uses: target {tgt!r} is "
                    f"ambiguous (defined in {', '.join(sorted(owners))})")
                continue
            owner = owners[0]
            item = m.group("item")
            if item and item not in element_items[(owner, tgt)]:
                uses_findings.append(
                    f"{fmp}: element {name} Uses: target {tgt}.{item} — "
                    f"{tgt} defines no item {item}")
            if owner != aid:
                cross_targets.setdefault(aid, set()).add(owner)
    has_elements = {cmp for cmp, _ in element_blocks}
    for aid, fm in artifacts.items():
        if fm.get("type") != "component" or aid not in has_elements:
            continue
        declared = set(as_list((fm.get("links") or {}).get("depends-on")))
        derived = cross_targets.get(aid, set())
        for t in sorted(derived - declared):
            uses_findings.append(f"{fm['_path']}: element Uses: edges "
                                 f"reach {t} but depends-on omits it "
                                 f"(per DEC-0309)")
        for t in sorted(declared - derived):
            uses_findings.append(f"{fm['_path']}: depends-on {t} is "
                                 f"supported by no element Uses: edge "
                                 f"(per DEC-0309)")

    # Body prose bare-ID mentions, shared by rules 8 and 15-18
    mentions = {}
    for aid, fm in artifacts.items():
        prose = INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("",
                                                          fm["_body"] or ""))
        fm["_prose"] = prose
        mentions[aid] = set(BARE_ID_RE.findall(MD_LINK_RE.sub("", prose)))

    # Rule 8: body cross-references are bare IDs and resolve (DEC-0242)
    for aid, fm in artifacts.items():
        prose = fm["_prose"]
        base = (root / fm["_path"]).parent
        for text, target in MD_LINK_RE.findall(prose):
            if target.startswith(EXTERNAL_TARGET):
                continue
            plain = target.split("#")[0]
            if ARTIFACT_FILE_RE.search(plain):
                errors.append(f"{fm['_path']}: inline artifact link "
                              f"[{text}]({target}) — use the bare ID "
                              f"(per DEC-0242)")
            elif not (base / plain).resolve().exists():
                errors.append(f"{fm['_path']}: link [{text}]({target}) "
                              f"does not resolve")
        for b in sorted(mentions[aid]):
            if b not in artifacts:
                errors.append(f"{fm['_path']}: cross-reference {b} does "
                              f"not resolve to any artifact")

    # Rule 15: derived-work completeness (DEC-0246)
    for aid, fm in artifacts.items():
        for p in as_list((fm.get("links") or {}).get("derives-from")):
            parent = artifacts.get(p)
            if parent is None:
                continue  # unresolved target: rule 2
            if parent.get("type") in ("business-goal", "epic") \
                    and aid not in mentions[p]:
                errors.append(f"{parent['_path']}: body does not reference "
                              f"derived child {aid} (per DEC-0246)")

    # Rule 16: cites/prose synchronization (DEC-0247)
    CITES_SYNC_TYPES = {"business-goal", "epic", "story", "spike",
                        "component"}
    for aid, fm in artifacts.items():
        if fm.get("type") not in CITES_SYNC_TYPES:
            continue
        cited = set(as_list(fm.get("cites")))
        for c in sorted(cited):
            if c in artifacts and c not in mentions[aid]:
                errors.append(f"{fm['_path']}: dead cite {c} — cited in "
                              f"frontmatter, never referenced in body "
                              f"prose (per DEC-0247)")
        linked = set()
        for v in (fm.get("links") or {}).values():
            linked |= set(as_list(v))
        for b in sorted(mentions[aid]):
            if b.startswith("DEC-") and b in artifacts \
                    and b not in cited and b not in linked:
                errors.append(f"{fm['_path']}: body references {b} but "
                              f"cites: omits it (per DEC-0247)")

    # Rule 17: impactor-side impact prose (DEC-0249)
    for aid, fm in artifacts.items():
        for t in as_list((fm.get("links") or {}).get("impacts")):
            if t in artifacts and t not in mentions[aid]:
                errors.append(f"{fm['_path']}: impacts {t} but body prose "
                              f"never explains the impact (per DEC-0249)")

    # Rule 18: session mention completeness (DEC-0250)
    for aid, fm in artifacts.items():
        if fm.get("type") != "session":
            continue
        for t in as_list((fm.get("links") or {}).get("relates-to")):
            if t in artifacts and t not in mentions[aid]:
                errors.append(f"{fm['_path']}: session relates-to {t} but "
                              f"body never references it (per DEC-0250)")

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
            fields = {f for f in ("Condition", "Subscribers", "Cites")
                      if f"**{f}:**" in block}
            for f in ("Condition", "Subscribers", "Cites"):
                if f not in fields:
                    errors.append(f"docs/TRIGGERS.md: {tid} lacks "
                                  f"**{f}:** field")
            tstatus = status_of[tid]
            # Subscriber lines: target link + per-DEC citation; on armed
            # entries the target must be a deferred artifact (rule 14)
            sub_lines = []
            if "**Subscribers:**" in block:
                seg = block.split("**Subscribers:**", 1)[1]
                for ln in seg.splitlines():
                    if ln.startswith("- "):
                        sub_lines.append(ln)
                    elif ln.startswith("**"):
                        break
            if "Subscribers" in fields and not sub_lines:
                errors.append(f"docs/TRIGGERS.md: {tid} has an empty "
                              f"**Subscribers:** list")
            for ln in sub_lines:
                ids_in = BARE_ID_RE.findall(ln)
                if not ids_in:
                    errors.append(f"docs/TRIGGERS.md: {tid} subscriber "
                                  f"line has no artifact-ID target: {ln!r}")
                    continue
                if not re.search(r"\(per DEC-\d{4}", ln):
                    errors.append(f"docs/TRIGGERS.md: {tid} subscriber "
                                  f"line lacks a (per DEC) citation: "
                                  f"{ln!r}")
                if tstatus == "armed":
                    aid = ids_in[0]
                    if aid not in artifacts:
                        continue  # unresolved ID reported separately
                    if artifacts[aid].get("status") != "deferred":
                        errors.append(
                            f"docs/TRIGGERS.md: {tid} (armed) subscribes "
                            f"{aid}, whose status is "
                            f"{artifacts[aid].get('status')!r} — armed "
                            f"triggers may only subscribe deferred "
                            f"artifacts")
            if tstatus in ("fired", "retired"):
                marker = tstatus.capitalize()
                seg = block.split(f"**{marker}:**", 1)
                if len(seg) < 2:
                    errors.append(f"docs/TRIGGERS.md: {tid} is {tstatus} "
                                  f"but lacks **{marker}:** field")
                elif not re.search(r"DEC-\d{4}", seg[1].split("**", 1)[0]):
                    errors.append(f"docs/TRIGGERS.md: {tid} **{marker}:** "
                                  f"names no decision")
        reg_prose = INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("", text))
        for text_, target in MD_LINK_RE.findall(reg_prose):
            if target.startswith(EXTERNAL_TARGET):
                continue
            plain = target.split("#")[0]
            if ARTIFACT_FILE_RE.search(plain):
                errors.append(f"docs/TRIGGERS.md: inline artifact link "
                              f"[{text_}]({target}) — use the bare ID "
                              f"(per DEC-0242)")
            elif not (docs / plain).resolve().exists():
                errors.append(f"docs/TRIGGERS.md: link [{text_}]({target}) "
                              f"does not resolve")
        for b in sorted(set(BARE_ID_RE.findall(
                MD_LINK_RE.sub("", reg_prose)))):
            if b not in artifacts:
                errors.append(f"docs/TRIGGERS.md: cross-reference {b} does "
                              f"not resolve to any artifact")

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
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Downstream consumer (head, less) closed the pipe — not an
        # error (SES-0077, DEC-0404). Re-point stdout so interpreter
        # shutdown doesn't re-raise, and exit clean.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)
