---
id: DEC-0400
type: decision
title: "Batches pre-validate wholly and refuse entirely on any invalid op"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T8-T9"
overview: >-
  The batch namespace builder had silently dropped CLI-style link
  strings, surfaced at SES-0067, and written unrecognized rel keys
  verbatim into frontmatter, two opposite failures both unreported
  (IDEA-0034). write apply now validates every operation in a batch
  before applying any: unknown op-spec keys, rel keys outside the
  closed link vocabulary, and unknown op names each refuse the whole
  batch, naming the offending op and key. Nothing applies on a
  validation failure. Skip-and-report was rejected as reintroducing
  partial application. Decided at SES-0077, paired with the failure-
  accounting decision.
links:
  derives-from: [SES-0077]
  relates-to: [IDEA-0034, DEC-0401]
---
# DEC-0400: Batches pre-validate wholly and refuse entirely on any invalid op

## Context

The batch namespace builder had been silently dropping CLI-style link strings (surfaced at SES-0067) and writing unrecognized rel keys verbatim into frontmatter, two opposite failure modes that both went unreported.

## Decision

`write apply` now validates every operation in a batch before applying any of them: unknown op-spec keys, rel keys outside the closed link vocabulary, and unknown op names each refuse the whole batch, with a message naming the offending op and key. Nothing applies when validation fails.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

Skip-and-report was considered and rejected as an alternative, since it would reintroduce the same partial-application problem the pre-validation is meant to close.

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
