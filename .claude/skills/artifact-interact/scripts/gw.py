#!/usr/bin/env python3
"""gw — the unified Groundwork artifact CLI (DEC-0316).

One entry point, subcommand families, uniform --root convention:

  read         concise ID-addressed reads (overview, outline, section,
               element, item, turns, term, citers)         [stdlib]
  write        typed, guardrailed write operations (create, set-status,
               add-link, add-cite, update-overview, edit-section,
               append-turn, supersede, apply)               [stdlib]
  check        full integrity suite (the pre-commit gate)   [stdlib]
  status       project status report                        [stdlib]
  consistency  post-distillation sweeps (sweep, terms)      [stdlib]
  coupling     sibling impact-coupling check                [stdlib]
  search       hybrid semantic search + recall audit        [uv-run]
  graph        LadybugDB graph queries                      [uv-run]

Dependencies are layered (DEC-0317): the common path is pure stdlib and
runs under python3; search and graph carry inline uv metadata and load
their engines only when invoked (requires `uv` on PATH).

Usage: python3 gw.py [--root DIR] <family> [args...]
       python3 gw.py <family> --help
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
