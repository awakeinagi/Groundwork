---
id: DEC-0100
type: decision
title: Deferral and revival each cite a Decision
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0016 @ T4-T5"
links:
  derives-from: [SES-0016]
  relates-to: [DEC-0097, DEC-0015]
---

# DEC-0100: Deferral and Revival Each Cite a Decision

## Context

Deferring a story ([DEC-0097](DEC-0097-deferred-status.md)) and bringing
it back both change what a release contains. Is that provenance-worthy,
or a mechanical status flip?

## Decision

Both transitions cite a Decision record: deferring adds the deferral
decision to the artifact's `cites`, and revival adds the reviving
decision. One decision may cover several items scoped in the same
breath. The citation answers "why isn't/wasn't this in the release?"
from the artifact itself, indefinitely.

## Rationale

Scoping something out of a release is a genuine trade-off — exactly the
bar this system sets for Decision records
([DEC-0015](DEC-0015-transcript-decision-citation-chain.md)). In-session
capture stays cheap because one deferral decision can park a batch.

## Alternatives Considered

- **Defer freely, cite only on revival**: rejected — a year later, "why
  was this parked?" would be git archaeology, the failure mode
  Groundwork exists to eliminate.
- **Neither — mechanical writes only**: rejected — scope changes are
  design decisions by any definition this system uses; leaving them
  uncited undermines the provenance guarantee everywhere else.

## Implications

[SPEC-story](../specs/SPEC-story.md) and
[SPEC-epic](../specs/SPEC-epic.md) rules gain the requirement. The
checker can only enforce "deferred implies at least one citation"
heuristically (it can't know which citation is the deferral), so the
normative rule is spec-level, human-checked at gates.
