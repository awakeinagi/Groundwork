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
3. **Component Impact** — which Component Docs this story implements or
   modifies; contract sections affected.
4. **Out of Scope** — adjacent work explicitly excluded.
5. **Notes for Implementers** — constraints, gotchas, links to relevant
   Consolidations. Optional context, never a substitute for contracts.

## Rules

- Derivable only from an `approved` Epic.
- A story whose `depends-on` includes a non-`approved` Component Doc cannot
  pass its gate.
- Jira projection follows the same summary-plus-link rule as Epics
  ([DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)).
