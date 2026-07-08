---
id: SES-0026
type: session
title: EP-0005 story derivation — release scoping, connector pluggability, attribution, secrets
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0005]
---

# SES-0026: [EP-0005](../epics/EP-0005-connectors-and-identity.md) Story Derivation

## Purpose

Slice the approved [EP-0005](../epics/EP-0005-connectors-and-identity.md)
(Connectors & Identity) into implementable stories, resolving the
epic's four recorded open questions plus the findings of the
pre-drafting decision-recall audit
([DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md)).

## Transcript

**T1 — Sponsor.** Create the stories for [EP-0005](../epics/EP-0005-connectors-and-identity.md).

**T2 — Agent.** Prep: loaded the epic's cited decisions, the boundary
seams ([ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md)
leaves the BBDC implementation to this epic;
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)
consumes team/check administration;
[ST-0012](../stories/ST-0012-governance-config-schemas.md) owns the
`people.yaml`/`repos.yaml` schemas), and ran the decision-recall audit
on the epic (judge fork). Findings: (1) the binding consumption lists —
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
forward-declared operations
([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md))
and the gate engine's registration/administration set
([DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md));
(2) a genuine tension —
[DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)'s
planned `jira-status` frontmatter telemetry versus
[DEC-0095](../decisions/DEC-0095-percent-complete-metrics.md)'s
rejection of volatile state in canon; (3) secrets have no defined home
in the embedded stack
([DEC-0046](../decisions/DEC-0046-person-registry.md),
[DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)); (4) the
[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)
future-work rule to walk per story. Plus a scope gap: the notifier
connector contract assigned to this epic by
[DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)
after its approval, and a release wrinkle:
[BG-0001](../goals/BG-0001-groundwork.md) names connectors as release-2
work while the PR gate needs the code-host connector in v1. Proposed a
slate of ~7 current + 2 deferred stories + 1 spike. Round 1 with
recommendations: (a) Jira sync stories born deferred at release 2
(recommended); (b) notifier story + epic scope amendment (recommended);
(c) timeboxed spike on BBDC's required-check surface (recommended);
(d) Jira backlog read feed deferred with the sync work (recommended)
vs. a thin v1 read story.

**T3 — Sponsor.** All four as recommended.

**T4 — Agent.** Read-back of Round 1. Round 2 with recommendations:
(a) resolve the telemetry tension projection-side — `jira-key` linkage
stays the only canonical write, workflow state joined at query time
(recommended); (b) secrets envelope-encrypted in the app database via
the App Database Port, master key from deployment config (recommended)
vs. a fifth port or OS keyring; (c) program-user attribution as a
service-signed block, asymmetric key, gate-policy verifies signature +
registry resolution (recommended) vs. HMAC or unsigned+log-cross-check;
(d) role→review-path mapping in deployment configuration, taking
[DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)
at its word (recommended) vs. a governance file.

**T5 — Sponsor.** (a), (c), (d) as recommended. (b) as recommended,
**amended**: also create a deferred spike, behind a trigger, for the
enterprise-mandated external vault.

**T6 — Agent.** Round 3: (a) confirm the Jira Data Center assumption as
a decision now (recommended); (b) mint the future-work families as two
deferred backlog stories with demand triggers (recommended) vs. no
triggers or one combined story; (c) new secrets-specific trigger for
the vault spike (recommended) vs. reusing TRG-0004.

**T7 — Sponsor.** (b), (c) as recommended. (a) confirmed Data Center,
**amended**: keep the modularity principle — the agile work-management
system must be pluggable (switch to monday.com, OpenProject, etc. in
the future).

**T8 — Agent.** Read-back of all nine decisions in plain language and
the final slate; noted the work-management generalization extends the
future-work pattern to a third backlog story + trigger
(work-management adapters), and that the epic body needs a
re-affirmable amendment (notifier scope, resolved risks, Derived Work).

**T9 — Sponsor.** Asked: what exactly is `jira-key`, and where is it
written?

**T10 — Agent.** Answered: the work-management issue key (`PROJ-456`
style) of the projection mirroring an artifact — the canon-side half of
the two-way linkage (the issue carries the doc ID + link back per
[DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)). Written
once into the artifact's own frontmatter (the epic/story/spike specs
already declare the field) via the `set-jira-key` typed mechanical
write ([DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md))
when the projection is created on first merge to main
([DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md))
— by the storage service, never the agent or connector directly. A
set-once metadata fact, unlike volatile workflow state, which stays
projection-side.

**T11 — Sponsor.** Confirmed — record.

**T12 — Agent (synthesis).** Recorded
[DEC-0148](../decisions/DEC-0148-work-management-stories-release-2.md)–[DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md);
drafted [ST-0019](../stories/ST-0019-code-host-connector-protocol.md)–[ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md)
(current), [ST-0025](../stories/ST-0025-work-management-projection-lifecycle.md)–[ST-0027](../stories/ST-0027-work-management-backlog-read-feed.md)
(release 2, deferred), [ST-0028](../stories/ST-0028-additional-code-host-connectors.md)–[ST-0030](../stories/ST-0030-additional-work-management-connectors.md)
(backlog, trigger-subscribed), spikes
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) (draft-ahead,
ratified with this bundle) and
[SP-0005](../spikes/SP-0005-external-secret-store-adapter.md) (backlog);
armed TRG-0006–TRG-0009; stubbed
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)–[CMP-0008](../components/CMP-0008-notification-delivery.md);
amended [EP-0005](../epics/EP-0005-connectors-and-identity.md) (scope,
interfaces, risks→resolutions, Derived Work; set `stale` pending
re-affirmation); added glossary entries **Work-Management Connector**
and **Attribution Block**.

**T13 — Agent (decision-recall audits,
[DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md)).**
Ran the audit on all fifteen drafts/amendments; two judge forks.
Findings applied — [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md):
sequencing note added to
[ST-0019](../stories/ST-0019-code-host-connector-protocol.md) (check
administration must not harden before the spike's findings);
[DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md)/[DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md):
[ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md) Out
of Scope now distinguishes human-attributed reviews from
machine-verified auto-PR approvals, which carry no attribution block;
[DEC-0040](../decisions/DEC-0040-role-pool-delegation.md): role claims
in [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
criterion 3 include active time-bounded delegations;
[DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md): hermetic
fake-connector criterion added to
[ST-0023](../stories/ST-0023-read-only-context-access.md);
[DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md):
adapter-credential criterion added to
[ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md);
[DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md):
pass→fail un-passing added to
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)'s
validation matrix. "Nothing to add" verdicts: all six deferred/backlog
stories, [SP-0005](../spikes/SP-0005-external-secret-store-adapter.md),
[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md), and
the amended epic. The judges' flagged contract gaps were repaired by
amending two approved artifacts, now `stale` for re-affirmation in
this gate bundle:
[ST-0006](../stories/ST-0006-typed-mechanical-writes.md) and
[CMP-0001](../components/CMP-0001-artifact-store-service.md) drop the
`set-jira-status` mechanical operation (cancelled by
[DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md))
and gain `migrate-person-ids`, giving
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)'s
bootstrap-identity migration its sanctioned typed operation (per
[DEC-0046](../decisions/DEC-0046-person-registry.md),
[DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

## Decisions Produced

[DEC-0148](../decisions/DEC-0148-work-management-stories-release-2.md),
[DEC-0149](../decisions/DEC-0149-notifier-story-under-ep-0005.md),
[DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md),
[DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md),
[DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
[DEC-0154](../decisions/DEC-0154-review-path-mapping-deployment-config.md),
[DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md),
[DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md)

## Conflicts Raised

None — the [DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)/[DEC-0095](../decisions/DEC-0095-percent-complete-metrics.md)
telemetry tension was resolved in-session by
[DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)
before it hardened into a conflict.
