# SPEC: Story (ST)

An implementable unit of work derived from an approved Epic. Stories are where
requirements become testable: every acceptance criterion cites the Decision
that established it.

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: story
jira-key: PROJ-456
release: "1.2"        # optional target release; absent = current release
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
4. **Out of Scope** — adjacent work explicitly excluded. Entries are two
   species with different obligations
   ([DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)):
   an entry that is *future work* ("wanted later") must exist as a
   deferred story or spike and be linked from the entry — prose-only
   future work is a review-time smell; a *boundary statement* (behavior
   that belongs elsewhere or nowhere) links the owning artifact if one
   exists and never mints a deferred artifact. Classification is human
   judgment at gate review.
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
- **Release scoping** (see
  [SPEC-artifact-common](SPEC-artifact-common.md) § Release scoping): a
  story targeted at anything other than a current release is `deferred`
  ([DEC-0097](../decisions/DEC-0097-deferred-status.md)) and carries a
  `release:` label
  ([DEC-0098](../decisions/DEC-0098-semver-release-labels.md)); its
  parent epic's label is the default. Deferral and revival each cite a
  Decision ([DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md));
  revival lands at `draft`. Deferred stories are excluded from design-%
  rollups and coverage warnings and surface in the deferred report
  ([DEC-0101](../decisions/DEC-0101-deferred-out-of-metrics.md)).
