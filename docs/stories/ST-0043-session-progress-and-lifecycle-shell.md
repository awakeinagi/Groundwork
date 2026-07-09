---
id: ST-0043
type: story
title: Session progress and lifecycle shell
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0042]
  impacts: [ST-0044]
  impacted-by: [ST-0059]
cites: [DEC-0057, DEC-0074, DEC-0182, DEC-0184, DEC-0186, DEC-0187, DEC-0188]
---

# ST-0043: Session Progress and Lifecycle Shell

## Summary

The container every session conversation renders inside: a progress
panel showing settled/open/parked items, and pause/resume handling that
re-orients a returning participant to what's settled and what's open
(per DEC-0057,
DEC-0074).
ST-0044's cards render inside this
shell's content region.

## Acceptance Criteria

1. A progress panel renders three buckets — settled, open, parked — kept
   current as the session's turns and distilled decisions change (per
   DEC-0074).
2. Opening a session already in progress (resume) shows a re-orientation
   summary of what's settled and what's still open before the
   participant resumes answering, rather than dropping them back into a
   blank stream
   (per DEC-0057).
3. A session auto-closed on inactivity (partial distillation) is
   rendered as closed and read-only; the shell offers no "continue" —
   only "start a new session" that loads the prior one as context (per
   DEC-0057). The shell
   never shows an auto-close while a turn is actively streaming — a
   streaming turn resets the inactivity clock, so auto-close only ever
   fires between completed turns
   (per DEC-0182).
4. The shell consumes the session engine's streaming client
   (DEC-0187)
   to keep the progress panel live while a turn streams, without
   requiring a manual refresh.
5. Shell components ship as `'use client'` exports of the npm package
   (per DEC-0184,
   DEC-0186).
6. The shell and its re-orientation summary meet WCAG 2.1 AA and remain
   usable at every Tailwind breakpoint from `sm` up, including the
   progress panel collapsing to an accessible summary below `md`
   (per DEC-0188).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The conversation content itself — question cards, decision-playback
cards, notes/free-text/elaborate affordances
(ST-0044); the session engine's
open/resume/append-turn/close contract
(ST-0032).

## Notes for Implementers

Treat this as the layout/state shell and ST-0044
as its content — the shell owns progress/lifecycle state, the
conversation story owns per-turn rendering.
