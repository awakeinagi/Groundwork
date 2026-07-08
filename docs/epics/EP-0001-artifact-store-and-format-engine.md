---
id: EP-0001
type: epic
title: Artifact Store & Format Engine
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  impacts: [EP-0002, EP-0003, EP-0004, EP-0005, EP-0006, EP-0007, EP-0008]
  impacted-by: [EP-0003, EP-0005]
cites: [DEC-0008, DEC-0009, DEC-0002, DEC-0018, DEC-0026, DEC-0028, DEC-0029,
        DEC-0030, DEC-0031, DEC-0033, DEC-0034, DEC-0035, DEC-0121, DEC-0122,
        DEC-0124]
---

# EP-0001: Artifact Store & Format Engine

## Summary

The canonical heart of Groundwork: a storage service that owns the fork-pull
git model over the upstream doc repository, allocates immutable artifact
IDs, validates every write, orchestrates item branches, session worktrees,
and gate PRs, and enforces link-graph integrity. All writes — UI, agents,
connectors — go through its API; nothing else holds write credentials to the
repository.

## Why (Goal Alignment)

[BG-0001](../goals/BG-0001-groundwork.md)'s traceability outcome depends on artifacts being well-formed and
their links resolvable at all times ([DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)).
Canonical-store discipline ([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md))
holds because this service is the single write authority
([DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)); human
ratification is durable because gate sign-off is PR approval on the upstream
repository ([DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).

## Scope

**In** (refined at [SES-0003](../sessions/SES-0003-ep-0001-refinement.md)):

- **Git model** ([DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)):
  application-owned fork of upstream; one item branch per artifact under
  refinement, carrying the item plus its sessions and decisions; PR to
  upstream main opened with the branch; merge = approval; post-merge changes
  reuse the branch with a new PR. The frontmatter `status` field is kept
  synchronized with branch/PR state by the service.
- **Concurrency** ([DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md)):
  one git worktree per user session; sole-version worktrees merge into the
  generic item branch; divergent versions get user-suffixed branches until
  reconciled (synthesis or Conflict flow).
- **Access** ([DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)):
  all writes via the storage API; read-only git access sanctioned for
  external consumers pinned to refs.
- **ID allocation** ([DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md)):
  sequential per prefix, never reused, serialized by a thread/process-safe
  service lock.
- **Mechanical writes** ([DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)):
  typed operations only (`append-turn`, `mark-stale`, `set-jira-key`, …);
  agents hold no git credentials; direct-commit or program-user auto-PR
  fallback with a deterministic mechanical-diff CI check, per deployment.
- **Validation** ([DEC-0034](../decisions/DEC-0034-two-tier-validation.md)):
  tier 1 (schema + branch-local link resolution) on every write to any
  branch; tier 2 (completeness: required sections, decision citations,
  reciprocal impact links, no open conflicts) as required PR checks.
- **Type-aware write rules** ([DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)):
  session artifacts are append-only at the API level.

**Out:** graph queries ([EP-0004](EP-0004-graph-index.md)); gate *policy* — who must approve what —
([EP-0003](EP-0003-governance-and-gate-engine.md), which compiles policies onto host branch-protection via [EP-0005](EP-0005-connectors-and-identity.md));
the PR review UI ([EP-0006](EP-0006-refinement-web-ui.md), per [DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md));
rendering ([EP-0006](EP-0006-refinement-web-ui.md)).

## Domain Context

Bounded context: **Canonical Store**. Terms: Artifact, Canonical Store,
status lifecycle, Item Branch, Session Worktree, Mechanical Write — per
[CONTEXT.md](../../CONTEXT.md) and
[SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Storage API contract** (OpenAPI, language-neutral per
  [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)):
  CRUD via item branches, versioned reads, typed mechanical operations,
  session lifecycle (open worktree / append-turn / close), branch and PR
  orchestration operations.
- **Artifact schema definitions**: machine-readable (JSON Schema) versions
  of each SPEC's frontmatter — the tier-1 validators.
- **Tier-2 check suite**: the productionized `tools/check_links.py` plus the
  mechanical-diff validator, packaged as required PR checks.
- **Change-event stream**: artifact-changed events (branch-aware) consumed
  by the Graph Index ([EP-0004](EP-0004-graph-index.md)), impact analysis ([EP-0003](EP-0003-governance-and-gate-engine.md)), and consolidation
  freshness ([EP-0007](EP-0007-consolidation-memory-layer.md)).
- **App database port** ([DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)):
  the Protocol seam for the relational/transactional workload (outbox per
  [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md),
  bookkeeping, counters); adapters config-selected with a conformance
  suite ([DEC-0122](../decisions/DEC-0122-config-selected-adapters.md));
  v1 ships the DuckDB adapter only
  ([DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
- **Consumed from [EP-0005](EP-0005-connectors-and-identity.md)**: code-host connector operations for fork, PR
  open/merge, review state, and required-check registration.

## Risks & Open Questions

- Counter durability across restarts and multi-node deployment (distributed
  lock) — story-level design ([DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md) implication).
- Branch-aware reads for the Graph Index: which branches does the index see,
  and how are draft-only artifacts marked in query results? ([EP-0004](EP-0004-graph-index.md)
  refinement input, via the EP-0001→[EP-0004](EP-0004-graph-index.md) impact edge.)
- Worktree lifecycle hygiene: abandoned sessions, worktree GC, and the
  reconciliation queue for user-suffixed branches.
- Upstream host permission model: service identity vs. program user vs.
  delegated approver reviews — to be pinned during [EP-0005](EP-0005-connectors-and-identity.md) refinement.

## Derived Work

- [CMP-0001](../components/CMP-0001-artifact-store-service.md) — Artifact
  Store Service (contract-completed by the stories below)
- [CMP-0002](../components/CMP-0002-change-event.md) — ChangeEvent
  Contract (graduated event seam per
  [DEC-0134](../decisions/DEC-0134-graduate-change-event.md))
- [CMP-0003](../components/CMP-0003-app-database-port.md) — App Database
  Port (graduated protocol seam per
  [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md))
- [ST-0001](../stories/ST-0001-tier1-schema-suite.md) — Tier-1 schema suite
  and validation library
- [ST-0002](../stories/ST-0002-storage-api-core.md) — Storage service core
  and OpenAPI contract
- [ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md) —
  Item-branch and gate-PR lifecycle orchestration
- [ST-0004](../stories/ST-0004-session-worktree-management.md) — Session
  worktree management and divergence handling
- [ST-0005](../stories/ST-0005-id-allocation.md) — ID allocation
- [ST-0006](../stories/ST-0006-typed-mechanical-writes.md) — Typed
  mechanical write operations
- [ST-0007](../stories/ST-0007-tier2-check-suite.md) — Tier-2 completeness
  check suite
- [ST-0008](../stories/ST-0008-change-event-stream.md) — Branch-aware
  change-event stream
- [ST-0010](../stories/ST-0010-app-database-port.md) — App database
  port: protocol contract, conformance suite, DuckDB adapter
- [ST-0011](../stories/ST-0011-schema-evolution-machinery.md) — Schema
  evolution and migration machinery (deferred, `backlog`, trigger
  `TRG-0005`)
