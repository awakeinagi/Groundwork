---
id: DEC-0126
type: decision
title: CMP-0001 decomposes into thirteen design elements — focused services, lifecycle entities, and the port
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  CMP-0001 comprises thirteen design elements: six services
  (StorageService, BranchOrchestrator, WorktreeManager, IdAllocator,
  MechanicalWriteService, SchemaValidator, CheckSuite); three entities
  (Artifact, ItemBranch, SessionWorktree); one value (ArtifactId); one
  event (ChangeEvent); one protocol (AppDatabasePort). One OpenAPI
  document spans the whole API surface; the element split is a
  contract-organization choice, not deployment. Element-per-story keeps
  contract blocks reviewable and item IDs meaningful.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T1-T2"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0081, DEC-0082, DEC-0092, DEC-0121]
---

# DEC-0126: Element Decomposition of the Artifact Store Service

## Context

The CMP-0001 draft
stub lumped five stories into one StorageService element, left
ST-0007 uncovered, and left
the tier-1 validation library's home undecided
(SES-0022 T1).

## Decision

CMP-0001 comprises **thirteen** design elements:

- **Services**: `StorageService` (core read/write API,
  ST-0002);
  `BranchOrchestrator` (ST-0003);
  `WorktreeManager` (ST-0004);
  `IdAllocator` (ST-0005);
  `MechanicalWriteService` (ST-0006);
  `SchemaValidator` (tier-1 library and schema assets,
  ST-0001);
  `CheckSuite` (tier-2 suite, ST-0007).
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
(DEC-0018) so it
deserves a standalone contract; CheckSuite closes the known
ST-0007 coverage gap inside
the component rather than minting a second CMP and gate. ItemBranch and
SessionWorktree have identity and lifecycle — modeling them as entities
gives the coherence and reconstructibility guarantees a single testable
home instead of restating them across API items.

## Alternatives Considered

- **One StorageService element for ST-0002..ST-0006** — fewer headings,
  unreviewable contract block.
- **Split only IdAllocator** — middle ground; rejected with the full
  split preferred for uniform story↔element mapping.
- **CheckSuite as its own CMP** — a separately deployed CI artifact,
  but it shares the Canonical Store language wholesale and would add a
  second gate before EP-0001 completes.
- **Branch/worktree lifecycles as service behavior items** — no single
  home for the cross-cutting invariants.

## Implications

Settling the thirteen-element inventory at T2 is what let the session proceed — the facilitator explicitly read the inventory back before opening Round 2 on cross-cutting semantics (SES-0022 T3), and the invariant and acceptance-suite decisions of Round 3 were likewise built against this settled element set. The decomposition therefore functions as the foundation the session's later decisions (DEC-0127 through DEC-0133) were reasoned over, not merely a naming exercise. (skeleton restored at SES-0078)
