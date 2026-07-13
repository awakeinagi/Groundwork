---
id: DEC-0467
type: decision
title: "Export/Packaging stays underived; trigger is the first third-party consumer"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  Export/packaging is a DEC-0443 roster topic with no third-party
  consumer currently existing. SES-0089's derivation leaves it
  undeveloped as an epic: it remains an anticipated roster topic
  whose derivation trigger is the first concrete third-party
  consumer materializing, mirroring DEC-0423's library-extraction
  trigger principle. Deriving a deferred, spike-gated epic now would
  add a stale-checkable artifact and gate debt for a consumer,
  scope, and session that do not yet exist; folding it into Adoption
  was also rejected since the adopter persona bootstrapping their
  own project differs from a third-party recipient consuming a
  package. Nothing is kept stale-checked under this posture.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0443, DEC-0423, DEC-0462]
---

# DEC-0467: Export/Packaging stays underived; trigger is the first third-party consumer

## Context

Export/packaging is a DEC-0443 roster topic with no third-party
consumer currently existing.

## Decision

Export/Packaging is not derived as an epic. It remains an anticipated
roster topic whose derivation trigger is the first concrete
third-party consumer materializing; the trigger firing starts a normal
derivation session.

## Rationale

DEC-0443's mechanism has epics derive only through their own refinement
session; creating a deferred epic artifact now would add a
stale-checkable artifact and gate debt for a consumer, scope, and
session that do not exist. This mirrors DEC-0423's library-extraction
trigger principle.

## Alternatives Considered

Deriving a deferred, spike-gated epic now (process debt); folding
export into Adoption (the adopter persona bootstrapping their own
project differs from the third-party recipient consuming a package).

## Implications

Nothing is kept stale-checked; the roster works as designed.
