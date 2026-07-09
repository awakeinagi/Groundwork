---
id: DEC-0248
type: decision
title: Cross-reference enrichment of immutable artifacts is sanctioned
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Extending DEC-0091: cross-reference enrichment of ratified or closed
  artifacts is sanctioned—adding bare-ID mentions, cites: entries, or
  frontmatter links that surface already-existing relationships. Never
  alters recorded meaning, never triggers staleness or re-gating. In
  closed sessions, body-side enrichment lands in a dated Post-Close
  Enrichment subsection appended at the bottom of the Transcript
  (testimony itself never edited). Enables remediation for DEC-0246,
  DEC-0247, DEC-0249, and DEC-0250.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T6-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0091]
---

# DEC-0248: Cross-Reference Enrichment Is Sanctioned

## Context

Fixing the reciprocity gaps requires touching ratified artifacts and
closed sessions: adding missing `cites:` entries, derived-work
entries, and body mentions of already-linked artifacts. The
provenance invariants say accepted decisions are immutable and closed
sessions are append-only. DEC-0091 already sanctioned formatting-only
edits to immutable artifacts (under which DEC-0243 de-linkified the
whole corpus). The stakeholder's framing: "Is editing
cross-references in a closed document really a violation? As long as
we're not changing the content, I see it more as data enrichment."

## Decision

Extending DEC-0091's principle: **cross-reference enrichment** of
ratified or closed artifacts is sanctioned — adding bare-ID mentions,
`cites:` entries, or frontmatter link entries that surface
*already-existing* relationships. Enrichment never alters recorded
meaning, never rewrites what was said or decided, and does not
trigger staleness, re-affirmation, or re-gating.

In closed sessions, body-side enrichment lands in a dated
**Post-Close Enrichment** subsection appended at the bottom of the
Transcript section (`### Post-Close Enrichment` with dated, cited
entries). Transcript turns themselves are never edited — the turn
record is testimony, and stays faithful to what was said.

## Rationale

The append-only invariant protects the *testimony property* — that
the record reflects what participants actually said and decided. A
bare-ID mention of a relationship the frontmatter already records
adds navigability and provenance visibility without touching that
property. Restricting session enrichment to an appended, dated
subsection keeps even the enrichment itself auditable.

## Alternatives Considered

- **Enrichment inside transcript turns**: maximal placement freedom,
  but weakens the testimony property for marginal gain.
- **Frontmatter-only enrichment**: would leave closed-session bodies
  unfixable, forcing the session mention rule (DEC-0250) to be
  forward-only and leaving SES-0040..SES-0044 permanently
  non-compliant.

## Implications

Enables the remediation sweep for DEC-0246, DEC-0247, DEC-0249, and
DEC-0250 without staleness cascades. The session template gains the
Post-Close Enrichment form; AGENTS.md and the process reference
document the sanction's boundary (relationship must already exist in
frontmatter or in the artifact graph — enrichment never *creates*
relationships, only surfaces them).
