---
id: CMP-0001
type: component
title: Artifact Store Service
status: gated
owner: eng-lead
created: 2026-07-06
context: canonical-store
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0009, DEC-0018, DEC-0026, DEC-0028, DEC-0029, DEC-0030, DEC-0031,
        DEC-0033, DEC-0034, DEC-0035, DEC-0038, DEC-0043, DEC-0045, DEC-0047,
        DEC-0048, DEC-0055, DEC-0057, DEC-0059, DEC-0060, DEC-0077, DEC-0079,
        DEC-0080, DEC-0081, DEC-0082, DEC-0085, DEC-0087, DEC-0088, DEC-0089,
        DEC-0092, DEC-0093, DEC-0097, DEC-0098, DEC-0099, DEC-0101, DEC-0102,
        DEC-0103, DEC-0104, DEC-0108, DEC-0109, DEC-0110, DEC-0121, DEC-0122,
        DEC-0124, DEC-0125, DEC-0126, DEC-0127, DEC-0128, DEC-0129, DEC-0130,
        DEC-0131, DEC-0132]
---

# CMP-0001: Artifact Store Service

## Purpose

The single write authority over the Canonical Store: owns the fork-pull
git model, validates every write, allocates IDs, orchestrates item
branches, session worktrees, and gate PRs, executes typed mechanical
writes, and emits the change-event stream every other component
consumes.

## Ubiquitous Language

Canonical Store, Artifact, Item Branch, Session Worktree, Mechanical
Write, Gate, Design Element, Port, Adapter — per
[CONTEXT.md](../../CONTEXT.md). No new terms introduced.

## Design Elements

Decomposition per [DEC-0126](../decisions/DEC-0126-cmp-0001-element-decomposition.md).
One OpenAPI document spans the API items of all services
(per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md));
all non-2xx responses use the problem+json model
(per [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)).

### SchemaValidator (service)

Implements: [ST-0001](../stories/ST-0001-tier1-schema-suite.md)

- `SchemaValidator.A-1` — `validate(document, artifact-type) →
  ok | problem(tier1-validation-failed) with errors[]{field, rule,
  message}`. Validates frontmatter against the type's schema asset;
  unknown link types and malformed IDs are rejections; impact-link
  reciprocity is explicitly not checked here (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
  [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0026](../decisions/DEC-0026-directional-impact-links.md), [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)).
- `SchemaValidator.A-2` — `validate-config(file, config-kind) →
  ok | problem(tier1-validation-failed)` for the governance config
  files (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
- `SchemaValidator.B-1` — a document failing validation never reaches
  the repository: the library is invoked before any commit is
  constructed, on every write path (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
- `SchemaValidator.B-2` — errors are field-level and actionable: each
  names the failing field path, the violated rule, and a human-readable
  message (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)).
- `SchemaValidator.D-1` — one JSON Schema asset per artifact type (BG,
  EP, ST, SP, CMP, SES, DEC, CFL, CON, CP), exactly matching its SPEC,
  published language-neutrally with the spec set (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
  [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md), [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)).
- `SchemaValidator.D-2` — schema assets for `governance/roles.yaml`
  (incl. decision-rights), `domains.yaml`, `gate-policies.yaml`,
  `people.yaml`, `repos.yaml` (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md), [DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md),
  [DEC-0046](../decisions/DEC-0046-person-registry.md), [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
- `SchemaValidator.D-3` — the element-type enum (entity, value,
  service, event, protocol) as a standalone schema asset; the CMP
  frontmatter schema validates optional `component-type` against it
  (per [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md), [DEC-0082](../decisions/DEC-0082-closed-element-type-taxonomy.md)).
- `SchemaValidator.D-4` — story/epic/spike schemas accept `deferred`
  status and the `release:` grammar (`backlog` or SemVer version-core
  prefix, numeric identifiers, no leading zeroes, no `v`, no
  pre-release/build); the field and status are rejected on any other
  type. Cross-file label validity is tier-2, not here (per
  [DEC-0097](../decisions/DEC-0097-deferred-status.md), [DEC-0098](../decisions/DEC-0098-semver-release-labels.md), [DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

### StorageService (service)

Implements: [ST-0002](../stories/ST-0002-storage-api-core.md)

- `StorageService.A-1` — `read(artifact-id, [ref]) → {document,
  ref: commit-sha} | problem(not-found)`. Reads return the resolving
  sha; the optional ref/branch parameter pins the read (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)).
- `StorageService.A-2` — `write(document, item-branch) → {commit-sha}
  | problem(tier1-validation-failed | branch-diverged)`. Runs
  `SchemaValidator.A-1` before constructing any commit; routes the
  commit to the artifact's item branch (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md),
  [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `StorageService.A-3` — session mutation surface is exactly
  `append-turn` and `close` (delegated to
  MechanicalWriteService.A-1/A-2); no operation that edits or deletes
  an existing turn exists in the API (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
- `StorageService.B-1` — the service identity is the only holder of
  repository write credentials; every commit reaching the fork or
  upstream is constructed by this service (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md), [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `StorageService.B-2` — external read-only git access is sanctioned
  for consumers pinned to refs; such consumers never observe
  half-written state because writes are single commits (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)).
- `StorageService.B-3` — every landed write causes exactly one
  `ChangeEvent` emission via the outbox (see `ChangeEvent.B-1`,
  `AppDatabasePort.B-1`) (per [DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md), [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).

### BranchOrchestrator (service)

Implements: [ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md)

- `BranchOrchestrator.A-1` — `create-artifact(type, seed-content) →
  {artifact-id, item-branch, pr-ref}`. Allocates the ID via
  IdAllocator, creates the ItemBranch on the fork, opens the gate PR
  against upstream main (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md), [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md)).
- `BranchOrchestrator.A-2` — `reopen(artifact-id) → {item-branch,
  pr-ref}`. Post-merge changes reuse the artifact's existing branch and
  open a new PR; the artifact returns to `in-refinement` (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `BranchOrchestrator.B-1` — PR merge transitions the artifact to
  `approved`, recording `approved-by` from approver identities resolved
  out of the PR's reviews (OAuth identity, program-user fallback)
  (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md), [DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md), [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
- `BranchOrchestrator.B-2` — every ItemBranch lifecycle transition
  updates frontmatter `status` and branch/PR state atomically, or
  reconciles on the next observed event; see `ItemBranch.B-2` and
  invariant `C-3` (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `BranchOrchestrator.B-3` — all host interactions go through the
  code-host connector contract and respect its capability manifest;
  no direct host-API calls (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md), [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).

### WorktreeManager (service)

Implements: [ST-0004](../stories/ST-0004-session-worktree-management.md)

- `WorktreeManager.A-1` — `open-session-worktree(artifact-id,
  session-id) → {worktree-ref}`. Provisions a dedicated worktree off
  the item branch; all of that session's writes land in it (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md)).
- `WorktreeManager.A-2` — `close-session-worktree(session-id) →
  {merged | diverged{user-branches[]}}`. Sole live version merges to
  the item branch; concurrent divergent versions produce user-suffixed
  branches surfaced to synthesis, never auto-merged (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md), [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).
- `WorktreeManager.B-1` — worktrees of sessions auto-closed for
  inactivity are garbage-collected after their partial distillation
  commits land (per [DEC-0057](../decisions/DEC-0057-session-lifecycle.md)).
- `WorktreeManager.B-2` — after service restart, worktree state is
  reconstructed from refs: no in-flight session is orphaned or
  double-provisioned; see `SessionWorktree.B-2` and invariant `C-1`
  (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md), [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md)).

### IdAllocator (service)

Implements: [ST-0005](../stories/ST-0005-id-allocation.md)

- `IdAllocator.A-1` — `allocate(prefix) → ArtifactId |
  problem(id-conflict)`. Returns the next sequential ID for the prefix
  (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md)).
- `IdAllocator.B-1` — allocation is serialized by a
  thread/process-safe service lock; concurrent requests never mint
  duplicates (per [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md)).
- `IdAllocator.B-2` — allocation accounts for artifacts existing only
  on unmerged item branches: a fresh scan of all refs yields no
  collision with any allocated ID (per [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md), [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).
- `IdAllocator.B-3` — counter state is rebuilt on boot by scanning all
  refs for the max existing ID per prefix; no persistent counter store
  exists anywhere — not in the app database, not behind the port
  (per [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md), [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).
- `IdAllocator.B-4` — single-allocator deployment is a documented
  constraint of the service (per [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

### MechanicalWriteService (service)

Implements: [ST-0006](../stories/ST-0006-typed-mechanical-writes.md)

- `MechanicalWriteService.A-1..A-8` — one API item per operation of the
  closed set: `append-turn(session-id, turn-content)`,
  `close-session(session-id)`, `mark-stale(artifact-id, cause-ref)`,
  `clear-stale(artifact-id, reaffirm-ref)`,
  `set-jira-key(artifact-id, key)`, `set-jira-status(artifact-id,
  status)`, `create-change-proposal(cp-document)`,
  `set-cp-triage(cp-id, outcome)`. Each constructs its commit entirely
  from typed parameters and returns `{commit-sha} |
  problem(mechanical-op-rejected)` (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md), [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md),
  [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md), [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md), [DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md), [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).
- `MechanicalWriteService.B-1` — no mechanical operation can modify
  artifact body content or non-allowlisted frontmatter fields; the
  restriction is structural (the diff is constructed, not filtered),
  not a policy check (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `MechanicalWriteService.B-2` — where upstream branch protection
  forbids direct pushes, mechanical writes flow through auto-PRs
  approved by the program user, gated by the mechanical-diff validator
  (`CheckSuite.B-3`) as a required check; direct-commit vs auto-PR is
  per-deployment configuration with no code change (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `MechanicalWriteService.D-1` — the **allowlist asset**: the published
  operation → permitted-fields/append-regions map, consumed by both
  this service's write path and the mechanical-diff validator — one
  source of truth, two consumers. Extending it is a gated contract
  change (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md), [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).

### CheckSuite (service)

Implements: [ST-0007](../stories/ST-0007-tier2-check-suite.md)

- `CheckSuite.A-1` — `run(ref-range) → findings[]{artifact, rule,
  explanation, fix-hint, severity: violation|warning}`. Registered as a
  required PR check via the connector; any `violation` finding blocks
  merge (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).
- `CheckSuite.B-1` — graph-integrity and provenance rules: ID
  uniqueness and filename match; links/citations resolve; work
  artifacts trace to a goal; decisions derive from a session or spike;
  impact-link reciprocity and same-type; no approved artifact linked to
  an open conflict; required sections present; CMP contract items cite
  decisions (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0026](../decisions/DEC-0026-directional-impact-links.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
- `CheckSuite.B-2` — session diffs are verified append-only; any
  rewrite of an existing turn is a violation (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
- `CheckSuite.B-3` — the mechanical-diff validator: auto-PRs touch only
  what `MechanicalWriteService.D-1` allows for the claimed operation
  (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md), [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).
- `CheckSuite.B-4` — element rules for component docs: parseable
  `### <Name> (<type>)` headings against the closed enum; typed
  contract obligations present; API schemas resolve inline or to
  declared value/event elements; element-scoped item IDs well-formed
  and unique; Constraints cited, Notes exempt; `Implements:` lines
  present, resolvable, reciprocal with story Component Impact;
  story design-coverage audit (per [DEC-0081](../decisions/DEC-0081-element-first-contract-layout.md), [DEC-0087](../decisions/DEC-0087-parseable-element-headings.md), [DEC-0088](../decisions/DEC-0088-revised-typed-obligations.md),
  [DEC-0089](../decisions/DEC-0089-api-schema-resolution-rule.md), [DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md), [DEC-0092](../decisions/DEC-0092-element-implements-line.md), [DEC-0093](../decisions/DEC-0093-story-design-coverage-check.md), [DEC-0094](../decisions/DEC-0094-implements-reciprocity-check.md)).
- `CheckSuite.B-5` — release-scoping rules: `deferred`/`release:` only
  on stories/epics/spikes; labels resolve against the governing goal's
  declared releases or `backlog`; deferred ⇔ non-current effective
  release; deferred-only-Implements audit warning (per [DEC-0097](../decisions/DEC-0097-deferred-status.md),
  [DEC-0098](../decisions/DEC-0098-semver-release-labels.md), [DEC-0099](../decisions/DEC-0099-releases-declared-in-goal-scope.md), [DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md), [DEC-0101](../decisions/DEC-0101-deferred-out-of-metrics.md)).
- `CheckSuite.B-6` — trigger-registry rules: `docs/TRIGGERS.md`
  well-formed; unique never-reused TRG IDs; required fields per status;
  decision-cited subscriber lines; armed triggers subscribe only
  deferred artifacts, ≥1 each (per [DEC-0109](../decisions/DEC-0109-trigger-subscriptions.md), [DEC-0110](../decisions/DEC-0110-subscription-lifecycle.md), [DEC-0108](../decisions/DEC-0108-trigger-surfacing.md)).
- `CheckSuite.B-7` — every finding names the artifact, the rule, and a
  human-readable fix (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

### Artifact (entity)

Implements: [ST-0001](../stories/ST-0001-tier1-schema-suite.md),
[ST-0002](../stories/ST-0002-storage-api-core.md)

- `Artifact.B-1` — identity is the immutable `ArtifactId`; the filename
  slug may change, the ID may not; IDs are never reused (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)).
- `Artifact.B-2` — lifecycle states and transitions are exactly those
  of [SPEC-artifact-common](../specs/SPEC-artifact-common.md) (draft,
  in-refinement, gated, approved, stale, superseded, archived;
  deferred for stories/epics/spikes); the store rejects writes claiming
  any other status value at tier-1 (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0097](../decisions/DEC-0097-deferred-status.md), [DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md)).
- `Artifact.B-3` — session-type artifacts are append-only after
  creation and immutable after close, enforced by the write surface
  (`StorageService.A-3`), not by convention (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
- `Artifact.D-1` — one artifact per file: YAML frontmatter + markdown
  body; frontmatter shape per the type's `SchemaValidator.D-1` asset;
  typed links use the closed vocabulary (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

### ItemBranch (entity)

Implements: [ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md)

- `ItemBranch.B-1` — identity: exactly one item branch per artifact,
  named for it, living on the application fork; lifecycle:
  `open → pr-open → merged → reopened(pr-open) → …`; the branch carries
  the artifact plus its sessions and decisions as they accrue
  (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `ItemBranch.B-2` — coherence: the artifact's frontmatter `status` and
  the branch/PR state never disagree at rest; any transient
  disagreement is repaired by the next reconciliation event (per
  [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `ItemBranch.D-1` — branch metadata (artifact-id, pr-ref,
  lifecycle-state, last-reconciled-sha) is bookkeeping behind the
  AppDatabasePort, rebuildable from refs and host PR state
  (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md), [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md)).

### SessionWorktree (entity)

Implements: [ST-0004](../stories/ST-0004-session-worktree-management.md)

- `SessionWorktree.B-1` — identity: one worktree per (artifact,
  session); lifecycle: `provisioned → active → closed(merged) |
  diverged(user-branch) → gc'd`; divergence always yields a
  user-suffixed branch, never an auto-merge (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md), [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).
- `SessionWorktree.B-2` — reconstructibility: after restart, the full
  worktree set and each lifecycle state are recomputed from refs and
  bookkeeping; inactivity-closed worktrees are GC'd only after their
  partial distillation commits are on a ref (per [DEC-0057](../decisions/DEC-0057-session-lifecycle.md), [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md)).
- `SessionWorktree.D-1` — worktree record (artifact-id, session-id,
  branch-ref, state, last-activity) is bookkeeping behind the
  AppDatabasePort (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).

### ArtifactId (value)

Implements: [ST-0005](../stories/ST-0005-id-allocation.md)

- `ArtifactId.D-1` — format `<PREFIX>-<4-digit zero-padded n>`, prefix
  from the closed artifact-type set; equality by value; immutable;
  sequential per prefix; never reused even after deletion or
  abandonment on unmerged branches (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0031](../decisions/DEC-0031-service-lock-id-allocation.md)).

### ChangeEvent (event)

Implements: [ST-0008](../stories/ST-0008-change-event-stream.md)

- `ChangeEvent.D-1` — payload schema: `event_id` (uuid),
  `schema_version` (int), `artifact_id` (ArtifactId), `artifact_type`,
  `branch`, `commit` (sha), `kind` (closed enum: `created |
  content-amended | status-changed | merged | deleted`),
  `changed_fields[]`, `occurred_at` (timestamp). Enum or payload
  changes are gated contract changes (per [DEC-0128](../decisions/DEC-0128-change-event-closed-schema.md), [DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)).
- `ChangeEvent.B-1` — emission: every write landing in the repository —
  content, mechanical, merge — emits exactly one event via the
  transactional outbox (per [DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md), [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).
- `ChangeEvent.B-2` — delivery: at-least-once with per-artifact
  ordering; consumers are idempotent by contract; no cross-artifact
  ordering or exactly-once guarantee exists (per [DEC-0060](../decisions/DEC-0060-session-sync-global-async.md)).
- `ChangeEvent.B-3` — merge events carry what the Graph Index needs to
  promote overlay state to the main view and drop the overlay
  (per [DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)).
- `ChangeEvent.B-4` — replayability: the stream is derivable from git
  history for any ref range; a consumer rebuilt from scratch converges
  to the state of one that consumed live. The outbox is delivery
  plumbing, never truth (per [DEC-0060](../decisions/DEC-0060-session-sync-global-async.md), [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md)).

### AppDatabasePort (protocol)

Implements: [ST-0010](../stories/ST-0010-app-database-port.md),
[ST-0008](../stories/ST-0008-change-event-stream.md)

- `AppDatabasePort.A-1` — `begin() → UnitOfWork` with atomic
  commit/rollback across all operations enlisted in it (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.A-2` — outbox family: `outbox.append(events[],
  uow)`; `outbox.claim(batch-size) → leased events`;
  `outbox.ack(lease)` / `outbox.nack(lease)` for the dispatcher's
  retry loop (per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.A-3` — bookkeeping family:
  `bookkeeping.put/get/delete(namespace, key, document)` for
  operational records (worktree state, branch metadata, retry
  counters); no ID-counter surface exists on the port (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md),
  [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).
- `AppDatabasePort.B-1` — atomicity guarantee: outbox append and the
  write's bookkeeping commit or roll back together within one
  UnitOfWork (per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.B-2` — no SQL crosses the seam; adapters implement
  semantics, not a dialect. The Adapter is selected by deployment
  configuration only (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md), [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `AppDatabasePort.B-3` — conformance expectations: a shared suite
  exercises every operation family including UnitOfWork atomicity under
  failure injection; passing it is the definition of a valid Adapter;
  the v1 DuckDB Adapter passes it (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md), [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).

## Component Invariants

- `C-1` — **Rebuild-sufficiency**: all derived state — app database
  contents, outbox, worktrees, ID counters, caches — is reconstructible
  from the fork's git refs alone; a deployment restored from only the
  fork converges to correct service state (per [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md), [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md),
  [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).
- `C-2` — **Single write authority**: no path to a repository commit
  exists except through this service's identity (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md), [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `C-3` — **Status coherence**: artifact frontmatter `status` and
  branch/PR state never disagree at rest (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `C-4` — **No unvalidated write**: every commit the service constructs
  passed tier-1 validation first, on every branch (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

## Implementation Guidance

### Constraints

- `IG-1` — v1 storage stack is embedded-only; the app database engine
  is DuckDB behind the port (per [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md), [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
- `IG-2` — all app-database access goes through the AppDatabasePort;
  Adapter selection is deployment configuration (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md), [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `IG-3` — ID counters are rebuilt by rescan-on-boot over all refs; no
  durable counter store may be introduced (per [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md), [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).
- `IG-4` — the reference implementation is Python; the OpenAPI contract
  and schema assets are the deliverables of record and must stand
  language-neutral (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
- `IG-5` — v1 code-host target is Bitbucket Data Center via the
  connector contract; nothing in this component may depend on a
  BBDC-specific behavior (per [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md), [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

### Notes

- The local-git fake connector is a permanent test double tracking the
  connector contract spec, never any host's quirks — build against it
  first.
- Write the OpenAPI document before implementation; generate server
  stubs from it, not vice versa.
- DuckDB's single-writer character matches the v1 single-process
  constraint; do not add connection pooling that pretends otherwise.

## Dependencies

- **Code-host connector contract** ([EP-0005](../epics/EP-0005-connectors-and-identity.md);
  future standalone `protocol`-type CMP per
  [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)) —
  consumption forward-declared per
  [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
  binding on [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s
  refinement. Operations consumed: fork provisioning; branch
  create/delete; PR open, merge, review-state; required-check
  registration; permission probe. All consumed per the capability
  manifest (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md));
  hermetic testing via the local-git fake connector
  (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).

## Acceptance & Test Expectations

1. OpenAPI conformance suite runs against the published contract, not
   the implementation (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
2. The full orchestration suite passes hermetically against the
   local-git fake connector (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).
3. The AppDatabasePort conformance suite passes with the DuckDB
   Adapter (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md), [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
4. The tier-2 CheckSuite passes against this repository's bootstrap
   corpus as its regression baseline (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
5. Replay convergence: a consumer rebuilt from git history converges to
   the state of one that consumed the live stream (per [DEC-0060](../decisions/DEC-0060-session-sync-global-async.md)).
6. Write-credential isolation: a host-side permission test proves no
   identity other than the service can push (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md), [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

## Out of Scope

Boundary statements (per [DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md),
each linking its owning artifact where one exists):

- **No gate-policy evaluation** — the store merges what the host lets
  merge; who must approve what is the Governance engine's
  ([EP-0003](../epics/EP-0003-governance-and-gate-engine.md)), compiled
  onto branch protection via [EP-0005](../epics/EP-0005-connectors-and-identity.md).
  An implementer must not "helpfully" check roles.
- **No auto-merge of divergence** — divergent worktrees surface as
  user-suffixed branches; reconciliation is agent-driven synthesis
  ([EP-0002](../epics/EP-0002-refinement-session-agent.md)). The store
  never picks a winner.
- **No cross-artifact event ordering** — per-artifact ordering and
  at-least-once only; consumers must not assume global order or
  exactly-once ([EP-0004](../epics/EP-0004-graph-index.md) and other
  consumers own their idempotency).
- **No implementation-status storage** — implementation progress stays
  projection-side in the issue tracker; the store rejects attempts to
  write it into design docs.
- Graph queries ([EP-0004](../epics/EP-0004-graph-index.md)); retrieval
  ([EP-0007](../epics/EP-0007-consolidation-memory-layer.md)); any UI
  ([EP-0006](../epics/EP-0006-refinement-web-ui.md)).
- Schema *evolution*/migration machinery — future work, tracked as
  [ST-0011](../stories/ST-0011-schema-evolution-machinery.md)
  (deferred, `backlog`, revived by trigger `TRG-0005`).
