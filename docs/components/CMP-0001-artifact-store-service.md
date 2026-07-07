---
id: CMP-0001
type: component
title: Artifact Store Service
status: draft
owner: eng-lead
created: 2026-07-06
context: canonical-store
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0028, DEC-0029, DEC-0030, DEC-0031, DEC-0033, DEC-0034, DEC-0035,
        DEC-0080, DEC-0081, DEC-0082, DEC-0085, DEC-0087, DEC-0088, DEC-0089]
---

# CMP-0001: Artifact Store Service

> Draft stub, birthed by [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md).
> Contract sections are filled in as the epic's stories (ST-0001–ST-0008)
> refine and settle their designs; this component is gate-eligible only
> when contract-complete per
> [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md).
> Structured element-first per
> [DEC-0081](../decisions/DEC-0081-element-first-contract-layout.md).

## Purpose

The single write authority over the Canonical Store: owns the fork-pull
git model, validates every write, allocates IDs, orchestrates item
branches, session worktrees, and gate PRs, executes typed mechanical
writes, and emits the change-event stream every other component consumes.

## Ubiquitous Language

Canonical Store, Artifact, Item Branch, Session Worktree, Mechanical
Write, Gate, Design Element — per [CONTEXT.md](../../CONTEXT.md). No new
terms introduced.

## Design Elements

Candidate elements (per
[DEC-0082](../decisions/DEC-0082-closed-element-type-taxonomy.md)); each
block is itemized as its stories settle. The list is provisional until
gate time.

### StorageService (service)

Pending — API contract (`StorageService.A-*`) from ST-0002 (OpenAPI),
mechanical operations from ST-0006, branch/PR operations from ST-0003;
behavior contract (`StorageService.B-*`) anchors already decided: single
write authority (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md));
branch/PR lifecycle (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md));
worktree concurrency (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md));
mechanical-write inexpressibility of content diffs
(per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md));
append-only sessions
(per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).

### Artifact (entity)

Pending — identity/lifecycle invariants and data contract
(`Artifact.B-*`, `Artifact.D-*`) from the tier-1 schema suite (ST-0001)
and status lifecycle (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
[SPEC-artifact-common](../specs/SPEC-artifact-common.md)).

### ArtifactId (value)

Pending — schema, allocation and immutability invariants
(`ArtifactId.D-*`) from ST-0005
(per [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md),
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

### ChangeEvent (event)

Pending — payload schema and emission/ordering/delivery semantics
(`ChangeEvent.D-*`, `ChangeEvent.B-*`) from ST-0008
(per [DEC-0078](../decisions/DEC-0078-postgres-outbox-events.md)).

## Component Invariants

Pending — cross-element guarantees (`C-*`) itemized as stories settle;
known anchor: the repository remains rebuild-sufficient — all derived
state reconstructible from the fork.

## Implementation Guidance

### Constraints

Pending — candidates from accepted decisions: Postgres transactional
outbox for the event stream
(per [DEC-0078](../decisions/DEC-0078-postgres-outbox-events.md));
ID rescan-on-boot, no durable counter store
(per [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

### Notes

Pending — populated during story implementation refinement (advisory,
per [DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md)).

## Dependencies

- Code-host connector contract (EP-0005 / future standalone
  `protocol`-type CMP per
  [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)) —
  fork, branch, PR, review, protection operations; consumed per its
  capability manifest
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Acceptance & Test Expectations

Pending — assembled from story acceptance criteria; must include the
tier-2 check suite (ST-0007) passing against this repo's bootstrap
corpus.

## Out of Scope

Gate policy logic (Governance engine); graph queries (Graph Index);
retrieval (Memory layer); any UI.
