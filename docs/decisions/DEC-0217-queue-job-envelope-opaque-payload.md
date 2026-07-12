---
id: DEC-0217
type: decision
title: Queue Port job envelope is fixed with an opaque payload document
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Queue Port defines a fixed job envelope with opaque payload, not
  per-job-type typed schemas. The envelope comprises job-id, job-type (open
  string per DEC-0214), opaque JSON payload, attempt-count, and enqueued-at
  timestamp. Only the runtime's registered handler parses the payload; the
  port treats it as transport and durability, mirroring App Database Port's
  bookkeeping document.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T1-T2"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0129, DEC-0203, DEC-0214]
  supersedes: []
---

# DEC-0217: Queue Job Envelope Is Fixed, Payload Opaque

## Context

CMP-0012 needed a job payload
shape before its `enqueue`/`claim` API items could be written: a fixed
port-defined envelope with an opaque payload, or per-job-type typed
payload schemas declared at the port (which would require every new
job type to add a value element to this CMP).

## Decision

The port defines a fixed job envelope — job-id, job-type (open string
per DEC-0214), payload (an
opaque JSON document), attempt-count, and enqueued-at timestamp — as a
`Job` value element. The `payload` field's internal shape is
uninterpreted by the port; only the runtime's registered handler for
that `job-type` parses it.

## Rationale

Mirrors `AppDatabasePort.A-3`'s bookkeeping `document`, already opaque
to the port for the same reason: the port's job is transport and
durability, not payload semantics. Declaring per-job-type schemas at
the port would couple this CMP to every future job type, contradicting
DEC-0214's open-namespace
choice — new job types would still need a gated change here for their
payload shape even though the type name itself is open.

## Alternatives Considered

The facilitator's Round 1 question set posed per-job-type typed payload schemas declared at the port as the alternative to a fixed envelope with an opaque payload — noting that typed schemas would require every new job type to add a value element to CMP-0012. The fixed-envelope, opaque-payload recommendation was given instead because it mirrors `AppDatabasePort.A-3`'s bookkeeping `document`, and the stakeholder confirmed the recommendation as given. (skeleton restored at SES-0078)

## Implications

Because the port's `payload` field is uninterpreted by the port itself, only the runtime's registered handler for a given job-type parses it — the port's role stays limited to transport and durability, not payload semantics. This preserves DEC-0214's open-namespace choice for job-type: declaring per-job-type schemas at the port would have coupled CMP-0012 to every future job type, meaning new job types would still need a gated change here for payload shape even though the type name itself is open. (skeleton restored at SES-0078)
