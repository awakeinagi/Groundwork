---
id: IDEA-0051
type: idea
title: "Indexer boilerplate dedupe silently drops decision chunks from the audit candidate pool"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: Claude Fable 5 (facilitator), capture sanctioned by the stakeholder-approved SES-0077 design package
overview: >-
  The semantic index's boilerplate dedupe (DEC-0119) skips any chunk
  whose body hash is already indexed, so a decision section
  textually identical to an earlier chunk can never surface as a
  recall-audit candidate, a silent recall gap in the very pool the
  audit ranks. A future session should weigh scoping the dedupe per
  artifact, exempting decision chunks, or accepting and documenting
  the gap.
links:
  derives-from: [SES-0077]
---

# IDEA-0051: Indexer boilerplate dedupe silently drops decision chunks from the audit candidate pool

## The Idea

The semantic index's boilerplate dedupe (DEC-0119) skips any chunk whose body hash is already indexed, so a decision section textually identical to an earlier chunk can never surface as a recall-audit candidate, a silent recall gap in the very pool the audit ranks. A future session should weigh scoping the dedupe per artifact, exempting decision chunks, or accepting and documenting the gap.

## Spark Context

Surfaced by SES-0077's packet-generator reconnaissance for the IDEA-0027 take-up.

## Disposition

Pending.

