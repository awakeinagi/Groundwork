---
id: DEC-0229
type: decision
title: The Inbound API contracts behavioral endpoint groups in its Component Doc; a maintained OpenAPI document is the authoritative wire contract
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  CMP-0011 contracts the route surface as behavioral endpoint groups (artifact
  reads, gate actions, conflict reads, notifications, governance metrics,
  session SSE), each stating its behavior, auth requirement, called component,
  and problem+json failure classes. A maintained OpenAPI document is named as
  the authoritative wire contract for exact paths, verbs, and request/response
  schemas. The Component Doc does not restate every path and schema inline.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0044 @ T1"
links:
  derives-from: [SES-0044]
  relates-to: [DEC-0018, DEC-0202, DEC-0127]
  supersedes: []
---

# DEC-0229: Behavioral Endpoint Groups in the Doc; OpenAPI Is the Wire Contract

## Context

ST-0058 AC6
requires the route surface documented as a language-neutral contract
(OpenAPI), per
DEC-0018.
Drafting CMP-0011 needed to
decide how concrete the route surface is *inside the Component Doc*
versus in that OpenAPI document.

## Decision

CMP-0011 contracts the route
surface as **behavioral endpoint groups** — each group (artifact reads,
gate actions, conflict reads, notifications, governance metrics, session
SSE) a contract item stating its behavior, auth requirement, the
component it calls into, and its problem+json failure classes. A
**maintained OpenAPI document is named as the authoritative wire
contract** for exact paths, verbs, and request/response schemas
(satisfying DEC-0018).
The Component Doc does not restate every path and schema inline.

## Rationale

Keeps the Component Doc a contract of *behavior and boundaries* — what
each group does, what it calls, how it fails — while the exact wire
shape lives in one language-neutral place. Restating every path+schema
in prose would duplicate the OpenAPI document, bloat the doc, and create
two artifacts that can silently drift with no source of truth between
them.

## Alternatives Considered

- **Enumerate every concrete path + verb + schema inline in the doc**:
  rejected — duplicates OpenAPI, and drift between the two has no
  designated winner. The behavioral contract + a single authoritative
  wire document is both smaller and unambiguous.

## Implications

CMP-0011's Design Elements list
endpoint-group service items and carry a Constraint that the routes are
published as OpenAPI; API-item schemas resolve to declared value
elements or the named OpenAPI document, never to undocumented inline
shapes.
