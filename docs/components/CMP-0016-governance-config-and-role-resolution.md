---
id: CMP-0016
type: component
title: Governance Config & Role Resolution
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Graduated from CMP-0004 per DEC-0234 for shared consumption by gate
  evaluation and identity claims. Typed in-memory value of five governance/
  files at a git ref: roles.yaml, domains.yaml, gate-policies.yaml,
  repos.yaml, people.yaml. Role-membership evaluation including active
  time-bounded delegation windows. Three elements: GovernanceConfig (parsed
  value, never persisted independently of git), RoleClaims (person-id,
  governance-ref, evaluated-at, roles with direct/delegation sources),
  RoleResolution (pure live evaluation service answering membership and
  claims questions). Evaluation identical on identical inputs; consumed by
  both CMP-0004 (gate verdicts) and CMP-0007 (person claims).
context: governance
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [CMP-0001]
cites: [DEC-0020, DEC-0034, DEC-0037, DEC-0040, DEC-0046, DEC-0140, DEC-0164,
        DEC-0234]
---

# CMP-0016: Governance Config & Role Resolution

> Graduated out of CMP-0004 per
> DEC-0234:
> the parsed governance-config value plus the single shared
> implementation of role-membership and delegation-window evaluation,
> consumed by both CMP-0004
> (gate verdicts) and CMP-0007
> (person resolution and role claims). The `governance/` file schemas
> themselves remain CMP-0001's
> (`SchemaValidator.D-2`).

## Purpose

One answer to "who holds which role right now": the typed in-memory
value of the five `governance/` files at a git ref, and the resolution
service that evaluates role membership — including active time-bounded
delegation — at an explicit ref and point in time
(per DEC-0037,
DEC-0040).

## Ubiquitous Language

Governance-as-Code, Gate Policy, Approver, Role Claims — per
[CONTEXT.md](../../CONTEXT.md).

## Design Elements

### GovernanceConfig (value)

Implements: ST-0012

- `GovernanceConfig.D-1` — the parsed, typed representation of the five
  `governance/` files (`roles.yaml`, `domains.yaml`,
  `gate-policies.yaml`, `repos.yaml`, `people.yaml`) at a resolving git
  ref; schema shape is exactly
  CMP-0001's published
  `SchemaValidator.D-2` assets — this element defines no schema of its
  own, only the in-memory value its consumers read. Equality by value
  at a given ref; never persisted independently of git
  (per DEC-0037,
  DEC-0034).
- `GovernanceConfig.D-2` — role membership entries carry stable
  person-ids from `people.yaml` and optional time-bounded delegation
  windows; domain entries carry an approver-routing target and an
  optional exclusivity flag; gate-policy entries carry per-artifact-type
  committee composition and a timeout-to-default default rule
  (per DEC-0040,
  DEC-0020,
  DEC-0046).

### RoleClaims (value)

Implements: ST-0022,
ST-0014

- `RoleClaims.D-1` — schema: `person_id`, `governance_ref`, `at`
  (timestamp evaluated against), `roles[]` — each entry `{role,
  source}` where `source` is `direct` or `delegation{delegator,
  window_start, window_end}`
  (per DEC-0040,
  DEC-0234).

### RoleResolution (service)

Implements: ST-0014,
ST-0022

- `RoleResolution.A-1` — `resolve(governance_ref, person_id, at) →
  RoleClaims`; typed error: `unknown-person` (person-id absent from
  `people.yaml` at that ref)
  (per DEC-0040,
  DEC-0046,
  DEC-0234).
- `RoleResolution.A-2` — `holders(governance_ref, role, at) →
  person_id[]` — direct members plus delegates with an active window
  at `at`; typed error: `unknown-role`
  (per DEC-0040,
  DEC-0234).
- `RoleResolution.B-1` — delegation semantics: a delegate holds
  exactly the delegated role's claims while the window is active —
  active at `t` iff `window_start ≤ t < window_end` (UTC); outside the
  window the delegation contributes nothing
  (per DEC-0040).
- `RoleResolution.B-2` — evaluation is pure and live: computed from
  `GovernanceConfig` at the given ref on every call, no cached
  compilation; identical inputs yield identical claims
  (per DEC-0164,
  DEC-0234).

## Component Invariants

- `C-1` — this component never writes governance files; changes arrive
  through the PR-gated governance flow — whose single decided exception
  is the one-time seeded bootstrap commit, written by
  CMP-0004's `GovernanceInit`
  before gating exists, never by this component
  (per DEC-0037,
  DEC-0140).
- `C-2` — every role-membership or delegation judgement anywhere in
  the system is produced by `RoleResolution` — no consumer re-implements
  window evaluation
  (per DEC-0234).

## Implementation Guidance

### Constraints

- `IG-1` — parsing validates against `SchemaValidator.D-2` assets
  before constructing the value; a non-conformant file is a parse
  failure, never a best-effort value
  (per DEC-0034).

### Notes

- Callers that evaluate many people at one ref (committee quorum,
  team sync) should hold one `GovernanceConfig` value and call
  resolution repeatedly against it; the purity guarantee makes this
  safe.

## Dependencies

- CMP-0001 — consumed sections:
  `StorageService.A-1` (reading `governance/` files at a ref),
  `SchemaValidator.D-2` (the governance file schema assets this value
  parses against).

## Acceptance & Test Expectations

1. Parse conformance: each of the five files round-trips through
   `GovernanceConfig` against the `SchemaValidator.D-2` fixtures;
   non-conformant files fail
   (per DEC-0034).
2. Delegation windows: boundary tests at `window_start` and
   `window_end` (inclusive/exclusive), plus overlapping and expired
   delegations (per DEC-0040).
3. Parity: CMP-0004's gate
   fixtures and CMP-0007's claims
   fixtures resolve through this service with identical results
   (per DEC-0234).
4. Ref-pinning: resolving the same person at two refs with differing
   `roles.yaml` yields each ref's answer, no leakage between them
   (per DEC-0164).

## Out of Scope

- Gate-policy *verdicts* (quorum arithmetic, staleness, attribution
  verification) — CMP-0004's
  `GatePolicyCheck`; this component answers only membership/claims
  questions.
- The governance file schemas and their validation library —
  CMP-0001 (`SchemaValidator`).
- Editing governance files (Admin UI, PR flow) —
  EP-0006 and the gate flow.
- Person-id ↔ auth-subject/host-identity resolution —
  CMP-0007; this component treats
  person-ids as opaque keys from `people.yaml`.
