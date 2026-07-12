---
id: SES-0029
type: session
title: Refine CMP-0004 (Governance & Gate Engine) — element decomposition and contract shape
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0004 from stub toward contract-completeness. Proposed
  10-element decomposition mapping 1:1 to seven stories; no element
  qualifies for graduation under DEC-0080 (hypothetical future consumers
  vs. existing ones). Grilled three contract-shape questions: metrics API
  fixed named endpoints, gate-policy live evaluation with no cache,
  conflict-gate four-operation arbiter surface. Confirmed all
  recommendations. Produced DEC-0162-DEC-0165.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude (Sonnet 5)
transcript-fidelity: verbatim
links:
  derives-from: [EP-0003]
  relates-to: [ST-0012, ST-0013, ST-0014, ST-0015, ST-0016, ST-0017, ST-0018, DEC-0162, DEC-0163, DEC-0164, DEC-0165]
---

# SES-0029: Refine the Governance & Gate Engine Component Doc

## Purpose

CMP-0004 existed
only as a stub — Purpose section plus a list of pending headings. All
seven of its stories
(ST-0012–ST-0018)
were already approved with detailed acceptance criteria citing
DEC-0140–DEC-0147,
so this session's grilling targeted only the genuinely open translation
choices: how the component decomposes into Design Elements, and the
handful of concrete contract shapes (metrics API surface, check
evaluation model, conflict-operations surface) those stories left
unspecified.

## Transcript

**T1 — Facilitator.** Proposed a 10-element decomposition — one element
per story concern: `GovernanceConfig`(value), `GovernanceInit`(service)
for ST-0012;
`PolicyCompiler`(service) for
ST-0013;
`GatePolicyCheck`(service) for
ST-0014; `ConflictGate`
(service) for
ST-0015;
`StalenessSweepService`(service), `ImpactReport`(value) for
ST-0016;
`ReaffirmationService`(service) for
ST-0017;
`GovernanceEvent`(event), `GovernanceEventLog`(service) for
ST-0018 —
mirroring
CMP-0001's
one-service-per-capability granularity, against a coarser
single-`GovernanceEngine`-service alternative.

**T2 — Product Owner.** No option selected outright; raised: "should we
break these into multiple CMPs?" — questioning whether any element
should graduate to a standalone component under
DEC-0080's
seam-graduation rule, before committing to the nested-element shape.

**T3 — Facilitator.** Walked the graduation test (consumed by more than
one CMP, or needs independent conformance versioning) against all ten
candidate elements. Found one plausible case — `GovernanceConfig`,
since ST-0012's
implementer notes flag
EP-0002's session
guardrails as a future consumer of the decision-rights portion — but
concluded it doesn't clear the bar today: the governance file schemas
are already owned and published by
CMP-0001
(`SchemaValidator.D-2`), so a future session-agent component can read
`governance/roles.yaml` directly via `StorageService.A-1` against that
published schema without depending on
CMP-0004 at all. No
other element has a plausible second consumer — `GovernanceEvent` and
`ImpactReport` are consumed externally only through
`GovernanceEventLog`'s API (ordinary component-boundary consumption,
not a shared seam). Recommended: no graduation now, matching the
precedent that
CMP-0002/CMP-0003
graduated out of
CMP-0001 only once
there was an actual second consumer, not a hypothetical one.

**T4 — Product Owner.** Confirmed: all ten elements stay nested in
CMP-0004. If
EP-0002 later makes
governance decision-rights an actual dependency, that graduation call
gets made when EP-0002
is refined.

**T5 — Facilitator.** Three further contract-shape questions, each with
a recommended option:
1. ST-0018's
   metrics/query API — fixed named endpoints per dashboard metric
   (approval latency, stale counts, conflict aging, gate throughput)
   plus a provenance-grade-only event search, versus one generic
   parametrized query endpoint.
2. `GatePolicyCheck`'s evaluation model — live evaluation against
   `governance/*.yaml` plus PR/staleness/conflict facts on every call
   with no persisted intermediate, versus a cached `CompiledPolicy`
   value refreshed on governance ChangeEvents.
3. `ConflictGate`'s Arbiter operation surface — `escalate` / `resolve`
   / `override-approver` API items plus frontmatter-expressed
   timeout-to-default election, versus a minimal
   evaluate-plus-fire-timeout-only surface.

**T6 — Product Owner.** Selected the recommended option on all three:
fixed named endpoints; live evaluation with no cache (citing
rebuild-sufficiency and coherence with
DEC-0141's
mid-flight recompute); and the four-operation Arbiter surface.

## Decisions Produced

DEC-0162,
DEC-0163,
DEC-0164,
DEC-0165

## Conflicts Raised

None.
