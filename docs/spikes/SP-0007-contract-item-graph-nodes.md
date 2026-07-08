---
id: SP-0007
type: spike
title: Contract-item-level graph nodes with per-item decision citations
status: draft
owner: eng-lead
created: 2026-07-08
timebox: 3d
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  relates-to: [EP-0004, SP-0006]
cites: [DEC-0158, DEC-0160]
---

# SP-0007: Contract-Item Graph Nodes

> Opened by [DEC-0160](../decisions/DEC-0160-sp-0007-item-nodes-spike.md).
> In the [SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md)
> incident, graph queries could only say "somewhere in
> [CMP-0001](../components/CMP-0001-artifact-store-service.md)" — the
> affected allowlist item (`MechanicalWriteService.A-1..A-8`) is opaque
> prose to the index.

## Question

Do contract-item nodes pay their way? Concretely: can element contract
items (`<Element>.<B|A|D|C|IG>-<n>` with their per-item `(per DEC-…)`
citations) be parsed from Component Docs reliably enough to add
item→decision `CITES` edges to the graph index — making impact sweeps
and the [DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)
review item-precise — without the parse fragility, index bloat, or
markdown-convention rigidity costing more than the precision is worth?

## Why It Blocks

Nothing today — element-level granularity plus the
[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)/[DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md)
tooling is the operating state. The answer is design input to
[EP-0004](../epics/EP-0004-graph-index.md)'s Graph Index contracts
(IMPLEMENTS edges and rollups already ride element granularity;
item nodes would extend that schema), so it should land before
[EP-0004](../epics/EP-0004-graph-index.md)'s stories harden the index
schema.

## Method

Prototype in the skill's graph tool against this corpus (the real
bootstrap corpus): extend the element parser to item IDs and per-item
citations across the four existing CMPs; count parse failures against
hand-verified ground truth; re-run the
[SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md) incident
queries at item granularity; measure index growth and rebuild time.
Report precision gained vs. convention rigidity imposed (does every
future CMP author now owe the parser a grammar?). Findings become
decisions and [EP-0004](../epics/EP-0004-graph-index.md) design input.

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — a completed spike produces at least one decision, even
"assumption confirmed, no change."
