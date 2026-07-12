#!/usr/bin/env python3
"""Proactive consistency checks over a Groundwork corpus.

Two complements to the semantic decision-recall audit (DEC-0137), both
born from the SES-0026/SES-0027 incident where DEC-0151 partially
cancelled DEC-0048 and two approved artifacts kept enumerating the
cancelled operation:

  sweep  — the relates-to sweep (DEC-0157). A new decision that lists
           accepted decisions in `relates-to`/`supersedes` may narrow or
           contradict them without triggering the staleness walk (which
           keys on `supersedes` alone). For each given decision, list
           every artifact citing each related accepted decision, so the
           facilitator reviews the citers for consistency at
           distillation time.

  terms  — the identifier co-occurrence audit (DEC-0158). Contract
           identifiers in code spans (operation names, field names,
           config paths) are quasi-formal symbols. For each given
           artifact, extract its code-span identifiers, then report
           other artifacts sharing *rare* identifiers, flagging pairs
           with no direct frontmatter link — exact-match contract
           overlap the embedding audit can miss.

Pure stdlib; no index, no dependencies. Usage:

  python3 groundwork_consistency.py --root <project> sweep DEC-0151 [...]
  python3 groundwork_consistency.py --root <project> terms DEC-0151 [...]
      [--max-df 6] [--all-statuses]

Both commands are advisory: they emit review lists, not verdicts.
Exit code 0 always (findings are for human/judge review, not CI).
"""

import argparse
import re
import os
import sys
from pathlib import Path

ID_RE = re.compile(
    r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CP|CON|IDEA)-\d{4}$"
)
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
FENCE_RE = re.compile(r"^(```|~~~)")
# identifier-ish: word chars plus -_./, must contain a letter and at
# least one of - _ . / or an inner capital (camelCase); no spaces.
TOKEN_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.\-/()]*$")


def looks_like_identifier(tok: str) -> bool:
    tok = tok.strip()
    if not tok or " " in tok or len(tok) < 3 or len(tok) > 80:
        return False
    if ID_RE.match(tok):
        return False  # artifact IDs ride the typed link graph already
    if not TOKEN_RE.match(tok):
        return False
    core = tok.rstrip("()")
    has_sep = any(c in core for c in "-_./")
    has_inner_cap = any(c.isupper() for c in core[1:])
    return has_sep or has_inner_cap


class Doc:
    __slots__ = ("id", "path", "type", "status", "title", "links", "cites",
                 "body")

    def __init__(self):
        self.id = self.type = self.status = self.title = ""
        self.links = {}   # link-type -> [ids]
        self.cites = []
        self.body = ""


def parse_id_list(text: str):
    return re.findall(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CP|CON|IDEA)-\d{4}\b",
                      text)


def parse_doc(path: Path):
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not raw.startswith("---"):
        return None
    end = raw.find("\n---", 3)
    if end < 0:
        return None
    fm, body = raw[3:end], raw[end + 4:]
    d = Doc()
    d.path, d.body = path, body

    # fold bracketed lists that span lines, then scan key: value lines
    folded, buf = [], ""
    for line in fm.splitlines():
        buf = (buf + " " + line.strip()) if buf else line.rstrip()
        if buf.count("[") > buf.count("]"):
            continue
        folded.append(buf)
        buf = ""
    if buf:
        folded.append(buf)

    in_links = False
    for line in folded:
        if re.match(r"^links\s*:", line):
            in_links = True
            continue
        m = re.match(r"^(\s+)([A-Za-z-]+)\s*:\s*(.*)$", line)
        if in_links and m:
            d.links[m.group(2)] = parse_id_list(m.group(3))
            continue
        in_links = False
        m = re.match(r"^([A-Za-z-]+)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "id":
            d.id = val
        elif key == "type":
            d.type = val
        elif key == "status":
            d.status = val
        elif key == "title":
            d.title = val.strip("\"'")
        elif key == "cites":
            d.cites = parse_id_list(val)
    return d if d.id else None


def load_corpus(root: Path):
    docs = {}
    for p in sorted((root / "docs").rglob("*.md")):
        d = parse_doc(p)
        if d:
            docs[d.id] = d
    return docs


def body_tokens(doc: Doc):
    toks, fenced = set(), False
    for line in doc.body.splitlines():
        if FENCE_RE.match(line.strip()):
            fenced = not fenced
            continue
        if fenced:
            continue
        for m in CODE_SPAN_RE.finditer(line):
            tok = m.group(1).strip()
            if looks_like_identifier(tok):
                toks.add(tok)
    return toks


def directly_linked(a: Doc, b: Doc) -> bool:
    if b.id in a.cites or a.id in b.cites:
        return True
    for ids in a.links.values():
        if b.id in ids:
            return True
    for ids in b.links.values():
        if a.id in ids:
            return True
    return False


def cmd_sweep(docs, targets, all_statuses):
    findings = 0
    for tid in targets:
        t = docs.get(tid)
        if not t:
            print(f"?? {tid}: not found", file=sys.stderr)
            continue
        related = []
        for key in ("relates-to", "supersedes"):
            for rid in t.links.get(key, []):
                r = docs.get(rid)
                if r and r.type == "decision" and r.status == "accepted":
                    related.append((key, r))
        if not related:
            print(f"{tid}: no accepted decisions in relates-to/supersedes "
                  "— nothing to sweep.")
            continue
        print(f"\n== sweep {tid}: {t.title}")
        for key, r in related:
            citers = [d for d in docs.values()
                      if r.id in d.cites and d.id != tid]
            if not all_statuses:
                citers = [d for d in citers
                          if d.status in ("approved", "stale", "gated")]
            print(f"  {key} {r.id} ({r.title})")
            if not citers:
                print("    no ratified citers — clear.")
                continue
            findings += len(citers)
            for d in sorted(citers, key=lambda x: x.id):
                print(f"    REVIEW {d.id} [{d.status}] {d.title}")
    print(f"\nsweep: {findings} citer(s) to review for consistency "
          f"with the new decision(s).")


RATIFIED = ("approved", "stale", "gated", "accepted")


def tokens_match(a: str, b: str) -> bool:
    """Exact match or containment (`jira-status` ⊂ `set-jira-status`) —
    the SES-0026 incident joined on containment, not equality."""
    if a == b:
        return True
    small, big = (a, b) if len(a) <= len(b) else (b, a)
    return len(small) >= 6 and small in big


def cmd_terms(docs, targets, max_df, all_statuses):
    tok_docs = {}
    for d in docs.values():
        if d.type == "session":
            continue  # transcripts mention everything; pure noise
        for tok in body_tokens(d):
            tok_docs.setdefault(tok, set()).add(d.id)
    findings = 0
    for tid in targets:
        t = docs.get(tid)
        if not t:
            print(f"?? {tid}: not found", file=sys.stderr)
            continue
        print(f"\n== terms {tid}: {t.title}")
        printed = False
        for tok in sorted(body_tokens(t)):
            family = {}  # matched corpus token -> holder ids
            for other, hids in tok_docs.items():
                if tokens_match(tok, other):
                    family[other] = hids
            holders = set().union(*family.values()) - {tid} \
                if family else set()
            if not holders or len(holders) + 1 > max_df:
                continue
            rows = []
            for hid in sorted(holders):
                h = docs[hid]
                if not all_statuses and h.status not in RATIFIED:
                    continue
                rows.append(h)
            if not rows:
                continue
            printed = True
            via = ", ".join(f"`{o}`" for o in sorted(family)
                            if o != tok)
            print(f"  `{tok}` (df={len(holders) + 1}"
                  + (f"; also matches {via}" if via else "") + ")")
            for h in rows:
                linked = "linked" if directly_linked(t, h) else "NO-LINK"
                findings += linked == "NO-LINK"
                print(f"    {linked:7} {h.id} [{h.status}] {h.title}")
        if not printed:
            print("  no rare-identifier overlap with ratified artifacts.")
    print(f"\nterms: {findings} unlinked rare-identifier co-occurrence(s) "
          "to review.")


def main():
    ap = argparse.ArgumentParser(
        description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--root", default=".", type=Path)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser(
        "sweep", help="relates-to sweep (DEC-0157)",
        description="For each new DEC, list ratified citers of every "
        "accepted decision in its relates-to/supersedes — the partial-"
        "supersession review list.")
    p1.add_argument("ids", nargs="+", help="new decision IDs (DEC-nnnn)")
    p1.add_argument("--all-statuses", action="store_true",
                    help="include non-ratified citers")
    p2 = sub.add_parser(
        "terms", help="identifier co-occurrence audit (DEC-0158)",
        description="Report ratified artifacts sharing rare code-span "
        "identifiers with the new DECs (containment-matched), flagging "
        "unlinked co-occurrences.")
    p2.add_argument("ids", nargs="+", help="new decision IDs (DEC-nnnn)")
    p2.add_argument("--max-df", type=int, default=6,
                    help="ignore identifiers appearing in more docs")
    p2.add_argument("--all-statuses", action="store_true",
                    help="include non-ratified artifacts")
    args = ap.parse_args()

    docs = load_corpus(args.root)
    if not docs:
        print("no artifacts found under --root docs/", file=sys.stderr)
        return 1
    if args.cmd == "sweep":
        cmd_sweep(docs, args.ids, args.all_statuses)
    else:
        cmd_terms(docs, args.ids, args.max_df, args.all_statuses)
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
