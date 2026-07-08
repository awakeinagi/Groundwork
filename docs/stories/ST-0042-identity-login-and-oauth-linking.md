---
id: ST-0042
type: story
title: Identity — login and OAuth host-identity linking
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: []
  impacts: [ST-0046, ST-0048, ST-0049]
  impacted-by: []
cites: [DEC-0024, DEC-0043, DEC-0046, DEC-0153, DEC-0184, DEC-0186, DEC-0188]
---

# ST-0042: Identity — Login and OAuth Host-Identity Linking

## Summary

The auth surface every other v1 story assumes: a login flow against the
pluggable auth provider, and a one-time OAuth flow letting a participant
link their code-host identity so gate approvals in
[ST-0046](ST-0046-goal-gate-surface.md) can post as them
(per [DEC-0024](../decisions/DEC-0024-pluggable-auth.md),
[DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).

## Acceptance Criteria

1. A login component renders against whichever auth provider a
   deployment configures behind the pluggable interface, without the
   package hardcoding a specific provider
   (per [DEC-0024](../decisions/DEC-0024-pluggable-auth.md)).
2. An authenticated participant sees their resolved person-id (per
   [DEC-0046](../decisions/DEC-0046-person-registry.md)), not a raw
   provider subject, anywhere identity is displayed.
3. A "link your code-host identity" flow walks the participant through
   the code-host's OAuth grant once; a linked identity is shown as
   connected on subsequent visits, and posting a gate review as that
   identity requires no re-consent
   (per [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
4. When a participant's role has no host seat, the linking flow instead
   surfaces the program-user fallback path (their approvals attribute to
   them via the service-signed attribution block) rather than blocking
   them from approving
   (per [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md),
   [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).
5. The login and linking components ship as `'use client'` exports of the
   npm package and render inside a host's own page tree
   (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
6. Login and linking flows meet WCAG 2.1 AA (keyboard-operable, focus
   order preserved through redirects) and render usably at every
   Tailwind breakpoint from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The auth provider implementations themselves and the person registry's
storage format ([EP-0005](../epics/EP-0005-connectors-and-identity.md));
which roles use the OAuth-vs-program-user path in a given deployment
(deployment configuration, not this story).

## Notes for Implementers

Every other v1 story in this bundle assumes an authenticated participant
is already available from this story's session/context provider. The
standalone app ([ST-0049](ST-0049-standalone-application-shell.md))
bootstraps this story's login flow itself; an embedding host may instead
supply its own already-authenticated context and use only the linking
flow.
