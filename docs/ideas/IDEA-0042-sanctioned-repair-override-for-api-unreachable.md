---
id: IDEA-0042
type: idea
title: "Sanctioned-repair override for API-unreachable surfaces (closed-session bodies, frontmatter fields, body H1s)"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  SES-0072's recall audit (DEC-0312 finding) showed that sanctioned repairs
  on three API-unreachable surfaces -- closed-session bodies, frontmatter
  fields on existing artifacts, and body H1s -- currently force
  operator-sanctioned freehand edits that violate DEC-0312's letter, exactly
  the out-of-band pattern DEC-0377 closed for section structure. Proposal to
  grill in a future session: an explicit sanctioned-repair mechanism (e.g. a
  --sanctioned-by SES-nnnn override on edit ops) that pierces immutability
  while recording the sanction in the operation itself, keeping repairs
  in-API and auditable. Core trade-off to weigh: any immutability override
  weakens the guarantee it pierces. Amended 2026-07-12 (SES-0074,
  operator-approved) with a fourth surface: creating a missing required
  top-level body section, since no write op creates a new top-level section
  and the historical append-turn workaround is now refused by the DEC-0376
  heading guard. Supporting evidence for urgency: SES-0072 needed six
  operator-sanctioned direct edits across these surfaces, and SES-0073's
  close deadlocked on the frontmatter-fields surface until a facilitator
  direct edit resolved it. Status remains captured, pending a future
  grilling session.
links:
  relates-to: [SES-0074]
  derives-from: [SES-0072]
---

# IDEA-0042: Sanctioned-repair override for API-unreachable surfaces (closed-session bodies, frontmatter fields, body H1s)

## The Idea

SES-0072's recall audit (DEC-0312 finding) showed that sanctioned repairs on three API-unreachable surfaces — closed-session bodies, frontmatter fields on existing artifacts, and body H1s — currently force operator-sanctioned freehand edits that violate DEC-0312's letter, exactly the out-of-band pattern DEC-0377 closed for section structure. Proposal to grill in a future session: an explicit sanctioned-repair mechanism (e.g. a --sanctioned-by SES-nnnn override on edit ops) that pierces immutability while recording the sanction in the operation itself, keeping repairs in-API and auditable. Core trade-off to weigh: any immutability override weakens the guarantee it pierces.

Fourth surface (added 2026-07-12, SES-0074): creating a missing required top-level body section. No write op creates a new top-level section — edit-section requires an existing heading match, and the historical workaround (append-turn content opening with the new heading) is now refused by the DEC-0376 heading guard. Supporting evidence for the idea's urgency accumulated the same day: SES-0072 required six operator-sanctioned direct edits across these surfaces, and SES-0073's close deadlocked on the frontmatter-fields surface until an operator-sanctioned facilitator direct edit resolved it.

## Spark Context

Raised by the facilitator from the SES-0072 recall-audit judge's DEC-0312 finding; the stakeholder directed its capture at the session's inspired-ideas check.

## Disposition

Pending.

Amended 2026-07-12 (SES-0074) to add a fourth API-unreachable surface (creating a missing required top-level body section), per operator approval.

Evidence note (2026-07-12, SES-0078): this session repeated the freehand operator-sanctioned direct-edit stopgap across thirty-six further artifacts (the rule-26 legacy-skeleton repair, IDEA-0052), the same pattern SES-0072 and SES-0073 hit — further strengthening the case for bringing sanctioned repairs in-API.

