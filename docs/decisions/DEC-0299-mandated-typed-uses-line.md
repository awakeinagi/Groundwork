---
id: DEC-0299
type: decision
title: Mandated Uses. line — every element declares typed dependencies (interface | implementation | test)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7, T16-T17"
overview: >-
  Every design element carries a Uses: line (mirroring Implements:)
  declaring each dependency on another element as a named contract
  item with an edge-type qualifier from the closed set
  interface | implementation | test. interface = non-serializing (the
  consumer builds against stubs generated from the referenced
  contract items, which ship in its bundle); implementation =
  serializing (requires the built artifact; the only edge type
  constraining build-order tiers); test = test-execution only. The
  store validates Uses: targets and edge types at write time
  (tier-2); the graph derives the typed element DAG. Adopted with
  three types over the facilitator's defer-test recommendation; test
  doubles therefore become owned elements per DEC-0306. Edge
  projection to component level is DEC-0309.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0081, DEC-0297, DEC-0306, DEC-0309]
---

# DEC-0299: Mandated Typed `Uses:` Line

## Context

Elements' sibling dependencies exist today only in contract prose
(CMP-0001: StorageService.A-2 runs SchemaValidator.A-1;
BranchOrchestrator.A-1 allocates via IdAllocator). An element-grain
build-order is underivable without declared edges, and undifferentiated
edges would either serialize everything or under-order.

## Decision

Every design element carries a mandated **`Uses:` line** declaring
each dependency on another element as a named contract item with an
edge-type qualifier from the closed set:

- **`(interface)`** — contract-only; non-serializing; the consumer
  builds against stubs generated from the referenced items, which
  ship in its work-package bundle. Default when omitted.
- **`(implementation)`** — requires the built artifact; the only
  edge type that constrains build-order tiers.
- **`(test)`** — needed only at test execution.

Example:
`Uses: SchemaValidator.A-1 (interface), ItemBranch.B-2 (implementation), LocalGitFakeConnector (test)`

The store validates targets and qualifiers at write time (tier-2);
the graph derives the typed element DAG.

## Rationale

"Atomic" means no *unspecified* dependencies; typed edges keep
interface coupling from manufacturing false serialization
(API-first, stub-from-spec practice — already CMP-0001's own
implementation guidance).

## Alternatives Considered

- **Untyped Uses:** — serializes interface deps or under-orders;
  rejected.
- **Two types now, test deferred** (facilitator recommendation) —
  stakeholder chose three to keep fixture dependencies owned and
  visible; DEC-0306 settles double ownership.
- **Mining prose for edges** — unreliable; rejected.

## Implications

SPEC-design-elements gains the Uses: syntax; all 53 existing elements
need retrofit (queued follow-on); check_links and the product's
tier-2 checks enforce resolution (DEC-0309); closed qualifier set
extensible only by decision.
