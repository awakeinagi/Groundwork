---
id: IDEA-0025
type: idea
title: "Backfill typed Uses: lines across the approved CMPs and arm checker enforcement"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  SP-0013's projection found zero typed Uses: lines anywhere across
  the 16 approved CMPs despite the DEC-0299/DEC-0306/DEC-0309
  mandate -- a SPEC-mandated mechanism the corpus never carried,
  predating and never backfilled after the mandate, with
  tools/check_links.py not flagging the absence. Proposes
  backfilling Uses: lines across all 16 CMPs and arming checker
  enforcement in the same take-up. This is a modification of
  approved artifacts, so take-up must run the full DEC-0267 cascade
  (superseding/amending decisions, staleness walk, re-affirmation)
  before close. Blocks SP-0014 per DEC-0358, which made this
  backfill's completion the explicit precondition for SP-0014's
  execution.
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0299, DEC-0306, DEC-0309, SP-0014, DEC-0358]
---

## The Idea

Backfill the mandated `Uses:` line (DEC-0299, extended to test doubles by DEC-0306, projected to component `depends-on` by DEC-0309) across all 16 approved Component Docs, where SP-0013's projection found zero instances despite the mandate having been SPEC-mandated since DEC-0299/DEC-0306/DEC-0309. Arm `tools/check_links.py` to enforce the mandate going forward -- it currently does not flag the absence, which is an enforcement gap to close in the same take-up as the backfill itself.

## Spark Context

Raised at SES-0064 T21-T22: SP-0013's executed findings surfaced the `Uses:`-line absence as a central negative finding, and the stakeholder's T22 disposition made this backfill's take-up and completion the explicit precondition for SP-0014's execution (DEC-0358) -- SP-0014 is blocked on this idea's take-up.

## Disposition

Taken up at SES-0066. The corpus-wide backfill executed (DEC-0359) -- 71
typed Uses: edges across 53 elements in the 15 conforming CMPs, 20 explicit
Uses: none -- and checker enforcement was armed (DEC-0360, rule 20). The
DEC-0267 amendment cascade ran in-session: the four extraction escalations
were recorded as decisions (DEC-0361..DEC-0364) and the batched
re-affirmation of the 15 modified approved CMPs completed before close.
SP-0014's DEC-0358 precondition is satisfied (DEC-0365).

