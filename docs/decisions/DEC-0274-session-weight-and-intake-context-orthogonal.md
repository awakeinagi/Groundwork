---
id: DEC-0274
type: decision
title: The session contract models weight and intake-opening context as orthogonal fields
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0274 constrains ST-0032's session contract to model weight and
  intake-opening context as orthogonal fields: a session kind enum (full
  | expedited | idea-capture) and an optional intake context (verbatim
  proposal, proposer, origin: user | agent | cp | idea, source ref when
  origin is CP or Idea). Expedited and idea-capture sessions always carry
  intake context; full sessions open either planned or intake-opened.
  idea-capture stays in the enum for the conversational case; form-shaped
  capture remains a sessionless mechanical write.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T4-T7"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0254, DEC-0258, DEC-0272]
---

# DEC-0274: Session weight and intake context are orthogonal

## Context

The paradigm has three session weights (full, expedited, idea-capture
micro-session) and a separate notion of how a session opens
(intake-opened at a verbatim proposal vs. planned refinement from the
frontier). IDEA-0001's own take-up demonstrated the overlap: an
intake-opened *full* grilling session is both things at once. And
SES-0051 had already made form-shaped Idea capture a sessionless
mechanical write (DEC-0272) — does `idea-capture` still belong in a
session enum?

## Decision

ST-0032's session contract (and SPEC-session's frontmatter) carry two
orthogonal fields: a session **kind** (weight) enum — `full |
expedited | idea-capture` — and an optional **intake-opening context**
(verbatim proposal, proposer, origin: `user | agent | cp | idea`,
source ref when the origin is a CP or Idea). Expedited and
idea-capture sessions always carry intake context; full sessions open
either planned or intake-opened. `idea-capture` stays in the enum for
the *conversational* case: an intake conversation whose path-pick
lands on "just capture this" closes as an idea-capture micro-session
recording the restate/align provenance (zero decisions valid, per
DEC-0258). Form-shaped capture (quick-capture, park-as-Idea) remains a
sessionless mechanical write per DEC-0272 — the two paths coexist.

## Rationale

A single enum with `intake` as a kind conflates weight with opening
mode. Dropping `idea-capture` would mislabel zero-decision sessions as
expedited (which implies a recorded semantic change), muddying the
eval harness's and audits' view of session shapes.

## Alternatives Considered

- **Single kind enum including `intake`**: wrong shape — intake is how
  a session of any weight begins, not a fourth weight.
- **Separate pre-session intake object**: keeps ST-0032 untouched but
  splits provenance; DEC-0255's paradigm rule is that T1 of the
  session *is* the proposal.
- **Drop `idea-capture`; require sessions for all capture**: would
  re-litigate the accepted DEC-0272 with no cause.

## Implications

SPEC-session gains `kind` and `intake` frontmatter; ST-0032's open
operation accepts the intake context and materializes the proposal as
T1. The take-up flow (DEC-0281) and CP routing (DEC-0277) populate
`origin: idea` and `origin: cp` respectively.
