---
id: CMP-0005
type: component
title: Code-Host Connector Protocol
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: integration
component-type: protocol
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
cites: [DEC-0014, DEC-0028, DEC-0032, DEC-0036, DEC-0043, DEC-0045, DEC-0049,
        DEC-0079, DEC-0080, DEC-0132, DEC-0141, DEC-0142, DEC-0145,
        DEC-0150, DEC-0153, DEC-0156, DEC-0167, DEC-0168, DEC-0169,
        DEC-0170, DEC-0171, DEC-0172, DEC-0173]
---

# CMP-0005: Code-Host Connector Protocol

## Purpose

The capability seam every host interaction crosses: operation contracts
for fork/branch/PR orchestration, reviews, check administration, team
administration, and allowlisted read access; the capability-manifest
schema with the documented minimum set; the normalized host-event
schema; and the conformance suite any adapter — the local-git fake
included — must pass. The standalone `protocol`-type CMP promised by
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md) and
bound by [CMP-0001](CMP-0001-artifact-store-service.md)'s and
[CMP-0004](CMP-0004-governance-gate-engine.md)'s forward-declared
consumption lists
([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).

> **v1 host: GitHub (cloud).** Bitbucket Data Center is deferred to
> backlog behind trigger `TRG-0010`
> (per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).
> This protocol itself is host-agnostic and unaffected by which
> adapter is v1 — the swap only retargets
> [CMP-0006](CMP-0006-bitbucket-data-center-connector.md)'s consumer,
> now [CMP-0009](CMP-0009-github-connector.md)'s. `A-5`/`A-6` are no
> longer provisional: GitHub's documented Checks API and
> required-status-checks are known to support the assumed semantics
> (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)).

## Ubiquitous Language

Connector, Code-Host Connector, Capability Manifest, Adapter — per
[CONTEXT.md](../../CONTEXT.md).

## Design Elements

### CodeHostConnector (protocol)

Implements: [ST-0019](../stories/ST-0019-code-host-connector-protocol.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)

Every operation enumerates typed error conditions from the closed
vocabulary `not-found | permission-denied | conflict |
capability-unsupported | rate-limited`; creation operations are
idempotent on their natural key (per
[DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).

- `CodeHostConnector.A-1` — `provision_fork(repo) → ForkHandle{fork_url,
  default_branch}`: idempotent per repo — a repeat call returns the
  existing fork. Errors: `not-found` (repo absent from the allowlist,
  per `A-9`'s indistinguishability rule), `permission-denied`
  (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `CodeHostConnector.A-2` — branch operations: `branch.create(fork,
  name, from_ref)`, `branch.delete(fork, name)`, `branch.push(fork,
  name, commits)`, idempotent on `(fork, name)` for create. Errors:
  `conflict` (branch exists / non-fast-forward push), `not-found`,
  `permission-denied` (per
  [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)).
- `CodeHostConnector.A-3` — PR lifecycle: `pr.open(fork, source_branch,
  target_branch, title, description) → PrHandle`, idempotent on
  `(source_branch, target_branch)`; `pr.merge(pr_id, strategy)`;
  `pr.get_review_state(pr_id) → ReviewState`. Errors: `conflict` (merge
  conflict, already merged), `not-found`, `permission-denied`
  (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md),
  [DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md)).
- `CodeHostConnector.A-4` — review posting, both paths of
  [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md):
  `review.post_as_user(pr_id, oauth_token, verdict, body)` (delegated
  OAuth — the host records the real approver) and
  `review.post_as_program_user(pr_id, verdict, attribution_block)`
  (the `attribution_block` is an opaque, pre-signed value this
  contract passes through unmodified — its concrete shape (person-id,
  PR reference, decision timestamp, Ed25519-class signature) and
  signing are the identity component's contract, not this protocol's
  (per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md))).
  Errors: `not-found`, `permission-denied`.
- `CodeHostConnector.A-5` — check-run
  result posting: `check.post_result(pr_id, check_name, status,
  details_url)`; re-postable and idempotent to support recomputation,
  including flipping an already-green result back to failing on an
  open PR
  (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
  [DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md)).
  Errors: `not-found`, `permission-denied`,
  `capability-unsupported`.
- `CodeHostConnector.A-6` —
  required-check registration and reconciliation:
  `check.register_required(repo, branch, check_names[])`;
  `check.unregister_required(repo, branch, check_names[])` clears a
  previously registered required-check entry from branch protection
  when a gate policy stops requiring it. Both exclusively invoked by
  the gate engine's policy compiler, never by
  [CMP-0001](CMP-0001-artifact-store-service.md)
  (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
  Errors: `permission-denied`, `capability-unsupported` (above
  minimum — see `CapabilityManifest`, per
  [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).
- `CodeHostConnector.A-7` — branch-protection administration:
  `protection.set(repo, branch, rules)`, `protection.get(repo, branch)
  → rules`. Errors: `permission-denied`, `capability-unsupported` for
  rule shapes above the minimum set — the minimum stays a floor every
  future adapter must meet regardless of which host is v1, so it
  excludes native path-scoped reviewer rules even though GitHub (v1)
  supports them via CODEOWNERS
  (per [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md),
  [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).
- `CodeHostConnector.A-8` — team administration: `team.create(name)`,
  `team.sync(name, members[])`. Errors: `permission-denied`,
  `capability-unsupported` (above minimum, per
  [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).
- `CodeHostConnector.A-9` — read-only browse/search:
  `read.browse(repo, ref, path) → listing`, `read.file(repo, ref,
  path) → content + citation`, `read.search(repo, ref, query) →
  results + citation`. **Allowlist behavior** (per
  [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md),
  [DEC-0170](../decisions/DEC-0170-allowlist-filter-behavior-clause.md)):
  a repository absent from `governance/repos.yaml` returns `not-found`,
  indistinguishable from a repository that doesn't exist on the host;
  per-repository path excludes never appear in listings, search
  results, or file reads; every returned item carries a repo+ref
  citation (`{repo, ref, path}`) in the published citation format. No
  write operation is expressible on this item family
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
  Errors: `not-found` (including allowlist denial), `permission-denied`.
- `CodeHostConnector.A-10` — permission probe: `probe.permissions(repo)
  → PermissionSet` — what the connector's current credentials can do
  against `repo`, called before attempting privileged operations.
  Errors: `not-found`.
- `CodeHostConnector.A-11` — webhook/event subscription:
  `webhook.register(repo, event_types[], callback_url) →
  WebhookHandle`, `webhook.unregister(handle)`. Inbound host payloads
  normalize into `HostEvent`
  (per [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).
  Errors: `capability-unsupported` (no webhook capability — callers
  fall back entirely to the gate engine's reconciliation sweep, per
  [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)),
  `permission-denied`.
- `CodeHostConnector.B-1` — capability gating: invoking any
  above-minimum operation against a manifest that doesn't declare it
  fails fast with `capability-unsupported`, never a host-specific error
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
  [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).
- `CodeHostConnector.B-2` — conformance: the local-git fake connector
  implements this contract in full, manifest included, and is the
  hermetic CI double every consumer tests against
  (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).

### CapabilityManifest (value)

Implements: [ST-0019](../stories/ST-0019-code-host-connector-protocol.md)

- `CapabilityManifest.D-1` — schema: `host_type` (string), `adapter_version`
  (string), and boolean capability flags. **Minimum set** (all must be
  `true` for a connector to be deployable): `fork_provisioning`,
  `branch_ops`, `pr_lifecycle`, `review_posting`, `read_access`,
  `permission_probe`, `check_result_posting`. **Above-minimum**
  (adapted or emulated when `false`): `required_check_registration`,
  `team_sync`, `review_dismissal`, `native_path_scoped_reviewers`,
  `webhook_delivery`
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
  [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).
- `CapabilityManifest.D-2` — validity: a manifest with any minimum-set
  flag `false` makes the connector invalid for deployment; the
  documented minimum is part of this contract, not per-adapter
  discretion
  (per [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).

### HostEvent (event)

Implements: [ST-0019](../stories/ST-0019-code-host-connector-protocol.md)

- `HostEvent.D-1` — payload schema: `event_id` (uuid), `schema_version`
  (int), `repo`, `kind` (closed enum: `pr-opened | pr-updated |
  pr-merged | pr-closed | review-posted | push | check-requested`),
  `payload` (kind-specific, normalized — never raw host JSON),
  `occurred_at` (timestamp), `source_ref` (host-native event
  identifier, for dedup)
  (per [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).
- `HostEvent.B-1` — emission: every event type registered via
  `CodeHostConnector.A-11` normalizes to exactly one `HostEvent`; no
  host-specific payload shape crosses the seam.
- `HostEvent.B-2` — delivery: at-least-once, ordered only within a
  single `repo` + PR (`source_ref`-scoped); consumers key idempotency
  on `event_id`/`source_ref`, matching
  [CMP-0002](CMP-0002-change-event.md)'s delivery contract shape
  (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).

## Component Invariants

- `C-1` — no write operation to codebase *content* is expressible
  through this protocol at any capability level: orchestration
  operations write git refs, PR metadata, reviews, and check results —
  never file content in a target repository
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
- `C-2` — credentials used for `CodeHostConnector.A-9` (context reads)
  are always read-only and scoped to the allowlisted repositories; they
  are never the same credential used for orchestration writes
  (`A-1`–`A-8`)
  (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
- `C-3` — the `CapabilityManifest` is the single source of truth for
  what an adapter can do; no operation succeeds against a host whose
  manifest doesn't declare the corresponding capability
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Implementation Guidance

### Constraints

- `IG-1` — typed error conditions: adapters map every host-native
  error onto the closed vocabulary in
  `CodeHostConnector`'s preamble; no host-specific exception type
  crosses the seam
  (per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).
- `IG-2` — check-result posting and required-check registration
  (`A-5`/`A-6`) should still be isolated behind their own internal
  adapter boundary: a general good practice for any operation family
  another host's quirks might later touch, not a sign these items
  remain provisional
  (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)).
- `IG-3` — webhook delivery is push-primary; adapters must not
  implement their own polling loop for freshness — the reconciliation
  sweep is the gate engine's sole polling path
  (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
  [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).
- `IG-4` — the minimum capability set is fixed at
  `CapabilityManifest.D-1`'s list, independent of which host is v1; a
  host that cannot meet it is out of scope for a connector, not an
  emulation target
  (per [DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md)).

### Notes

- Rate-limit backoff scheduling is adapter-specific; `rate-limited`
  signals to callers that retry-with-backoff is appropriate, but the
  schedule itself is not part of this contract.
- GitHub's Checks API and required-status-checks are the expected
  backing for `A-5`/`A-6` — native support for blocking merge on a
  named check, re-posting results, and flipping a passed check back to
  failing on an open PR
  (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)).

## Dependencies

Consumers, not dependencies, dominate this seam. This contract is a
leaf: it depends on nothing else in the system.

- [CMP-0001](CMP-0001-artifact-store-service.md) — consumes
  `CodeHostConnector.A-1` (fork provisioning), `A-2` (branch
  create/delete), `A-3` (PR open/merge/review-state), `A-5`
  (check-run result posting), `A-10` (permission probe), all gated by
  `CapabilityManifest`
  (per [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
  [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
- [CMP-0004](CMP-0004-governance-gate-engine.md) — consumes
  `CodeHostConnector.A-6` (required-check registration), `A-7`
  (branch-protection administration), `A-8` (team administration),
  `A-5` (check-run result posting), `A-3` (PR review-state reads),
  `A-10` (permission probe)
  (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).

## Acceptance & Test Expectations

1. The conformance suite exercises every `CodeHostConnector` operation
   family, the `CapabilityManifest` schema, and the closed error
   vocabulary; the local-git fake connector passes it in full
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).
2. [CMP-0001](CMP-0001-artifact-store-service.md)'s forward-declared
   consumption list is satisfied operation-for-operation against this
   contract, or a conflict is raised
   (per [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).
3. [CMP-0004](CMP-0004-governance-gate-engine.md)'s forward-declared
   consumption list is satisfied operation-for-operation against this
   contract
   (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
4. Idempotent re-invocation: retrying `A-1`/`A-2`/`A-3` creation calls
   with the same natural key returns the existing resource, never a
   duplicate
   (per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).
5. Allowlist enforcement: `A-9` calls against a non-allowlisted
   repository or an excluded path behave exactly as documented in
   `A-9`'s behavior clause, verified against the fake connector's
   allowlist fixture
   (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
6. Webhook events registered via `A-11` normalize to `HostEvent` and
   are redeliverable idempotently under at-least-once delivery
   (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
   [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).

## Out of Scope

- The GitHub implementation of this contract
  ([CMP-0009](CMP-0009-github-connector.md),
  [ST-0031](../stories/ST-0031-github-connector.md)); the Bitbucket
  Data Center implementation, deferred to backlog behind `TRG-0010`
  ([CMP-0006](CMP-0006-bitbucket-data-center-connector.md),
  [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md),
  per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).
- Token issuance, OAuth linkage, and program-user attribution signing —
  identity's concern
  ([CMP-0007](CMP-0007-identity-and-access.md),
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md));
  `A-4`'s review-posting operations accept opaque
  credential/attribution parameters and pass them through without
  interpreting them.
- Consumption of the repo+ref citation in agent context or Decision
  records — [EP-0002](../epics/EP-0002-refinement-session-agent.md)'s
  concern; this protocol only guarantees every read result carries the
  citation data.
- Connectors for hosts other than GitHub and (deferred) Bitbucket Data
  Center — Bitbucket Cloud and GitLab, behind an armed demand trigger
  ([ST-0028](../stories/ST-0028-additional-code-host-connectors.md),
  per [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md)).
- Writing to codebase content — permanently out for the whole system
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
