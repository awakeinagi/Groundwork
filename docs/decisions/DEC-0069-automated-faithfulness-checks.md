---
id: DEC-0069
type: decision
title: Consolidations serve without human gates, guarded by automated faithfulness checks
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T4-T5"
links:
  derives-from: [SES-0008]
---

# DEC-0069: Automated faithfulness checks instead of human gates

## Context

Consolidations are agent-generated and a bad summary silently biases every
consuming session — but they are also derived, rebuildable, non-citable
([SPEC-consolidation](../specs/SPEC-consolidation.md)) and regenerate too
often for human review to be meaningful.

## Decision

No human gate. Every generation passes an automated faithfulness check —
no-new-claims verification against sources (the
[DEC-0058](DEC-0058-evaluation-harness.md) harness pattern) — before the
consolidation may serve; failures block serving and alert. Samples get
periodic independent-judge review, and every served element carries source
refs so any consumer can drop to ground truth.

## Rationale

Human gates ratify decisions; consolidations contain none. Machine
verification matched to a mechanical guarantee (faithfulness to sources)
is the same trade [DEC-0033](DEC-0033-typed-mechanical-writes.md) made for
mechanical writes.

## Alternatives Considered

- **Gate catalog entries only**: regeneration review becomes approval spam.
- **Full PR gating**: unworkable at hot-item regeneration frequency.

## Implications

The faithfulness checker is a retrieval-layer component with its own eval
coverage; blocked-consolidation alerts flow to the ops surface
([DEC-0042](DEC-0042-governance-reporting-split.md)).
