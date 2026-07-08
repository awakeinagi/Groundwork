---
id: DEC-0201
type: decision
title: The Backend Application Platform epic owns the Composition Root; engine epics keep owning Port contracts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
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

[EP-0008](../epics/EP-0008-backend-application-platform.md) (Backend
Application Platform) needed a boundary against
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md),
[EP-0004](../epics/EP-0004-graph-index.md), and
[EP-0007](../epics/EP-0007-consolidation-memory-layer.md), which already
own the four infrastructure Port contracts
([DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).

## Decision

[EP-0008](../epics/EP-0008-backend-application-platform.md) owns the
**Composition Root**: the single place where Port contracts are bound to
concrete Adapters at process startup, from deployment configuration.
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
continue to own what each Port contractually guarantees;
[EP-0008](../epics/EP-0008-backend-application-platform.md) only wires
them, and never redefines a Port's contract.

## Rationale

Keeps each engine's contract stable regardless of which Adapter is
selected at deployment time, and gives the new epic a clean, narrow
scope (wiring, not re-specifying) consistent with the Protocol Seam's
"separate the engine from what consumes/assembles it" framing.

## Alternatives Considered

- **[EP-0008](../epics/EP-0008-backend-application-platform.md) owns the
  Port contracts too**: rejected — would move
  [DEC-0121](DEC-0121-infrastructure-ports.md)'s scope into this epic,
  re-scoping/staling
  [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
  for no functional benefit.
- **Defer composition-root ownership to story level**: rejected — the
  epic-level boundary needs to be settled before stories can be sliced
  against it (per `story-slicing-seams.md`'s Data/Operations seams,
  which assume a settled parent contract).

## Implications

[EP-0008](../epics/EP-0008-backend-application-platform.md)'s Scope and
Domain Context reflect this split; its `depends-on` is scoped to
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) only
(the app-database Port contract it wires first), not the full set of
composed engines.
