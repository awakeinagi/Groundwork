---
id: DEC-0307
type: decision
title: Components group by bounded context, data ownership, and closure axis — never regrouped for end-to-end flows
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T10-T13, T16-T17"
overview: >-
  A component groups design elements that share a bounded context (one
  model, one ubiquitous language), a data-ownership boundary, and a
  common closure axis — a single shared reason-for-change, such that
  changes of that kind stay inside the component (CMP-0001/storage
  model, CMP-0009/GitHub API surface, CMP-0004/governance semantics).
  End-to-end behaviors that span components are expressed and verified
  by Slices (DEC-0302) and integration work packages (DEC-0301),
  never by regrouping components. Codifies SPEC-component's existing
  DDD alignment as a ratified rule after a dual-instance consultation
  unanimously rejected vertical-slice component regrouping (violates
  common closure and bounded-context cohesion; ~4 real flows span 4-6
  components under any grouping). The 16-component inventory stands.
  "Closure axis" and "lifted edge" enter CONTEXT.md.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0080, DEC-0302, DEC-0301, DEC-0309]
---

# DEC-0307: Bounded-Context Grouping Principle

## Context

The grouping principle lived in SPEC-component's opening line but no
decision ratified it; the stakeholder asked whether components should
instead be coherent vertical slices enabling end-to-end design and
testing.

## Decision

A component groups design elements that share:

1. a **bounded context** — one model, one ubiquitous language;
2. a **data-ownership boundary** — the component exclusively owns the
   data behind its contracts;
3. a **common closure axis** — one shared reason-for-change, so
   changes of that kind stay inside the component.

End-to-end behaviors spanning components are expressed and verified
by Slices (DEC-0302) and integration work packages (DEC-0301) —
**never by regrouping components**.

## Rationale

A flow-shaped component holds four unrelated change-reasons in one
gated doc and is closed under nothing — nearly every change reopens
it. Verticality is a dispatch/verification concern, answered by
slices at manifest time.

## Alternatives Considered

- **Pure vertical-slice components** — violates common closure,
  duplicates shared seams, re-gates 15 approved docs; rejected
  unanimously by both consultation instances.
- **Hybrid flow + substrate components** — asymmetric taxonomy, no
  data-ownership story for flow docs; rejected.
- **Leave the principle unstated** — rule-type knowledge fails
  silently; rejected.

## Implications

The 16-component inventory stands; future component derivation cites
this rule; glossary gains "closure axis".
