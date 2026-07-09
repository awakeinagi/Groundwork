---
id: DEC-0261
type: decision
title: Captured Ideas join the project's work queue; each take-up runs the intake flow as its own session
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Inspired Ideas never extend the current session; they are parked per
  DEC-0260 and join the project's work queue (status report and "what is
  to be done?" surfaces captured Ideas alongside gated, stale, and
  frontier items). Each take-up runs the full intake protocol (DEC-0255)
  as its own session. The post-grilling summary reviews captured Ideas
  and asks for any last ones before artifact generation.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T14-T15, T20"
links:
  derives-from: [SES-0050]
---

# DEC-0261: Ideas are backlog work, not a same-session loop

## Context

The original proposal's steps 5–6 looped inspired ideas back into the
same session's grilling. That strains one-session-one-focus: decisions
would interleave across topics and `relates-to` would lose meaning.

## Decision

Inspired ideas never extend the current session. They are parked as
Ideas (per DEC-0260) and join the project's **work queue**: the status
report and "what is to be done?" answers surface captured Ideas
alongside gated, stale, and frontier items. Each take-up runs the full
intake protocol (DEC-0255) as its own session — back-to-back in the
same conversation is fine; session boundaries are provenance
boundaries, not scheduling. The post-grilling summary still performs
the inspired-ideas check: it reviews the Ideas the session captured
and asks for any last ones before artifact generation.

## Rationale

The stakeholder's framing: Ideas are work to do, like drafts needing
refinement — users can brain-dump when inspiration strikes and the
backlog holds the thought at zero cost, rather than the session
ballooning or the thought being lost. The current session closes
complete and focused.

## Alternatives Considered

- **Same-session continuation (original steps 5–6)**: simpler count,
  multi-focus records, interleaved decisions — the strain that
  motivated the question.
- **Mandatory immediate follow-on session per idea**: turns a capture
  mechanism into an obligation; take-up timing belongs to the user.

## Implications

Status report lists captured Ideas as open items. The intake playbook's
closing step reviews spawned Ideas. Mode-3 work-selection guidance
adds captured Ideas as session candidates.
