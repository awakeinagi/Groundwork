---
id: DEC-0235
type: decision
title: Identity provides the email-to-person-id mapping; CMP-0001's mechanical write executes the migration
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  CMP-0007 exposes a batch email→person-id mapping operation (pure resolver
  over the registry); the migration itself is CMP-0001's migrate-person-ids
  mechanical-write operation, initiated by operator action. Mechanical writes
  stay single-owner; identity stays a pure resolver with no write-orchestration
  responsibility or hidden trigger.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T1-T2"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0046, DEC-0033, DEC-0130]
---

# DEC-0235: Person-Id Migration Split

## Context

ST-0022
AC5: when `governance/people.yaml` is first populated, bootstrap-era
email values in `owner`/`decided-by`/`approved-by` frontmatter migrate
to person-ids via the `migrate-person-ids` operation of the typed
mechanical-write allowlist
(DEC-0033,
DEC-0130). Whose
contract carries what was open.

## Decision

CMP-0007 exposes a
batch email→person-id mapping operation (a pure resolver over the
registry); the migration itself is
CMP-0001's
`migrate-person-ids` mechanical-write operation, initiated by an
operator action.

## Rationale

Mechanical writes stay single-owner (CMP-0001's allowlist); identity
stays a pure resolver with no write-orchestration responsibility or
hidden trigger.

## Alternatives Considered

- **CMP-0007 detects first population and triggers the migration**:
  less operator ceremony, but a hidden write trigger inside identity.
- **Ops runbook only**: leaves an acceptance criterion uncontracted.

## Implications

CMP-0007 carries the resolver item; CMP-0001's existing allowlisted
operation is the executor — no CMP-0001 contract change.
