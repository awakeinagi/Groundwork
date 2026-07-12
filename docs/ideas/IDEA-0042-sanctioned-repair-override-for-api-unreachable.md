---
id: IDEA-0042
type: idea
title: "Sanctioned-repair override for API-unreachable surfaces (closed-session bodies, frontmatter fields, body H1s)"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  SES-0072's recall audit (DEC-0312 finding) showed that sanctioned
  repairs on three API-unreachable surfaces -- closed-session
  bodies, frontmatter fields on existing artifacts, and body H1s --
  currently force operator-sanctioned freehand edits that violate
  DEC-0312's letter, exactly the out-of-band pattern DEC-0377 closed
  for section structure. Proposal to grill in a future session: an
  explicit sanctioned-repair mechanism (e.g. a --sanctioned-by SES-
  nnnn override on edit ops) that pierces immutability while
  recording the sanction in the operation itself, keeping repairs
  in-API and auditable. Core trade-off to weigh: any immutability
  override weakens the guarantee it pierces.
links:
  derives-from: [SES-0072]
---

# IDEA-0042: Sanctioned-repair override for API-unreachable surfaces (closed-session bodies, frontmatter fields, body H1s)

## The Idea

SES-0072's recall audit (DEC-0312 finding) showed that sanctioned repairs on three API-unreachable surfaces — closed-session bodies, frontmatter fields on existing artifacts, and body H1s — currently force operator-sanctioned freehand edits that violate DEC-0312's letter, exactly the out-of-band pattern DEC-0377 closed for section structure. Proposal to grill in a future session: an explicit sanctioned-repair mechanism (e.g. a --sanctioned-by SES-nnnn override on edit ops) that pierces immutability while recording the sanction in the operation itself, keeping repairs in-API and auditable. Core trade-off to weigh: any immutability override weakens the guarantee it pierces.

## Spark Context

Raised by the facilitator from the SES-0072 recall-audit judge's DEC-0312 finding; the stakeholder directed its capture at the session's inspired-ideas check.

## Disposition

Pending.
