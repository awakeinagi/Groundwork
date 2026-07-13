---
id: DEC-0448
type: decision
title: "RSCH lifecycle and gating"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  Research artifacts carry the statuses commissioned, in-progress,
  concluded, and abandoned. Two entry points exist: an investigation
  commissioned at intake starts at commissioned, and research that
  already happened is created post-hoc directly at concluded. A
  concluded Research artifact is reopenable: it may return to in-
  progress for a follow-up round, and every round is recorded in its
  own timestamped, append-only section — earlier rounds are never
  rewritten, preserving what was known at each point in time. The
  type is ungated; every transition to concluded is a stakeholder
  findings review, and all derived work passes its own normal gates.
  Reopenability was a stakeholder override of the recommended
  immutable-once-concluded model.
links:
  derives-from: [SES-0086]
---

# DEC-0448: RSCH lifecycle and gating

## Context

Grilling round 1 (T5) asked when an RSCH comes into existence and whether it is gated. Grilling round 2 (T7) asked for the status lifecycle. The stakeholder (T6, T8) chose both a commissioned entry point and a post-hoc entry point, an ungated type with a reviewed close, and at T13 overrode the recommendation that a concluded RSCH be immutable.

## Decision

Research artifacts carry the statuses commissioned, in-progress, concluded, and abandoned. Two entry points exist: an investigation commissioned at intake starts at commissioned, and research that already happened is created post-hoc directly at concluded. A concluded Research artifact is reopenable: it may return to in-progress for a follow-up round, and every round is recorded in its own timestamped, append-only section — earlier rounds are never rewritten, preserving what was known at each point in time. The type is ungated; every transition to concluded is a stakeholder findings review, and all derived work passes its own normal gates.

## Rationale

Research is exploratory by nature — gating the investigation itself would slow the very activity meant to surface fast learning, while the findings-review-at-close step and normal gating on any derived work keep quality control where it belongs. Reopenability with timestamped rounds matches how real investigations resume without falsifying the historical record of an earlier round's findings.

## Alternatives Considered

A fully gated lifecycle (draft/in-refinement/gated/approved) was recommended but rejected by the stakeholder as excessive for exploratory work. Treating a concluded RSCH as immutable (mirroring accepted Decisions) was recommended but overridden at T13 in favor of reopenability.

## Implications

The checker needs a distinct lifecycle table for RSCH rather than reusing SPEC-artifact-common's gate lifecycle; append-only round sections need their own structural convention, similar in spirit to session transcripts.
