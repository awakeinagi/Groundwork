---
id: SES-0025
type: session
title: EP-0003 story derivation — bootstrap, recomputation, check ownership, engine state
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0003]
---

# SES-0025: [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) Story Derivation

## Purpose

Slice the approved [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)
(Governance & Gate Engine) into implementable stories, resolving the
epic's recorded open questions (bootstrap, mid-flight policy changes)
plus the design points surfaced by the decision-recall audit
([DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md))
before drafting.

## Transcript

**T1 — Sponsor.** Refine [EP-0003](../epics/EP-0003-governance-and-gate-engine.md).

**T2 — Agent.** Prep: loaded the epic's seven governance decisions
([DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)–[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)),
verified boundary seams ([ST-0006](../stories/ST-0006-typed-mechanical-writes.md)
leaves mark-stale invocation to this epic;
[ST-0007](../stories/ST-0007-tier2-check-suite.md) leaves the
`gate-policy`/`conflicts-open` checks to it), and ran the
decision-recall audit on the epic. Judge findings: the mechanical-diff
validator provisioning duty
([DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)),
decision-rights config
([DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md)),
the v1 embedded stack and App Database Port constraints
([DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)), and
`governance/repos.yaml`
([DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)) — all
absorbed at story level — plus a genuine contract gap: required-check
registration is forward-declared on
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md))
while [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)
assigns check administration to the gate engine. Proposed a seven-story
slate (config schemas; compilation & host provisioning; `gate-policy`
check; `conflicts-open` & conflict ops; staleness sweep; re-affirmation
& queues; event log & metrics) with no new spikes. Round 1 questions
with recommendations: (a) governance bootstrap (recommended seeded init
commit before protection compiles); (b) mid-flight policy changes
(recommended recompute all open PRs, keep host reviews as facts);
(c) required-check registration owner (recommended gate engine, with
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
operation narrowed to result posting); (d) how timeout-to-default
System Decisions get written given the mechanical allowlist cannot
create Decisions (recommended templated auto-PR via the
[DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md) machinery
with a template-conformance check).

**T3 — Sponsor.** All four as recommended.

**T4 — Agent.** Read-back of Round 1. Noted
[DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)
already settles the notification boundary (engine emits, notification
center + notifier connectors deliver — no question needed). Round 2:
(a) truth grade of the governance event log given the
rebuild-sufficiency invariant
([DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md))
(recommended two-grade log — mirrored provenance facts, lossy
telemetry); (b) check recomputation triggers (recommended ChangeEvents
+ host webhooks with a periodic reconciliation sweep); (c) where impact
reports live (recommended re-affirmation PR descriptions + event log,
never committed); (d) queue state model (recommended derived views, no
persisted queue truth).

**T5 — Sponsor.** All four as recommended.

**T6 — Agent.** Played back the eight decisions in plain language and
the final slate: seven stories, no new spikes ([SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md)
already covers the ranking question; queues proceed on human judgment
until it lands, per
[DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md)).
Flagged two glossary terms (System Decision, Governance Event Log) and
the [CMP-0001](../components/CMP-0001-artifact-store-service.md)
Dependencies amendment for re-affirmation.

**T7 — Sponsor.** Confirmed — record and draft.

**T8 — Agent (synthesis).** Recorded
[DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)–[DEC-0147](../decisions/DEC-0147-derived-queue-views.md);
drafted [ST-0012](../stories/ST-0012-governance-config-schemas.md)–[ST-0018](../stories/ST-0018-governance-event-log-metrics.md)
with dependency and impact edges; added the glossary entries; updated
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s Derived
Work; amended
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
Dependencies per
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md).

**T9 — Agent (decision-recall audits,
[DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md)).**
Ran the audit on all seven drafts; two judge forks. Findings applied:
[DEC-0046](../decisions/DEC-0046-person-registry.md) —
`governance/people.yaml` added to
[ST-0012](../stories/ST-0012-governance-config-schemas.md)'s schema
suite and person-id references to
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)'s
team projection; [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md) —
Implements-edge propagation and element-scoped reporting added to
[ST-0016](../stories/ST-0016-staleness-sweep-impact-analysis.md);
[DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md) — the
re-affirmation PR named as gate-PR-machinery reuse in
[ST-0017](../stories/ST-0017-reaffirmation-flow-queues.md) with a
build dependency on
[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md) (also
added to [ST-0015](../stories/ST-0015-conflicts-open-check-and-operations.md)
for its auto-PR path);
[DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md) —
impact-report storage named in
[ST-0018](../stories/ST-0018-governance-event-log-metrics.md)'s event
coverage. The judges' flagged contract gap — how the checks treat
machine-verified auto-PRs — became explicit criteria: `gate-policy`
passes them on validator + program-user approval
([ST-0014](../stories/ST-0014-gate-policy-check.md) criterion 8, per
[DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)/[DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md));
`conflicts-open` governs gate PRs only, never wedging mechanical
writes on contested artifacts
([ST-0015](../stories/ST-0015-conflicts-open-check-and-operations.md)
criterion 1). "Nothing to add" verdicts:
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)
(beyond the person-id consistency note),
[ST-0014](../stories/ST-0014-gate-policy-check.md),
[ST-0015](../stories/ST-0015-conflicts-open-check-and-operations.md)
candidate lists.

## Decisions Produced

[DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md),
[DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md),
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md),
[DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md),
[DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md),
[DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
[DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md),
[DEC-0147](../decisions/DEC-0147-derived-queue-views.md)

## Conflicts Raised

None — the [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)/[DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)
registration ambiguity was resolved in-session by
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)
before it hardened into a conflict.
