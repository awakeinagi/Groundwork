---
id: EP-0001
type: epic
title: Artifact Store & Format Engine
status: draft
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
cites: [DEC-0008, DEC-0009, DEC-0002, DEC-0018]
---

# EP-0001: Artifact Store & Format Engine

## Summary

The canonical heart of Groundwork: a storage service that owns the git-backed
markdown repository, allocates immutable artifact IDs, validates every write
against the artifact format specs, and enforces link-graph integrity. All
reads and writes — UI, agents, connectors — go through its API; nothing else
touches the repository.

## Why (Goal Alignment)

BG-0001's traceability outcome depends on artifacts being well-formed and
their links resolvable at all times ([DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)).
Canonical-store discipline ([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md))
only holds if a single component mediates access to the git repo
([DEC-0008](../decisions/DEC-0008-git-backed-markdown-store.md)).

## Scope

**In:** storage API (CRUD over artifacts, structured queries by type/status);
ID allocation (sequential per prefix, never reused); frontmatter schema
validation per type spec; status-lifecycle transition enforcement; link
integrity checking (the productionized `tools/check_links.py` rules); git
plumbing (commits, refs, history) hidden behind the interface.

**Out:** graph queries (EP-0004); gate approval logic (EP-0003 — this epic
only enforces that transitions come from the gate engine); rendering (EP-0006).

## Domain Context

Bounded context: **Canonical Store**. Terms: Artifact, Canonical Store,
status lifecycle (draft/in-refinement/gated/approved/stale/superseded/
archived) — all per [CONTEXT.md](../../CONTEXT.md) and
[SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Storage API contract**: language-neutral (OpenAPI) so backends other
  than git-markdown remain swappable ([DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
- **Artifact schema definitions**: machine-readable (JSON Schema) versions
  of each SPEC's frontmatter.
- **Change-event stream**: artifact-changed events consumed by the Graph
  Index (EP-0004), impact analysis (EP-0003), and consolidation freshness
  (EP-0007).

## Risks & Open Questions

- Concurrent writes to one artifact (agent + human): optimistic locking vs.
  git merge semantics — candidate spike.
- Where transcript append-only enforcement lives: store layer or session
  agent.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
