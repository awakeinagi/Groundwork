---
id: DEC-0435
type: decision
title: "Artifact frontmatter supports multiple approvals via an additive approvals list"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0082 @ T33-T34, T37"
overview: >-
  Artifact frontmatter gains an additive approvals list — entries
  carrying approver, date, and optional role — that legal-shapes
  today's approved-by/approved-on pair as a list of one, requiring
  no migration under the DEC-0425 evolution contract. The checker
  validates recorded approvals against governance policy. Confirmed
  by the stakeholder at SES-0082 T37, extending the T33/T34
  recommendation.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0425, DEC-0428, DEC-0263]
---

# DEC-0435: Artifact frontmatter supports multiple approvals via an additive approvals list

## Context

The single approved-by/approved-on pair in artifact frontmatter records only one approver, but governance configuration (DEC-0263) can require more than one reviewer to sign off on a gate. The frontmatter needed a shape that could record several approvals without breaking the corpus format's evolution contract (DEC-0425).

## Decision

Artifact frontmatter records approvals as a list — an `approvals:` field whose entries carry the approver, the date, and optionally the authority or role the approval exercises.

## Rationale

The change is additive under the DEC-0425 evolution contract: the legacy approved-by and approved-on pair remains valid and reads as an approvals list of one, so no existing corpus requires migration and solo mode is unaffected. The checker validates the recorded approvals against the governance policy in force.

## Alternatives Considered

Replacing approved-by/approved-on outright with the new list was rejected: it would force a migration of every already-approved artifact and break DEC-0425's backward-compatibility contract for no functional gain, since a list-of-one already expresses the legacy shape.

## Implications

Checker logic that validates approvals must read either shape (a bare approved-by/approved-on pair or a populated approvals list) and reconcile it against governance policy (DEC-0428, DEC-0263). Approver-group quorum policy (DEC-0428 lineage) consumes this list directly.
