---
id: DEC-0247
type: decision
title: Frontmatter cites and body prose stay synchronized in both directions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  For business goals, epics, stories, spikes, and components, both
  directions are blocking: dead cites (DECs in cites: not in body prose)
  and missing cites (DECs in prose but not in cites: or frontmatter
  links). cites: becomes the complete machine-readable considered set,
  per DEC-0242's notation. Sessions and decisions exempt (sessions use
  DEC-0250; decisions use relates-to). Remediation applied per instance:
  genuine governance adds citation; structural governs add provenance
  note; cruft drops; missing cites added.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T4-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0242, DEC-0248]
---

# DEC-0247: Cites and Body Prose Stay Synchronized

## Context

A reciprocity sweep found ~66 dead cites (a frontmatter `cites:` DEC
never referenced in body prose) and 110 reverse instances (a DEC
referenced in prose but absent from `cites:`) across ~70 artifacts.
Since every contract line and acceptance criterion carries its
`(per DEC)` citation in prose, a dead cite means frontmatter cruft or
missing provenance in the text; a missing cite means the
machine-readable considered set understates what the artifact actually
rests on. The stakeholder ruled missing provenance a first-class
problem.

## Decision

For business goals, epics, stories, spikes, and components, both
directions are blocking checker violations:

1. **Dead cite** — a DEC in `cites:` that appears nowhere in body
   prose (code spans excluded, per DEC-0242's notation).
2. **Missing cite** — a DEC referenced in body prose that is in
   neither `cites:` nor a frontmatter link.

`cites:` thereby becomes the complete, machine-readable considered
set — the same set the decision-recall audit already assumes.
Sessions and decisions are exempt from this rule (sessions have their
own mention rule, DEC-0250; decisions reference each other narratively
via `relates-to`).

Remediation dispositions, applied per instance:

- the DEC genuinely governs content → add the `(per DEC)` citation at
  the governed line;
- the DEC governs the artifact's *structure or template* (e.g.
  BG-0001's DEC-0192..0194) → add a one-line provenance note;
- genuine cruft → drop the cite;
- missing cite → add the DEC to `cites:` (enrichment per DEC-0248);
- dead cite on a **superseded** DEC the artifact genuinely rested on →
  the prose gains the mention with its supersession noted; the cite is
  re-pointed only through the staleness/re-affirmation path, never
  mechanically.

## Rationale

Provenance is the product: an implementer must be able to trust that
`cites:` is exactly the decision set behind the document. The
existing conventions were already strong (82–97% dead-cite-free);
enforcement locks in what practice already intended. Blocking (rather
than warning-first) was chosen because 66+ standing warnings would
drown the signal, and remediation happens in the adopting session.

## Alternatives Considered

- **Warning first, blocking later**: lower immediate effort, but the
  backlog persists and the signal drowns.
- **Dead-cite direction only**: leaves the considered set incomplete —
  the recall audit would keep silently compensating by folding inline
  references in.

## Implications

~176 remediation items across ~70 artifacts, executed in the adopting
session under DEC-0248's enrichment sanction. `check_links.py` (both
copies) gains the two-direction rule; the graph's `gaps` audit mirrors
it (DEC-0251).
