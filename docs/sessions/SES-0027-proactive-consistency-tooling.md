---
id: SES-0027
type: session
title: Proactive consistency tooling — relates-to sweep, identifier co-occurrence, two spikes
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0026, SP-0006, SP-0007]
---

# SES-0027: Proactive Consistency Tooling

## Purpose

Turn the [SES-0026](SES-0026-ep-0005-story-derivation.md) audit
incident — [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)
partially cancelling
[DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)
while two approved artifacts kept enumerating the cancelled operation —
into systematic prevention: decide which graph operations catch this
class proactively, ship the cheap ones, spike the structural ones.

## Transcript

**T1 — Sponsor.** With the [EP-0005](../epics/EP-0005-connectors-and-identity.md)
gate bundle pending: what graph
operations/algorithms could we have used to proactively identify the
issue the audit found?

**T2 — Agent.** Analysis: the existing `impact` algorithm (reverse
`cites`/`derives-from` walk) already computes the right set — it never
fired because [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)
is a *partial supersession*: it narrows
[DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)
via `relates-to`, and the staleness walk keys on `supersedes` alone —
a modeling gap, not an algorithm gap. Four options, in ascending cost:
(1) treat `relates-to` on accepted decisions as a sweep trigger — a
1-hop reverse-cites review list at distillation time, zero new
machinery; (2) an `amends`/`narrows` link type so the existing walk
sees partial supersession — a closed-vocabulary spec change; (3) an
identifier co-occurrence index over code-span tokens — exact-match
contract overlap (the incident was findable lexically) complementing
the embedding audit; (4) contract-item-level graph nodes with per-item
citation edges — item-precise sweeps. Also noted the upstream
tension-detection case is the deferred
[ST-0009](../stories/ST-0009-hybrid-search-capabilities.md)
unlinked-neighbor audit, for which this incident is a demand data
point. Recommended #1 now, #3 as best-value tooling, #2 as a
future session question.

**T3 — Sponsor.** Directive, upgrading the recommendation: build
tooling for **#1 and #3 now** and assign both to the relevant
decision-refinement events; open **spikes for #2 and #4**.

**T4 — Agent (synthesis).** Shipped
`scripts/groundwork_consistency.py` in the skill (pure stdlib):
`sweep` ([DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md))
and `terms`
([DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md)),
both assigned as required steps immediately after decision
distillation (SKILL.md + refinement-process reference updated).
Validated by replaying the incident: `sweep DEC-0151` flags
[ST-0006](../stories/ST-0006-typed-mechanical-writes.md),
[CMP-0001](../components/CMP-0001-artifact-store-service.md), and
[EP-0005](../epics/EP-0005-connectors-and-identity.md) in one hop;
`terms DEC-0151` initially missed because `jira-status` and
`set-jira-status` are different exact tokens — matching was changed to
**containment**, after which both artifacts surface. First live run
also caught a miss the semantic audit never flagged:
[DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)'s
Decision text enumerates the cancelled `set-jira-status`. Disposition:
no artifact edit — accepted decisions are immutable and the enumeration
is historically correct; the live contracts are already amended, and
the [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)↔[DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)
relationship is recorded here and discoverable by the tool — a second
instance of the partial-supersession blind spot, strengthening
[SP-0006](../spikes/SP-0006-amends-link-type.md)'s case. Opened
[SP-0006](../spikes/SP-0006-amends-link-type.md) (amends link type,
2d, per [DEC-0159](../decisions/DEC-0159-sp-0006-amends-link-spike.md))
and [SP-0007](../spikes/SP-0007-contract-item-graph-nodes.md)
(contract-item graph nodes, 3d, per
[DEC-0160](../decisions/DEC-0160-sp-0007-item-nodes-spike.md)), both
process-level, deriving from [BG-0001](../goals/BG-0001-groundwork.md).
Ran the new tool on its own decisions
([DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)–[DEC-0160](../decisions/DEC-0160-sp-0007-item-nodes-spike.md)):
sweep clean; terms hits reviewed — all conscious references (these
decisions name the incident's identifiers by design), no action.

## Decisions Produced

[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md),
[DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md),
[DEC-0159](../decisions/DEC-0159-sp-0006-amends-link-spike.md),
[DEC-0160](../decisions/DEC-0160-sp-0007-item-nodes-spike.md)

## Conflicts Raised

None.
