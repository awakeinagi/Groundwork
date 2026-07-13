---
id: DEC-0513
type: decision
title: "Governance rules prefer false positives over false negatives"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: SES-0094 @ T15-T16
overview: >-
  When a governance rule is uncertain whether an artifact violates
  an obligation, it reports rather than stays silent: governance
  rules prefer false positives over false negatives. Context:
  EP-0014's gate-prep reviewer consultation (SES-0094) found the
  epic stated no quality goals, and this correctness bias was the
  one item needing a fresh stakeholder decision. Rationale: under
  the check-time, report-only posture (DEC-0509), an over-report
  costs a moment of review, while a missed violation is an
  ungoverned capability persisting invisibly — the failure DEC-0442
  exists to prevent. Rejected alternatives: reporting only high-
  confidence findings (the silent-failure direction is the dangerous
  one); deferring the bias to per-rule story refinement (story teams
  need a named epic-level expectation, and per-family biases would
  drift). Implications: EP-0014's quality-goals statement names this
  bias; if continuous enforcement is later adopted, the story that
  builds it inherits this bias explicitly.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0509, DEC-0442]
---

# DEC-0513: Governance rules prefer false positives over false negatives

## Context

The gate-prep reviewer consultation found EP-0014 stated no epic-level quality goals, and the correctness trade-off — which failure direction a governance rule prefers when uncertain — was the one item requiring a fresh stakeholder decision rather than a restatement of existing ones.

## Decision

When a governance rule is uncertain whether an artifact violates an obligation, it reports: governance rules prefer false positives over false negatives.

## Rationale

Under the check-time, report-only posture (DEC-0509) a report never blocks work, so an over-report costs a moment of review, while a missed violation is an ungoverned capability persisting invisibly — the exact failure DEC-0442 exists to prevent.

## Alternatives Considered

Reporting only high-confidence findings was rejected because the silent failure direction is the dangerous one for a governance system. Deferring the bias to per-rule story refinement was rejected because story teams need a named epic-level expectation to write acceptance criteria against, and per-family biases would drift inconsistently.

## Implications

EP-0014's quality-goals statement names this bias. If continuous enforcement is later adopted (the question DEC-0509 defers to story level), noise management escalates and that story inherits this bias explicitly.
