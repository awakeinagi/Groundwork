# SPEC: Story (ST)

An implementable unit of work derived from an approved Epic. Stories are where
requirements become testable: every acceptance criterion cites the Decision
that established it.

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: story
jira-key: PROJ-456
links:
  derives-from: [EP-....]
  satisfies: [BG-....]
  depends-on: [CMP-...., ST-....]   # components consumed, ordering deps
```

## Required body sections

1. **Summary** — the change, its user/beneficiary, and the value; projected
   to Jira.
2. **Acceptance Criteria** — numbered, individually testable. Each criterion
   ends with a citation: `(per DEC-....)`. A criterion no Decision supports is
   a signal to refine further, not to invent provenance.
3. **Component Impact** — which Component Docs this story builds or
   modifies; contract sections affected. This is the story-side forward
   declaration: as design settles, elements in those CMPs back-reference
   the story via `Implements:` lines, and an element may only reference
   a story whose Component Impact links its CMP
   ([DEC-0092](../decisions/DEC-0092-element-implements-line.md),
   [DEC-0094](../decisions/DEC-0094-implements-reciprocity-check.md)).
4. **Out of Scope** — adjacent work explicitly excluded.
5. **Notes for Implementers** — constraints, gotchas, links to relevant
   Consolidations. Optional context, never a substitute for contracts.

## Rules

- Derivable only from an `approved` Epic.
- A story whose `depends-on` includes a non-`approved` Component Doc cannot
  pass its gate.
- Jira projection follows the same summary-plus-link rule as Epics
  ([DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)).
- Amending or superseding an approved story marks every Component Doc
  with a referencing element stale, element-scoped
  ([DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md)).
  A story's design and implementation percent-complete are computed over
  the elements referencing it
  ([DEC-0095](../decisions/DEC-0095-percent-complete-metrics.md)).
