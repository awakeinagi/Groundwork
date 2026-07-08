---
id: CMP-0009
type: component
title: GitHub Connector
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0005]
cites: [DEC-0014, DEC-0028, DEC-0043, DEC-0045, DEC-0049, DEC-0079,
        DEC-0141, DEC-0142, DEC-0145, DEC-0152, DEC-0153, DEC-0167,
        DEC-0168, DEC-0169, DEC-0170, DEC-0172, DEC-0173, DEC-0174,
        DEC-0175, DEC-0176, DEC-0177]
---

# CMP-0009: GitHub Connector

## Purpose

The v1 reference adapter of the
[code-host connector protocol](CMP-0005-code-host-connector-protocol.md):
GitHub (cloud) REST/GraphQL and webhook integration, an honest
capability manifest, the Checks API and required-status-checks as the
required-check surface, CODEOWNERS and org teams for reviewer/team
routing. Takes Bitbucket Data Center's former v1 slot
(per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md); see
[CMP-0006](CMP-0006-bitbucket-data-center-connector.md), now deferred).

## Ubiquitous Language

Connector, Code-Host Connector, Capability Manifest, Adapter,
Orchestrator App, Reader App — per [CONTEXT.md](../../CONTEXT.md).

## Design Elements

### GitHubConnector (service)

Implements: [ST-0031](../stories/ST-0031-github-connector.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)

Implements [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
`CodeHostConnector` protocol in full, against GitHub cloud
(`github.com`). Two credential-distinct GitHub App installations back
the element: the **Orchestrator App** (write: contents, pull requests,
checks, administration, and — where granted — org members) for `A-1`
through `A-8` and `A-11`; the **Reader App** (read-only: contents,
metadata), installed only on allowlisted repositories, exclusively for
`A-9` (per [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).
REST is the default wire protocol; GraphQL backs only CODEOWNERS-derived
reviewer resolution and bulk team-membership queries
(per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
Every item below maps GitHub-native behavior onto
[CMP-0005](CMP-0005-code-host-connector-protocol.md)'s typed error
vocabulary and idempotency convention
(per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)):
a `404` maps to `not-found`; a `403` maps to `rate-limited` when
`X-RateLimit-Remaining: 0` or `Retry-After` is present, else
`permission-denied`; a `409`/unprocessable `422` maps to `conflict`;
creation operations on a natural key check for the existing resource
before writing, returning it instead of creating a duplicate
(per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).

- `GitHubConnector.A-1` — `provision_fork`: `POST
  /repos/{owner}/{repo}/forks`, targeting the Orchestrator App's
  dedicated service-owned account (per
  [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).
  Check-before-create: `GET /repos/{fork-owner}/{repo}` first; if the
  fork already exists, its `{fork_url, default_branch}` is returned
  unchanged. Implements
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
  `CodeHostConnector.A-1`.
- `GitHubConnector.A-2` — branch operations: `create` via `POST
  /repos/{owner}/{repo}/git/refs` (check-before-create against `GET
  .../git/ref/{ref}`), `push` via `PATCH .../git/refs/{ref}`, `delete`
  via `DELETE .../git/refs/{ref}`. A non-fast-forward `push` (`force:
  false`) surfaces GitHub's `422` as `conflict`. Implements
  `CodeHostConnector.A-2`.
- `GitHubConnector.A-3` — PR lifecycle: `pr.open` via `POST
  /repos/{owner}/{repo}/pulls`, check-before-create against `GET
  .../pulls?head={source}&base={target}`; `pr.merge` via `PUT
  .../pulls/{number}/merge`; `pr.get_review_state` via `GET
  .../pulls/{number}/reviews`. Implements `CodeHostConnector.A-3`.
- `GitHubConnector.A-4` — review posting: `post_as_user` uses the
  delegated approver's OAuth token (issued by the identity component,
  out of this contract's scope) against `POST
  /repos/{owner}/{repo}/pulls/{number}/reviews` — the review lands
  attributed to the real host user. `post_as_program_user` uses the
  Orchestrator App's installation token against the same endpoint; the
  review lands attributed to the App's own bot identity (e.g.
  `groundwork[bot]`), with the pre-signed `attribution_block` written
  verbatim into the review body
  (per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
  [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).
  Implements `CodeHostConnector.A-4`.
- `GitHubConnector.A-5` — check-run result posting: GitHub's Checks
  API, `POST /repos/{owner}/{repo}/check-runs` for a first post, `PATCH
  .../check-runs/{id}` for re-posts — never commit statuses. Re-posting
  is unconditional (idempotent by design) and can flip an already
  `success` check-run back to `failure` on an open PR
  (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md),
  [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
  [DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md)).
  Implements `CodeHostConnector.A-5`.
- `GitHubConnector.A-6` — required-check registration:
  `register_required`/`unregister_required` read-modify-write the
  `required_status_checks.contexts` (check-run names) array via
  classic branch protection (`PUT`/`GET
  /repos/{owner}/{repo}/branches/{branch}/protection`)
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
  Exclusively invoked by the gate engine
  (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
  Implements `CodeHostConnector.A-6`.
- `GitHubConnector.A-7` — branch-protection administration:
  `protection.set`/`protection.get` map directly onto classic
  `PUT`/`GET .../branches/{branch}/protection`
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
  Rule shapes above
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s documented
  minimum (per `DEC-0168`) that classic branch protection cannot
  express fail `capability-unsupported`. CODEOWNERS is read-only
  introspected to populate `CapabilityManifest.native_path_scoped_reviewers`;
  this element never writes a `CODEOWNERS` file
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
  Implements `CodeHostConnector.A-7`.
- `GitHubConnector.A-8` — team administration: `team.create` via
  `POST /orgs/{org}/teams`, `team.sync` via `PUT
  /orgs/{org}/teams/{team_slug}/memberships/{username}` per member
  added/removed. Available only when the Orchestrator App's
  installation was granted org-level `members` permission; otherwise
  every call fails `capability-unsupported`
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
  Implements `CodeHostConnector.A-8`.
- `GitHubConnector.A-9` — read-only browse/search: exclusively the
  Reader App's credentials
  (per [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).
  `read.browse`/`read.file` via `GET
  /repos/{owner}/{repo}/contents/{path}?ref={ref}`; `read.search` via
  `GET /search/code` scoped with `repo:{owner}/{repo}`. Allowlist
  filtering (`governance/repos.yaml`, path excludes) is applied before
  any GitHub call is issued — a non-allowlisted repository never
  reaches the API and returns `not-found`, indistinguishable from a
  repository absent on GitHub; excluded paths never appear in listing,
  search, or read results; every returned item carries `{repo, ref,
  path}`
  (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md),
  [DEC-0170](../decisions/DEC-0170-allowlist-filter-behavior-clause.md)).
  Implements `CodeHostConnector.A-9`.
- `GitHubConnector.A-10` — permission probe: `GET
  /app/installations/{installation_id}` (or, for a delegated-user
  token, `GET /repos/{owner}/{repo}` and its `permissions` field)
  returns the installation's actually-granted permission set as
  `PermissionSet`; this is the same introspection
  `CapabilityManifest.team_sync` is derived from
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
  Implements `CodeHostConnector.A-10`.
- `GitHubConnector.A-11` — webhook/event subscription: GitHub Apps
  declare their subscribed event families
  (`pull_request`, `pull_request_review`, `push`,
  `check_run`/`check_suite`) once, at App-registration time, and
  receive deliveries for every repository the installation covers —
  there is no per-call, per-repo GitHub registration endpoint.
  `webhook.register(repo, event_types[], callback_url)` is therefore
  local bookkeeping: it records which `(repo, event_types,
  callback_url)` tuples are active and installs a delivery filter;
  incoming deliveries outside any registered tuple are dropped before
  normalization. `webhook.unregister` removes the tuple. Every
  delivery that passes the filter is signature-verified
  (`X-Hub-Signature-256`, HMAC-SHA256, per-installation secret; per
  [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md))
  before normalizing into `HostEvent`
  (per [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).
  A delivery failing signature verification is discarded, never
  normalized. Implements `CodeHostConnector.A-11`.
- `GitHubConnector.B-1` — conformance: passes
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s conformance
  suite in full, unchanged from what the local-git fake passes — the
  swap-in validation
  (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md),
  [ST-0031](../stories/ST-0031-github-connector.md) AC6).
- `GitHubConnector.B-2` — capability manifest: `host_type:
  "github-cloud"`. Minimum set (all `true`): `fork_provisioning`,
  `branch_ops`, `pr_lifecycle`, `review_posting`, `read_access`,
  `permission_probe`, `check_result_posting`. Above-minimum:
  `required_check_registration: true`, `review_dismissal: true`
  (`DELETE /repos/{owner}/{repo}/pulls/{number}/reviews/{id}/dismissals`
  is stable and available), `native_path_scoped_reviewers: true`
  (CODEOWNERS, read-only), `webhook_delivery: true`; `team_sync` is
  set per-installation from `A-10`'s introspection, `true` only when
  org-level `members` permission was granted
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).

## Component Invariants

- `C-1` — the Orchestrator App and Reader App are structurally
  distinct App registrations and installations; `A-9` never issues a
  call with Orchestrator credentials, and `A-1`–`A-8`/`A-11` never
  issue a call with Reader credentials
  (per [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)),
  satisfying [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
  `C-2`.
- `C-2` — no operation writes repository content; `A-7`'s CODEOWNERS
  introspection and every other element item are read-only with
  respect to file content
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)),
  satisfying [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
  `C-1`.
- `C-3` — every fork provisioned via `A-1` lands in the Orchestrator
  App's dedicated service-owned account, never in the source
  repository's own org or a source-org fork
  (per [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).

## Implementation Guidance

### Constraints

- `IG-1` — REST is the default wire protocol for every operation
  family with adequate REST coverage; GraphQL is used only for
  CODEOWNERS-derived reviewer resolution and bulk team-membership
  queries
  (per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
- `IG-2` — `403` disambiguation is normative: `rate-limited` when
  `X-RateLimit-Remaining: 0` or `Retry-After` is present in the
  response headers, else `permission-denied`; no code path may treat
  one as the other
  (per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
- `IG-3` — idempotency on natural-key creation calls (`A-1`
  fork, `A-2` branch create, `A-3` PR open) is implemented as
  check-before-create — a read for the existing resource precedes
  every write — never create-then-catch-error
  (per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
- `IG-4` — `team_sync` and any other permission-gated capability is
  determined by introspecting the Orchestrator App installation's
  actually-granted permissions (`A-10`) at connector startup and on
  installation-permission-change webhooks, never assumed from
  deployment configuration alone
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
- `IG-5` — each App installation's webhook signing secret is generated
  per-installation and stored in the encrypted app-database secret
  store, never shared across installations
  (per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
  [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
- `IG-6` — `A-6`/`A-7` branch-protection administration targets
  classic per-branch branch protection exclusively; repository
  rulesets are not read, written, or reconciled against by this
  element
  (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
- `IG-7` — check administration (`A-5`/`A-6`) is isolated behind its
  own internal adapter boundary, per
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s `IG-2`
  (general good practice, not a provisional marker — check
  administration is no longer provisional, per
  [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)).
- `IG-8` — `A-11`'s local registration state (the `(repo, event_types,
  callback_url)` filter tuples) is not guaranteed durable across a
  connector restart: callers must re-issue `webhook.register` for
  every tuple they need on process start, which is idempotent and
  cheap. Any gap between a restart and re-registration is bounded by
  [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)'s
  reconciliation sweep, the system's existing backstop for missed
  events — this element does not need its own independent persistence
  story for registration state.

### Notes

- `A-11`'s `webhook.register`/`unregister` are local filtering
  bookkeeping, not GitHub API calls — GitHub Apps subscribe to event
  families once at App-registration time and deliver for every
  installed repository; this element narrows deliveries to what
  callers actually registered for.
- Rate-limit backoff scheduling (exponential with jitter, honoring
  `Retry-After`/`X-RateLimit-Reset`) is a reasonable default; the
  exact schedule is not part of this contract
  (per [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
  Implementation Guidance Notes).
- The Orchestrator App's org-level `members` permission is typically
  the harder grant to obtain from an org admin; deployments that can't
  obtain it still run Groundwork at the minimum capability set, with
  [CMP-0004](CMP-0004-governance-gate-engine.md)'s policy compiler
  emulating team-scoped routing.

## Dependencies

- [CMP-0005](CMP-0005-code-host-connector-protocol.md) — implements
  the `CodeHostConnector` protocol, `CapabilityManifest` schema, and
  `HostEvent` schema in full; consumes nothing else from it. Internals
  of consumers ([CMP-0001](CMP-0001-artifact-store-service.md),
  [CMP-0004](CMP-0004-governance-gate-engine.md)) are out of bounds —
  they program against
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s contract, not
  this adapter directly.
- Identity component ([CMP-0007](CMP-0007-identity-and-access.md),
  not yet contract-complete) — supplies the delegated-user OAuth token
  `A-4`'s `post_as_user` accepts, and the pre-signed
  `attribution_block` `post_as_program_user` accepts, both opaque and
  passed through unmodified
  (per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).

## Acceptance & Test Expectations

1. Conformance to [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
   suite, unchanged from the local-git fake, is the headline expectation
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
   [ST-0031](../stories/ST-0031-github-connector.md) AC1, AC6).
2. The declared `CapabilityManifest` matches `GitHubConnector.B-2`'s
   values exactly for a given installation, including a `team_sync`
   flag that reflects that installation's actual granted permissions,
   verified by an introspection test against both an org-level and a
   repo-only installation fixture
   (per [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
3. Idempotent re-invocation: retrying `A-1`/`A-2`/`A-3` creation calls
   with the same natural key returns the existing resource — verified
   via check-before-create, never a duplicate fork/branch/PR
   (per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
4. Required-check registration/unregistration and result posting
   (`A-5`/`A-6`) support per-PR blocking, idempotent re-posting, and
   flipping an already-`success` check-run back to `failure` on an
   open PR
   (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md),
   [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
   [DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md),
   [ST-0031](../stories/ST-0031-github-connector.md) AC3).
5. Allowlist enforcement: `A-9` calls against a non-allowlisted
   repository or an excluded path behave exactly as
   [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s `A-9`
   documents, verified against a `governance/repos.yaml` fixture, and
   the Reader App's credentials are never reachable from an
   `A-1`–`A-8` code path
   (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md),
   [DEC-0174](../decisions/DEC-0174-github-connector-identity-architecture.md)).
6. Webhook events: deliveries with a valid `X-Hub-Signature-256` for
   a registered `(repo, event_type)` normalize to `HostEvent`;
   deliveries with an invalid signature are discarded and never
   normalized; deliveries outside any registered tuple are dropped
   (per [DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md),
   [DEC-0176](../decisions/DEC-0176-github-capability-and-admin-surface.md)).
7. `403` responses disambiguate correctly into `rate-limited` vs.
   `permission-denied` per `IG-2`'s header rule, verified against
   fixtures for both a real permission failure and a secondary
   rate-limit response
   (per [DEC-0175](../decisions/DEC-0175-github-wire-protocol-conventions.md)).
8. Consumer test suites that pass against the local-git fake pass
   against this connector unchanged
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md),
   [ST-0031](../stories/ST-0031-github-connector.md) AC6).
9. Restart recovery: after a connector restart with no re-registration,
   a caller that re-issues `webhook.register` for the same tuples
   resumes receiving filtered deliveries with no duplicate or lost
   registration state; deliveries for the gap window are recoverable
   via the reconciliation sweep, not this element's own persistence
   (per `IG-8`, [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).

## Out of Scope

- The Bitbucket Data Center implementation of
  [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s protocol,
  deferred to backlog behind `TRG-0010`
  ([CMP-0006](CMP-0006-bitbucket-data-center-connector.md),
  per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).
- Token issuance, OAuth linkage, and program-user attribution-block
  signing — identity's concern
  ([CMP-0007](CMP-0007-identity-and-access.md),
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md));
  `A-4` accepts opaque credential/attribution parameters and never
  interprets them.
- Repository rulesets as a branch-protection backend — classic branch
  protection only, per `IG-6`; a future story would be needed to add
  ruleset support.
- Writing to CODEOWNERS or any other repository content — permanently
  out of scope for the whole system
  (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
- GitHub Enterprise Server as a target — this contract is GitHub
  cloud (`github.com`) only
  (per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).
- Provisioning or rotating the Orchestrator/Reader App registrations
  themselves (org admin setup, App manifest creation) — deployment
  operations, not this contract's runtime behavior.
- Connectors for hosts other than GitHub and (deferred) Bitbucket
  Data Center
  ([ST-0028](../stories/ST-0028-additional-code-host-connectors.md),
  per [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md)).
