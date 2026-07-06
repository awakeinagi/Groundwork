---
id: DEC-0066
type: decision
title: Consolidation regeneration is debounced, with on-demand rebuild at request time
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T2-T3"
links:
  derives-from: [SES-0008]
---

# DEC-0066: Debounced + on-demand regeneration

## Context

An item under active refinement invalidates its consolidations on every
commit — regenerating each time is pure waste while the item churns, but
staleness must never be served ([DEC-0017](DEC-0017-consolidation-memory-layer.md)).

## Decision

Staleness remains instant and absolute: a stale consolidation is never
served. Regeneration is debounced — rebuild fires after a quiet window with
no further source changes, or a max-wait cap, whichever comes first. If a
request arrives for a consolidation that is currently stale, regeneration
runs on-demand for that request.

## Rationale

Hot items never thrash the generator; requesters never receive stale
content and never wait for a schedule. The freshness guarantee is
preserved by serving rules, not regeneration speed.

## Alternatives Considered

- **Regenerate on every change**: one rebuild per confirmed decision
  during active sessions — waste.
- **Scheduled batch only**: freshest context unavailable exactly when
  adjacent sessions want it.

## Implications

Quiet-window and max-wait values are deployment configuration; on-demand
regeneration latency becomes part of the recipe resolver's
([DEC-0068](DEC-0068-recipe-resolver.md)) budget accounting.
