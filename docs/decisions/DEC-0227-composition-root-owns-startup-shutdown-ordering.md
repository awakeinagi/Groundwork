---
id: DEC-0227
type: decision
title: The Composition Root owns the deterministic process startup/shutdown ordering; the ASGI lifespan invokes it
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Composition Root owns a single deterministic startup and shutdown sequence
  exposed as lifecycle hooks (startup() / shutdown()). Startup order: open
  engine resources → bind adapters → build services → start runtime → ready.
  Shutdown runs the reverse. CMP-0011's ASGI lifespan invokes these but does not
  own the ordering. This keeps ordering knowledge next to the bindings it
  constrains and enables non-HTTP entrypoints to use the same sequence.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0043 @ T2"
links:
  derives-from: [SES-0043]
  relates-to: [DEC-0201, DEC-0202, DEC-0208, DEC-0226]
  supersedes: []
---

# DEC-0227: The Composition Root Owns Startup/Shutdown Ordering

## Context

Binding Adapters is not order-free: engine resources (the DuckDB /
LadybugDB handles) must open before their Adapters bind, services
construct after their Ports exist, and the Background Job Execution
Runtime's `start()`/`stop()` must be wired
(CMP-0013
already forward-declares the Composition Root does this, per
DEC-0132).
Drafting CMP-0010 needed
to decide who owns that ordering: the Root, or the ASGI/API layer.

## Decision

The **Composition Root owns a single deterministic startup and shutdown
sequence** and exposes it as lifecycle hooks (`startup()` / `shutdown()`).
Startup order: open engine resources → bind Adapters to Ports → build
the typed container's services → `JobRuntime.start()` → ready. Shutdown
runs the reverse: stop claiming new jobs → drain in-flight work (grace
period) → close engine resources.
CMP-0011's FastAPI/ASGI
**lifespan** hook *invokes* these — it decides *when* in the ASGI
lifecycle they fire, but does not own the ordering itself.

## Rationale

Ordering knowledge (what must open before what, drain-before-close)
belongs next to the bindings it constrains, in the one place that holds
them, not scattered into the HTTP layer — which would couple the API to
runtime and engine internals it otherwise never touches. A single owner
also makes non-HTTP entrypoints (a CLI job, a migration) able to bring
the application up and down through the same sequence.

## Alternatives Considered

- **API/ASGI layer owns lifecycle; Root only returns a container**:
  rejected — pushes ordering and drain/close discipline into
  CMP-0011, coupling it to
  CMP-0013
  internals and leaving no shared bring-up path for non-HTTP
  entrypoints.

## Implications

CMP-0010 contracts the
`startup()`/`shutdown()` sequence and its ordering as behavior items;
CMP-0011 consumes them from its
ASGI lifespan rather than orchestrating bring-up itself
(DEC-0226,
DEC-0202,
DEC-0208).
