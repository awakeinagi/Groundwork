---
id: ST-0048
type: story
title: Notification center
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0042]
  impacts: []
  impacted-by: [ST-0042]
cites: [DEC-0075, DEC-0149, DEC-0184, DEC-0186, DEC-0187, DEC-0188]
---

# ST-0048: Notification Center

## Summary

The in-app source of truth for a participant's notifications — read
state, per-user channel preferences, and email delivery through the
first notifier connector
(per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).

## Acceptance Criteria

1. An in-app center lists notification events for the authenticated
   participant (per [ST-0042](ST-0042-identity-login-and-oauth-linking.md)),
   each with read/unread state that persists across sessions
   (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
2. Marking an item read/unread updates immediately in the UI and
   persists via the notification API; the in-app center remains correct
   even if email delivery for the same event fails or is disabled
   (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
3. A preferences panel lets the participant choose, per notification
   category, whether they also receive email — changes take effect for
   new events immediately
   (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
4. New events appear in the center live (via the same streaming client
   as session turns) without a manual refresh
   (per [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
5. The center and preferences panel ship as `'use client'` exports of the
   npm package (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
6. The center meets WCAG 2.1 AA (unread state is conveyed by more than
   color, list items are keyboard-navigable) and reflows usably from
   `sm` up, including a collapsed/badge-only presentation below `md`
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The notifier connector implementations themselves (email adapter and
any future channel, sliced as their own [EP-0005](../epics/EP-0005-connectors-and-identity.md)
story per [DEC-0149](../decisions/DEC-0149-notifier-story-under-ep-0005.md));
the event schema's producing side (backend, emits events this story
only renders).

## Notes for Implementers

The notification event schema (event → center entry → connector
delivery) is a contract this story consumes, not one it owns — confirm
its shape against [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s
notifier work before locking the center's data model.
