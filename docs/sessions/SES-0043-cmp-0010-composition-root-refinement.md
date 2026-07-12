---
id: SES-0043
type: session
title: CMP-0010 Composition Root — component contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0010 (Composition Root) toward contract-completeness
  against ST-0057. Settled wiring shape (typed application container
  with explicit constructor injection, no global service locator),
  lifecycle ownership (Root owns deterministic startup/shutdown sequence,
  ASGI lifespan invokes it), and config resolution (path from single env
  var with default; enumerated overrides only, no arbitrary dotted-path).
  Graduation review found no graduation. Decision-recall audit added
  out-of-scope clarification on job-handler registration. Produced
  DEC-0226-DEC-0228.
participant: awakeinagi@gmail.com
links:
  relates-to: [CMP-0010, EP-0008, ST-0057, DEC-0226, DEC-0227, DEC-0228]
---

# SES-0043: Composition Root — Contract Refinement

## Purpose

Make CMP-0010 contract-
complete against approved story
ST-0057. Everything
ST-0057 already settles (YAML
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
DEC-0226.

**T2 — Lifecycle: who owns process startup/shutdown ordering (open DB
resources, bind adapters, start the JobRuntime, signal ready)?**

Facilitator recommended: the **Composition Root owns a deterministic
startup()/shutdown() sequence** (open resources → bind → build services
→ JobRuntime.start() → ready; reverse on shutdown), which
CMP-0011's FastAPI lifespan
*invokes*. Noted that
CMP-0013
already forward-declares the Root wiring its `start()`/`stop()`.
Alternative: API/ASGI layer owns lifecycle, Root only returns a
container (rejected — scatters ordering into the API and couples it to
runtime internals; no shared bring-up path for non-HTTP entrypoints).

Participant: selected the recommended Root-owns-ordering option. →
DEC-0227.

**T3 — Config resolution: where does the YAML path come from, and what
may an env var override on top of it?**

Facilitator recommended: path from a **single env var with a documented
default**; env overrides limited to an **enumerated set** (the master
secret-decryption key plus a small set of per-deployment
path/endpoint values) — never arbitrary keys, never adapter selection.
Preserves
DEC-0206's "one
reviewable file is the topology" rationale. Alternative: arbitrary
dotted-path env overrides (rejected — re-opens exactly what
DEC-0206 closed;
adapter selection could drift into env space).

Participant: selected the recommended single-var + enumerated-overrides
option. →
DEC-0228.

**T4 — Confirm decisions.** Facilitator played back
DEC-0226/DEC-0227/DEC-0228
in plain language; participant confirmed all three as recorded.
Facilitator noted the remaining contract mechanics (uniform per-Port
config shape, fail-fast on unknown/extra keys, single-binder invariant,
partial-startup teardown) are derivable from
ST-0057's ACs + the confirmed
decisions and would be written into the doc without needing separate
DECs.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session refined CMP-0010, a component of the Backend
  Application Platform epic EP-0008.

## Decisions Produced

- DEC-0226
  — typed application container + constructor injection (no service
  locator).
- DEC-0227
  — the Composition Root owns the deterministic startup/shutdown
  ordering; the ASGI lifespan invokes it.
- DEC-0228
  — config path from one env var + default; enumerated overrides only,
  no arbitrary dotted-path.

## Conflicts Raised

None raised during this session. (skeleton restored at SES-0078)

## Post-Session Steps

- Consistency `sweep`/`terms` over
  DEC-0226..DEC-0228:
  no contradictions; the six new DECs narrow/add at component grain
  without conflicting with any ratified citer. (Run jointly with
  SES-0044's
  DECs.)
- Graduation review (required before gating): checked all three
  elements — `DeploymentConfig`/`CompositionRoot` are Root-internal;
  `ApplicationContainer` is owned by the Root and consumers receive
  Port-typed references *from* it (`ApplicationContainer.D-2`), not the
  container type itself. No element is consumed by a second CMP or needs
  independently versioned conformance. **Outcome: no graduation.**
- Decision-recall audit on
  CMP-0010: Sonnet 5 judge
  over the 15-candidate packet. **Findings addressed:** (1) added
  DEC-0222
  — a new Out-of-Scope bullet disclaiming job-handler registration (owned
  by CMP-0013,
  the Root only start/stops the runtime); (2) contract-accuracy fix —
  CMP-0013 is
  an approved, existing dependency, not forward-declared, so it was moved
  to a normal Dependencies bullet and added to `depends-on`. Remaining
  candidates judged noise (adapter-internal / unrelated domains).
- CMP-0010 drafted
  contract-complete and set `gated`.
