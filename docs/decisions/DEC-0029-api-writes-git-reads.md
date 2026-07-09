---
id: DEC-0029
type: decision
title: All writes via the storage API; read-only git access sanctioned
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T3"
links:
  derives-from: [SES-0003]
---

# DEC-0029: API writes only; sanctioned read-only git access

## Context

DEC-0008's rationale wants the implementation swarm to consume docs the way
it consumes code, but unmediated writes would bypass validation, ID
allocation, and lifecycle enforcement.

## Decision

All writes go through the storage API — no exceptions, including agents.
Reads: application components use the API; external consumers
(implementation swarm, engineers, CI) get read-only git access pinned to
refs, exactly as the Handoff Manifest already assumes.

## Rationale

One write authority preserves every invariant the store exists to enforce;
the repo remains the zero-infrastructure distribution format for readers.

## Alternatives Considered

- **API-only, repo private**: gives up docs-as-code consumption.
- **Git-native writes for technical users**: two sources of write truth.

## Implications

The storage API contract (EP-0001) is the sole write surface; host-side
branch protection should reject pushes from anything but the service
identity (DEC-0033).
