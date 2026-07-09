---
id: ST-0048
type: story
title: Notification center
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
overview: >-
  In-app notification source of truth for authenticated participants:
  per-user event list with persistent read/unread state, per-category
  email-delivery preferences, and live new-event streaming via the same
  client as session turns. Per DEC-0075, DEC-0149, DEC-0184, DEC-0186,
  DEC-0187, DEC-0188.
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0042]
  impacts: [ST-0058]
  impacted-by: [ST-0042]
cites: [DEC-0075, DEC-0149, DEC-0184, DEC-0186, DEC-0187, DEC-0188]
---

# ST-0048: Notification Center

## Summary

The in-app source of truth for a participant's notifications — read
state, per-user channel preferences, and email delivery through the
first notifier connector
(per DEC-0075).

## Acceptance Criteria

1. An in-app center lists notification events for the authenticated
   participant (per ST-0042),
   each with read/unread state that persists across sessions
   (per DEC-0075).
2. Marking an item read/unread updates immediately in the UI and
   persists via the notification API; the in-app center remains correct
   even if email delivery for the same event fails or is disabled
   (per DEC-0075).
3. A preferences panel lets the participant choose, per notification
   category, whether they also receive email — changes take effect for
   new events immediately
   (per DEC-0075).
4. New events appear in the center live (via the same streaming client
   as session turns) without a manual refresh
   (per DEC-0187).
5. The center and preferences panel ship as `'use client'` exports of the
   npm package (per DEC-0184,
   DEC-0186).
6. The center meets WCAG 2.1 AA (unread state is conveyed by more than
   color, list items are keyboard-navigable) and reflows usably from
   `sm` up, including a collapsed/badge-only presentation below `md`
   (per DEC-0188).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The notifier connector implementations themselves (email adapter and
any future channel, sliced as their own EP-0005
story per DEC-0149);
the event schema's producing side (backend, emits events this story
only renders).

## Notes for Implementers

The notification event schema (event → center entry → connector
delivery) is a contract this story consumes, not one it owns — confirm
its shape against EP-0005's
notifier work before locking the center's data model.

The center's reads, read/unread updates, and preference writes define
ST-0058's notification
routes — the Inbound API's notification surface is specified against
this story's data model.
