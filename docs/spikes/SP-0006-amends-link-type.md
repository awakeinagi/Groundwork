---
id: SP-0006
type: spike
title: An amends link type for partial supersession — semantics, checker, migration
status: draft
owner: eng-lead
created: 2026-07-08
timebox: 2d
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  relates-to: [EP-0001, SP-0007]
cites: [DEC-0157, DEC-0159]
---

# SP-0006: The `amends` Link Type

> Opened by [DEC-0159](../decisions/DEC-0159-sp-0006-amends-link-spike.md)
> after the [SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md)
> incident: [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)
> partially cancelled
> [DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)
> and (found by the new tooling's first live run)
> [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)'s
> operation enumeration, with no typed edge the staleness walk could
> see.

## Question

Should the closed link vocabulary gain an `amends` (or `narrows`) link
type for decisions that cancel *part* of an accepted decision — and if
so, with what semantics? Specifically: does an `amends` edge stale the
amended decision's citers the way `supersedes` does (all citers? only
citers of the amended aspect — and can that even be expressed at
decision granularity?); what does the checker enforce (resolvability,
decision-to-decision only, acyclicity?); how do the graph tool's
`impact`/`trace` incorporate it; and do existing narrowing decisions
(the [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)
cases) migrate — or does the
[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)
sweep already cover the need at acceptable review cost, making the
vocabulary change unjustified?

## Why It Blocks

Nothing is hard-blocked — the sweep is the operating mitigation. But
every narrowing decision recorded before this is answered accrues as
un-typed, sweep-dependent debt, and the answer changes the artifact
spec ([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)'s
format engine validates link vocabulary), so it should land before the
format-engine contract hardens further.

## Method

Enumerate the narrowing decisions in this corpus (the tool's `sweep`
output over all accepted DECs with `relates-to` on accepted DECs);
prototype the edge in the skill's graph tool on a branch of this
corpus; run `impact` with and without `amends` participating in
staleness; draft the checker rule and spec diff; compare total review
burden (sweep-only vs. edge-plus-sweep) on the corpus's real history.
Findings become decisions, including "sweep is enough, no new edge."

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — a completed spike produces at least one decision, even
"assumption confirmed, no change."
