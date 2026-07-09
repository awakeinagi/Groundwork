---
id: CMP-0007
type: component
title: Identity & Access
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Who anyone is and how the system acts for them. Pluggable auth-provider
  protocol with email/OIDC v1 provider. Session issuance and validation.
  Person-id resolution and role claims via shared RoleResolution seam
  (CMP-0016). OAuth host-identity linkage over secret store (CMP-0015).
  Delegated-review posting with signed attribution block consumed by
  gate-policy check. Seven elements: AuthProvider (protocol), AuthSubject,
  SessionToken, IdentityService, HostIdentityLink, AttributionBlock,
  ReviewDelegationService. Secret Store graduated per DEC-0232.
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0003, CMP-0005, CMP-0015, CMP-0016]
cites: [DEC-0024, DEC-0033, DEC-0040, DEC-0043, DEC-0046, DEC-0143, DEC-0152,
        DEC-0153, DEC-0154, DEC-0232, DEC-0233, DEC-0234, DEC-0235, DEC-0236,
        DEC-0237, DEC-0238]
---

# CMP-0007: Identity & Access

## Purpose

Who anyone is, and how the system acts for them: the pluggable
auth-provider protocol with the v1 email/OIDC provider
(DEC-0024), session
issuance and validation
(DEC-0236),
person-id resolution and role claims backed by the shared
role-resolution seam
(DEC-0046,
DEC-0234),
OAuth host-identity linkage over the secret store
(DEC-0237,
DEC-0152),
and delegated-review posting with the signed attribution block
(DEC-0043,
DEC-0153).

Element decomposition per
SES-0045:
seven elements. Graduation review outcome: the secret store graduated
to CMP-0015
(per DEC-0232);
`AttributionBlock` stays here with
CMP-0004 consuming it as a
dependency
(per DEC-0233);
role-claims evaluation lives in
CMP-0016
(per DEC-0234).
All API schemas resolve against this document's value elements or
dependency contracts named in `## Dependencies`.

## Ubiquitous Language

Attribution Block, Approver, Role Claims, Secret Store, Session Token,
Person Registry, Connector — per [CONTEXT.md](../../CONTEXT.md).

## Design Elements

### AuthProvider (protocol)

Implements: ST-0022

- `AuthProvider.A-1` — `authenticate(credential) → AuthSubject`; the
  credential shape is provider-specific (email challenge, OIDC
  callback assertion); typed error: `auth-failed` (never
  distinguishes unknown-user from bad-credential)
  (per DEC-0024).
- `AuthProvider.B-1` — conformance: swapping providers is deployment
  configuration plus a new adapter passing the shared provider suite —
  no core change; providers are stateless — sessions belong to
  `IdentityService`, never a provider
  (per DEC-0024,
  DEC-0236).

### AuthSubject (value)

Implements: ST-0022

- `AuthSubject.D-1` — schema: `provider_id` (string), `subject`
  (string, stable within the provider), optional `email`, optional
  `display_name`. Never a person-id — resolution is
  `IdentityService.A-1`'s job
  (per DEC-0024,
  DEC-0046).

### SessionToken (value)

Implements: ST-0022

- `SessionToken.D-1` — schema: `token` (opaque handle, ≥128 bits of
  entropy), `expires_at` (timestamp). Carries no claims and no
  identity payload; everything else is server-side state
  (per DEC-0236).

### IdentityService (service)

Implements: ST-0022

- `IdentityService.A-1` — `resolve(auth_subject) → person_id` via the
  `people.yaml` value (`GovernanceConfig.D-1`); typed error:
  `unmapped-subject`
  (per DEC-0046).
- `IdentityService.A-2` — `host_identity(person_id, identity_column) →
  identifier` — the registry entry's provider-specific column (host
  username, Jira accountId) each connector resolves from; typed
  errors: `not-found` (no such person), `not-linked` (column empty)
  (per DEC-0046).
- `IdentityService.A-3` — `claims(person_id) → RoleClaims`, delegated
  to `RoleResolution.A-1`
  (CMP-0016) at
  the current governance ref and time; typed error: `unknown-person`
  (per DEC-0040,
  DEC-0234).
- `IdentityService.A-4` — `issue_session(auth_subject) → SessionToken`:
  resolves the person-id, records the session server-side, returns the
  opaque handle; typed error: `unmapped-subject`
  (per DEC-0236).
- `IdentityService.A-5` — `validate_session(token) → {person_id}`;
  typed error: `session-invalid` (expired, revoked, or unknown — never
  distinguished)
  (per DEC-0236).
- `IdentityService.A-6` — `revoke_session(token) → ok`, idempotent
  (per DEC-0236).
- `IdentityService.A-7` — `map_emails(emails[]) → {email →
  person_id | unmapped}` — the batch resolver backing
  CMP-0001's
  `migrate-person-ids` mechanical write; pure read over the registry
  (per DEC-0235,
  DEC-0046).
- `IdentityService.B-1` — session state (person-id, expiry) lives in
  the app database via `AppDatabasePort.A-3`; the handle is
  meaningless without it; revocation takes effect on the next
  `validate_session` call — there is no cached validity
  (per DEC-0236).
- `IdentityService.B-2` — session TTL comes from deployment
  configuration; expiry is enforced at validation, not by background
  cleanup (cleanup is hygiene, never semantics)
  (per DEC-0236).
- `IdentityService.B-3` — role claims are resolved fresh per request
  via `A-3`, never embedded in the session — a delegation window
  opening or closing changes the next request's claims
  (per DEC-0236,
  DEC-0040).

### HostIdentityLink (entity)

Implements: ST-0021,
ST-0022

- `HostIdentityLink.D-1` — identity `(person_id, host)`; attributes:
  `host_username`, `token_ref` (a
  CMP-0015 key — never the token itself),
  `scopes`, `linked_at`; states: `pending | linked | needs-reauth`
  (per DEC-0046,
  DEC-0237,
  DEC-0152).
- `HostIdentityLink.A-1` — `begin_link(person_id, host) →
  {authorize_url, state}`: starts the OAuth grant, records `pending`
  keyed by the `state` nonce
  (per DEC-0237).
- `HostIdentityLink.A-2` — `complete_link(state, callback_params) →
  linked`: finishes the code exchange, stores the token via
  `SecretStore.A-1`, transitions to `linked`; typed errors:
  `link-failed` (exchange rejected), `not-found` (unknown/expired
  `state`)
  (per DEC-0237,
  DEC-0152).
- `HostIdentityLink.A-3` — `status(person_id, host) → unlinked |
  pending | linked | needs-reauth` — the UI's "shown as connected"
  read (per DEC-0237,
  DEC-0043).
- `HostIdentityLink.A-4` — `unlink(person_id, host) → ok`: deletes the
  stored token (`SecretStore.A-3`) and the link record; idempotent
  (per DEC-0237).
- `HostIdentityLink.B-1` — lifecycle: `begin_link` supersedes any
  prior `pending` for the same `(person_id, host)`; a host-reported
  expired/revoked token transitions `linked → needs-reauth` — the
  state that drives
  ST-0021's
  re-authorization prompt; re-linking from `needs-reauth` runs the
  same `A-1`/`A-2` flow
  (per DEC-0237,
  DEC-0043).

### AttributionBlock (value)

Implements: ST-0021

- `AttributionBlock.D-1` — schema: `schema_version` (int),
  `person_id`, `pr_ref`, `decision_timestamp`, `key_id`, `signature`
  (per DEC-0153,
  DEC-0238).
- `AttributionBlock.D-2` — canonical serialization: UTF-8 JSON with
  lexicographically sorted keys and no insignificant whitespace; the
  signature covers the canonical bytes of all fields except
  `signature`
  (per DEC-0153).
- `AttributionBlock.B-1` — signing: Ed25519-class service key; the
  private key lives in CMP-0015; the
  ordered active public-key list, keyed by `key_id`, is deployment
  configuration
  (per DEC-0153,
  DEC-0238,
  DEC-0152).
- `AttributionBlock.B-2` — verification contract (consumed by
  CMP-0004): valid iff the
  signature verifies under the configured public key matching
  `key_id` AND the `person_id` resolves in `people.yaml` to a holder
  of the required role at verification time; verification capability
  never implies signing capability
  (per DEC-0153,
  DEC-0238,
  DEC-0233).

### ReviewDelegationService (service)

Implements: ST-0021

- `ReviewDelegationService.A-1` — `post_review(pr_ref, person_id,
  verdict, body) → {path: as-user | program-user}`; typed errors:
  `reauth-required` (OAuth path with expired/revoked token),
  `unmapped-person`, `no-path-configured` (the person's roles map to
  no review path); `CodeHostConnector.A-4`'s own typed errors
  (`not-found`, `permission-denied`, `rate-limited`) pass through
  unmapped — they describe the host interaction, not the delegation
  (per DEC-0043,
  DEC-0154).
- `ReviewDelegationService.B-1` — path selection reads the
  role→review-path mapping from deployment configuration at review
  time; no governance file is consulted or modified
  (per DEC-0154).
- `ReviewDelegationService.B-2` — as-user path: fetches the token via
  the person's `HostIdentityLink`, posts through
  `CodeHostConnector.A-4` `review.post_as_user` — host-side audit
  shows the real approver
  (per DEC-0043).
- `ReviewDelegationService.B-3` — program-user path: constructs the
  `AttributionBlock`, signs it, posts through `CodeHostConnector.A-4`
  `review.post_as_program_user`
  (per DEC-0043,
  DEC-0153).
- `ReviewDelegationService.B-4` — an expired or revoked token on the
  as-user path fails with `reauth-required` and flips the link to
  `needs-reauth`; it **never** silently falls back to the program
  user — that would misattribute the review path
  (per DEC-0043,
  DEC-0153).

## Component Invariants

- `C-1` — no secret material (OAuth tokens, the signing key) is
  stored, returned, or logged by this component outside
  CMP-0015; contracts traffic only in
  `token_ref` keys
  (per DEC-0152).
- `C-2` — every identity that crosses this component's boundary
  outward is a person-id; raw provider subjects appear only in
  `AuthSubject` inputs
  (per DEC-0046).
- `C-3` — no role-membership or delegation-window judgement is
  computed here; all claims come from
  CMP-0016's
  `RoleResolution`
  (per DEC-0234).

## Implementation Guidance

### Constraints

- `IG-1` — the v1 auth provider is email/OIDC; organizational SSO
  arrives as a new `AuthProvider` adapter, never a core change
  (per DEC-0024).
- `IG-2` — the v1 signing algorithm is Ed25519; the `key_id` scheme
  must allow a future algorithm change to ride the same rotation
  mechanism (per DEC-0153,
  DEC-0238).

### Notes

- OIDC provider adapters should use a mature library for the code
  exchange and assertion validation rather than hand-rolling; the
  provider suite exercises semantics, not library choice.
- The re-authorization prompt surfaced on `reauth-required` is
  rendered by the UI (ST-0042);
  this component only guarantees the typed error and the
  `needs-reauth` state.

## Dependencies

- CMP-0003 — consumed sections:
  `AppDatabasePort.A-1` (UnitOfWork), `AppDatabasePort.A-3`
  (bookkeeping) for session and link state.
- CMP-0005 — consumed
  sections: `CodeHostConnector.A-4` (both review-posting operations);
  the attribution block crosses it as an opaque pre-signed value.
- CMP-0015 — consumed sections:
  `SecretStore.A-1`/`A-2`/`A-3` for OAuth tokens and the attribution
  signing key.
- CMP-0016 —
  consumed sections: `GovernanceConfig.D-1`/`D-2` (the `people.yaml`
  value for `A-1`/`A-2`/`A-7`), `RoleResolution.A-1` and
  `RoleClaims.D-1` (claims for `A-3`).

## Acceptance & Test Expectations

1. Provider conformance: the shared suite passes with the v1
   email/OIDC adapter; switching providers is configuration only
   (per DEC-0024).
2. Session lifecycle: issue → validate → revoke → `session-invalid`;
   expiry honored at validation across restart; revocation effective
   on the next call
   (per DEC-0236).
3. Review paths: both paths exercised against the local-git fake
   connector; the negative path — expired/revoked token — yields
   `reauth-required`, flips the link to `needs-reauth`, and posts
   nothing as the program user
   (per DEC-0043).
4. Attribution round-trip: sign → canonical-serialize → verify with
   the configured public key; a rotation fixture (two active keys,
   blocks signed under each) verifies both; a tampered field fails
   (per DEC-0153,
   DEC-0238).
5. Secret hygiene: captured logs and error output across the suite
   contain no token or key material
   (per DEC-0152).
6. Migration mapping: `map_emails` resolves a bootstrap-era fixture
   (mapped, unmapped, and duplicate-email cases) correctly
   (per DEC-0235).
7. Delegation freshness: a delegation window opening between two
   requests changes the second request's claims with no re-login
   (per DEC-0040,
   DEC-0236).

## Out of Scope

- Login and linking UI — ST-0042
  / EP-0006; this component
  supplies the contracts those components call.
- Attribution verification at gate time — the `gate-policy` check's
  side of the seam (CMP-0004,
  ST-0014); this component
  publishes the block and its verification contract.
- Host review API plumbing — CMP-0005
  defines it, CMP-0009 implements it.
- Executing `migrate-person-ids` — CMP-0001's
  mechanical-write operation; this component only maps
  (per DEC-0235).
- Secret storage mechanics — CMP-0015.
- Role-membership evaluation — CMP-0016.
- Machine-verified program-user approvals of mechanical/System-Decision
  auto-PRs — they carry no attribution block; the requirement applies
  only to reviews standing in for a human approver
  (per DEC-0033,
  DEC-0143).
- Participant Profiles — interaction memory, not identity
  (EP-0002).
