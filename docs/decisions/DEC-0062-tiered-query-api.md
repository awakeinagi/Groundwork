---
id: DEC-0062
type: decision
title: "Three query tiers: named traversals, bounded primitive, guarded openCypher"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T3-T5"
links:
  derives-from: [SES-0007]
---

# DEC-0062: Tiered query API with guarded openCypher

## Context

Consumers range from fixed shapes (trace-to-goal for the UI, build-order
for manifests) through agent on-demand exploration
([DEC-0056](DEC-0056-context-recipes-in-packs.md)) to power-user analysis —
and the sponsor wants an advanced query language available — while the
engine must stay swappable.

## Decision

Three tiers. **Named traversals** (the stable contract): trace-to-goal,
subtree/descendants, impact-neighborhood, cited-by, conflict-neighborhood,
build-order. **Bounded generic primitive**: start set, edge types,
direction, depth limit, view — the mid-session agent tool. **Advanced
endpoint**: read-only **openCypher** with depth/time/result-size guards and
a required view parameter. openCypher is chosen over raw engine passthrough
because it is an engine-independent standard (Neo4j, KuzuDB, Memgraph,
Apache AGE) — the advanced tier constrains the engine choice
([DEC-0061](DEC-0061-engine-via-spike.md)) instead of the engine
constraining the contract.

## Rationale

Each consumer gets the least-power interface that serves it; full
expressiveness exists without marrying an engine or opening a
resource-exhaustion surface.

## Alternatives Considered

- **GraphQL as the advanced tier**: engine-agnostic and UI-friendly, but
  variable-depth path queries fight its shape.
- **Named traversals only**: agent exploration outgrows any fixed list.

## Implications

openCypher support is a hard SP-0002 criterion; guard limits are
deployment configuration; GraphQL remains a possible future convenience
layer for EP-0006, not a commitment.
