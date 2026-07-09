---
id: DEC-0185
type: decision
title: Components are styled with Tailwind CSS utility classes, sharing the host's Tailwind config
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Components are styled with Tailwind utility classes and Radix UI
  primitives, sharing the host's Tailwind v4 configuration and theme
  tokens. No separate compiled stylesheet; smallest bundle and
  native look-and-feel for the stated host stack.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0034 @ T2-T3"
links:
  derives-from: [SES-0034]
  relates-to: [DEC-0184]
  supersedes: []
---

# DEC-0185: Tailwind-Class Components Sharing the Host's Config

## Context

The stated host stack styles with Tailwind CSS 4 + Radix UI. Given
DEC-0184's
direct-render packaging, the components need a styling strategy that
either matches or stays independent of that host stack.

## Decision

Components are authored with Tailwind utility classes and Radix UI
primitives for interactive behavior/accessibility, sharing the host's
Tailwind v4 configuration and theme tokens rather than shipping a
separate compiled stylesheet. The host adds the Groundwork package to
its Tailwind content sources so the utility classes compile.

## Rationale

Matches the stated host exactly — native look-and-feel, smallest bundle
(no duplicate CSS runtime), and Groundwork's components inherit the
host's design tokens (color, spacing, radius) instead of fighting them.
The cost — coupling to a host that runs Tailwind v4 — is accepted
because that is the stated integration target, not a hypothetical one.

## Alternatives Considered

- **Pre-compiled, scoped CSS (CSS Modules or similar)**: portable to any
  host regardless of styling stack, but ships a foreign visual language
  unless heavily themed, and duplicates styling infrastructure the host
  already has.
- **Headless (Radix primitives only, no baked-in styling)**: maximum
  flexibility, but pushes full styling work onto every host — the
  opposite of "drop-in" for the stated Tailwind/Radix host.

## Implications

Component docs for this bounded context must declare the exact Tailwind
v4 content-source/config contract a host must satisfy (package glob,
required theme tokens, Radix version compatibility) as part of the
package's public contract, not as an implementation note.
