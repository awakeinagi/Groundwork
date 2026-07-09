#!/usr/bin/env python3
"""Validate the frontmatter `overview:` field of Groundwork artifacts
against DEC-0287's integrity rule: non-empty, at most 250 words, and
every bare artifact ID inside it resolves to an existing artifact.

This mirrors tools/check_links.py's rule 19 exactly (same word-count
method, same ID pattern), so a clean run here is also a clean run of
that rule for the files checked.

Usage:
    python3 validate_overview.py <artifact.md> [<artifact.md> ...]
    python3 validate_overview.py --all [--root <project_root>]

Exit code 0 if every checked file passes, 1 if any fails.
Stdlib only, no dependencies.
"""
import argparse
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}\b")
FILENAME_ID_RE = re.compile(r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}")
BLOCK_SCALAR_INDICATORS = {">-", ">", "|-", "|", ">+", "|+"}


def build_id_index(root):
    ids = set()
    for p in root.rglob("*.md"):
        m = FILENAME_ID_RE.match(p.name)
        if m:
            ids.add(p.name[:m.end()])
    return ids


def extract_overview(content):
    """Returns (overview_text_or_None, error_or_None)."""
    if not content.startswith("---\n"):
        return None, "no frontmatter block (file does not start with '---')"
    try:
        end = content.index("\n---\n", 4)
    except ValueError:
        return None, "frontmatter block is not terminated with '---'"
    fm_lines = content[4:end].split("\n")

    i = 0
    while i < len(fm_lines) and not fm_lines[i].startswith("overview:"):
        i += 1
    if i == len(fm_lines):
        return None, "missing overview: field"

    first = fm_lines[i][len("overview:"):].strip()
    parts = [] if (not first or first in BLOCK_SCALAR_INDICATORS) else [first]
    i += 1
    while i < len(fm_lines) and (not fm_lines[i] or fm_lines[i][0].isspace()):
        if fm_lines[i].strip():
            parts.append(fm_lines[i].strip())
        i += 1

    return " ".join(parts), None


def validate_file(path, id_index):
    content = path.read_text()
    text, err = extract_overview(content)
    if err or text is None:
        return [err or "missing overview: field"]
    if not text.strip():
        return ["overview: field is present but empty"]

    problems = []
    words = text.split()
    if len(words) > 250:
        problems.append(f"overview is {len(words)} words (max 250, DEC-0286)")
    for m in ID_RE.finditer(text):
        if m.group(0) not in id_index:
            problems.append(f"overview references {m.group(0)}, which does not resolve")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="artifact file paths")
    ap.add_argument("--all", action="store_true",
                     help="validate every artifact file under <root>/docs")
    ap.add_argument("--root", default=".", help="project root (default: cwd)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    docs = root / "docs"
    id_index = build_id_index(docs if docs.is_dir() else root)

    if args.all:
        if not docs.is_dir():
            sys.exit(f"error: {docs} not found")
        files = sorted(p for p in docs.rglob("*.md") if FILENAME_ID_RE.match(p.name))
    else:
        if not args.files:
            sys.exit("error: pass one or more file paths, or --all")
        files = [Path(f) for f in args.files]

    failed = 0
    for f in files:
        if not f.is_file():
            print(f"FAIL {f}\n  - file not found")
            failed += 1
            continue
        problems = validate_file(f, id_index)
        if problems:
            failed += 1
            print(f"FAIL {f}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"ok   {f}")

    print(f"\n{len(files) - failed}/{len(files)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
