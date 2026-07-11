---
id: CMP-0009
type: component
title: GitHub Connector
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  V1 reference adapter for CMP-0005 (Code-Host Connector Protocol),
  targeting GitHub cloud. Implements full protocol via REST/GraphQL
  against GitHub cloud, with dual GitHub Apps (Orchestrator for writes,
  Reader for allowlisted read-only access). Check-run result posting,
  required-check registration via classic branch protection. Every GitHub
  error maps to closed typed-error vocabulary. Idempotency on natural-key
  creation via check-before-create. Capability manifest declares
  native-path-scoped reviewers (CODEOWNERS) and team-sync support when
  org-level members permission granted.
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0005, CMP-0015]
cites: [DEC-0014, DEC-0028, DEC-0043, DEC-0045, DEC-0049, DEC-0079,
        DEC-0141, DEC-0142, DEC-0145, DEC-0152, DEC-0153, DEC-0156,
        DEC-0167, DEC-0168, DEC-0169, DEC-0170, DEC-0172, DEC-0173,
        DEC-0174, DEC-0175, DEC-0176, DEC-0177, DEC-0232]
---

# CMP-0009: GitHub Connector

## Purpose

The v1 reference adapter of the
code-host connector protocol (CMP-0005):
GitHub (cloud) REST/GraphQL and webhook integration, an honest
capability manifest, the Checks API and required-status-checks as the
required-check surface, CODEOWNERS and org teams for reviewer/team
routing. Takes Bitbucket Data Center's former v1 slot
(per DEC-0172; see
CMP-0006, now deferred).

## Ubiquitous Language

Connector, Code-Host Connector, Capability Manifest, Adapter,
Orchestrator App, Reader App — per [CONTEXT.md](../../CONTEXT.md).

## Design Elements

Decomposition per DEC-0177: a single service element carrying every
operation family; the graduation review found no split warranted.

### GitHubConnector (service)

Implements: ST-0031,
ST-0023
Uses: CodeHostConnector (interface), CapabilityManifest (interface),
HostEvent (interface), SecretStore.A-1 (interface), SecretStore.A-2 (interface)

Implements CMP-0005's
`CodeHostConnector` protocol in full, against GitHub cloud
(`github.com`). Two credential-distinct GitHub App installations back
the element: the **Orchestrator App** (write: contents, pull requests,
checks, administration, and — where granted — org members) for `A-1`
through `A-8` and `A-11`; the **Reader App** (read-only: contents,
metadata), installed only on allowlisted repositories, exclusively for
`A-9` (per DEC-0174).
REST is the default wire protocol; GraphQL backs only CODEOWNERS-derived
reviewer resolution and bulk team-membership queries
(per DEC-0175).
Every item below maps GitHub-native behavior onto
CMP-0005's typed error
vocabulary and idempotency convention
(per DEC-0167):
a `404` maps to `not-found`; a `403` maps to `rate-limited` when
`X-RateLimit-Remaining: 0` or `Retry-After` is present, else
`permission-denied`; a `409`/unprocessable `422` maps to `conflict`;
creation operations on a natural key check for the existing resource
before writing, returning it instead of creating a duplicate
(per DEC-0175).

- `GitHubConnector.A-1` — `provision_fork`: `POST
  /repos/{owner}/{repo}/forks`, targeting the Orchestrator App's
  dedicated service-owned account (per
  DEC-0174).
  Check-before-create: `GET /repos/{fork-owner}/{repo}` first; if the
  fork already exists, its `{fork_url, default_branch}` is returned
  unchanged. Implements
  CMP-0005's
  `CodeHostConnector.A-1`, the fork-provisioning leg of the fork-pull
  gating model (per DEC-0028).
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
  (per DEC-0153,
  DEC-0174).
  Implements `CodeHostConnector.A-4`, both review-posting paths of
  DEC-0043.
- `GitHubConnector.A-5` — check-run result posting: GitHub's Checks
  API, `POST /repos/{owner}/{repo}/check-runs` for a first post, `PATCH
  .../check-runs/{id}` for re-posts — never commit statuses. Re-posting
  is unconditional (idempotent by design) and can flip an already
  `success` check-run back to `failure` on an open PR
  (per DEC-0173,
  DEC-0145,
  DEC-0141).
  Implements `CodeHostConnector.A-5`.
- `GitHubConnector.A-6` — required-check registration:
  `register_required`/`unregister_required` read-modify-write the
  `required_status_checks.contexts` (check-run names) array via
  classic branch protection (`PUT`/`GET
  /repos/{owner}/{repo}/branches/{branch}/protection`)
  (per DEC-0176).
  Exclusively invoked by the gate engine
  (per DEC-0142).
  Implements `CodeHostConnector.A-6`.
- `GitHubConnector.A-7` — branch-protection administration:
  `protection.set`/`protection.get` map directly onto classic
  `PUT`/`GET .../branches/{branch}/protection`
  (per DEC-0176).
  Rule shapes above
  CMP-0005's documented
  minimum (per DEC-0168) that classic branch protection cannot
  express fail `capability-unsupported`. CODEOWNERS is read-only
  introspected to populate `CapabilityManifest.native_path_scoped_reviewers`;
  this element never writes a `CODEOWNERS` file
  (per DEC-0014).
  Implements `CodeHostConnector.A-7`.
- `GitHubConnector.A-8` — team administration: `team.create` via
  `POST /orgs/{org}/teams`, `team.sync` via `PUT
  /orgs/{org}/teams/{team_slug}/memberships/{username}` per member
  added/removed. Available only when the Orchestrator App's
  installation was granted org-level `members` permission; otherwise
  every call fails `capability-unsupported`
  (per DEC-0176).
  Implements `CodeHostConnector.A-8`.
- `GitHubConnector.A-9` — read-only browse/search: exclusively the
  Reader App's credentials
  (per DEC-0174).
  `read.browse`/`read.file` via `GET
  /repos/{owner}/{repo}/contents/{path}?ref={ref}`; `read.search` via
  `GET /search/code` scoped with `repo:{owner}/{repo}`. Allowlist
  filtering (`governance/repos.yaml`, path excludes) is applied before
  any GitHub call is issued — a non-allowlisted repository never
  reaches the API and returns `not-found`, indistinguishable from a
  repository absent on GitHub; excluded paths never appear in listing,
  search, or read results; every returned item carries `{repo, ref,
  path}`
  (per DEC-0049,
  DEC-0170).
  Implements `CodeHostConnector.A-9`.
- `GitHubConnector.A-10` — permission probe: `GET
  /app/installations/{installation_id}` (or, for a delegated-user
  token, `GET /repos/{owner}/{repo}` and its `permissions` field)
  returns the installation's actually-granted permission set as
  `PermissionSet`; this is the same introspection
  `CapabilityManifest.team_sync` is derived from
  (per DEC-0176).
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
  DEC-0176)
  before normalizing into `HostEvent`
  (per DEC-0169).
  A delivery failing signature verification is discarded, never
  normalized. Implements `CodeHostConnector.A-11`.
- `GitHubConnector.B-1` — conformance: passes
  CMP-0005's conformance
  suite in full, unchanged from what the local-git fake passes — the
  swap-in validation
  (per DEC-0079,
  ST-0031 AC6).
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
  (per DEC-0176).

## Component Invariants

- `C-1` — the Orchestrator App and Reader App are structurally
  distinct App registrations and installations; `A-9` never issues a
  call with Orchestrator credentials, and `A-1`–`A-8`/`A-11` never
  issue a call with Reader credentials
  (per DEC-0174),
  satisfying CMP-0005's
  `C-2`.
- `C-2` — no operation writes repository content; `A-7`'s CODEOWNERS
  introspection and every other element item are read-only with
  respect to file content
  (per DEC-0014),
  satisfying CMP-0005's
  `C-1`.
- `C-3` — every fork provisioned via `A-1` lands in the Orchestrator
  App's dedicated service-owned account, never in the source
  repository's own org or a source-org fork
  (per DEC-0174).

## Implementation Guidance

### Constraints

- `IG-1` — REST is the default wire protocol for every operation
  family with adequate REST coverage; GraphQL is used only for
  CODEOWNERS-derived reviewer resolution and bulk team-membership
  queries
  (per DEC-0175).
- `IG-2` — `403` disambiguation is normative: `rate-limited` when
  `X-RateLimit-Remaining: 0` or `Retry-After` is present in the
  response headers, else `permission-denied`; no code path may treat
  one as the other
  (per DEC-0175).
- `IG-3` — idempotency on natural-key creation calls (`A-1`
  fork, `A-2` branch create, `A-3` PR open) is implemented as
  check-before-create — a read for the existing resource precedes
  every write — never create-then-catch-error
  (per DEC-0175).
- `IG-4` — `team_sync` and any other permission-gated capability is
  determined by introspecting the Orchestrator App installation's
  actually-granted permissions (`A-10`) at connector startup and on
  installation-permission-change webhooks, never assumed from
  deployment configuration alone
  (per DEC-0176).
- `IG-5` — each App installation's webhook signing secret is generated
  per-installation and stored in the Secret Store
  (CMP-0015, graduated per
  DEC-0232), never
  shared across installations
  (per DEC-0152,
  DEC-0176).
- `IG-6` — `A-6`/`A-7` branch-protection administration targets
  classic per-branch branch protection exclusively; repository
  rulesets are not read, written, or reconciled against by this
  element
  (per DEC-0176).
- `IG-7` — check administration (`A-5`/`A-6`) is isolated behind its
  own internal adapter boundary, per
  CMP-0005's `IG-2`
  (general good practice, not a provisional marker — check
  administration is no longer provisional, per
  DEC-0173).
- `IG-8` — `A-11`'s local registration state (the `(repo, event_types,
  callback_url)` filter tuples) is not guaranteed durable across a
  connector restart: callers must re-issue `webhook.register` for
  every tuple they need on process start, which is idempotent and
  cheap. Any gap between a restart and re-registration is bounded by
  DEC-0145's
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
  (per CMP-0005's
  Implementation Guidance Notes).
- The Orchestrator App's org-level `members` permission is typically
  the harder grant to obtain from an org admin; deployments that can't
  obtain it still run Groundwork at the minimum capability set, with
  CMP-0004's policy compiler
  emulating team-scoped routing.

## Dependencies

- CMP-0005 — implements
  the `CodeHostConnector` protocol, `CapabilityManifest` schema, and
  `HostEvent` schema in full; consumes nothing else from it. Internals
  of consumers (CMP-0001,
  CMP-0004) are out of bounds —
  they program against
  CMP-0005's contract, not
  this adapter directly.
- CMP-0015 — consumed sections:
  `SecretStore.A-1`/`A-2` for the per-installation webhook signing
  secrets of `IG-5`
  (per DEC-0232,
  DEC-0152).
- Identity component (CMP-0007) —
  supplies the delegated-user OAuth token
  `A-4`'s `post_as_user` accepts, and the pre-signed
  `attribution_block` `post_as_program_user` accepts, both opaque and
  passed through unmodified
  (per DEC-0153).

## Acceptance & Test Expectations

1. Conformance to CMP-0005's
   suite, unchanged from the local-git fake, is the headline expectation
   (per DEC-0079,
   DEC-0045,
   ST-0031 AC1, AC6).
2. The declared `CapabilityManifest` matches `GitHubConnector.B-2`'s
   values exactly for a given installation, including a `team_sync`
   flag that reflects that installation's actual granted permissions,
   verified by an introspection test against both an org-level and a
   repo-only installation fixture
   (per DEC-0176).
3. Idempotent re-invocation: retrying `A-1`/`A-2`/`A-3` creation calls
   with the same natural key returns the existing resource — verified
   via check-before-create, never a duplicate fork/branch/PR
   (per DEC-0175).
4. Required-check registration/unregistration and result posting
   (`A-5`/`A-6`) support per-PR blocking, idempotent re-posting, and
   flipping an already-`success` check-run back to `failure` on an
   open PR
   (per DEC-0173,
   DEC-0145,
   DEC-0141,
   ST-0031 AC3).
5. Allowlist enforcement: `A-9` calls against a non-allowlisted
   repository or an excluded path behave exactly as
   CMP-0005's `A-9`
   documents, verified against a `governance/repos.yaml` fixture, and
   the Reader App's credentials are never reachable from an
   `A-1`–`A-8` code path
   (per DEC-0049,
   DEC-0174).
6. Webhook events: deliveries with a valid `X-Hub-Signature-256` for
   a registered `(repo, event_type)` normalize to `HostEvent`;
   deliveries with an invalid signature are discarded and never
   normalized; deliveries outside any registered tuple are dropped
   (per DEC-0169,
   DEC-0176).
7. `403` responses disambiguate correctly into `rate-limited` vs.
   `permission-denied` per `IG-2`'s header rule, verified against
   fixtures for both a real permission failure and a secondary
   rate-limit response
   (per DEC-0175).
8. Consumer test suites that pass against the local-git fake pass
   against this connector unchanged
   (per DEC-0079,
   ST-0031 AC6).
9. Restart recovery: after a connector restart with no re-registration,
   a caller that re-issues `webhook.register` for the same tuples
   resumes receiving filtered deliveries with no duplicate or lost
   registration state; deliveries for the gap window are recoverable
   via the reconciliation sweep, not this element's own persistence
   (per `IG-8`, DEC-0145).

## Out of Scope

- The Bitbucket Data Center implementation of
  CMP-0005's protocol,
  deferred to backlog behind `TRG-0010`
  (CMP-0006,
  per DEC-0172).
- Token issuance, OAuth linkage, and program-user attribution-block
  signing — identity's concern
  (CMP-0007,
  ST-0021);
  `A-4` accepts opaque credential/attribution parameters and never
  interprets them.
- Repository rulesets as a branch-protection backend — classic branch
  protection only, per `IG-6`; a future story would be needed to add
  ruleset support.
- Writing to CODEOWNERS or any other repository content — permanently
  out of scope for the whole system
  (per DEC-0014).
- GitHub Enterprise Server as a target — this contract is GitHub
  cloud (`github.com`) only
  (per DEC-0172).
- Provisioning or rotating the Orchestrator/Reader App registrations
  themselves (org admin setup, App manifest creation) — deployment
  operations, not this contract's runtime behavior.
- Connectors for hosts other than GitHub and (deferred) Bitbucket
  Data Center
  (ST-0028,
  per DEC-0156).

