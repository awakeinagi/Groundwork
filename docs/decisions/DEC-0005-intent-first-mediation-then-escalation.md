---
id: DEC-0005
type: decision
title: Conflicts get intent-first mediation, then documented escalation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T4-T5"
links:
  derives-from: [SES-0001]
---

# DEC-0005: Conflicts get intent-first mediation, then documented escalation

## Context

Contradictory and competing requests are the core pain point Groundwork
exists to fix. With unsupervised sessions
([DEC-0003](DEC-0003-unsupervised-sessions.md)), conflict handling cannot
default to "sort it out in the room."

## Decision

On detecting a conflict, the agent first works to understand each
stakeholder's underlying intention. Informed by that intent, it explains the
conflict to the stakeholder and offers compromises and alternatives
(mediation). If mediation fails, it escalates to the appropriate team members
(product lead, scrum master, etc.) with a well-documented Conflict record
capturing intents, proposals, and responses. Downstream generation from the
artifacts in tension is blocked until resolution.

## Rationale

Intent-first questioning makes both the compromise proposals and the
escalation record genuinely informative; a bare flag-and-escalate reproduces
today's problem with better paperwork, and pure agent mediation lacks a
backstop.

## Alternatives Considered

- **Flag + escalate only**: safe but forfeits cheap resolutions.
- **Record both and proceed**: non-blocking; ships the contradiction.

## Implications

Conflicts are first-class artifacts ([SPEC-conflict](../specs/SPEC-conflict.md))
with a fixed lifecycle: intent discovery → mediation → escalation →
resolution ratified by Decision.
