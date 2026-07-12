---
id: DEC-0385
type: decision
title: "IDEA-0028 is absorbed into IDEA-0041's take-up"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T3-T4"
overview: >-
  IDEA-0028 (edit-section hardening + duplicate-section checker gap
  + body-only docs note) described the same root defect as IDEA-0041
  with two additions; both are resolved by this session's decisions
  — the duplicate-Design-Elements parsing loophole closes via
  checker rule 21 (DEC-0379), and the body-only payload contract is
  enforced (DEC-0376) and documented in the skill. Both ideas are
  dispositioned taken-up by SES-0072 rather than worked as separate
  sessions.
links:
  derives-from: [SES-0072]
---

# DEC-0385: IDEA-0028 is absorbed into IDEA-0041's take-up

## Context

Two captured ideas covered one defect; working them separately would re-tread the same ground.

## Decision

Fold IDEA-0028 into this take-up; disposition both ideas taken-up citing this session's decisions.

## Rationale

Same root cause, overlapping proposed fixes, one coherent design.

## Alternatives Considered

A separate later session (duplicated effort); partial fold (splitting one defect's fixes across sessions).

## Implications

The idea queue drops from 33 to 31 captured items.
