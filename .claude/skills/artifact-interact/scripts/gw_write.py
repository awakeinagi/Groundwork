#!/usr/bin/env python3
"""Typed write operations over a Groundwork corpus (DEC-0312, DEC-0313).

The sole sanctioned write path for agents: every operation validates its
preconditions against the SPECs (docs/specs/SPEC-*.md are the normative
basis, DEC-0311), performs the write plus its bookkeeping atomically,
re-validates the artifacts it touched (DEC-0315), and prints a compact
result so the caller need not re-read the file (DEC-0314).

Operations (DEC-0313): create, append-turn, edit-section, delete-section,
set-status, add-link, add-cite, supersede, update-overview, apply
(JSON batch).

Structural guards (SES-0072, from IDEA-0041/IDEA-0028): section payloads
are body-only — content carrying a heading line at the target section's
level or higher is refused (phantom-heading defect); `edit-section
--occurrence N` and `delete-section` recover already-corrupted structure;
ratifying transitions (approved/accepted/closed) refuse bodies with
duplicate sibling headings or placeholder text; session close requires
complete frontmatter and either a produced decision or an explicit
--no-decisions-ok assessment.

Long content travels via stdin or --from-file, never shell arguments.
Errors name the sanctioned alternative where one exists.

Usage: python3 gw_write.py --root <project> <operation> ...
Exit codes: 0 ok, 1 refused/invalid request, 2 setup problem.
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import NoReturn

# Optional (SES-0072): frontmatter YAML validation at recheck time when
# PyYAML is present. Absent, the check skips silently — the write path
# stays stdlib-only (DEC-0317); the pre-commit checker (which requires
# PyYAML) remains the backstop.
try:
    import yaml as _yaml
except ImportError:  # pragma: no cover
    _yaml = None

# ---------------------------------------------------------------- model

TYPE_INFO = {  # type -> (prefix, directory)
    "business-goal": ("BG", "goals"),
    "epic": ("EP", "epics"),
    "story": ("ST", "stories"),
    "spike": ("SP", "spikes"),
    "component": ("CMP", "components"),
    "session": ("SES", "sessions"),
    "decision": ("DEC", "decisions"),
    "conflict": ("CFL", "conflicts"),
    "change-proposal": ("CP", "change-proposals"),
    "idea": ("IDEA", "ideas"),
    "consolidation": ("CON", "consolidations"),
}
PREFIX_TO_TYPE = {v[0]: k for k, v in TYPE_INFO.items()}

LINK_VOCAB = ("derives-from", "satisfies", "depends-on", "conflicts-with",
              "supersedes", "relates-to", "impacts", "impacted-by")
RECIPROCAL = {"impacts": "impacted-by", "impacted-by": "impacts"}

GATE_TYPES = {"business-goal", "epic", "story", "spike", "component",
              "consolidation"}
DEFERRABLE = {"story", "epic", "spike"}

# Legal status transitions per SPEC-artifact-common + reduced lifecycles.
GATE_TRANSITIONS = {
    "draft": {"in-refinement", "gated", "deferred"},
    "in-refinement": {"gated", "draft", "deferred"},
    "gated": {"approved", "in-refinement", "deferred"},
    "approved": {"stale", "superseded", "archived", "deferred"},
    "stale": {"approved"},
    "deferred": {"draft"},
}
REDUCED_TRANSITIONS = {
    "decision": {"proposed": {"accepted", "superseded"},
                 "accepted": {"superseded"}},
    "session": {"open": {"closed"}},
    "idea": {"captured": {"taken-up", "declined"}},
    "conflict": {"open": {"mediating"}, "mediating": {"escalated", "resolved"},
                 "escalated": {"resolved"}},
}
INITIAL_STATUS = {"decision": "proposed", "session": "open",
                  "idea": "captured", "conflict": "open"}

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

ID_RE = re.compile(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}\b")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
ANY_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
PLACEHOLDER_LINE_RE = re.compile(r"^(?:TBD|TODO|FIXME)\s*[.!:]?$", re.I)
ID_PLACEHOLDER_RE = re.compile(
    r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-XXXX\b")
BODY_H1_ID_RE = re.compile(
    r"^#\s+((?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4})\b")
RATIFYING_STATUSES = {"approved", "accepted", "closed"}
SESSION_CLOSE_FIELDS = ("participant", "participant-role", "facilitator",
                        "transcript-fidelity")


def today():
    return datetime.date.today().isoformat()


def fail(msg, code=1) -> "NoReturn":
    print(f"REFUSED: {msg}", file=sys.stderr)
    raise SystemExit(code)


# ------------------------------------------- structural guards (SES-0072)

def prose_lines(text):
    """(lineno, line) outside fenced code blocks, inline code blanked.

    Quoting a placeholder or heading legitimately is done in backticks —
    inline code and fenced blocks are exempt from every structural scan.
    """
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            yield n, INLINE_CODE_RE.sub("", line)


def guard_heading_lines(content, max_level, where):
    """Refuse body-only payloads carrying heading lines (IDEA-0041).

    A heading at the target section's level or higher becomes a phantom
    section boundary no later edit-section call can reach past.
    """
    for n, line in prose_lines(content):
        m = ANY_HEADING_RE.match(line.rstrip())
        if m and len(m.group(1)) <= max_level:
            fail(f"{where}: content line {n} is a heading-level line "
                 f"({line.strip()[:60]!r}) — this op writes section BODY "
                 "only; the tool owns heading lines (IDEA-0041). Strip it; "
                 "to repair existing structure use delete-section or "
                 "edit-section --occurrence")


def duplicate_sibling_headings(body):
    """[(level, text, count)] of repeated same-level headings sharing a
    parent — the phantom-heading signature."""
    stack, seen = [], {}
    for _, line in prose_lines(body):
        m = ANY_HEADING_RE.match(line.rstrip())
        if not m:
            continue
        level, text = len(m.group(1)), m.group(2)
        while stack and stack[-1][0] >= level:
            stack.pop()
        key = (tuple(t for _, t in stack), level, text)
        seen[key] = seen.get(key, 0) + 1
        stack.append((level, text))
    return [(k[1], k[2], n) for k, n in seen.items() if n > 1]


def placeholder_findings(body):
    """Standalone TBD/TODO/FIXME lines and unallocated ID placeholders."""
    out = []
    for n, line in prose_lines(body):
        s = line.strip()
        if PLACEHOLDER_LINE_RE.match(s):
            out.append(f"line {n} is placeholder text {s!r}")
        for tok in ID_PLACEHOLDER_RE.findall(line):
            out.append(f"line {n} carries unallocated ID placeholder {tok}")
    return out


# ------------------------------------------------------------ file model

class Artifact:
    """One corpus file, split into frontmatter text and body text.

    Writes are text-surgical: only the touched lines change, so diffs
    stay reviewable and untouched formatting survives byte-for-byte.
    """

    def __init__(self, path):
        self.path = path
        raw = path.read_text(encoding="utf-8")
        if not raw.startswith("---"):
            fail(f"{path}: no frontmatter")
        end = raw.find("\n---\n", 3)
        if end < 0:
            fail(f"{path}: unterminated frontmatter")
        self.fm = raw[3:end].lstrip("\n")
        self.body = raw[end + 5:]

    def write(self):
        self.path.write_text(f"---\n{self.fm}---\n{self.body}"
                             if self.fm.endswith("\n")
                             else f"---\n{self.fm}\n---\n{self.body}",
                             encoding="utf-8")

    # -- frontmatter helpers (top-level keys and links: subkeys) --

    def scalar(self, key):
        m = re.search(rf"^{re.escape(key)}:\s*(.*)$", self.fm, re.M)
        return m.group(1).strip().strip("\"'") if m else None

    def set_scalar(self, key, value):
        pat = re.compile(rf"^({re.escape(key)}:)\s*.*$", re.M)
        if pat.search(self.fm):
            self.fm = pat.sub(rf"\1 {value}", self.fm, count=1)
        else:  # insert after status: (or at top)
            anchor = re.search(r"^status:.*$", self.fm, re.M)
            pos = anchor.end() if anchor else 0
            self.fm = self.fm[:pos] + f"\n{key}: {value}" + self.fm[pos:]

    def _list_span(self, key, indent=""):
        """(start, end, ids) of an inline list `key: [..]`, multi-line ok."""
        pat = re.compile(rf"^{indent}{re.escape(key)}:\s*\[", re.M)
        m = pat.search(self.fm)
        if not m:
            return None
        i, depth = m.end() - 1, 0
        while i < len(self.fm):
            if self.fm[i] == "[":
                depth += 1
            elif self.fm[i] == "]":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if depth != 0:
            fail(f"{self.path.name}: unbalanced list for {key}")
        inner = self.fm[m.end():i]
        ids = [t.strip() for t in inner.replace("\n", " ").split(",")
               if t.strip()]
        return (m.start(), i + 1, ids)

    def get_list(self, key, indent=""):
        span = self._list_span(key, indent)
        return span[2] if span else []

    def add_to_list(self, key, value, indent=""):
        span = self._list_span(key, indent)
        if span:
            start, end, ids = span
            if value in ids:
                return False
            ids.append(value)
            self.fm = (self.fm[:start] +
                       f"{indent}{key}: [{', '.join(ids)}]" + self.fm[end:])
            return True
        if indent:  # a links: subkey — ensure links: block exists
            if not re.search(r"^links:\s*$", self.fm, re.M):
                self.fm = self.fm.rstrip("\n") + "\nlinks:\n"
            lm = re.search(r"^links:\s*$", self.fm, re.M)
            assert lm is not None
            pos = lm.end()
            self.fm = (self.fm[:pos] + f"\n{indent}{key}: [{value}]" +
                       self.fm[pos:])
        else:
            anchor = re.search(r"^links:", self.fm, re.M)
            pos = anchor.start() if anchor else len(self.fm)
            self.fm = (self.fm[:pos] + f"{key}: [{value}]\n" + self.fm[pos:])
        return True

    # -- body helpers --

    def section_span(self, heading_substr, occurrence=1):
        lines = self.body.splitlines(keepends=True)
        want = heading_substr.lower()
        start = end = None
        level = 0
        in_code = False
        pos = 0
        matched = 0
        for line in lines:
            stripped = line.rstrip("\n")
            if stripped.startswith("```"):
                in_code = not in_code
            m = HEADING_RE.match(stripped) if not in_code else None
            if start is None:
                if m and want in m.group(2).lower():
                    matched += 1
                    if matched == occurrence:
                        start, level = pos, len(m.group(1))
            elif m and len(m.group(1)) <= level:
                end = pos
                break
            pos += len(line)
        if start is None:
            return None
        return (start, end if end is not None else len(self.body))


# ------------------------------------------------------------- corpus

class Corpus:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.docs = self.root / "docs"
        # Batch mode (DEC-0314: validated and applied as a unit) defers
        # post-write re-validation to the end of the batch so members
        # may reference each other regardless of creation order.
        self.defer_recheck = False
        self.pending_recheck = []
        self.pending_resolve = []
        if not self.docs.is_dir():
            fail(f"no docs/ under {self.root}", 2)
        self.paths = {}   # id -> path
        for p in self.docs.rglob("*.md"):
            if p.parent.name == "specs" or p.name == "TRIGGERS.md":
                continue
            m = re.match(r"^((?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)"
                         r"-\d{4})-", p.name)
            if m:
                self.paths[m.group(1)] = p

    def load(self, aid):
        if aid not in self.paths:
            fail(f"{aid}: no such artifact")
        return Artifact(self.paths[aid])

    def next_id(self, prefix):
        nums = [int(a.split("-")[1]) for a in self.paths
                if a.startswith(prefix + "-")]
        return f"{prefix}-{max(nums, default=0) + 1:04d}"

    def resolve_all(self, text, where):
        # In batch mode, content resolution defers like recheck does:
        # payloads may reference artifacts created later in the batch.
        if self.defer_recheck:
            self.pending_resolve.append((text, where))
            return
        missing = [i for i in set(ID_RE.findall(text))
                   if i not in self.paths]
        if missing:
            fail(f"{where}: unresolved IDs {sorted(missing)}")

    # targeted post-write re-check (DEC-0315)
    def recheck(self, path):
        if self.defer_recheck:
            if path not in self.pending_recheck:
                self.pending_recheck.append(path)
            return True
        art = Artifact(path)
        aid = art.scalar("id")
        problems = []
        if _yaml is not None:
            try:
                if not isinstance(_yaml.safe_load(art.fm), dict):
                    problems.append("frontmatter parsed as non-mapping "
                                    "YAML")
            except _yaml.YAMLError as e:
                first = str(e).splitlines()[0] if str(e) else "parse error"
                problems.append(f"frontmatter is not parseable YAML "
                                f"({first})")
        if not aid or not path.name.startswith(aid + "-"):
            problems.append("id/filename mismatch")
        for i in set(ID_RE.findall(art.fm) + ID_RE.findall(art.body)):
            if i != aid and i not in self.paths:
                problems.append(f"unresolved {i}")
        first = art.body.lstrip("\n").split("\n", 1)[0]
        if first.startswith("# "):
            if ID_PLACEHOLDER_RE.search(first):
                problems.append("body H1 carries an unallocated ID "
                                "placeholder")
            else:
                h1 = BODY_H1_ID_RE.match(first)
                if h1 and h1.group(1) != aid:
                    problems.append(f"body H1 names {h1.group(1)}, "
                                    f"not {aid}")
        ov = extract_overview(art.fm)
        if not ov:
            problems.append("missing overview")
        elif len(ov.split()) > 250:
            problems.append(f"overview {len(ov.split())} words (max 250)")
        for rel in ("impacts", "impacted-by"):
            for other_id in art.get_list(rel, indent="  "):
                if other_id not in self.paths:
                    continue
                other = Artifact(self.paths[other_id])
                if aid not in other.get_list(RECIPROCAL[rel], indent="  "):
                    problems.append(
                        f"{rel} {other_id} not reciprocated")
        if problems:
            fail(f"post-write check failed on {path.name}: "
                 f"{'; '.join(problems)} — file written, fix required")
        return True


def extract_overview(fm):
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^overview:\s*(.*)$", line)
        if not m:
            continue
        v = m.group(1)
        if v.startswith((">", "|")) or v == "":
            block = []
            for follow in lines[i + 1:]:
                if follow.strip() and not follow.startswith((" ", "\t")):
                    break
                block.append(follow.strip())
            return " ".join(b for b in block if b)
        return v.strip("\"'")
    return ""


def kebab(title, limit=52):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(slug) > limit:
        slug = slug[:limit].rsplit("-", 1)[0]
    return slug


def read_payload(args, implicit_stdin=True):
    ff = getattr(args, "from_file", None)
    if ff == "-":
        return sys.stdin.read()
    if ff:
        return Path(ff).read_text(encoding="utf-8")
    # Ops that require content may read piped stdin; ops with a default
    # (create's template body) never block waiting on it.
    if implicit_stdin and not sys.stdin.isatty():
        data = sys.stdin.read()
        if data.strip():
            return data
    return None


def ok(msg, touched, json_mode):
    if json_mode:
        print(json.dumps({"result": "ok", "detail": msg,
                          "touched": [str(t) for t in touched]}))
    else:
        print(f"OK {msg}")


# ----------------------------------------------------------- operations

def op_create(c, args, json_mode):
    if args.type not in TYPE_INFO:
        fail(f"unknown type {args.type!r}; one of {sorted(TYPE_INFO)}")
    prefix, subdir = TYPE_INFO[args.type]
    if not args.overview or not args.overview.strip():
        fail("create requires --overview (checker rule 11: non-empty, "
             "max 250 words)")
    if len(args.overview.split()) > 250:
        fail(f"overview is {len(args.overview.split())} words (max 250)")
    if args.type == "decision" and not args.derives_from:
        fail("a decision requires --link derives-from=SES-nnnn or SP-nnnn "
             "(integrity rule 4)")
    aid = c.next_id(prefix)
    status = args.status or INITIAL_STATUS.get(args.type, "draft")
    allowed = (set(REDUCED_TRANSITIONS.get(args.type, {}).keys())
               | set(INITIAL_STATUS.values()) | set(GATE_TRANSITIONS)
               | {"accepted", "closed", "taken-up", "declined"})
    if status not in allowed:
        fail(f"bad initial status {status!r} for {args.type}")

    links_lines = []
    for rel, ids in args.links.items():
        links_lines.append(f"  {rel}: [{', '.join(ids)}]")
    for ids in args.links.values():
        for i in ids:
            if i not in c.paths:
                fail(f"link target {i} does not exist")

    # Titles are always double-quoted: unquoted YAML breaks on ':' and
    # friends (SES-0059 T22-class defect, stakeholder-approved fix).
    quoted_title = '"' + args.title.replace("\\", "\\\\") \
                                   .replace('"', '\\"') + '"'
    fm = [f"id: {aid}", f"type: {args.type}", f"title: {quoted_title}",
          f"status: {status}", f"owner: {args.owner}",
          f"created: {today()}"]
    for extra in args.field:
        fm.append(extra)
    ov_lines = ["overview: >-"]
    import textwrap as _tw
    ov_lines += _tw.wrap(args.overview.strip(), width=68,
                         initial_indent="  ", subsequent_indent="  ")
    fm += ov_lines
    if links_lines:
        fm.append("links:")
        fm += links_lines
    if args.cites:
        fm.append(f"cites: [{', '.join(args.cites)}]")

    body = read_payload(args, implicit_stdin=False)
    if body is None:
        parts = [f"# {aid}: {args.title}", ""]
        for sec in REQUIRED_SECTIONS.get(args.type, []):
            parts += [f"## {sec}", "", "TBD.", ""]
        body = "\n".join(parts)
    else:
        # Stamp the allocated ID into a placeholder H1 (SES-0072): bodies
        # are authored before the ID exists; `# SES-XXXX: …` is expected.
        body_lines = body.split("\n")
        if body_lines and body_lines[0].startswith("# "):
            body_lines[0] = body_lines[0].replace(f"{prefix}-XXXX", aid)
            body = "\n".join(body_lines)

    path = c.docs / subdir / f"{aid}-{kebab(args.title)}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + "\n".join(fm) + "\n---\n\n" +
                    body.rstrip("\n") + "\n", encoding="utf-8")
    c.paths[aid] = path
    # reciprocity bookkeeping for impact links
    for rel in ("impacts", "impacted-by"):
        for other_id in args.links.get(rel, []):
            other = c.load(other_id)
            if other.scalar("type") != args.type:
                fail(f"impact links are same-type only ({aid} is "
                     f"{args.type}, {other_id} is {other.scalar('type')})")
            other.add_to_list(RECIPROCAL[rel], aid, indent="  ")
            other.write()
    c.recheck(path)
    ok(f"create {aid} -> {path.relative_to(c.root)}", [path], json_mode)


def op_set_status(c, args, json_mode):
    art = c.load(args.id)
    atype, cur = art.scalar("type"), art.scalar("status")
    new = args.status
    if atype == "change-proposal":
        fail("change proposals use the triage field, not status; "
             "edit triage via edit-section / a triage session")
    table = REDUCED_TRANSITIONS.get(atype, GATE_TRANSITIONS)
    if new == cur:
        fail(f"{args.id} is already {cur}")
    if new not in table.get(cur, set()):
        alt = ""
        if atype == "decision" and cur == "accepted":
            alt = " — accepted decisions are immutable; use `supersede`"
        if atype == "session" and cur == "closed":
            alt = " — closed sessions are immutable; open a new session"
        fail(f"illegal transition {cur} -> {new} for {atype}{alt}")
    if new == "deferred":
        if atype not in DEFERRABLE:
            fail(f"deferred applies only to {sorted(DEFERRABLE)}")
        if not (args.release or art.scalar("release")):
            fail("deferral requires --release (DEC-0098)")
    zero_dec_note = ""
    if new in RATIFYING_STATUSES:
        # Structural completeness gate (SES-0072): ratified artifacts may
        # not carry phantom-heading duplicates or placeholder text.
        problems = [f"duplicate sibling heading {'#' * lv} {t!r} x{n}"
                    for lv, t, n in duplicate_sibling_headings(art.body)]
        problems += placeholder_findings(art.body)
        if problems:
            fail(f"{args.id}: cannot ratify ({cur} -> {new}) — "
                 + "; ".join(problems))
    if atype == "session" and new == "closed":
        missing = [f for f in SESSION_CLOSE_FIELDS if not art.scalar(f)]
        if missing:
            fail(f"{args.id}: session close requires frontmatter "
                 f"{', '.join(missing)}")
        produced = [aid for aid, p in c.paths.items()
                    if aid.startswith("DEC-") and args.id in
                    Artifact(p).get_list("derives-from", indent="  ")]
        if not produced:
            if not args.no_decisions_ok:
                fail(f"{args.id}: no decision derives from this session — "
                     "assess whether that is right (idea-capture sessions "
                     "legitimately produce none, DEC-0258): either record "
                     "the session's decisions first, or re-run with "
                     '--no-decisions-ok "<reason>" to record the '
                     "assessment")
            zero_dec_note = (" [zero decisions acknowledged: "
                             f"{args.no_decisions_ok}]")
    if new == "accepted" and atype == "decision":
        # accepted-in stamp (SES-0072): where a decision proposed in one
        # session gets ratified later, the graph keeps the site.
        if not args.session:
            fail("accepting a decision requires --session SES-nnnn "
                 "(accepted-in stamp)")
        if args.session not in c.paths:
            fail(f"{args.session} does not exist")
        art.set_scalar("accepted-in", args.session)
    if new == "approved":
        if not args.approved_by:
            fail("approval requires --approved-by (gate stamping)")
        art.set_scalar("approved-by", args.approved_by)
        art.set_scalar("approved-on", today())
    if new == "superseded" and not args.superseded_by:
        fail("superseding requires --superseded-by NEW-ID (or use "
             "`supersede` for decisions, which does the bookkeeping)")
    if args.superseded_by:
        if args.superseded_by not in c.paths:
            fail(f"{args.superseded_by} does not exist")
        art.set_scalar("superseded-by", f"[{args.superseded_by}]")
    if args.release:
        art.set_scalar("release", f'"{args.release}"')
    art.set_scalar("status", new)
    art.write()
    c.recheck(art.path)
    ok(f"set-status {args.id} {cur} -> {new}{zero_dec_note}",
       [art.path], json_mode)


def op_add_link(c, args, json_mode):
    if args.rel not in LINK_VOCAB:
        fail(f"link type {args.rel!r} not in closed vocabulary "
             f"{LINK_VOCAB} (decision citations use add-cite)")
    src, dst = c.load(args.id), c.load(args.target)
    if args.rel in RECIPROCAL and src.scalar("type") != dst.scalar("type"):
        fail("impact links connect same-type artifacts only")
    if src.scalar("type") == "decision" and src.scalar("status") == \
            "accepted" and args.rel != "relates-to":
        fail("accepted decisions are immutable; only relates-to "
             "cross-reference enrichment is sanctioned (DEC-0248) — "
             "otherwise supersede")
    changed = src.add_to_list(args.rel, args.target, indent="  ")
    if changed:
        src.write()
    if args.rel in RECIPROCAL:
        if dst.add_to_list(RECIPROCAL[args.rel], args.id, indent="  "):
            dst.write()
    c.recheck(src.path)
    ok(f"add-link {args.id} {args.rel} {args.target}"
       + ("" if changed else " (already present)"),
       [src.path, dst.path], json_mode)


def op_add_cite(c, args, json_mode):
    art = c.load(args.id)
    if not args.target.startswith("DEC-"):
        fail("cites reference decisions (DEC-nnnn)")
    c.load(args.target)
    if art.scalar("type") == "decision" and art.scalar("status") == \
            "accepted":
        fail("accepted decisions are immutable — supersede instead")
    changed = art.add_to_list("cites", args.target)
    if changed:
        art.write()
    c.recheck(art.path)
    ok(f"add-cite {args.id} <- {args.target}"
       + ("" if changed else " (already present)"), [art.path], json_mode)


def op_update_overview(c, args, json_mode):
    art = c.load(args.id)
    text = read_payload(args) or args.text
    if not text or not text.strip():
        fail("provide overview text via stdin, --from-file, or --text")
    text = " ".join(text.split())
    if len(text.split()) > 250:
        fail(f"overview is {len(text.split())} words (max 250)")
    c.resolve_all(text, f"{args.id} overview")
    import textwrap as _tw
    block = "overview: >-\n" + "\n".join(
        _tw.wrap(text, width=68, initial_indent="  ",
                 subsequent_indent="  "))
    lines = art.fm.splitlines()
    out, i, replaced = [], 0, False
    while i < len(lines):
        if re.match(r"^overview:", lines[i]):
            out.append(block)
            i += 1
            while i < len(lines) and (lines[i].startswith((" ", "\t"))
                                      or not lines[i].strip()):
                i += 1
            replaced = True
            continue
        out.append(lines[i])
        i += 1
    if not replaced:
        anchor = next((j for j, ln in enumerate(out)
                       if ln.startswith("links:")), len(out))
        out.insert(anchor, block)
    art.fm = "\n".join(out) + "\n"
    art.write()
    c.recheck(art.path)
    ok(f"update-overview {args.id} ({len(text.split())} words) — "
       "derived/non-normative, legal on any artifact (DEC-0285)",
       [art.path], json_mode)


def op_edit_section(c, args, json_mode):
    art = c.load(args.id)
    atype, status = art.scalar("type"), art.scalar("status")
    if atype == "decision" and status in ("accepted", "superseded"):
        fail("accepted decisions are immutable — supersede instead")
    if atype == "session" and status == "closed":
        fail("closed sessions are immutable — use append-turn "
             "--enrichment for cross-reference enrichment (DEC-0248), "
             "or open a new session")
    if status in ("approved", "stale") and not args.amend:
        fail(f"{args.id} is {status}; semantic edits to ratified "
             "artifacts happen in a session — re-run with --amend to "
             "assert a session sanctions this edit")
    content = read_payload(args)
    if content is None:
        fail("provide section content via stdin or --from-file")
    span = art.section_span(args.heading, args.occurrence)
    if span is None:
        where = (f" (occurrence {args.occurrence})"
                 if args.occurrence != 1 else "")
        fail(f"{args.id}: no section matching {args.heading!r}{where}")
    start, end = span
    head_line = art.body[start:].splitlines()[0]
    hm = HEADING_RE.match(head_line)
    assert hm is not None
    guard_heading_lines(content, len(hm.group(1)),
                        f"{args.id} {args.heading!r}")
    art.body = (art.body[:start] + head_line + "\n\n" +
                content.strip() + "\n\n" + art.body[end:])
    art.write()
    c.resolve_all(content, f"{args.id} section")
    c.recheck(art.path)
    warn = ("" if args.overview_ok else
            " — if this changed the artifact's meaning, update-overview "
            "in the same change (DEC-0288)")
    ok(f"edit-section {args.id} {args.heading!r}{warn}", [art.path],
       json_mode)


def op_delete_section(c, args, json_mode):
    """Remove a section (heading + body) — the recovery op for
    phantom-heading corruption (SES-0072): duplicates are deletable,
    the type's required template is not."""
    art = c.load(args.id)
    atype, status = art.scalar("type"), art.scalar("status")
    if atype == "decision" and status in ("accepted", "superseded"):
        fail("accepted decisions are immutable — supersede instead")
    if atype == "session" and status == "closed":
        fail("closed sessions are immutable — open a new session")
    if status in ("approved", "stale") and not args.amend:
        fail(f"{args.id} is {status}; semantic edits to ratified "
             "artifacts happen in a session — re-run with --amend to "
             "assert a session sanctions this deletion")
    span = art.section_span(args.heading, args.occurrence)
    if span is None:
        where = (f" (occurrence {args.occurrence})"
                 if args.occurrence != 1 else "")
        fail(f"{args.id}: no section matching {args.heading!r}{where}")
    start, end = span
    head_line = art.body[start:].splitlines()[0]
    hm = HEADING_RE.match(head_line)
    assert hm is not None
    level, text = len(hm.group(1)), hm.group(2)
    if level == 2 and text in REQUIRED_SECTIONS.get(atype, []):
        count = sum(1 for _, ln in prose_lines(art.body)
                    if (m2 := ANY_HEADING_RE.match(ln.rstrip()))
                    and len(m2.group(1)) == level and m2.group(2) == text)
        if count <= 1:
            fail(f"{args.id}: {text!r} is a required section for {atype} "
                 "and this is its only occurrence — deleting it would "
                 "break the template (duplicate occurrences are "
                 "deletable)")
    art.body = art.body[:start] + art.body[end:]
    art.write()
    c.recheck(art.path)
    ok(f"delete-section {args.id} {text!r} (occurrence {args.occurrence})",
       [art.path], json_mode)


def op_append_turn(c, args, json_mode):
    art = c.load(args.id)
    if art.scalar("type") != "session":
        fail("append-turn applies to sessions")
    content = read_payload(args)
    if content is None:
        fail("provide turn content via stdin or --from-file")
    guard_heading_lines(content, 2, f"{args.id} turn")
    c.resolve_all(content, f"{args.id} turn")
    span = art.section_span("Transcript")
    if span is None:
        fail(f"{args.id} has no Transcript section")
    start, end = span
    closed = art.scalar("status") == "closed"
    if closed and not args.enrichment:
        fail("closed sessions are immutable; only dated Post-Close "
             "Enrichment is sanctioned (DEC-0248) — re-run with "
             "--enrichment, or open a new session")
    if closed:
        seg = art.body[start:end]
        marker = f"### Post-Close Enrichment ({today()})"
        if "### Post-Close Enrichment" not in seg:
            insert = f"\n{marker}\n\n{content.strip()}\n"
        else:
            insert = f"\n{content.strip()}\n"
        art.body = (art.body[:end].rstrip("\n") + "\n" + insert +
                    "\n" + art.body[end:])
    else:
        art.body = (art.body[:end].rstrip("\n") + "\n\n" +
                    content.strip() + "\n\n" + art.body[end:])
    art.write()
    c.recheck(art.path)
    ok(f"append-turn {args.id}"
       + (" (post-close enrichment)" if closed else ""),
       [art.path], json_mode)


def op_supersede(c, args, json_mode):
    old = c.load(args.id)
    if old.scalar("type") != "decision":
        fail("supersede applies to decisions; for other artifacts use "
             "create + set-status --superseded-by")
    if old.scalar("status") == "superseded":
        fail(f"{args.id} is already superseded by "
             f"{old.scalar('superseded-by')}")
    ns = argparse.Namespace(
        type="decision", title=args.title, overview=args.overview,
        owner=args.owner, status="accepted",
        links={"derives-from": [args.session],
               "supersedes": [args.id]},
        cites=args.cites, from_file=args.from_file,
        field=[f"decided-by: {args.owner}", f"decided-on: {today()}",
               f'source-span: "{args.source_span}"'],
        derives_from=[args.session])
    new_id = c.next_id("DEC")
    op_create(c, ns, json_mode=False)
    old.set_scalar("status", "superseded")
    old.set_scalar("superseded-by", f"[{new_id}]")
    old.write()
    c.recheck(old.path)
    # stale-walk hint: ratified artifacts citing the old decision
    citers = []
    for aid, p in sorted(c.paths.items()):
        if aid in (args.id, new_id):
            continue
        a = Artifact(p)
        if args.id in a.get_list("cites"):
            if a.scalar("status") in ("approved", "accepted", "gated"):
                citers.append(f"{aid} [{a.scalar('status')}]")
    note = (f"; review citers for staleness: {', '.join(citers)}"
            if citers else "; no ratified citers")
    ok(f"supersede {args.id} -> {new_id}{note}",
       [old.path, c.paths[new_id]], json_mode)


def op_apply(c, args, json_mode):
    ops = json.loads(Path(args.file).read_text(encoding="utf-8"))
    if not isinstance(ops, list):
        fail("apply expects a JSON list of operation objects")
    print(f"apply: {len(ops)} operation(s)")
    c.defer_recheck = True
    for i, spec in enumerate(ops):
        op = spec.pop("op", None)
        if op not in DISPATCH or op == "apply":
            fail(f"apply[{i}]: unknown op {op!r}")
        ns = build_namespace(op, spec)
        DISPATCH[op](c, ns, json_mode)
    # DEC-0314: the batch validates as a unit — re-check every touched
    # file now that all members exist, reporting all failures together.
    c.defer_recheck = False
    failures = 0
    for text, where in c.pending_resolve:
        try:
            c.resolve_all(text, where)
        except SystemExit:
            failures += 1
    for path in c.pending_recheck:
        try:
            c.recheck(path)
        except SystemExit:
            failures += 1
    if failures:
        fail(f"apply: {failures} file(s) failed post-batch validation "
             "(details above) — files are written; fix required")
    print(f"apply: post-batch validation clean "
          f"({len(c.pending_recheck)} file(s))")


def build_namespace(op, spec):
    """Build an argparse-like namespace from a JSON op spec."""
    defaults = dict(
        links={}, cites=[], field=[], from_file=None, text=None,
        overview=None, status=None, owner="awakeinagi@gmail.com",
        release=None, approved_by=None, superseded_by=None, amend=False,
        enrichment=False, overview_ok=False, derives_from=None,
        session=None, source_span=None, title=None, heading=None,
        id=None, target=None, rel=None, occurrence=1,
        no_decisions_ok=None)
    content = spec.pop("content", None)
    defaults.update({k.replace("-", "_"): v for k, v in spec.items()})
    ns = argparse.Namespace(**defaults)
    if content is not None:  # inline payloads allowed in batch mode
        import tempfile
        tf = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        tf.write(content)
        tf.close()
        ns.from_file = tf.name
    if ns.links:
        ns.derives_from = ns.links.get("derives-from")
    return ns


DISPATCH = {
    "create": op_create, "set-status": op_set_status,
    "add-link": op_add_link, "add-cite": op_add_cite,
    "update-overview": op_update_overview, "edit-section": op_edit_section,
    "delete-section": op_delete_section, "append-turn": op_append_turn,
    "supersede": op_supersede, "apply": op_apply,
}


# ------------------------------------------------------------------ CLI

def parse_links(pairs):
    links = {}
    for pair in pairs or []:
        if "=" not in pair:
            fail(f"--link takes rel=ID[,ID...], got {pair!r}")
        rel, ids = pair.split("=", 1)
        if rel not in LINK_VOCAB:
            fail(f"link type {rel!r} not in {LINK_VOCAB}")
        links.setdefault(rel, []).extend(
            i.strip() for i in ids.split(",") if i.strip())
    return links


def main():
    ap = argparse.ArgumentParser(
        description="Typed, guardrailed writes over a Groundwork corpus")
    ap.add_argument("--root", default=".")
    ap.add_argument("--json", action="store_true", dest="json_mode")
    sub = ap.add_subparsers(dest="op", required=True)

    p = sub.add_parser(
        "create",
        description="Create an artifact; the API allocates the next "
        "sequential ID. A body H1 written as '# PREFIX-XXXX: ...' is "
        "stamped with the allocated ID. BATCH KEYS: type, title, "
        "overview, status, owner, links (a DICT of rel->list, e.g. "
        '{"derives-from": ["SES-0001"]} — the CLI\'s link string form '
        "is ignored in batch), cites (list), field (list), "
        "content|from-file.")
    p.add_argument("--type", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--overview", required=True)
    p.add_argument("--owner", default="awakeinagi@gmail.com")
    p.add_argument("--status", default=None)
    p.add_argument("--link", action="append", dest="link_pairs",
                   metavar="rel=ID[,ID...]")
    p.add_argument("--cite", action="append", dest="cites", default=[])
    p.add_argument("--field", action="append", default=[],
                   metavar="'key: value'")
    p.add_argument("--from-file", help="body content (else template)")

    p = sub.add_parser(
        "set-status",
        description="Change lifecycle status. Transitions to approved/"
        "accepted/closed refuse duplicate sibling headings and "
        "placeholder lines (quote tokens in backticks to mention "
        "them). Accepting a proposed decision requires --session "
        "(stamps accepted-in). Closing a session requires identity "
        "frontmatter (participant, participant-role, facilitator, "
        "transcript-fidelity) and a produced decision, or "
        "--no-decisions-ok. BATCH KEYS: id, status, approved-by, "
        "superseded-by, release, session, no-decisions-ok.")
    p.add_argument("id")
    p.add_argument("status")
    p.add_argument("--approved-by")
    p.add_argument("--superseded-by")
    p.add_argument("--release")
    p.add_argument("--session",
                   help="SES-nnnn ratifying a proposed decision "
                        "(stamped as accepted-in)")
    p.add_argument("--no-decisions-ok", metavar="REASON",
                   help="acknowledge closing a session that produced "
                        "no decisions (DEC-0258)")

    p = sub.add_parser(
        "add-link",
        description="Add a frontmatter link (closed vocabulary). "
        "impacts/impacted-by reciprocate automatically; relates-to "
        "does NOT — add the reverse side explicitly where wanted. "
        "BATCH KEYS: id, rel, target.")
    p.add_argument("id")
    p.add_argument("rel")
    p.add_argument("target")

    p = sub.add_parser(
        "add-cite",
        description="Add a DEC citation; also reference the DEC in "
        "body prose (DEC-0247). BATCH KEYS: id, target.")
    p.add_argument("id")
    p.add_argument("target")

    p = sub.add_parser(
        "update-overview",
        description="Replace the frontmatter overview (max 250 words; "
        "derived/non-normative, legal on any artifact incl. closed/"
        "accepted). BATCH KEY for the text is 'text' or 'content' — "
        "there is no 'overview' key.")
    p.add_argument("id")
    p.add_argument("--text")
    p.add_argument("--from-file")

    p = sub.add_parser(
        "edit-section",
        description="Replace one section's BODY — the tool keeps the "
        "heading; payloads containing a heading line at the section's "
        "level or higher are refused (IDEA-0041). Heading matched by "
        "case-insensitive substring. BATCH KEYS: id, heading, "
        "occurrence, amend, overview-ok, content|from-file.")
    p.add_argument("id")
    p.add_argument("heading")
    p.add_argument("--from-file")
    p.add_argument("--occurrence", type=int, default=1,
                   help="target the Nth heading matching the substring "
                        "(structural repair; default 1)")
    p.add_argument("--amend", action="store_true")
    p.add_argument("--overview-ok", action="store_true",
                   help="assert the overview is already faithful")

    p = sub.add_parser(
        "delete-section",
        description="Remove a heading and its span — the phantom-"
        "heading repair op. Refuses the LAST occurrence of a type-"
        "required section (duplicates are deletable, the template is "
        "not). BATCH KEYS: id, heading, occurrence, amend.")
    p.add_argument("id")
    p.add_argument("heading")
    p.add_argument("--occurrence", type=int, default=1)
    p.add_argument("--amend", action="store_true")

    p = sub.add_parser(
        "append-turn",
        description="Append turn content to a session's Transcript. "
        "###-level turn headings are fine; ##-level lines are refused. "
        "Closed sessions need --enrichment (dated Post-Close "
        "Enrichment, DEC-0248). BATCH KEYS: id, enrichment, "
        "content|from-file.")
    p.add_argument("id")
    p.add_argument("--from-file")
    p.add_argument("--enrichment", action="store_true")

    p = sub.add_parser(
        "supersede",
        description="Replace an accepted decision: creates the new "
        "accepted DEC (supersedes + derives-from set), flips the old "
        "to superseded, prints ratified citers as the stale-walk "
        "hint. BATCH KEYS: id, title, overview, session, source-span, "
        "owner, cites, content|from-file.")
    p.add_argument("id")
    p.add_argument("--title", required=True)
    p.add_argument("--overview", required=True)
    p.add_argument("--session", required=True,
                   help="SES/SP the new decision derives from")
    p.add_argument("--source-span", required=True)
    p.add_argument("--owner", default="awakeinagi@gmail.com")
    p.add_argument("--cite", action="append", dest="cites", default=[])
    p.add_argument("--from-file")

    p = sub.add_parser(
        "apply",
        description="Run a JSON list of ops as one unit (validation "
        "defers to batch end so members may reference each other). "
        "Keys are each op's BATCH KEYS (see that op's --help); "
        "'content' replaces --from-file inline. A refusal stops the "
        "batch; earlier ops remain applied — re-run only the "
        "unexecuted remainder. Full schema: references/operations.md.")
    p.add_argument("file", help="JSON list of operation objects")

    args = ap.parse_args()
    if args.op == "create":
        args.links = parse_links(getattr(args, "link_pairs", None))
        args.derives_from = args.links.get("derives-from")
    c = Corpus(args.root)
    DISPATCH[args.op](c, args, args.json_mode)


if __name__ == "__main__":
    main()
