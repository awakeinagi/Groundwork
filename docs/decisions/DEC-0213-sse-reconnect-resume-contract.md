---
id: DEC-0213
type: decision
title: The SSE session-streaming story defines reconnect-with-backoff and resume-from-last-event-id now
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T3-T4"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0187]
  supersedes: []
---

# DEC-0213: SSE Reconnect/Resume Defined at Story Grain

## Context

DEC-0187
requires a transport-agnostic client abstraction but left connection-
drop behavior unspecified. Story derivation needed to decide whether
ST-0059
pins this down now or defers it to Component Doc stage.

## Decision

ST-0059's
Acceptance Criteria require: the client reconnects automatically with
backoff on a dropped connection, and resumes the stream from the
last-seen SSE event id (standard `Last-Event-ID` semantics) — without
dropping or duplicating turns for the UI.

## Rationale

A dropped connection during a live refinement session is exactly the
kind of edge case
[refinement-process.md](../../CONTEXT.md)'s story-derivation guidance
calls out: surfaced but unresolved upstream (DEC-0187
left it open), so it becomes concrete, testable Acceptance Criteria
here rather than an implementer's silent guess. It is also directly
observable and testable (kill the connection, assert resume), fitting
this story's grain rather than needing the fuller Component Doc
contract to pin it down first.

## Alternatives Considered

- **Defer to Component Doc stage**: rejected — leaves a real, sponsor-
  relevant edge case (a stakeholder's session losing turns on a network
  blip) unspecified through an entire story's gate cycle.

## Implications

ST-0059's
Component Doc, once drafted, must implement `Last-Event-ID`-based
resume as a Constraint, not merely a Note.
