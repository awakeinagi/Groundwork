#!/usr/bin/env python3
"""gw — the unified Groundwork artifact CLI (DEC-0316).

One entry point, subcommand families, uniform --root convention:

  read         concise ID-addressed reads                   [stdlib]
               overview | outline | section | element | item | turns
               | term | citers
  write        typed, guardrailed write operations          [stdlib]
               create | set-status | add-link | add-cite | remove-cite
               | update-overview | edit-section | delete-section
               | append-turn | supersede | apply (JSON batch)
  check        full integrity suite (the pre-commit gate)   [stdlib]
  status       project status report                        [stdlib]
  consistency  post-distillation sweeps: sweep | terms      [stdlib]
  coupling     sibling impact-coupling check: check         [stdlib]
  search       semantic search + recall audit:              [uv-run]
               search | similar | audit | build
  graph        LadybugDB graph queries: build | impact | trace
               | order | gaps | elements | percent | query  [uv-run]

Dependencies are layered (DEC-0317): the common path is pure stdlib and
runs under python3; search and graph carry inline uv metadata and load
their engines only when invoked (requires `uv` on PATH).

Usage: python3 gw.py [--root DIR] <family> [args...]
       python3 gw.py <family> --help              family overview
       python3 gw.py <family> <subcommand> --help subcommand details

Examples:
  gw.py --root . read overview --type idea --status captured
  gw.py --root . read section EP-0009 "Derived Work"
  gw.py --root . write create --type idea --title "T" --overview "..."
  echo "New body." | gw.py --root . write edit-section SES-0077 Purpose
  gw.py --root . write apply ops.json
  gw.py --root . search audit SES-0077 --output packet.json
  gw.py --root . graph impact DEC-0325
  gw.py --root . check
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

FAMILIES = {
    "read": ("python3", "groundwork_read.py"),
    "write": ("python3", "gw_write.py"),
    "status": ("python3", "status_report.py"),
    "consistency": ("python3", "groundwork_consistency.py"),
    "coupling": ("python3", "groundwork_epic_coupling.py"),
    "search": ("uv", "groundwork_search.py"),
    "graph": ("uv", "groundwork_graph.py"),
    "check": ("python3", "check_links.py"),
}


def main():
    argv = sys.argv[1:]
    root = "."
    if argv[:1] == ["--root"] and len(argv) >= 2:
        root, argv = argv[1], argv[2:]
    if not argv or argv[0] in ("-h", "--help"):
        print((__doc__ or "").strip())
        sys.exit(0)
    family, rest = argv[0], argv[1:]
    if family not in FAMILIES:
        print(f"unknown family {family!r}; one of {sorted(FAMILIES)}",
              file=sys.stderr)
        sys.exit(2)
    runner, script = FAMILIES[family]

    if family == "check":
        # check_links.py scans the project it runs in; execute from root.
        cmd = [sys.executable, str(HERE / script)]
        sys.exit(subprocess.call(cmd, cwd=Path(root).resolve()))

    if runner == "uv":
        if not shutil.which("uv"):
            print(f"the {family} family needs `uv` on PATH (DEC-0317); "
                  "read/write/check/status remain available via python3",
                  file=sys.stderr)
            sys.exit(2)
        cmd = ["uv", "run", str(HERE / script), "--root", root] + rest
    else:
        # status_report.py takes the root positionally.
        if family == "status":
            cmd = [sys.executable, str(HERE / script), root] + rest
        else:
            cmd = [sys.executable, str(HERE / script), "--root", root] + rest
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    main()
