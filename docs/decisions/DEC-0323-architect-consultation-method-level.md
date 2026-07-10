---
id: DEC-0323
type: decision
title: System-architect consultation is discretionary at method-level sessions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T6-T7"
overview: >-
  Extends DEC-0292's invocation policy to the tier it left undefined:
  method-level sessions (those refining the skills, tooling, or
  process machinery rather than a BG/EP/ST/CMP artifact). At method
  level the system-architect consultation is discretionary — the
  facilitator offers it when the session is architecture-shaped
  (tool decomposition, API surfaces, authority boundaries) and the
  stakeholder decides; declining is recorded in the transcript. Same
  stance as business-goal level; the EP/ST/CMP requirement is
  unchanged. Recorded to close a recall-audit contract gap: SES-0057
  applied exactly this rule (offered at T6, declined at T7) without
  an accepted decision backing it.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0292]
---

# DEC-0323: Architect Consultation Discretionary at Method Level

## Context

DEC-0292 defines system-architect consultation policy for BG
(discretionary) and EP/ST/CMP (required) refinement only. SES-0057 —
a method-level session on skill tooling — offered the consultation as
"discretionary" and the stakeholder declined; the recall audit
flagged that no accepted decision defined any policy for that tier.

## Decision

At method-level sessions (refining skills, tooling, or process
machinery rather than a BG/EP/ST/CMP artifact), the system-architect
consultation is discretionary: the facilitator offers it when the
session is architecture-shaped, the stakeholder decides, and the
offer and disposition are recorded in the transcript.

## Rationale

Method-level sessions vary from mechanical conventions to genuine
architecture (like SES-0057's tool decomposition); a blanket
requirement would tax the former, silence would keep the rule
improvised. Discretionary-with-recorded-offer matches the BG-level
stance for the same reason: the stakeholder is best placed to price
the consultation against the session's stakes.

## Alternatives Considered

- **Required at method level** — disproportionate for
  non-architectural process tweaks; rejected.
- **Supersede DEC-0292 with a full-tier table** — heavier change for
  the same effect; extension via a new decision suffices; rejected.
- **Leave undefined** — the gap the audit flagged persists; rejected.

## Implications

The refinement-process reference's consultation section gains the
method-level clause at the DEC-0320 cutover. SES-0057's T6/T7
handling is retroactively regular.
