---
id: DEC-0076
type: decision
title: Gate review renders a semantic diff with agent summary and impact report
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Gate sign-off renders an artifact-aware semantic diff: section-level
  before/after with changed contract items highlighted, agent
  plain-language change summary on top, impact report (staleness, affected
  parties) alongside, and provenance links for every claim. Raw text diff
  remains one click away; the PR description carries the same summary for
  host-side reviewers. Semantic rendering makes the human gate a real
  check, not a rubber stamp.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0010 @ T2-T3"
links:
  derives-from: [SES-0010]
---

# DEC-0076: Semantic gate diff + agent summary

## Context

Gate sign-off is PR approval (DEC-0032),
but a Product Owner re-affirming a changed goal cannot be handed a raw
markdown diff.

## Decision

The gate surface renders an artifact-aware diff: section-level rendered
before/after with changed contract items highlighted, the agent's
plain-language change summary on top, the impact report (what goes stale,
who is affected) alongside, and provenance links for every changed claim.
A raw text diff remains one click away for technical reviewers, and the
PR description carries the same agent summary so host-side reviewers see
it too.

## Rationale

Approval quality is bounded by comprehension; the semantic rendering makes
the human gate a real check rather than a rubber stamp, for exactly the
audience DEC-0032 exists to serve.

## Alternatives Considered

- **Rendered side-by-side only**: small changes hide in large documents.
- **Raw diff default**: hostile to business approvers.

## Implications

Change summaries are agent-generated at PR open/update (a strategy-pack
duty); summary faithfulness is eval-covered
(DEC-0058); the impact report comes from
the gate engine's analysis (DEC-0038).
