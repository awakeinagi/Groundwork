---
id: DEC-0105
type: decision
title: SP-0002 is re-scoped to the Postgres + pgvector graduation evaluation and deferred
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T3, T6-T7"
links:
  derives-from: [SES-0017]
  relates-to: [DEC-0102, DEC-0104, DEC-0106]
---

# DEC-0105: `SP-0002` Re-scoped to the Graduation Evaluation and Deferred

## Context

With the v1 stack decided (DEC-0102),
SP-0002's original
question — which engine backs the Graph Index — is answered. The open
question that remains is *when and how to graduate* off the embedded
stack.

## Decision

SP-0002 is amended
rather than archived: its question becomes **"when and how should
Groundwork graduate from embedded LadybugDB/DuckDB to Postgres +
pgvector (or equivalent server-grade infrastructure)?"**, its method is
rewritten for that question, and it is set `deferred` with
`release: backlog` (per DEC-0104).
Revival is governed by the armed triggers `TRG-0001`–`TRG-0004` in the
registry ([TRIGGERS.md](../TRIGGERS.md), per
DEC-0106): multi-node/HA required; more
than one concurrent writer process; embedded performance degrading at
scale; an enterprise deployment mandating external managed databases.
This decision is the deferral citation required by
DEC-0100.

## Rationale

Re-scoping preserves the spike's accumulated context — the query
contract, overlay semantics, and criteria it already names — which is
exactly the frame the graduation evaluation needs. The participant chose
continuity over archive-and-recreate.

## Alternatives Considered

- **Archive the spike; derive a fresh one when a trigger fires**
  (facilitator's recommendation): cleaner WIP hygiene, but discards the
  spike's context and history; the participant upgraded it by extending
  deferral to spikes instead.
- **Execute the original spike anyway**: spends a timebox answering a
  question v1 no longer asks.

## Implications

The spike's file is renamed to match its new title (ID immutable, slug
not); inbound links are mechanically updated. It leaves the active
pipeline and the WIP lists, surfacing instead via the Deferred section
and its armed triggers.
