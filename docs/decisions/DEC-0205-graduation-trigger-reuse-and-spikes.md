---
id: DEC-0205
type: decision
title: Queue/KV-store graduation reuses TRG-0001/TRG-0002; two evaluation spikes opened
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0038 @ T2-T4"
links:
  derives-from: [SES-0038]
  relates-to: [DEC-0203, DEC-0204, DEC-0105, DEC-0109]
  supersedes: []
---

# DEC-0205: Queue/KV-Store Graduation Reuses TRG-0001/TRG-0002; Two Evaluation Spikes Opened

## Context

Embedded v1 default adapters for Queue and KV-store
(DEC-0204) will
eventually need external adapters (AWS SQS, Redis, etc.) once Groundwork
runs multi-node or needs more than one concurrent writer — exactly the
conditions `TRG-0001` and `TRG-0002` already watch for, currently
subscribing
SP-0002's
app-database graduation.

## Decision

Queue and KV-store Port graduation (embedded → external adapter) reuses
the existing `TRG-0001` (multi-node/HA) and `TRG-0002` (concurrent
writers) armed triggers rather than arming new ones, per the process
rule to reuse an existing trigger with the same condition. Two new
deferred/backlog spikes are opened, subscribed to both:
SP-0009 (AWS
SQS adapter evaluation for the Queue Port — named by stakeholder
request) and
SP-0010
(external KV-store adapter evaluation), mirroring
SP-0002's role for
the app-database Port.

## Rationale

An embedded, single-process Queue or KV-store adapter can't serve
multiple app instances any more than the embedded app database can —
the same two conditions govern all three Ports' graduation, so reusing
the triggers avoids duplicating a condition already tracked and keeps
one firing revive every affected spike at once
(DEC-0110).

## Alternatives Considered

- **Arm new, Queue/KV-specific triggers**: rejected — the underlying
  condition (multi-node or multi-writer) is identical to
  `TRG-0001`/`TRG-0002`'s; a distinct trigger would just duplicate the
  same watch with no different revival behavior.
- **One combined spike for both Queue and KV-store external adapters**:
  rejected — the stakeholder named AWS SQS specifically for the Queue
  Port, and this project's existing pattern
  (SP-0002,
  SP-0005) is one
  spike per adapter-graduation question, not bundled evaluations.

## Implications

`docs/TRIGGERS.md`'s `TRG-0001` and `TRG-0002` entries gain subscriber
lines for
SP-0009 and
SP-0010.
