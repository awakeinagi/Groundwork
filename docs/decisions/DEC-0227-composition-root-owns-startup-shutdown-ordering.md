---
id: DEC-0227
type: decision
title: The Composition Root owns the deterministic process startup/shutdown ordering; the ASGI lifespan invokes it
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
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
([CMP-0013](../components/CMP-0013-background-job-execution-runtime.md)
already forward-declares the Composition Root does this, per
[DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).
Drafting [CMP-0010](../components/CMP-0010-composition-root.md) needed
to decide who owns that ordering: the Root, or the ASGI/API layer.

## Decision

The **Composition Root owns a single deterministic startup and shutdown
sequence** and exposes it as lifecycle hooks (`startup()` / `shutdown()`).
Startup order: open engine resources → bind Adapters to Ports → build
the typed container's services → `JobRuntime.start()` → ready. Shutdown
runs the reverse: stop claiming new jobs → drain in-flight work (grace
period) → close engine resources.
[CMP-0011](../components/CMP-0011-inbound-api.md)'s FastAPI/ASGI
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
  [CMP-0011](../components/CMP-0011-inbound-api.md), coupling it to
  [CMP-0013](../components/CMP-0013-background-job-execution-runtime.md)
  internals and leaving no shared bring-up path for non-HTTP
  entrypoints.

## Implications

[CMP-0010](../components/CMP-0010-composition-root.md) contracts the
`startup()`/`shutdown()` sequence and its ordering as behavior items;
[CMP-0011](../components/CMP-0011-inbound-api.md) consumes them from its
ASGI lifespan rather than orchestrating bring-up itself
([DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md),
[DEC-0202](../decisions/DEC-0202-fastapi-selected.md),
[DEC-0208](../decisions/DEC-0208-queue-port-runtime-split.md)).
