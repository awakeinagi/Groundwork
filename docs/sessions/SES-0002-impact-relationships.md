---
id: SES-0002
type: session
title: Impact relationships between same-level artifacts
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-05
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [BG-0001]
---

# SES-0002: Impact Relationships Between Same-Level Artifacts

## Purpose

Extend the artifact model with impact relationships between items at the
same level of the hierarchy, and establish how refinement order should be
decided when one item's refinement decisions would shape another's.

## Transcript

**T1 — Sponsor.** At each level of the documentation we should also model
impact relationships between items at that level. Example: with the 7
current epics, decisions made during the refinement of epic #5 might impact
the decisions made in epics 1–4 — and the same situation is possible at the
goals, stories, and spikes levels. How should we decide which epics to
refine first? For now, start by tracking impact with direction: add two
frontmatter items, `impacts` and `impacted-by`, each containing a list of
items. Then define a spike to develop an algorithm for ranking (determining
refinement order) items based on impact relationships.

**T2 — Agent.** Implemented as follows, surfacing one design tension: the
two fields are inverses, and storing both creates a consistency risk (A
lists `impacts: [B]` but B omits `impacted-by: [A]`). Resolution: keep both
fields for human/agent readability in either direction, and make
reciprocity a mechanically enforced integrity rule in the link checker —
same pattern as Jira's blocks/is-blocked-by. Impact links are restricted to
same-type artifacts, per the sponsor's "at that level" framing. Defined
semantics: "X impacts Y" means decisions recorded while refining X are
expected to constrain, shape, or invalidate decisions in Y. Seeded an
initial agent-proposed edge set across EP-0001–EP-0007 (to be ratified or
corrected at each epic's refinement gate); the set contains cycles
(EP-0001↔EP-0003, EP-0002↔EP-0006), confirming that naive topological
ordering is insufficient and motivating the ranking spike. SPEC-spike was
relaxed to allow cross-cutting spikes to derive directly from a Business
Goal, since refinement ordering is a goal-level concern that exists before
any epic is approved.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session extended the artifact model under the Groundwork
  business goal BG-0001 — the refinement-ordering spike it defined is
  a goal-level concern deriving directly from BG-0001.

## Decisions Produced

DEC-0026,
DEC-0027

## Conflicts Raised

None.
