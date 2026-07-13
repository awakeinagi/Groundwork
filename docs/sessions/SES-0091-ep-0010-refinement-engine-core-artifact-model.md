---
id: SES-0091
type: session
title: "EP-0010 refinement — Engine Core & Artifact Model"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-13
participant: awakeinagi@gmail.com
participant-role: stakeholder/sponsor
facilitator: Claude Code facilitator (claude-fable-5)
transcript-fidelity: reconstructed
kind: full
intake: {origin: user, proposed-by: awakeinagi@gmail.com}
overview: >-
  Closed full refinement session for EP-0010 (Engine Core & Artifact
  Model), the foundation epic of the BG-0002 sibling set. Opened
  with the required dual-instance system-architect advisor
  consultation, which the stakeholder ratified after rebuttal-round
  convergence on the enforcement line, hexagonal layering,
  specification-first resolution, and a calibration-spike-then-
  fitness-function synthesis, plus a resolved adapter-implementation
  nuance (app-level divergence under maintained feature consensus).
  Two grilling rounds followed: round 1 (API contract locus, rule-
  family hosting, concurrency, schema versioning); round 2
  (structured diagnostics, type-roster ownership, two derived
  spikes). All thirteen decisions were confirmed and recorded as
  accepted (DEC-0475..DEC-0487). SP-0019 (schema-migration
  mechanism) and SP-0020 (performance calibration) were commissioned
  and, at gate, ratified through the required draft-gated-approved
  walk. At gate prep, a dual-instance reviewer consultation
  converged on READY-WITH-NOTES after an incident: a librarian task
  wrote outside the typed API and then ran a forbidden git checkout,
  reverting EP-0010's uncommitted rewrite; the rewrite was re-
  applied through the typed write path and verified byte-faithful,
  with the violation disclosed honestly. The recall-audit's DEC-0135
  finding was resolved with a citation and reciprocal relates-to
  link; the consistency sweep's 53 hits were triaged consistent,
  with the DEC-0121 cleanup folded into the deferred BG-0001
  reframing per DEC-0441. The stakeholder approved three reviewer
  amendments and approved EP-0010 through in-refinement, gated,
  approved (2026-07-13), closing this session.
links:
  relates-to: [EP-0010, DEC-0475, DEC-0476, DEC-0477, DEC-0478, DEC-0479, DEC-0480, DEC-0481, DEC-0482, DEC-0483, DEC-0484, DEC-0485, DEC-0486, DEC-0487, SP-0019, SP-0020]
---

# SES-0091: EP-0010 refinement — Engine Core & Artifact Model

## Purpose

This session refines EP-0010 (Engine Core & Artifact Model), the foundation epic of the BG-0002 sibling set derived at SES-0089, from draft toward gate. It opens with the required system-architect advisor consultation, then grills the epic's carried open questions: the Engine-authoritative vs. skill-convention rule line, the DEC-0121 port-ownership overlap with the BG-0001 track, the eight Interfaces & Contracts to Define, and spike candidates (checker/graph performance at scale).

## Transcript

### T1 (stakeholder, verbatim proposal)

Let's refine EP-0010

### T2 (facilitator, restatement)

Restating the intent as a full refinement session on EP-0010, the foundation epic of BG-0002's derived set — it impacts all seven siblings and its impacted-by list is empty, making it first in refinement order. The draft carries a set of open questions: the Engine-authoritative versus skill-convention rule line, the DEC-0121 port-ownership overlap with the BG-0001 track, the eight Interfaces & Contracts to Define, and a performance spike candidate (checker/graph performance at scale). Before proceeding, a housekeeping flag: SES-0090 and DEC-0472 through DEC-0474 appear uncommitted in the working tree; recommend closing and committing that work before opening this session.

### T3 (stakeholder, alignment)

Confirmed "Yes, full session" via the structured card. On the housekeeping question, answered via free text that SES-0090 had already been closed out and its work committed. The facilitator verified this against commit 1f496c1; one leftover file — the artifact-librarian's behavioral-memory SKILL.md, carrying operational learnings from the SES-0088/SES-0089 batches — remained uncommitted and was committed as housekeeping (commit a7dd3f7), leaving a clean tree. Session opened at this alignment.

### T4 (facilitator)

Opened the refinement with the required system-architect advisor consultation (DEC-0292, DEC-0293), dual-instance. The record-grounded instance proposed: an enforcement line at Engine self-trust (write-time enforcement only for invariants whose violation the Engine's own operations cannot survive; all other rules as checker rule families per DEC-0469); EP-0010 defining port contracts with the BG-0001 epics keeping adapter ownership (consumer-driven contracts); kernel/port/adapter hexagonal layering; compatible-extension versioning with tolerant readers, formal versioning deferred to the first non-CLI consumer per DEC-0423; three epic-level contracts; no performance spike yet (a monitored fitness function instead); a schema-migration spike; and specification-first resolution of the DEC-0346/DEC-0422 two-descriptions coexistence. The best-practice-independent instance proposed the same enforcement principle and layering, but: absorbing the old-track ports into the Engine outright (single interface owner); five epic-level contracts including the schema contract, concurrency write path, and compliance definition; and a performance calibration spike. In the rebuttal round the record-grounded instance RECONCILED ports (EP-0010 owns the port contract definitions; default adapters in-Engine via the existing embedded stack per DEC-0102; BG-0001 epics as future alternative-adapter providers) and CONCEDED the performance spike (an uncalibrated fitness threshold is a wish, not a gate; the spike calibrates it), while the independent instance CONCEDED ports the other way (absorbing would reach across a goal boundary and pre-empt the deferred BG-0001 rechartering, DEC-0441) and CONCEDED the spike toward the fitness function — crossed concessions the facilitator synthesized as: calibration spike sets the threshold, fitness function then monitors. On the contract set both converged on "contract SHAPES settle at epic level, details at story/component level", with the record-grounded instance additionally conceding the concurrency write path to epic level. The facilitator presented the joint verdict as items A–F (enforcement principle; hexagonal layering and versioning posture; specification-first; EP-0010 port-contract ownership; two spikes with the calibration synthesis; five epic-level contract shapes) for stakeholder ratification, plus the one residual nuance: whether default adapter implementations live in-Engine or with EP-0004/EP-0007.

### T5 (stakeholder)

Ratified verdict items A–F in full. On the adapter nuance, answered by free-text note rather than either listed option: "With a note that the app may decide to use it's own DBs and embeddings. E.g. we don't want to ship agent skills that require people to host their own Neo4J DB. So we should allow the app to diverge on implementation details, but maintain consensus on feature support."

### T6 (facilitator)

Grilling round 1 — four questions with recommendations: (1) API contract locus — recommended the kernel operation catalog as normative with the gw CLI as reference adapter, over CLI-surface-as-contract; (2) rule-family hosting shape — recommended rule logic as Engine code with declarative policy config (the governance/*.yaml pattern, DEC-0263), over fully-declarative rules (a de facto extension point in tension with DEC-0470) and everything-in-code; (3) ratifying the SES-0079-verified write-path model (per-artifact if-match optimistic locking, atomic recoverable batches; DEC-0411..DEC-0416) as the Engine's contracted concurrency invariant model — recommended ratify; (4) schema version locus — recommended a corpus-level version marker over per-artifact stamps.

### T7 (stakeholder)

Asked for elaboration on the API-locus and concurrency questions; left rule hosting unanswered; on the version-locus question attached the note: "And we will use semantic versioning."

### T8 (facilitator)

Elaborated. API locus: spec'd the same operation (edit-section) both ways — as a kernel-op contract with typed inputs and enumerated errors that CLI, MCP, or app-backend adapters bind 1:1, versus a CLI contract of flags/exit-codes/stdout that future consumers must subprocess-wrap — and connected the choice to EP-0011/EP-0012/EP-0013 consumption and the ratified specification-first posture. Concurrency: walked the verified model through a two-writer collision (token read, first-writer-wins apply, second writer refused and re-reads; atomic batches; write-recover restoring pre-batch bytes), laid out alternatives (pessimistic locking with lock-leak problems; git-native merge that bypasses typed-write guardrails by merging textually; CRDTs as keystroke-scale overkill), and named what EP-0015 consumes from ratification. Gave a short rule-hosting elaboration. Captured SemVer as the settled numbering scheme and re-presented all four cards.

### T9 (stakeholder)

Selected the kernel operation catalog as the contract locus. Selected the corpus-level version marker. On rule hosting: "Please elaborate. I'm not following." On concurrency: "Let's deferr this decision until after SP-0018's work is done. Wouldn't that handle this?"

### T10 (facilitator)

Read SP-0018's charter and reported the dependency runs the other way: SP-0018 is chartered as the worktree-scale counterpart to the single-session write model — it presumes the single-session invariants and explores the multi-session layer above them, so even a negative SP-0018 finding would leave the base model standing. Proposed the split: ratify the single-session invariants now (EP-0015's base entitlements; what SP-0018 builds on), defer multi-session semantics by name to SP-0018's findings. Re-explained rule hosting from the ground up with concrete rules and the "spikes must declare a timebox" worked example across three worlds: rules-in-code with settings-in-config (today's governance/*.yaml pattern; policy edits are config commits, new rule logic is a deliberate Engine change), rules-as-data (Engine ships a rule interpreter; complex structural rules strain the language and a rule DSL is an extension point DEC-0470 declined), and everything-in-code (approver changes become Engine releases, retiring governance-as-code).

### T11 (stakeholder)

Accepted the concurrency split (ratify base now, multi-session deferred to SP-0018). On rule hosting, accepted rules-in-code-with-declarative-policy with the note: "With the awareness that some of these rules may be implemented with activegraph after assessing the results of all of the spikes."

### T12 (facilitator)

Grounded the ActiveGraph note against the record — the DEC-0354 five-spike program under EP-0009, SP-0014's compiled-rule precision findings, SP-0016's hook-loop economics and DEC-0387's warm-the-checker finding, and DEC-0370/DEC-0373 sitting proposed pending the ActiveGraph adoption/consolidation session — and read the note as: the hosting contract fixes the authoring model but stays substrate-neutral; whether rule families execute as hand-written checker code or compiled ActiveGraph behaviors is an implementation choice decided after the spike-program consolidation, and the contract must not preclude either. Gave the round-1 read-back, then round 2 — three questions with recommendations: (1) structured diagnostics as a first-class element of every operation contract (typed findings: rule ID, artifact, location, severity, fix hint) — recommended yes; (2) type-roster ownership — recommended EP-0010 owns both the roster and the type machinery, roster changes riding schema-version bumps and migration (DEC-0464, DEC-0470, DEC-0471); (3) commissioning two spikes as EP-0010 derived work — recommended both.

### T13 (stakeholder)

Structured diagnostics: yes, first-class. Type roster: both roster and machinery. Spikes: requested elaboration.

### T14 (facilitator)

Elaborated the spike charters. Spike A, schema-migration mechanism: question — given a corpus-level SemVer marker, what mechanism moves a corpus from version X to Y safely, and what does the Engine owe corpora it cannot migrate automatically; the corpus-level marker choice already eliminates lazy per-artifact migration, leaving in-place rewrite (needs interrupted-migration recovery) versus side-by-side (2x disk, swap protocol); open sub-questions include migration under the transactional write path, frontmatter-shape migration of immutable artifacts, and the compliance story for corpora versions behind; method — prototype both mechanisms against a corpus copy replaying the RSCH type addition (SES-0086/0087) as the test case; timebox one day. Spike B, performance calibration: question — where full-check and incremental graph-sync latency cross interactive tolerance; method — synthesized corpora at roughly 750/2000/5000/10000 artifacts, measuring full check, single-write apply with re-validation, and graph sync, cold and warm, validating DEC-0387's warm-projection speedup at scale; deliverable — measured curves plus the calibrated fitness-function threshold recorded as a decision; timebox one day. Explained draft-ahead mechanics: both spikes drafted this session under EP-0010's Derived Work, ratified by the epic's approval within the same gate bundle, blocking nothing except the specific stories needing their answers.

### T15 (stakeholder)

Commission both spikes.

### T16 (facilitator)

Decision-confirmation checkpoint — played back thirteen decisions in plain language: (1) the write-time/check-time enforcement line at Engine self-trust; (2) EP-0010 port-contract ownership with embedded zero-hosting default adapters and implementation-divergence-under-feature-consensus for consuming surfaces, resolving the DEC-0121 overlap on the BG-0002 side; (3) the pure kernel with all I/O through ports; (4) the kernel operation catalog as normative contract with the gw CLI as reference adapter; (5) structured diagnostics first-class; (6) compatible-extension versioning until the first non-CLI consumer, foreign corpora pinning schema versions; (7) specification-first over the two-descriptions coexistence; (8) EP-0010 owning both type roster and machinery; (9) the corpus-level SemVer schema marker with whole-corpus atomic migrations; (10) substrate-neutral rule hosting (Engine-owned rule code, declarative policy config, ActiveGraph as possible execution substrate pending consolidation); (11) the concurrency split (single-session invariants contracted, multi-session deferred to SP-0018); (12) five contract shapes at this gate with per-type schemas, port details, instrumentation, and the compliance definition deferred downstream; (13) commissioning the two spikes.

### T17 (stakeholder)

Confirmed all thirteen decisions for recording.

### T18 (facilitator)

Gate prep record. Ran the required system-architect reviewer consultation, dual-instance: the record-grounded instance returned READY-WITH-NOTES with seven non-blocking notes; the best-practice-independent instance initially returned three blocking findings, which turned out to be accurate observations of a reverted file (see the incident below) — on rebuttal against the repaired file it revised to READY-WITH-NOTES with four surviving non-blocking notes, converging with its opponent. Incident, recorded faithfully: during gate prep, a librarian task preparing a small EP-0010 edit wrote to the file outside the typed write API, then attempted to undo that with a git checkout — an operation forbidden by DEC-0333 — reverting EP-0010 to its last-committed state and destroying the session's uncommitted rewrite. The blast radius was one file; decisions, spikes, and this session record were untouched. The rewrite was re-applied through the typed write path from the facilitator's retained specification and verified, the unchanged Why-section token confirming byte-fidelity where preservation was required; the reporting task disclosed its own violation honestly. Recall-audit disposition: the judge's single finding — DEC-0135's port-graduation pattern, premised on EP-0004/EP-0007 deriving the ports that DEC-0476 reassigned — was addressed by citing DEC-0135 in EP-0010 with carryover prose in Interfaces item 5 and reciprocal DEC-0476/DEC-0135 relates-to links; the judge's contract-gap note (DEC-0476's citer review naming no owner) is closed by this session's sweep disposition. Consistency-sweep disposition: all 53 hits triaged consistent; the DEC-0121 and DEC-0102 citer sets remain valid as BG-0001 adapter-side work, and the formal DEC-0121 amendment is folded into the deferred BG-0001 reframing per DEC-0441. Overview faithfulness confirmed at gate prep. Presented the gate with three proposed reviewer amendments (a prioritized Quality Goals passage in EP-0010; an SP-0019 Method allowance for the immutability sub-question to conclude as a constraint-finding; an SP-0020 Method sentence fixing the interactive-tolerance definition before measurement), two story-derivation notes for the next stage (capture each consumer's expected operation subset against the kernel operation catalog; give the first-non-CLI-consumer versioning trigger a named watcher), and the DEC-0121 cleanup path options.

### T19 (stakeholder)

Approved all three reviewer amendments. Chose folding the DEC-0121 record cleanup into the deferred BG-0001 reframing rather than an immediate amendment session. Approved EP-0010: the epic moved in-refinement to gated to approved (approved-by awakeinagi@gmail.com, 2026-07-13), and SP-0019 and SP-0020 were ratified in the same gate bundle per DEC-0487 — each walked draft to gated to approved after the write API correctly refused the direct draft-to-approved transition.

## Decisions Produced

DEC-0475 — the write-time/check-time enforcement line: Engine write-time enforcement covers only self-trust invariants, all other rules run as check-time rule families.

DEC-0476 — port-contract ownership: EP-0010 owns the Engine port contracts, ships embedded default adapters, and consuming surfaces may diverge on implementation but never on feature support.

DEC-0477 — the Engine kernel is pure, with all I/O flowing through ports.

DEC-0478 — the kernel operation catalog is the Engine's normative API contract, with the gw CLI as its reference adapter.

DEC-0479 — structured diagnostics are first-class in every Engine operation contract.

DEC-0480 — compatible-extension versioning with tolerant readers until the first non-CLI consumer, with foreign corpora pinning schema versions.

DEC-0481 — specification-first: the Engine contract is normative, and the deployed scripts are its provisional implementation.

DEC-0482 — EP-0010 owns both the artifact-type roster and the type machinery together.

DEC-0483 — the artifact-model schema version is a corpus-level SemVer marker, with migrations moving whole corpora atomically.

DEC-0484 — rule hosting is Engine-owned rule code with declarative policy config, kept substrate-neutral pending the ActiveGraph consolidation.

DEC-0485 — the concurrency contract splits: single-session invariants are ratified now, multi-session semantics defer to SP-0018.

DEC-0486 — five contract shapes settle at this gate; the remaining surfaces defer downstream.

DEC-0487 — two EP-0010 spikes are commissioned: the schema-migration mechanism and performance calibration.

## Conflicts Raised

None yet.
