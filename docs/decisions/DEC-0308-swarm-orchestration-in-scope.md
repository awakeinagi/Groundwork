---
id: DEC-0308
type: decision
title: Swarm orchestration is in scope for v1 as a full deliverable (supersedes DEC-0014)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T13-T15"
supersedes: [DEC-0014]
overview: >-
  Groundwork v1 ships a production implementation-swarm orchestrator
  as a first-class deliverable: it consumes the Handoff Manifest,
  Slices, and work packages, dispatches implementation agents, and
  reports results. The manifest remains the boundary contract between
  specification and orchestration. Supersedes DEC-0014 ("docs are the
  product; swarm orchestration is out of scope") on the orchestration
  clause; DEC-0014's other exclusion — feedback-loop ingestion of
  implementation results into the doc corpus — stays out of v1 scope,
  revisited on SP-0012's findings. BG-0001's scope is amended
  accordingly (gated); spike SP-0012 defines the orchestration model
  far enough to constrain the manifest/slice contracts before epic
  derivation (new epic vs extension decided then). Stakeholder chose
  the full-deliverable reading explicitly over the facilitator's
  specify-plus-reference-implementation recommendation. Raised so
  manifest design happens against a concrete consumer, not an
  abstract one.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0300, DEC-0302, BG-0001]
---

# DEC-0308: Swarm Orchestration In Scope

## Context

DEC-0014 kept v1 scope sane by ending Groundwork's responsibility at
approved docs plus the manifest. Designing the element-grain manifest,
slices, and work packages surfaced that their consumer — the
orchestrator — was undesigned, leaving the contracts aimed at an
abstraction.

## Decision

Groundwork v1 ships a **production implementation-swarm
orchestrator** as a first-class deliverable:

- consumes the Handoff Manifest, Slices (DEC-0302), and work packages
  (DEC-0300);
- dispatches implementation agents per slice ordering and lifted
  implementation edges;
- reports results (execution status, acceptance outcomes).

The manifest remains the boundary contract between specification and
orchestration. **Feedback-loop ingestion stays out of v1**, revisited
on SP-0012's findings. BG-0001's scope is amended (gated). Spike
**SP-0012** defines the orchestration model before epic derivation.

## Rationale

The stakeholder's driver: the manifest cannot be designed well
against a hand-waved consumer. Owning the orchestrator makes the
southern-boundary contracts real and testable end-to-end (slices'
acceptance criteria gain an executor).

## Alternatives Considered

- **Specify + reference implementation** (facilitator recommendation,
  CMP-0005/CMP-0009 pattern) — rejected by stakeholder for the
  stronger commitment.
- **Design-input-only spike** — no product commitment; rejected.
- **Keep DEC-0014** — leaves manifest design aimed at an abstract
  consumer; rejected.

## Implications

Gated BG-0001 scope amendment; consistency review of DEC-0014 citers
(BG-0001, EP-0005, CMP-0005, CMP-0009); SP-0012 chartered; epic
home (new EP vs extension) decided after the spike; v1 scope and
identity framing ("specification producer") change materially.
