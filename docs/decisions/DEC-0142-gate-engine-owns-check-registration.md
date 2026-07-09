---
id: DEC-0142
type: decision
title: The gate engine owns all required-check registration; CMP-0001 posts its own check results
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Required-check registration — which checks are required on which branches —
  is exclusively the gate engine's policy-compilation duty, covering gate-
  policy, conflicts-open, tier-2 suite, and mechanical-diff validator.
  CMP-0001's forward-declared operation is narrowed to posting its own check
  results (tier-2 suite and mechanical-diff verdicts). One component owns
  what-blocks-merge: branch-protection settings get single writer and
  reconciler, preserving the seam. Storage service keeps computing what it is
  authoritative for without administering policy.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T2-T3"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0036, DEC-0132, DEC-0033]
---

# DEC-0142: Gate Engine Owns Required-Check Registration

## Context

The decision-recall audit at story derivation surfaced an ownership
ambiguity: DEC-0132
forward-declares "required-check registration" among
CMP-0001's consumed
connector operations, while
DEC-0036 has the gate
engine administering branch protection and required checks. Two
components appeared to administer what blocks merge.

## Decision

Required-check registration — which checks are required on which
branches — is exclusively the gate engine's policy-compilation duty,
covering `gate-policy`, `conflicts-open`, the tier-2 suite, and the
mechanical-diff validator. CMP-0001's
forward-declared operation is narrowed to *posting its own check
results* (the tier-2 suite and mechanical-diff verdicts it computes).
The registration and result-posting operations themselves live in
EP-0005's connector
contract, which both components consume.

## Rationale

One component owns what-blocks-merge: branch-protection settings get a
single writer and reconciler, preserving the seam
DEC-0036 drew. The
storage service keeps computing what it is authoritative for without
administering policy.

## Alternatives Considered

- **CMP-0001
  registers everything**: one host-admin caller, but the
  component deciding merge policy no longer controls what blocks merge.
- **Each component registers its own checks**: branch protection
  becomes multi-writer with no reconciler.

## Implications

CMP-0001's
Dependencies list is amended (registration → check-run result posting)
for re-affirmation; the gate engine's registration duty lands in
ST-0013.
DEC-0132's rule —
forward-declared consumption binds EP-0005
refinement — is unchanged; the gate engine's operations join that
binding list.
