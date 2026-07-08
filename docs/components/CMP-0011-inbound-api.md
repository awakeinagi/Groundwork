---
id: CMP-0011
type: component
title: Inbound API
status: draft
owner: eng-lead
created: 2026-07-08
context: platform
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0010, CMP-0004, CMP-0001]
---

# CMP-0011: Inbound API

## Purpose

The FastAPI/ASGI HTTP+SSE surface serving the Web UI
([EP-0006](../epics/EP-0006-refinement-web-ui.md)): artifact reads with
provenance drill-down, gate actions, conflict reads, notification
reads/writes, and governance metrics
([ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md)),
plus SSE streaming of session-engine turns with reconnect/resume
([ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md))
([DEC-0202](../decisions/DEC-0202-fastapi-selected.md),
[DEC-0207](../decisions/DEC-0207-inbound-api-rest-sse-split.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition follows [ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md)/[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md)
refinement: the route surface, the problem+json vocabulary, and the
SSE transport abstraction plus reconnect/resume contract.

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Consumes [CMP-0010](CMP-0010-composition-root.md) (process bootstrap),
[CMP-0004](CMP-0004-governance-gate-engine.md) (gate actions),
[CMP-0001](CMP-0001-artifact-store-service.md) (artifact reads); exact
consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

## Pending — Out of Scope
