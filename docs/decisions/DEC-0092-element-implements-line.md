---
id: DEC-0092
type: decision
title: Every design element declares the stories it implements
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0015 @ T2-T5"
links:
  derives-from: [SES-0015]
  relates-to: [DEC-0087, DEC-0090]
---

# DEC-0092: Every design element declares the stories it implements

## Context

Design elements carry the contracts, but nothing recorded which stories'
requirements each element realizes — so "is this story fully designed?"
and any percent-complete estimate had no data to stand on.
[CMP-0001](../components/CMP-0001-artifact-store-service.md) already
named its filling stories informally in each element's Pending block;
the instinct existed without a rule. Elements deliberately have no
frontmatter ([DEC-0087](DEC-0087-parseable-element-headings.md)), so the
reference must be parseable body syntax.

## Decision

Every design element carries a mandated **`Implements:`** line directly
under its `### <ElementName> (<type>)` heading, listing one or more
stories as resolvable markdown links
(per [DEC-0090](DEC-0090-clickable-body-cross-references.md)):

```markdown
### StorageService (service)

Implements: [ST-0002](../stories/ST-0002-storage-api-core.md),
[ST-0006](../stories/ST-0006-typed-mechanical-writes.md)
```

A missing line, an empty list, or an unresolvable target is a
gate-blocker. **Implements** is glossary-fixed as *design element ⇒
story*: the element handles (part of) the implementation the story
calls for; [SPEC-story](../specs/SPEC-story.md)'s Component Impact
wording changes from "implements or modifies" to "builds or modifies"
so the word has one direction corpus-wide. Private helper values/events
list the same stories as the element they support; a graduated seam CMP
references the stories that birthed the seam. The Graph Index derives
element→story `IMPLEMENTS` edges from these lines.

## Rationale

An element no story motivates is a design smell — either the epic needs
another story or the element is speculative — mirroring the existing
rule that an acceptance criterion no decision supports means "refine
more, never invent provenance". Mandatory-with-enforcement because
[DEC-0090](DEC-0090-clickable-body-cross-references.md) demonstrated
that non-enforced conventions drift, and the completion metrics
([DEC-0095](DEC-0095-percent-complete-metrics.md)) would otherwise sit
on unreliable data. The line-under-heading placement reuses the
[DEC-0087](DEC-0087-parseable-element-headings.md) pattern: parseable
body syntax as single source of truth, no frontmatter mirror.

## Alternatives Considered

- **Per-contract-item citations** (`(per DEC-…; for ST-…)`): finest
  granularity, enables acceptance-criterion-level mapping — rejected as
  noisy on every line when most items within one element serve the same
  story.
- **Element line plus optional item-level override**: flexible but two
  syntaxes to validate and teach; not needed until a real case demands
  finer attribution.
- **Advisory only**: rejected — drifts, per the
  [DEC-0090](DEC-0090-clickable-body-cross-references.md) lesson.
- **`Realizes:` as the line name**: avoids rewording
  [SPEC-story](../specs/SPEC-story.md), but the metric story ("percent
  implemented") would no longer match the edge name.

## Implications

[SPEC-design-elements](../specs/SPEC-design-elements.md) gains the
declaration rule; [SPEC-component](../specs/SPEC-component.md) gains the
gate rule; [SPEC-story](../specs/SPEC-story.md) Component Impact is
reworded; the glossary gains **Implements**;
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s elements
gain Implements lines; the tier-2 suite
([ST-0007](../stories/ST-0007-tier2-check-suite.md)) validates presence
and resolution; `tools/check_links.py` and the skill's bundled tooling
enforce and index the line. Coverage, reciprocity, metrics, and
staleness ride this edge per
[DEC-0093](DEC-0093-story-design-coverage-check.md)–[DEC-0096](DEC-0096-implements-staleness-propagation.md).
