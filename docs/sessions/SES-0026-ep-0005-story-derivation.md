---
id: SES-0026
type: session
title: EP-0005 story derivation — release scoping, connector pluggability, attribution, secrets
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Sliced Connectors & Identity epic into stories resolving Jira sync
  deferral, notifier connector scope, secrets storage architecture, and
  attribution-block cryptography. Deferred Jira sync, backlog adapters,
  and external vault spike behind triggers preserving pluggability.
  Resolved telemetry tension via DEC-0151 (jira-key canonical, workflow
  joined at query time). Adopted envelope encryption in app database for
  secrets. Produced ST-0019-ST-0030, SP-0004-SP-0005, and
  DEC-0148-DEC-0156.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0005, DEC-0148, DEC-0149, DEC-0150, DEC-0151, DEC-0152, DEC-0153, DEC-0154, DEC-0155, DEC-0156]
---

# SES-0026: EP-0005 Story Derivation

## Purpose

Slice the approved EP-0005
(Connectors & Identity) into implementable stories, resolving the
epic's four recorded open questions plus the findings of the
pre-drafting decision-recall audit
(DEC-0137).

## Transcript

**T1 — Sponsor.** Create the stories for EP-0005.

**T2 — Agent.** Prep: loaded the epic's cited decisions, the boundary
seams (ST-0003
leaves the BBDC implementation to this epic;
ST-0013
consumes team/check administration;
ST-0012 owns the
`people.yaml`/`repos.yaml` schemas), and ran the decision-recall audit
on the epic (judge fork). Findings: (1) the binding consumption lists —
CMP-0001's
forward-declared operations
(DEC-0132)
and the gate engine's registration/administration set
(DEC-0142);
(2) a genuine tension —
DEC-0048's
planned `jira-status` frontmatter telemetry versus
DEC-0095's
rejection of volatile state in canon; (3) secrets have no defined home
in the embedded stack
(DEC-0046,
DEC-0102,
DEC-0121); (4) the
DEC-0133
future-work rule to walk per story. Plus a scope gap: the notifier
connector contract assigned to this epic by
DEC-0075
after its approval, and a release wrinkle:
BG-0001 names connectors as release-2
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
DEC-0043
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
DEC-0013). Written
once into the artifact's own frontmatter (the epic/story/spike specs
already declare the field) via the `set-jira-key` typed mechanical
write (DEC-0033)
when the projection is created on first merge to main
(DEC-0048)
— by the storage service, never the agent or connector directly. A
set-once metadata fact, unlike volatile workflow state, which stays
projection-side.

**T11 — Sponsor.** Confirmed — record.

**T12 — Agent (synthesis).** Recorded
DEC-0148–DEC-0156;
drafted ST-0019–ST-0024
(current), ST-0025–ST-0027
(release 2, deferred), ST-0028–ST-0030
(backlog, trigger-subscribed), spikes
SP-0004 (draft-ahead,
ratified with this bundle) and
SP-0005 (backlog);
armed TRG-0006–TRG-0009; stubbed
CMP-0005–CMP-0008;
amended EP-0005 (scope,
interfaces, risks→resolutions, Derived Work; set `stale` pending
re-affirmation); added glossary entries **Work-Management Connector**
and **Attribution Block**.

**T13 — Agent (decision-recall audits,
DEC-0137).**
Ran the audit on all fifteen drafts/amendments; two judge forks.
Findings applied — DEC-0150:
sequencing note added to
ST-0019 (check
administration must not harden before the spike's findings);
DEC-0143/DEC-0033:
ST-0021 Out
of Scope now distinguishes human-attributed reviews from
machine-verified auto-PR approvals, which carry no attribution block;
DEC-0040: role claims
in ST-0022
criterion 3 include active time-bounded delegations;
DEC-0079: hermetic
fake-connector criterion added to
ST-0023;
DEC-0152:
adapter-credential criterion added to
ST-0024;
DEC-0141:
pass→fail un-passing added to
SP-0004's
validation matrix. "Nothing to add" verdicts: all six deferred/backlog
stories, SP-0005,
ST-0020, and
the amended epic. The judges' flagged contract gaps were repaired by
amending two approved artifacts, now `stale` for re-affirmation in
this gate bundle:
ST-0006 and
CMP-0001 drop the
`set-jira-status` mechanical operation (cancelled by
DEC-0151)
and gain `migrate-person-ids`, giving
ST-0022's
bootstrap-identity migration its sanctioned typed operation (per
DEC-0046,
DEC-0033).

## Decisions Produced

DEC-0148,
DEC-0149,
DEC-0150,
DEC-0151,
DEC-0152,
DEC-0153,
DEC-0154,
DEC-0155,
DEC-0156

## Conflicts Raised

None — the DEC-0048/DEC-0095
telemetry tension was resolved in-session by
DEC-0151
before it hardened into a conflict.
