#!/usr/bin/env python3
"""Typed write operations over a Groundwork corpus (DEC-0312, DEC-0313).

The sole sanctioned write path for agents: every operation validates its
preconditions against the SPECs (docs/specs/SPEC-*.md are the normative
basis, DEC-0311), performs the write plus its bookkeeping atomically,
re-validates the artifacts it touched (DEC-0315), and prints a compact
result so the caller need not re-read the file (DEC-0314).

Operations (DEC-0313): create, append-turn, edit-section, set-status,
add-link, add-cite, supersede, update-overview, apply (JSON batch).

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


def today():
    return datetime.date.today().isoformat()


def fail(msg, code=1) -> "NoReturn":
    print(f"REFUSED: {msg}", file=sys.stderr)
    raise SystemExit(code)


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

    def section_span(self, heading_substr):
        lines = self.body.splitlines(keepends=True)
        want = heading_substr.lower()
        start = end = None
        level = 0
        in_code = False
        pos = 0
        for line in lines:
            stripped = line.rstrip("\n")
            if stripped.startswith("```"):
                in_code = not in_code
            m = HEADING_RE.match(stripped) if not in_code else None
            if start is None:
                if m and want in m.group(2).lower():
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
        missing = [i for i in set(ID_RE.findall(text))
                   if i not in self.paths]
        if missing:
            fail(f"{where}: unresolved IDs {sorted(missing)}")

    # targeted post-write re-check (DEC-0315)
    def recheck(self, path):
        art = Artifact(path)
        aid = art.scalar("id")
        problems = []
        if not aid or not path.name.startswith(aid + "-"):
            problems.append("id/filename mismatch")
        for i in set(ID_RE.findall(art.fm) + ID_RE.findall(art.body)):
            if i != aid and i not in self.paths:
                problems.append(f"unresolved {i}")
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

    fm = [f"id: {aid}", f"type: {args.type}", f"title: {args.title}",
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
    ok(f"set-status {args.id} {cur} -> {new}", [art.path], json_mode)


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
    span = art.section_span(args.heading)
    if span is None:
        fail(f"{args.id}: no section matching {args.heading!r}")
    start, end = span
    head_line = art.body[start:].splitlines()[0]
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


def op_append_turn(c, args, json_mode):
    art = c.load(args.id)
    if art.scalar("type") != "session":
        fail("append-turn applies to sessions")
    content = read_payload(args)
    if content is None:
        fail("provide turn content via stdin or --from-file")
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
    for i, spec in enumerate(ops):
        op = spec.pop("op", None)
        if op not in DISPATCH or op == "apply":
            fail(f"apply[{i}]: unknown op {op!r}")
        ns = build_namespace(op, spec)
        DISPATCH[op](c, ns, json_mode)


def build_namespace(op, spec):
    """Build an argparse-like namespace from a JSON op spec."""
    defaults = dict(
        links={}, cites=[], field=[], from_file=None, text=None,
        overview=None, status=None, owner="awakeinagi@gmail.com",
        release=None, approved_by=None, superseded_by=None, amend=False,
        enrichment=False, overview_ok=False, derives_from=None,
        session=None, source_span=None, title=None, heading=None,
        id=None, target=None, rel=None)
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
    "append-turn": op_append_turn, "supersede": op_supersede,
    "apply": op_apply,
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

    p = sub.add_parser("create")
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

    p = sub.add_parser("set-status")
    p.add_argument("id")
    p.add_argument("status")
    p.add_argument("--approved-by")
    p.add_argument("--superseded-by")
    p.add_argument("--release")

    p = sub.add_parser("add-link")
    p.add_argument("id")
    p.add_argument("rel")
    p.add_argument("target")

    p = sub.add_parser("add-cite")
    p.add_argument("id")
    p.add_argument("target")

    p = sub.add_parser("update-overview")
    p.add_argument("id")
    p.add_argument("--text")
    p.add_argument("--from-file")

    p = sub.add_parser("edit-section")
    p.add_argument("id")
    p.add_argument("heading")
    p.add_argument("--from-file")
    p.add_argument("--amend", action="store_true")
    p.add_argument("--overview-ok", action="store_true",
                   help="assert the overview is already faithful")

    p = sub.add_parser("append-turn")
    p.add_argument("id")
    p.add_argument("--from-file")
    p.add_argument("--enrichment", action="store_true")

    p = sub.add_parser("supersede")
    p.add_argument("id")
    p.add_argument("--title", required=True)
    p.add_argument("--overview", required=True)
    p.add_argument("--session", required=True,
                   help="SES/SP the new decision derives from")
    p.add_argument("--source-span", required=True)
    p.add_argument("--owner", default="awakeinagi@gmail.com")
    p.add_argument("--cite", action="append", dest="cites", default=[])
    p.add_argument("--from-file")

    p = sub.add_parser("apply")
    p.add_argument("file", help="JSON list of operation objects")

    args = ap.parse_args()
    if args.op == "create":
        args.links = parse_links(getattr(args, "link_pairs", None))
        args.derives_from = args.links.get("derives-from")
    c = Corpus(args.root)
    DISPATCH[args.op](c, args, args.json_mode)


if __name__ == "__main__":
    main()
