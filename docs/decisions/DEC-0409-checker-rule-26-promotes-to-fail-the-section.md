---
id: DEC-0409
type: decision
title: "Checker rule 26 promotes to FAIL — the section skeleton is a hard corpus-wide guarantee"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0078 @ T6-T7
overview: >-
  DEC-0407 set checker rule 26 (required-section presence) to WARN
  pending repair of thirty-six legacy offenders queued as IDEA-0052.
  SES-0078 executed those repairs under the DEC-0408 convention
  across the DEC-0121 and DEC-0214-0225 decision clusters, eight
  closed sessions, CMP-0006, and SP-0012. With the backlog clear,
  this decision promotes rule 26 to FAIL severity corpus-wide,
  making the section skeleton a hard, self-maintaining guarantee
  alongside DEC-0407's create-time refusals.
links:
  derives-from: [SES-0078]
  relates-to: [DEC-0407, DEC-0408]
---

# DEC-0409: Checker rule 26 promotes to FAIL — the section skeleton is a hard corpus-wide guarantee

## Context

DEC-0407 established checker rule 26 (required-section presence per artifact type) at WARN severity, deferring promotion to FAIL until the thirty-six legacy offenders found by its rollout sweep were repaired under their own queued take-up (IDEA-0052). SES-0078 executed those repairs under the DEC-0408 convention: fourteen decisions in the DEC-0121 cluster gained transcript-derived Implications sections, the twelve decisions DEC-0214 through DEC-0225 gained transcript-derived Alternatives Considered and Implications sections, eight closed sessions gained Purpose and/or Conflicts Raised sections with transcript turns untouched, CMP-0006's seven placeholder headings were normalized to canonical headings, and SP-0012's Decisions Produced heading was renamed to Resulting Decisions.

## Decision

Checker rule 26 enforces required-section presence at FAIL severity corpus-wide. The section skeleton is a hard guarantee: the checker refuses a corpus in which any artifact lacks a required top-level section, so such a state can no longer pass the pre-commit gate. The tools copy of the checker stays byte-identical-synced with the skill's canonical copy.

## Rationale

With zero offenders remaining after the SES-0078 repairs, WARN severity would only allow new structural drift to accumulate silently; FAIL makes the skeleton guarantee self-maintaining alongside DEC-0407's create-time refusals, which remain the first line of defense while the checker is the backstop.

## Alternatives Considered

Keeping rule 26 at WARN until IDEA-0042's in-API sanctioned-repair mechanism ships was considered and rejected because the backlog is clear now and continued deferral would invite exactly the drift the rule exists to prevent.

## Implications

Any future artifact missing a required top-level section blocks the pre-commit checker until repaired. A legacy gap discovered later requires an operator-sanctioned repair citing DEC-0408. Verification at SES-0078 close: the full checker reports 648 artifacts sound with zero rule-26 findings, and a scratch-copy negative test confirmed a stripped section fails.
