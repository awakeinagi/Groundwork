---
id: DEC-0128
type: decision
title: ChangeEvent carries a closed change-kind enum and a schema-version field
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T3-T4"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0059, DEC-0060, DEC-0103]
---

# DEC-0128: ChangeEvent Closed Kind Enum and Schema Versioning

## Context

ST-0008 fixed the event
stream's delivery semantics but not the payload vocabulary or its
evolution story.

## Decision

The `ChangeEvent` payload comprises: `event_id`, `schema_version`,
`artifact_id`, `artifact_type`, `branch`, `commit` (sha), `kind`,
`changed_fields[]`, `occurred_at`. `kind` is a **closed enum**:
`created | content-amended | status-changed | merged | deleted`.
Extending the enum or changing the payload is a contract change through
a gate — the same discipline as the mechanical-write allowlist
(DEC-0033); `schema_version`
lets consumers handle evolution explicitly.

## Rationale

Consumers can exhaustively match a closed enum; a typo'd kind cannot
ship silently. The closed-set discipline already governs link types,
element types, and mechanical operations — events follow suit.

## Alternatives Considered

- **Open-ended kind string** — cheaper to extend, but unmatchable
  exhaustively and silently extensible.
