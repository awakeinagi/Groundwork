---
id: DEC-0082
type: decision
title: Closed five-type element taxonomy — entity, value, service, event, protocol
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T6-T7"
links:
  derives-from: [SES-0012]
---

# DEC-0082: Closed Five-Type Element Taxonomy

## Context

The sponsor seeded five types (object, value, service, event, protocol)
and invited renaming/expansion/contraction. Candidates for additional
types (repository/store, workflow/process, policy/rule) were tested
against real Groundwork elements; "object" competed with the DDD
canonical term.

## Decision

The element-type taxonomy is exactly five types — **entity, value,
service, event, protocol** — defined language-neutrally. "Entity"
replaces the seeded "object". The set is closed: adding a type requires
a refinement session, a new decision, and a spec change. No ad-hoc types.

## Rationale

Entity is the canonical DDD term for identity+state+lifecycle and
unambiguous next to value; "object" is overloaded (in Python everything
is an object). Every current element fits the five (the outbox and ID
counters are data-contract details of a service; orchestration is a
service; a gate policy is a value interpreted by a service). A closed
enum is machine-validatable and gives the Implementation Swarm stable
semantics; deliberate friction keeps the shared vocabulary from
sprawling.

## Alternatives Considered

- **Keep "object"**: everyday phrasing, but costs precision the glossary
  discipline exists to protect.
- **Additional v1 types (repository, workflow, policy)**: each models as
  a composition of the five; dedicated types would encode implementation
  patterns rather than contract kinds. Kept as catalog patterns instead
  ([DEC-0084](DEC-0084-modeling-patterns-catalog.md)).
- **Open set with a core**: flexible, but drift defeats the shared
  vocabulary and typed obligations become unenforceable for ad-hoc types.

## Implications

Enum defined in [SPEC-design-elements](../specs/SPEC-design-elements.md);
type names become glossary terms in [CONTEXT.md](../../CONTEXT.md);
[ST-0001](../stories/ST-0001-tier1-schema-suite.md) publishes the enum as a language-neutral schema asset; [ST-0007](../stories/ST-0007-tier2-check-suite.md)
validates element headings against it.
