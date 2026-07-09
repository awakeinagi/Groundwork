---
id: DEC-0160
type: decision
title: Contract-item-level graph nodes are evaluated by spike SP-0007, not adopted now
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0027 @ T2-T3"
links:
  derives-from: [SES-0027]
  relates-to: [DEC-0158]
---

# DEC-0160: Contract-Item Graph Nodes Spike Opened

## Context

The graph index models design elements but not their contract items —
`MechanicalWriteService.A-1..A-8` is opaque prose to every graph
query, so an impact sweep resolves to "somewhere in
CMP-0001" rather
than the specific allowlist item. Per-item `CITES` edges already exist
in the text (every item cites decisions); the graph just doesn't parse
them.

## Decision

SP-0007 — a timeboxed
spike — prototypes contract-item nodes in the skill's graph tool:
parse element contract items (`<Element>.<K>-<n>`) with their per-item
decision citations, add item→DEC `CITES` edges, and measure whether
item-precise impact/sweep queries pay for the added parse fragility
and graph size. Findings are design input for the product's Graph
Index (EP-0004) as well as the
skill tool.

## Rationale

Item-level precision would have named the exact allowlist item in the
SES-0026 incident;
whether the markdown item conventions are stable enough to parse
reliably is an empirical question — spike-shaped, not decidable from
the armchair.

## Alternatives Considered

- **Model items now in the graph tool**: parse conventions untested;
  a wrong item grammar embedded in tooling calcifies.
- **Skip; element granularity is enough**: the incident argues
  otherwise, but cheaply — hence a spike, not a story.

## Implications

SP-0007 is drafted
deriving from BG-0001
(process-level); findings land as decisions and as
EP-0004 design input.
