---
id: DEC-0383
type: decision
title: "accepted-in: the ratification site of a later-accepted decision is stamped by set-status accepted --session"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T17-T18"
overview: >-
  The set-status accepted transition on a decision requires --session SES-nnnn and
  stamps accepted-in on the decision, making "where was this
  proposed decision ratified" graph-queryable without a new link
  type. Decisions created accepted in their originating session need
  nothing — derives-from already says it. Documented in SPEC-
  decision. Resolves the stakeholder's open-now-resolve-later
  question (T17): precise semantics live on the decision (derives-
  from = born, accepted-in = ratified); sessions carry one generic
  relates-to mirror.
links:
  relates-to: [DEC-0382]
  derives-from: [SES-0072]
---

# DEC-0383: accepted-in: the ratification site of a later-accepted decision is stamped by set-status accepted --session

## Context

DEC-0369..0373 sit proposed awaiting later ratification; prior to this the ratifying session was prose-only.

## Decision

Require --session on decision acceptance and stamp accepted-in.

## Rationale

A scalar field on the decision is the cheapest precise encoding; no reciprocity machinery, no vocabulary change.

## Alternatives Considered

Dedicated resolves/resolved-by links (heavy); prose-only (not queryable).

## Implications

Acceptance tasks must name the ratifying session.
