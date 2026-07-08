---
id: SES-0022
type: session
title: CMP-0001 contract refinement — element decomposition, cross-cutting semantics, gate-blockers
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0001, EP-0001, ST-0011]
---

# SES-0022: Artifact Store Service Contract Refinement

## Purpose

Refine [CMP-0001](../components/CMP-0001-artifact-store-service.md)
from draft stub to contract-complete, now that all nine
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) stories
are approved. Settled ground recapped at open: the draft's five
candidate elements, the approved story set, and the stack/port
commitments ([DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)–[DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).

## Transcript

**T1 — facilitator.** Opened with the recap and Round 1 (element
structure), recommendations first: (1) split the draft's single
StorageService into five focused services mapping 1:1 to
[ST-0002](../stories/ST-0002-storage-api-core.md)–[ST-0006](../stories/ST-0006-typed-mechanical-writes.md)
(recommended) vs. one mega-service vs. splitting only the ID allocator;
(2) tier-1 validation as its own SchemaValidator service element
(recommended) vs. folded into StorageService; (3) close the
[ST-0007](../stories/ST-0007-tier2-check-suite.md) coverage gap with a
CheckSuite service element (recommended) vs. a separate CMP; (4) model
ItemBranch and SessionWorktree as entities with lifecycle contracts
(recommended) vs. service behavior state.

**T2 — awakeinagi.** Accepted all four recommendations — thirteen
elements total.

**T3 — facilitator.** Read back the inventory and asked Round 2
(cross-cutting semantics), recommendations first: (1) RFC 9457
problem+json as the API error model (recommended) vs. a custom
envelope; (2) ChangeEvent payload with a closed change-kind enum plus
`schema_version` (recommended) vs. open-ended kind string;
(3) AppDatabasePort as typed operation families — unit-of-work, outbox
append/claim/ack, keyed bookkeeping; no SQL across the seam
(recommended) vs. a SQL-level port; (4) mechanical operations as eight
typed API items sharing one allowlist data asset with the
mechanical-diff validator (recommended) vs. a value element per
operation.

**T4 — awakeinagi.** Accepted all four recommendations.

**T5 — facilitator.** Read back Round 2 and asked Round 3
(gate-blockers), recommendations first: (1) four component invariants —
rebuild-sufficiency, single write authority, status coherence, no
unvalidated write (recommended) vs. trimming to two; (2) keep
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
gate-eligible by forward-declaring its connector consumption as a
binding input to [EP-0005](../epics/EP-0005-connectors-and-identity.md)
(recommended) vs. blocking on [EP-0005](../epics/EP-0005-connectors-and-identity.md) design; (3) six acceptance suites
— OpenAPI conformance, hermetic fake-connector, port conformance,
tier-2 on bootstrap corpus, replay convergence, credential isolation
(recommended) vs. adding chaos/restart testing; (4) which adjacent
behaviors Out of Scope must deny (multi-select): no gate-policy
evaluation, no auto-merge of divergence, no cross-artifact event
ordering, no implementation-status storage.

**T6 — awakeinagi.** Accepted all recommendations, selected all four
Out of Scope denials, and raised a new question: "Should we require
out of scope items to be created as deferred spikes or stories so the
information is tracked in the system?"

**T7 — facilitator.** Analyzed the question: Out of Scope entries are
two species — boundary statements (permanent denials, tracked by the
owning artifact's link, wrong to backlog) and future work in disguise
(e.g. [ST-0001](../stories/ST-0001-tier1-schema-suite.md)'s
schema-evolution line, living untracked as prose). Recommended a
differentiated rule: future-work entries must exist as deferred
stories/spikes and be linked; boundary statements link the owning
artifact; classification is gate-review judgment, not a mechanical
check. Alternatives offered: blanket requirement (backlog pollution)
and status quo (the gap stands).

**T8 — awakeinagi.** Selected the differentiated rule, with immediate
application to the schema-evolution case.

## Decisions Produced

- [DEC-0126](../decisions/DEC-0126-cmp-0001-element-decomposition.md) —
  thirteen-element decomposition of [CMP-0001](../components/CMP-0001-artifact-store-service.md)
- [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md) —
  RFC 9457 problem+json error model
- [DEC-0128](../decisions/DEC-0128-change-event-closed-schema.md) —
  ChangeEvent closed kind enum + schema versioning
- [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md) —
  AppDatabasePort typed operation families, no SQL across the seam
- [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md) —
  mechanical ops as A-items with a shared allowlist asset
- [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md) —
  rebuild-sufficiency component invariant
- [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)
  — forward-declared connector consumption binding [EP-0005](../epics/EP-0005-connectors-and-identity.md)
- [DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)
  — differentiated Out-of-Scope rule; first application
  [ST-0011](../stories/ST-0011-schema-evolution-machinery.md) +
  trigger `TRG-0005`

## Conflicts Raised

None.
