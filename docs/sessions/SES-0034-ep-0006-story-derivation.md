---
id: SES-0034
type: session
title: EP-0006 story derivation — v1 surfaces, packaging/styling/transport, post-v1 backlog
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Sliced Refinement Web UI epic into 15 stories (8 v1, 7 post-v1
  deferred). Amended stakeholder's React recommendation to require
  pluggability into Next.js 15 App Router with Tailwind 4, Radix UI.
  Settled packaging as npm component library, styling via Tailwind
  sharing host config, RSC boundaries as use-client everywhere, SSE
  default streaming with WebSocket swappability. Drafted standalone Next
  wrapper app. Decision-recall audit found citations to add across
  multiple stories and required adding DEC-0133 to all deferred stories.
  Produced ST-0042-ST-0056 and DEC-0184-DEC-0188.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0006]
---

# SES-0034: EP-0006 Story Derivation

## Purpose

Slice the approved EP-0006
(Refinement Web UI) into implementable stories, resolving its two
recorded open questions (frontend framework/packaging selection,
accessibility/responsive baseline) plus the session experience's
internal split and the post-v1 bullet list.

## Transcript

**T1 — Sponsor.** Continue with creating stories for
EP-0006.

**T2 — Agent.** Prep: confirmed EP-0006
is the design frontier (approved, no derived work) and its five
depends-on/impacted-by epics (EP-0001,
EP-0002,
EP-0003,
EP-0005,
EP-0007) are all
approved — no blocking upstream work. Round 1 with recommendations: (a)
story slice for the six v1 scope bullets — 6 stories 1:1 with the
bullets (recommended) vs. 5 merging goal view into the gate surface vs.
7 splitting session experience into conversation and progress/lifecycle;
(b) frontend framework — decide now: React (recommended, citing
DEC-0018)
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
append (ST-0032
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
DEC-0184–DEC-0188;
drafted ST-0042–ST-0049
(eight v1 stories, `draft`, `depends-on` build-order edges rooted at
identity, reciprocal `impacts`/`impacted-by` edges per the goal-view →
gate-surface/conflict-view and shell → conversation-UX relationships)
and ST-0050–ST-0056
(seven post-v1 stories, `deferred`, `release: "2"`, citing
DEC-0073 for the deferral and
DEC-0100 for the
scope-move citation convention — no trigger subscription, revival is
release-2 planning); amended
EP-0006 (Risks → resolutions
citing the new decisions and stories, Derived Work, `cites`; set `stale`
pending re-affirmation in this gate bundle). No CMP stub drafted, per
the same precedent EP-0002's
story derivation (SES-0033)
set — deferred until a story actually refines toward one.

**T10 — Agent (consistency checks,
DEC-0157/DEC-0158).**
Ran `sweep`/`terms` on
DEC-0184–DEC-0188.
`sweep`: DEC-0184's
`relates-to: [DEC-0018]` surfaced eight ratified citers of
DEC-0018
(BG-0001,
CMP-0001,
CMP-0004,
EP-0001,
ST-0001,
ST-0002,
ST-0010,
ST-0018) —
reviewed each: all are backend/storage artifacts under the
language-agnostic-specs commitment
DEC-0184
elaborates for the frontend specifically; none narrowed or contradicted,
no changes needed.
DEC-0185–DEC-0187's
`relates-to: [DEC-0184]` surfaced only
EP-0006 itself (already being
amended this session). `terms`: three unlinked `depends-on`
co-occurrences on
DEC-0188
against DEC-0009,
DEC-0026,
DEC-0135
— reviewed: false positives, the shared term is the generic link-type
name `depends-on`, not a genuine relation; no link added.

**T11 — Agent (decision-recall audit,
DEC-0137).** Ran
the audit on all sixteen drafts/amendments
(EP-0006,
ST-0042–ST-0056),
one Sonnet 5 judge per artifact (≤15 candidates each). Findings applied:
DEC-0153
(signed attribution block) to
ST-0042 AC4;
DEC-0182
to ST-0043
AC3; DEC-0009 and
DEC-0090 to
ST-0045 AC2/AC3, plus an
added dedup rule for the typed-link-vs-body-citation contract gap the
judge surfaced;
DEC-0146 to
ST-0046 AC2, and its Out of
Scope's bare "later story" reference linked to
ST-0051;
DEC-0165
and
DEC-0183
to ST-0047 AC3;
DEC-0149 to
ST-0048's Out of Scope;
DEC-0163
to ST-0050 AC1;
DEC-0038
and
DEC-0147 to
ST-0051
AC1/AC3;
DEC-0047 to
ST-0054;
DEC-0101 and
DEC-0119 to
ST-0056's Notes.
One cross-cutting finding: every deferred story
(ST-0050–ST-0056)
was missing
DEC-0133
— the sibling deferred-artifact rule
ST-0011 already
pairs with DEC-0100
— added to all seven, matching that precedent.
"Nothing to add" verdicts on
EP-0006,
ST-0044,
ST-0049,
ST-0052, and
ST-0053.

## Decisions Produced

DEC-0184,
DEC-0185,
DEC-0186,
DEC-0187,
DEC-0188

## Conflicts Raised

None.
