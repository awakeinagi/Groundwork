---
id: SES-0081
type: session
title: "Session creates require close-required frontmatter at creation"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
kind: expedited
intake: {origin: user, proposed-by: awakeinagi}
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Expedited session (DEC-0254) that generalized the SES-0079 close-
  refusal trap into a durable guard. Root cause: session close
  validates participant/participant-role/facilitator/transcript-
  fidelity frontmatter, but create --field is the only operation
  that can write those fields, and create did not require them — a
  create-time-optional, close-time-required, no-post-creation-path
  trap (IDEA-0042 class). Stakeholder awakeinagi asked whether the
  fix could generalize beyond sessions; the facilitator audited
  every lifecycle gate in the write path and designed a declarative
  REQUIRED_AT_CREATE table read by op_create (currently one row:
  session, the four SESSION_CLOSE_FIELDS), with set-status close's
  own check kept as backstop. Stakeholder approved the design
  verbatim. Built: the guard, a table-driven test (auto-covers
  future rows), and an operations.md create-section update. Suites:
  guards 49/49, lock 18/18, audit-packet 8/8. Produced DEC-0417
  (accepted). A Sonnet 5 recall audit over a 15-candidate packet
  found nothing to add; the closest near-miss, DEC-0407, was judged
  non-duplicative (body-completeness gate vs. frontmatter-presence
  gate). One immutable-decision wording note on DEC-0417 was
  dispositioned in the closing turn rather than by supersession.
  Session closed.
links:
  relates-to: [SES-0079, DEC-0313, IDEA-0042, DEC-0417, IDEA-0055]
---

# SES-0081: Session creates require close-required frontmatter at creation

## Purpose

DEC-0254 authorizes expedited method-level take-up sessions for process gaps discovered mid-work. This session takes up a gap surfaced immediately after SES-0079's close was refused for missing frontmatter and repaired only by an operator direct edit: session close requires participant/participant-role/facilitator/transcript-fidelity frontmatter, but nothing in the create-time path or the intake protocol enforces supplying them, so the gap surfaces hours later as an API-unreachable repair (IDEA-0042). The write API's fixed operation set (DEC-0313) makes create --field the only path that can ever write these fields, which is why the fix under discussion targets create itself rather than a new operation.

## Transcript

### T1 (stakeholder awakeinagi, verbatim; context — this arose immediately after SES-0079's close was refused for missing frontmatter and repaired by operator direct edit)

"Why wasn't that frontmatter added to begin with?" followed by, after the facilitator's root-cause analysis and offer of paths (expedited session / idea capture / leave), "Run it as a quick session"

### T2 (facilitator restatement and root cause)

Three stacked misses caused the SES-0079 close refusal. First, the facilitator's own session-open prompt omitted the identity fields. Second, librarian diligence on setting them at create time varies by spawn — SES-0080's librarian set them unprompted, SES-0079's did not. Third, and structurally, the toolchain validates participant/participant-role/facilitator/transcript-fidelity only at set-status closed while create --field is the only operation that can write them at all — create-time optional plus close-time required plus no post-creation path is a trap that surfaces hours later as an API-unreachable repair (IDEA-0042 class). Proposed fix, design pending stakeholder gate per DEC-0335/DEC-0345: op_create refuses --type session unless all four SESSION_CLOSE_FIELDS arrive via --field, with the refusal naming the missing fields and the flag syntax; placed after per-field value validation so existing value-errors keep precedence; one new guard test plus full-suite regression; one create-section line in operations.md. Alignment on intent confirmed at T1; design approval remains pending.

### T3 (stakeholder awakeinagi, verbatim, responding to the facilitator's session-scoped guard design)

"Can we handle this more generally for all artifact types? Required fields must be created when the artifact is created?"

### T4 (facilitator)

Generalization audit of every lifecycle gate in the write path: a field is a creation trap only when a later gate requires it AND only create can write it. Session close's four fields (participant, participant-role, facilitator, transcript-fidelity) are the sole current trap — accepted-in, approved-by/approved-on, superseded-by, and release are all stamped or settable by set-status itself, and decided-by/source-span/timebox/sponsor are demanded by no gate. Revised design: a declarative REQUIRED_AT_CREATE table (currently one row: session -> the four close fields) with one guard in op_create iterating it, placed after per-field value validation so value errors keep precedence; refusal names the type, missing fields, and --field syntax; set-status close's check stays as backstop, both reading SESSION_CLOSE_FIELDS. Test plan: table-driven guard test (auto-covers future rows), existing bad-value tests as precedence checks, full three-suite regression.

### T5 (stakeholder awakeinagi, verbatim)

"Approved."

### T6 (facilitator, build record)

Guard and REQUIRED_AT_CREATE table landed in gw_write.py; table-driven test added to test_gw_guards.py; operations.md create section documents the rule. Suites: guards 49/49, lock 18/18, audit-packet 8/8. Librarian surfaces updated per stakeholder instruction: operations.md in-build, librarian memory entry recorded alongside this turn.

### T7 (facilitator, close-out)

Recall audit on DEC-0417: a Sonnet 5 judge over the 15-candidate packet returned nothing-to-add. The closest near-miss was DEC-0407 (the create-time section-skeleton gate), which fails as a parallel because it governs body completeness rather than frontmatter presence — a non-interacting guard, not a duplicate.

One wording observation is dispositioned here rather than by supersession, since accepted decisions are immutable: DEC-0417's Implications phrase "there is no retroactive path if they are omitted" describes the pre-guard condition that motivated the decision (the SES-0079 close refusal), and remains true only for writes that bypass the guarded API — under the guard itself, omission is impossible at creation. No edit to DEC-0417 is warranted; this turn is the durable record of the observation.

Session complete: the generalized REQUIRED_AT_CREATE guard was designed, approved, built, and tested (guards 49/49, lock 18/18, audit-packet 8/8); DEC-0417 is accepted; the recall audit came back clean.

### Post-Close Enrichment (2026-07-12)

2026-07-12: IDEA-0055 (guard transcript turn-heading style at write time) was captured from this session's close-out turn-numbering defect and joins the work queue.

## Decisions Produced

SES-0081 produced DEC-0417, "Gate-required create-only fields are demanded at artifact creation" — the generalized REQUIRED_AT_CREATE guard, accepted after stakeholder approval at T5.

## Conflicts Raised

None.
