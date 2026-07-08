---
id: DEC-0108
type: decision
title: Armed triggers surface in the status report, at release-gate reviews, and under checker validation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T4-T5"
links:
  derives-from: [SES-0017]
  relates-to: [DEC-0106, DEC-0099, DEC-0101]
---

# DEC-0108: Trigger Surfacing and Validation

## Context

A registry no one reads is where conditions go to rot. Armed triggers
must appear at the moments scope is actually examined.

## Decision

Three surfaces:

1. **Status report**: every run lists armed triggers — ID, target,
   condition inline — adjacent to the Deferred section (the items they
   would revive, per [DEC-0101](DEC-0101-deferred-out-of-metrics.md)).
2. **Release-gate review**: any release-declaration amendment to a
   Business Goal ([DEC-0099](DEC-0099-releases-declared-in-goal-scope.md))
   must review the registry — has any armed condition been met?
3. **Checker validation**: heading format
   (`## TRG-nnnn (armed|fired|retired)`), unique sequential IDs, required
   fields per status, resolvable markdown links, and a decision link on
   every fired/retired entry.

## Rationale

The status report is the skill's step-0 read — armed triggers there cost
a few lines and reach every session. Release amendments are exactly when
"should deferred work come back?" is live. Checker validation keeps the
strict format ([DEC-0106](DEC-0106-trigger-registry.md)) actually strict.

## Alternatives Considered

- **Status report only**: visibility without process hooks; nothing
  forces a look during re-planning.
- **Freshness warnings (unreviewed for N months)**: real pressure, needs
  per-entry review dates — addable later by decision if triggers rot.

## Implications

`tools/check_links.py` gains registry validation; the status tooling
gains the armed-triggers section; the Business Goal spec notes the
release-amendment review duty.
