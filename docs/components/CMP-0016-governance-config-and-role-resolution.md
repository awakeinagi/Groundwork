---
id: CMP-0016
type: component
title: Governance Config & Role Resolution
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: governance
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [CMP-0001]
cites: [DEC-0020, DEC-0034, DEC-0037, DEC-0040, DEC-0046, DEC-0140, DEC-0164,
        DEC-0234]
---

# CMP-0016: Governance Config & Role Resolution

> Graduated out of [CMP-0004](CMP-0004-governance-gate-engine.md) per
> [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md):
> the parsed governance-config value plus the single shared
> implementation of role-membership and delegation-window evaluation,
> consumed by both [CMP-0004](CMP-0004-governance-gate-engine.md)
> (gate verdicts) and [CMP-0007](CMP-0007-identity-and-access.md)
> (person resolution and role claims). The `governance/` file schemas
> themselves remain [CMP-0001](CMP-0001-artifact-store-service.md)'s
> (`SchemaValidator.D-2`).

## Purpose

One answer to "who holds which role right now": the typed in-memory
value of the five `governance/` files at a git ref, and the resolution
service that evaluates role membership — including active time-bounded
delegation — at an explicit ref and point in time
(per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
[DEC-0040](../decisions/DEC-0040-role-pool-delegation.md)).

## Ubiquitous Language

Governance-as-Code, Gate Policy, Approver, Role Claims — per
[CONTEXT.md](../../CONTEXT.md).

## Design Elements

### GovernanceConfig (value)

Implements: [ST-0012](../stories/ST-0012-governance-config-schemas.md)

- `GovernanceConfig.D-1` — the parsed, typed representation of the five
  `governance/` files (`roles.yaml`, `domains.yaml`,
  `gate-policies.yaml`, `repos.yaml`, `people.yaml`) at a resolving git
  ref; schema shape is exactly
  [CMP-0001](CMP-0001-artifact-store-service.md)'s published
  `SchemaValidator.D-2` assets — this element defines no schema of its
  own, only the in-memory value its consumers read. Equality by value
  at a given ref; never persisted independently of git
  (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
  [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
- `GovernanceConfig.D-2` — role membership entries carry stable
  person-ids from `people.yaml` and optional time-bounded delegation
  windows; domain entries carry an approver-routing target and an
  optional exclusivity flag; gate-policy entries carry per-artifact-type
  committee composition and a timeout-to-default default rule
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
  [DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md),
  [DEC-0046](../decisions/DEC-0046-person-registry.md)).

### RoleClaims (value)

Implements: [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md),
[ST-0014](../stories/ST-0014-gate-policy-check.md)

- `RoleClaims.D-1` — schema: `person_id`, `governance_ref`, `at`
  (timestamp evaluated against), `roles[]` — each entry `{role,
  source}` where `source` is `direct` or `delegation{delegator,
  window_start, window_end}`
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
  [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).

### RoleResolution (service)

Implements: [ST-0014](../stories/ST-0014-gate-policy-check.md),
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)

- `RoleResolution.A-1` — `resolve(governance_ref, person_id, at) →
  RoleClaims`; typed error: `unknown-person` (person-id absent from
  `people.yaml` at that ref)
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
  [DEC-0046](../decisions/DEC-0046-person-registry.md),
  [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).
- `RoleResolution.A-2` — `holders(governance_ref, role, at) →
  person_id[]` — direct members plus delegates with an active window
  at `at`; typed error: `unknown-role`
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
  [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).
- `RoleResolution.B-1` — delegation semantics: a delegate holds
  exactly the delegated role's claims while the window is active —
  active at `t` iff `window_start ≤ t < window_end` (UTC); outside the
  window the delegation contributes nothing
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md)).
- `RoleResolution.B-2` — evaluation is pure and live: computed from
  `GovernanceConfig` at the given ref on every call, no cached
  compilation; identical inputs yield identical claims
  (per [DEC-0164](../decisions/DEC-0164-gate-policy-check-live-evaluation.md),
  [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).

## Component Invariants

- `C-1` — this component never writes governance files; changes arrive
  through the PR-gated governance flow — whose single decided exception
  is the one-time seeded bootstrap commit, written by
  [CMP-0004](CMP-0004-governance-gate-engine.md)'s `GovernanceInit`
  before gating exists, never by this component
  (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
  [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).
- `C-2` — every role-membership or delegation judgement anywhere in
  the system is produced by `RoleResolution` — no consumer re-implements
  window evaluation
  (per [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).

## Implementation Guidance

### Constraints

- `IG-1` — parsing validates against `SchemaValidator.D-2` assets
  before constructing the value; a non-conformant file is a parse
  failure, never a best-effort value
  (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

### Notes

- Callers that evaluate many people at one ref (committee quorum,
  team sync) should hold one `GovernanceConfig` value and call
  resolution repeatedly against it; the purity guarantee makes this
  safe.

## Dependencies

- [CMP-0001](CMP-0001-artifact-store-service.md) — consumed sections:
  `StorageService.A-1` (reading `governance/` files at a ref),
  `SchemaValidator.D-2` (the governance file schema assets this value
  parses against).

## Acceptance & Test Expectations

1. Parse conformance: each of the five files round-trips through
   `GovernanceConfig` against the `SchemaValidator.D-2` fixtures;
   non-conformant files fail
   (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
2. Delegation windows: boundary tests at `window_start` and
   `window_end` (inclusive/exclusive), plus overlapping and expired
   delegations (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md)).
3. Parity: [CMP-0004](CMP-0004-governance-gate-engine.md)'s gate
   fixtures and [CMP-0007](CMP-0007-identity-and-access.md)'s claims
   fixtures resolve through this service with identical results
   (per [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md)).
4. Ref-pinning: resolving the same person at two refs with differing
   `roles.yaml` yields each ref's answer, no leakage between them
   (per [DEC-0164](../decisions/DEC-0164-gate-policy-check-live-evaluation.md)).

## Out of Scope

- Gate-policy *verdicts* (quorum arithmetic, staleness, attribution
  verification) — [CMP-0004](CMP-0004-governance-gate-engine.md)'s
  `GatePolicyCheck`; this component answers only membership/claims
  questions.
- The governance file schemas and their validation library —
  [CMP-0001](CMP-0001-artifact-store-service.md) (`SchemaValidator`).
- Editing governance files (Admin UI, PR flow) —
  [EP-0006](../epics/EP-0006-refinement-web-ui.md) and the gate flow.
- Person-id ↔ auth-subject/host-identity resolution —
  [CMP-0007](CMP-0007-identity-and-access.md); this component treats
  person-ids as opaque keys from `people.yaml`.
