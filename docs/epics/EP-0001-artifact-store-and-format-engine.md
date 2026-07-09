---
id: EP-0001
type: epic
title: Artifact Store & Format Engine
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-05
overview: >-
  EP-0001 delivers the canonical Artifact Store & Format Engine as the
  authoritative storage service for the goal→docs refinement system:
  owns the fork-pull git model over upstream docs, allocates immutable
  artifact IDs, validates every write, orchestrates item branches,
  session worktrees, and gate PRs, and enforces link-graph integrity.
  All writes go through its API. The store is git-backed markdown with
  YAML frontmatter per DEC-0008, supporting concurrent session
  refinement and typed mechanical writes. Approved 2026-07-07.
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  impacts: [EP-0002, EP-0003, EP-0004, EP-0005, EP-0006, EP-0007, EP-0008]
  impacted-by: [EP-0003, EP-0005]
cites: [DEC-0008, DEC-0009, DEC-0002, DEC-0018, DEC-0026, DEC-0028, DEC-0029,
        DEC-0030, DEC-0031, DEC-0032, DEC-0033, DEC-0034, DEC-0035, DEC-0103,
        DEC-0121, DEC-0122, DEC-0124, DEC-0134, DEC-0135]
---

# EP-0001: Artifact Store & Format Engine

## Summary

The canonical heart of Groundwork: a storage service that owns the fork-pull
git model over the upstream doc repository, allocates immutable artifact
IDs, validates every write, orchestrates item branches, session worktrees,
and gate PRs, and enforces link-graph integrity. All writes — UI, agents,
connectors — go through its API; nothing else holds write credentials to the
repository. The store's reference implementation is git-backed markdown with
YAML frontmatter (per DEC-0008).

## Why (Goal Alignment)

BG-0001's traceability outcome depends on artifacts being well-formed and
their links resolvable at all times (DEC-0009).
Canonical-store discipline (DEC-0002)
holds because this service is the single write authority
(DEC-0029); human
ratification is durable because gate sign-off is PR approval on the upstream
repository (DEC-0028).

## Scope

**In** (refined at SES-0003):

- **Git model** (DEC-0028):
  application-owned fork of upstream; one item branch per artifact under
  refinement, carrying the item plus its sessions and decisions; PR to
  upstream main opened with the branch; merge = approval; post-merge changes
  reuse the branch with a new PR. The frontmatter `status` field is kept
  synchronized with branch/PR state by the service.
- **Concurrency** (DEC-0030):
  one git worktree per user session; sole-version worktrees merge into the
  generic item branch; divergent versions get user-suffixed branches until
  reconciled (synthesis or Conflict flow).
- **Access** (DEC-0029):
  all writes via the storage API; read-only git access sanctioned for
  external consumers pinned to refs.
- **ID allocation** (DEC-0031):
  sequential per prefix, never reused, serialized by a thread/process-safe
  service lock.
- **Mechanical writes** (DEC-0033):
  typed operations only (`append-turn`, `mark-stale`, `set-jira-key`, …);
  agents hold no git credentials; direct-commit or program-user auto-PR
  fallback with a deterministic mechanical-diff CI check, per deployment.
- **Validation** (DEC-0034):
  tier 1 (schema + branch-local link resolution) on every write to any
  branch; tier 2 (completeness: required sections, decision citations,
  reciprocal impact links (DEC-0026), no open conflicts) as required PR
  checks.
- **Type-aware write rules** (DEC-0035):
  session artifacts are append-only at the API level.

**Out:** graph queries (EP-0004); gate *policy* — who must approve what —
(EP-0003, which compiles policies onto host branch-protection via EP-0005);
the PR review UI (EP-0006, per DEC-0032);
rendering (EP-0006).

## Domain Context

Bounded context: **Canonical Store**. Terms: Artifact, Canonical Store,
status lifecycle, Item Branch, Session Worktree, Mechanical Write — per
[CONTEXT.md](../../CONTEXT.md) and
[SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Storage API contract** (OpenAPI, language-neutral per
  DEC-0018):
  CRUD via item branches, versioned reads, typed mechanical operations,
  session lifecycle (open worktree / append-turn / close), branch and PR
  orchestration operations. This is the surface the session agent
  (EP-0002) writes through — the typed-mechanical-write and append-only
  rules (DEC-0033, DEC-0035) constrain how EP-0002 persists turns and
  decisions (the EP-0001→EP-0002 impact edge).
- **Artifact schema definitions**: machine-readable (JSON Schema) versions
  of each SPEC's frontmatter — the tier-1 validators.
- **Tier-2 check suite**: the productionized `tools/check_links.py` plus the
  mechanical-diff validator, packaged as required PR checks.
- **Change-event stream**: artifact-changed events (branch-aware) consumed
  by the Graph Index (EP-0004), impact analysis (EP-0003), and consolidation
  freshness (EP-0007).
- **App database port** (DEC-0121):
  the Protocol seam for the relational/transactional workload (outbox per
  DEC-0103,
  bookkeeping, counters); adapters config-selected with a conformance
  suite (DEC-0122);
  v1 ships the DuckDB adapter only
  (DEC-0124). EP-0008's Composition Root binds this port to its
  configured adapter at startup, and its inbound API fronts this
  service for the UI — contract decisions here constrain that platform
  assembly (the EP-0001→EP-0008 impact edge).
- **Consumed from EP-0005**: code-host connector operations for fork, PR
  open/merge, review state, and required-check registration.

## Risks & Open Questions

- Counter durability across restarts and multi-node deployment (distributed
  lock) — story-level design (DEC-0031 implication).
- Branch-aware reads for the Graph Index: which branches does the index see,
  and how are draft-only artifacts marked in query results? (EP-0004
  refinement input, via the EP-0001→EP-0004 impact edge.)
- Worktree lifecycle hygiene: abandoned sessions, worktree GC, and the
  reconciliation queue for user-suffixed branches.
- Upstream host permission model: service identity vs. program user vs.
  delegated approver reviews — to be pinned during EP-0005 refinement.

## Derived Work

- CMP-0001 — Artifact
  Store Service (contract-completed by the stories below)
- CMP-0002 — ChangeEvent
  Contract (graduated event seam per
  DEC-0134)
- CMP-0003 — App Database
  Port (graduated protocol seam per
  DEC-0135)
- ST-0001 — Tier-1 schema suite
  and validation library
- ST-0002 — Storage service core
  and OpenAPI contract
- ST-0003 —
  Item-branch and gate-PR lifecycle orchestration
- ST-0004 — Session
  worktree management and divergence handling
- ST-0005 — ID allocation
- ST-0006 — Typed
  mechanical write operations
- ST-0007 — Tier-2 completeness
  check suite
- ST-0008 — Branch-aware
  change-event stream
- ST-0010 — App database
  port: protocol contract, conformance suite, DuckDB adapter
- ST-0011 — Schema
  evolution and migration machinery (deferred, `backlog`, trigger
  `TRG-0005`)
