---
id: DEC-0215
type: decision
title: Queue Port dead-lettering is terminal in v1; no redrive operation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  v1 defines no redrive/requeue operation on Queue Port contract.
  Dead-lettered jobs remain queryable through status/bookkeeping surface
  but recovery, if ever needed, is an operator action outside the port
  or a future contract addition. No Acceptance Criterion or cited decision
  calls for redrive; adding unrequested operation would be scope creep.
  Visibility (queryable dead-letter state) is v1 guarantee; recovery
  ergonomics can be added later if real need surfaces. Status accepted.
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

## Alternatives Considered

The facilitator's Round 1 question set posed an explicit `requeue(job-id)` operation as the alternative to leaving dead-lettering terminal in v1. The terminal-in-v1 recommendation was given instead because no Acceptance Criterion in ST-0060 calls for redrive, and the stakeholder confirmed that recommendation as given, without raising the requeue alternative further. (skeleton restored at SES-0078)

## Implications

Because the Queue Port contract defines no redrive/requeue operation in v1, dead-lettered jobs remain queryable only through the status/bookkeeping surface (`QueuePort.A-*`); recovery, if ever needed, is left to an operator action outside the port or to a future contract addition rather than a v1 obligation. Visibility of dead-lettered state is the guarantee v1 actually delivers, and recovery ergonomics can be added later as a gated contract change if a real need surfaces. (skeleton restored at SES-0078)
