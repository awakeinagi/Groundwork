# Epic-Slicing Seams

Guidance for the "boundaries between epics" question in epic derivation
(BG → EPs). Epics are macro-containers — related capabilities, user
groups, or phases of system development grouped together with minimal
inter-dependencies between them. Where you cut a goal into epics
determines whether the resulting work can proceed in parallel or
bottlenecks on itself.

## Vertical slicing vs. horizontal (layer) slicing

**Vertical slicing** — the goal, epic-by-epic. Each epic cuts through
every architectural layer it touches (UI, logic, data) to deliver a
complete, coherent, demoable capability along a real business or domain
boundary. This is what all six seams below produce.

**Horizontal (layer) slicing** — the anti-pattern. Epics named after
architectural layers instead of business seams: "Database Changes,"
"Frontend Components," "Stripe Integration." Nothing is testable or
demoable until every layer-epic is (mostly) done, because every
capability needs a piece of each one — the split creates false
dependencies and a bottleneck at the end instead of independent,
parallelizable work. If a candidate epic's title names a technology or
architectural layer rather than a capability, treat that as a signal to
re-slice.

## No fixed number of epics

The six seams below are a checklist of candidate cuts, not a quota.
Apply only the ones that actually carve a real boundary in this specific
goal. A narrow goal may need one epic; a broad platform goal may need
eight. Forcing multiple epics onto a small goal just to exercise every
seam adds governance overhead (a session, a gate, an approval) without
unlocking any real parallel work — and running the
[deliverable-coverage pass](refinement-process.md) after an
over-fragmented split just produces more surface area to audit, not more
clarity.

**Signals to split one candidate epic into two:**
- The two halves have genuinely independent "Why"s — you can't state one
  sentence tying both halves to the goal's outcomes without "and also."
- The halves fall on opposite sides of one of the six seams below
  (different persona, lifecycle stage, channel, third-party risk,
  sophistication tier, or bounded context).
- The halves could be built and demoed by different people with zero
  mutual blocking — forcing them into one epic creates an artificial
  bottleneck where nothing gates until everything is done (see
  horizontal slicing, above).
- Run the [cross-epic coupling check](../scripts/groundwork_epic_coupling.py)
  once draft stories exist — if a single epic's own stories cluster into
  two groups with near-zero decisions in common, that's the same signal
  one level down, and usually means the epic should have been two from
  the start.

**Signals to keep two candidate epics as one:**
- They fail the coupling check the other way: every attempt to refine
  one immediately produces decisions that reopen the other — persistent
  mutual `impacts`/`impacted-by` coupling that never resolves. An epic
  boundary that just becomes a permanent, unresolved mutual edge isn't a
  real boundary; it's the same epic wearing two IDs.
- One half has no standalone outcome of its own — it exists only in
  service of the other. That's a story inside the epic, not a sibling
  epic.
- The goal's total scope is narrow enough that splitting wouldn't unlock
  real parallelism — merging avoids paying gate/session overhead for a
  boundary nobody will build against independently.

## Cross-epic coupling check (required step)

After deriving a draft epic set and drawing its `impacts`/`impacted-by`
edges (per refinement-process.md's Epic derivation playbook), run:

```bash
python3 <skill-dir>/scripts/groundwork_epic_coupling.py --root <project> check EP-nnnn ...
```

It flags **mutual** (bidirectional) coupling between sibling epics —
pairs where each shapes the other's decisions — as a candidate for
re-seaming before either is refined in depth. One-directional fan-out is
reported for context only, never as a finding: bounded-context-sliced
systems (seam 6, below) routinely produce heavy one-way fan-out from
foundational epics (a storage engine, a governance layer), and that's
expected, not a defect. Advisory only — walk findings in-session and
record the disposition, same as the decision-recall audit.

## The seams

### 1. Access Seam — persona or access tier

When different users require entirely separate workflows, interfaces, or
security permissions to interact with the system, separate them at the
epic level.

**The Rule:** One epic per distinct user role if their interactions,
access controls, or operational needs do not overlap.

**Examples:**
- Epic A: Customer-Facing Portal (ordering, browsing, self-service
  tracking).
- Epic B: Internal Support Dashboard (issue overrides, order
  cancellations, system audits).

**Why this seam works:** These epics can be built completely in
parallel by separate teams or engineers. The Customer-Facing Portal epic
has zero dependency on the progress of the Internal Support Dashboard
epic.

### 2. Timeline Seam — state changes or data lifecycle

Look at how data flows through the application. Break the system down
by sequential, high-level phases of the core business object's
lifecycle.

**The Rule:** Create separate epics for the generation, management, and
ultimate archival/reporting of core system data.

**Examples:**
- Epic A: Inbound Intake & Validation (state: received / pending
  review).
- Epic B: Core Processing & Enrichment (state: validated / in-progress).
- Epic C: Downstream Distribution & Reporting (state: dispatched /
  archived).

**Why this seam works:** It proves the internal application logic works
end-to-end. You can demo a user subscribing and canceling in a test
environment without waiting for third-party payment approvals.

### 3. Protocol Seam — channel or system delivery

When a system must deliver its core value across vastly different
technological formats, channels, or physical mediums, use those channels
as epic boundaries.

**The Rule:** Separate the fundamental processing engine from the
various external channels that consume it.

**Examples:**
- Epic A: Core Platform Engine & API Foundation.
- Epic B: Automated Native Slack/Teams Chatbot Integration.
- Epic C: Mobile-Optimized Companion App Views.

**Why this seam works:** The engine epic can gate and ship independently
of any one channel; a channel epic can be added, dropped, or delayed
without touching the engine. Groundwork's own gap (the missing
`EP-0008`, Backend Application Platform, retrospected in `SES-0035`) is
exactly the Epic-A shape of this seam, distinct from `EP-0006`'s
Refinement Web UI as the channel that consumes it.

### 4. Integration Seam — third-party systems and risk

External vendors, third-party APIs, and legacy internal platforms
introduce massive dependencies, shifting timelines, and unique security
requirements.

**The Rule:** Isolate external network or platform integrations into
their own epics to prevent external delays from blocking core
application logic.

**Examples:**
- Epic A: Local Account Identity Framework.
- Epic B: Third-Party Enterprise SSO Integration (Okta / Azure AD).
- Epic C: External Logistics Vendor Real-Time Sync (FedEx / DHL APIs).

**Why this seam works:** External APIs are notorious for slowing down
development. Keeping these isolated ensures that issues like API
changes, credential problems, or sandbox testing environments don't
block delivery of core app mechanics or internal admin tools.
Groundwork's own `EP-0005` (Connectors & Identity) uses this seam to
isolate Jira/code-host/auth risk from the core engines.

### 5. Sophistication Seam — happy path vs. bad day

Do not blend core operations with complex edge-case management or
advanced system optimization in the same phase.

**The Rule:** Build a lean epic for standard operational success first,
then create separate epics to harden, scale, or automate the
application.

**Examples:**
- Epic A: Core Data Processing & Storage (standard transaction success).
- Epic B: Advanced Error Handling & Recovery (retries, circuit breakers,
  data healing).
- Epic C: Performance Optimization & Caching (scaling to peak traffic
  loads).

**Why this seam works:** This is complex logic that's critical for
revenue but not critical for a phase-1 launch. Putting it in its own
epic protects the launch timeline of the initial feature.

**Caveat:** don't let this seam excuse shipping without *baseline* error
handling — that's a definition-of-done concern for the core epic, not
phase-2 work. Reserve a separate hardening epic for genuinely advanced
resilience (circuit breakers, retries-with-backoff, chaos-level
scenarios), and keep ordinary failure handling for the core paths inside
the core epic's own stories. A goal-level Illustrative Scenario's "bad
paths" (per `DEC-0191`) usually resolve as ordinary stories inside the
core epic; only push them out to a dedicated epic when the hardening
work is large and independent enough to justify its own "Why."

### 6. Context Seam — bounded context or domain capability

When the system's substance is internal tooling, platform
infrastructure, or a complex domain model rather than a customer-facing
product surface, the clearest boundaries come from Domain-Driven
Design's bounded contexts (Evans/Vernon) — the distinct sub-domains
where a term, model, or rule set has one consistent meaning and evolves
independently of its neighbors.

**The Rule:** One epic per bounded context — a cohesive capability with
its own ubiquitous language, internal consistency rules, and data model,
kept separate from neighboring contexts even when they collaborate
closely.

**Examples:**
- Epic A: Artifact Store & Format Engine (canonical document storage,
  versioning, schema validation).
- Epic B: Governance & Gate Engine (approval policy, staleness, conflict
  mediation).
- Epic C: Cross-Reference Graph Index (derived queryable graph over the
  same artifacts).

**Why this seam works:** Each context owns its own model and vocabulary
— "gate" or "stale" means one precise thing inside Governance & Gate
Engine and doesn't leak its internal rules into the Artifact Store. This
is the seam Groundwork's own epics (`EP-0001`..`EP-0007`) actually used:
most internal/platform systems decompose this way rather than by user
persona or delivery channel, since there often isn't a customer-facing
persona split to seam along. Expect heavy one-directional fan-out from
foundational contexts under this seam (see the coupling check, above) —
that's normal, not a defect.
