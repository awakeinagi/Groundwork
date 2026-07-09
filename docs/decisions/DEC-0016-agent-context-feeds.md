---
id: DEC-0016
type: decision
title: "Agent context feeds: read-only codebases, Jira backlog, and the doc repo"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T8-T9"
links:
  derives-from: [SES-0001]
---

# DEC-0016: Agent context feeds — codebases, Jira backlog, doc repo

## Context

Refining new goals requires awareness of the existing world
(DEC-0004): current systems,
in-flight backlog, prior decisions.

## Decision

The agent gets three context feeds: (1) read-only codebase access via the
code-host connectors (Bitbucket/GitHub) — what exists today, integration
points, conventions; (2) Jira backlog read access — overlap and conflict
detection against items that never went through Groundwork; (3) the
git-tracked canonical docs themselves, traversed via the cross-reference
graph.

## Rationale

These are the three places organizational truth actually lives. The
cross-reference system and Graph Index
(DEC-0010) exist precisely to make feed
(3) efficiently navigable.

## Alternatives Considered

- **Wiki/Confluence ingestion**: deferred; can be added as another read
  connector later.
- **Human-curated context packs**: evolved into the Consolidation memory
  layer (DEC-0017) rather than a
  manual authoring burden.

## Implications

Code-host and Jira connectors need read scopes from v1 context work; all
feeds sit behind pluggable connector contracts.
