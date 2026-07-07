---
id: SES-0012
type: session
title: Component spec refinement — design-element taxonomy and implementation guidance
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0001, ST-0001, ST-0007, EP-0001]
---

# SES-0012: Component Spec — Design Elements & Implementation Guidance

## Purpose

Refine [SPEC-component](../specs/SPEC-component.md): introduce a typed
taxonomy for the design elements a component comprises, and give
implementation details a legal home in the doc. Already settled and not
re-litigated: contract-completeness with crawlable fallback
([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)),
language-agnostic specs
([DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)),
bounded contexts emerging from glossary work
([DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).

## Transcript

**T1 — Sponsor.** Proposed defining component types plus an
implementation notes/details section in the spec doc. Seed taxonomy,
explicitly subject to change: *object* (DDD-like concept with
identity/state, e.g. a Python class), *value* (immutable,
attribute-defined, e.g. frozen dataclass/pydantic model), *service*
(stateless operation/capability, e.g. a function or Protocol with
methods), *event* (payload crossing an interface, e.g. pydantic
model/TypedDict), *protocol* (capability seam/interface, e.g. a
Protocol). Invited expansion, contraction, renaming.

**T2 — Agent.** Recapped the settled decisions above and surfaced two
tensions: (a) the seed types are class/function-scale while CMP docs are
bounded-context-scale ([CMP-0001](../components/CMP-0001-artifact-store-service.md) spans the whole Artifact Store Service),
so granularity is the load-bearing question; (b) [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md) requires the
types be defined language-neutrally, with Python mappings as
illustrations only. Opened round 1: granularity (recommended a typed
"Design Elements" section inside bounded-context CMPs), implementation
notes normativity, closed vs. open taxonomy, normative home.

**T3 — Sponsor.** Asked to rethink CMP granularity before answering:
would one doc per element (object, service, value, …) be better than
multi-element CMPs? Concern: with multiple elements in one CMP, how are
the behavior/data/API contracts managed across elements? One CMP per
element would be cleaner for contract management.

**T4 — Agent.** Elaborated the trade-off anchored on [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)'s gate
test (the unit an implementer can build *and test* independently): a
value or schema doc alone is not independently buildable-and-testable —
the Handoff Manifest would have to reassemble elements into work units;
one-CMP-per-element means ~10–15 gates per component and piecemeal
approvals that can ratify incoherent combinations; it also promotes
internals to published artifacts against [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)'s contracts-not-
internals rule. Countered the manageability concern with an
element-first layout: each element carries its own contract block with
element-scoped item IDs, and the element's *type* determines which
contract kinds it owes (typed obligations). Recommended a hybrid:
nested elements by default; an element consumed across component
boundaries (protocol seam, shared event schema, shared value kernel)
graduates to its own standalone CMP — noting [CMP-0001](../components/CMP-0001-artifact-store-service.md)'s Dependencies
already anticipate a future connector-contract CMP. Re-asked:
granularity (hybrid recommended), contract layout (element-first
recommended), typed obligations (yes recommended).

**T5 — Sponsor.** All three as recommended: hybrid granularity with the
graduation rule (more than one consuming CMP, or independently versioned
conformance); element-first contract blocks with component-level
invariants; types carry gate-checkable contract obligations.

**T6 — Agent.** Round 2: rename *object* → *entity* (recommended; DDD
canonical, "object" overloaded); additional v1 types tested against real
elements (recommended none — repository/workflow/policy model as
compositions of the five); closed vs. open set (recommended closed,
extended only by decision); implementation-notes normativity
(recommended a split: normative decision-cited Constraints binding the
reference implementation + advisory, possibly stack-specific Notes that
are never load-bearing).

**T7 — Sponsor.** Entity rename accepted. Five types accepted, deferring
to the recommendation, with an amendment: the proposed additions
(repository/store, workflow/process, policy/rule) must be included as
examples/guidance in the spec — a catalog showing how common system
constructs are modeled as compositions of the five types, including
which sub-elements are required to honor the independently
buildable-and-testable decision. Closed set accepted. Split
Constraints + Notes accepted.

**T8 — Agent.** Round 3: normative home (recommended a new
SPEC-design-elements.md, since the patterns catalog would bloat
SPEC-component); machine-readable element syntax (recommended parseable
body headings `### <ElementName> (<type>)` as single source of truth);
handling of gated [ST-0001](../stories/ST-0001-tier1-schema-suite.md)/[ST-0007](../stories/ST-0007-tier2-check-suite.md), to which today's decisions add
validation work (recommended amending before approval, since no approved
artifact is touched).

**T9 — Sponsor.** New SPEC-design-elements.md accepted. Story amendment
before approval accepted. On element syntax, asked: would a frontmatter
elements list *also* help, or just add noise?

**T10 — Agent.** Analysis: every real consumer parses the body anyway —
the check suite must validate obligations/IDs/citations in body
sections; the Graph Index is the sanctioned derived home for queryable
structure (per [DEC-0010](../decisions/DEC-0010-graph-index-derived.md)) and can expose element nodes; the Handoff
Manifest is compiled by tooling. A frontmatter mirror serves only a
hypothetical YAML-only consumer while costing dual maintenance and a new
drift failure mode. Recommended body headings only, Graph Index for
machine consumers; adding a derived frontmatter block later is a cheap
mechanical spec change if ever needed.

**T11 — Sponsor.** Confirmed: body headings only, no frontmatter mirror.

**T12 — Agent (synthesis).** Played back the eight decisions to record
(hybrid granularity; element-first layout; closed five-type taxonomy
with entity naming; typed obligations; modeling-patterns catalog;
Implementation Guidance split; SPEC-design-elements home; parseable
headings) plus the process call to amend [ST-0001](../stories/ST-0001-tier1-schema-suite.md)/[ST-0007](../stories/ST-0007-tier2-check-suite.md) before
approval.

**T13 — Sponsor.** Confirmed — record them.

## Decisions Produced

[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md),
[DEC-0081](../decisions/DEC-0081-element-first-contract-layout.md),
[DEC-0082](../decisions/DEC-0082-closed-element-type-taxonomy.md),
[DEC-0083](../decisions/DEC-0083-typed-contract-obligations.md),
[DEC-0084](../decisions/DEC-0084-modeling-patterns-catalog.md),
[DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md),
[DEC-0086](../decisions/DEC-0086-design-elements-spec-home.md),
[DEC-0087](../decisions/DEC-0087-parseable-element-headings.md)

## Conflicts Raised

None.
