---
id: DEC-0457
type: decision
title: "RSCH is subject to the cites-sync check"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  Research artifacts are subject to the DEC-0247 cites-sync check
  exactly as business goals, epics, stories, spikes, and components
  are: any decision mentioned in a Research artifact's body prose
  must appear in its cites frontmatter, and every cited decision
  must appear in body prose. Raised at the SES-0086 recall-audit
  review, where the facilitator recommended a session-style
  exemption; the stakeholder overrode it, favoring the same
  bidirectional discipline already applied to design-tree types,
  since RSCH findings are meant to be cited and trusted going
  forward rather than treated as transcript narration.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0247]
---

# DEC-0457: RSCH is subject to the cites-sync check

## Context

The SES-0086 recall-audit review (T16) surfaced an open decision: whether Research artifacts fall under DEC-0247's cites-sync check, which today binds business goals, epics, stories, spikes, and components, but exempts sessions and decisions. The facilitator recommended a session-style exemption, reasoning that a Research artifact's body prose narrates an investigation rather than governing derived work the way a design-tree artifact's prose does. The stakeholder (T17) overrode that recommendation.

## Decision

Research artifacts are subject to the DEC-0247 cites-sync check exactly as business goals, epics, stories, spikes, and components are: any decision mentioned in a Research artifact's body prose must appear in its `cites:` frontmatter, and every cited decision must appear in body prose.

## Rationale

Research artifacts accumulate decision-relevant findings and reasoning over multiple rounds, the same way a design-tree artifact's prose accretes governing citations over its refinement. Holding RSCH to the same bidirectional discipline keeps `cites:` a trustworthy machine-readable considered set corpus-wide, rather than carving out a growing exception class every time a new artifact type narrates decisions in prose.

## Alternatives Considered

A session-style exemption (RSCH treated like sessions and decisions, with no cites-sync obligation) was recommended by the facilitator on the theory that research narration is closer to a session transcript than to a governed design artifact. The stakeholder rejected this: unlike a session's turn-by-turn record, an RSCH's findings and applicability sections are meant to be cited and trusted going forward, which calls for the same discipline as the design-tree types.

## Implications

The checker's cites-sync rule (DEC-0247) must add `research` to its governed-type set alongside business-goal, epic, story, spike, and component. RSCH bodies that narrate a decision by ID now require a matching `cites:`/`add-cite`, and existing or future RSCH artifacts need the same reconciliation sweep already applied to the other governed types.
