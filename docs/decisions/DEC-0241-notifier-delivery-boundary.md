---
id: DEC-0241
type: decision
title: Notifier delivery boundary — resolved-address, pre-rendered, center-resolved
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Establishes the notifier connector boundary: the center resolves
  per-user channel preferences and renders content before calling
  deliver(), the connector receives resolved addresses and pre-rendered
  payloads only, the center composes digests, and results are idempotent
  on notification_id. This constrains CMP-0008's NotifierConnector
  protocol contract.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0046 @ T1-T6"
links:
  derives-from: [SES-0046]
  relates-to: [DEC-0075, DEC-0045, DEC-0167]
---

# DEC-0241: Notifier Delivery Boundary

## Context

CMP-0008's contract
needs a clear seam with the notification center
(ST-0048,
EP-0006): who resolves
per-user channel preferences, who renders notification content, who
composes digests, and what the `deliver()` operation receives.

## Decision

The notifier connector is a delivery pipe. The boundary:

1. **Resolved-address delivery.** The center resolves per-user channel
   preferences and routing before calling `deliver()`. The connector
   receives a resolved channel address (opaque string — the adapter
   interprets: email address for email, channel/user ID for Slack) and
   a notification payload. It never queries preferences.

2. **Pre-rendered content.** The caller renders `subject`, `body_text`,
   and optional `body_html` before calling. Adapters transport, never
   render — no template surface per channel type.

3. **Center composes digests.** Digest/batch timing, accumulation, and
   composition are the center's concern
   (DEC-0075's "batched
   via configured channels"). The connector sees one `deliver()` call
   per logical message, whether a single event or a pre-composed digest.

4. **Idempotent on notification_id.** A retry with the same
   `notification_id` returns the previous result without re-sending,
   following the connector convention
   (DEC-0167).

## Rationale

Matches the code-host connector pattern: connectors receive resolved
inputs (repo + credentials), not "figure out which repo." Preference
storage is already the center's
(ST-0048 AC3); splitting
resolution across two components would duplicate logic.
Pre-rendered content keeps adapters simple and future channels
(Slack/Teams, deferred behind `TRG-0008`) render-free. Opaque addresses
mean a new channel type adds an adapter, never a protocol type change.

## Alternatives Considered

- **Person-id delivery (connector resolves preferences)**: more
  autonomous connector, but duplicates center logic and contradicts
  ST-0048's preference
  ownership.
- **Structured data, adapter renders**: channel-native output (Slack
  blocks vs. HTML email) but a second template surface per adapter.
- **Connector-side batching**: requires the connector to own a
  timer/flush lifecycle and preference awareness — crossing the boundary
  ST-0048 drew.

## Implications

CMP-0008's
NotifierConnector protocol specifies resolved inputs only;
its typed error vocabulary and conformance expectations follow the
established connector pattern.
