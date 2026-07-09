---
id: DEC-0169
type: decision
title: Host events reach the connector protocol via registered webhooks; polling is the reconciliation-sweep backstop only
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Decides that the connector protocol exposes webhook registration for
  push-based event delivery, with periodic reconciliation polling as a
  backstop only. Constrains how host events reach the protocol and
  ensures freshness within seconds.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T2"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0145, DEC-0050]
---

# DEC-0169: Push-Webhook Event Delivery

## Context

ST-0019 AC5
requires host webhooks to surface through the protocol as a normalized
event schema; DEC-0145
already assumes the gate engine "subscribes to... host webhooks" with a
periodic reconciliation sweep as the backstop for missed events, and
DEC-0050 notes BBDC
Data Center's event families as the drift-diff webhook source — but
CMP-0005
still needed to fix whether the protocol itself is push- or
pull-shaped.

## Decision

The connector protocol exposes webhook registration
(`CodeHostConnector.A-11`): an adapter registers a callback for named
event types and normalizes inbound host payloads into the shared
`HostEvent` schema before handing them to subscribers. Polling exists
only as the reconciliation sweep
(DEC-0145),
owned by the gate engine, not as a connector-level primary delivery
path — connectors must not implement their own polling loop for
freshness.

## Rationale

Matches DEC-0145's
design intent (freshness within seconds via events, the sweep bounding
missed-delivery damage) and BBDC Data Center's actual webhook support
(DEC-0050). A
poll-based protocol would either duplicate the sweep's job at the
connector layer or leave two independent staleness-detection paths to
keep consistent.

## Alternatives Considered

- **Pull: connector exposes a poll/list-events operation** — simpler
  for adapters avoiding an inbound HTTP surface, but contradicts
  DEC-0145's
  explicit design (push primary, sweep backstop) and would give every
  future adapter a second, connector-owned polling mechanism to
  reconcile against the gate engine's sweep.

## Implications

`CodeHostConnector.A-11` (webhook registration) and the `HostEvent`
value element carry this contract; adapters lacking webhook capability
declare it false in their `CapabilityManifest` and rely entirely on the
gate engine's sweep (per DEC-0168).
