---
id: IDEA-0046
type: idea
title: "Librarian-internal action speedups: op batching and warm per-op rechecks"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi@gmail.com
overview: >-
  Post-adoption residual of SES-0076's IDEA-0031 take-up: once
  DEC-0388's targeted-read charter and DEC-0391's concurrent-apply
  build are in use, measure remaining artifact-librarian task
  latency and evaluate internal speedups — batching related
  operations more aggressively within a task, and warming or
  incrementalizing the per-operation recheck, the same economics
  DEC-0387 demonstrated for the checker projection (eight to twenty-
  two times warm versus cold). Scoping routes through the DEC-0337
  cross-spike survey alongside IDEA-0043's checker-warming proposal.
  Captured at SES-0076.
links:
  relates-to: [IDEA-0031, IDEA-0043, DEC-0387]
  derives-from: [SES-0076]
---

# IDEA-0046: Librarian-internal action speedups: op batching and warm per-op rechecks

## The Idea

Once DEC-0388's targeted-read charter and DEC-0391's concurrent-apply build are in use, measure remaining artifact-librarian task latency and evaluate internal speedups: batching related operations more aggressively within a task, and warming or incrementalizing the per-operation recheck — the same economics DEC-0387 demonstrated for the checker projection (eight to twenty-two times warm versus cold).

## Spark Context

Surfaced at SES-0076 as the residual of IDEA-0031's take-up: DEC-0388 and DEC-0391 resolve the externally visible spawn-overhead and write-serialization costs, but do not address the librarian's own internal per-operation economics. Scoping routes through the DEC-0337 cross-spike survey alongside IDEA-0043's checker-warming proposal.

## Disposition

Pending — awaiting take-up, intended as a post-adoption measurement once DEC-0388 and DEC-0391 are in production use.
