---
id: DEC-0403
type: decision
title: "A remove-cite operation extends the write surface"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T10-T11"
overview: >-
  The DEC-0313 v1 operation set has no cite-removal path, leaving
  dead-cite repairs API-unreachable, IDEA-0047, surfaced by
  SES-0076's DEC-0267 cascade. An eleventh operation, remove-cite,
  joins the set following the DEC-0377 extension precedent. It
  refuses when the target is absent from cites, when code-stripped
  body prose still references the decision, or on immutable
  artifacts, accepted decisions and closed sessions; approved or
  stale artifacts require --amend. Batch-key support and operations-
  doc updates ship with the operation. A generic remove-from-list
  operation was deliberately not built; it joins the queue as a
  follow-up Idea. Decided at SES-0077.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0313, DEC-0377, DEC-0247, IDEA-0047, IDEA-0035]
---
# DEC-0403: A remove-cite operation extends the write surface

## Context

The DEC-0313 v1 operation set has no cite-removal path, leaving dead-cite repairs API-unreachable — IDEA-0047, surfaced by SES-0076's DEC-0267 cascade.

## Decision

An eleventh operation, `remove-cite`, joins the write API's operation set, following the DEC-0377 extension precedent. It refuses when the target is absent from the artifact's cites, when code-stripped body prose still references the decision (removal would mint a missing-cite violation), and on immutable artifacts — accepted decisions and closed sessions; approved or stale artifacts require `--amend`. Batch-key support and operations-doc updates ship together with the operation.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

A generic remove-from-list operation was deliberately not built as part of this decision; it joins the queue as a follow-up Idea instead.

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
