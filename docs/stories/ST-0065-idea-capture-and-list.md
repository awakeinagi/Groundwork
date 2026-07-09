---
id: ST-0065
type: story
title: Idea capture and minimal list
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
owner: eng-lead
created: 2026-07-09
overview: >-
  Release-1 UI support for the Idea artifact: capturing raw change intent
  mid-session or standalone via quick-capture, seeing what has been
  captured, and taking a captured Idea up into an intake-opened session
  with the Idea's verbatim text as proposal. Capture and take-up are the
  release-1 value; browsing/queue surfaces remain release-2. Per
  DEC-0258, DEC-0260, DEC-0261, DEC-0269, DEC-0270, DEC-0271, DEC-0281.
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0049]
  impacts: [ST-0055, ST-0056]
cites: [DEC-0258, DEC-0260, DEC-0261, DEC-0269, DEC-0270, DEC-0271, DEC-0281]
---

# ST-0065: Idea Capture and Minimal List

## Summary

Release-1 UI support for the Idea artifact (DEC-0258): capturing raw
change intent at the moment it strikes — mid-session or not — seeing
what has been captured, and taking a captured Idea up into an
intake-opened session (DEC-0281). Capture and take-up are the
release-1 value (DEC-0270); browsing/queue surfaces remain release-2
territory.

## Acceptance Criteria

1. The session conversation surface offers a **"park as Idea"**
   action — the UI form of the focus-artifact test: invocable by the
   participant at any time, and proposable by the agent when a tangent
   is detected; the captured Idea records the session as its spawning
   context (per DEC-0260, DEC-0270).
2. The application shell offers a **global quick-capture** entry,
   usable outside any session, writing a valid Idea artifact from a
   title and verbatim text (per DEC-0270, DEC-0261).
3. Captured Ideas are written through the store's typed operations and
   tier-1 validation — statuses, required `proposed-by`, rejection of
   release/gate fields per the Idea schema (per DEC-0269).
4. A **minimal captured-Ideas list** shows each Idea's title, status,
   and spark context; selecting an Idea exposes its full record
   (per DEC-0270).
5. The list offers **decline with required rationale**, recorded in
   the Idea's Disposition and setting status `declined`; the action is
   gate-policy-checked against governance config (per DEC-0270).
6. The list offers a **take-up** action on a captured Idea: it opens
   an intake-opened session with the Idea's verbatim text as the
   proposal (`origin: idea`) and sets the Idea `taken-up` via
   `set-idea-disposition`, the Disposition naming the opened session —
   fulfilling the hand-off point DEC-0271 reserved (per DEC-0281,
   DEC-0261).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Impact Notes

ST-0065's capture and list decisions shape the release-2 surfaces:
ST-0055 (change-proposal triage views) will surface captured Ideas
beside untriaged CPs as one work queue, and ST-0056 (full artifact and
graph browsing) will subsume the minimal list in its all-types
browsing — both inherit this story's list semantics and lifecycle
affordances as constraints (per DEC-0270).

## Out of Scope

Work-queue surfacing beside untriaged CPs and full browsing: release
2, ST-0055 and ST-0056. Idea editing after capture: Ideas are verbatim
captures, not documents under refinement (per DEC-0258). The intake
session the take-up action opens — its protocol, cards, and lifecycle —
belongs to ST-0032/ST-0044; this story owns only the affordance and
the disposition write.

## Notes for Implementers

Quick-capture should be reachable in one interaction from anywhere in
the shell — capture that takes three clicks loses the thought it
exists to keep.
