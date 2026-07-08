---
id: DEC-0202
type: decision
title: FastAPI selected as the inbound API framework
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0038 @ T1"
links:
  derives-from: [SES-0038]
  relates-to: [DEC-0187, DEC-0018]
  supersedes: []
---

# DEC-0202: FastAPI Selected as the Inbound API Framework

## Context

[EP-0008](../epics/EP-0008-backend-application-platform.md) needs to
name the framework serving the Web UI's HTTP + SSE traffic. SSE is
already the required default streaming transport
([DEC-0187](DEC-0187-sse-default-pluggable-websocket.md)), and the
reference stack is Python
([DEC-0018](DEC-0018-python-backend-language-agnostic-specs.md)).

## Decision

FastAPI is the v1 inbound API framework: ASGI-native, first-class
SSE/WebSocket support, typed request/response models.

## Rationale

[DEC-0187](DEC-0187-sse-default-pluggable-websocket.md) already requires
a client abstraction supporting both SSE and
WebSocket — FastAPI supports both natively on ASGI without a bolted-on
shim. Typed request/response models fit the contract-complete standard
([DEC-0011](DEC-0011-contract-complete-component-docs.md)) this project
holds itself to elsewhere.

## Alternatives Considered

- **Flask + ASGI shim**: rejected — more moving parts to get SSE working
  well; fights the framework instead of using native support.
- **Django REST Framework**: rejected — heavier, brings an ORM/admin/
  auth stack Groundwork doesn't need given its own artifact-store and
  auth models.

## Implications

[EP-0008](../epics/EP-0008-backend-application-platform.md)'s Interfaces
& Contracts to Define names the FastAPI route surface as a required
contract; concrete routes are resolved at story derivation.
