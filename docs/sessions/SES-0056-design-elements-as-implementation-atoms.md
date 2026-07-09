---
id: SES-0056
type: session
title: Design elements as the atomic units of implementation
status: open
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Took up the SES-0055 T9 proposal (design elements as atomic
  implementation units) through two dual-instance system-architect
  consultations and a one-by-one decision walk, yielding
  DEC-0297..DEC-0309: the dual-granularity model (element = terminal
  specification/dispatch atom with gate-checked atomicity; component =
  unchanged gate/coherence unit — DEC-0080 narrowed, not superseded);
  mandated typed Uses: lines (interface | implementation | test) with
  exact projection to component depends-on and strongest-member-wins
  edge lifting; work packages as generated dispatch bundles with a
  principled batching criterion and Shared Preamble; per-component
  integration work packages; Slices as a new first-class artifact type
  (SL-, owning end-to-end acceptance criteria); empty-context
  semantics extending DEC-0011; manifest ownership (EP-0001
  generation, EP-0004 topology, EP-0008 endpoint — resolving
  IDEA-0006's core); test doubles owned by the contract-owning
  component; the bounded-context grouping principle codified
  (vertical-slice regrouping rejected unanimously); and — the largest
  change — swarm orchestration entering v1 scope as a full deliverable
  (DEC-0308 supersedes DEC-0014; ingestion deferred; SP-0012
  chartered). Executed: SPEC-handoff-manifest v2, SPEC-slice,
  SPEC-design-elements extension, nine glossary entries, gated
  BG-0001/EP-0001/EP-0004/EP-0008 amendments, sweeps clean. Open:
  gate approvals, Uses: retrofit, SP-0012 run.
links:
  relates-to: [SES-0055, IDEA-0006, IDEA-0009, DEC-0011, DEC-0014,
               DEC-0136]
---

# SES-0056: Design Elements as Implementation Atoms

## Purpose

Refine the SES-0055 T9 stakeholder proposal under the change-intake
protocol: make the design element (currently the typed
`### <Name> (entity|value|service|event|protocol)` structure inside
Component Docs) the atomic unit of implementation handoff, and
reconsider its name. Touches DEC-0011 (contract-completeness unit),
DEC-0014 (manifest handoff), SPEC-component, SPEC-handoff-manifest,
and DEC-0136 (element graduation). The granularity-sensitive SES-0055
dispositions (IDEA-0006; IDEA-0009 F5/F9) resolve under this
session's outcome.

## Transcript

**T1 — Stakeholder.** Verbatim proposal (raised at SES-0055 T9): "I
would like to propose that we treat what we've named 'design
elements' as the atomic units of implementation. Atomic in the sense
that they don't need to be broken down any further. There are no
internal dependency relationships that can lead to implementation
race conditions. They are the most logical items to handoff to an
agent (with initially empty context) for implementation because of
the feasibility of self-contained, fully specified documentation. I
raise this proposal now because I believe it will impact the rest of
the decisions that we need to make for the dispositions surfaced from
the architecture review." Followed by: "We may want to reconsider the
naming."

**T2 — Facilitator.** Restatement (carried from SES-0055 T10): the
design element becomes the unit of implementation handoff, defined by
(1) terminal decomposition, (2) no internal dependencies — all
sequencing lives between elements, so parallelism is governed by the
inter-element graph, (3) empty-context implementability via
self-contained fully-specified documentation. Component docs shift
from "the deliverable" to the grouping/context layer;
contract-completeness (DEC-0011) re-anchors at element level;
build-order and manifest granularity move to elements; "design
element" may be renamed. Flagged tensions to grill: DEC-0011's
sanctioned crawlable-provenance fallback vs strict self-containment;
how atomicity is verified (DEC-0136 graduation as enforcement
point?); whether inter-element dependencies are captured well enough
to sort on.

**T3 — Stakeholder.** Confirmed the T2 restatement matches intent;
instructed proceeding to grilling with a system-architect
dual-instance consultation.

**T4 — Facilitator.** Locate-first (DEC-0266): semantic search
surfaces the governing prior record — DEC-0080 (hybrid CMP
granularity; "one CMP per element" was a considered-and-rejected
alternative — gate explosion, incoherent piecemeal approval),
DEC-0081 (element-first contract layout, element-scoped item IDs),
DEC-0082 (closed five-type taxonomy), DEC-0136 (element-graduation
review), SES-0012 (created SPEC-design-elements.md). Working
hypothesis: the proposal is plausibly orthogonal to DEC-0080 —
that decision fixed documentation/gate granularity at the component,
while this proposal moves implementation/handoff granularity to the
element; whether it narrows or supersedes DEC-0011 (crawlable
provenance fallback) and DEC-0014/SPEC-handoff-manifest (component
build-order) is a grilling subject. Corpus inventory: 53 elements
across 16 CMPs (25 service, 15 value, 6 protocol, 4 entity,
3 event), every element carrying Implements: story links. Spawned
the DEC-0293 dual-instance advisor consultation (record-grounded
and best-practice-independent, strongest model with explicit
override) on: conflict-vs-complement with the record, whether the
three atomicity properties hold for today's elements and how they'd
be verified, inter-element dependency capture for an element-level
build-order, self-containment vs the DEC-0011 crawl fallback,
granularity economics of 53 element-grain handoffs, integration
ownership, and naming.

**T5 — Facilitator (system-architect consultation — opening
positions).** Record-grounded instance: proposal sound and
complementary to DEC-0080 (which rejected one-doc-per-element on the
ratification axis only), but three claims need tempering — elements
are not inter-dependency-free today (CMP-0001 prose evidence:
StorageService.A-2 runs SchemaValidator.A-1, BranchOrchestrator.A-1
allocates via IdAllocator, StorageService.A-3 delegates to
MechanicalWriteService); DEC-0080's rationale sentence anchoring the
build-and-test unit at CMP needs an explicit narrowing DEC; and
"empty context" must mean empty conversational context with
pinned-corpus crawl preserved, else it silently supersedes DEC-0011's
sanctioned fallback. Recommended dual-granularity: element = atom of
specification/tracking, manifest work units batched by cohesion rule,
per-component integration unit owning C-n invariants and acceptance
expectations, mandated Uses: line, EP-0004-derived edges, atomicity
verified by extending the DEC-0136 review plus a mechanical
bundle-closure check (DEC-0089 precedent). Supersession inventory:
SPEC-handoff-manifest superseded; DEC-0011 and DEC-0136 extended;
DEC-0080 rationale narrowed; DEC-0081/0082/0087/0088/0089/0092/0014
untouched. Flagged: manifest ownership (IDEA-0006, critical) should
be settled in this session; element topo-order tensions with
walking-skeleton vertical slices. Independent instance: directionally
sound but the proposal conflates three roles — unit of work
assignment (right at element grain), unit of contract completeness
and unit of integration/verification (both belong at component
grain); same CMP-0001 dependency evidence independently found;
criterion restated as "no unspecified deps"; recommended the same
two-tier model with generated (never authored) bundles, batching of
trivial values, typed dependency edges so interface deps don't
serialize the build (stub-from-contract), a per-component assembly
task, a swarm-wide shared preamble, and a cold-start probe as the
atomicity fitness test. Risks ranked by both: integration-ownership
vacuum; prose-only sibling couplings must become pinned references;
bundle duplication/drift if authored; over-fragmentation without a
batching rule; DAG mis-typing causing false serialization.

**T6 — Facilitator (consultation — rebuttal round and joint
proposal).** One rebuttal round produced convergence on: dual
granularity (element = dispatch/spec atom, CMP = gate + assembly
unit, both unchanged as authored artifacts); mandated Uses: line with
edge-type qualifier, only implementation edges serializing
build-order; generated work bundles (element contract block +
component Purpose/language + relevant C-n/IG-n + interface-dependency
contract blocks + glossary slice) referencing one generated Shared
Preamble (reference stack DEC-0018, error model DEC-0127, repo
conventions); slice-scoped handoff sets in the manifest so vertical
walking-skeleton slices override horizontal topo-layers; atomicity as
gate-checked obligations (DEC-0136 checklist extension + tier-2
bundle-closure check); empty-context = empty conversational context,
pinned-corpus crawl sanctioned (DEC-0011 extension); keep the name
"design element" for the design-time construct; settle manifest
ownership in-session (joint recommendation: EP-0001 owns the manifest
as a generated store artifact, EP-0004 supplies graph-derived
topology — updating the SES-0055 T8 recommendation). Three points
left to the stakeholder: (1) name of the generated dispatch artifact
— "work package" vs "element task"/"assembly task" (the instances
swapped positions in rebuttal, each conceding to the other);
(2) entity batching — standalone (record-grounded final position:
entities are testable domain modules; enforcement by a service is a
consumer edge) vs the principled criterion "standalone iff it carries
self-contained implementable A/B items" (independent final position);
(3) edge-type vocabulary — two types now (interface/implementation,
test-time deferred until test-double ownership is designed;
record-grounded, grounded in DEC-0085 Notes being non-normative) vs
three types now (independent). Verdict presented to the stakeholder
as a proposal with an eight-decision ratification list.

**T7 — Stakeholder.** Ratified the core dual-granularity model as
recommended. Open calls: (1) the generated dispatch artifact is named
**work package** (two kinds: element work package, integration work
package; "task" avoided for collision with the work-management
domain); (2) batching by the **principled criterion** — an element is
a standalone work package iff it carries self-contained implementable
A/B items (not solely enforcement of another element's contract);
values/events typically ride with their primary consumer, entities
typically qualify standalone, protocols always standalone; applied by
the manifest generator, never hand-tagged; (3) **three edge types
now** — Uses: qualifiers (interface|implementation|test), rejecting
the facilitator's defer-test recommendation, which forces test-double
ownership to be settled in-session.

**T8 — Facilitator.** Grilling round 2 (consequences of T7):
(a) manifest ownership — recommended the joint consultation position:
EP-0001 owns generation/validation/write of the manifest as a
generated store artifact, EP-0004 supplies graph-derived topology via
declared dependency, EP-0008 exposes the trigger endpoint (revising
the SES-0055 T8 facilitator recommendation); (b) test-double
ownership — recommended: a test double is a design element of the
component that owns the contract it fakes, promoted from
non-normative Notes (DEC-0085) via normal component amendment when
first (test)-referenced.

**T9 — Stakeholder.** Both accepted as recommended: manifest
ownership EP-0001 + EP-0004 topology + EP-0008 endpoint (resolves the
IDEA-0006 core question; the DEC-0194 coverage-pass rerun remains
queued there); test doubles owned by the contract-owning component's
element.

**T10 — Stakeholder.** Distillation of the proposed DEC-0297..DEC-0306
held. Verbatim: "I think we should spend time grilling the principles
of grouping design elements into components. Should we strive for
coherent vertical slices that enable end-to-end design and testing of
an integral part of the system?" Instructed: "Seek advice from the
architects."

**T11 — Facilitator.** Opened a second advisor consultation with the
same dual-instance pair (rebuttal rounds reset). Framing given:
today's 16 components are subsystem/port/connector-shaped
(bounded-context within their epics), not vertical slices; the
question interacts with the held DEC drafts — what an integration
work package verifies (horizontal invariants vs end-to-end behavior),
whether manifest slice sets (DEC-0302 draft) suffice as the E2E unit,
re-grouping cost against 15 approved CMPs, and DEC-0080's
gate-economics rationale. Both instances asked for grouping
principles (cohesion axes: common closure, conceptual cohesion,
contract stability, end-to-end testability), a verdict on
component-as-vertical-slice, candidate principles (pure vertical /
bounded-context + slice overlay / hybrid), and grilling questions.

**T12 — Facilitator (system-architect consultation — component
grouping principles).** Both instances converge without needing a
rebuttal round: keep bounded-context grouping; do not re-cut the
component inventory. Record-grounded: the principle is explicit, not
emergent — SPEC-component's opening line ("aligned with a DDD-style
bounded context"), DEC-0080's "bounded-context-scale" anchor, the
four context: values (canonical-store, governance, integration,
platform), and DEC-0126's element-per-story alignment; seams serve
multiple flows (CMP-0003 consumed by store and governance; CMP-0002
emitted by store, consumed by governance/graph), so vertical slices
would duplicate contracts or blur seam governance — DEC-0080's
graduation rationale at full force; the just-ratified mechanisms
(manifest slices for dispatch, integration work packages for
per-component verification, SPEC-story Component Impact sections for
the vertical path) already answer the vertical question at
dispatch/verification time. Independent: vertical regrouping violates
common closure (ports change for infrastructure reasons, rules for
policy reasons) and bounded-context cohesion (one model, one language
per doc — CMP-0001 speaks artifact/branch/worktree, CMP-0004 speaks
gate/policy/arbiter); ~12 of 16 components are substrate; the real
end-to-end flows number about four (run a session, gate an artifact,
emit a manifest, resolve a conflict) and span 4-6 CMPs regardless of
grouping. Both recommend codifying the grouping principle as an
explicit decision. One divergence, presented as alternatives:
where E2E acceptance criteria live — independent: slices must be
owned spec constructs with acceptance blocks or nobody writes the
E2E test; record-grounded: cross-CMP acceptance is orchestrator
territory per DEC-0014. Facilitator synthesis offered: slice
definitions in the manifest carry acceptance criteria (specification
content, in scope), while executing them remains the swarm's
responsibility (DEC-0014 untouched).

**T13 — Stakeholder.** (1) Ratified the bounded-context grouping
principle as an explicit decision; the 16-component inventory stands.
(2) On the E2E divergence, sided with the independent instance in
full — slices become first-class owned artifacts with acceptance
criteria and their own lifecycle — and raised new change intent,
verbatim: "I also want to supersede the decision that swarm
orchestration is out of scope. We need it on the table in v1 so we
can properly think about manifest design." (3) On distillation:
review the decision drafts one by one before acceptance.

**T14 — Facilitator.** Impact analysis on DEC-0014: cited by BG-0001
(swarm orchestration sits in its out-of-scope list), EP-0005,
CMP-0005, CMP-0009 — supersession requires a gated BG-0001 scope
amendment plus consistency review of citers. Scope-depth grilling:
recommended "specify + reference implementation" (protocol +
reference adapter pattern, CMP-0005/CMP-0009 precedent); alternatives
full deliverable / design-input-only. Vehicle: recommended
supersession DEC + gated BG amendment + orchestration-model spike in
this session, epic derivation after the spike reports.

**T15 — Stakeholder.** Chose **full deliverable** — Groundwork v1
ships a production implementation-swarm orchestrator as a
first-class product capability (stronger than the facilitator's
recommendation, explicitly). Vehicle as recommended: supersession DEC
+ gated BG-0001 amendment + spike SP-0012 defining the orchestration
model (which must run far enough to constrain the manifest/slice
contracts); epic derivation (new epic vs extension) follows the
spike through normal gates.

**T16 — Facilitator.** One-by-one decision walk (drafts DEC-0297..
DEC-0308 presented in three batches) interleaved with a grilling
thread the stakeholder opened at the DEC-0299 review: consistency
between element-level Uses: edges and component-level depends-on
("if element A in component X uses element B in component Y, then X
uses Y"). Grilled: authority between the levels (recommended exact
projection, checker-enforced both ways), type lifting (recommended
strongest-member-wins, implementation > interface > test), epic
lifting (recommended report-don't-enforce, preserving DEC-0026
impact-edge semantics), enforcement locations (recommended
check_links now, product tier-2 later). Elaborations delivered on
request: "lifting"/"lifted edge" (deriving a coarse-grained edge from
fine-grained ones; the component edge as the shadow of member element
edges) with worked type-lifting example, and "closure axis" (Common
Closure Principle; the shared reason-for-change a component is closed
under — CMP-0001/storage model, CMP-0009/GitHub API surface,
CMP-0004/governance semantics; a flow-shaped component holds four
unrelated change-reasons and is closed under nothing). Both terms
queued for CONTEXT.md.

**T17 — Stakeholder.** Accepted all thirteen decisions: DEC-0297,
DEC-0298, DEC-0300, DEC-0301, DEC-0302, DEC-0303, DEC-0304, DEC-0305,
DEC-0306 as recommended; DEC-0299 accepted with the edge-projection
addition (distilled as DEC-0309: exact projection,
strongest-member-wins type lifting, epic-level report-don't-enforce,
checker now + product later); DEC-0307 accepted after the
closure-axis elaboration; DEC-0308 accepted with feedback-loop
ingestion explicitly deferred (revisited on SP-0012's findings).

**T18 — Facilitator.** Distillation executed: DEC-0297..DEC-0309
recorded as accepted; DEC-0014 marked superseded by DEC-0308.
Artifact work executed in-session: SP-0012 chartered (orchestration
model, draft); gated BG-0001 scope amendment (orchestrator in,
ingestion out, outcome 4 reworded to orchestrated empty-context
dispatch); gated EP-0001/EP-0004/EP-0008 scope amendments per
DEC-0305; SPEC-handoff-manifest superseded (manifest-version 2: work
packages, typed depends-on, slices, Shared Preamble, seven rules);
SPEC-design-elements extended (mandated Uses: line, qualifiers,
projection, atomicity gate checks); SPEC-slice created (SL- artifact
type); CONTEXT.md glossary gained Swarm Orchestrator, Work Package,
Integration Work Package, Shared Preamble, Slice, Empty Context,
Lifted Edge, Closure Axis, Uses; IDEA-0006 narrowed to the
coverage-pass rerun + emission stories. Consistency sweep over the 13
DECs (48 citer hits) dispositions: DEC-0080 citers (CMP-0001..0005,
ST-0001) — cite granularity/graduation, unaffected by the DEC-0298
rationale narrowing, consistent; DEC-0011 citers (BG-0001, CMP-0001,
ST-0007) — crawl fallback survives per DEC-0304, consistent, but
ST-0007's tier-2 suite gains new checks (Uses: validation, bundle
closure, projection) — amendment queued with the retrofit work;
DEC-0081 citers — Uses: line is additive to the element layout,
consistent pending retrofit; DEC-0026 citers (epics, ST-0045) —
DEC-0309 explicitly preserves impact-edge semantics
(report-don't-enforce), consistent; DEC-0014 citers — BG-0001
re-pointed in the gated amendment; EP-0005/CMP-0005/CMP-0009 cite it
for boundary framing that DEC-0308 preserves (manifest remains the
boundary contract) — re-point citations at next touch, no content
drift. Terms check: one finding (DEC-0304/DEC-0305 shared
canonical-ref unlinked) — fixed by adding the sibling link. Remaining
queued follow-on: Uses: retrofit across 53 elements + check_links
projection check (blocked on retrofit), ST-0007 amendment, CMP-0001
tier-2 amendment, slice derivation, SP-0012 run, epic home for the
orchestrator.

**T19 — Facilitator.** Decision-recall audit on the amended BG-0001
(12 candidates, one Sonnet judge). Ten NO-GAP (epic/story/component-
level, correctly absent from a boundary-level goal). Findings
addressed: (1) DEC-0104 — the Process Flow's uncited claim that only
epics/stories/spikes carry deferred + release is exactly DEC-0104's
content; cited at the sentence. (2) Judge flagged DEC-0050 (BBDC sole
v1 connector) against the Context Diagram's "GitHub/Bitbucket" —
facilitator verification showed DEC-0172 (accepted, later) swapped v1
to GitHub cloud with BBDC deferred behind TRG-0010; resolved by
citing DEC-0172 on the external-dependency item, not DEC-0050. Noted
for a future hygiene pass: DEC-0050's status is still accepted though
DEC-0172 displaced its choice. (3) Judge's contract-sync catch:
System Context item 4's output contract had not been updated for the
scope amendment — extended with the Handoff Manifest and Swarm
Orchestrator outputs (DEC-0300, DEC-0302, DEC-0308). BG-0001 remains
gated awaiting approval.

## Decisions Produced

- DEC-0297 — dual-granularity implementation model (element dispatch
  atom / component gate unit)
- DEC-0298 — narrowing of DEC-0080's rationale
- DEC-0299 — mandated typed Uses: line (interface | implementation |
  test)
- DEC-0300 — work package as manifest dispatch unit; batching
  criterion; Shared Preamble
- DEC-0301 — integration work package per component
- DEC-0302 — Slice as a first-class artifact type (SL-, SPEC-slice)
- DEC-0303 — atomicity verification (DEC-0136 checklist extension +
  bundle-closure check)
- DEC-0304 — empty-context semantics (extends DEC-0011)
- DEC-0305 — Handoff Manifest ownership (EP-0001 + EP-0004 topology +
  EP-0008 endpoint)
- DEC-0306 — test-double ownership (contract-owning component's
  element)
- DEC-0307 — bounded-context grouping principle codified
- DEC-0308 — swarm orchestration in v1 scope as full deliverable
  (supersedes DEC-0014; ingestion deferred)
- DEC-0309 — edge projection and lifting (exact typed projection;
  epic-level report only)

## Conflicts Raised

None yet.
