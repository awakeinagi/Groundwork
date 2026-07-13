---
id: DEC-0496
type: decision
title: "Two-tier validation split"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Research validation follows SPEC-idea's two-tier pattern per
  DEC-0269. Tier 1, refused by the write API: a missing
  commissioned-by, source-mode, or derives-from at create; invalid
  source-mode or status values; any release field or TRIGGERS
  subscription; and a missing required-section skeleton at create.
  Tier 2, flagged by the checker: subfile/index correspondence;
  round numbering and dating; [Sn] and goal-reference resolution;
  finding-identifier uniqueness and round-prefix match; inspired-
  by/inspired reciprocity; Derived Work matching the inspired list;
  cites-sync per DEC-0457; and bare-ID resolution inside subfiles
  per DEC-0456.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0269, DEC-0456, DEC-0457, DEC-0475]
---

# DEC-0496: Two-tier validation split

## Context

Research validation needs to distinguish checks that can and must
refuse a write outright from checks that require completed,
cross-file, or cross-artifact context and so can only run at commit
time — the same distinction SPEC-idea already draws via DEC-0269.

## Decision

Research validation follows SPEC-idea's two-tier pattern per
DEC-0269. Tier 1, refused by the write API: a missing commissioned-by,
source-mode, or derives-from at create; invalid source-mode or status
values; any release field or TRIGGERS subscription; and a missing
required-section skeleton at create. Tier 2, flagged by the checker:
the subfile directory and the Subtopic Files index matching both ways;
round numbering gapless and dates non-decreasing; [Sn] citations and
goal references resolving; finding-identifier uniqueness and
round-prefix match; inspired-by and inspired reciprocity; the Derived
Work section matching the inspired list both ways under the rule-18
pattern; cites-sync per DEC-0457; and bare-ID resolution inside
subfiles per DEC-0456.

## Rationale

Every tier-1 check is decidable from the payload alone and must never
be wrong even mid-work, so it belongs at the write boundary; every
tier-2 check requires either completed round content, another
artifact's state, or the filesystem, and would incorrectly refuse
legitimate mid-round saves if pushed into tier 1 — exactly the
distinction DEC-0269 already established for Idea and now extends to
Research.

## Alternatives Considered

A single-tier all-at-commit validation model was considered and
rejected: it would let structurally invalid Research artifacts exist
on disk between creation and the first checker run. Pushing
completeness checks (round numbering, citation resolution) into tier
1 was considered and rejected as unworkable against in-progress,
legitimately incomplete rounds.

## Implications

check_links.py gains the enumerated tier-2 rules for type=research;
the write API's create/edit paths gain the enumerated tier-1 refusals.
