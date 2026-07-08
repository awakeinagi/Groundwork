---
id: DEC-0203
type: decision
title: Queue and KV-store extend the Port family to six
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0038 @ T2"
links:
  derives-from: [SES-0038]
  relates-to: [DEC-0121, DEC-0204, DEC-0205, DEC-0135]
  supersedes: []
---

# DEC-0203: Queue and KV-Store Extend the Port Family to Six

## Context

[DEC-0121](DEC-0121-infrastructure-ports.md) named "four infrastructure
ports." Refining [EP-0008](../epics/EP-0008-backend-application-platform.md)'s
async/background execution model and inter-process coordination needs
surfaced two more swappable infrastructure seams. Nothing about the
original four changes — this narrows/extends
[DEC-0121](DEC-0121-infrastructure-ports.md) without superseding it, the
exact case
[DEC-0157](DEC-0157-relates-to-sweep-at-distillation.md)'s relates-to
sweep exists for.

## Decision

Two additional Ports join the family, bringing the total to six: app
database, vector store, embedding, graph store
([DEC-0121](DEC-0121-infrastructure-ports.md), unchanged), plus
**Queue** and **KV-store**. This decision `relates-to`
[DEC-0121](DEC-0121-infrastructure-ports.md) rather than superseding it.

**Queue Port**: background/async job execution — enqueue, consume,
acknowledge, retry.

**KV-store Port**: scope is **ephemeral coordination state** (rate
limiting, single-writer coordination locks, connection/session
bookkeeping) as the baseline use case, extended to also support
**general-purpose caching** (e.g. avoiding recomputation of graph query
results). Further use cases beyond these two are tracked by a deferred
spike ([SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md))
rather than scoped now.

## Rationale

Both are genuine swappable infrastructure capabilities — exactly what a
Port seam is for (per [DEC-0121](DEC-0121-infrastructure-ports.md)'s own
definition) — not engine-specific
logic. Scoping KV-store's baseline narrowly (coordination state) while
explicitly supporting the caching extension avoids either
under-specifying the contract or overreaching into every conceivable
future use at once.

## Alternatives Considered

- **Supersede [DEC-0121](DEC-0121-infrastructure-ports.md) with a new
  "six ports" decision**: rejected — the
  original four are unchanged in every respect; superseding would force
  a staleness walk over every artifact that cites
  [DEC-0121](DEC-0121-infrastructure-ports.md)
  ([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md),
  [EP-0004](../epics/EP-0004-graph-index.md),
  [EP-0007](../epics/EP-0007-consolidation-memory-layer.md),
  [CMP-0003](../components/CMP-0003-app-database-port.md)) for no
  reason — nothing in their content is wrong or now contradicted.
- **Scope KV-store to coordination state only, no caching**: rejected —
  the caching use case is concrete and near-term enough
  ([EP-0004](../epics/EP-0004-graph-index.md)'s query results are an
  obvious candidate) to design the contract against now rather than
  extend it again immediately after gating.

## Implications

[CONTEXT.md](../../CONTEXT.md)'s Port glossary entry updated to six
ports; a Composition Root term added. Consistency sweep run against
[DEC-0121](DEC-0121-infrastructure-ports.md)'s citers per
[DEC-0157](DEC-0157-relates-to-sweep-at-distillation.md). The Queue Port
and KV-store Port each
graduate to a standalone `protocol`-type CMP at component-derivation
time, following [DEC-0135](DEC-0135-graduate-app-database-port.md)'s
established pattern — the same conformance-testability reasoning that
applied to the original four ports applies here without modification.
