---
id: SES-0043
type: session
title: CMP-0010 Composition Root — component contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
links:
  relates-to: [CMP-0010, EP-0008, ST-0057]
---

# SES-0043: Composition Root — Contract Refinement

## Purpose

Make [CMP-0010](../components/CMP-0010-composition-root.md) contract-
complete against approved story
[ST-0057](../stories/ST-0057-composition-root.md). Everything
[ST-0057](../stories/ST-0057-composition-root.md) already settles (YAML
config binding the six Ports, fail-fast on bad config,
swap-is-config-not-code, the four pre-existing + two new v1 adapters) was
recapped as settled and not re-litigated; three genuinely open
contract-shaping questions were grilled.

## Transcript

**T1 — Wiring shape: what does the Composition Root produce, and how do
consumers receive their bound Ports?**

Facilitator recommended (first option): the Root builds one **typed
application container** holding every bound Port + top-level service and
passes each dependency **explicitly into consumers' constructors**
(constructor injection); no global mutable state, fully testable by
constructing a container with test doubles. Alternatives offered: a
runtime service-locator/registry (rejected — implicit, late-resolved
deps; ambient global the Root was meant to replace), and a DI framework
(rejected for v1 — adds framework idioms to the seam meant to be one
plain auditable place).

Participant: selected the recommended typed-container + constructor-
injection option. →
[DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md).

**T2 — Lifecycle: who owns process startup/shutdown ordering (open DB
resources, bind adapters, start the JobRuntime, signal ready)?**

Facilitator recommended: the **Composition Root owns a deterministic
startup()/shutdown() sequence** (open resources → bind → build services
→ JobRuntime.start() → ready; reverse on shutdown), which
[CMP-0011](../components/CMP-0011-inbound-api.md)'s FastAPI lifespan
*invokes*. Noted that
[CMP-0013](../components/CMP-0013-background-job-execution-runtime.md)
already forward-declares the Root wiring its `start()`/`stop()`.
Alternative: API/ASGI layer owns lifecycle, Root only returns a
container (rejected — scatters ordering into the API and couples it to
runtime internals; no shared bring-up path for non-HTTP entrypoints).

Participant: selected the recommended Root-owns-ordering option. →
[DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md).

**T3 — Config resolution: where does the YAML path come from, and what
may an env var override on top of it?**

Facilitator recommended: path from a **single env var with a documented
default**; env overrides limited to an **enumerated set** (the master
secret-decryption key plus a small set of per-deployment
path/endpoint values) — never arbitrary keys, never adapter selection.
Preserves
[DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)'s "one
reviewable file is the topology" rationale. Alternative: arbitrary
dotted-path env overrides (rejected — re-opens exactly what
[DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md) closed;
adapter selection could drift into env space).

Participant: selected the recommended single-var + enumerated-overrides
option. →
[DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md).

**T4 — Confirm decisions.** Facilitator played back
[DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)/[DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)/[DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md)
in plain language; participant confirmed all three as recorded.
Facilitator noted the remaining contract mechanics (uniform per-Port
config shape, fail-fast on unknown/extra keys, single-binder invariant,
partial-startup teardown) are derivable from
[ST-0057](../stories/ST-0057-composition-root.md)'s ACs + the confirmed
decisions and would be written into the doc without needing separate
DECs.

## Decisions Produced

- [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)
  — typed application container + constructor injection (no service
  locator).
- [DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)
  — the Composition Root owns the deterministic startup/shutdown
  ordering; the ASGI lifespan invokes it.
- [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md)
  — config path from one env var + default; enumerated overrides only,
  no arbitrary dotted-path.

## Post-Session Steps

- Consistency `sweep`/`terms` over
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)..[DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md):
  no contradictions; the six new DECs narrow/add at component grain
  without conflicting with any ratified citer. (Run jointly with
  [SES-0044](../sessions/SES-0044-cmp-0011-inbound-api-refinement.md)'s
  DECs.)
- Graduation review (required before gating): checked all three
  elements — `DeploymentConfig`/`CompositionRoot` are Root-internal;
  `ApplicationContainer` is owned by the Root and consumers receive
  Port-typed references *from* it (`ApplicationContainer.D-2`), not the
  container type itself. No element is consumed by a second CMP or needs
  independently versioned conformance. **Outcome: no graduation.**
- Decision-recall audit on
  [CMP-0010](../components/CMP-0010-composition-root.md): Sonnet 5 judge
  over the 15-candidate packet. **Findings addressed:** (1) added
  [DEC-0222](../decisions/DEC-0222-runtime-owns-handler-registration.md)
  — a new Out-of-Scope bullet disclaiming job-handler registration (owned
  by [CMP-0013](../components/CMP-0013-background-job-execution-runtime.md),
  the Root only start/stops the runtime); (2) contract-accuracy fix —
  [CMP-0013](../components/CMP-0013-background-job-execution-runtime.md) is
  an approved, existing dependency, not forward-declared, so it was moved
  to a normal Dependencies bullet and added to `depends-on`. Remaining
  candidates judged noise (adapter-internal / unrelated domains).
- [CMP-0010](../components/CMP-0010-composition-root.md) drafted
  contract-complete and set `gated`.
