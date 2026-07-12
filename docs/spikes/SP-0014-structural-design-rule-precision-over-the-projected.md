---
id: SP-0014
type: spike
title: "Structural design-rule precision over the projected corpus"
status: approved
approved-on: 2026-07-11
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Executed and complete at SES-0069 (2026-07-11). Question: do
  compiled structural rules fire true findings on the real design?
  The stakeholder expanded the rulebase at take-up from the planned
  ~12 rules to every structural rule the two curated sources
  worthily ground: 24 rules (14 discovery, 5 calibration with
  recorded expected outputs, 3 vacuous against current data, 2
  weak/proxy-grounding noise-rate probes), compiled as ActiveGraph
  behaviors and fired against SP-0013's re-established projection.
  Round-trip validation reproduced every SP-0013 structural baseline
  exactly. All five calibration instruments passed. 102 findings
  fired from 15 of 24 rules; the stakeholder disposed 33 as real or
  change-worthy, 9 as debatable, 60 as noise, with per-rule
  precision notes recorded. Precision proved strongly source-
  dependent: decision-compiled rules fired near-perfectly, prose-
  compiled rules produced most of the noise. The premise affirmed:
  findings included four ratified items citing superseded DEC-0014,
  three ungraduated multi-consumer elements, six happy-path-only
  contracts, and a numeric error in DEC-0359 -- none caught by the
  existing checker or gate process. ActiveGraph served only as a
  passive store; the spike yields no differential evidence for its
  reactive/fork machinery, deferring that question to SP-0016 and
  SP-0017. Two proposed decisions resulted: DEC-0367 (premise
  affirmed, source-dependent precision) and DEC-0368 (no
  differential reactive-substrate evidence). Follow-ups: IDEA-0035
  through IDEA-0040. Deliverable: complete findings catalog with
  dispositions.
links:
  impacts: [SP-0016, SP-0017]
  impacted-by: [SP-0013]
  derives-from: [EP-0009]
  relates-to: [SP-0013, DEC-0369, DEC-0370, DEC-0371]
cites: [DEC-0354, DEC-0351, DEC-0355, DEC-0335, DEC-0337, DEC-0345, DEC-0336, DEC-0315, DEC-0309, DEC-0299, DEC-0086, DEC-0358, DEC-0365, DEC-0359, DEC-0360, DEC-0088, DEC-0089, DEC-0092, DEC-0094, DEC-0096, DEC-0303, DEC-0306, DEC-0014, DEC-0242, DEC-0247, DEC-0356, DEC-0367, DEC-0368, DEC-0308, DEC-0234, DEC-0126]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Do compiled structural rules fire true findings on the real design? Concretely: when ~12 structural rules -- drawn half from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and half from Groundwork's own rule-type decisions (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order) -- are compiled as ActiveGraph behaviors and fired against SP-0013's projected graph, are the findings real, noise, or change-worthy?

## Why It Blocks

Blocks nothing today. It is the load-bearing evidence for the executable-design-knowledge idea (DEC-0354): if compiled structural rules mostly fire noise, the approach's central premise weakens regardless of ActiveGraph as substrate. SP-0016 (SP-D) and SP-0017 (SP-E) both depend on this spike's rulebase.

## Method

Hand-compile approximately 12 structural rules as ActiveGraph behaviors: roughly six from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and roughly six from Groundwork's own rule-type DECs (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order). Fire the rulebase against the graph SP-0013 projected. The stakeholder disposes every finding the rules produce -- real, noise, or change-worthy.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

The rulebase must position itself against DEC-0315's per-operation-checks-vs-full-checker-gate architecture: these rules are exploratory firing over a projection, not a replacement for the pre-commit gate. The structural contracts it validates are the ones SP-0013 projects -- DEC-0309's Uses-edges source-of-truth/depends-on projection and DEC-0299's typed Uses vocabulary (interface/implementation/test) -- and element-taxonomy/obligation checks defer to DEC-0086, which gives SPEC-design-elements ownership of that taxonomy.

### Expanded rulebase (SES-0069)

At take-up, the stakeholder directed expansion beyond the planned ~12 rules to every structural rule the two curated sources worthily ground (SES-0069 T9): the executed rulebase is 24 rules -- 14 discovery rules (including schema resolution per DEC-0089, test-double ownership and promotion-candidate detection per DEC-0306, staleness propagation per DEC-0096, seam-graduation candidates, bundle closure per DEC-0303, and best-practice rules for data reach-in, pass-through services, and happy-path-only contracts), 5 calibration rules with recorded expected outputs (item-citation completeness: SP-0013's 10 provenance edge cases; DEC-0309 projection equality: zero; bundle closure: the IDEA-0026 range dispute; fake-promotion candidates: DEC-0359's three; uncovered approved stories: the 19 known checker coverage warnings), 3 rules vacuous against current data (per DEC-0365's acknowledgment), and 2 weak/proxy-grounding probes retained deliberately as noise-rate tests. Contract-kind completeness checks follow DEC-0088's obligation matrix; Implements-coverage checks follow DEC-0092 and DEC-0094. Grounding-strength tags are recorded per rule; the best-practice corpus grounds its rules via practitioner sources, not Martin's named package principles.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): a complete findings catalog with the stakeholder's disposition on each (real / noise / change-worthy); per-rule precision notes (which rules fired only real findings, which fired noise, and why).

## Data-Source Assumptions

**Execution precondition (DEC-0358).** SP-0013's findings show zero typed `Uses:` lines exist anywhere in the corpus, so the dependency-cycle, stability-direction, and build-order rules in this spike's planned rulebase have no edge data to fire against today. Per DEC-0358, this spike's execution is deferred until the corpus-wide `Uses:` backfill is taken up and completed; it does not proceed with a reduced rulebase in the interim.

**Precondition met (DEC-0365).** SES-0066 executed the corpus-wide `Uses:` backfill (DEC-0359) and armed checker enforcement (DEC-0360): 71 typed edges now exist across the 15 conforming CMPs' 53 elements. DEC-0358's precondition is satisfied; SP-0014 is unblocked and may execute in its own future session. Note the qualifier distribution is 100% `(interface)`, zero `(implementation)` -- SP-0014's build-order/serialization rules will be vacuously satisfied against this data (an acknowledged, not blocking, consequence).

## Findings

Executed at SES-0069 (2026-07-11) by the facilitator under the re-confirmed read-only direct-parse sanction (SES-0069 T8/T11), all build artifacts confined to the session scratchpad per DEC-0351. The rulebase ran as 24 rules compiled per the Expanded rulebase subsection of Method, fired as ActiveGraph behaviors (activegraph 1.9.0, throwaway venv) over the re-established SP-0013 projection.

### Round-trip validation

The projection reproduced every SP-0013 structural baseline exactly: 16 Components, 53 Elements, 346 ContractItems (262 element-scoped / 38 C-n / 46 IG-n), 581 CITES, 65 IMPLEMENTS, 28 implemented stories, 140 cited decisions. Reaching 581 CITES required recovering SP-0013's exact counting conventions: bare IDs only (code spans excluded per DEC-0242) and item bodies bounded at bullet-plus-indented-continuations (column-0 prose after a bullet is section text, not item text). Two parser defects were found and fixed en route (wrapped `Uses:` continuation lines; item-body bleed into trailing prose), exercising the halt-on-mismatch test plan as designed.

Two baselines were revised against current corpus ground truth rather than SP-0013's snapshot: DEPENDS_ON is now 30 (was 26; explained by DEC-0359's both-directions reconciliation), and typed `Uses:` edges are **72, not the 71 DEC-0359 records** — confirmed by two independent counts with no component file modified since the backfill commit. The DEC-0359 numeric discrepancy is itself a change-worthy finding (routed to the record-repair Idea below). The qualifier distribution (100% `(interface)`) and the 20 `Uses: none` declarations match DEC-0359 exactly.

### Calibration results (5 instruments)

All five calibration gates passed before discovery findings were cataloged:

- Item-citation completeness fired **exactly** SP-0013's 10 recorded provenance edge cases.
- Uncovered-approved-stories fired **exactly** the 19 known checker coverage warnings (ST-0032..ST-0049, ST-0065).
- Test-double detection rediscovered **all three** DEC-0359 promotion candidates (after one in-run rule fix: the fakes live in prose form, not CamelCase — a compilation-fidelity lesson recorded below).
- DEC-0309 projection equality fired once instead of zero — the compiled rule omitted checker rule 20's element-less-doc carve-out, so it flagged CMP-0006 (the non-conforming stub). Kept in the catalog as compilation-fidelity noise: the substrate was right, the compilation was incomplete.
- Bundle closure fired zero, matching its revised expectation: the IDEA-0026 range dispute is invisible at edge grain because both written edges target the undisputed portion — the original "⊇1" expectation in the design presentation was itself corrected during execution (dispute detection needs declaration-comparison, not edge resolution).

### Findings catalog with stakeholder dispositions

102 findings from 15 of 24 rules; 9 rules fired zero. Dispositions per DEC-0355 (real / noise / change-worthy), taken at SES-0069 T17: recommendations accepted wholesale, change-worthy findings consolidated into follow-up Ideas IDEA-0035..IDEA-0038, debatable findings routed to the follow-up architecture-review session IDEA-0039.

**R1 dependency cycles — 1.** MechanicalWriteService → CheckSuite → MechanicalWriteService (intra-CMP-0001, element grain). Disposition: **debatable → architecture-review session** (IDEA-0039, paired with R23).

**R3 orphaned interfaces — 11.** Zero-inbound-`Uses:` services/protocols. Disposition: **noise (7)** for boundary roles the rule cannot see — HTTP-edge elements (ApiApplication, RestSurface, SessionSseEndpoint), protocol-implementing adapters consumed via their protocol (GitHubConnector, EmailNotifier, AuthProvider), and ReviewDelegationService; **debatable → architecture-review session (IDEA-0039) (4)** for the workflow services whose invocation wiring is genuinely unestablished: WorktreeManager, GovernanceInit, StalenessSweepService, ReaffirmationService. Precision note: the rule needs role modeling (edge/adapter/entry-point annotations) and protocol-indirection awareness to be usable.

**R5 fan-out hubs — 3.** StorageService, GitHubConnector, CompositionRoot (out-degree 5 each). Disposition: **noise (informational)** — a composition root's job is fan-out.

**R6 speculative contract items — 24.** A-items of consumed elements no consumer's `Uses:` targets. Disposition: **noise (all 24)** — the rule is incompatible with DEC-0359's ratified bare-element edge convention: one item-grain edge anywhere flags every sibling item of an otherwise element-grain-consumed element. Lowest-precision rule of the run.

**R7 item-citation completeness — 10 (calibration).** CMP-0004:StalenessSweepService.A-1, CMP-0005:CodeHostConnector.A-10, CMP-0005:HostEvent.B-1, CMP-0009:GitHubConnector.A-2/A-3, CMP-0011:RestSurface.A-1..A-4 (4 items), CMP-0014:KvStorePort.A-3. Disposition: **real (previously recorded by SP-0013)** → IDEA-0035.

**R8 superseded-decision citations — 4.** CMP-0005:CodeHostConnector.A-9, CMP-0005:C-1, CMP-0009:GitHubConnector.A-7, CMP-0009:C-2 — all citing superseded DEC-0014 (superseded by DEC-0308, whose scope-in of swarm orchestration is exactly what the repair must reconcile each item against). Disposition: **change-worthy (all 4)** → IDEA-0035, via DEC-0247's remediation path. Strongest discovery of the run: the exact SES-0026-class staleness the consistency machinery exists to prevent, present in ratified contracts and caught by no current checker rule.

**R11 projection equality — 1 (calibration, expected 0).** CMP-0006 depends-on/projection mismatch. Disposition: **noise (compilation infidelity** — missing element-less-doc carve-out; see Calibration above).

**R12 build-order tiers — 1.** Zero lifted implementation edges → no serialization constraints. Disposition: **noise (informational, vacuous by data** per DEC-0365's acknowledgment).

**R13 schema resolution — 10 findings, 9 distinct (one duplicate emission), 8 distinct tokens.** Unresolved A-item type tokens per DEC-0089: `UnitOfWork` (CMP-0003:AppDatabasePort.A-1), `QueueEntry` (CMP-0004:ReaffirmationService.A-2), `PrHandle` and `ReviewState` (CMP-0005:CodeHostConnector.A-3), `PermissionSet` (CMP-0005:CodeHostConnector.A-10 and CMP-0009:GitHubConnector.A-10), `WebhookHandle` (CMP-0005:CodeHostConnector.A-11), `DeliveryResult` (CMP-0008:NotifierConnector.A-1), `JobId` (CMP-0012:QueuePort.A-1). Disposition: **change-worthy (as a review list)** → IDEA-0036; heuristic parse limits acknowledged (some tokens may be inline-defined at sibling items).

**R14 test-double ownership — 5.** Disposition: **real (3)** — CMP-0005 (local-git fake connector), CMP-0008 (in-memory fake adapter), CMP-0009 (local-git fake parity tie), matching DEC-0359's flagged candidates → IDEA-0038; **noise (2)** — CMP-0001 and CMP-0004 hits are cross-references to CMP-0005's fake, not owned constructs.

**R16 seam-graduation candidates — 3.** SchemaValidator (consumed by CMP-0004, CMP-0016), StorageService (CMP-0004, CMP-0011, CMP-0016), GovernanceConfig (CMP-0004, CMP-0007) — multi-consumer elements not graduated to standalone CMPs. Disposition: **debatable → architecture-review session** (IDEA-0039); the graduation rule's letter says these graduate, and the gate-time graduation reviews did not surface them. Provenance context from the recall audit: GovernanceConfig already graduated once — DEC-0234 moved it to CMP-0016 to resolve a dependency cycle — so its R16 flag is a second-order graduation question, not a first-time oversight; SchemaValidator and StorageService trace to DEC-0126's thirteen-element decomposition of CMP-0001.

**R19 uncovered approved stories — 19 (calibration).** ST-0032..ST-0049, ST-0065. Disposition: **real (previously known)** — already continuously reported as checker coverage warnings; pipeline work, not a new Idea.

**R20 fan-in hubs — 3.** AppDatabasePort (8), SecretStore (8), MechanicalWriteService (6). Disposition: **noise (informational)** — ports are supposed to have high fan-in; the weakly-grounded rule behaved as predicted.

**R23 pass-through service — 1.** CheckSuite (CMP-0001, one consumer, one dependency). Disposition: **debatable → architecture-review session** (IDEA-0039, paired with R1's cycle through the same element).

**R24 happy-path-only contracts — 6.** BranchOrchestrator, WorktreeManager (CMP-0001); GovernanceInit, StalenessSweepService (CMP-0004); EmailNotifier (CMP-0008); SessionSseEndpoint (CMP-0011) — no error/failure language in any A/B item. Disposition: **change-worthy (all 6)** → IDEA-0037.

**Meta-finding.** DEC-0359 records 71 typed edges; the corpus carries 72. Disposition: **change-worthy** → IDEA-0035.

**Silent rules — 9.** R2 stability direction (no inversions at the 0.25 margin), R4 implementation coupling and R22 data reach-in (the acknowledged vacuous pair), R9 contract-kind completeness, R10 implements coverage/bidirectionality, R15 staleness propagation, R17 bundle closure, R18 deferred-only elements, R21 mutual component coupling — all zero. R9/R10/R15/R17/R21 at zero are corpus-health confirmations on invariants the checker does not (or only partially) enforces.

Disposition totals: 33 real/change-worthy (routed to IDEA-0035, IDEA-0036, IDEA-0037, IDEA-0038), 9 debatable (routed to IDEA-0039), 60 noise (41 substantive noise + informational/vacuous), with per-rule precision notes above.

### Per-rule precision verdict

Precision was strongly **source-dependent**. Rules compiled from Groundwork's precisely-written accepted decisions were near-perfect: every calibration exact, R8's discoveries all real, and the single R11 misfire traceable to incomplete compilation of a documented carve-out, not to the rule's source or the substrate. Rules compiled from prose best practices were noisy: R6 produced 24 convention-mismatch false positives, R3 was blind to boundary roles and protocol indirection (7 of 11 noise), and the deliberately weak probes (R20 fan-in, R23 pass-through at n=1) behaved exactly as their grounding-strength tags predicted. Both in-run rule defects (R14's CamelCase-only scan, R11's missing carve-out) were compilation-fidelity failures — the corpus text was right and the executable rendering incomplete — direct corroborating evidence for SP-0015's prose-to-rule fidelity concern from the structural side.

### Feasibility assessment: what this reveals about ActiveGraph for this project

Recorded per stakeholder instruction (SES-0069 T17), from the facilitator's assessment at T16:

**The program's central premise survived its test.** DEC-0354's bet was that design rules compiled into executable form fire true findings on a real corpus. They did: roughly two dozen real or change-worthy findings that twenty checker rules and the human gate process had not caught — four ratified items citing a superseded decision, three multi-consumer elements the mandatory graduation reviews missed, six services with happy-path-only contracts, and a numeric error inside DEC-0359 itself. The graduation misses are the sharpest example: the process rule existed, gate reviews ran, and "citing a rule is not applying it" happened anyway. Mechanical enforcement caught what process discipline leaked. Had the rules fired mostly noise, the premise would have weakened regardless of substrate; the opposite happened.

**About ActiveGraph specifically, the spike reveals less than it looks.** ActiveGraph served as a passive store: the projection loaded cleanly, 102 finding objects landed as typed nodes, and expressiveness was never a constraint (consistent with SP-0013). Feasibility in the "no blockers" sense is confirmed. But the rulebase fired as one batch behavior running plain graph queries; nothing exercised what makes ActiveGraph distinctive — reactive behaviors firing incrementally on graph mutations, event-sourced replay, run forking. Everything this spike did could have been done with dictionaries or by extending tools/check_links.py. The evidence that would justify ActiveGraph specifically — rules re-firing cheaply as the corpus changes rather than batch re-scanning, and fork-a-run/what-if diffing — is exactly SP-0016's and SP-0017's territory.

**Benefits, conditionally.** If the DEC-0356-deferred option survey eventually lands in its favor: continuous contract-grain enforcement of rule-type decisions that today live only in process memory (the superseded-cite/staleness/graduation family — a grain the artifact-level checker does not reach); a standing element/item-grain structural query surface; and provenance-carrying findings (each finding object can cite its rule's source decision). But batch-mode structural checking demonstrably does not need a reactive graph runtime, so the thin owned implementation DEC-0356 mandates comparing remains a real competitor; ActiveGraph earns its place only if SP-0016/SP-0017 show the reactive/fork machinery paying for itself.

**Data caveat carried forward.** With 100% `(interface)` edges, the build-order, serialization, implementation-coupling, and data-reach-in rules remain untested against data that could make them fire — that slice is unmeasured, not confirmed.

### Evidence retention

Per stakeholder instruction (SES-0069 T17), the run's evidence files are left in place in the session scratchpad (`sp0014/findings.md`, `sp0014/findings.json`, `sp0014/sp0014.py`, plus the throwaway venv) and are not committed, per DEC-0351. The scratchpad is session-scoped and volatile; this Findings section is the durable record of the complete catalog and dispositions. A durable spike-results retention policy is IDEA-0040's question, not decided here.

## Resulting Decisions

Two decisions resulted, both recorded **proposed** (stand pending confirmation at the DEC-0354/DEC-0355 spike-program gate):

- **DEC-0367** — Compiled structural rules fire true findings; precision is source-dependent. SP-0014's question is answered affirmatively: 102 findings, 33 disposed real/change-worthy, none caught by the existing checker or gate process. Precision is strongly source-dependent between decision-compiled and prose-compiled rules.
- **DEC-0368** — SP-0014 produced no differential evidence for a reactive substrate. The rulebase exercised ActiveGraph only as a passive store; the DEC-0356 option survey must weigh SP-0016 and SP-0017's evidence on the reactive/fork question, not this spike's.

