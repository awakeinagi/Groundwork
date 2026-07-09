---
id: DEC-0271
type: decision
title: The Idea take-up flow is out of ST-0065's scope, reserved as a hand-off point for IDEA-0001's session
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0271 constrains the Idea take-up flow to be out of ST-0065's
  scope, reserved as a hand-off point for IDEA-0001's future session.
  The list view's contract exposes the full Idea record on selection but
  provides no session-opening affordance until IDEA-0001 designs the
  intake flow. This prevents scope bleed through the focus-artifact
  boundary; until then, take-up happens through the agent path.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0051 @ T4-T5, T8-T9"
links:
  derives-from: [SES-0051]
---

# DEC-0271: The take-up seam

## Context

Selecting a captured Idea and opening an intake session from it is the
natural next affordance after a list view — but designing that flow is
the subject of IDEA-0001 (the change-intake workflow in the
application's session engine and UI), whose take-up was explicitly
redirected behind this session.

## Decision

ST-0065's Out of Scope names the take-up flow as IDEA-0001's future
session. The list view's contract reserves the hand-off point:
selecting an Idea exposes its full record, and no session-opening
affordance exists until IDEA-0001's session designs the intake flow it
would invoke.

## Rationale

The focus-artifact test cuts both ways: pulling IDEA-0001's subject in
through a UI story's side door is exactly the scope bleed the boundary
declared at intake exists to prevent. Reserving the hand-off point
gives that future session a concrete attachment rather than a
retrofit.

## Alternatives Considered

- **Design take-up now**: absorbs a parked Idea's whole subject into a
  story about capture.

## Implications

IDEA-0001's future session gains a ready integration point in
ST-0065's list view; until then, take-up happens through the agent
path.
