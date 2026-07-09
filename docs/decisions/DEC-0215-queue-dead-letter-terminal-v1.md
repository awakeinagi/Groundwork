---
id: DEC-0215
type: decision
title: Queue Port dead-lettering is terminal in v1; no redrive operation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T1-T2"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0139, DEC-0210]
  supersedes: []
---

# DEC-0215: Queue Dead-Lettering Is Terminal in v1

## Context

DEC-0210 established
that dead-lettered jobs are "visible through the port's own bookkeeping
surface, never silently dropped," but left open whether the port itself
exposes an operation to move a dead-lettered job back to queued.
ST-0060's Acceptance Criteria name
visibility, not recovery.

## Decision

v1 defines no redrive/requeue operation on the Queue Port contract.
Dead-lettered jobs remain queryable through the status/bookkeeping
surface (`QueuePort.A-*`) but recovery — if ever needed — is an
operator action outside the port (e.g. re-enqueueing manually) or a
future contract addition, not a v1 obligation.

## Rationale

No Acceptance Criterion or cited decision calls for redrive; adding an
unrequested operation would be scope creep the gate test doesn't
require. Visibility (queryable dead-letter state) is the actual v1
guarantee — recovery ergonomics can be added later as a gated contract
change if a real need surfaces, consistent with how
CMP-0003's dead-letter
handling (`AppDatabasePort.B-5`) also stops at visibility.
