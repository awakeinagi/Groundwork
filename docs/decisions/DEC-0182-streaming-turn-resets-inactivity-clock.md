---
id: DEC-0182
type: decision
title: A streaming turn resets the session inactivity clock; auto-close never truncates mid-turn
status: accepted
owner: ds-lead
created: 2026-07-08
overview: >-
  Resolves DEC-0057's race condition: a turn actively streaming counts
  as activity; the inactivity window only starts once the turn fully
  completes. Auto-close never truncates mid-turn. Constrains session
  lifecycle behavior.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T9-T10"
links:
  derives-from: [SES-0033]
  relates-to: [DEC-0057]
  supersedes: []
---

# DEC-0182: A Streaming Turn Resets the Session Inactivity Clock; Auto-Close Never Truncates Mid-Turn

## Context

The decision-recall audit on
ST-0032
flagged a race DEC-0057 left open:
streaming turn append (AC5) can overlap with the inactivity-window
auto-close (AC3) — what happens if the window elapses while a turn is
still streaming?

## Decision

A turn actively streaming counts as activity: the inactivity window only
starts counting once the current turn fully completes. Auto-close never
force-closes or truncates a session mid-stream.

## Rationale

Truncating a partial turn risks losing a participant's in-flight answer
and produces an incomplete, hard-to-interpret transcript entry — worse
than simply deferring the timeout check until the turn resolves, which
costs nothing since a genuinely inactive participant isn't streaming
anything.

## Alternatives Considered

- **Auto-close can truncate a partial turn**: simpler timer
  implementation, but risks data loss on exactly the participant input
  the system exists to capture faithfully
  (per DEC-0052).

## Implications

ST-0032
AC6 states this as a testable behavior.
