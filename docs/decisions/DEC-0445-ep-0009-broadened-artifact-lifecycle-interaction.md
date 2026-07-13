---
id: DEC-0445
type: decision
title: "EP-0009 broadened: Artifact Lifecycle & Interaction"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0085 T19, T21, T22"
overview: >-
  EP-0009 is renamed Artifact Lifecycle & Interaction and broadened
  from the artifact-interaction-surface framing to the dynamic
  domain of Groundwork artifacts — creation, editing, evolution,
  governance, and data capture, including where interactions happen,
  who performs them, and how. The static design of artifact types
  and their scoping stays with the anticipated Artifact model epic
  (DEC-0443), giving a dynamic-versus-static seam. EP-0009's
  contracted deliverables — the artifact-librarian agent and the
  artifact-interact skill (DEC-0339) — are unchanged. The detailed
  re-scope is grilled at EP-0009's own refinement session, not in
  SES-0085.
links:
  derives-from: [SES-0085]
  relates-to: [EP-0009, DEC-0339, DEC-0441, DEC-0443]
---

# DEC-0445: EP-0009 broadened: Artifact Lifecycle & Interaction

## Context

SES-0085 T18 presented EP-0009's four before/after amendment lines under the narrower artifact-interaction-surface framing (the epic governing the artifact-librarian agent and the artifact-interact skill) and asked whether to apply and re-affirm. The stakeholder (T19) instead asked to broaden the epic's focus to general interaction with Groundwork artifacts — creation, editing, evolution, governance, data capture, where those interactions happen, who performs them, and how — and asked for help with the terminology.

## Decision

EP-0009 is renamed Artifact Lifecycle & Interaction and broadened from the artifact-interaction-surface framing to the dynamic domain of Groundwork artifacts: their creation, editing, evolution, governance interactions, and data capture, including where those interactions happen, who performs them, and how. The static design of artifact types and their scoping remains with the anticipated Artifact model epic (per DEC-0443), giving a dynamic-versus-static seam between the two. EP-0009's current contracted deliverables — the artifact-librarian agent and the artifact-interact skill (per DEC-0339) — are unchanged by the broadening. The detailed re-scope (interaction loci, actor and mode inventories, any new stories) is grilled at EP-0009's own refinement session from the work queue, not in SES-0085.

## Rationale

T21 proposed that the domain the stakeholder described is the artifact lifecycle (creation, editing, evolution, governance) combined with the interaction model (actors, loci, modes) — "surface" named only the tooling seam and undersold the broader scope. Flagging the boundary against DEC-0443's anticipated Artifact model epic keeps EP-0009 on the dynamic side (operations on artifacts through their lifecycle) versus that epic's static type/schema design, giving a clean seam between the two rather than an overlapping one.

## Alternatives Considered

T21 offered a depth choice: fully re-scope EP-0009 in SES-0085 now (interaction loci, actor and mode inventories, new stories) versus recharter the framing lines now and grill the detailed re-scope at EP-0009's own refinement session. T22 selected the lighter, recommended option — "Recharter lines now, grill later (Recommended)" — over the full re-scope, alongside selecting the recommended new epic name, "Artifact Lifecycle & Interaction (Recommended)", over the other offered naming options.

## Implications

The static design of artifact types and their scoping is out of scope for the broadened EP-0009 and belongs instead to DEC-0443's anticipated Artifact model epic. EP-0009's contracted deliverables — the artifact-librarian agent and the artifact-interact skill (DEC-0339) — carry forward unchanged. The detailed re-scope work (interaction loci, actor and mode inventories, any new stories) is deferred to EP-0009's own refinement session from the work queue rather than performed inside SES-0085.
