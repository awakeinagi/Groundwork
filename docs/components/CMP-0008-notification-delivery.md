---
id: CMP-0008
type: component
title: Notification Delivery
status: gated
owner: eng-lead
created: 2026-07-08
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0015]
cites: [DEC-0045, DEC-0075, DEC-0136, DEC-0149, DEC-0152, DEC-0156, DEC-0167,
        DEC-0204, DEC-0240, DEC-0241]
---

# CMP-0008: Notification Delivery

## Purpose

The delivery seam under the in-app notification center: the notifier
connector protocol — delivery operation, capability manifest,
conformance expectations — and the v1 email adapter. The connector is a
delivery pipe: it receives resolved channel addresses and pre-rendered
notification payloads from the notification center
([EP-0006](../epics/EP-0006-refinement-web-ui.md)), delivers them, and
reports a terminal result. The center owns preference resolution, event
routing, digest composition, and content rendering
(per [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md),
[DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
The center itself (event routing, read state, the in-app surface)
belongs to [EP-0006](../epics/EP-0006-refinement-web-ui.md).

The NotifierConnector protocol lives in this component per graduation
review: one future direct consumer (the notification center, no CMP
yet) does not trigger the graduation rule
(per [DEC-0240](../decisions/DEC-0240-notifier-protocol-stays-in-cmp-0008.md),
[DEC-0136](../decisions/DEC-0136-graduation-review-required.md)).

## Ubiquitous Language

Connector, Notifier Connector, Capability Manifest, Adapter — per
[CONTEXT.md](../../CONTEXT.md).

## Design Elements

### NotifierConnector (protocol)

Implements: [ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md)

Every operation enumerates typed error conditions from the closed
vocabulary `recipient-invalid | credential-error | delivery-failed |
rate-limited`
(per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).

- `NotifierConnector.A-1` — `deliver(channel_address, notification_payload)
  → DeliveryResult`: delivers a single pre-rendered notification to the
  resolved channel address. `channel_address` is an opaque string the
  adapter interprets (email address for email, channel/user ID for Slack).
  `notification_payload` carries `notification_id` (uuid), `category`
  (string — the notification type, e.g. `gate-request`,
  `reaffirmation-batch`, `conflict-escalation`), `subject` (string),
  `body_text` (string), and optional `body_html` (string). Returns
  `DeliveryResult`: `{status: delivered | failed, detail?}`. Idempotent
  on `notification_id` — a retry with the same ID returns the previous
  result without re-sending. Errors: `recipient-invalid` (malformed or
  permanently undeliverable address), `credential-error` (adapter
  credentials missing or invalid from
  [CMP-0015](CMP-0015-secret-store.md)), `delivery-failed` (transient
  external failure — SMTP timeout, provider error), `rate-limited`
  (per [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md),
  [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md),
  [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
  [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).
- `NotifierConnector.A-2` — `manifest() →
  NotifierCapabilityManifest`: the adapter declares its capabilities at
  registration
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
- `NotifierConnector.B-1` — delivery is terminal: `deliver()` returns
  either `delivered` or `failed` — no "pending" or "unknown" state. A
  failed delivery is reported back to the caller; the notification
  remains authoritative in-app regardless of external delivery outcome
  (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md),
  [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md)).
- `NotifierConnector.B-2` — adapter credentials live in the Secret Store
  ([CMP-0015](CMP-0015-secret-store.md)), never in configuration files,
  the repository, logs, or error output
  (per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).
- `NotifierConnector.B-3` — conformance: a test-double (in-memory fake)
  adapter implements this protocol in full, records deliveries without
  sending, and is the hermetic test surface consumers verify against —
  no real external delivery in tests
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

### NotifierCapabilityManifest (value)

Implements: [ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md)

- `NotifierCapabilityManifest.D-1` — schema: `channel_type` (string —
  "email", "slack", etc.), `adapter_version` (string), and boolean
  capability flags. **Minimum set** (must be `true` for a notifier
  adapter to be deployable): `deliver`. **Above-minimum** (adapted when
  `false`): `supports_html` (`body_html` ignored if false; `body_text`
  always required)
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
- `NotifierCapabilityManifest.D-2` — validity: a manifest with the
  minimum-set flag `false` makes the adapter invalid for deployment;
  the documented minimum is part of this contract, not per-adapter
  discretion
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

### EmailNotifier (service)

Implements: [ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md)

- `EmailNotifier.A-1` — implements `NotifierConnector` for
  `channel_type: "email"`. Sends to the recipient email address via
  SMTP or a provider API. Manifest: `deliver: true`,
  `supports_html: true`
  (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
- `EmailNotifier.B-1` — SMTP/provider credentials stored in
  [CMP-0015](CMP-0015-secret-store.md) (SecretStore), in the
  `email-notifier` namespace; never in configuration files, the
  repository, or logs
  (per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).
- `EmailNotifier.B-2` — passes the conformance expectations defined by
  `NotifierConnector.B-3`
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Component Invariants

- `C-1` — no notification is lost to external delivery failure: a
  failed or unconfigured external delivery never loses the
  notification — it remains authoritative in-app. The connector reports
  failure; the caller (notification center) decides how to handle it
  (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
- `C-2` — this component never resolves per-user channel preferences,
  composes digests, or renders notification content — those are the
  notification center's ([EP-0006](../epics/EP-0006-refinement-web-ui.md))
  concern. The connector delivers what it's given
  (per [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md)).

## Implementation Guidance

### Constraints

- `IG-1` — typed error conditions: adapters map every external failure
  onto the closed vocabulary in `NotifierConnector`'s preamble; no
  provider-specific exception type crosses the seam
  (per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).

### Notes

- The v1 email adapter's transport (SMTP vs. provider API such as
  SendGrid or SES) is an implementation choice, not a contract
  distinction — both are "email" adapters behind the same
  `channel_type`.
- Namespacing: the email adapter's credentials use the
  `email-notifier` namespace in
  [CMP-0015](CMP-0015-secret-store.md)'s `put`/`get` operations.
- The notification center ([EP-0006](../epics/EP-0006-refinement-web-ui.md))
  is expected to call `deliver()` via background jobs
  ([CMP-0013](CMP-0013-background-job-execution-runtime.md)/[CMP-0012](CMP-0012-queue-port.md))
  for durable retry —
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)
  anticipates "notifier retries" as a job type. This component delivers
  synchronously per call; the retry loop is the caller's.

## Dependencies

- [CMP-0015](CMP-0015-secret-store.md) — consumed sections:
  `SecretStore.A-2` (get adapter credentials).

## Acceptance & Test Expectations

1. Conformance suite: the test-double (fake) adapter passes all protocol
   expectations — deliver, idempotency, manifest validity, typed errors
   (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
2. Idempotency: `deliver()` with the same `notification_id` returns the
   previous result without re-sending; verified against the fake adapter
   (per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).
3. Error vocabulary: each typed error (`recipient-invalid`,
   `credential-error`, `delivery-failed`, `rate-limited`) is raised under
   the right conditions against the fake adapter; no provider-specific
   exception escapes
   (per [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)).
4. Credential hygiene: no adapter credentials appear in logs, error
   messages, or traces across the test suite
   (per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).
5. Email round-trip: the email adapter delivers to a test SMTP server
   and returns `delivered`; a connection-refused scenario returns
   `delivery-failed`
   (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
6. HTML capability: when `supports_html` is `true`, `body_html` is
   delivered; when `false`, only `body_text` is sent — verified against
   a fake adapter with `supports_html: false`
   (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Out of Scope

- **Notification center** — event routing, read state, per-user
  preferences, digest composition, the in-app surface — all
  [EP-0006](../epics/EP-0006-refinement-web-ui.md)'s concern
  (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md),
  [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md)).
- **Slack/Teams and other channel adapters** — deferred behind
  `TRG-0008`
  ([ST-0029](../stories/ST-0029-additional-notifier-adapters.md),
  per [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md)).
- **Content rendering and template management** — the caller renders
  `subject`/`body_text`/`body_html` before calling; this component
  transports, never renders
  (per [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md)).
- **Preference storage and resolution** — the notification center's
  concern
  ([ST-0048](../stories/ST-0048-notification-center.md) AC3,
  per [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md)).
- **Retry orchestration** — the background job runtime's
  ([CMP-0013](CMP-0013-background-job-execution-runtime.md)) concern;
  this component delivers synchronously per call
  (per [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
