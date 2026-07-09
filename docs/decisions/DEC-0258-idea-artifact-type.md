---
id: DEC-0258
type: decision
title: A new Idea artifact type (IDEA-) captures raw change intent verbatim, with lifecycle captured → taken-up | declined
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  New Idea artifact type (IDEA- prefix, docs/ideas/) captures raw change
  intent verbatim. Statuses: captured → taken-up (intake session derives
  and refinement begins) or declined (with recorded rationale). Captured
  mid-session under focus-artifact test (DEC-0260) or via dedicated
  idea-capture micro-session. Pass no gates; nothing derives except
  take-up session. Frictionless capture keeps mandatory-session rule
  (DEC-0252) and focus-artifact test livable.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T13-T15"
links:
  derives-from: [SES-0050]
---

# DEC-0258: The Idea artifact type

## Context

Two capture needs had no artifact form: new ideas arising mid-session
that require a separate session, and a user wanting to record an idea
without grilling or artifact generation. Overloading the CP for these
would convolute its purpose (out-of-band and unauthorized-attempt
capture, DEC-0262).

## Decision

A new artifact type, **Idea** (`IDEA-` prefix, `docs/ideas/`),
captures raw change intent verbatim. Statuses: `captured` (open) →
`taken-up` (an intake session derives from it and refinement begins)
or `declined` (with recorded rationale — the durable answer to "why
didn't we ever do X?"). Ideas are captured mid-session under the
focus-artifact test (DEC-0260) or via a dedicated idea-capture
micro-session — a session record with zero linked decisions is valid
for this purpose, and one micro-session may batch several ideas. Every
session that spawns an Idea cross-references it (`relates-to` + body
mention), preserving the provenance of the spawn context. Ideas pass
no gates and nothing derives from them except their take-up session.

## Rationale

Frictionless capture is what makes the mandatory-session rule
(DEC-0252) and the focus-artifact test (DEC-0260) livable: parking a
thought must cost seconds. Declined-with-rationale preserves
institutional memory that deletion would erase; IDs are never reused
and history is never rewritten, so a statusless inbox was ruled out.

## Alternatives Considered

- **Statusless inbox notes, deleted when handled**: cheapest, breaks
  provenance and loses declined rationale.
- **Full gated artifact**: an idea is pre-commitment by definition;
  gating contradicts frictionless capture.
- **Overload the CP**: conflates in-band raw intent with out-of-band/
  unauthorized capture semantics.

## Implications

Checker learns the prefix and type; the status report lists captured
Ideas beside untriaged CPs; templates gain an Idea template; the
graph, search, consistency, and coupling tools accept the new prefix.
The boundary against the deferral mechanism is DEC-0259. Application
reflection (data model, views, SPEC-idea) is parked as IDEA-0002.
