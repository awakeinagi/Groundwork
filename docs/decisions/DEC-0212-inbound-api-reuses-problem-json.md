---
id: DEC-0212
type: decision
title: The Inbound API reuses DEC-0127's RFC 9457 problem+json error model
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T3-T4"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0127, DEC-0202]
  supersedes: []
---

# DEC-0212: Inbound API Reuses the Problem+JSON Error Model

## Context

[DEC-0127](../decisions/DEC-0127-problem-json-error-model.md) already
establishes RFC 9457 problem+json as the storage API's error model. The
new Inbound API ([ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md))
is a different surface (the UI-facing FastAPI app, not
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s internal
service API) and needed its own explicit call: reuse the existing model
or define a new one.

## Decision

Every non-2xx response from the Inbound API is `application/problem+json`
per RFC 9457, following
[DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)'s
established shape (stable `type` URI per failure class, tier-1
field-level errors in an `errors[]` extension member where applicable).
The Inbound API defines its own problem-type vocabulary (e.g.
`gate-already-approved`, `session-not-found`, `identity-required`)
rather than reusing the storage API's types verbatim, since the failure
classes differ by surface.

## Rationale

One error-model standard for the whole application is simpler to build
client tooling against than two competing envelopes for two HTTP
surfaces that both ultimately serve the same UI
([EP-0006](../epics/EP-0006-refinement-web-ui.md)). The decision-recall
audit surfaced [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)
directly — this is exactly the kind of duplicate-decision risk that
check exists to catch.

## Alternatives Considered

- **New, Inbound-API-specific envelope**: rejected — no reason has
  surfaced for the two HTTP surfaces to disagree on error shape, and
  disagreeing would cost UI client code a second parsing path for no
  benefit.

## Implications

[ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md)'s
Acceptance Criteria cite
[DEC-0127](../decisions/DEC-0127-problem-json-error-model.md) directly
rather than restating the envelope shape as a new requirement.
