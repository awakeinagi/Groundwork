#!/usr/bin/env python3
"""Mechanically write/replace the frontmatter `overview:` field of a
Groundwork artifact (SPEC-artifact-common.md; DEC-0284..DEC-0288).

Usage:
    python3 set_overview.py <artifact.md> --text-file <text.txt>
    python3 set_overview.py <artifact.md> --text "inline overview text"

Composes the YAML folded block scalar (`overview: >-`, 2-space indent,
lines <=76 chars) from the given prose and inserts it into the
frontmatter at the position every existing artifact uses: immediately
before the first of `component-type:` / `links:` / `sources:` (falling
back to right after `created:` if none of those keys are present,
which should not happen on a well-formed artifact). If an `overview:`
field already exists, it is removed first. Nothing else in the file is
touched -- not the body, not any other frontmatter field.

Stdlib only, no dependencies.
"""
import argparse
import re
import sys
from pathlib import Path

WRAP_WIDTH = 76
INDENT = "  "
ANCHOR_RE = re.compile(r"^(component-type|links|sources):")


def wrap(text, width=WRAP_WIDTH, indent=INDENT):
    words = text.split()
    if not words:
        return []
    lines, cur = [], ""
    for w in words:
        candidate = f"{cur} {w}".strip()
        if len(indent) + len(candidate) > width and cur:
            lines.append(indent + cur)
            cur = w
        else:
            cur = candidate
    if cur:
        lines.append(indent + cur)
    return lines


def strip_existing_overview(fm_lines):
    out = []
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if line.startswith("overview:"):
            i += 1
            while i < len(fm_lines) and (not fm_lines[i] or fm_lines[i][0].isspace()):
                i += 1
            continue
        out.append(line)
        i += 1
    return out


def insert_overview(fm_lines, new_block):
    anchor = next((idx for idx, l in enumerate(fm_lines) if ANCHOR_RE.match(l)), None)
    if anchor is not None:
        fm_lines[anchor:anchor] = new_block
        return fm_lines
    created = next((idx for idx, l in enumerate(fm_lines) if l.startswith("created:")), None)
    if created is None:
        sys.exit("error: found none of component-type:/links:/sources:/created: "
                  "to anchor the overview: field to")
    print("warning: no component-type:/links:/sources: key found; "
          "inserted overview: right after created: instead", file=sys.stderr)
    fm_lines[created + 1:created + 1] = new_block
    return fm_lines


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("artifact")
    ap.add_argument("--text", help="overview text, inline")
    ap.add_argument("--text-file", help="path to a file containing the overview text")
    args = ap.parse_args()

    if bool(args.text) == bool(args.text_file):
        sys.exit("error: pass exactly one of --text or --text-file")

    raw = args.text if args.text else Path(args.text_file).read_text()
    text = " ".join(raw.split())
    if not text:
        sys.exit("error: overview text is empty")

    path = Path(args.artifact)
    if not path.is_file():
        sys.exit(f"error: {path} not found")
    content = path.read_text()
    if not content.startswith("---\n"):
        sys.exit(f"error: {path} has no frontmatter block (must start with '---')")
    try:
        end = content.index("\n---\n", 4)
    except ValueError:
        sys.exit(f"error: {path} frontmatter block is not terminated with '---'")

    fm_lines = content[4:end].split("\n")
    body = content[end:]  # starts with "\n---\n"

    fm_lines = strip_existing_overview(fm_lines)
    new_block = ["overview: >-"] + wrap(text)
    fm_lines = insert_overview(fm_lines, new_block)

    path.write_text("---\n" + "\n".join(fm_lines) + body)
    word_count = len(text.split())
    print(f"{path}: overview set ({word_count} words)")
    if word_count > 250:
        print(f"warning: {word_count} words exceeds the 250-word cap "
              f"(DEC-0286) -- shorten it, then re-run this script",
              file=sys.stderr)


if __name__ == "__main__":
    main()
