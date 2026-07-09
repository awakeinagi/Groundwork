---
id: SP-0007
type: spike
title: Contract-item-level graph nodes with per-item decision citations
status: draft
owner: eng-lead
created: 2026-07-08
overview: >-
  Question: do contract-item nodes pay their way? Can element contract
  items (Element.B|A|D|C|IG-n with per-item decision citations) be parsed
  reliably enough to add item→decision CITES edges to the graph index,
  making impact sweeps and DEC-0157 review item-precise, without parse
  fragility, index bloat, or markdown-convention rigidity costing more
  than the precision gained? Blocks no current work; element-level
  granularity plus DEC-0157/DEC-0158 tooling is the operating state, but
  the answer shapes EP-0004's Graph Index contracts (IMPLEMENTS edges and
  rollups already ride element granularity). Method prototypes in skill
  graph tool, extends parser for item IDs and per-item citations, counts
  parse failures, re-runs SES-0026 queries at item granularity, measures
  index growth. Draft status.
timebox: 3d
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  relates-to: [EP-0004, SP-0006]
cites: [DEC-0157, DEC-0158, DEC-0160]
---

# SP-0007: Contract-Item Graph Nodes

> Opened by DEC-0160.
> In the SES-0026
> incident, graph queries could only say "somewhere in
> CMP-0001" — the
> affected allowlist item (`MechanicalWriteService.A-1..A-8`) is opaque
> prose to the index.

## Question

Do contract-item nodes pay their way? Concretely: can element contract
items (`<Element>.<B|A|D|C|IG>-<n>` with their per-item `(per DEC-…)`
citations) be parsed from Component Docs reliably enough to add
item→decision `CITES` edges to the graph index — making impact sweeps
and the DEC-0157
review item-precise — without the parse fragility, index bloat, or
markdown-convention rigidity costing more than the precision is worth?

## Why It Blocks

Nothing today — element-level granularity plus the
DEC-0157/DEC-0158
tooling is the operating state. The answer is design input to
EP-0004's Graph Index contracts
(IMPLEMENTS edges and rollups already ride element granularity;
item nodes would extend that schema), so it should land before
EP-0004's stories harden the index
schema.

## Method

Prototype in the skill's graph tool against this corpus (the real
bootstrap corpus): extend the element parser to item IDs and per-item
citations across the four existing CMPs; count parse failures against
hand-verified ground truth; re-run the
SES-0026 incident
queries at item granularity; measure index growth and rebuild time.
Report precision gained vs. convention rigidity imposed (does every
future CMP author now owe the parser a grammar?). Findings become
decisions and EP-0004 design input.

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — a completed spike produces at least one decision, even
"assumption confirmed, no change."
