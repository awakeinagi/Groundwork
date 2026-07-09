---
id: IDEA-0008
type: idea
title: Scenario-form quality goals and release annotations on BG-0001
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-09
proposed-by: awakeinagi@gmail.com
overview: >-
  Captured from SES-0055 findings 7 and 8 (MINOR, ratified at T7).
  Finding 7: quality attributes across all eight epics are adjectives
  ("instant staleness", "read-your-writes", "budget-bounded"), not
  scenario-form requirements with SLI/SLO and measurement points —
  define 3–5 prioritized scenario-form quality goals at BG level
  before remaining story gates close. Finding 8 (editorial): BG-0001's
  outcomes read as v1 promises but outcomes 2 and 5 land post-v1
  (DEC-0067, DEC-0148) — annotate each outcome with the release that
  first demonstrates it. Take-up grilling resumes at the goal set
  (SES-0055 T8 recommendation on record: five provisional goals —
  session turn round-trip p95 ≤ 2s excl. LLM inference; gate-check
  computation ≤ 30s from PR event; graph/index rebuild ≤ 60s at 10k
  artifacts; read-your-writes overlay staleness ≤ 1s; zero loss of
  ratified artifacts). Amends the approved BG-0001 (gated,
  editorial + additive); largely independent of the SES-0055 T9
  atom-model proposal.
links:
  derives-from: [SES-0055]
  relates-to: [BG-0001, DEC-0067, DEC-0148]
---

# IDEA-0008: BG-0001 Quality Goals & Release Annotations

## The Idea

Execute SES-0055 findings 7 and 8 (ratified accepts): set 3–5
scenario-form quality goals at BG level (stimulus + response measure +
measurement point) and annotate BG-0001's outcomes with their
first-demonstrating release.

## Spark Context

Surfaced by the SES-0055 dual-architect review (independent instance
finding 6; record-grounded instance finding 9; both co-signed).
Grilling on the goal set began at SES-0055 T8 (five provisional goals
recommended, Low-tier) and was paused by the T9 atom-model proposal.
Resume at the goal set; the numbers are provisional until the
IDEA-0007 metrics stories can validate them.

## Disposition

Pending.
