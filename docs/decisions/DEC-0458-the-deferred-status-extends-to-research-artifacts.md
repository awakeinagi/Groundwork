---
id: DEC-0458
type: decision
title: "The deferred status extends to Research artifacts"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  A commissioned or in-progress Research artifact may enter
  deferred, an intentional pause during which no research rounds are
  recorded, and is revived to its prior status, mirroring the
  deferred semantics DEC-0104 established for stories, epics, and
  spikes. This extends the status set DEC-0448 defined; abandoned
  remains the terminal state for investigations that end without
  conclusion. Confirmed at the SES-0086 recall-audit review after
  the facilitator flagged it as a genuine open decision.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0104, DEC-0448]
---

# DEC-0458: The deferred status extends to Research artifacts

## Context

DEC-0104 extended the deferred status and release scoping already established for stories to epics and spikes. DEC-0448 defined RSCH's own status set: commissioned, in-progress, concluded, and abandoned, with abandoned as the terminal state for investigations that end without conclusion. The SES-0086 recall-audit review (T16) surfaced whether deferred also applies to RSCH, given RSCH is commissioned and pursued much like a spike or story. The stakeholder (T17) confirmed it should.

## Decision

A commissioned or in-progress Research artifact may enter deferred — an intentional pause during which no research rounds are recorded — and is revived to its prior status, mirroring the deferred semantics DEC-0104 established for stories, epics, and spikes. This extends the status set DEC-0448 defined; abandoned remains the terminal state for investigations that end without conclusion.

## Rationale

Investigations legitimately stall for the same reasons other work does — a dependency isn't ready, priorities shift — without the investigator meaning to abandon the question. Deferred gives RSCH the same honest-parking behavior DEC-0104 already gives stories, epics, and spikes, distinct from abandoned's terminal "this line of inquiry concluded without an answer" meaning.

## Alternatives Considered

Treating a stalled RSCH as abandoned was considered and rejected: abandoned is a terminal, no-revival state meant for investigations that end without conclusion, which would misrepresent a pause that is expected to resume. Leaving RSCH without a deferred option at all (silence rather than a pause) was also considered and rejected as inconsistent with the deferred precedent DEC-0104 already set for comparable exploratory/derived-work types.

## Implications

RSCH's status lifecycle table (DEC-0448) gains deferred as an entry/exit point from commissioned or in-progress, reviving to whichever of those it was in. The checker and status report need to recognize deferred RSCH the same way they already recognize deferred stories, epics, and spikes — excluded from active-work surfaces, included in the "what is to be done?" parked-work accounting.
