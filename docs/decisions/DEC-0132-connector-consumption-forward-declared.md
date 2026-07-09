---
id: DEC-0132
type: decision
title: CMP-0001 forward-declares its code-host connector consumption; the list binds EP-0005 refinement
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  CMP-0001 enumerates exactly the connector operations it requires: fork
  provisioning, branch create/delete, PR open/merge/review-state,
  required-check registration, and a permission probe, consumed via
  capability manifest. This consumption list is a binding input to EP-0005
  refinement: the connector protocol CMP must satisfy it or raise a conflict.
  The component is gate-eligible on the strength of the list; the local-git
  fake connector proves the seam implementable today. Consumer-side shape is
  fully determined by approved stories.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T5-T6"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0045, DEC-0079, DEC-0080]
---

# DEC-0132: Forward-Declared Connector Consumption

## Context

CMP-0001 consumes
the code-host connector contract, but
EP-0005 has not been
refined — that contract does not exist yet. Blocking this component's gate on
it would serialize the two epics.

## Decision

CMP-0001's Dependencies section **enumerates exactly the connector
operations it requires** — fork provisioning, branch create/delete,
PR open/merge/review-state, required-check registration, and a
permission probe — consumed via the capability manifest
(DEC-0045). This
consumption list is a **binding input to EP-0005's refinement**: the
connector protocol CMP must satisfy it or raise a conflict. The component is
gate-eligible on the strength of the list; the local-git fake connector
(DEC-0079) proves the seam
implementable today.

## Rationale

The consumer-side shape is already fully determined by approved stories
(ST-0003); waiting
for the provider-side design adds serialization without information.
Dependency sections cite contract sections, not internals — a precise
consumption list is exactly what that discipline needs.

## Alternatives Considered

- **Refine EP-0005 first** — strictly cleaner dependency order; rejected
  as delaying the EP-0001
  deliverable for a contract whose consumer half is already known.
