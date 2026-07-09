#!/usr/bin/env python3
"""Concise, ID-addressed reads over a Groundwork corpus (DEC-0289).

Progressive disclosure: read overviews (DEC-0284) first, open bodies
only when needed. Pure stdlib, no index, no dependencies.

Usage: python3 groundwork_read.py --root <project> <command> ...

Commands:
  overview <ID>... [--type T] [--status S]   batch overviews (IDs and/or filters)
  outline <ID>                               headings; CMP elements w/ Implements
  section <ID> <heading>                     one body section (fuzzy heading match)
  element <CMP-ID> <name>                    one design element's block
  item <CMP-ID> <item-ID>                    one contract item (X.B-1, C-2, IG-1)
  turns <SES-ID> <span>                      transcript turn span (T4 or T4-T6)
  term <name>                                one CONTEXT.md glossary entry
  citers <ID>                                artifacts referencing the ID

Exit codes: 0 ok, 1 not found / bad request, 2 setup problem.
"""

import argparse
import re
import sys
import textwrap
from pathlib import Path

ID_RE = re.compile(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}\b")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
ELEMENT_RE = re.compile(r"^###\s+(\S.*?)\s+\((entity|value|service|event|"
                        r"protocol)\)\s*$")
TURN_RE = re.compile(r"^(?:###\s+T(\d+)\b|\*\*T(\d+)\b)")
SCALAR_KEYS = ("id", "type", "status", "title")


def parse_doc(path):
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not raw.startswith("---"):
        return None
    end = raw.find("\n---\n", 3)
    if end < 0:
        return None
    fm_raw, body = raw[3:end], raw[end + 5:]
    doc = {"path": path, "fm": fm_raw, "body": body, "overview": ""}
    lines = fm_raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z-]+)\s*:\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2)
            if key == "overview":
                if value.startswith((">", "|")) or value == "":
                    block = []
                    i += 1
                    while i < len(lines) and (
                            lines[i].startswith((" ", "\t")) or
                            not lines[i].strip()):
                        block.append(lines[i].strip())
                        i += 1
                    doc["overview"] = " ".join(b for b in block if b)
                    continue
                doc["overview"] = value.strip("\"'")
            elif key in SCALAR_KEYS:
                doc[key] = value.strip("\"'")
        i += 1
    return doc if doc.get("id") else None


def load_corpus(root):
    docs_dir = root / "docs"
    if not docs_dir.is_dir():
        print(f"No docs/ directory under {root}", file=sys.stderr)
        sys.exit(2)
    corpus = {}
    for path in sorted(docs_dir.rglob("*.md")):
        if path.parent.name == "specs" or path.name == "TRIGGERS.md":
            continue
        doc = parse_doc(path)
        if doc:
            corpus[doc["id"]] = doc
    return corpus


def wrap(text, indent="  "):
    return textwrap.fill(text, width=78, initial_indent=indent,
                         subsequent_indent=indent)


def get(corpus, aid):
    doc = corpus.get(aid)
    if not doc:
        print(f"{aid}: no such artifact", file=sys.stderr)
        sys.exit(1)
    return doc


def header(doc):
    return f"{doc['id']} [{doc.get('status', '?')}] {doc.get('title', '')}"


def cmd_overview(corpus, ids, type_f, status_f):
    picked = []
    if ids:
        picked = [get(corpus, a) for a in ids]
    if type_f or status_f:
        filtered = [d for d in corpus.values()
                    if (not type_f or d.get("type") == type_f) and
                       (not status_f or d.get("status") == status_f)]
        picked = ([d for d in picked if d in filtered]
                  if ids else sorted(filtered, key=lambda d: d["id"]))
    if not picked:
        print("nothing matched", file=sys.stderr)
        return 1
    for doc in picked:
        print(header(doc))
        print(wrap(doc["overview"] or "(no overview)"))
        print()
    return 0


def cmd_outline(corpus, aid):
    doc = get(corpus, aid)
    print(header(doc))
    lines = doc["body"].splitlines()
    in_code = False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        depth = len(m.group(1)) - 2
        print("  " * depth + "- " + m.group(2))
        e = ELEMENT_RE.match(line)
        if e:
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip().startswith("Implements:"):
                    impl = [lines[j].strip()]
                    for cont in lines[j + 1:]:
                        if not cont.strip() or HEADING_RE.match(cont):
                            break
                        impl.append(cont.strip())
                    print("  " * (depth + 1) + " ".join(impl))
                    break
    return 0


def section_slice(body, match_fn):
    """Return the lines of the first section whose heading satisfies
    match_fn, up to the next heading of the same or higher level."""
    lines = body.splitlines()
    out, level, in_code = [], None, False
    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
        m = HEADING_RE.match(line) if not in_code else None
        if level is None:
            if m and match_fn(m.group(2)):
                level = len(m.group(1))
                out.append(line)
        else:
            if m and len(m.group(1)) <= level:
                break
            out.append(line)
    return out if level is not None else None


def cmd_section(corpus, aid, heading):
    doc = get(corpus, aid)
    want = heading.lower()
    out = section_slice(doc["body"], lambda h: want in h.lower())
    if out is None:
        print(f"{aid}: no section matching {heading!r}", file=sys.stderr)
        return 1
    print(header(doc))
    print("\n".join(out).rstrip())
    return 0


def cmd_element(corpus, aid, name):
    doc = get(corpus, aid)
    want = name.lower()

    def match(h):
        e = re.match(r"^(\S.*?)\s+\((entity|value|service|event|protocol)\)$",
                     h)
        return bool(e) and want in e.group(1).lower()

    out = section_slice(doc["body"], match)
    if out is None:
        print(f"{aid}: no design element matching {name!r}", file=sys.stderr)
        return 1
    print(header(doc))
    print("\n".join(out).rstrip())
    return 0


def cmd_item(corpus, aid, item_id):
    doc = get(corpus, aid)
    pat = re.compile(r"^\s*-\s+[`*]{0,2}" + re.escape(item_id) +
                     r"[`*]{0,2}\s*[:—–-]")
    lines = doc["body"].splitlines()
    out = []
    for i, line in enumerate(lines):
        if not pat.match(line):
            continue
        out.append(line)
        for follow in lines[i + 1:]:
            if (re.match(r"^\s*-\s", follow) or HEADING_RE.match(follow)
                    or not follow.strip()):
                break
            out.append(follow)
        break
    if not out:
        print(f"{aid}: no contract item {item_id!r}", file=sys.stderr)
        return 1
    print(header(doc))
    print("\n".join(out))
    return 0


def cmd_turns(corpus, aid, span):
    doc = get(corpus, aid)
    m = re.match(r"^T(\d+)(?:-T?(\d+))?$", span, re.IGNORECASE)
    if not m:
        print(f"bad span {span!r} — use T4 or T4-T6", file=sys.stderr)
        return 1
    lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
    lines = doc["body"].splitlines()
    out, current = [], None
    for line in lines:
        t = TURN_RE.match(line)
        if t:
            current = int(t.group(1) or t.group(2))
        elif current is None and HEADING_RE.match(line):
            current = None
        if current is not None and lo <= current <= hi:
            out.append(line)
        elif current is not None and current > hi:
            break
    if not out:
        print(f"{aid}: no turns in {span}", file=sys.stderr)
        return 1
    print(header(doc))
    print("\n".join(out).rstrip())
    return 0


def cmd_term(root, name):
    ctx = root / "CONTEXT.md"
    if not ctx.is_file():
        print("no CONTEXT.md", file=sys.stderr)
        return 2
    want = name.lower()
    lines = ctx.read_text(encoding="utf-8").splitlines()
    out = []
    for i, line in enumerate(lines):
        m = re.match(r"^-\s+\*\*(.+?)\*\*", line)
        if not (m and want in m.group(1).lower()):
            continue
        out.append(line)
        for follow in lines[i + 1:]:
            if re.match(r"^-\s+\*\*", follow) or follow.startswith("#") \
                    or not follow.strip():
                break
            out.append(follow)
        out.append("")
    if not out:
        print(f"no glossary term matching {name!r}", file=sys.stderr)
        return 1
    print("\n".join(out).rstrip())
    return 0


def cmd_citers(corpus, aid):
    get(corpus, aid)
    hits = []
    for doc in sorted(corpus.values(), key=lambda d: d["id"]):
        if doc["id"] == aid:
            continue
        where = []
        if aid in ID_RE.findall(doc["fm"]):
            where.append("frontmatter")
        if aid in ID_RE.findall(doc["body"]):
            where.append("body")
        if where:
            hits.append(f"{header(doc)}  ({', '.join(where)})")
    if not hits:
        print(f"nothing references {aid}")
        return 0
    print(f"{len(hits)} artifact(s) reference {aid}:")
    for h in hits:
        print("  " + h)
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Concise, ID-addressed reads over a Groundwork corpus")
    ap.add_argument("--root", default=".", help="project root")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("overview")
    p.add_argument("ids", nargs="*")
    p.add_argument("--type", dest="type_f")
    p.add_argument("--status", dest="status_f")
    p = sub.add_parser("outline")
    p.add_argument("id")
    p = sub.add_parser("section")
    p.add_argument("id")
    p.add_argument("heading")
    p = sub.add_parser("element")
    p.add_argument("id")
    p.add_argument("name")
    p = sub.add_parser("item")
    p.add_argument("id")
    p.add_argument("item_id")
    p = sub.add_parser("turns")
    p.add_argument("id")
    p.add_argument("span")
    p = sub.add_parser("term")
    p.add_argument("name")
    p = sub.add_parser("citers")
    p.add_argument("id")

    args = ap.parse_args()
    root = Path(args.root).resolve()
    if args.cmd == "term":
        sys.exit(cmd_term(root, args.name))
    corpus = load_corpus(root)
    if args.cmd == "overview":
        if not args.ids and not args.type_f and not args.status_f:
            print("give IDs and/or --type/--status", file=sys.stderr)
            sys.exit(1)
        sys.exit(cmd_overview(corpus, args.ids, args.type_f, args.status_f))
    if args.cmd == "outline":
        sys.exit(cmd_outline(corpus, args.id))
    if args.cmd == "section":
        sys.exit(cmd_section(corpus, args.id, args.heading))
    if args.cmd == "element":
        sys.exit(cmd_element(corpus, args.id, args.name))
    if args.cmd == "item":
        sys.exit(cmd_item(corpus, args.id, args.item_id))
    if args.cmd == "turns":
        sys.exit(cmd_turns(corpus, args.id, args.span))
    if args.cmd == "citers":
        sys.exit(cmd_citers(corpus, args.id))


if __name__ == "__main__":
    main()
