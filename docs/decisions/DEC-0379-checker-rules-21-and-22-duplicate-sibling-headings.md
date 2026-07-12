---
id: DEC-0379
type: decision
title: "Checker rules 21 and 22: duplicate sibling headings flagged in all artifacts, placeholder text in ratified artifacts only"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T13-T14"
overview: >-
  Checker rule 21 (check_links.py) errors on any artifact whose body repeats a
  same-level heading under one parent (the phantom-heading
  signature; also closes IDEA-0028's first-Design-Elements-only
  parsing loophole by flagging duplicated Design Elements sections);
  rule 22 errors on standalone TBD/TODO/FIXME lines and unallocated
  ID placeholders, but only in approved/accepted/closed artifacts,
  preserving the draft-early stub workflow.
links:
  relates-to: [DEC-0315, DEC-0378]
  derives-from: [SES-0072]
---

# DEC-0379: Checker rules 21 and 22: duplicate sibling headings flagged in all artifacts, placeholder text in ratified artifacts only

## Context

Duplicate headings and placeholders were invisible to the integrity suite — the gap that let SP-0015 and five other instances ship.

## Decision

Rule 21 scans every artifact; rule 22 scans ratified artifacts only.

## Rationale

A duplicate sibling heading is structurally wrong at any lifecycle stage; placeholder stubs are the sanctioned drafting workflow and only become defects at ratification.

## Alternatives Considered

Both rules ratified-only (drafts carry corruption silently until gating); both everywhere (breaks stub drafting).

## Implications

The corpus-wide sweep these rules ran found and fixed six previously unknown shipped instances in this session.
