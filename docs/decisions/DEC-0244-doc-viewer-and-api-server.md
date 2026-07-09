---
id: DEC-0244
type: decision
title: A single-file doc viewer plus a skill-backed API server carry human navigability
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0047 @ T4-T6, T8"
links:
  derives-from: [SES-0047]
  relates-to: [DEC-0242, DEC-0138]
---

# DEC-0244: Doc Viewer and API Server

## Context

DEC-0242 removes inline links from the canonical docs, so the human
navigability DEC-0090 provided needs a new home. The stakeholder
upgraded the facilitator's linkify-script recommendation to a proper
browsing surface.

## Decision

Two tools, both in `tools/`:

1. **`viewer.html`** — a single-page webapp, one file, vanilla
   JavaScript: hand-rolled markdown renderer covering the
   checker-constrained dialect the corpus uses, styled with Tailwind
   CSS, Mermaid diagram rendering, eager load of the full corpus at
   startup, discovery by parsing the HTTP server's directory
   listings (no manifest, no derived state). Features: sidebar index
   by type with status badges, clickable bare IDs (linkified at
   render time), full-text search, a backlinks panel ("referenced
   by" — navigation the raw files never had), and frontmatter
   rendered as chips.

2. **`serve_docs.py`** — a stdlib HTTP server that serves the repo
   with directory listings and exposes `/api/` endpoints that invoke
   the vendored `.agents` skill scripts: semantic search
   (`groundwork_search.py`) and graph queries
   (`groundwork_graph.py`). Script output is returned as text and
   rendered in the viewer with artifact IDs auto-linkified, so any
   tool output becomes navigable.

Tailwind and Mermaid load from CDN at view time: the viewer needs
internet when a human opens it. Agents never load the viewer, so
agent workflows are unaffected.

## Rationale

Render-time linkification gives humans strictly more than the old
inline links did — backlinks, search, graph and semantic queries in
one surface — while the canonical files stay agent-optimal. Directory
-listing discovery keeps zero derived state: what is on disk is what
the viewer shows. Plugging the server into the skill scripts reuses
the search and graph investments (DEC-0138) instead of duplicating
them in JavaScript.

## Alternatives Considered

- **CLI linkify script** (facilitator's original recommendation):
  cheap, but produces throwaway renderings with none of the browsing
  affordances.
- **Checker-emitted manifest.json**: would let the viewer run on any
  static host (GitHub Pages), at the cost of a committed derived
  file that can drift; rejected for zero-state discovery, revisitable
  if remote browsing becomes a need.
- **Committed rendered mirror of docs/**: full GitHub navigation,
  double the doc surface, a standing sync invariant — rejected.
- **Embedded markdown library**: robust full-CommonMark rendering,
  but a ~40 KB opaque blob against the vanilla-JS brief; the corpus
  dialect is checker-constrained, so a subset renderer is reliable.

## Implications

`python3 tools/serve_docs.py` (or plain `http.server` with API
features absent) is the documented way to browse the docs; the repo
README/AGENTS.md notes it. The viewer is human-facing tooling, not an
artifact surface — no gate applies beyond normal review.
