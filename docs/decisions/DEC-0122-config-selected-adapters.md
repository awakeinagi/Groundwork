---
id: DEC-0122
type: decision
title: Adapters are selected by deployment configuration; every port carries a conformance test suite
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0020 @ T2-T3, T6-T7"
links:
  derives-from: [SES-0020]
  relates-to: [DEC-0121, DEC-0124]
---

# DEC-0122: Config-Selected Adapters with Per-Port Conformance Suites

## Context

"Easily swappable/pluggable" (DEC-0121)
needs an operational definition — clean seams with code-level wiring,
config-time selection, or runtime plugin discovery.

## Decision

Each port's concrete **Adapter** is selected by **deployment
configuration**: swapping an engine or model is a config change plus an
adapter implementation — never a change to consumer code. Every port
ships a **shared conformance test suite** that any adapter (bundled or
future) must pass; passing the suite is the definition of a valid
adapter.

## Rationale

Config selection is the strength the requirement actually needs: the
graduation path (SP-0002)
becomes "write an adapter, pass the suite, flip the config." The
conformance suite is what makes a port real rather than aspirational —
it is the executable form of the port contract, in the same spirit as
the storage API's contract-first conformance testing
(DEC-0018).

## Alternatives Considered

- **Clean seams only (code-level wiring)** — cheaper now; swapping later
  is a PR instead of a config edit. Rejected as under-shooting
  "easily swappable".
- **Runtime plugin discovery (entry-points)** — lets third parties ship
  adapters without touching the codebase; rejected as
  packaging/versioning machinery v1 doesn't need. Nothing in this
  decision forecloses adding it later.
