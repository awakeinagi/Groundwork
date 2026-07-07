---
id: BG-0001
type: business-goal
title: Groundwork — ground implementation in refined business intent
status: approved
owner: awakeinagi@gmail.com
sponsor: awakeinagi@gmail.com
created: 2026-07-05
links:
  derives-from: [SES-0001]
cites: [DEC-0001, DEC-0002, DEC-0003, DEC-0004, DEC-0005, DEC-0006, DEC-0011,
        DEC-0014, DEC-0015, DEC-0018, DEC-0019, DEC-0022, DEC-0025]
---

# BG-0001: Groundwork — ground implementation in refined business intent

## Problem

Business requests reach the tech side poorly defined, vague, or mutually
contradictory. Requirements arrive without the refinement needed to implement
them; competing requests work against each other undetected. The cost appears
downstream as rework, misaligned implementations, and systems that drift from
the intent that motivated them. ([SES-0001](../sessions/SES-0001-groundwork-inception.md) @ T1.)

## Intent

Build **Groundwork** (per [DEC-0025](../decisions/DEC-0025-name-groundwork.md)):
a standalone application ([DEC-0001](../decisions/DEC-0001-standalone-application.md))
in which an AI agent refines raw business ideas into implementation-ready
specifications through unsupervised 1:1 Q&A sessions
([DEC-0003](../decisions/DEC-0003-unsupervised-sessions.md)) with business
stakeholders, product owners, and engineering/data-science leads — producing
a gated hierarchy of Business Goals → Epics → Stories/Spikes →
contract-complete Component Docs, with every artifact provenance-linked to
the decisions and conversations that shaped it
([DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)).

## Outcomes & Success Criteria

1. **Traceability**: every implemented component traces through the artifact
   graph to at least one approved Business Goal, and every contract line
   cites the Decision behind it (per
   [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md),
   [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
2. **Conflict surfacing**: contradictory or competing requests are detected
   during refinement and either mediated or escalated with documented intent
   — never silently shipped (per
   [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).
3. **Human-ratified layers**: no artifact feeds the next stage without a
   named approver's sign-off (per
   [DEC-0006](../decisions/DEC-0006-gate-every-stage.md)).
4. **Parallel implementability**: an implementation swarm can build
   components from the Handoff Manifest with (ideally) no context beyond the
   docs and their cross-references (per
   [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md),
   [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
5. **Sync without drift**: Jira reflects the canonical docs at all times;
   detected drift reconciles toward canon (per
   [DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)).

## Scope

**In:** the refinement pipeline (sessions, synthesis, conflict handling);
the artifact model and canonical store; gates and governance; the
cross-reference graph and derived Graph Index; the consolidation memory
layer; Jira projection; read-only code-host context; the Handoff Manifest.

**Out:** orchestrating the implementation swarm
([DEC-0014](../decisions/DEC-0014-docs-are-the-product.md));
retroactive ingestion of the existing backlog
([DEC-0004](../decisions/DEC-0004-new-goals-existing-context.md));
post-implementation feedback ingestion (a candidate future goal).

## Constraints

- Reference stack: Python backend, TypeScript frontend; all specifications
  language-agnostic and sufficient to rebuild any layer in another stack
  ([DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
- Pluggable, contract-defined boundaries for: Q&A UI, doc storage/retrieval,
  Jira connection, code-host connections, auth
  ([DEC-0024](../decisions/DEC-0024-pluggable-auth.md)).
- Groundwork is specified using its own formats — this repository is the
  first Canonical Store ([DEC-0019](../decisions/DEC-0019-full-dogfood.md)).

## Stakeholders & Roles

- **Sponsor / Arbiter (bootstrap):** awakeinagi@gmail.com — tech-side lead
  bridging business and engineering.
- **Future participants:** business thought leaders (Stakeholders), product
  owners, engineering leads, data science leads, per the role model in
  [CONTEXT.md](../../CONTEXT.md).

## Conflicts & Tensions

None identified. The known internal tension — 100% self-contained component
docs vs. quality-first pragmatism — was resolved by
[DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)
(contract-complete standard, crawlable fallback, iterative tightening).

## Derived Work

- [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) — Artifact Store & Format Engine
- [EP-0002](../epics/EP-0002-refinement-session-agent.md) — Refinement Session Agent
- [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) — Governance & Gate Engine
- [EP-0004](../epics/EP-0004-graph-index.md) — Cross-Reference Graph Index
- [EP-0005](../epics/EP-0005-connectors-and-identity.md) — Connectors & Identity
- [EP-0006](../epics/EP-0006-refinement-web-ui.md) — Refinement Web UI
- [EP-0007](../epics/EP-0007-consolidation-memory-layer.md) — Consolidation Memory Layer
- [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md) — Ranking algorithm
  for impact-based refinement ordering (cross-cutting spike, per
  [DEC-0027](../decisions/DEC-0027-impact-ranked-refinement-order.md))
