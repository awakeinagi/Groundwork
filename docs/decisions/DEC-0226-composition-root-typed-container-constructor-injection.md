---
id: DEC-0226
type: decision
title: The Composition Root exposes a typed application container and injects Ports via constructor injection, not a runtime service locator
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Composition Root builds one typed application container holding every
  bound Port instance and each constructed top-level service, passing each
  dependency explicitly into consumers' constructors (constructor injection).
  Consumers never reach into a global registry or service locator. This makes
  each component's dependency set visible, keeps the binding graph in one
  auditable place, and is trivially testable without framework or global reset.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0043 @ T1"
links:
  derives-from: [SES-0043]
  relates-to: [DEC-0121, DEC-0122, DEC-0201]
  supersedes: []
---

# DEC-0226: Composition Root Uses a Typed Container + Constructor Injection

## Context

DEC-0201 gives
EP-0008 the
Composition Root — the single place where Port contracts bind to
concrete Adapters at startup. Drafting
CMP-0010 needed the
central open question: *what does the Root produce*, and how do
consumers receive their bound Ports?

## Decision

The Composition Root builds one **typed application container** — a
value holding every bound Port instance and each constructed top-level
service — and passes each dependency **explicitly into consumers'
constructors** (constructor injection). Consumers never reach into a
global registry or service locator to resolve a Port at call time, and
there is no ambient/mutable global state holding the bindings.

## Rationale

Constructor injection makes each component's dependency set visible in
its own signature, keeps the binding graph in one auditable place
(the Root), and is trivially testable — a test constructs a container
with test doubles and injects them, no framework or global reset
needed. It matches the "single place, everything else programs against
Port contracts only" intent of
DEC-0121/DEC-0201.

## Alternatives Considered

- **Runtime service-locator / registry** (consumers call
  `registry.get(QueuePort)`): rejected — dependencies become implicit
  and late-resolved, a missing binding hides until first call, and the
  registry becomes ambient global state the Root was meant to replace.
- **A dependency-injection framework** (`dependency-injector`, `wired`,
  …): rejected for v1 — adds a framework and its idioms to the very
  seam meant to be one plain, auditable place; its resolution magic
  obscures the binding graph. Not precluded later, but no v1 need.

## Implications

CMP-0010's contract
exposes a container-builder service and a typed container value;
CMP-0011,
CMP-0013,
and every engine consumer receive their Ports as constructor
arguments, consistent with
DEC-0122's
config-selected-adapter seam.
