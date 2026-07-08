---
id: SES-0023
type: session
title: Gate challenge — applying the DEC-0080 graduation rule to CMP-0001; graduation review as required step
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0001, CMP-0002, CMP-0003, DEC-0080, SES-0022]
---

# SES-0023: Graduation Review at the Store Component Gate

## Purpose

At [CMP-0001](../components/CMP-0001-artifact-store-service.md)'s gate
presentation, the participant asked whether the component design could
be improved by considering
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)
(hybrid granularity; seam elements graduate). This session runs that
review, graduates the qualifying elements, and turns the review into a
required step of component design.

## Transcript

**T1 — awakeinagi.** "Could we improve this component design by
considering [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)?"

**T2 — facilitator.** Re-read the decision and applied its graduation
rule (more than one consuming CMP, or independently versioned
conformance) to all thirteen elements. Findings: **ChangeEvent** fails
the first criterion — [ST-0008](../stories/ST-0008-change-event-stream.md)
already names Graph Index, governance sweeps, and consolidation
invalidation as consumers, each a future CMP that would otherwise have
to depend on all of [CMP-0001](../components/CMP-0001-artifact-store-service.md)
to cite an event field. **AppDatabasePort** fails the second — the
adapter conformance suite ([DEC-0122](../decisions/DEC-0122-config-selected-adapters.md))
is literally independently versioned conformance, and graduating it
sets a uniform every-port-is-a-protocol-CMP pattern for the three ports
arriving with [EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md).
All other elements stay nested (spec-anchored values, published assets,
internals — graduating them is the gate-explosion failure
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)
rejected). Recommended graduating both now, at the gate, rather than
amputating elements from an approved doc later; alternatives offered:
graduate one, or defer until the second consumer/adapter materializes.

**T3 — awakeinagi.** Accepted graduating both, and added two
directives: (1) make the graduation review a **required consideration
when designing components in the future — for both the system and the
skill**; (2) asked whether semantic search over design decisions would
have surfaced [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)
without intervention, and how the process can learn from the miss.

**T4 — facilitator.** Answered: the miss was not retrieval —
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md) was
already cited by the draft and present in context; it was applied as a
*fact* (the connector note) but not operationalized as a *checklist*
against each element. Semantic search
([DEC-0111](../decisions/DEC-0111-skill-semantic-search-duckdb-vss.md)–[DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md))
helps surface decisions an author has not cited; it would not reliably
fix failure-to-apply. The durable fix is the participant's directive:
rule-type decisions become required review steps at the stage they
govern. Recorded as
[DEC-0136](../decisions/DEC-0136-graduation-review-required.md) (system
SPEC + skill playbook), with the graph tool's element-inventory command
noted as the mechanical aid, and a facilitator-memory note so future
sessions apply rule-decisions as checklists.

## Decisions Produced

- [DEC-0134](../decisions/DEC-0134-graduate-change-event.md) —
  ChangeEvent graduates to
  [CMP-0002](../components/CMP-0002-change-event.md)
  (`component-type: event`)
- [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md) —
  AppDatabasePort graduates to
  [CMP-0003](../components/CMP-0003-app-database-port.md)
  (`component-type: protocol`); every future infrastructure port
  follows the same standalone-CMP pattern
- [DEC-0136](../decisions/DEC-0136-graduation-review-required.md) —
  an explicit element-graduation review is a required step before any
  CMP gates

## Conflicts Raised

None.
