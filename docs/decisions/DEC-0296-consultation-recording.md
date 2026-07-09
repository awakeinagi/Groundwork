---
id: DEC-0296
type: decision
title: System-architect consultations enter session records as attributed transcript turns with inline dispositions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0054 @ T5-T8"
overview: >-
  Both consultation moments (advisor and pre-gate reviewer, DEC-0292)
  enter the session record as ordinary transcript turns: the
  facilitator summarizes the debate outcome (DEC-0293) in a turn
  explicitly attributed to the system-architect consultation, and the
  stakeholder's responses in subsequent turns are the dispositions.
  Proposals adopted into artifacts are ratified by the stakeholder
  like any other session input; no separate findings protocol, no
  session attachments. Chosen over a formal audit-style findings list
  (stronger trail, more ceremony per gate) and over saving full
  consultation packets (maximum fidelity, corpus bloat) — matching how
  research results and audit findings already flow through sessions.
links:
  derives-from: [SES-0054]
  relates-to: [DEC-0292, DEC-0293]
---

# DEC-0296: Consultation Recording Rule

## Context

DEC-0292's consultations produce analysis that shapes artifacts, so
provenance must show which design input came from the specialist
agent and what the stakeholder did with it — without inventing new
record machinery.

## Decision

Both consultation moments enter the session record as **ordinary
transcript turns**:

- the facilitator summarizes the consultation outcome (the DEC-0293
  debate verdict or documented disagreement) in a turn **explicitly
  attributed** to the system-architect consultation;
- the stakeholder's responses in subsequent turns **are the
  dispositions** — no separate findings list or per-item protocol;
- proposals adopted into artifacts are ratified by the stakeholder
  like any other session input.

No consultation packets or full outputs are stored as session
attachments.

## Rationale

This is exactly how research results and recall-audit findings
already flow through sessions — attribution preserves provenance
while adding no new machinery or corpus bloat.

## Alternatives Considered

- **Formal findings protocol for the review pass** — stronger audit
  trail, more ceremony at every gate; rejected.
- **Consultation packet as session attachment** — maximum fidelity but
  grows the corpus with large derived documents; rejected.
- **Unattributed absorption into facilitator recommendations** —
  rejected: provenance of specialist input would be lost.

## Implications

Session records at EP/ST/CMP gain at least two attributed
consultation turns per artifact (advisor and reviewer moments,
DEC-0292). Decisions distilled from consulted sessions cite those
turns via their source spans, so specialist provenance survives into
the decision layer without new frontmatter or record machinery.
