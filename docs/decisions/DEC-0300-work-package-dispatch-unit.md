---
id: DEC-0300
type: decision
title: The work package is the manifest dispatch unit — generated bundles, principled batching, shared preamble
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7"
overview: >-
  The Handoff Manifest dispatches work packages: generated projections
  assembling one or more elements' contract blocks + the transitive
  closure of referenced contract items + applicable component
  invariants (C-n) and IG constraints + a glossary slice + a reference
  to the single generated Shared Preamble (reference stack, error
  model, repo conventions). Batching criterion: an element is a
  standalone work package iff it carries self-contained implementable
  A/B items (not solely enforcement of another element's contract);
  otherwise it rides with its enforcing/consuming element; protocols
  always standalone. Batching is manifest-generator logic — never
  hand-tagged. Bundles are never authored; same canonical-ref yields
  identical bundles (reproducibility rule preserved). Yields ~34
  packages from today's 53 elements. Two kinds exist: element work
  packages and integration work packages (DEC-0301).
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0297, DEC-0299, DEC-0301, DEC-0304, DEC-0305]
---

# DEC-0300: Work Package as Dispatch Unit

## Context

Element-grain handoff needs a dispatch artifact sized for one
empty-context agent, without authoring 53 self-contained documents
that would drift (doc-rot anti-pattern) and without dispatching
one-item value objects as standalone tasks.

## Decision

The manifest dispatches **work packages** — generated projections,
never authored:

- **Contents**: the element contract block(s) + transitive closure of
  referenced contract items + applicable `C-n`/`IG-n` + glossary
  slice + a reference to the single generated **Shared Preamble**
  (reference stack, error model, repo conventions).
- **Batching criterion**: an element is standalone iff it carries
  self-contained implementable A/B items — not solely enforcement of
  another element's contract. Otherwise it rides with its
  enforcing/consuming element. Protocols are always standalone.
- Batching is manifest-generator logic; authors never hand-tag.
- Same `canonical-ref` ⇒ identical bundles.

## Rationale

Generated projections give empty-context feasibility with zero new
authored surface; the principled criterion ("does it produce a
testable artifact in isolation?") beats type-based heuristics while
matching them in practice (values/events ride, entities typically
standalone).

## Alternatives Considered

- **53 standalone packages** — dispatch overhead swamps one-item
  values; rejected.
- **Authored self-contained bundles** — 53-way context duplication
  and drift; rejected.
- **Type-based batching rule** — no principle when a type surprises;
  rejected in favor of the criterion.

## Implications

SPEC-handoff-manifest superseded (schema: tasks, typed depends-on,
slices, preamble); EP-0001 owns generation (DEC-0305); the Shared
Preamble and "work package" enter the glossary.
