---
id: DEC-0133
type: decision
title: Out of Scope entries that are future work must exist as deferred artifacts; boundary statements need only links
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T7-T8"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0097, DEC-0100, DEC-0109, DEC-0120]
---

# DEC-0133: Differentiated Out-of-Scope Rule

## Context

The participant asked whether Out of Scope items should be required to
exist as deferred spikes/stories so they stay tracked
([SES-0022](../sessions/SES-0022-cmp-0001-contract-refinement.md) T7).
Out of Scope entries are two species: boundary statements (behavior
that belongs elsewhere or nowhere, denied so implementers don't assume
it) and future work in disguise (wanted-later work living only as
prose).

## Decision

A differentiated rule for Out of Scope sections on stories and
component docs:

1. **Future work** — an entry meaning "we will want this later" **must
   exist as a deferred story or spike** (with a `release:` label per
   [DEC-0098](DEC-0098-semver-release-labels.md) and, when revival has
   an observable condition, a trigger subscription per
   [DEC-0109](DEC-0109-trigger-subscriptions.md)), and the entry links
   to it. Prose-only future work is a review-time smell.
2. **Boundary statements** — entries denying adjacent behavior link the
   owning artifact if one exists, or stand alone if the behavior is
   permanently out. No deferred artifact is minted; an anti-requirement
   must never sit in the backlog.

The classification is human judgment at gate review, not a mechanical
tier-2 check.

## Rationale

Blanket capture would make permanent denials ("no auto-merge of
divergence") unschedulable backlog residents polluting every trigger
review; the status quo leaves genuine future work invisible to the
status report and trigger reviews. The rule sends each species where it
is actually trackable.

## Alternatives Considered

- **Blanket requirement** — every entry gets a deferred artifact;
  rejected as backlog pollution.
- **Status quo (prose only)** — rejected; the gap the participant
  spotted is real.

## Implications

First application: [ST-0001](../stories/ST-0001-tier1-schema-suite.md)'s
schema-evolution Out of Scope line becomes
[ST-0011](../stories/ST-0011-schema-evolution-machinery.md)
(`backlog`, deferred at creation per this decision and
[DEC-0100](DEC-0100-scope-moves-cite-decisions.md)) subscribed to a new
trigger `TRG-0005` ("first post-launch artifact-spec change"), armed by
this decision. [SPEC-story](../specs/SPEC-story.md) and
[SPEC-component](../specs/SPEC-component.md) record the rule.
