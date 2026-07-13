---
id: DEC-0485
type: decision
title: "Concurrency contract split: single-session invariants ratified; multi-session semantics deferred to SP-0018"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T6-T11"
overview: >-
  The verified single-session write-path model needed a ruling on
  whether it becomes the Engine's contracted concurrency model,
  alongside SP-0018's pending multi-session work. This decision
  ratifies the single-session invariants (if-match optimistic
  conflict detection, refusal over merge, atomic recoverable
  batches) as the contracted base, while deferring multi-session
  semantics (parallel sessions, worktree isolation, merge policy) to
  SP-0018's findings.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0391, DEC-0411, DEC-0412, DEC-0413, DEC-0414, DEC-0415, DEC-0416, SP-0018, DEC-0486]
---

# DEC-0485: Concurrency contract split: single-session invariants ratified; multi-session semantics deferred to SP-0018

## Context

The verified write-path model needed a ruling on whether it becomes the contracted concurrency model, and the stakeholder asked whether SP-0018's pending work should settle the question instead.

## Decision

The single-session write-path invariants — per-artifact optimistic conflict detection via if-match tokens, refusal rather than merge on collision, and atomic multi-op batches recoverable to pre-batch state — are ratified as the Engine's contracted concurrency invariant model. Multi-session semantics, covering parallel sessions, worktree isolation, and merge policy, are explicitly deferred to SP-0018's findings.

## Rationale

SP-0018 is chartered as the worktree-scale counterpart of the single-session write model — it presumes these invariants and explores the layer above them — so ratifying the base unblocks EP-0015's entitlements without pre-empting the spike.

## Alternatives Considered

Deferring the entire contract to SP-0018 was rejected because the spike's question is narrower than the base model it presumes, leaving verified guarantees uncontracted. Ratifying multi-session semantics now was rejected as pre-empting a chartered spike.

## Implications

EP-0015 designs against the ratified invariants; token format, lock granularity, and worktree layering stay component-level; SP-0018's findings extend rather than replace the contracted base.
