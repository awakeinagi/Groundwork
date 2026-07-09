---
id: DEC-0186
type: decision
title: All exported components are client-component boundaries; no server-prefetch helpers in v1
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0034 @ T2-T3"
links:
  derives-from: [SES-0034]
  relates-to: [DEC-0184]
  supersedes: []
---

# DEC-0186: All Components Are Client Boundaries

## Context

Next.js App Router renders React Server Components by default, but
Groundwork's UI is inherently interactive and streaming (question cards,
live decision-playback, streaming turn append per
ST-0032
AC5). The host needs to know exactly where the server/client boundary
falls when composing the package into its own tree.

## Decision

Every component the package exports is marked `'use client'` and
renders entirely client-side; the host mounts them inside its own server
component tree as leaf client boundaries. v1 ships no RSC-compatible
server-side data-fetching/prefetch helpers.

## Rationale

Simplest, smallest v1 contract: one rule ("everything from this package
is a client component") a host integrator can hold in their head, with
no partial-hydration edge cases to reason about. Server-side prefetch
would improve first-paint/SEO but adds real surface (streaming-safe
serialization, cache-tag design, a second API shape to version) for
content that's inherently ephemeral, per-session, and not
search-indexed.

## Alternatives Considered

- **Also ship server-side data-fetching helpers**: better TTFB by
  prefetching initial state server-side before client components
  hydrate, but doubles the API surface to design and version in v1 for
  content with no SEO/indexing motivation.

## Implications

Component docs for this bounded context must document the client-only
contract explicitly (which npm exports carry `'use client'`, what a host
may and may not attempt to render server-side) as an Out of Scope /
Constraint item, so an implementer doesn't wrongly assume SSR support.
