#!/usr/bin/env python3
"""Cross-sibling impact-coupling check (epic-slicing seams, DEC-0196;
story-slicing seams, DEC-0199).

Flags *mutual* (bidirectional) `impacts` coupling between sibling
epics — or, with `--type story`, between sibling stories/spikes under
the same epic. Run right after a draft sibling set is proposed and its
impact edges are drawn, before any of them is individually refined. A
mutual pair (A impacts B and B impacts A) is a signal, not a verdict,
that the split followed a technical-layer seam (see epic-slicing-seams.md
/ story-slicing-seams.md) rather than a real business/domain boundary;
refinement-process.md's "cycles are normal" guidance still applies, and
this check does not override it — it just surfaces the candidates for
that judgment call before time is spent refining siblings that may need
to be re-seamed.

One-directional fan-out is reported alongside as context only, never as
a finding: a smoke test against this project's own approved epic set
showed that bounded-context slicing (the seam Groundwork's own
EP-0001..EP-0007 actually used) produces near-universal one-way fan-out
from foundational/substrate epics (storage, governance) — that's
expected, not a defect, and a density-threshold flag on it is pure
noise. Mutual coupling is the one mechanically reliable signal here, and
it matters even more at story granularity: INVEST's "Independent"
criterion is a harder requirement for a story than for an epic.

Pure stdlib; no index, no dependencies. Usage:

  python3 groundwork_epic_coupling.py --root <project> check [EP-nnnn ...]
  python3 groundwork_epic_coupling.py --root <project> check --type story [ST-nnnn|SP-nnnn ...]

With no explicit IDs, checks every parent's sibling set separately
(every goal's epics, or every epic's stories+spikes). Advisory: emits a
review list, not a verdict. Exit code 0 always.
"""

import argparse
import re
import os
import sys
from pathlib import Path

TYPE_CONFIG = {
    "epic": {"subdirs": ["epics"], "types": {"epic"}, "noun": "epic"},
    "story": {"subdirs": ["stories", "spikes"],
              "types": {"story", "spike"}, "noun": "story/spike"},
}


def parse_id_list(text):
    return re.findall(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CP|CON|IDEA)-\d{4}\b",
                       text)


class Doc:
    __slots__ = ("id", "path", "type", "status", "title", "links")

    def __init__(self):
        self.id = self.type = self.status = self.title = ""
        self.links = {}
        self.path = None


def parse_doc(path):
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not raw.startswith("---"):
        return None
    end = raw.find("\n---", 3)
    if end < 0:
        return None
    fm = raw[3:end]
    d = Doc()
    d.path = path

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
    return d if d.id else None


def load_docs(root, kind):
    cfg = TYPE_CONFIG[kind]
    docs = {}
    for subdir in cfg["subdirs"]:
        d = root / "docs" / subdir
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            doc = parse_doc(p)
            if doc and doc.type in cfg["types"]:
                docs[doc.id] = doc
    return docs


def parent_groups(docs):
    groups = {}
    for d in docs.values():
        parents = d.links.get("derives-from", []) or ["(no parent)"]
        groups.setdefault(parents[0], []).append(d)
    return groups


def check_group(label, group, noun):
    ids = {e.id for e in group}
    findings = 0
    if len(group) < 2:
        print(f"\n== {label}: {len(group)} {noun} — nothing to compare.")
        return 0

    print(f"\n== {label}: {len(group)} {noun}s")
    edges = 0
    mutual_pairs = []
    seen_pairs = set()
    fanout = {e.id: set() for e in group}
    for e in group:
        for target in e.links.get("impacts", []):
            if target not in ids:
                continue
            edges += 1
            fanout[e.id].add(target)
            fanout[target].add(e.id)
            pair = tuple(sorted((e.id, target)))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            other = next(x for x in group if x.id == target)
            if e.id in other.links.get("impacts", []):
                mutual_pairs.append(pair)

    if mutual_pairs:
        for a, b in sorted(mutual_pairs):
            findings += 1
            print(f"  REVIEW mutual coupling: {a} <-> {b} — cycles are "
                  "normal (refinement-process.md's Impact edges "
                  "section), but confirm this wasn't a technical-layer "
                  "split before refining either in depth; if real, "
                  "resolve via a provisional bounding decision on one "
                  "side.")
    else:
        print("  no mutual (bidirectional) coupling — clear.")

    n = len(group)
    print("  fan-out (informational only — high fan-out from a "
          "foundational/substrate item is normal and expected, not "
          "itself a signal to re-seam; only mutual pairs above are an "
          "actionable finding):")
    for e in sorted(group, key=lambda x: -len(fanout[x.id])):
        print(f"    {e.id} ({e.title}): {len(fanout[e.id])}/{n - 1} "
              "siblings")

    possible = n * (n - 1) / 2
    pairs_touched = len(seen_pairs)
    print(f"  {edges} impact edge(s) across {pairs_touched} pair(s) "
          f"({len(mutual_pairs)} mutual), density "
          f"{pairs_touched / possible:.0%} of {int(possible)} possible "
          "pairs.")
    return findings


def main():
    ap = argparse.ArgumentParser(
        description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--root", default=".", type=Path)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("check", help="cross-sibling impact-coupling check")
    p1.add_argument("ids", nargs="*",
                     help="explicit IDs to check as one sibling set; omit "
                          "to check every parent's sibling set separately")
    p1.add_argument("--type", choices=("epic", "story"), default="epic",
                     help="epic: sibling epics under a goal (default). "
                          "story: sibling stories+spikes under an epic.")
    args = ap.parse_args()

    docs = load_docs(args.root, args.type)
    noun = TYPE_CONFIG[args.type]["noun"]
    if not docs:
        print(f"no {noun}s found under --root", file=sys.stderr)
        return 1

    total = 0
    if args.ids:
        for m in [i for i in args.ids if i not in docs]:
            print(f"?? {m}: not found", file=sys.stderr)
        group = [docs[i] for i in args.ids if i in docs]
        total += check_group("explicit set", group, noun)
    else:
        for parent_id, group in sorted(parent_groups(docs).items()):
            total += check_group(parent_id, group, noun)

    print(f"\ncoupling check: {total} finding(s) to review.")
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
