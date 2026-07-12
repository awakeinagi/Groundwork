---
id: IDEA-0027
type: idea
title: "Fix the recall-audit packet generator's tooling defects"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Three Sonnet 5 judges auditing SP-0013..SP-0017 and DEC-0356 at
  SES-0064 T17 surfaced defects in the recall-audit packet generator
  beyond the substantive findings themselves: packets omit the
  audited artifact's own content/overview so judges evaluate blind;
  considered candidate lists are sometimes mis-copied across
  different artifacts' packets; stderr/progress output leaks into
  the JSON stream the judges parse; and a stale-graph warning
  surfaced during packet generation. Flagged for idea capture at
  session close (T17); captured now under T22's batched-capture
  selection.
links:
  derives-from: [SES-0064]
---

## The Idea

Fix four defects in the recall-audit packet generator that three Sonnet 5 judges surfaced while auditing SP-0013..SP-0017 and DEC-0356: packets omit the audited artifact's own content/overview (judges evaluate blind to what they are auditing); `considered` candidate lists are sometimes mis-copied across different artifacts' packets; stderr/progress output leaks into the JSON stream the judges parse; and a stale-graph warning surfaced during packet generation that was not otherwise investigated. A further instance was recorded at SES-0076 (2026-07-12): the judge packet for the SES-0076 audit contained only candidate IDs, titles, and matched-section labels — no artifact body, candidate bodies, or citation/provenance data — so the judge could not follow citation chains as its instructions require and judged from titles alone.

## Spark Context

Surfaced at SES-0064 T17 during the recall-audit verdict presentation, flagged there for idea capture at session close, and captured now under T22's batched-capture selection (DEC-0258).

## Disposition

Pending.
