---
id: SP-0012
type: spike
title: Implementation-swarm orchestration model
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Question: what orchestration model does the v1 implementation-swarm
  orchestrator (DEC-0308) need, defined far enough to constrain the
  manifest, Slice, and work-package contracts before they finalize?
  Must answer: how agents are dispatched per slice ordering and lifted
  implementation edges (DEC-0309); what an agent receives (work-package
  bundle + Shared Preamble, DEC-0300/DEC-0304) and returns (execution
  status, acceptance outcomes against DEC-0302 slice criteria and
  DEC-0301 integration charters); retry/failure semantics; where
  orchestration state lives; and whether result-reporting requires
  feedback-loop ingestion into the doc corpus (deferred by DEC-0308 —
  this spike reports evidence either way). Output feeds the epic-home
  decision (new epic vs extension) and the gated BG-0001 scope
  amendment's release framing. Chartered at SES-0056 T15; draft
  pending its own refinement session.
timebox: 5d
links:
  derives-from: [SES-0056]
  satisfies: [BG-0001]
  relates-to: [DEC-0308, DEC-0300, DEC-0302, DEC-0305, DEC-0309]
cites: [DEC-0308, DEC-0300, DEC-0301, DEC-0302, DEC-0304, DEC-0309,
        DEC-0102]
---

# SP-0012: Implementation-Swarm Orchestration Model

## Question

What orchestration model does the v1 implementation-swarm
orchestrator (DEC-0308) need — defined far enough to constrain the
Handoff Manifest, Slice, and work-package contracts before they
finalize?

## Why It Blocks

DEC-0308 puts a production orchestrator in v1 precisely so the
southern-boundary contracts are designed against a concrete consumer.
Until the orchestration model is sketched, SPEC-handoff-manifest v2,
SPEC-slice acceptance execution, and the epic home for the
orchestrator (new epic vs extension of an existing one) cannot be
settled soundly.

## Method

1. Draft the orchestrator's consumption loop against the ratified
   contracts: manifest → slices (ordered, walking skeleton first,
   DEC-0302) → work packages (element per DEC-0300 + integration per
   DEC-0301, sequenced on lifted implementation edges per DEC-0309) →
   dispatch → verify acceptance → report.
2. Define the agent-facing contract: inputs (bundle + Shared
   Preamble, empty-context semantics per DEC-0304), outputs
   (execution status, test/acceptance results), failure and retry
   semantics.
3. Determine orchestration-state ownership (app database vs store)
   against the DEC-0102 embedded-first constraints.
4. Assess whether result-reporting requires feedback-loop ingestion
   into the corpus (deferred by DEC-0308) — report evidence either
   way.
5. Recommend the epic home: new epic vs extension, with derivation
   consequences.

## Findings

(pending — spike not yet run)

## Resulting Decisions

(pending)
