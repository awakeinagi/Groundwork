---
id: DEC-0184
type: decision
title: The Groundwork UI ships as an embeddable npm React component library, plus a thin standalone app in the same repo wrapping it
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Ships the Groundwork UI as an npm package of React components and
  hooks for direct embedding in Next.js App Router applications,
  reused by a thin standalone app in the same repo. Enables component
  sharing with host context and theme inheritance.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0034 @ T2-T3"
links:
  derives-from: [SES-0034]
  relates-to: [DEC-0018]
  supersedes: []
---

# DEC-0184: UI Ships as an Embeddable npm React Component Library

## Context

EP-0006's reference frontend
must be a genuine drop-in for a specific class of host: an existing
Next.js 15 (App Router) application using React. DEC-0018
committed to a TypeScript frontend but left the delivery shape open.

## Decision

The reference UI publishes as an npm package of React components and
hooks. A host app imports and renders them directly inside its own
Next.js App Router page tree — no iframe boundary, no framework-agnostic
web-component wrapper. Groundwork also needs to run on its own, so this
repository additionally ships a thin standalone Next.js App Router app
that imports the *same* npm package and adds only routing, page layout,
and its own auth/session bootstrapping — one source of components, two
consumption modes (embedded-in-host, standalone). The standalone app
lives only in this repo; it is not itself published as a separate
distributable.

## Rationale

Direct-render composition lets the host share its own React context
(routing, theming, auth) with Groundwork's components, matching the
"drop-in" requirement exactly. An iframe would isolate cleanly but read
as a foreign surface and complicate cross-frame event/state sharing; web
components would trade that composition away to support non-React hosts
that don't exist in the stated use case. Reusing the same package for the
standalone app (rather than a parallel implementation) keeps the two
modes from drifting apart — a fix or new surface lands once and both
consumption modes get it.

## Alternatives Considered

- **Standalone app behind an iframe (for the drop-in mode)**: stronger
  isolation and an independent deploy, but breaks the "renders inside the
  host's own tree" requirement and adds postMessage plumbing for every
  cross-boundary interaction (approve clicks, notification counts).
- **Framework-agnostic web components wrapping React**: portable to
  non-React hosts, but loses direct context/composition sharing with the
  host's React tree for no benefit given the stated host is React/Next.js.
- **A separate standalone build sharing only lower-level code**: decouples
  standalone-specific UX from the embeddable contract, but risks the two
  experiences drifting apart since top-level components would be
  implemented twice.

## Implications

Every v1 story in EP-0006
ships as exported React components/hooks from one package; component
docs for this bounded context must define the package's public API
surface (component props, hooks, session-engine client) as its
contract. A new story (ST-0049)
covers the standalone app's routing/layout/auth-bootstrap shell around
that same package.
