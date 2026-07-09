#!/usr/bin/env python3
"""Serve the Groundwork docs for the viewer (per DEC-0244).

Usage: python3 tools/serve_docs.py [port]   (default: 8420)

Serves the repository root with directory listings (which
tools/viewer.html uses to discover artifacts) plus /api endpoints that
invoke the vendored .agents skill scripts:

  /api/ping                         → "ok" (viewer probes this)
  /api/search?q=<query>[&k=N]      → semantic search (groundwork_search.py)
  /api/similar?id=<ID>             → similar artifacts (groundwork_search.py)
  /api/graph?cmd=<cmd>[&arg=<x>]   → graph queries (groundwork_graph.py);
                                      cmd ∈ impact|trace|gaps|order|
                                      elements|progress

Falling back to `python3 -m http.server` also works — the viewer then
hides its advanced-search panel (static browsing still fully works).
Requires `uv` on PATH for the /api endpoints.
"""

import re
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = ROOT / ".agents" / "skills" / "groundwork-design-session" \
    / "scripts"
GRAPH_CMDS = {"impact", "trace", "gaps", "order", "elements", "progress"}
ARG_RE = re.compile(r"^[A-Za-z0-9-]{0,40}$")
TIMEOUT = 180


def run_tool(script, args):
    cmd = ["uv", "run", str(SKILL_SCRIPTS / script), "--root", str(ROOT)] \
        + args
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=TIMEOUT)
    except FileNotFoundError:
        return 500, "uv not found on PATH — /api endpoints need uv"
    except subprocess.TimeoutExpired:
        return 504, f"{script} timed out after {TIMEOUT}s"
    out = proc.stdout
    if proc.returncode != 0:
        return 500, (out + "\n" + proc.stderr).strip()
    return 200, out


class Handler(SimpleHTTPRequestHandler):

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def do_GET(self):
        url = urlparse(self.path)
        if not url.path.startswith("/api/"):
            return super().do_GET()
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        status, body = self.api(url.path, q)
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def api(self, path, q):
        if path == "/api/ping":
            return 200, "ok"
        if not SKILL_SCRIPTS.is_dir():
            return 500, f"skill scripts not found at {SKILL_SCRIPTS}"
        if path == "/api/search":
            query = q.get("q", "").strip()
            if not query:
                return 400, "missing q parameter"
            k = q.get("k", "10")
            if not k.isdigit() or not 1 <= int(k) <= 50:
                return 400, "k must be 1..50"
            return run_tool("groundwork_search.py",
                            ["search", query, "--k", k])
        if path == "/api/similar":
            aid = q.get("id", "")
            if not ARG_RE.match(aid) or not aid:
                return 400, "bad id"
            return run_tool("groundwork_search.py", ["similar", aid])
        if path == "/api/graph":
            cmd = q.get("cmd", "")
            if cmd not in GRAPH_CMDS:
                return 400, f"cmd must be one of {sorted(GRAPH_CMDS)}"
            arg = q.get("arg", "")
            if not ARG_RE.match(arg):
                return 400, "bad arg"
            return run_tool("groundwork_graph.py",
                            [cmd] + ([arg] if arg else []))
        return 404, "unknown API endpoint"

    def log_message(self, format, *args):
        if "/api/" in (args[0] if args else ""):
            super().log_message(format, *args)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8420
    addr = ("127.0.0.1", port)
    print(f"Groundwork docs: http://{addr[0]}:{port}/tools/viewer.html")
    ThreadingHTTPServer(addr, Handler).serve_forever()


if __name__ == "__main__":
    main()
