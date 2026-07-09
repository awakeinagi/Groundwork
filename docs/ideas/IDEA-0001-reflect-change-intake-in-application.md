---
id: IDEA-0001
type: idea
title: Reflect the change-intake workflow in the Groundwork application's session engine and UI
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Reflect the change-intake workflow defined in SES-0050 throughout the
  application's session engine and UI. The workflow includes mandatory
  sessions for semantic change, mechanical floor requirements, expedited
  sessions, restate/align loops with verbatim proposal records,
  todo-list enforcement, agent-proposes/user-disposes intake,
  locate-first classification, and in-session staleness cascades.
  Implementation scope: intake session kinds, alignment loop in session
  UI, expedited-session support, and CP triage routing into intake.
  Taken up by SES-0052.
proposed-by: awakeinagi@gmail.com
links:
  derives-from: [SES-0050]
  relates-to: [ST-0032, ST-0055]
---

# IDEA-0001: Reflect the change-intake workflow in the application

## The Idea

SES-0050 defined a paradigm-level change-intake protocol: mandatory
sessions for semantic change (DEC-0252), the mechanical floor
(DEC-0253), expedited sessions (DEC-0254), the restate/align loop with
records opening at the verbatim proposal (DEC-0255), todo-list
enforcement (DEC-0256), agent-proposes/user-disposes intake for
agent-originated intent (DEC-0257), locate-first classification
(DEC-0266), and the in-session staleness cascade (DEC-0267). The
application's session engine (ST-0032) and triage/session surfaces
(ST-0055) should embody this protocol — intake session kinds, the
alignment loop in the session UI, expedited-session support, and CP
triage routing into intake.

## Spark Context

Parked at SES-0050 T18–T19 under the focus-artifact test: the
application's design is a different focus than the method change the
session refined.

## Disposition

Taken up 2026-07-09 by SES-0052 (intake session per DEC-0261).
