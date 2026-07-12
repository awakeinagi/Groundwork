---
id: DEC-0138
type: decision
title: The POC retrieval is promoted into the skill's groundwork_search.py, with implementation stances recorded
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  POC retrieval audit is promoted into skill's groundwork_search.py
  implementing search, similar, audit, and build per accepted semantics.
  Hybrid graph features compute from frontmatter links directly (one-hop
  boost, subtree closure, redirect) without LadybugDB read-only dependency.
  The vss extension is not loaded; similarity is brute-force. Both stances
  are reversible and scoped to implementation, leaving every accepted
  retrieval semantic intact. Verification during promotion caught and fixed
  index-refresh defect.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0024 @ T2-T3, T6"
links:
  derives-from: [SES-0024]
  relates-to: [DEC-0111, DEC-0113, DEC-0114, DEC-0116, DEC-0117, DEC-0118, DEC-0119, DEC-0137, DEC-0372]
---

# DEC-0138: Promote the Audit POC into groundwork_search.py

## Context

DEC-0116 designed
`scripts/groundwork_search.py` but it had not been built; the audit POC
(SES-0024) de-risked
its retrieval core.

## Decision

The POC is promoted into the skill's `scripts/groundwork_search.py`
implementing `search`, `similar`, `audit`, and `build` per the accepted
semantics (DEC-0111,
DEC-0113,
DEC-0114,
DEC-0117,
DEC-0118,
DEC-0119), with two recorded
implementation stances:

1. **Hybrid graph features compute from frontmatter links directly**
   (one-hop boost with 0.25 decay, `--within` subtree closure,
   superseded redirect) — the same edges
   DEC-0119 names, without
   the read-only LadybugDB dependency of
   DEC-0116's
   dependency list. The graph tool remains authoritative for
   provenance traversal; the staleness warning of
   DEC-0117 is kept.
2. **The vss extension is not loaded**: similarity is brute-force
   (already mandated by DEC-0114);
   vss returns with HNSW if
   SP-0003 revives.

## Rationale

The edges are twenty lines of frontmatter parsing; importing a graph
engine to read them adds a dependency without semantics. Both stances
are reversible and scoped to implementation, leaving every accepted
retrieval semantic intact.

## Alternatives Considered

- **Implement DEC-0116's dependency list verbatim** — ladybug read-only
  + vss loaded; rejected as dependencies without behavior at current
  corpus scale.

## Implications

Verification during promotion caught and fixed an index-refresh defect
(dedupe snapshot taken before deleting a changed file's chunks
suppressed re-insertion of its unchanged sections). `.groundwork-search`
joins `.groundwork-graph` in `.gitignore`.
