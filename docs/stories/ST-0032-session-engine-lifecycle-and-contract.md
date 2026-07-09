---
id: ST-0032
type: story
title: Session engine lifecycle and contract
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
created: 2026-07-08
overview: >-
  Pluggable-UI seam for 1:1 refinement sessions: open/resume/append-turn/close
  operations for one participant conducting one conversation with agent.
  Sessions stay open across pauses by default; inactivity auto-closes with
  partial distillation. Sessions carry kind (full/expedited/idea-capture) and
  optional intake-opening context with verbatim proposal, proposer, origin,
  source ref. Modified-approved artifacts trigger staleness cascade at close.
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: []
  impacts: [ST-0016, ST-0017, ST-0034, ST-0035, ST-0036, ST-0037, ST-0040, ST-0059]
  impacted-by: []
cites: [DEC-0021, DEC-0035, DEC-0057, DEC-0182, DEC-0273, DEC-0274, DEC-0279,
        DEC-0280]
---

# ST-0032: Session Engine Lifecycle and Contract

## Summary

The pluggable-UI seam every refinement session runs through: open,
resume, append-turn, and close operations, plus streaming, for one
participant conducting one 1:1 conversation with the agent. Every other
in-session capability in this epic (transcript capture ST-0034,
guardrails ST-0035, conflict mediation ST-0036, synthesis ST-0037,
glossary maintenance ST-0040) executes inside a session this engine
opened, under this story's lifecycle and inactivity semantics. Sessions
carry a kind and, when intake-opened, the intake context that starts
the record at the verbatim proposal — the engine end of the
change-intake protocol (DEC-0273, DEC-0274).

## Acceptance Criteria

1. The engine exposes open/resume/append-turn/close operations for a 1:1
   session (one participant, one artifact focus), independent of any
   particular chat UI — the pluggable-UI seam. `append-turn` and `close`
   are the only mutations the storage API accepts for session artifacts —
   no edit or delete of existing turns, enforced server-side
   (per DEC-0021,
   DEC-0035).
2. Sessions stay open across pauses by default; resuming re-orients the
   participant with what's settled and what's open
   (per DEC-0057).
3. After a configurable inactivity window, the engine auto-closes the
   session with partial distillation: confirmed decisions commit as
   accepted, unconfirmed material is marked `proposed`, and the record
   notes incompleteness
   (per DEC-0057).
4. A later return opens a *new* session that loads the prior one as
   context, never reopening a closed session
   (per DEC-0057).
5. Turn append is streaming-capable: a consuming UI can render partial
   agent output as it's produced, without changing the append-turn
   contract's eventual-consistency guarantee once a turn completes.
6. A turn actively streaming counts as activity: the inactivity window of
   AC3 only starts counting after the current turn fully completes.
   Auto-close never truncates a turn mid-stream
   (per DEC-0182).
7. The session contract carries a kind — `full | expedited |
   idea-capture` — and an optional intake-opening context: the verbatim
   proposal, the proposer, an origin (`user | agent | cp | idea`), and a
   source ref when the origin is a CP or Idea. Expedited and
   idea-capture sessions always carry intake context; full sessions open
   either planned or intake-opened
   (per DEC-0274).
8. An intake-opened session begins its transcript at the verbatim
   proposal (T1) followed by the agent's restatement; the engine runs
   the intake authority check (ST-0035) at open, and does not enter
   grilling phases before a confirmed typed alignment turn exists
   (per DEC-0273,
   DEC-0280).
9. A session that modified approved artifacts cannot close until the
   staleness cascade is marked: superseding Decisions and stale marks
   are durably written via the staleness sweep (ST-0016) before close.
   Re-affirmation is presented in-session when the participant holds the
   approval right; otherwise the stale marks feed ST-0017's
   re-affirmation queues
   (per DEC-0279).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Impact Notes

AC9's close-cascade invariant shapes EP-0003's staleness machinery:
ST-0016's sweep must be synchronously invocable at session close, and
ST-0017's re-affirmation queues receive their stale marks from sessions
closing under this contract — the ST-0032 → ST-0016/ST-0017 impact
edges (per DEC-0279).

## Out of Scope

Transcript content and storage format
(ST-0034);
what strategy pack drives the session's questions
(ST-0033); the
chat UI consuming this engine (EP-0006).

## Notes for Implementers

The engine's contract must be UI-agnostic enough that both a chat web UI
(EP-0006) and a CLI/agent-driven
facilitator (as used in this project's own bootstrap) can drive it
without engine changes.

ST-0059's SSE endpoint is the transport consumer of AC5's streaming
turn append: it resumes from the stable, monotonically ordered
per-session event ids this engine assigns, and its reconnect behavior
leans on AC6's rule that a streaming turn counts as activity.
