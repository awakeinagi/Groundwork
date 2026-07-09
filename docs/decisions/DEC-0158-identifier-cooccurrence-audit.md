---
id: DEC-0158
type: decision
title: An identifier co-occurrence audit over code-span tokens is required at decision distillation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  After new decisions are distilled, facilitator runs consistency
  tool's terms command: extract new DEC's code-span identifiers and
  report every ratified artifact sharing a rare identifier
  (frequency ≤ 6 by default), flagging pairs with no direct link.
  Matching by containment (jira-status joins set-jira-status). Session
  transcripts excluded. Hits reviewed with recorded dispositions.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0027 @ T1-T3"
links:
  derives-from: [SES-0027]
  relates-to: [DEC-0137, DEC-0157]
---

# DEC-0158: The Identifier Co-Occurrence Audit

## Context

The SES-0026
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
(DEC-0137): embeddings find
conceptual overlap, identifier joins find contract overlap, and
contract overlap is what bites. Replayed on the incident, the tool
flags ST-0006 and
CMP-0001 from
DEC-0151 — and its
first live run additionally surfaced
DEC-0130's enumeration
of the cancelled operation, which the semantic audit had missed.

## Alternatives Considered

- **Exact-match tokens only** — misses the incident (`jira-status` vs
  `set-jira-status` never join).
- **Full lexical index with stemming/BM25** — heavier machinery for
  marginal gain over containment on quasi-formal identifiers.
- **Contract items as graph nodes** — the structural upgrade; deferred
  to SP-0007
  (DEC-0160).

## Implications

Ships in `scripts/groundwork_consistency.py` alongside the sweep
(DEC-0157); the skill
docs carry the step. Design input for the product's session agent when
EP-0002 derives
stories.
