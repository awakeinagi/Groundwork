---
id: SES-0051
type: session
title: IDEA-0002 take-up — the Idea artifact type in the application
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  derives-from: [IDEA-0002]
  relates-to: [IDEA-0001, EP-0001, EP-0006, ST-0001, CMP-0001, ST-0055, ST-0056, ST-0065]
---

# SES-0051: The Idea Type in the Application

First take-up of an Idea artifact under the change-intake protocol
(DEC-0255, DEC-0261): IDEA-0002 — reflecting the paradigm's Idea type
(DEC-0258) in the application's specs, schema suite, store, and UI.
Touches EP-0001 (schema-suite amendments: ST-0001 and CMP-0001) and
EP-0006 (a new release-1 story, ST-0065). ST-0055 and ST-0056 receive
impact edges as the release-2 surfacing homes. IDEA-0001 was briefly
opened for take-up and redirected — it remains captured.

## Transcript

### T1 — Stakeholder

"Let's take IDEA-0001."

### T2 — Facilitator

Ran the intake steps for IDEA-0001: todo list created, authority check
passed (solo governance), locate pass over the session engine and UI
(EP-0002 stories ST-0032/ST-0034/ST-0035/ST-0039; EP-0006 stories
ST-0043/ST-0044; ST-0055 deferred), and restated the intent with a
working classification hypothesis.

### T3 — Stakeholder

"Actually let's handle IDEA-0002 first."

### T4 — Facilitator

IDEA-0001 left `captured` — the exchange changed nothing, so it stays
off the record per DEC-0255. Locate pass for IDEA-0002:
SPEC-artifact-common enumerates ten prefixes (no IDEA); ST-0001 AC1
and CMP-0001 `SchemaValidator.D-1` hard-enumerate the type set —
approved-contract amendments unavoidable, so the DEC-0267 cascade
applies; UI/work-queue surfaces sit in EP-0006, whose ST-0055 is
deferred to release 2. Restated the intent, declaring the boundary:
this session covers the type's existence, validation, capture, and
queue visibility; the take-up flow (Idea → intake session) belongs to
IDEA-0001's future session.

### T5 — Stakeholder

Confirmed alignment.

### T6 — Facilitator

Round 1 (recommendations first): (1) change shape — amendments only to
ST-0001/CMP-0001 (recommended: ST-0001's charter is "a schema for
every artifact type") / a new story under EP-0001; (2) SPEC-idea
contract — mirror SES-0050 semantics with tier-1 shape and tier-2
cross-artifact rules (recommended) / tier-1 only / everything tier-1;
(3) UI/work-queue release scope — new deferred release-2 story beside
ST-0055 (recommended) / release-1 UI story now / fold into ST-0055 at
revival.

### T7 — Stakeholder

(1) Amendments only. (2) Mirror SES-0050, tier-1 shape / tier-2 rules.
(3) Overrode the recommendation: a release-1 UI story now.

### T8 — Facilitator

Explored EP-0006's derived set and surfaced the tension honestly:
release 1's UI is deliberately session-centric — dashboards, queues,
triage, and full browsing (ST-0050, ST-0051, ST-0055, ST-0056) are all
deferred to release 2, so a full capture+browse+queue story in release
1 would re-open that settled seam. Round 2: (1) release-1 scope —
capture + minimal list, queue surfacing joins release 2 via impact
edges (recommended) / full scope in release 1 / capture only, no list;
(2) capture entry — in-session "park as Idea" plus a global
quick-capture in the shell (recommended) / in-session only / global
only; (3) decline in release 1 — yes, minimal, rationale required,
gate-policy-checked (recommended) / defer to release 2; (4) the
take-up seam — named out-of-scope with a reserved hand-off point for
IDEA-0001's session (recommended) / include take-up now.

### T9 — Stakeholder

All four recommendations accepted.

### T10 — Facilitator

Detailed summary: SPEC-idea.md + SPEC-artifact-common amendment;
ST-0001 AC1 extension plus a new Idea-validation AC; CMP-0001 D-1
extension with the staleness cascade and re-affirmation completing
in-session; new release-1 story ST-0065 (in-session park + global
quick-capture, minimal captured-Ideas list, decline with required
rationale; take-up out of scope naming IDEA-0001; impact edges to
ST-0055/ST-0056 as the release-2 surfacing homes). Asked the
inspired-ideas question.

### T11 — Stakeholder

"Approved" — no new ideas.

### T12 — Facilitator (distillation checks & recall audit)

**Cross-story coupling check (per DEC-0196, DEC-0199)** over the
touched sibling set (ST-0065, ST-0055, ST-0056): no mutual coupling;
ST-0065's fan-out is one-directional as designed — clear.

**Consistency checks (per DEC-0157, DEC-0158)** over
DEC-0268..DEC-0271. `sweep`: four review hits, all ST-0065 against
DEC-0258/DEC-0261 — the story was drafted this session to implement
those decisions; consistent by construction. `terms`: shared
identifiers (`proposed-by`, `docs/ideas/`) between this session's own
artifacts and the SES-0050 decision set — intentional shared
vocabulary; reviewed, clear.

**Decision-recall audit** on this session (15 candidates, one Sonnet 5
judge): "Nothing to add" — nearest near-miss DEC-0007 (staleness
ancestor), correctly carried by SPEC-artifact-common's citation and
the more specific DEC-0267 already in the considered set. The judge
separately flagged a **contract gap**: CMP-0001's only documented
creation operation (`BranchOrchestrator.A-1`) mandates gate-PR-and-
merge, while Ideas are gateless — no durable-write path existed for
capture. Facilitator proposed mirroring the Change Proposal precedent
(`create-change-proposal`/`set-cp-triage` in
`MechanicalWriteService`): add `create-idea` and
`set-idea-disposition` to the closed operation set.

### T13 — Stakeholder

"I agree with your fix. Approved."

### T14 — Facilitator (execution record)

Implemented in-session:

- **Specs**: SPEC-idea.md created (mirroring DEC-0258/DEC-0259/
  DEC-0261 semantics, tiering per DEC-0269); SPEC-artifact-common
  gained the IDEA prefix, the type-enum entry, and the reduced-
  lifecycle note.
- **Store amendments (DEC-0268)**: ST-0001 AC1 extended + new AC8
  (Idea tier-1 validation); CMP-0001 `SchemaValidator.D-1` extended +
  new `D-5`; per the T12 gap resolution (DEC-0272), CMP-0001
  `MechanicalWriteService` extended to `A-1..A-10` with `create-idea`
  and `set-idea-disposition`. DEC-0272's own consistency sweep then
  surfaced ST-0006 (its AC1 enumerates the closed operation set) —
  amended in the same change. Cascade per DEC-0267: the story
  amendments staled CMP-0001; all amended artifacts re-affirmed
  in-session by the sole approver (approved-on 2026-07-09).
- **UI (DEC-0270, DEC-0271)**: ST-0065 derived, refined, and approved
  (release 1; capture affordances, minimal list, decline with
  rationale; take-up reserved for IDEA-0001); EP-0006 Derived Work
  updated in the same edit; impact edges ST-0065 → ST-0055/ST-0056
  with impactor-side prose.
- **Take-up bookkeeping**: IDEA-0002 → `taken-up`, Disposition naming
  this session.
- **Verification**: coupling check clear; `check_links.py` → OK, 426
  artifacts, 0 violations (ST-0065 joins the known element-coverage
  warnings pending its epic's CMP); graph rebuilt; consistency checks
  for DEC-0272 run post-amendment and dispositioned clear.

## Decisions Produced

DEC-0268, DEC-0269, DEC-0270, DEC-0271, DEC-0272

## Conflicts Raised

None.
