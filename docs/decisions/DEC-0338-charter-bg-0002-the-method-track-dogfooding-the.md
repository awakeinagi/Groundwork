---
id: DEC-0338
type: decision
title: "Charter BG-0002 — the method track (dogfooding: the method's tooling gated by its own pipeline)"
status: superseded
superseded-by: [DEC-0441]
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T4-T6, T19"
overview: >-
  Charters BG-0002: the Groundwork method's own executable tooling
  is documented, contracted, and gated by the same pipeline it
  implements. Falsifiable outcomes: every deployed method executable
  traces to a gated contract; no ungoverned capability (an
  undiscussed tool, model, memory, or write path on a deployed agent
  is a named gate failure); human gates before deployment; nothing
  ratified stays invisibly unbuilt; no build without intake. Non-
  goals: product features, pure-prose references, re-deciding
  ratified architecture. Admission predicate: deployed execution
  surfaces operating on Groundwork corpora — the test being whether
  runtime behavior can diverge from the record without anyone
  editing the record. Sacrificial by design: per-component
  absorption clauses as armed triggers, retiring each piece when the
  BG-0001 application ships its replacement. Product epics could not
  honestly host method stories (trace corruption); a second root
  keeps both trees honest.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0335, DEC-0336, DEC-0006, DEC-0011, IDEA-0011, BG-0001, DEC-0339, DEC-0344, DEC-0019]
---

# DEC-0338: Charter BG-0002 — the Method Track

## Context

With Round 1 ratifying that method work gets standard Stories and
Component Docs, integrity rule 3 (everything traces to a Business
Goal) demanded a root the product goal cannot honestly provide: method
tooling does not advance BG-0001's outcomes (T4-T5). The stakeholder
at T6: dogfooding was a stated goal of this project, and we dropped
the ball.

## Decision

Charter BG-0002: the method track. Its capability, in one sentence:
the Groundwork method's own tooling is documented, contracted, and
gated by the same pipeline it implements. Its shape:

- **Outcomes (falsifiable):** (1) every deployed method executable
  traces to a gated contract whose lines cite decisions; (2) no
  ungoverned capability — a deployed agent holding any tool, model,
  memory, or write path absent from its gated contract is a named
  gate failure; (3) method tooling changes pass human gates before
  deployment; (4) nothing ratified stays invisibly unbuilt (the
  IDEA-0011 fix, DEC-0344); (5) no method build enters implementation
  without the DEC-0335 intake path.
- **Non-goals:** product features; governance of pure-prose process
  references (DEC-0336's boundary); re-deciding ratified architecture.
- **Admission predicate:** an artifact belongs under BG-0002 iff it is
  a deployed execution surface operating on Groundwork corpora —
  agents, skills with scripts, install machinery, hooks. The test:
  can its runtime behavior diverge from its record without anyone
  editing the record?
- **Sacrificial by design:** each method component carries an
  absorption clause — decommissioned when the BG-0001 application
  ships the absorbing capability — recorded as armed triggers in
  docs/TRIGGERS.md.

## Rationale

A second root keeps both trees honest: product traceability stays
uncorrupted, method work gains real gates, and the status report
tracks method drafts natively. The predicate and non-goals are the
junk-drawer guard; the absorption triggers prevent two permanent
canonical descriptions of artifact handling.

## Alternatives Considered

- **Umbrella method epic under BG-0001** — dishonest trace chains,
  polluted design metrics; rejected at T6.
- **New Implementation artifact type** — duplicates the CMP's
  contract-complete role (DEC-0011) with weaker rules; rejected at T2
  and by both architect instances.

## Implications

BG-0002 is drafted and gated in this session; on approval, DEC-0339's
epic derives. It cites DEC-0335 as constraint and carries the
DEC-0336 yardstick in its Scope. IDEA-0011's disposition points here.
