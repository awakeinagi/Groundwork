---
id: SES-0024
type: session
title: Decision-recall audit — POC, judge topology, codification; port failure semantics
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0023, CMP-0003, DEC-0111, DEC-0116, DEC-0136]
---

# SES-0024: Decision-Recall Audit

## Purpose

Building on the [SES-0023](SES-0023-dec-0080-graduation-review.md)
lesson (a relevant decision can sit unapplied), the participant
proposed a new process step: at each refinement stage, an exploratory
subagent with the facilitator's context searches for accepted decisions
relevant to the artifact under refinement but missing from
consideration, reporting findings or "nothing to add" — refined via a
throwaway POC before codification.

## Transcript

**T1 — awakeinagi.** Directed: at each stage of refinement, spawn an
exploratory subagent with the facilitator's context to consider the
artifacts being produced and search for relevant accepted decisions not
currently considered; report them or report nothing to add. "Let's
refine this process using a throwaway POC script."

**T2 — facilitator.** Built the POC (model2vec embeddings per
[DEC-0112](../decisions/DEC-0112-model2vec-static-embeddings.md),
section+item chunking per [DEC-0113](../decisions/DEC-0113-section-and-turn-chunking.md),
accepted-only with superseded redirect per [DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md))
and reported: (1) held-out benchmark — hide an artifact's citations,
ask where each real cite ranks among non-cited decisions — recall 0.46
@8 / 0.60 @15 / 0.73 @24, ~2 s per audit, absolute scores useless
(rank only); item-level chunking worth +20% relative; (2) **negative
result**: replaying [CMP-0001](../components/CMP-0001-artifact-store-service.md)
with all [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)
traces scrubbed, the decision does not surface — rule-type decisions that
govern structure have no lexical footprint in documents violating
them, so the audit complements, never replaces, the
[DEC-0136](../decisions/DEC-0136-graduation-review-required.md)
checklists; (3) end-to-end demo on
[CMP-0003](../components/CMP-0003-app-database-port.md): a fork judge
correctly reported "Nothing to add" with a defensible near-miss
analysis ([DEC-0105](../decisions/DEC-0105-sp-0002-rescoped-deferred.md)'s
provenance already carried by the cited
[DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)) — and flagged,
unprompted, that the port CMP defines no failure semantics for its
operations. Proposed: codify the step; promote the POC into the
[DEC-0116](../decisions/DEC-0116-separate-search-script-and-index.md)-designed
search script; patch the port CMP before its gate.

**T3 — awakeinagi.** Agreed to both updates; asked whether the first
subagent should pull the ~24 retrieved docs and spawn 24 parallel
agents to judge each result's relevance individually; added that
cheaper models (Haiku, Sonnet) are available for subagents.

**T4 — facilitator.** Analyzed: cost was never the objection —
calibration is. Comparative judgment over the whole list produces the
strictness that made the demo trustworthy; isolated one-candidate
judges over-flag (acquiescence bias), and cheaper models amplify that.
Parallelism buys little latency (one judge over 12 took ~49 s). Where
cheap models help: sharded batches (~8 candidates each, comparative
within batch) and cascades (cheap prune, strong final). Noted the
mechanics constraint: a fork always runs the parent's model, so a
cheap-model judge must be a fresh agent fed an explicit context
packet. Asked two questions: judge topology (recommended single strict
judge, shard at scale, never 1:1) and the port failure-semantics
package (recommended full contract: expired-lease typed error with
event still claimable; retry exhaustion to a dead-letter state, never
silently dropped; crash mid-unit-of-work leaves no partial visibility;
typed error conditions enumerated per operation).

**T5 — awakeinagi.** Ratified the topology with model assignments:
**Opus for the fork judge, Sonnet for the 8-record batch agents**; and
accepted the full failure contract for
[CMP-0003](../components/CMP-0003-app-database-port.md).

**T6 — facilitator.** Executed: promoted the POC into
`scripts/groundwork_search.py` (search / similar / audit / build) per
[DEC-0111](../decisions/DEC-0111-skill-semantic-search-duckdb-vss.md)–[DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md)
semantics — during verification found and fixed an index-refresh bug
(dedupe snapshot taken before deleting a changed file's chunks
suppressed re-insertion; an edited file collapsed from 11 chunks to 1;
round-trip now verified) — added the SKILL.md routing row, the
semantic-search reference with recipes and the audit protocol, and the
playbook step; recorded the decisions below; patched
[CMP-0003](../components/CMP-0003-app-database-port.md).

## Decisions Produced

- [DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md) —
  the decision-recall audit is a required refinement-stage step, with
  the single-judge/shard-at-scale topology and Opus/Sonnet model
  assignments
- [DEC-0138](../decisions/DEC-0138-promote-audit-into-search-script.md)
  — the POC retrieval is promoted into the skill's
  `groundwork_search.py` with recorded implementation stances
- [DEC-0139](../decisions/DEC-0139-port-operation-failure-semantics.md)
  — app database port operations carry the full failure contract

## Conflicts Raised

None.
