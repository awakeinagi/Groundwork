---
id: DEC-0202
type: decision
title: FastAPI selected as the inbound API framework
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Selects FastAPI as v1 inbound API framework for EP-0008: ASGI-native,
  first-class SSE/WebSocket support, typed request/response models.
  Satisfies DEC-0187's required streaming transport and DEC-0018's
  Python reference stack. Aligns with contract-complete standard
  DEC-0011. Constrains EP-0008's Interfaces & Contracts to Define.
  Status accepted.
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

EP-0008 needs to
name the framework serving the Web UI's HTTP + SSE traffic. SSE is
already the required default streaming transport
(DEC-0187), and the
reference stack is Python
(DEC-0018).

## Decision

FastAPI is the v1 inbound API framework: ASGI-native, first-class
SSE/WebSocket support, typed request/response models.

## Rationale

DEC-0187 already requires
a client abstraction supporting both SSE and
WebSocket — FastAPI supports both natively on ASGI without a bolted-on
shim. Typed request/response models fit the contract-complete standard
(DEC-0011) this project
holds itself to elsewhere.

## Alternatives Considered

- **Flask + ASGI shim**: rejected — more moving parts to get SSE working
  well; fights the framework instead of using native support.
- **Django REST Framework**: rejected — heavier, brings an ORM/admin/
  auth stack Groundwork doesn't need given its own artifact-store and
  auth models.

## Implications

EP-0008's Interfaces
& Contracts to Define names the FastAPI route surface as a required
contract; concrete routes are resolved at story derivation.
