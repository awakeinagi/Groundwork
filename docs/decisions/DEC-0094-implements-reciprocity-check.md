---
id: DEC-0094
type: decision
title: Implements references must agree with the story's Component Impact
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0015 @ T4-T5"
links:
  derives-from: [SES-0015]
  relates-to: [DEC-0092, DEC-0093]
---

# DEC-0094: Implements references must agree with the story's Component Impact

## Context

With [DEC-0092](DEC-0092-element-implements-line.md) there are two views
of the same relationship: the story's coarse forward declaration
(Component Impact, written at story-gate time before elements exist) and
the element's fine-grained Implements claim (written as design settles).
Unchecked, the two diverge silently and whichever a reader trusts is
sometimes wrong.

## Decision

A design element may only reference a story whose Component Impact
section links that element's Component Doc. A mismatch — an element
claiming to implement a story that does not name its CMP — is a tier-2
gate finding on the CMP and an audit finding corpus-wide. Component
Impact remains a required story section (the story-side forward
declaration); the element side is the fine-grained truth.

## Rationale

The check makes mis-attribution loud. When the element's claim is right,
the fix is a scoped story amendment updating Component Impact — exactly
the audit trail wanted when design lands somewhere unexpected.
Legitimate re-scoping now touches both sides, which is a feature:
re-scoping should be visible.

## Alternatives Considered

- **Element side authoritative, no cross-check**: simpler checker, but
  the story-side reader gets silently stale information — rejected.
- **Retire Component Impact and derive the story→CMP view from the
  Graph Index**: removes duplication but loses the story-gate-time
  declaration, which exists before any element does — rejected.

## Implications

[SPEC-story](../specs/SPEC-story.md) notes the consistency obligation;
[SPEC-design-elements](../specs/SPEC-design-elements.md) states the
constraint on Implements targets;
[ST-0007](../stories/ST-0007-tier2-check-suite.md) and
`tools/check_links.py` enforce it.
