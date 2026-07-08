---
id: DEC-0158
type: decision
title: An identifier co-occurrence audit over code-span tokens is required at decision distillation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0027 @ T1-T3"
links:
  derives-from: [SES-0027]
  relates-to: [DEC-0137, DEC-0157]
---

# DEC-0158: The Identifier Co-Occurrence Audit

## Context

The [SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md)
incident was findable lexically: the cancelled operation's name
appeared verbatim in the artifacts that still enumerated it. Contract
identifiers in code spans — operation names, field names, config paths
— are quasi-formal symbols, and exact-token overlap is higher-precision
evidence of contract coupling than embedding similarity.

## Decision

Immediately after new decisions are distilled, the facilitator runs the
consistency tool's `terms` on each
(`groundwork_consistency.py terms`): extract the new DEC's code-span
identifiers, and report every ratified artifact sharing a **rare**
identifier (document frequency ≤ 6 by default), flagging pairs with no
direct frontmatter link. Matching is by **containment**, not equality —
`jira-status` joins `set-jira-status` — because the incident joined on
containment. Session transcripts are excluded from the index (they
mention everything). Hits are reviewed in-session with recorded
dispositions.

## Rationale

Exact-identifier joins complement the embedding audit
([DEC-0137](DEC-0137-decision-recall-audit-step.md)): embeddings find
conceptual overlap, identifier joins find contract overlap, and
contract overlap is what bites. Replayed on the incident, the tool
flags [ST-0006](../stories/ST-0006-typed-mechanical-writes.md) and
[CMP-0001](../components/CMP-0001-artifact-store-service.md) from
[DEC-0151](DEC-0151-workflow-telemetry-projection-side.md) — and its
first live run additionally surfaced
[DEC-0130](DEC-0130-mechanical-ops-shared-allowlist.md)'s enumeration
of the cancelled operation, which the semantic audit had missed.

## Alternatives Considered

- **Exact-match tokens only** — misses the incident (`jira-status` vs
  `set-jira-status` never join).
- **Full lexical index with stemming/BM25** — heavier machinery for
  marginal gain over containment on quasi-formal identifiers.
- **Contract items as graph nodes** — the structural upgrade; deferred
  to [SP-0007](../spikes/SP-0007-contract-item-graph-nodes.md)
  ([DEC-0160](DEC-0160-sp-0007-item-nodes-spike.md)).

## Implications

Ships in `scripts/groundwork_consistency.py` alongside the sweep
([DEC-0157](DEC-0157-relates-to-sweep-at-distillation.md)); the skill
docs carry the step. Design input for the product's session agent when
[EP-0002](../epics/EP-0002-refinement-session-agent.md) derives
stories.
