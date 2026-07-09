---
id: DEC-0260
type: decision
title: The focus-artifact test delineates in-session enrichment from parking an Idea
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Apply the focus-artifact test mid-session: if a thought changes the
  artifact this session is refining—its contracts, scope, bounds, or
  decisions—it is enrichment and is grilled now. If acting on it requires
  refining a different artifact or creating one at another level, it is
  parked in seconds as an Idea (DEC-0258) when level unclear, as
  deferred ST/SP (DEC-0259) when clear. The session's focus is the bright
  line; mechanical rule preserves consistency across sessions.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T14-T15"
links:
  derives-from: [SES-0050]
---

# DEC-0260: The focus-artifact test

## Context

Grilling inspires tangents. One session has one artifact focus; the
line between "grill this now" and "this belongs elsewhere" needed a
mechanical rule rather than per-case negotiation.

## Decision

Mid-session, apply the **focus-artifact test**: if a thought changes
the artifact this session is refining — its contracts, scope, bounds,
or decisions — it is enrichment and is grilled now. If acting on it
requires refining a *different* artifact, or creating one at another
level, it is parked in seconds — as an Idea (DEC-0258) when its level
is unclear, as a deferred ST/SP (DEC-0259) when clear — and the
session continues. The session's focus is the bright line.

## Rationale

Mechanical rules survive; judgment calls drift. Size-based tests fail
in both directions (small change to a different artifact still breaks
focus; a big change to the focus artifact is what the session is for),
and asking the user each time interrupts flow for cases the test
answers instantly.

## Alternatives Considered

- **Ask each time**: maximally user-controlled, inconsistent records,
  needless interruptions.
- **Size-based test**: intuitive and wrong.

## Implications

Enters the grilling method's core bullets in the skill reference and
AGENTS.md. Works jointly with DEC-0261 (parked Ideas join the work
queue).
