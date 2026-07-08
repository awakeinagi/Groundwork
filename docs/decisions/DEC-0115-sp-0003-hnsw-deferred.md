---
id: DEC-0115
type: decision
title: SP-0003 captures HNSW adoption as a deferred spike subscribed to TRG-0003
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T4"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0104, DEC-0105, DEC-0109, DEC-0114]
---

# DEC-0115: `SP-0003` — HNSW Adoption as a Deferred Spike under `TRG-0003`

## Context

[DEC-0114](DEC-0114-no-persisted-hnsw.md) rejects an HNSW index at
current corpus scale. The question isn't dead — at some scale
approximate indexing wins — so the participant directed capturing it as
a deferred spike rather than losing it.

## Decision

[SP-0003](../spikes/SP-0003-hnsw-index-adoption.md) is created
`deferred` with `release: backlog` (deferred spikes per
[DEC-0104](DEC-0104-deferred-extends-to-spikes.md); this decision is
the deferral citation per
[DEC-0100](DEC-0100-scope-moves-cite-decisions.md)). It **subscribes to
the existing armed trigger `TRG-0003`** — embedded engine performance
degrading at real corpus or query scale, explicitly including vector
search latency — rather than arming a new trigger (reuse over
duplication, per [DEC-0109](DEC-0109-trigger-subscriptions.md)).

## Rationale

`TRG-0003`'s condition is verbatim the situation in which HNSW becomes
worth its risks; a second trigger with the same condition would violate
the registry's reuse rule. When it fires, both subscribers revive
together — [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)
evaluates graduating *off* embedded storage while
[SP-0003](../spikes/SP-0003-hnsw-index-adoption.md) evaluates making
embedded search faster *in place*; they are competing answers to the
same firing and should be studied together.

## Alternatives Considered

- **No spike — revisit ad hoc when slow**: loses the POC evidence and
  the persistence-risk analysis that should frame the future evaluation.
- **A new dedicated trigger**: duplicates `TRG-0003`'s condition;
  forbidden by the reuse discipline of
  [DEC-0109](DEC-0109-trigger-subscriptions.md).

## Implications

`TRG-0003` in [TRIGGERS.md](../TRIGGERS.md) gains a second subscriber
line citing this decision. A future firing revives
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) and
[SP-0003](../spikes/SP-0003-hnsw-index-adoption.md) together under one
firing decision.
