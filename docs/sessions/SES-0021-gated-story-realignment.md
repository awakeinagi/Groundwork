---
id: SES-0021
type: session
title: Realign gated EP-0001 stories with release scoping, trigger subscriptions, and infrastructure ports
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [ST-0001, ST-0007, ST-0008, ST-0010, EP-0001, DEC-0121, DEC-0077]
---

# SES-0021: Gated-Story Realignment

## Purpose

The eight gated stories ([ST-0001](../stories/ST-0001-tier1-schema-suite.md)–[ST-0008](../stories/ST-0008-change-event-stream.md))
were gated on 2026-07-06, before four design sessions landed:
[SES-0016](SES-0016-version-scoped-stories.md) (release scoping),
[SES-0017](SES-0017-v1-storage-stack-and-triggers.md) (embedded stack +
trigger registry), [SES-0018](SES-0018-trigger-subscriptions.md)
(trigger subscriptions), and
[SES-0020](SES-0020-pluggable-infrastructure-ports.md) (infrastructure
ports). This session audits the gated set against the decisions those
sessions produced, agrees the amendments, and resolves a wording
tension between [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)
and [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md).

## Transcript

**T1 — awakeinagi.** Asked the facilitator to revisit the gated stories
and see if they need updating given the recent changes to the design.

**T2 — facilitator.** Presented the audit verdict: two stories need
real amendment, one a light touch, five are unaffected, and
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) has a
new coverage gap. Specifically: (1)
[ST-0007](../stories/ST-0007-tier2-check-suite.md)'s check inventory is
missing the release-scoping rule family
([DEC-0097](../decisions/DEC-0097-deferred-status.md),
[DEC-0098](../decisions/DEC-0098-semver-release-labels.md),
[DEC-0099](../decisions/DEC-0099-releases-declared-in-goal-scope.md),
[DEC-0101](../decisions/DEC-0101-deferred-out-of-metrics.md),
[DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md)) and the
trigger-registry rule family
([DEC-0108](../decisions/DEC-0108-trigger-surfacing.md),
[DEC-0109](../decisions/DEC-0109-trigger-subscriptions.md),
[DEC-0110](../decisions/DEC-0110-subscription-lifecycle.md));
(2) [ST-0001](../stories/ST-0001-tier1-schema-suite.md)'s frontmatter
schemas must validate the `deferred` status and `release:` grammar;
(3) [ST-0008](../stories/ST-0008-change-event-stream.md)'s outbox
criterion should be phrased against the app database port
([DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
[DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
[DEC-0124](../decisions/DEC-0124-v1-adapter-set.md));
(4) no story delivers the app database port
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) now
lists in Interfaces & Contracts — recommended a new story rather than
folding it into
[ST-0008](../stories/ST-0008-change-event-stream.md), since the port
serves outbox and bookkeeping and the conformance suite is a distinct
deliverable. Flagged one genuine tension:
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md) lists
"counters" among app-database-port workloads while
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md) says no
persistent ID-counter store exists anywhere; recommended reading
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)'s "counters"
as operational bookkeeping counters, leaving
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md) intact, rather
than superseding it. Noted
[SES-0019](SES-0019-semantic-search-hybrid-tooling.md) does not touch
the gated set (its product output
[ST-0009](../stories/ST-0009-hybrid-search-capabilities.md) is deferred
backlog and skill tooling is outside the port requirement per
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
[ST-0002](../stories/ST-0002-storage-api-core.md),
[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md),
[ST-0004](../stories/ST-0004-session-worktree-management.md),
[ST-0005](../stories/ST-0005-id-allocation.md), and
[ST-0006](../stories/ST-0006-typed-mechanical-writes.md) are
unaffected.

**T3 — awakeinagi.** Asked for an overview of the proposed
"counters = non-ID bookkeeping" reading of
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md).

**T4 — facilitator.** Explained the collision and the reading:
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md) is a specific,
deliberate decision that ID-counter state has no persistent store —
rescan-on-boot over all refs — chosen so no second source of truth can
drift from git; [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)'s
"counters" is one word in an illustrative workload list, its session
never discussed ID allocation, and it does not list
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md) as superseded.
Proposed reading: the port's counters are operational bookkeeping
(outbox retry counts, debounce state, session-inactivity tracking) —
losable inconvenience, not truth; ID counters are derivable truth about
the repo and stay rescan-only. Supersession in Groundwork is explicit,
never incidental; specific beats general; and the engineering still
favors rescan-on-boot. Consequences: no change to
[ST-0005](../stories/ST-0005-id-allocation.md); the new port story's
scope wording makes the exclusion explicit; the alternative
(superseding [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md))
was not recommended.

**T5 — awakeinagi.** "Agreed on all three — run SES-0021 as proposed."
Ratified: (1) amend
[ST-0001](../stories/ST-0001-tier1-schema-suite.md),
[ST-0007](../stories/ST-0007-tier2-check-suite.md), and
[ST-0008](../stories/ST-0008-change-event-stream.md) as presented;
(2) derive a new story
([ST-0010](../stories/ST-0010-app-database-port.md)) for the app
database port; (3) the counters-as-operational-bookkeeping reading of
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md), with
[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md) standing.

## Decisions Produced

- [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)
  — clarifying, not superseding:
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)'s app-database-port
  "counters" are operational bookkeeping; artifact-ID allocation state
  stays rescan-only per
  [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md).

The story amendments themselves cite already-accepted decisions — they
are alignment, not new design.

## Conflicts Raised

None — the [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)/[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)
tension was resolved in-session by clarification
([DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).
