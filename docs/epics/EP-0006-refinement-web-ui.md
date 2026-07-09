---
id: EP-0006
type: epic
title: Refinement Web UI
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0002, EP-0003]
  impacts: [EP-0002, EP-0008]
  impacted-by: [EP-0001, EP-0002, EP-0003, EP-0005, EP-0007, EP-0008]
cites: [DEC-0001, DEC-0002, DEC-0003, DEC-0022, DEC-0026, DEC-0032, DEC-0041,
        DEC-0042, DEC-0043, DEC-0051, DEC-0055, DEC-0057, DEC-0071, DEC-0072,
        DEC-0073, DEC-0074, DEC-0075, DEC-0076, DEC-0184, DEC-0185, DEC-0186,
        DEC-0187, DEC-0188]
---

# EP-0006: Refinement Web UI

## Summary

The TypeScript web application business users actually touch: a
structured-hybrid session experience, artifact views with provenance
drill-down, gate review surfaces that wrap PRs in semantic diffs, an
in-app notification center, and — post-v1 — dashboards, re-affirmation
queues, profile management, and consolidation review. Built against the
session-engine, storage, governance, graph, and retrieval contracts so the
UI layer itself remains pluggable.

## Why (Goal Alignment)

Groundwork is a standalone application because stakeholders interact with
it directly (DEC-0001),
unsupervised (DEC-0003) —
the UI is where that bet is won or lost. Canonical-store discipline
(DEC-0002) requires the UI
to be good enough that people prefer it over editing Jira, and gate
quality is bounded by what approvers can comprehend
(DEC-0076).

## Scope

**In — v1** (DEC-0073, refined
at SES-0010):

- **Session experience** (DEC-0074):
  conversation stream mixing free chat with typed cards — question cards
  (options, recommended-first) and decision-playback cards
  (DEC-0051) —
  plus a progress panel (settled/open/parked). Guaranteed affordances on
  every question: notes/clarifications on any choice, a free-text response,
  and an "elaborate" option (agent expands with examples and
  compare/contrast). Pause/resume per
  DEC-0057.
- **Goal artifact view**: rendered Business Goal with provenance
  drill-down (goal → decisions → transcript spans) and typed-link
  navigation.
- **Goal gate surface** (DEC-0076):
  semantic section-level diff, agent change summary, impact report,
  provenance links, approve/request-changes driving the host PR via the
  connector (DEC-0032); raw
  diff one click away.
- **Minimal conflict view**: tension, party intents, mediation record,
  escalation status (mediation itself happens in-session).
- **Notification center** (DEC-0075):
  in-app source of truth with read state; email delivery via the first
  notifier connector; per-user channel preferences.
- **Identity**: login via the pluggable auth provider; OAuth host-identity
  linking flow (DEC-0043).

The goal-scoped v1 surface set (goal artifact view, goal gate surface)
tracks the v1 vertical slice — goal refinement end-to-end (DEC-0022).

**In — post-v1 stories** (each arriving with the capability that needs
it): governance dashboards (DEC-0042);
impact-ranked re-affirmation and approval queues
(DEC-0041);
participant profile viewer/editor with consent management
(DEC-0071);
consolidation review and flagging
(DEC-0072);
synthesis shared-draft commenting feeding CPs
(DEC-0055);
CP triage views; full artifact/graph browsing across all types.

**Out:** the agent behind the sessions (EP-0002); approval semantics
(EP-0003); connectors and auth providers themselves (EP-0005); retrieval
and profiles storage (EP-0007).

## Domain Context

Bounded context: **Experience**. Uses the whole glossary; introduces no
domain terms of its own — a deliberate constraint: UI vocabulary must
match [CONTEXT.md](../../CONTEXT.md) exactly.

## Interfaces & Contracts to Define

- Consumes: session engine with **typed turn payloads** (question-card,
  decision-playback, elaboration-request/response — the EP-0006→EP-0002
  impact realized by DEC-0074),
  storage API (EP-0001), approval + metrics APIs (EP-0003), graph queries
  (EP-0004), identity (EP-0005), recipe resolver outputs and profile store
  (EP-0007). All of these reach the UI through EP-0008's inbound API:
  the UI's HTTP + SSE transport needs define that route and streaming
  surface (DEC-0187) — the EP-0006→EP-0008 impact edge (per DEC-0026).
- **UI-pluggability boundary**: the typed session-engine contract is the
  seam — an alternative front end (Slack bot, CLI) must be buildable
  against it without backend changes.
- **Notification event schema**: event → center entry → connector
  delivery.

## Risks & Open Questions

- Typed-payload contract elaboration must land in EP-0002's session-engine
  stories — recorded as a story-level contract elaboration within
  ST-0044, consuming
  ST-0032's
  contract (would be an EP-0002
  re-affirmation in live operation).
- Async session ergonomics: re-orientation quality after long pauses —
  resolved into ST-0043
  AC2 (per DEC-0057).
- Frontend framework and packaging selection — resolved at
  SES-0034: an
  embeddable npm React component library for the stated Next.js 15 App
  Router / Tailwind CSS 4 / Radix UI host, plus a thin standalone app in
  this repo wrapping the same package
  (DEC-0184, DEC-0185, DEC-0186, DEC-0187).
- Accessibility and responsive baseline — resolved at
  SES-0034: WCAG 2.1
  AA plus Tailwind's default breakpoints, folded into every v1 story's
  acceptance criteria rather than a standalone story
  (DEC-0188).

## Derived Work

v1 stories (SES-0034):
ST-0042
(identity), ST-0043
(session progress/lifecycle shell),
ST-0044 (session
conversation UX), ST-0045
(goal artifact view), ST-0046
(goal gate surface), ST-0047
(minimal conflict view), ST-0048
(notification center), ST-0049
(standalone application shell).

Late-derived (SES-0051): ST-0065 (Idea capture and minimal list —
release 1).

Deferred to release 2: ST-0050–ST-0056
(dashboards, re-affirmation queues, profile viewer, consolidation review,
synthesis commenting, CP triage views, full artifact/graph browsing):

- ST-0050 — governance dashboards
- ST-0051 — impact-ranked re-affirmation and approval queues
- ST-0052 — participant profile viewer/editor with consent management
- ST-0053 — consolidation review and flagging
- ST-0054 — synthesis shared-draft commenting feeding change proposals
- ST-0055 — change proposal triage views
- ST-0056 — full artifact/graph browsing
