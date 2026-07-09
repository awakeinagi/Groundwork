---
id: DEC-0117
type: decision
title: The search index auto-refreshes on every search; graph staleness is detected and warned
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T5-T6, T13"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0112, DEC-0116, DEC-0119]
---

# DEC-0117: Auto-Refresh on Search; Graph-Staleness Warning

## Context

Derived views drift from the docs. The graph tool uses explicit
`build`/`sync` discipline; a search index serving yesterday's
embeddings looks exactly like a healthy one — stale results are
silent. And the hybrid features depend on a *second* derived view (the
graph) with its own freshness: POC 2 accidentally discovered the live
`.groundwork-graph` was missing
SES-0018's decisions
entirely, which silently disables `SUPERSEDES` redirects exactly for
the newest decisions.

## Decision

Every `search` (and `similar`) invocation **first reconciles the index
with the docs** — per-file content hashes; only changed, new, or
deleted files are re-embedded — then queries. The tool also **checks
graph freshness** (the `.groundwork-graph` file's age against the
newest doc and its own index state) and prints a loud warning naming
the rebuild command when the graph is stale or missing; hybrid
features degrade gracefully rather than failing.

## Rationale

Static embeddings make this affordable: full corpus re-embed measured
at 0.14 s, incremental refresh near-instant — so the index can simply
never serve stale results, and there is no sync discipline for the
agent to forget. The graph cannot be auto-rebuilt from the search tool
(it is another tool's artifact and a slower build); detection plus a
loud warning is the honest boundary.

## Alternatives Considered

- **Explicit build/sync like the graph tool**: consistent discipline,
  but stale-search bugs are silent where stale-graph bugs at least
  surface as missing nodes.
- **Full rebuild every search**: no hash bookkeeping, but hard-codes
  the corpus staying small.
- **Auto-rebuilding the graph too**: crosses tool ownership and turns
  a 35 ms search into a multi-second graph build without the user
  asking.

## Implications

Status changes (e.g., a DEC becoming superseded) reach the index
automatically, since editing frontmatter changes the file hash — the
`--current` filter and redirect annotations of
DEC-0119 stay correct
without ceremony.
