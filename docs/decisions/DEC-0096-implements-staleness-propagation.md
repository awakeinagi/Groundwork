---
id: DEC-0096
type: decision
title: Story changes propagate staleness to referencing Component Docs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0015 @ T4-T5"
links:
  derives-from: [SES-0015]
  relates-to: [DEC-0092, DEC-0007, DEC-0038]
---

# DEC-0096: Story changes propagate staleness to referencing Component Docs

## Context

Staleness walks `derives-from`/`satisfies`
([DEC-0007](DEC-0007-impact-analysis-stale-marks.md)), and Component
Docs typically derive from epics — so a story amendment would often
never reach the CMP whose elements realize it. A superseded story could
leave elements claiming coverage of requirements that no longer exist,
and the completion metrics
([DEC-0095](DEC-0095-percent-complete-metrics.md)) would silently
report on a stale basis.

## Decision

The element→story Implements edge
([DEC-0092](DEC-0092-element-implements-line.md)) participates in
staleness propagation, one direction only: when an approved story is
amended or superseded, every Component Doc containing an element that
references it is marked `stale`, and the impact report names the
specific referencing elements so re-affirmation is scoped to them.
Component Doc and element edits never stale stories.

## Rationale

This is what keeps "story X is 100% designed" honest after change. The
cost — story churn triggers CMP re-affirmations — is the cheap path by
design: re-affirmation, not re-refinement, per
[DEC-0038](DEC-0038-subtree-staleness-reaffirmation.md). Element-scoped
impact reporting keeps it from becoming whole-document panic.

## Alternatives Considered

- **Informational-only edge**: no staleness, metrics rot silently after
  story changes — rejected.
- **Bidirectional propagation**: element edits staling stories would
  invert provenance (references point upward, like `cites`) and create
  churn loops — rejected.

## Implications

Impact analysis ([EP-0004](../epics/EP-0004-graph-index.md) walks, the
skill's `impact` command, and the storage service's stale-marking
mechanical writes per
[DEC-0033](DEC-0033-typed-mechanical-writes.md)) must traverse
IMPLEMENTS edges story→CMP; impact reports gain element scoping.
