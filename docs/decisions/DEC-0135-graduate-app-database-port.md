---
id: DEC-0135
type: decision
title: AppDatabasePort graduates to a standalone protocol-type component; all infrastructure ports follow this pattern
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0023 @ T2-T3"
links:
  derives-from: [SES-0023]
  relates-to: [DEC-0080, DEC-0121, DEC-0122, DEC-0129]
---

# DEC-0135: AppDatabasePort Graduation and the Port-CMP Pattern

## Context

[DEC-0080](DEC-0080-hybrid-component-granularity.md)'s second
graduation criterion is independently versioned conformance. Every
port carries a conformance suite any adapter must pass
([DEC-0122](DEC-0122-config-selected-adapters.md)) — adapter authors
are conformance implementers who need the port contract without the
consuming component's internals.

## Decision

The `AppDatabasePort` element graduates to
[CMP-0003](../components/CMP-0003-app-database-port.md), a standalone
CMP with `component-type: protocol`, owned by the Canonical Store
context ([DEC-0121](DEC-0121-infrastructure-ports.md) ownership
unchanged). It carries the typed operation families
([DEC-0129](DEC-0129-port-typed-operation-families.md)) and the
conformance expectations;
[CMP-0001](../components/CMP-0001-artifact-store-service.md) becomes a
consumer via `depends-on`. **Pattern**: the remaining infrastructure
ports (vector store, embedding, graph store) likewise arrive as
standalone `protocol`-type CMPs in their owning contexts when
[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
derive them.

## Rationale

The conformance criterion holds today, not hypothetically; and one
uniform pattern across all four ports spares two future epics the same
deliberation.

## Alternatives Considered

- **Keep nested until a second adapter ships** — the [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) graduation
  path would then re-open an approved store doc to extract the seam it
  needs.
