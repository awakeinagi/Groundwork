---
id: SES-0005
type: session
title: EP-0005 refinement — review identity, drift, host variance, person registry
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0005, EP-0003, EP-0001]
---

# SES-0005: EP-0005 Refinement Session

## Purpose

Refine EP-0005 (Connectors &
Identity) to gate-readiness, absorbing the requirements accumulated from
SES-0003 (PR orchestration, host permission model) and SES-0004 (policy
compilation, team/required-check administration, host variance).

## Transcript

**T1 — Sponsor.** Approved EP-0003. Proceed to EP-0005.

**T2 — Agent.** Round 1: (a) acting-on-behalf for UI-driven PR reviews when
business approvers may lack code-host seats (recommended per-user OAuth
with a program-user fallback carrying verified attribution); (b) what
happens to a direct Jira edit under reconcile-toward-canon (recommended
revert + capture the edit as a change proposal routed to refinement);
(c) absorbing Bitbucket/GitHub variance (recommended capability-declaring
connectors with a documented minimum set and gate-compiler adaptation);
(d) the person registry tying OIDC/host/Jira identities together
(recommended `governance/people.yaml` with stable person-ids).

**T3 — Sponsor.** All four as recommended.

**T4 — Agent.** Round 2: (a) representation of the "change proposal"
concept T3(b) introduced (recommended first-class CP artifact type);
(b) projection timing and field ownership once implementation moves tickets
(recommended project-on-approval; content fields canonical-owned, workflow
fields Jira-owned syncing in as telemetry); (c) governance of the agent's
read-only codebase scope (recommended `governance/repos.yaml` allowlist);
(d) which host connectors v1 ships (multi-select).

**T5 — Sponsor.** (a) First-class CP artifact. (b) Project on approval with
split field ownership. (c) Allowlist in governance config. (d) **Bitbucket
Data Center only** for v1.

**T6 — Agent (synthesis).** Distilled DEC-0043–DEC-0050. Added the Change
Proposal artifact type (SPEC, checker, directory). Noted consequences of
the Bitbucket Data Center baseline: no native path-scoped reviewer
requirements, so the `gate-policy` required check carries more enforcement
weight on BBDC, and merge-check/Code Insights integration is the native
required-check surface; Jira Data Center is the likely (unconfirmed) Jira
flavor. Extended the EP-0005→EP-0002 impact edge: CP triage becomes session
-agent scope. EP-0005 moved to `gated`.

## Decisions Produced

DEC-0043,
DEC-0044,
DEC-0045,
DEC-0046,
DEC-0047,
DEC-0048,
DEC-0049,
DEC-0050

## Conflicts Raised

None.
