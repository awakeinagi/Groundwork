---
id: DEC-0407
type: decision
title: "Create enforces the section skeleton and ratified-status creates run the structural gate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0077 @ T15-T18
overview: >-
  Nineteen decisions after DEC-0387 shipped structurally malformed
  because create never validated caller-supplied bodies against the
  type's required sections, and creating directly at a ratifying
  status bypassed the DEC-0378 structural gate. This decision closes
  both gaps: create now refuses a caller-supplied body missing
  required sections (SPEC-optional sections exempt), and a ratified-
  status create runs the same duplicate-heading/placeholder gate as
  set-status. Checker rule 26 enforces section presence corpus-wide
  at WARN, deferred to FAIL pending repair of thirty-six legacy
  artifacts found by the rollout sweep. The nineteen malformed
  decisions were repaired under the SES-0077 T17 sanction.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0378, DEC-0402, DEC-0315]
---

# DEC-0407: Create enforces the section skeleton and ratified-status creates run the structural gate

## Context

Nineteen decisions after DEC-0387 shipped structurally malformed because create never validated that a caller-supplied body carries the type's required sections, creating directly at a ratifying status bypassed the DEC-0378 structural gate, and no checker rule enforced section presence. The stakeholder surfaced the malformation at SES-0077 T15.

## Decision

The create operation refuses any caller-supplied body missing the artifact type's required top-level sections, with SPEC-optional sections exempt (a story's Notes for Implementers). Creating an artifact directly at a ratifying status runs the same duplicate-sibling-heading and placeholder gate as a set-status transition to that status. Checker rule 26 enforces required-section presence corpus-wide at WARN severity; the rollout sweep found thirty-six legacy artifacts beyond the nineteen sanctioned repairs, so promotion to FAIL is deferred until the legacy drift is repaired under its own queued take-up.

## Rationale

The template path always satisfied the skeleton by construction; only caller-supplied bodies could bypass it, and creating directly at accepted status was an unguarded side door into ratified content. Closing both at create time keeps the recheck and the pre-commit checker as backstops rather than the only line.

## Alternatives Considered

Enforcing the skeleton only at ratifying statuses was considered and rejected because drafts missing their skeleton surprise later edit-section calls just as badly; the template exists precisely so no body starts sectionless.

## Implications

The nineteen malformed decisions DEC-0388 through DEC-0406 were repaired under the T17 sanction in the same session. Legacy structural drift elsewhere in the corpus (twenty-six older decisions missing trailing sections, eight sessions, one component stub, one spike) remains WARN-reported by rule 26 pending its queued repair.
