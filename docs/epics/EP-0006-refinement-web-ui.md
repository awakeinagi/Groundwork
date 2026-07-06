---
id: EP-0006
type: epic
title: Refinement Web UI
status: draft
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0002, EP-0003]
  impacts: [EP-0002]
  impacted-by: [EP-0001, EP-0002, EP-0003, EP-0005, EP-0007]
cites: [DEC-0001, DEC-0003, DEC-0022, DEC-0026]
---

# EP-0006: Refinement Web UI

## Summary

The TypeScript web application business users actually touch: the Q&A
session experience, the artifact browser with traceability navigation, gate
approval flows, and conflict views. Built against the session-engine,
storage, and governance contracts so the UI layer itself remains pluggable.

## Why (Goal Alignment)

Groundwork is a standalone application because stakeholders must interact
with it directly ([DEC-0001](../decisions/DEC-0001-standalone-application.md)),
unsupervised ([DEC-0003](../decisions/DEC-0003-unsupervised-sessions.md)) —
the UI is where that bet is won or lost. Canonical-store discipline
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)) requires the UI
to be good enough that people prefer it over editing Jira.

## Scope

**In:** session UI — chat-style Q&A with the agent, resumability, progress
sense ("what we've settled, what's open"); artifact browser — render
markdown artifacts, navigate typed links up and down the graph, view
provenance (contract line → Decision → transcript span); gate UI — approval
queues per approver, sign-off/rejection with reasons, committee status;
conflict views — tension, party intents, mediation record, escalation;
staleness surfacing.

**Out:** the agent behind the sessions (EP-0002); approval semantics
(EP-0003); auth providers (EP-0005 — the UI consumes identity).

## Domain Context

Bounded context: **Experience**. Uses the whole glossary; introduces no
domain terms of its own — a deliberate constraint: the UI vocabulary must
match [CONTEXT.md](../../CONTEXT.md) exactly.

## Interfaces & Contracts to Define

- Consumes: session engine (EP-0002), storage API (EP-0001), approval API
  (EP-0003), graph queries (EP-0004), identity (EP-0005).
- **UI-pluggability boundary**: the session-engine contract is the seam —
  an alternative front end (Slack bot, CLI) must be buildable against it
  without backend changes.

## Risks & Open Questions

- The v1 slice ([DEC-0022](../decisions/DEC-0022-v1-goal-refinement-slice.md))
  needs only the session UI + goal view + goal gate; scoping the v1 subset
  precisely happens at this epic's refinement.
- Async session ergonomics: stakeholders answering over days, notifications.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
