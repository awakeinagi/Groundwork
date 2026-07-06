---
id: DEC-0073
type: decision
title: "v1 UI surfaces: session experience, goal view, goal gate, minimal conflict view"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0010 @ T2-T3"
links:
  derives-from: [SES-0010]
---

# DEC-0073: v1 UI surfaces

## Context

The UI owes surfaces to every sibling epic; the v1 slice
([DEC-0022](DEC-0022-v1-goal-refinement-slice.md)) needed its UI subset
pinned so the trust-critical session experience gets the attention.

## Decision

v1 ships exactly the goal-refinement spine: the Q&A session experience,
the Business Goal artifact view with provenance drill-down (goal →
decisions → transcript spans), the gate review/approve surface for goals,
and a minimal conflict view. Deferred to post-v1 stories, each arriving
with the capability that needs it: governance dashboards, re-affirmation
queues, participant profiles, consolidation review/flagging, CP triage
views, and epic/story/component browsing.

## Rationale

Building surfaces for artifact types the v1 pipeline cannot yet produce is
motion without progress; the session experience is where the unsupervised
bet ([DEC-0003](DEC-0003-unsupervised-sessions.md)) is won or lost.

## Alternatives Considered

- **Browse-everything early**: demo value, empty shelves.
- **Thin slice of every surface**: dilutes the trust-critical part.

## Implications

Post-v1 surface stories inherit their requirements from DEC-0041/0042/
0047/0071/0072; the v1 conflict view covers display and escalation status
only (mediation happens in-session).
