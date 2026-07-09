---
id: ST-0049
type: story
title: Standalone application shell
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
overview: >-
  Thin Next.js App Router application living in the repo, importing
  every v1 component exclusively from the published npm package with
  only routing, page layout, and auth/session bootstrapping added—so
  Groundwork is directly usable without any host app. Per DEC-0184,
  DEC-0186, DEC-0188.
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
(per DEC-0184).

## Acceptance Criteria

1. The shell app imports every v1 component exclusively from the
   published npm package — no component logic is reimplemented or
   forked inside the shell app itself
   (per DEC-0184).
2. The shell provides top-level routing (goal view/gate, session,
   conflict view, notification center) and page layout (navigation,
   authenticated-user chrome) around the imported components.
3. The shell bootstraps ST-0042's
   login flow itself (an embedding host is expected to supply its own
   authenticated context instead), so the standalone app is usable with
   zero host integration.
4. A component or contract change in the shared package is picked up by
   the standalone shell through the normal package-consumption path (no
   parallel API) — verified by a build/test step that runs the shell app
   against the current package build.
5. The shell app is excluded from the npm package's publish artifact; it
   is a repo-local reference deployment, not a distributable
   (per DEC-0184).
6. The shell's own chrome (navigation, layout) meets WCAG 2.1 AA and
   reflows usably from `sm` up
   (per DEC-0188).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

The components rendered inside the shell (owned by their own stories:
ST-0043–ST-0048);
deployment/hosting infrastructure for the standalone app (out of this
epic's UI scope); publishing the shell app itself as a distributable
product.

## Notes for Implementers

Treat drift between the shell and any host integration as a defect in
the shared package's contract, not something to special-case in the
shell — the whole point of this story is that the shell is just another
consumer of the same public API a host uses.

Every component the package exports is a client-component boundary
with no server-prefetch helpers (per DEC-0186) — the shell's App
Router pages mount them as leaf client components inside the shell's
own server-rendered tree and must not attempt to render or prefetch
package components server-side.
