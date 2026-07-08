---
id: DEC-0126
type: decision
title: CMP-0001 decomposes into thirteen design elements — focused services, lifecycle entities, and the port
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T1-T2"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0081, DEC-0082, DEC-0092, DEC-0121]
---

# DEC-0126: Element Decomposition of the Artifact Store Service

## Context

The [CMP-0001](../components/CMP-0001-artifact-store-service.md) draft
stub lumped five stories into one StorageService element, left
[ST-0007](../stories/ST-0007-tier2-check-suite.md) uncovered, and left
the tier-1 validation library's home undecided
([SES-0022](../sessions/SES-0022-cmp-0001-contract-refinement.md) T1).

## Decision

[CMP-0001](../components/CMP-0001-artifact-store-service.md) comprises **thirteen** design elements:

- **Services**: `StorageService` (core read/write API,
  [ST-0002](../stories/ST-0002-storage-api-core.md));
  `BranchOrchestrator` ([ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md));
  `WorktreeManager` ([ST-0004](../stories/ST-0004-session-worktree-management.md));
  `IdAllocator` ([ST-0005](../stories/ST-0005-id-allocation.md));
  `MechanicalWriteService` ([ST-0006](../stories/ST-0006-typed-mechanical-writes.md));
  `SchemaValidator` (tier-1 library and schema assets,
  [ST-0001](../stories/ST-0001-tier1-schema-suite.md));
  `CheckSuite` (tier-2 suite, [ST-0007](../stories/ST-0007-tier2-check-suite.md)).
- **Entities**: `Artifact`; `ItemBranch` (branch/PR lifecycle and
  status-coherence home); `SessionWorktree` (worktree lifecycle and
  restart-reconstructibility home).
- **Value**: `ArtifactId`. **Event**: `ChangeEvent`.
- **Protocol**: `AppDatabasePort`.

One OpenAPI document still spans the whole API surface; the element
split is a contract-organization choice, not a deployment one.

## Rationale

Element-per-story keeps contract blocks reviewable and item IDs
meaningful; a single mega-service would run to dozens of unrelated
items. SchemaValidator is independently reimplementable
([DEC-0018](DEC-0018-python-backend-language-agnostic-specs.md)) so it
deserves a standalone contract; CheckSuite closes the known
[ST-0007](../stories/ST-0007-tier2-check-suite.md) coverage gap inside
the component rather than minting a second CMP and gate. ItemBranch and
SessionWorktree have identity and lifecycle — modeling them as entities
gives the coherence and reconstructibility guarantees a single testable
home instead of restating them across API items.

## Alternatives Considered

- **One StorageService element for [ST-0002](../stories/ST-0002-storage-api-core.md)..[ST-0006](../stories/ST-0006-typed-mechanical-writes.md)** — fewer headings,
  unreviewable contract block.
- **Split only IdAllocator** — middle ground; rejected with the full
  split preferred for uniform story↔element mapping.
- **CheckSuite as its own CMP** — a separately deployed CI artifact,
  but it shares the Canonical Store language wholesale and would add a
  second gate before [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) completes.
- **Branch/worktree lifecycles as service behavior items** — no single
  home for the cross-cutting invariants.
