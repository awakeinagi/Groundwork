---
id: CMP-0002
type: component
title: ChangeEvent Contract
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Standalone event-type component, graduated from CMP-0001 per DEC-0134
  because multiple consumers depend on it. Defines the payload schema
  and delivery contract for artifact-change events emitted by CMP-0001's
  outbox. Specifies event_id, artifact_id, artifact_type, branch, commit,
  kind (created, content-amended, status-changed, merged, deleted),
  changed_fields, and timestamp. Delivery: at-least-once, per-artifact
  ordering only. Consumers idempotent by contract.
context: canonical-store
component-type: event
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0018, DEC-0059, DEC-0060, DEC-0080, DEC-0103, DEC-0128, DEC-0131,
        DEC-0133, DEC-0134]
---

# CMP-0002: ChangeEvent Contract

> Standalone `event`-type component, graduated out of
> CMP-0001 per
> DEC-0134 under the
> DEC-0080
> rule: multiple consuming components.

## Purpose

The cross-component seam every derived system rides: the schema and
delivery semantics of the artifact-changed event emitted for each
canonical write. Producers (CMP-0001)
and consumers (Graph Index, governance sweeps, consolidation freshness)
depend on this contract, not on each other.

## Ubiquitous Language

Canonical Store, Artifact, Item Branch — per
[CONTEXT.md](../../CONTEXT.md). No new terms introduced.

## Design Elements

### ChangeEvent (event)

Implements: ST-0008

- `ChangeEvent.D-1` — payload schema: `event_id` (uuid),
  `schema_version` (int), `artifact_id` (artifact-ID string per
  [SPEC-artifact-common](../specs/SPEC-artifact-common.md)),
  `artifact_type`, `branch`, `commit` (sha), `kind` (closed enum:
  `created | content-amended | status-changed | merged | deleted`),
  `changed_fields[]`, `occurred_at` (timestamp). Extending the enum or
  changing the payload is a gated contract change (per DEC-0128,
  DEC-0059).
- `ChangeEvent.B-1` — emission: every write landing in the repository —
  content, mechanical, merge — emits exactly one event, produced via
  the emitter's transactional outbox (per DEC-0059, DEC-0103).
- `ChangeEvent.B-2` — delivery: at-least-once with per-artifact
  ordering; consumers are idempotent by contract; no cross-artifact
  ordering or exactly-once guarantee exists (per DEC-0060).
- `ChangeEvent.B-3` — merge events carry what the Graph Index needs to
  promote overlay state to the main view and drop the overlay
  (per DEC-0059).
- `ChangeEvent.B-4` — replayability: the stream is derivable from git
  history for any ref range; a consumer rebuilt from scratch converges
  to the state of one that consumed live. Delivery plumbing is never
  truth (per DEC-0060, DEC-0103, DEC-0131).

## Component Invariants

- `C-1` — schema evolution is explicit: no payload change ships without
  a `schema_version` bump and a gated contract change (per DEC-0128).

## Implementation Guidance

### Constraints

- `IG-1` — the published event schema is language-neutral; producer and
  consumer implementations validate against the same asset
  (per DEC-0018).

### Notes

- Consumers should key idempotency on `event_id` and order on
  (`artifact_id`, `commit`) rather than arrival time.

## Dependencies

None — this contract is a leaf; the emitter and consumers depend on it.

## Acceptance & Test Expectations

1. Schema-asset validation: producer output and consumer fixtures
   validate against the published schema (per DEC-0018, DEC-0128).
2. Replay convergence: a consumer rebuilt from git history converges to
   the state of a live consumer over the same ref range (per DEC-0060).

## Out of Scope

Boundary statements (per DEC-0133):

- Emission mechanics — the outbox, dispatcher, and retries belong to
  CMP-0001 and
  CMP-0003.
- Consumer-side processing (Graph Index overlays, staleness sweeps,
  consolidation invalidation — EP-0003/EP-0004/EP-0007).
- User-facing notifications (EP-0006
  — they derive from governance events, not raw store events).
