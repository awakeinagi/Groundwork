---
id: IDEA-0024
type: idea
title: "Take up the Artifact Interaction Surface backfill"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Folds the already-built artifact-librarian and artifact-interact
  skill formally under EP-0009 -- drafting the two Component Docs
  intent-first (per DEC-0342's protocol: never transcribe from the
  as-built, diff after, dispose every divergence as keep-via-
  decision or fix-via-defect, strangler-shaped starting with the
  librarian's tool surface and its conformance check) and running
  the backfill. Also carries DEC-0340's SPEC agent-profile
  amendment, DEC-0341's checker addition, and arming TRIGGERS.md's
  unmet absorption triggers for this surface. Two open questions
  travel with it: the defect-tracking artifact shape (stakeholder
  sketch: severity plus a multi-state status workflow, per DEC-0353)
  and the install-script contract scope call (deferred a third time,
  per DEC-0352). Corrects IDEA-0015's Spark Context, which mis-
  summarized the record as a four-story-sequence verdict with six
  resolved questions; the accurate basis, verified at SES-0065, is
  SES-0059 T10's structural verdict plus SES-0060's four items (two
  resolved there, two deferred here).
links:
  derives-from: [SES-0065]
  relates-to: [EP-0009, DEC-0342, DEC-0340, DEC-0341, DEC-0350, DEC-0352, DEC-0353]
---

## The Idea

Fold the already-built artifact-librarian and artifact-interact
formally under EP-0009: draft the two Component Docs intent-first and
run the DEC-0342 backfill against the as-built surface.

## Spark Context

Captured at SES-0065's close, immediately after EP-0009 (Artifact
Interaction Surface) was drafted and confirmed with the backfill in
scope but its execution deferred by sequencing (DEC-0350). The
accurate grounding this Idea must carry forward:

- **DEC-0342's backfill protocol**: Stories and both CMPs are written
  intent-first from the decision record and caller expectations —
  never transcribed from the as-built implementation — then the
  as-built is diffed against them; every divergence found is
  explicitly dispositioned by the stakeholder as either keep (via a
  recording decision) or fix (via a defect item). The work is
  strangler-shaped: the first slice is the librarian's tool surface
  together with its conformance check, then the slice widens.
  Adversarial scenarios run at gate; independent review runs via the
  system-architect reviewer moment; provenance is honestly
  retro-documented, deriving from SES-0057/SES-0058/SES-0059; contract
  altitude is preserved (DEC-0322's eval-loop territory stays out).
- **DEC-0340's SPEC-component agent-profile amendment**: the
  runtime-policy contract section the librarian's CMP must carry
  (every config field and value, deny-by-default tool grants with
  rationale, double-pinned model, memory policy, refusal semantics,
  spawn contract, concurrency obligations, breaking-change list).
- **DEC-0341's checker addition**: the deployed-vs-contracted agent
  conformance check this backfill's CMP becomes the first real target
  of.
- **Arming docs/TRIGGERS.md's absorption triggers** for this surface
  (per DEC-0338/DEC-0346) — currently unmet; no armed trigger exists
  yet.

Two open questions travel with this Idea, both deliberately deferred
rather than resolved at EP-0009's derivation:

- The **defect-tracking artifact shape** (stakeholder sketch: a
  severity field plus a multi-state status workflow) — its sole named
  consumer is DEC-0342's fix-via-defect disposition path, so it is
  designed here, grounded in the backfill's actual divergence list
  (DEC-0353).
- The **install-script contract scope call** — whether install.sh is
  contracted within this epic or reserved for the future distribution
  epic (DEC-0339/IDEA-0010) — deferred a third time, to be settled
  here (DEC-0352).

**Correction note**: IDEA-0015's own Spark Context mis-summarized the
record — it claimed a "four-story sequence" verdict and "six
stakeholder-resolved open questions" from a prior architect
consultation. No such four-story-sequence verdict exists in the
record. The accurate basis, verified at SES-0065: SES-0059 T10's
structural verdict (the resume-from direction IDEA-0015 should have
cited) and SES-0060's four items — of which two were resolved there
(the sacrificial-framing narrowing that became DEC-0346, and
two-session structuring) and two were explicitly deferred to this
session (the install-script scope call and the defect-artifact
shape), both of which this Idea now carries forward per DEC-0352 and
DEC-0353 above.

## Disposition

Pending — awaiting take-up via the change-intake protocol as its own
session.
