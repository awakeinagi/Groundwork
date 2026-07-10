---
id: DEC-0345
type: decision
title: A test plan precedes any executable implementation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T24-T25"
overview: >-
  The presented design for anything executable includes a test plan
  — which tests will run, what each validates, what outcome counts
  as proper function — and approval covers design and test plan
  together. Implementation follows; results are reported against the
  plan, and deviations (a test dropped, added, or failing) are
  reported, never silently absorbed. Sized by the DEC-0336
  yardstick: one line suffices for a small fix; contract-bearing
  builds keep their fuller eval obligations (DEC-0322, DEC-0342).
  Motivated in-session: the approved batch-validation fix was
  verified before use, but its tests were chosen ad hoc after
  approval — validation criteria belong in the reviewed design, not
  in whatever the implementer happened to check.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0335, DEC-0336, DEC-0322, DEC-0342]
---

# DEC-0345: A Test Plan Precedes Any Executable Implementation

## Context

The DEC-0335 guard requires a presented, approved design before any
build. Mid-session, the in-flight batch-validation fix showed the
residual gap: its design was presented and approved, and it WAS tested
before use — but the tests themselves were chosen ad hoc after
approval, not reviewed as part of the design. Stakeholder refinement
at T24: "Before implementing anything executable, make a plan for
which tests will be run to validate proper function."

## Decision

The presented design for anything executable includes a test plan:
which tests will run, what each validates, and what outcome counts as
proper function. Approval covers design AND test plan together;
implementation follows; results are reported against the plan, and a
deviation from the plan (a test dropped, added, or failing) is
reported, not silently absorbed. The plan is sized like the design
itself (DEC-0336's yardstick): a one-line "run X on the scratch
corpus, expect Y" suffices for a small fix; contract-bearing builds
carry the fuller eval obligations they already have (DEC-0322,
DEC-0342's adversarial gate scenarios).

## Rationale

A design says what the thing should do; the test plan says how anyone
will know it does. Choosing tests after approval leaves "validated"
meaning whatever the implementer happened to check — the same
unexamined-assumption gap the guard rule exists to close, one step
later in the flow.

## Alternatives Considered

- **Tests chosen at implementation time** — the status quo; leaves
  validation criteria unreviewed; rejected at T24.
- **Full eval suites for everything** — disproportionate for
  one-line fixes; the sizing yardstick governs instead; rejected.

## Implications

The DEC-0335 intake path's design step gains the test-plan clause;
the AGENTS.md standing instruction and the design-session references
state it. The DEC-0342 backfill stories and the DEC-0340/DEC-0341
builds carry explicit test plans in their designs.
