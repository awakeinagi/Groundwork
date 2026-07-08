---
id: ST-0049
type: story
title: Standalone application shell
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
cites: [DEC-0184, DEC-0186, DEC-0188]
---

# ST-0049: Standalone Application Shell

## Summary

A thin Next.js App Router application, living only in this repo, that
imports the same npm component package every other v1 story ships and
adds only routing, page layout, and its own auth/session bootstrapping —
so Groundwork is directly usable without any host app
(per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)).

## Acceptance Criteria

1. The shell app imports every v1 component exclusively from the
   published npm package — no component logic is reimplemented or
   forked inside the shell app itself
   (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)).
2. The shell provides top-level routing (goal view/gate, session,
   conflict view, notification center) and page layout (navigation,
   authenticated-user chrome) around the imported components.
3. The shell bootstraps [ST-0042](ST-0042-identity-login-and-oauth-linking.md)'s
   login flow itself (an embedding host is expected to supply its own
   authenticated context instead), so the standalone app is usable with
   zero host integration.
4. A component or contract change in the shared package is picked up by
   the standalone shell through the normal package-consumption path (no
   parallel API) — verified by a build/test step that runs the shell app
   against the current package build.
5. The shell app is excluded from the npm package's publish artifact; it
   is a repo-local reference deployment, not a distributable
   (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md)).
6. The shell's own chrome (navigation, layout) meets WCAG 2.1 AA and
   reflows usably from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The components rendered inside the shell (owned by their own stories:
[ST-0043](ST-0043-session-progress-and-lifecycle-shell.md)–[ST-0048](ST-0048-notification-center.md));
deployment/hosting infrastructure for the standalone app (out of this
epic's UI scope); publishing the shell app itself as a distributable
product.

## Notes for Implementers

Treat drift between the shell and any host integration as a defect in
the shared package's contract, not something to special-case in the
shell — the whole point of this story is that the shell is just another
consumer of the same public API a host uses.
