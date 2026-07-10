---
id: DEC-0317
type: decision
title: Layered dependencies — stdlib core, opt-in heavy families
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T14-T15"
overview: >-
  The unified CLI's dependencies are layered: the read, write, and
  check subcommand families are pure stdlib and always work via
  python3; the search family (DuckDB + model2vec) and graph family
  (LadybugDB) carry their dependencies as inline uv script metadata
  and load their engines only when invoked, run via uv. One CLI
  surface, no heavy-install tax on the common path — a trivial read
  or a guarded write never pays managed-venv resolution, and the
  heavy engines never become hard requirements of the skill. Chosen
  over a single uv environment for everything (uniform but taxes
  every trivial call and hardens optional deps) and over splitting
  the heavy tools back out as separate scripts (which would re-
  fragment the surface DEC-0316 just unified).
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0316, DEC-0138]
---

# DEC-0317: Layered Dependencies

## Context

The unified CLI (DEC-0316) spans pure-stdlib work (reads, writes,
checks) and engine-backed work (DuckDB/model2vec search, LadybugDB
graph); invocation and dependency handling had to be reconciled.

## Decision

Layered: read/write/check families are pure stdlib, invoked via
`python3`; search/graph families declare their engines as inline uv
metadata, loaded only when those families are invoked, run via `uv`.

## Rationale

The common path (reads and guarded writes, dozens per session) stays
instant and dependency-free; heavy engines stay available without
becoming hard requirements.

## Alternatives Considered

- **Single uv environment for the whole CLI** — uniform invocation
  but every trivial read pays venv resolution and heavy deps become
  mandatory; rejected.
- **Core CLI + separate heavy scripts** — full isolation but
  re-fragments the unified surface; rejected.

## Implications

The build (DEC-0322) structures the entry point so stdlib families
never import engine modules; documentation shows both invocation
forms (python3 for core, uv run for search/graph). The search
family's inherited dependency stance is DEC-0138's (DuckDB without
vss, frontmatter-derived graph features, no LadybugDB in search) —
the operative narrowing of DEC-0116 — not DEC-0116's original
dependency list.
