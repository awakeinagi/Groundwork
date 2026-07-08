---
id: SES-0034
type: session
title: EP-0006 story derivation — v1 surfaces, packaging/styling/transport, post-v1 backlog
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0006]
---

# SES-0034: [EP-0006](../epics/EP-0006-refinement-web-ui.md) Story Derivation

## Purpose

Slice the approved [EP-0006](../epics/EP-0006-refinement-web-ui.md)
(Refinement Web UI) into implementable stories, resolving its two
recorded open questions (frontend framework/packaging selection,
accessibility/responsive baseline) plus the session experience's
internal split and the post-v1 bullet list.

## Transcript

**T1 — Sponsor.** Continue with creating stories for
[EP-0006](../epics/EP-0006-refinement-web-ui.md).

**T2 — Agent.** Prep: confirmed [EP-0006](../epics/EP-0006-refinement-web-ui.md)
is the design frontier (approved, no derived work) and its five
depends-on/impacted-by epics ([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md),
[EP-0002](../epics/EP-0002-refinement-session-agent.md),
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md),
[EP-0005](../epics/EP-0005-connectors-and-identity.md),
[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)) are all
approved — no blocking upstream work. Round 1 with recommendations: (a)
story slice for the six v1 scope bullets — 6 stories 1:1 with the
bullets (recommended) vs. 5 merging goal view into the gate surface vs.
7 splitting session experience into conversation and progress/lifecycle;
(b) frontend framework — decide now: React (recommended, citing
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md))
vs. leave as an open AC vs. spike it; (c) draft the six post-v1 bullets
as deferred stories now (recommended) vs. leave undrafted; (d) fold
accessibility/responsive baseline into each v1 story's ACs (recommended)
vs. a standalone story.

**T3 — Sponsor.** (a) 7 stories, splitting session experience. (b)
Amended: needs to be easy to plug/drop into another app's frontend
running Next.js 15 (App Router) + React, styled with Tailwind CSS 4 +
Radix UI — not a bare "pick React" answer. (c) Draft post-v1 as deferred
stories now, as recommended. (d) Fold into each v1 story's ACs, as
recommended.

**T4 — Agent.** Round 2, narrowing (b) into concrete architecture
questions with recommendations: packaging shape — an npm React component
library rendered directly in the host's tree (recommended) vs. a
standalone app behind an iframe vs. framework-agnostic web components;
styling — Tailwind-class components sharing the host's Tailwind v4
config (recommended) vs. pre-compiled scoped CSS vs. headless
Radix-only; React Server Components boundary — every exported component
is a `'use client'` boundary (recommended) vs. also shipping
RSC-compatible server prefetch helpers; streaming transport for turn
append ([ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)
AC5) — Server-Sent Events by default (recommended) vs. WebSockets from
the start vs. leaving the transport undecided.

**T5 — Sponsor.** Packaging, styling, and RSC boundary as recommended.
Transport: SSE as the default, but also build the client so WebSocket
support can be swapped in without an API change.

**T6 — Sponsor (unprompted addition).** The frontend also needs to work
as a standalone app, in addition to being droppable into the other app.

**T7 — Agent.** Round 3, one question to pin down the standalone shape:
a thin Next.js App Router app in this repo importing the same npm
package, adding only routing/layout/auth bootstrap (recommended) vs. a
separate standalone build sharing only lower-level code.

**T8 — Sponsor.** Thin wrapper around the same package, as recommended;
confirmed it lives only in this repo, not published separately.

**T9 — Agent (synthesis).** Recorded
[DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)–[DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md);
drafted [ST-0042](../stories/ST-0042-identity-login-and-oauth-linking.md)–[ST-0049](../stories/ST-0049-standalone-application-shell.md)
(eight v1 stories, `draft`, `depends-on` build-order edges rooted at
identity, reciprocal `impacts`/`impacted-by` edges per the goal-view →
gate-surface/conflict-view and shell → conversation-UX relationships)
and [ST-0050](../stories/ST-0050-governance-dashboards.md)–[ST-0056](../stories/ST-0056-full-artifact-graph-browsing.md)
(seven post-v1 stories, `deferred`, `release: "2"`, citing
[DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md) for the deferral and
[DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md) for the
scope-move citation convention — no trigger subscription, revival is
release-2 planning); amended
[EP-0006](../epics/EP-0006-refinement-web-ui.md) (Risks → resolutions
citing the new decisions and stories, Derived Work, `cites`; set `stale`
pending re-affirmation in this gate bundle). No CMP stub drafted, per
the same precedent [EP-0002](../epics/EP-0002-refinement-session-agent.md)'s
story derivation ([SES-0033](SES-0033-ep-0002-story-derivation.md))
set — deferred until a story actually refines toward one.

**T10 — Agent (consistency checks,
[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)/[DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md)).**
Ran `sweep`/`terms` on
[DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)–[DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md).
`sweep`: [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)'s
`relates-to: [DEC-0018]` surfaced eight ratified citers of
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)
([BG-0001](../goals/BG-0001-groundwork.md),
[CMP-0001](../components/CMP-0001-artifact-store-service.md),
[CMP-0004](../components/CMP-0004-governance-gate-engine.md),
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md),
[ST-0001](../stories/ST-0001-tier1-schema-suite.md),
[ST-0002](../stories/ST-0002-storage-api-core.md),
[ST-0010](../stories/ST-0010-app-database-port.md),
[ST-0018](../stories/ST-0018-governance-event-log-metrics.md)) —
reviewed each: all are backend/storage artifacts under the
language-agnostic-specs commitment
[DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)
elaborates for the frontend specifically; none narrowed or contradicted,
no changes needed.
[DEC-0185](../decisions/DEC-0185-tailwind-styled-sharing-host-config.md)–[DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)'s
`relates-to: [DEC-0184]` surfaced only
[EP-0006](../epics/EP-0006-refinement-web-ui.md) itself (already being
amended this session). `terms`: three unlinked `depends-on`
co-occurrences on
[DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)
against [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md),
[DEC-0026](../decisions/DEC-0026-directional-impact-links.md),
[DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md)
— reviewed: false positives, the shared term is the generic link-type
name `depends-on`, not a genuine relation; no link added.

**T11 — Agent (decision-recall audit,
[DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md)).** Ran
the audit on all sixteen drafts/amendments
([EP-0006](../epics/EP-0006-refinement-web-ui.md),
[ST-0042](../stories/ST-0042-identity-login-and-oauth-linking.md)–[ST-0056](../stories/ST-0056-full-artifact-graph-browsing.md)),
one Sonnet 5 judge per artifact (≤15 candidates each). Findings applied:
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)
(signed attribution block) to
[ST-0042](../stories/ST-0042-identity-login-and-oauth-linking.md) AC4;
[DEC-0182](../decisions/DEC-0182-streaming-turn-resets-inactivity-clock.md)
to [ST-0043](../stories/ST-0043-session-progress-and-lifecycle-shell.md)
AC3; [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md) and
[DEC-0090](../decisions/DEC-0090-clickable-body-cross-references.md) to
[ST-0045](../stories/ST-0045-goal-artifact-view.md) AC2/AC3, plus an
added dedup rule for the typed-link-vs-body-citation contract gap the
judge surfaced;
[DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md) to
[ST-0046](../stories/ST-0046-goal-gate-surface.md) AC2, and its Out of
Scope's bare "later story" reference linked to
[ST-0051](../stories/ST-0051-reaffirmation-and-approval-queues.md);
[DEC-0165](../decisions/DEC-0165-conflict-gate-operation-surface.md)
and
[DEC-0183](../decisions/DEC-0183-conflicts-no-default-timeout-election.md)
to [ST-0047](../stories/ST-0047-minimal-conflict-view.md) AC3;
[DEC-0149](../decisions/DEC-0149-notifier-story-under-ep-0005.md) to
[ST-0048](../stories/ST-0048-notification-center.md)'s Out of Scope;
[DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)
to [ST-0050](../stories/ST-0050-governance-dashboards.md) AC1;
[DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)
and
[DEC-0147](../decisions/DEC-0147-derived-queue-views.md) to
[ST-0051](../stories/ST-0051-reaffirmation-and-approval-queues.md)
AC1/AC3;
[DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md) to
[ST-0054](../stories/ST-0054-synthesis-shared-draft-commenting.md);
[DEC-0101](../decisions/DEC-0101-deferred-out-of-metrics.md) and
[DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md) to
[ST-0056](../stories/ST-0056-full-artifact-graph-browsing.md)'s Notes.
One cross-cutting finding: every deferred story
([ST-0050](../stories/ST-0050-governance-dashboards.md)–[ST-0056](../stories/ST-0056-full-artifact-graph-browsing.md))
was missing
[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)
— the sibling deferred-artifact rule
[ST-0011](../stories/ST-0011-schema-evolution-machinery.md) already
pairs with [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)
— added to all seven, matching that precedent.
"Nothing to add" verdicts on
[EP-0006](../epics/EP-0006-refinement-web-ui.md),
[ST-0044](../stories/ST-0044-session-conversation-ux.md),
[ST-0049](../stories/ST-0049-standalone-application-shell.md),
[ST-0052](../stories/ST-0052-participant-profile-viewer.md), and
[ST-0053](../stories/ST-0053-consolidation-review-and-flagging.md).

## Decisions Produced

[DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
[DEC-0185](../decisions/DEC-0185-tailwind-styled-sharing-host-config.md),
[DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md),
[DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md),
[DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)

## Conflicts Raised

None.
