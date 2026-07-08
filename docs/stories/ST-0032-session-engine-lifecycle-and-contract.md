---
id: ST-0032
type: story
title: Session engine lifecycle and contract
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: []
  impacts: [ST-0034, ST-0035, ST-0036, ST-0037, ST-0040, ST-0059]
  impacted-by: []
cites: [DEC-0021, DEC-0035, DEC-0057, DEC-0182]
---

# ST-0032: Session Engine Lifecycle and Contract

## Summary

The pluggable-UI seam every refinement session runs through: open,
resume, append-turn, and close operations, plus streaming, for one
participant conducting one 1:1 conversation with the agent. Every other
in-session capability in this epic (transcript capture, guardrails,
conflict mediation, synthesis, glossary maintenance) executes inside a
session this engine opened.

## Acceptance Criteria

1. The engine exposes open/resume/append-turn/close operations for a 1:1
   session (one participant, one artifact focus), independent of any
   particular chat UI — the pluggable-UI seam. `append-turn` and `close`
   are the only mutations the storage API accepts for session artifacts —
   no edit or delete of existing turns, enforced server-side
   (per [DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md),
   [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
2. Sessions stay open across pauses by default; resuming re-orients the
   participant with what's settled and what's open
   (per [DEC-0057](../decisions/DEC-0057-session-lifecycle.md)).
3. After a configurable inactivity window, the engine auto-closes the
   session with partial distillation: confirmed decisions commit as
   accepted, unconfirmed material is marked `proposed`, and the record
   notes incompleteness
   (per [DEC-0057](../decisions/DEC-0057-session-lifecycle.md)).
4. A later return opens a *new* session that loads the prior one as
   context, never reopening a closed session
   (per [DEC-0057](../decisions/DEC-0057-session-lifecycle.md)).
5. Turn append is streaming-capable: a consuming UI can render partial
   agent output as it's produced, without changing the append-turn
   contract's eventual-consistency guarantee once a turn completes.
6. A turn actively streaming counts as activity: the inactivity window of
   AC3 only starts counting after the current turn fully completes.
   Auto-close never truncates a turn mid-stream
   (per [DEC-0182](../decisions/DEC-0182-streaming-turn-resets-inactivity-clock.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

Transcript content and storage format
([ST-0034](ST-0034-transcript-capture-and-confirmed-distillation.md));
what strategy pack drives the session's questions
([ST-0033](ST-0033-strategy-pack-format-and-plugin-loading.md)); the
chat UI consuming this engine ([EP-0006](../epics/EP-0006-refinement-web-ui.md)).

## Notes for Implementers

The engine's contract must be UI-agnostic enough that both a chat web UI
([EP-0006](../epics/EP-0006-refinement-web-ui.md)) and a CLI/agent-driven
facilitator (as used in this project's own bootstrap) can drive it
without engine changes.
