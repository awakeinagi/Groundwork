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
        DEC-0080, DEC-0081, DEC-0082, DEC-0085, DEC-0087, DEC-0088, DEC-0089,
        DEC-0092, DEC-0093, DEC-0121, DEC-0122, DEC-0124]
---

# CMP-0001: Artifact Store Service

> Draft stub, birthed by [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md).
> Contract sections are filled in as the epic's stories ([ST-0001](../stories/ST-0001-tier1-schema-suite.md)–[ST-0008](../stories/ST-0008-change-event-stream.md))
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
gate time. Known coverage gap (per
[DEC-0093](../decisions/DEC-0093-story-design-coverage-check.md)):
[ST-0007](../stories/ST-0007-tier2-check-suite.md) has no referencing
element yet — a check-suite service element is expected to close it
before this doc gates.

### StorageService (service)

Implements: [ST-0002](../stories/ST-0002-storage-api-core.md),
[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md),
[ST-0004](../stories/ST-0004-session-worktree-management.md),
[ST-0005](../stories/ST-0005-id-allocation.md),
[ST-0006](../stories/ST-0006-typed-mechanical-writes.md)

Pending — API contract (`StorageService.A-*`) from [ST-0002](../stories/ST-0002-storage-api-core.md) (OpenAPI),
mechanical operations from [ST-0006](../stories/ST-0006-typed-mechanical-writes.md), branch/PR operations from [ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md);
behavior contract (`StorageService.B-*`) anchors already decided: single
write authority (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md));
branch/PR lifecycle (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md));
worktree concurrency (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md));
mechanical-write inexpressibility of content diffs
(per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md));
append-only sessions
(per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).

### Artifact (entity)

Implements: [ST-0001](../stories/ST-0001-tier1-schema-suite.md)

Pending — identity/lifecycle invariants and data contract
(`Artifact.B-*`, `Artifact.D-*`) from the tier-1 schema suite ([ST-0001](../stories/ST-0001-tier1-schema-suite.md))
and status lifecycle (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
[SPEC-artifact-common](../specs/SPEC-artifact-common.md)).

### ArtifactId (value)

Implements: [ST-0005](../stories/ST-0005-id-allocation.md)

Pending — schema, allocation and immutability invariants
(`ArtifactId.D-*`) from [ST-0005](../stories/ST-0005-id-allocation.md)
(per [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md),
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

### ChangeEvent (event)

Implements: [ST-0008](../stories/ST-0008-change-event-stream.md)

Pending — payload schema and emission/ordering/delivery semantics
(`ChangeEvent.D-*`, `ChangeEvent.B-*`) from [ST-0008](../stories/ST-0008-change-event-stream.md)
(per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).

### AppDatabasePort (protocol)

Implements: [ST-0008](../stories/ST-0008-change-event-stream.md)

Pending — the Port for this component's relational/transactional
workload: outbox tables
(per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)) and
service bookkeeping. Contract obligations
(`AppDatabasePort.A-*`, `AppDatabasePort.B-*`) itemized as [ST-0008](../stories/ST-0008-change-event-stream.md)
settles: operations the consumers require, transactional guarantees,
and the conformance suite any Adapter must pass
(per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
[DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)); v1
Adapter is DuckDB only
(per [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).

## Component Invariants

Pending — cross-element guarantees (`C-*`) itemized as stories settle;
known anchor: the repository remains rebuild-sufficient — all derived
state reconstructible from the fork.

## Implementation Guidance

### Constraints

Pending — candidates from accepted decisions: transactional outbox in
the app database, DuckDB in v1
(per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md));
embedded v1 storage stack
(per [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md));
app-database access only through the AppDatabasePort, Adapter selected
by deployment configuration
(per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
[DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
[DEC-0124](../decisions/DEC-0124-v1-adapter-set.md));
ID rescan-on-boot, no durable counter store
(per [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

### Notes

Pending — populated during story implementation refinement (advisory,
per [DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md)).

## Dependencies

- Code-host connector contract ([EP-0005](../epics/EP-0005-connectors-and-identity.md) / future standalone
  `protocol`-type CMP per
  [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)) —
  fork, branch, PR, review, protection operations; consumed per its
  capability manifest
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Acceptance & Test Expectations

Pending — assembled from story acceptance criteria; must include the
tier-2 check suite ([ST-0007](../stories/ST-0007-tier2-check-suite.md)) passing against this repo's bootstrap
corpus.

## Out of Scope

Gate policy logic (Governance engine); graph queries (Graph Index);
retrieval (Memory layer); any UI.
