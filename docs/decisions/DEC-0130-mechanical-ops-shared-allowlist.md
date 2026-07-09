---
id: DEC-0130
type: decision
title: Mechanical operations are typed API items sharing one allowlist asset with the mechanical-diff validator
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T3-T4"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0033, DEC-0034]
---

# DEC-0130: Mechanical Operations as A-Items with a Shared Allowlist Asset

## Context

The closed mechanical operation set
(DEC-0033) needed a contract
modeling: value elements per operation, or API items on the service.

## Decision

Each mechanical operation (`append-turn`, `close-session`,
`mark-stale`, `clear-stale`, `set-jira-key`, `set-jira-status`,
`create-change-proposal`, `set-cp-triage`) is its own
`MechanicalWriteService` API item with typed parameters and its exact
allowed diff shape. The **allowlist** — the operation → permitted
fields/append-regions map — is a single published data-contract asset
consumed by both the write path and the mechanical-diff validator in
the check suite: one source of truth, two consumers.

## Rationale

Eight value-element headings would be ceremony for schemas only one
service consumes; the shared allowlist asset is the piece that must not
fork, since the validator exists to verify exactly what the write path
promises.

## Alternatives Considered

- **A value element per operation** — maximum schema reuse if
  operations ever ride the event stream; deferred until that need
  exists.
