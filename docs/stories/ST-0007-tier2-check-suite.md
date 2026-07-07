---
id: ST-0007
type: story
title: Tier-2 completeness check suite as required PR checks
status: gated
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0001]
  impacted-by: [ST-0001]
cites: [DEC-0009, DEC-0026, DEC-0033, DEC-0034, DEC-0035, DEC-0081, DEC-0085,
        DEC-0087, DEC-0088, DEC-0089, DEC-0092, DEC-0093, DEC-0094]
---

# ST-0007: Tier-2 Completeness Check Suite

## Summary

The productionized successor of `tools/check_links.py`: the required PR
checks that make merge-to-main meaningful — graph integrity, completeness,
provenance discipline, append-only verification, and the mechanical-diff
validator.

## Acceptance Criteria

1. The suite runs as a required check on every gate PR and blocks merge on
   failure (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
2. Checks cover, at minimum: ID uniqueness and filename match; all links
   and citations resolve; work artifacts trace to a goal; decisions derive
   from a session or spike; impact-link reciprocity and same-type rule;
   no approved artifact linked to an open conflict; required body sections
   present; contract items in CMP docs cite decisions (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md),
   [DEC-0026](../decisions/DEC-0026-directional-impact-links.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
3. Session-file diffs are verified append-only — any rewrite of an
   existing turn fails the check (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
4. The mechanical-diff validator verifies auto-PRs touch only allowlisted
   fields/append regions (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
5. Every failure is reported with a human-readable explanation naming the
   artifact, the rule, and the fix (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
6. For component docs, the suite parses `### <ElementName> (<type>)`
   element headings in Design Elements sections: every type resolves
   against the closed element-type enum, each element's typed contract
   obligations are present (including entity's conditional API contract
   when boundary-exposed), API-item request/response schemas resolve
   inline or to declared value/event elements, element-scoped item IDs
   are well-formed and unique within the doc, and Implementation
   Guidance Constraints cite decisions while Notes are exempt (per
   [DEC-0081](../decisions/DEC-0081-element-first-contract-layout.md), [DEC-0088](../decisions/DEC-0088-revised-typed-obligations.md), [DEC-0089](../decisions/DEC-0089-api-schema-resolution-rule.md), [DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md), [DEC-0087](../decisions/DEC-0087-parseable-element-headings.md)).
7. Each element heading is followed by an `Implements:` line whose story
   links (≥1) resolve, and every referenced story's Component Impact
   links the containing component doc; violations block the CMP's gate
   (per [DEC-0092](../decisions/DEC-0092-element-implements-line.md),
   [DEC-0094](../decisions/DEC-0094-implements-reciprocity-check.md)).
8. A story design-coverage audit reports every approved story with no
   referencing element; on a component doc's gate PR, an uncovered story
   whose Component Impact names that component blocks the gate (per
   [DEC-0093](../decisions/DEC-0093-story-design-coverage-check.md)).
9. The suite passes against this repository's full bootstrap corpus as its
   initial regression baseline.

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
its Acceptance & Test Expectations; runs in CI, invoked via the code-host
connector's required-check surface.

## Out of Scope

The `gate-policy` and `conflicts-open` checks (Governance engine,
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md)) — this story provides the check *platform* they plug into only if
that platform falls out naturally; otherwise they ship with [EP-0003](../epics/EP-0003-governance-and-gate-engine.md).

## Notes for Implementers

`tools/check_links.py` is the seed — its rules 1–6 map directly onto
criterion 2.
