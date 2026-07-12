---
id: SES-0025
type: session
title: EP-0003 story derivation — bootstrap, recomputation, check ownership, engine state
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Sliced Governance & Gate Engine epic into seven stories covering
  config schemas, policy compilation, gate-policy checks, conflict
  operations, staleness sweeps, re-affirmation, and event logging.
  Resolved open questions on governance bootstrap, mid-flight policy
  changes, required-check registration ownership, and timeout-to-default
  mechanics through grilling and decision-recall audit. Produced
  ST-0012-ST-0018 and DEC-0140-DEC-0147. Amended CMP-0001 per
  DEC-0142.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0003, DEC-0140, DEC-0141, DEC-0142, DEC-0143, DEC-0144, DEC-0145, DEC-0146, DEC-0147]
---

# SES-0025: EP-0003 Story Derivation

## Purpose

Slice the approved EP-0003
(Governance & Gate Engine) into implementable stories, resolving the
epic's recorded open questions (bootstrap, mid-flight policy changes)
plus the design points surfaced by the decision-recall audit
(DEC-0137)
before drafting.

## Transcript

**T1 — Sponsor.** Refine EP-0003.

**T2 — Agent.** Prep: loaded the epic's seven governance decisions
(DEC-0036–DEC-0042),
verified boundary seams (ST-0006
leaves mark-stale invocation to this epic;
ST-0007 leaves the
`gate-policy`/`conflicts-open` checks to it), and ran the
decision-recall audit on the epic. Judge findings: the mechanical-diff
validator provisioning duty
(DEC-0033),
decision-rights config
(DEC-0054),
the v1 embedded stack and App Database Port constraints
(DEC-0102,
DEC-0121), and
`governance/repos.yaml`
(DEC-0049) — all
absorbed at story level — plus a genuine contract gap: required-check
registration is forward-declared on
CMP-0001
(DEC-0132)
while DEC-0036
assigns check administration to the gate engine. Proposed a seven-story
slate (config schemas; compilation & host provisioning; `gate-policy`
check; `conflicts-open` & conflict ops; staleness sweep; re-affirmation
& queues; event log & metrics) with no new spikes. Round 1 questions
with recommendations: (a) governance bootstrap (recommended seeded init
commit before protection compiles); (b) mid-flight policy changes
(recommended recompute all open PRs, keep host reviews as facts);
(c) required-check registration owner (recommended gate engine, with
CMP-0001's
operation narrowed to result posting); (d) how timeout-to-default
System Decisions get written given the mechanical allowlist cannot
create Decisions (recommended templated auto-PR via the
DEC-0033 machinery
with a template-conformance check).

**T3 — Sponsor.** All four as recommended.

**T4 — Agent.** Read-back of Round 1. Noted
DEC-0075
already settles the notification boundary (engine emits, notification
center + notifier connectors deliver — no question needed). Round 2:
(a) truth grade of the governance event log given the
rebuild-sufficiency invariant
(DEC-0131)
(recommended two-grade log — mirrored provenance facts, lossy
telemetry); (b) check recomputation triggers (recommended ChangeEvents
+ host webhooks with a periodic reconciliation sweep); (c) where impact
reports live (recommended re-affirmation PR descriptions + event log,
never committed); (d) queue state model (recommended derived views, no
persisted queue truth).

**T5 — Sponsor.** All four as recommended.

**T6 — Agent.** Played back the eight decisions in plain language and
the final slate: seven stories, no new spikes (SP-0001
already covers the ranking question; queues proceed on human judgment
until it lands, per
DEC-0041).
Flagged two glossary terms (System Decision, Governance Event Log) and
the CMP-0001
Dependencies amendment for re-affirmation.

**T7 — Sponsor.** Confirmed — record and draft.

**T8 — Agent (synthesis).** Recorded
DEC-0140–DEC-0147;
drafted ST-0012–ST-0018
with dependency and impact edges; added the glossary entries; updated
EP-0003's Derived
Work; amended
CMP-0001's
Dependencies per
DEC-0142.

**T9 — Agent (decision-recall audits,
DEC-0137).**
Ran the audit on all seven drafts; two judge forks. Findings applied:
DEC-0046 —
`governance/people.yaml` added to
ST-0012's schema
suite and person-id references to
ST-0013's
team projection; DEC-0096 —
Implements-edge propagation and element-scoped reporting added to
ST-0016;
DEC-0028 — the
re-affirmation PR named as gate-PR-machinery reuse in
ST-0017 with a
build dependency on
ST-0003 (also
added to ST-0015
for its auto-PR path);
DEC-0146 —
impact-report storage named in
ST-0018's event
coverage. The judges' flagged contract gap — how the checks treat
machine-verified auto-PRs — became explicit criteria: `gate-policy`
passes them on validator + program-user approval
(ST-0014 criterion 8, per
DEC-0033/DEC-0143);
`conflicts-open` governs gate PRs only, never wedging mechanical
writes on contested artifacts
(ST-0015
criterion 1). "Nothing to add" verdicts:
ST-0013
(beyond the person-id consistency note),
ST-0014,
ST-0015
candidate lists.

## Decisions Produced

DEC-0140,
DEC-0141,
DEC-0142,
DEC-0143,
DEC-0144,
DEC-0145,
DEC-0146,
DEC-0147

## Conflicts Raised

None — the DEC-0132/DEC-0036
registration ambiguity was resolved in-session by
DEC-0142
before it hardened into a conflict.
