---
id: DEC-0135
type: decision
title: AppDatabasePort graduates to a standalone protocol-type component; all infrastructure ports follow this pattern
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  AppDatabasePort element graduates to CMP-0003, a standalone CMP with
  component-type: protocol, owned by Canonical Store context. It carries
  typed operation families and conformance expectations; CMP-0001 becomes
  consumer via depends-on. Pattern: remaining infrastructure ports (vector
  store, embedding, graph store) likewise arrive as standalone protocol-type
  CMPs in their owning contexts when EP-0004/EP-0007 derive them.
  Conformance criterion holds today; one uniform pattern across all four
  ports spares future epics the same deliberation.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0023 @ T2-T3"
links:
  derives-from: [SES-0023]
  relates-to: [DEC-0080, DEC-0121, DEC-0122, DEC-0129]
---

# DEC-0135: AppDatabasePort Graduation and the Port-CMP Pattern

## Context

DEC-0080's second
graduation criterion is independently versioned conformance. Every
port carries a conformance suite any adapter must pass
(DEC-0122) — adapter authors
are conformance implementers who need the port contract without the
consuming component's internals.

## Decision

The `AppDatabasePort` element graduates to
CMP-0003, a standalone
CMP with `component-type: protocol`, owned by the Canonical Store
context (DEC-0121 ownership
unchanged). It carries the typed operation families
(DEC-0129) and the
conformance expectations;
CMP-0001 becomes a
consumer via `depends-on`. **Pattern**: the remaining infrastructure
ports (vector store, embedding, graph store) likewise arrive as
standalone `protocol`-type CMPs in their owning contexts when
EP-0004/EP-0007
derive them.

## Rationale

The conformance criterion holds today, not hypothetically; and one
uniform pattern across all four ports spares two future epics the same
deliberation.

## Alternatives Considered

- **Keep nested until a second adapter ships** — the SP-0002 graduation
  path would then re-open an approved store doc to extract the seam it
  needs.
