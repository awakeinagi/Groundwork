---
id: DEC-0061
type: decision
title: The graph engine is selected by spike SP-0002, with openCypher support required
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T2-T5"
links:
  derives-from: [SES-0007]
---

# DEC-0061: Engine selection via SP-0002

## Context

The engine choice was deferred at SES-0001 and again at EP-0004's drafting.
The deployment reality — self-hosted enterprise
([DEC-0050](DEC-0050-bitbucket-datacenter-v1.md)) — makes operational
burden a first-class criterion, and the advanced query decision
([DEC-0062](DEC-0062-tiered-query-api.md)) adds a language constraint.

## Decision

A timeboxed spike ([SP-0002](../spikes/SP-0002-graph-engine-selection.md))
prototypes the query contract against candidates — embedded graph
(KuzuDB), Postgres with Apache AGE / recursive CTEs, and a dedicated graph
DB (Neo4j) — on the real bootstrap graph plus synthetic scale. Criteria:
openCypher support (hard requirement), overlay/view support, traversal
ergonomics, rebuild speed, multi-node story, and on-prem ops burden.
Findings become Decisions per [DEC-0023](DEC-0023-spike-findings-become-decisions.md).

## Rationale

Every candidate is plausible; guessing bakes an unvalidated choice into a
load-bearing spot — exactly what spikes exist to prevent.

## Alternatives Considered

- **Postgres now**: probably sufficient, but overlay semantics unverified.
- **Embedded now**: multi-node deployment story unresolved.

## Implications

EP-0004 stories that depend on engine specifics block on SP-0002; the
query-tier contract ([DEC-0062](DEC-0062-tiered-query-api.md)) is designed
engine-neutral so contract work proceeds in parallel.
