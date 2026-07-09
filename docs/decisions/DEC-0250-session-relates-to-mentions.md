---
id: DEC-0250
type: decision
title: A session's relates-to targets must appear in its body
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Every artifact in a session's relates-to list must be referenced by
  bare ID in the session's body. Blocking rule in check_links.py (both
  copies). For closed sessions, fixes land in Post-Close Enrichment
  entries per DEC-0248; for new sessions, the template and playbook make
  the mention part of writing the Purpose section. Matches 76–100%
  existing convention; ensures session record traces back to its subjects
  without silent gaps.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T6-T7, T10-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0248]
---

# DEC-0250: Session relates-to Targets Must Appear in the Body

## Context

Sessions declare their subject artifacts via `relates-to`, and the
body almost always mentions them (76–100% by target type) — but
SES-0040..SES-0044 all relate to EP-0008 without ever saying so in
prose, leaving a reader of the session record without its epic
context. The facilitator recommended a non-blocking warning because
closed sessions are append-only; the stakeholder ruled it blocking,
with the append-only tension resolved by DEC-0248's enrichment
sanction.

## Decision

Every artifact in a session's `relates-to` list must be referenced by
bare ID in the session's body. Blocking rule in `check_links.py`
(both copies). For closed sessions the fix is a Post-Close Enrichment
entry per DEC-0248; for new sessions the template and playbook make
the mention part of writing the Purpose section.

## Rationale

A session record is the provenance root for its decisions; if it
doesn't name what it was about, the trace from artifact back to
conversation has a silent hole. The rule is cheap to satisfy at
write time (the Purpose section naturally names its subjects) and now
retroactively satisfiable without touching testimony.

## Alternatives Considered

- **Warning + playbook step only**: gaps persist as permanent noise.
- **Blocking for new sessions only**: adds a date-conditional to the
  checker and leaves the existing five gaps standing.

## Implications

SES-0040..SES-0044 gain Post-Close Enrichment entries naming EP-0008.
The session template (templates.md) notes the obligation; the
session-record protocol in refinement-process.md includes it.
