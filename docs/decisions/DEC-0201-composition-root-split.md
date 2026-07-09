---
id: DEC-0201
type: decision
title: The Backend Application Platform epic owns the Composition Root; engine epics keep owning Port contracts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  EP-0008 owns the Composition Root: the single place where Port
  contracts are bound to concrete Adapters at process startup from
  deployment configuration. EP-0001/EP-0004/EP-0007 continue to own
  what each Port contractually guarantees. Keeps each engine's contract
  stable regardless of Adapter selection, and gives EP-0008 a clean,
  narrow scope (wiring, not re-specifying). Constrains EP-0008's scope
  and depends-on relationships. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0038 @ T1"
links:
  derives-from: [SES-0038]
  relates-to: [DEC-0121]
  supersedes: []
---

# DEC-0201: The Backend Application Platform Epic Owns the Composition Root; Engine Epics Keep Owning Port Contracts

## Context

EP-0008 (Backend
Application Platform) needed a boundary against
EP-0001,
EP-0004, and
EP-0007, which already
own the four infrastructure Port contracts
(DEC-0121).

## Decision

EP-0008 owns the
**Composition Root**: the single place where Port contracts are bound to
concrete Adapters at process startup, from deployment configuration.
EP-0001/EP-0004/EP-0007
continue to own what each Port contractually guarantees;
EP-0008 only wires
them, and never redefines a Port's contract.

## Rationale

Keeps each engine's contract stable regardless of which Adapter is
selected at deployment time, and gives the new epic a clean, narrow
scope (wiring, not re-specifying) consistent with the Protocol Seam's
"separate the engine from what consumes/assembles it" framing.

## Alternatives Considered

- **EP-0008 owns the
  Port contracts too**: rejected — would move
  DEC-0121's scope into this epic,
  re-scoping/staling
  EP-0001/EP-0004/EP-0007
  for no functional benefit.
- **Defer composition-root ownership to story level**: rejected — the
  epic-level boundary needs to be settled before stories can be sliced
  against it (per `story-slicing-seams.md`'s Data/Operations seams,
  which assume a settled parent contract).

## Implications

EP-0008's Scope and
Domain Context reflect this split; its `depends-on` is scoped to
EP-0001 only
(the app-database Port contract it wires first), not the full set of
composed engines.
