---
id: ST-0044
type: story
title: Session conversation UX — question and decision-playback cards
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0043]
  impacts: [ST-0047]
  impacted-by: [ST-0043, ST-0059]
cites: [DEC-0051, DEC-0074, DEC-0184, DEC-0186, DEC-0187, DEC-0188]
---

# ST-0044: Session Conversation UX — Question and Decision-Playback Cards

## Summary

The conversation content rendered inside
[ST-0043](ST-0043-session-progress-and-lifecycle-shell.md)'s shell: free
chat mixed with typed question cards (recommended-first options) and
decision-playback cards, each carrying the guaranteed affordances the
sponsor amended into the session UX
(per [DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)).

## Acceptance Criteria

1. A question card renders a set of options with the recommended option
   listed first and visually marked, plus free chat interleaved in the
   same stream (per [DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)).
2. Every question card exposes three affordances regardless of question
   type: an option to attach a note/clarification to any choice, a
   free-text response instead of the offered options, and an "elaborate"
   action that requests the agent expand the question with examples and
   compare/contrast before answering
   (per [DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)).
3. A decision-playback card renders a proposed decision in plain
   language with confirm/correct actions; a correction reopens the topic
   rather than silently editing the record
   (per [DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md),
   [DEC-0074](../decisions/DEC-0074-structured-hybrid-session-ux.md)).
4. Cards render incrementally as the agent's turn streams (per
   [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)),
   without waiting for the full turn to complete, and never truncate a
   card mid-stream.
5. Card components ship as `'use client'` exports of the npm package,
   composed inside [ST-0043](ST-0043-session-progress-and-lifecycle-shell.md)'s
   shell (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
6. All card types meet WCAG 2.1 AA (option groups are keyboard-navigable
   and screen-reader-labeled, the elaborate/free-text affordances are
   reachable without a mouse) and reflow usably from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The progress panel and pause/resume/auto-close rendering
([ST-0043](ST-0043-session-progress-and-lifecycle-shell.md)); what
question sequence a strategy pack drives (backend, [EP-0002](../epics/EP-0002-refinement-session-agent.md));
the mediation-specific rendering of conflict tensions
([ST-0047](ST-0047-minimal-conflict-view.md)).

## Notes for Implementers

The typed turn payloads this story renders (question-card,
decision-playback, elaboration-request/response) are the
[EP-0006](../epics/EP-0006-refinement-web-ui.md)→[EP-0002](../epics/EP-0002-refinement-session-agent.md)
contract elaboration the epic flags in its Risks — confirm the payload
shapes against the session-engine's actual contract before locking this
story's rendering logic.
