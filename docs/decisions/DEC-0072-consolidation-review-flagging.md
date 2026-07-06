---
id: DEC-0072
type: decision
title: Consolidations are human-reviewable in the UI; flags quarantine immediately
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0009 @ T1-T2"
links:
  derives-from: [SES-0009]
---

# DEC-0072: Human review and flagging of consolidations

## Context

[DEC-0069](DEC-0069-automated-faithfulness-checks.md) guards consolidation
generation with automated checks and no human gate — leaving no path for a
human to catch what the agents and eval system miss, even though a bad
summary silently biases every consuming session.

## Decision

The UI surfaces consolidations for review: content, source refs,
freshness state, and faithfulness-check history are browsable by any user.
Any user can **flag** a consolidation with an issue report. A flag
quarantines it immediately — treated as stale, never served, the recipe
resolver falling back to underlying sources — pending disposition in a
review queue: regenerate, fix sources, or correct the faithfulness
checker. Confirmed misses become regression cases in the evaluation corpus
([DEC-0058](DEC-0058-evaluation-harness.md)).

## Rationale

Automated checks catch what they were built to catch; humans reading
consolidations in daily use are the sensor for everything else. Quarantine
is cheap (fallback to sources always exists for derived content), so
false-positive flags cost little while missed issues cost every downstream
session — and feeding confirmed flags back into the eval corpus makes the
automated guard converge on the human standard.

## Alternatives Considered

- **Flag creates a ticket, keeps serving**: possibly-bad context keeps
  biasing sessions while the ticket ages.
- **Restrict flagging to reviewers**: the people most likely to notice a
  bad summary are ordinary session participants.

## Implications

Review/flag surface joins the EP-0007→EP-0006 impact edge (alongside
profiles); flag/quarantine/disposition semantics are EP-0007 contract
items; quarantine events flow to the ops surface
([DEC-0042](DEC-0042-governance-reporting-split.md)).
