---
id: SES-0031
type: session
title: Pivot v1 code host from Bitbucket Data Center to GitHub
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude (Sonnet 5)
transcript-fidelity: reconstructed
links:
  derives-from: [EP-0005]
  relates-to: [ST-0019, ST-0020, ST-0028, SP-0004]
---

# SES-0031: GitHub Replaces Bitbucket Data Center as v1

## Purpose

Immediately after [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
gated in [SES-0030](SES-0030-cmp-0005-code-host-connector-refinement.md),
the Product Owner asked to move Bitbucket Data Center to a future spike
and use GitHub as the v1 code host, since this repository's actual
remote is GitHub and that's the available dogfooding target. This
session covers the resulting pivot: superseding
[DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md), the
downstream amendments it forces, and deriving the GitHub connector's
story and component stub in its place.

## Transcript

**T1 — Product Owner.** "Let's move BBDC to a spike and use Github as
the CodeHost for the v1 build and POC testing; Github is our current
remote so it should be easy to use during this dogfooding session."

**T2 — Facilitator.** Confirmed the actual remote via `git remote -v`
(`github.com/awakeinagi/Groundwork`) and asked three clarifying
questions before touching an accepted, wide-blast-radius decision:
(1) GitHub Cloud vs. GitHub Enterprise Server as the v1 target,
recommending Cloud since it matches the actual remote and no Enterprise
Server instance is available in this session; (2) what happens to BBDC
— recommending deferral to backlog behind a demand trigger, keeping
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) as its
future validation spike, over dropping it with no revival path; (3)
whether the GitHub swap should reopen
[DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)'s
two-layer gate architecture, recommending no — the architecture's
driver is role-conditional/committee logic no host vocabulary
expresses, GitHub's CODEOWNERS included, so this is an implementation
swap, not an architecture change.

**T3 — Product Owner.** Accepted all three recommendations. Also
noted, mid-flight: "The design should be modular and CodeHost should
be pluggable/swappable."

**T4 — Facilitator.** Confirmed this is already the case:
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)'s
protocol is host-agnostic and capability-declaring
([DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md))
precisely so a host swap costs a new adapter, not a contract change —
this pivot is the first live proof of that pluggability, ahead of
schedule (originally [ST-0028](../stories/ST-0028-additional-code-host-connectors.md)'s
job). Recorded [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)
(supersedes [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md))
and [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)
(supersedes [DEC-0166](../decisions/DEC-0166-cmp-0005-drafted-provisional-check-admin.md) —
GitHub's documented Checks API/required-status-checks make the
check-administration provisional flag unnecessary for v1).

**T5 — Facilitator.** Walked the impact of superseding
[DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md) via a
targeted grep for its citers across `docs/`, rather than the graph
tool (declined this turn). Found genuine (not merely
frontmatter-citation) BBDC-specific content in six approved/gated
artifacts:
[EP-0005](../epics/EP-0005-connectors-and-identity.md) (Scope's v1
line, Risks, Derived Work),
[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md) (AC5),
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)
(AC6),
[CMP-0001](../components/CMP-0001-artifact-store-service.md) (`IG-5`),
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)
(`PolicyCompiler.B-5`, `IG-1`, Out of Scope), and
[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
itself (still `gated`, not yet approved, so edited freely rather than
through the staleness/re-affirmation path). Everywhere else citing
[DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md) — several
other decisions' Context/Rationale prose, closed session transcripts —
is either immutable history or doesn't depend on which host is v1, and
was left alone.

**T6 — Facilitator.** Derived
[ST-0031](../stories/ST-0031-github-connector.md) (GitHub connector,
current release) mirroring
[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md)'s
structure, and its stub
[CMP-0009](../components/CMP-0009-github-connector.md), taking BBDC's
former v1 slot. Deferred
[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md) and
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) to
`backlog`, subscribed to a new trigger `TRG-0010` ("a deployment
requires Bitbucket Data Center") — distinct from the generic
`TRG-0007` (other hosts) since [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md)
already had a fully-scoped story of its own, unlike the placeholder
[ST-0028](../stories/ST-0028-additional-code-host-connectors.md).
Amended [ST-0028](../stories/ST-0028-additional-code-host-connectors.md)
to drop GitHub from its host list (no longer "additional") and edited
`TRG-0007`'s condition text accordingly. Re-affirmed
[EP-0005](../epics/EP-0005-connectors-and-identity.md),
[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md),
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md),
[CMP-0001](../components/CMP-0001-artifact-store-service.md), and
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) with the
GitHub-target edits, presenting the diff for approval rather than
re-running full sessions, since none of their contract shapes changed —
only which host is named as v1.

**T7 — Product Owner.** Reviewed and approved the consolidated diff.

## Decisions Produced

- [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md) —
  GitHub (cloud) is the v1 code-host connector; Bitbucket Data Center
  deferred to backlog behind `TRG-0010`. Supersedes
  [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md).
- [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md) —
  check-administration operations no longer provisional; [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)
  repurposed as the BBDC-revival spike. Supersedes
  [DEC-0166](../decisions/DEC-0166-cmp-0005-drafted-provisional-check-admin.md).

## Conflicts Raised

None.
