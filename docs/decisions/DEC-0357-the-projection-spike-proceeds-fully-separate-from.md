---
id: DEC-0357
type: decision
title: "The projection spike proceeds fully separate from SP-0007, with the parse-scope overlap accepted"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0064 @ T10-T11"
overview: >-
  The projection spike (SP-A, the first of the five ActiveGraph
  spikes) proceeds fully separate from SP-0007 (the draft spike
  DEC-0160 deferred contract-item-level graph nodes to). The parse-
  scope overlap -- both spikes parse Component Doc contract items --
  was identified in-session (SES-0064 T10) and the duplication
  deliberately accepted by the stakeholder (T11); SP-0007 remains
  draft under its original EP-0004 scoping, unmodified, and neither
  spike's scope references the other.
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0160, DEC-0354]
---

## Context

T6's schema grounding surfaced SP-0007 (draft, under EP-0004) as an existing spike prototyping contract-item-level graph nodes -- close in scope to the newly proposed projection spike (SP-A), which also parses Component Doc contract items. T10 asked the stakeholder to disposition the collision: merge the spikes, re-house SP-0007 under EP-0009, or keep them separate.

## Decision

The projection spike (SP-A) proceeds fully separate from SP-0007. The parse-scope overlap is a deliberately accepted duplication. SP-0007 remains draft, unmodified, under its original EP-0004 scoping; neither spike's scope references the other.

## Rationale

SP-0007 targets the existing graph-index tool's schema (EP-0004, IMPLEMENTS edges and rollups); SP-A targets an entirely separate, throwaway ActiveGraph run under different guardrails (DEC-0351). Merging them would tangle a production-index design question with a guardrailed exploratory spike's disposable output, and re-housing SP-0007 would touch a spike outside this session's mandate for no compensating benefit -- the stakeholder judged the duplicated parse work an acceptable cost to keep both scopes clean.

## Alternatives Considered

- **Merge SP-A into SP-0007** -- rejected; would conflate EP-0004's production graph-index question with EP-0009's throwaway exploratory guardrails.
- **Re-house SP-0007 under EP-0009 alongside the new spikes** -- rejected; SP-0007 already has a scoped home under EP-0004 and moving it is out of this session's scope.
- **Block SP-A until SP-0007 resolves, to avoid duplicate parse work** -- rejected; SP-0007 is draft with no active timeline, and blocking would stall the ActiveGraph program indefinitely.

## Implications

SP-0013 (SP-A)'s body notes explicitly that it proceeds separate from SP-0007 per this decision. SP-0007 is untouched by this session. Any future consolidation of the two parsers is a separate change, not implied by this decision.
