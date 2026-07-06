---
id: EP-0006
type: epic
title: Refinement Web UI
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0002, EP-0003]
  impacts: [EP-0002]
  impacted-by: [EP-0001, EP-0002, EP-0003, EP-0005, EP-0007]
cites: [DEC-0001, DEC-0003, DEC-0022, DEC-0026, DEC-0032, DEC-0041, DEC-0042,
        DEC-0055, DEC-0071, DEC-0072, DEC-0073, DEC-0074, DEC-0075, DEC-0076]
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
it directly ([DEC-0001](../decisions/DEC-0001-standalone-application.md)),
unsupervised ([DEC-0003](../decisions/DEC-0003-unsupervised-sessions.md)) —
the UI is where that bet is won or lost. Canonical-store discipline
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)) requires the UI
to be good enough that people prefer it over editing Jira, and gate
quality is bounded by what approvers can comprehend
([DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)).

## Scope

**In — v1** ([DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), refined
at [SES-0010](../sessions/SES-0010-ep-0006-refinement.md)):

- **Session experience** ([DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)):
  conversation stream mixing free chat with typed cards — question cards
  (options, recommended-first) and decision-playback cards
  ([DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md)) —
  plus a progress panel (settled/open/parked). Guaranteed affordances on
  every question: notes/clarifications on any choice, a free-text response,
  and an "elaborate" option (agent expands with examples and
  compare/contrast). Pause/resume per
  [DEC-0057](../decisions/DEC-0057-session-lifecycle.md).
- **Goal artifact view**: rendered Business Goal with provenance
  drill-down (goal → decisions → transcript spans) and typed-link
  navigation.
- **Goal gate surface** ([DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)):
  semantic section-level diff, agent change summary, impact report,
  provenance links, approve/request-changes driving the host PR via the
  connector ([DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md)); raw
  diff one click away.
- **Minimal conflict view**: tension, party intents, mediation record,
  escalation status (mediation itself happens in-session).
- **Notification center** ([DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)):
  in-app source of truth with read state; email delivery via the first
  notifier connector; per-user channel preferences.
- **Identity**: login via the pluggable auth provider; OAuth host-identity
  linking flow ([DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).

**In — post-v1 stories** (each arriving with the capability that needs
it): governance dashboards ([DEC-0042](../decisions/DEC-0042-governance-reporting-split.md));
impact-ranked re-affirmation and approval queues
([DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md));
participant profile viewer/editor with consent management
([DEC-0071](../decisions/DEC-0071-opt-in-participant-profiles.md));
consolidation review and flagging
([DEC-0072](../decisions/DEC-0072-consolidation-review-flagging.md));
synthesis shared-draft commenting feeding CPs
([DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md));
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
  impact realized by [DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)),
  storage API (EP-0001), approval + metrics APIs (EP-0003), graph queries
  (EP-0004), identity (EP-0005), recipe resolver outputs and profile store
  (EP-0007).
- **UI-pluggability boundary**: the typed session-engine contract is the
  seam — an alternative front end (Slack bot, CLI) must be buildable
  against it without backend changes.
- **Notification event schema**: event → center entry → connector
  delivery.

## Risks & Open Questions

- Typed-payload contract elaboration must land in EP-0002's session-engine
  stories (would be an EP-0002 re-affirmation in live operation).
- Async session ergonomics: re-orientation quality after long pauses is a
  UX-research-worthy story.
- Frontend framework selection — story-level, within the TS constraint
  ([DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
- Accessibility and responsive baseline — story-level definition before
  v1 build.

## Derived Work

None yet — stories/spikes follow gate approval of this epic.
