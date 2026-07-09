---
id: DEC-0303
type: decision
title: Atomicity is verified at gate time — DEC-0136 checklist extension plus mechanical bundle-closure check
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7"
overview: >-
  The DEC-0136 pre-gate element review extends with an atomicity
  checklist: (a) terminal — no further breakdown needed; (b) every
  sibling/cross-component dependency declared and typed on Uses:
  (DEC-0299); (c) typed contract obligations complete per DEC-0088. A
  new mechanical tier-2 check, bundle closure, assembles each
  element's work-package bundle and errors on any reference that does
  not resolve inside it (DEC-0089 schema-resolution precedent). The
  optional cold-start probe — a fresh agent given only the bundle
  enumerates unresolved questions — is sanctioned as a fitness
  function, not a gate requirement. Grounding: rule-type decisions
  fail silently unless operationalized as checklists at the stage
  they govern (DEC-0136's own rationale).
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0136, DEC-0089, DEC-0088, DEC-0297, DEC-0299, DEC-0300]
---

# DEC-0303: Atomicity Verification

## Context

DEC-0297 makes atomicity a gate-checked obligation; without an
operationalized check it would be asserted, not verified.

## Decision

- **Checklist extension** to the DEC-0136 pre-gate element review:
  (a) terminal? (b) all dependencies declared and typed on `Uses:`?
  (c) typed obligations complete per DEC-0088?
- **Bundle-closure check** (new mechanical tier-2): assemble each
  element's work-package bundle; error on any reference that does not
  resolve inside it. Precedent: DEC-0089's schema-resolution rule.
- **Cold-start probe** (optional fitness function): a fresh agent
  given only the bundle enumerates unresolved questions; zero is the
  target. Not a gate requirement.

## Rationale

Terminality needs judgment (checklist); closure is mechanical
(tier-2). Splitting them keeps gates cheap and honest.

## Alternatives Considered

- **Atomicity by declaration** — silent failure mode; rejected.
- **Cold-start probe as mandatory gate step** — expensive per gate;
  sanctioned as optional instead.

## Implications

SPEC-component gate steps and the facilitation playbook gain the
checklist; the product's CheckSuite gains the closure check
(follow-on amendment with DEC-0309's projection check).
