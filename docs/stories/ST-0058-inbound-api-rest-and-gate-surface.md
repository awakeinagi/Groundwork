---
id: ST-0058
type: story
title: Inbound API — artifact, session, and gate REST surface
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  FastAPI/ASGI HTTP surface for EP-0006's non-streaming views and
  actions: artifact reads with provenance drill-down, gate actions,
  conflict reads, and notification reads/writes. Session turn streaming
  is separate (ST-0059). HTTP surface exists because Groundwork ships as
  a standalone application with its own backend services. Per DEC-0001,
  DEC-0018, DEC-0042, DEC-0127, DEC-0163, DEC-0202, DEC-0207, DEC-0212.
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0057, ST-0022]
  impacts: []
  impacted-by: [ST-0057, ST-0045, ST-0046, ST-0047, ST-0048]
cites: [DEC-0001, DEC-0018, DEC-0042, DEC-0163, DEC-0202, DEC-0207, DEC-0212,
        DEC-0127]
---

# ST-0058: Inbound API — Artifact, Session, and Gate REST Surface

## Summary

The FastAPI/ASGI HTTP surface EP-0006's
non-streaming views and actions call: artifact reads with provenance
drill-down, gate actions, conflict reads, and notification reads/writes
(DEC-0202). Session turn
streaming is a separate story
(ST-0059) per the
Data-Seam channel split
(DEC-0207). An HTTP
surface exists at all because Groundwork ships as a standalone
application with its own backend services
(per DEC-0001).

## Acceptance Criteria

1. HTTP routes serve: Business Goal/Epic/Story/Spike artifact reads
   with full content and provenance drill-down
   (per ST-0045); gate actions
   (approve/request-changes) that drive the host PR through the
   connector (per ST-0046); conflict
   reads (per ST-0047); and
   notification reads, read/unread updates, and preference writes for
   the authenticated participant
   (per ST-0048).
2. Every route requires an authenticated participant, resolved through
   ST-0022's
   provider contract; an unauthenticated request receives a `401`
   `application/problem+json` response
   (per DEC-0212).
3. Every non-2xx response is `application/problem+json` per RFC 9457,
   with a stable `type` URI per failure class and tier-1 field-level
   errors in an `errors[]` extension member where applicable — reusing
   DEC-0127's
   established model rather than a new envelope, with its own
   Inbound-API-scoped problem-type vocabulary (e.g.
   `gate-already-approved`, `session-not-found`, `identity-required`)
   (per DEC-0212).
4. Gate actions call into the Governance & Gate Engine
   (CMP-0004)
   rather than reimplementing gate logic; artifact content is read from
   the Canonical Store
   (CMP-0001)
   rather than a duplicated projection.
5. Governance dashboard/metrics routes expose
   ST-0018's existing
   metrics/query API over HTTP as fixed named endpoints — never a
   generic query language at the HTTP boundary, preserving
   DEC-0163's
   shape; this story computes nothing itself — it fronts the existing
   API (per DEC-0042).
6. The route surface is documented as a language-neutral contract
   (OpenAPI), consistent with the project's language-agnostic-specs
   requirement (per DEC-0018).

## Component Impact

CMP-0011 — stubbed, contract
pending.

## Out of Scope

- SSE session-turn streaming —
  ST-0059.
- Gate/governance decision logic itself —
  EP-0003; this
  story's routes only call into it.
- Connector logic (code host, work management, notifier) —
  EP-0005.
- The UI itself, including all rendering and client-side state —
  EP-0006.
- Governance metrics computation — computed by
  ST-0018; this story only
  exposes it over HTTP.

## Notes for Implementers

ST-0018's metrics/query API
predates DEC-0127's
citation set; when wrapping it over HTTP here, translate its own error
signaling into this story's problem+json vocabulary rather than
assuming it already speaks RFC 9457.
