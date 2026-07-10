---
id: DEC-0350
type: decision
title: "EP-0009 derives with DEC-0339's full scope; backfill deferred by sequencing, not supersession"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0065 @ T5-T6"
overview: >-
  SES-0065's take-up of IDEA-0015 surfaced a collision between an
  initially-preferred thinner forward-only epic framing and
  DEC-0339's already-accepted full-surface charter. Resolved by
  reconciling, not narrowing: the Artifact Interaction Surface epic
  (EP-0009) derives with DEC-0339's complete scope intact --
  librarian agent CMP, artifact-interact skill CMP, and the
  mandatory runtime-policy contract sections in each. The backfill
  of the already-built surface (DEC-0342's retro-documentation
  protocol, DEC-0340's SPEC agent-contract profile amendment,
  DEC-0341's conformance check, TRIGGERS.md absorption-trigger
  arming) stays in scope but its execution is deferred to a
  dedicated fold-in Idea's own take-up session, rather than being
  executed as this session's derived work. This is work sequencing
  within an unchanged charter: DEC-0339 is neither superseded nor
  amended.
links:
  derives-from: [SES-0065]
  relates-to: [DEC-0339, DEC-0342, IDEA-0015]
---

## Context

Taking up IDEA-0015 to derive the Artifact Interaction Surface epic
surfaced a framing collision: SES-0065's grilling considered a
thinner, forward-only epic (govern only what's newly built from here)
against DEC-0339's already-accepted charter, which is full-surface —
both CMPs, the runtime-policy contract sections, and the DEC-0342
backfill of the already-built librarian/skill. The stakeholder chose
the thinner framing first (T4) before the collision was surfaced
(T5), which required reconciling rather than silently narrowing an
accepted decision's scope.

## Decision

EP-0009 (Artifact Interaction Surface) derives with DEC-0339's full
charted scope intact: the librarian agent CMP, the artifact-interact
skill CMP, and the mandatory runtime-policy contract sections in each.
The backfill of the already-built surface (DEC-0342's retro-
documentation protocol, DEC-0340's SPEC agent-contract profile
amendment, DEC-0341's conformance check, and arming the absorption
triggers in docs/TRIGGERS.md) is included in the epic's scope but its
execution is deferred — taken up later via a dedicated fold-in Idea's
own intake session, not folded into this session's derived work. This
is a work-sequencing choice inside an unchanged charter: DEC-0339 is
neither superseded nor amended.

## Rationale

DEC-0339 is an accepted decision; narrowing its charter to a
forward-only epic without a superseding decision would silently
contradict ratified scope. Deferring the backfill's *execution* while
keeping it *in scope* preserves DEC-0339's charter exactly, gives the
epic gate something derivable today (the exploratory spike program),
and lets the backfill take-up proceed on its own schedule without
blocking EP-0009's approval.

## Alternatives Considered

- **Forward-only thin epic** (the stakeholder's initial framing, T4)
  — rejected once the collision with DEC-0339's accepted full-surface
  charter was surfaced (T5); would have required superseding DEC-0339
  to be honest, which the stakeholder did not intend.
- **Supersede DEC-0339 to narrow it, then charter backfill
  separately** — rejected as disproportionate; DEC-0339's charter
  itself is not wrong, only its execution ordering needed settling.

## Implications

EP-0009's Derived Work section lists the backfill as pending,
resumed at the fold-in Idea's take-up. The fold-in Idea (created this
session) carries the accurate grounding for that future session.
