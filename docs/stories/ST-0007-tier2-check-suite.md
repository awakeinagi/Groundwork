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
cites: [DEC-0009, DEC-0026, DEC-0033, DEC-0034, DEC-0035]
---

# ST-0007: Tier-2 Completeness Check Suite

## Summary

The productionized successor of `tools/check_links.py`: the required PR
checks that make merge-to-main meaningful — graph integrity, completeness,
provenance discipline, append-only verification, and the mechanical-diff
validator.

## Acceptance Criteria

1. The suite runs as a required check on every gate PR and blocks merge on
   failure (per DEC-0034).
2. Checks cover, at minimum: ID uniqueness and filename match; all links
   and citations resolve; work artifacts trace to a goal; decisions derive
   from a session or spike; impact-link reciprocity and same-type rule;
   no approved artifact linked to an open conflict; required body sections
   present; contract items in CMP docs cite decisions (per DEC-0009,
   DEC-0026, DEC-0034, DEC-0011).
3. Session-file diffs are verified append-only — any rewrite of an
   existing turn fails the check (per DEC-0035).
4. The mechanical-diff validator verifies auto-PRs touch only allowlisted
   fields/append regions (per DEC-0033).
5. Every failure is reported with a human-readable explanation naming the
   artifact, the rule, and the fix (per DEC-0034).
6. The suite passes against this repository's full bootstrap corpus as its
   initial regression baseline.

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
its Acceptance & Test Expectations; runs in CI, invoked via the code-host
connector's required-check surface.

## Out of Scope

The `gate-policy` and `conflicts-open` checks (Governance engine,
EP-0003) — this story provides the check *platform* they plug into only if
that platform falls out naturally; otherwise they ship with EP-0003.

## Notes for Implementers

`tools/check_links.py` is the seed — its rules 1–6 map directly onto
criterion 2.
