---
id: SP-0017
type: spike
title: "Fork-and-diff as design-debate evidence"
status: approved
approved-on: 2026-07-12
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Spike SP-0017 asked whether fork-and-diff over SP-0014's
  structural rulebase produces decision-grade design evidence
  against a recorded dual-instance architect debate, then was
  extended (SES-0070 T11) into a broader ActiveGraph capability
  assessment. Four rounds: (1-2) fork-and-diff on two decided
  questions (DEC-0307 grouping; DEC-0134/0135 graduation) —
  directionally reliable, rationale-partial, correspondence tracking
  whether a rule models the decision's driver; (3) provenance +
  deterministic replay — strongest fit, event log as a unified
  audit-trail/impact substrate; (4) packs/schema/gates — typed
  validation strong, gate behavior-mediated/bypassable. Method
  validated by six tests on both benchmarks. Five proposed decisions
  (DEC-0369..0373); full adoption deferred to a post-SP-0016
  DEC-0337 cross-spike survey. All build code throwaway (DEC-0351).
  Re-affirmed approved under DEC-0441 (approved-by awakeinagi,
  approved-on 2026-07-12) after the SES-0085 staleness walk found it
  clean of the old charter.
links:
  impacted-by: [SP-0014]
  derives-from: [EP-0009]
  relates-to: [SP-0014]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336, DEC-0293, DEC-0134, DEC-0152, DEC-0307, DEC-0369, DEC-0370, DEC-0371, DEC-0372, DEC-0373, DEC-0374]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Does forking a design run and diffing rule findings across two alternative designs produce decision-grade evidence? Concretely: for a question the corpus has already decided through a recorded dual-instance architect debate, does an ActiveGraph fork-and-diff of the two alternatives' structural findings surface anything the debate missed, or miss anything the debate surfaced?

## Why It Blocks

Blocks nothing today; explicitly queued last since it depends on SP-0014's rulebase. It is the test of the T4 fork-and-diff idea as empirical evidence in design debates within the DEC-0354 executable-design-knowledge program -- if the diff mostly reproduces or misses what human/agent debate already surfaces, the case for fork-and-diff as a distinct value-add weakens.

## Method

Encode two alternative designs for a question the corpus has already decided (a question with a recorded dual-instance architect debate). Run both alternatives through SP-0014's rulebase via ActiveGraph's fork-and-diff mechanism. Compare the resulting structural findings-diff against what the recorded debate actually surfaced.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

The dual-instance architect debate this spike benchmarks against is the mechanism DEC-0293 established; the comparison is meaningful only because that mechanism already produces a recorded, citable debate record to diff against.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): the findings-diff compared against the historical-debate record -- what the diff surfaced that the debate missed, and what the debate surfaced that the diff missed.

## Data-Source Assumptions
At least one decided design question with a recorded dual-instance debate exists in the corpus (several do). SP-0014's rulebase exists and is reusable for this spike's two alternative-design encodings.

## Findings

SP-0017 ran as four rounds; rounds 3-4 are the stakeholder-directed ActiveGraph capability-assessment extension (SES-0070 T11).

Round 1 — fork-and-diff vs the DEC-0307 grouping debate. Two rival groupings (bounded-context vs a single 'gate an artifact' vertical slice) of one shared element-grain substrate were run through SP-0014's rulebase via ActiveGraph Runtime.fork and their rule-findings diffed. The diff (R1 cycles, R10 traceability, R16 graduation, R21 mutual coupling) surfaced three of the five recorded human rejection grounds plus an unnamed one (introduced dependency cycles); it was blind to the two semantic grounds (common-closure, ubiquitous-language cohesion). Directionally reliable, rationale-partial (DEC-0369, DEC-0371).

Round 2 — fork-and-diff on the DEC-0134/0135 seam-graduation question (graduated standalone vs kept inline). The diff was a single rule, R16, firing precisely on the un-graduated multi-consumer port AppDatabasePort (4 external consumers) and clearing when graduated — a near-direct hit — but it missed ChangeEvent's graduation, driven by event-contract decoupling (1 consumer), a driver no rule models. This sharpened the finding: correspondence tracks whether a rule models the decision's actual driver, not merely 'structural vs semantic.' All six method-tests passed on both benchmarks, with a global anchor reproducing SP-0014's recorded boundary findings exactly (DEC-0369, DEC-0370, DEC-0371).

Round 3 — provenance and deterministic replay. On the corpus projection (835 objects / 980 relations / 1815 events): save_state + Runtime.load rebuilt a byte-identical run (twice); the item-to-decision citation graph reconstructed from the reloaded event log alone and matched the live graph exactly; and patching one cited decision (DEC-0152, cited by 20 items) to superseded localized the finding-diff to exactly the 20 affected R8 findings. The event log is the append-only source-of-truth record Groundwork already keeps and could back both the audit trail and impact/staleness analysis. Nuance: post-fork patches to shared objects surface in fork_only_events (patch.applied), not diff.divergent_objects. Strongest single-capability fit (DEC-0372).

Round 4 — packs, typed schema, and policy gates. A minimal Groundwork pack enforced typed object and relation schemas (malformed writes and wrong-direction relations raise PackSchemaViolation) like the write API; the policy gate withheld a proposed artifact until approve(approved_by=...), materializing it with approval.proposed/approval.granted provenance. But gating is behavior-mediated — a direct add_object of a gated type bypasses it — unlike Groundwork's every-mutation write-API gate. Strong on validation, partial on gate enforcement (DEC-0373).

Cross-round: ActiveGraph is a strong fit as an analysis/provenance substrate (rounds 1-3) and a partial fit as the enforcing write layer (round 4). All build code was throwaway (DEC-0351), preserved off-corpus.

## Resulting Decisions

Five preliminary decisions, all proposed (adoption deferred — see below):
- DEC-0369 — fork-and-diff yields directionally-reliable but rationale-partial structural evidence for grouping decisions.
- DEC-0370 — the ActiveGraph fork-and-diff mechanism is viable for design-alternative evaluation (method-tested, generalized across two benchmarks).
- DEC-0371 — structural rulebases have a semantic/driver blind spot bounding automated design evidence.
- DEC-0372 — ActiveGraph event-log provenance and deterministic replay are a strong fit for Groundwork's audit trail and impact analysis.
- DEC-0373 — ActiveGraph enforces typed artifact/relation schemas like a write API, but its gate is behavior-mediated and not a drop-in for Groundwork's write-API gates.

The full-adoption decision is deferred to a post-SP-0016 cross-spike ActiveGraph adoption survey (the DEC-0337 step), which will synthesize SP-0014/0015/0016/0017, run the system-architect consultation, and ratify these five to accepted under a parent adoption decision — following SP-0015's precedent of ratifying findings while deferring adoption, and reinforced by SP-0016's convergent conclusion (DEC-0374/0375) that ActiveGraph earns its place as an event-sourced substrate, not as a faster checker.

