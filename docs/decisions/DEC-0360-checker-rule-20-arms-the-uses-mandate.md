---
id: DEC-0360
type: decision
title: "Checker rule 20 arms the Uses: mandate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T13-T15"
overview: >-
  tools/check_links.py (canonical: the artifact-interact skill's
  scripts copy, installed byte-identical) gains rule 20: per-element
  Uses: presence (Uses: none as explicit empty form), syntax against
  the closed qualifier set with omitted qualifier valid as interface
  default, target resolution to elements and their items (ranges
  expanded), and the DEC-0309 projection as both-directions set
  equality; element-less docs skipped by the existing section-
  presence guard. Blocking error by default; --uses-advisory demotes
  only rule-20 findings to warnings as an authoring-time aid.
  Fixture-based pytest suite (tests/test_check_links.py, 18 tests)
  covers positives, negatives, both projection directions, both-mode
  exit codes, stub-doc skip, and non-regression of the prior 19
  rules. Strongest-member-wins type lifting deliberately excluded
  from the checker -- it remains graph-layer work per DEC-0309's own
  implications. Built under the DEC-0335/DEC-0345 guard: design +
  test plan presented (T13) and approved (T14) before
  implementation.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0299, DEC-0309, DEC-0335]
---

## Context

DEC-0299/DEC-0306/DEC-0309 mandate typed `Uses:` lines and their component-level projection, but `tools/check_links.py` never enforced the mandate — SP-0013's findings surfaced this as a gap alongside the corpus-wide absence of the lines themselves. SES-0066's take-up of IDEA-0025 required arming enforcement before or alongside the backfill, per the no-arbitrary-builds guard (DEC-0335) requiring a presented, approved design before any build.

## Decision

`tools/check_links.py` (canonical: the artifact-interact skill's `scripts/check_links.py`, installed byte-identical) gains rule 20, enforcing the DEC-0299/DEC-0306/DEC-0309 `Uses:` mandate: per-element `Uses:` presence, with `Uses: none` as the explicit empty form; syntax against the closed qualifier set (`interface | implementation | test`), with an omitted qualifier valid as the interface default; target resolution to existing elements and, when named, to items within the target element's contract block (ranges expanded); and the DEC-0309 projection check as both-directions set equality between cross-component `Uses:` targets and frontmatter `depends-on`. Element-less docs (e.g. CMP-0006) are skipped by the existing section-presence guard.

The rule is a blocking error by default. A `--uses-advisory` flag demotes only rule-20 findings to warnings, as an authoring-time aid — it does not affect the other 19 rules. Strongest-member-wins type lifting (DEC-0309) is deliberately excluded from the checker: it remains graph-layer derivation work, per DEC-0309's own implications.

A fixture-based pytest suite, `tests/test_check_links.py` (18 tests), covers positive and negative `Uses:` forms, both projection directions, both-mode exit-code correctness, the element-less-doc skip, and non-regression of the prior 19 rules.

## Rationale

Built under the DEC-0335/DEC-0345 no-arbitrary-builds guard: the design and test plan were presented to the stakeholder (SES-0066 T13) and approved (T14) before implementation began. Defaulting to blocking-error (rather than a staged advisory rollout) was chosen because no external consumers require a transition window in this single-author corpus; the advisory flag exists solely as an authoring-time iteration aid during the backfill itself, not as a rollout mechanism.

## Alternatives Considered

A no-flag variant (rule always blocking, no advisory escape hatch) was considered simpler and free of a "ships unarmed" failure mode, but the error-default flag design was judged to capture the same safety property while still supporting an authoring-time iteration workflow, and was the joint position both system-architect consultation instances converged on unanimously. Excluding rule 20 entirely and enforcing the mandate only at the graph layer was rejected: the checker is the pre-commit gate (DEC-0315) and the mandate is SPEC-level, not graph-derived.

## Implications

The 71-edge, 20-explicit-none backfill (decision 1, this session) was authored and verified against this rule. Type-lifting enforcement remains open work for the graph layer. The advisory shakeout run against the pre-backfill corpus found exactly 53 "lacks a Uses: line" findings and 25 "depends-on supported by no element Uses: edge" findings, confirming full parser coverage before the backfill writes began.
