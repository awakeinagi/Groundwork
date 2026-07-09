---
id: ST-0024
type: story
title: Notifier connector contract and email adapter
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  impacted-by: [ST-0019]
cites: [DEC-0045, DEC-0075, DEC-0149, DEC-0152]
---

# ST-0024: Notifier Connector Contract and Email Adapter

## Summary

The delivery seam for everything that must reach a person outside the
app: the notifier connector contract — delivery operations, capability
manifest, per-user channel preferences — and the v1 email adapter,
with the in-app notification center remaining the source of truth.

## Acceptance Criteria

1. The notifier contract defines delivery of a notification to a
   recipient (person-id) over a channel, with each adapter declaring a
   capability manifest in the standard connector pattern
   (per DEC-0075,
   DEC-0045,
   DEC-0149).
2. The v1 email adapter implements the contract and passes its
   conformance expectations
   (per DEC-0075).
3. Delivery respects per-user channel preferences, including
   digest/batching settings, resolved per recipient
   (per DEC-0075).
4. Delivery success/failure is reported back to the notification
   center; a failed or unconfigured external delivery never loses the
   notification, which remains authoritative in-app
   (per DEC-0075).
5. Adapter credentials (SMTP/provider) live in the encrypted secret
   store — never in config files, the repo, logs, or error output
   (per DEC-0152).

## Component Impact

CMP-0008 — supplies
the notifier protocol and email-adapter contract sections.

## Out of Scope

The notification center itself — event routing rules, read state, the
in-app surface (EP-0006, per
DEC-0075);
Slack/Teams and other channels
(ST-0029, deferred);
preference storage — account-side, with the center.
