---
id: DEC-0023
type: decision
title: Spike findings are recorded as Decision records
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T12-T13"
links:
  derives-from: [SES-0001]
---

# DEC-0023: Spike findings become Decision records

## Context

Spike (research) outcomes often invalidate assumptions baked into sibling
stories and component contracts. The findings needed a home that triggers the
right downstream reaction.

## Decision

Spike findings are written up as Decision records — same DEC format, with
`derives-from` pointing at the spike instead of a session — and linked into
the graph. Every completed spike produces at least one Decision, even
"assumption confirmed, no change."

## Rationale

One mechanism, not two: the existing impact-analysis machinery
(DEC-0007) then marks affected
stories and contracts stale automatically, and spike knowledge becomes
citable provenance like any other decision.

## Alternatives Considered

- **Fold findings into the parent epic doc**: less ceremony, weaker
  provenance, no automatic impact propagation.
- **Manual follow-up**: humans decide what to update; misses the tail.

## Implications

[SPEC-spike](../specs/SPEC-spike.md) makes the produced-Decision a completion
requirement; [SPEC-decision](../specs/SPEC-decision.md) admits spikes as a
source.
