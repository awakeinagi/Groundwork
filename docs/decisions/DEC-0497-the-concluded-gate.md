---
id: DEC-0497
type: decision
title: "The concluded gate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  The transition to concluded is gated like session close: it
  refuses unless at least one round exists; every round carries
  Findings, Business-Goal Applicability, and Goals Assessment; all
  [Sn] and goal references resolve; and the final round's Goals
  Assessment states the goals met or explicitly re-scoped. Post-hoc
  creation directly at concluded passes the same gate at create. All
  other transitions — commissioned to in-progress, entry to deferred
  or abandoned, and reopening concluded to in-progress — are
  unrestricted.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0448, DEC-0475]
---

# DEC-0497: The concluded gate

## Context

Concluding a Research artifact is a claim that the investigation is
complete and its findings are trustworthy; that claim needs the same
kind of gate a session close already gets, rather than being a free
status flip.

## Decision

The transition to concluded is gated like session close: it refuses
unless at least one round exists; every round carries Findings,
Business-Goal Applicability, and Goals Assessment; all [Sn] and goal
references resolve; and the final round's Goals Assessment states the
goals met or explicitly re-scoped. Post-hoc creation directly at
concluded passes the same gate at create. All other transitions —
commissioned to in-progress, entry to deferred or abandoned, and
reopening concluded to in-progress — are unrestricted.

## Rationale

Concluded is the one transition downstream consumers (a future
EP-0010 story, a Business Goal's applicability review) will trust
without re-verifying; gating it exactly like session close reuses a
proven, well-understood pattern rather than inventing a new one, and
leaving every other transition free keeps the day-to-day research
workflow unencumbered.

## Alternatives Considered

An ungated concluded transition was considered and rejected: it would
let an incomplete or citation-broken investigation be marked
trustworthy. Gating every transition (not just concluded) was
considered and rejected as excessive friction for a working-draft
artifact.

## Implications

`set-status --status concluded` and post-hoc `create --status
concluded` both run the enumerated precondition checks before
succeeding; refusal messages name the specific missing precondition.
