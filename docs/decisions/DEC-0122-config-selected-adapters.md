---
id: DEC-0122
type: decision
title: Adapters are selected by deployment configuration; every port carries a conformance test suite
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Each port's concrete adapter is selected by deployment configuration,
  enabling adapter swaps via config change without touching consumer code.
  Every port ships a shared conformance test suite that any adapter must
  pass; passing the suite is the definition of a valid adapter. This makes
  graduation paths cheap: write an adapter, pass the suite, flip the config.
  The conformance suite is the executable form of the port contract, making
  it real rather than aspirational.
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

## Implications

The config-selected-adapter and conformance-suite requirement lands on the same three epics as the port decision it operationalizes — EP-0001, EP-0004, and EP-0007 — which the facilitator flagged at SES-0020 T6 as needing amendment and re-affirmation once this decision, among the session's five, took effect. The participant confirmed this at T7. Every adapter, present or future, for the four ports established in this session must pass its port's conformance suite before being considered valid, which is the concrete gate this decision imposes on subsequent adapter work. (skeleton restored at SES-0078)
