---
id: DEC-0423
type: decision
title: "Paradigm logic is single-sourced in one engine"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T18, T21, T31"
accepted-in: SES-0082
overview: >-
  All paradigm mechanics (artifact model/validation, ID allocation,
  gate state, locking, integrity checking, graph sync, governance
  evaluation, format parsing) live in exactly one engine; gw CLI and
  any application backend are thin in-process adapters. Library
  extraction happens at the first non-CLI consumer, not before, with
  no epic opened ahead of that trigger.
links:
  derives-from: [SES-0082]
  relates-to: [EP-0009, DEC-0346, BG-0001, BG-0002, DEC-0315, DEC-0310]
---

# DEC-0423: Paradigm logic is single-sourced in one engine

## Context

Two independently briefed system-architect instances converged on a four-component decomposition for avoiding duplicated paradigm logic between the gw CLI and any future application backend. SES-0082 needed to ratify the target shape and, critically, decide when the extraction actually happens rather than leaving it as permanent aspiration.

## Decision

All paradigm mechanics — artifact model and validation, ID allocation, gate state, locking, integrity checking, graph synchronization, governance evaluation, and format parsing/serialization — exist in exactly one engine. The target shape is a library with the gw CLI and the application backend as thin in-process adapters; no surface may reimplement paradigm logic. Library extraction is performed when the first non-CLI consumer is built, not before, and no epic is opened for it until that trigger fires.

## Rationale

Single-sourcing paradigm logic is the only way to guarantee the parity DEC-N (skill-mode as core subset, application as superset) depends on: if the CLI and the application each implemented gate rules independently, they would drift. Deferring the actual extraction until a second consumer exists avoids speculative work — a library with one caller is indistinguishable from the CLI itself, so there is nothing to gain by extracting early, and real cost in maintaining an abstraction boundary nobody yet needs.

## Alternatives Considered

Extracting the engine now, ahead of the application, was rejected as premature: EP-0009's artifact interaction surface already serves the only consumer that exists. Allowing the application backend to reimplement paradigm rules independently (with periodic reconciliation) was rejected outright — it reintroduces exactly the drift risk this decision exists to prevent.

## Implications

No epic is opened for library extraction as part of this decision; DEC-0346's implementation-swap precedent governs when that work is chartered — at the first non-CLI consumer. Until then, gw_write.py and its sibling scripts remain the de facto single implementation, and any application-backend prototype work must not duplicate their logic rather than wait for extraction.
