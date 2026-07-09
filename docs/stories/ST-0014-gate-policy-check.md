---
id: ST-0014
type: story
title: The gate-policy required check
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0012, ST-0013, ST-0016]
  impacts: [ST-0018]
  impacted-by: [ST-0012, ST-0013, ST-0016]
cites: [DEC-0020, DEC-0033, DEC-0036, DEC-0038, DEC-0040, DEC-0043, DEC-0141,
        DEC-0143, DEC-0145, DEC-0234]
---

# ST-0014: The `gate-policy` Required Check

## Summary

The service-computed check that makes PR merges meaningful: evaluates
everything richer than the host can express — domain-conditional
approvers, quorum composition, ancestor staleness, attribution — and
keeps its verdicts fresh while PRs sit open.

## Acceptance Criteria

1. The check evaluates the rich policy layer: domain-conditional
   approvers, role verification against `governance/roles.yaml`, and
   committee quorum composition by distinct roles
   (per DEC-0020,
   DEC-0036).
2. The check fails while any ancestor of the PR's artifact is stale,
   and passes only once every stale ancestor has cleared
   (per DEC-0038).
3. Any member of the required role's pool satisfies a gate by default;
   domain preference affects routing only, unless the policy sets an
   exclusivity flag — in which case only the named approver or their
   active time-bounded delegate passes
   (per DEC-0040).
4. Reviews posted by a program user pass only with verified human
   attribution (per DEC-0043).
5. Every check result carries a human-readable explanation naming the
   governing policy, the facts that satisfy it, and — on failure —
   exactly what is missing
   (per DEC-0036).
6. Verdicts recompute idempotently on relevant ChangeEvents and host
   webhooks, with a periodic reconciliation sweep re-verifying all open
   PRs as the backstop
   (per DEC-0145).
7. Merging a governance change bulk-recomputes the check on every open
   PR under the new policy, with existing host reviews standing as
   facts re-evaluated against it
   (per DEC-0141).
8. On the machine-verified path — program-user auto-PRs for mechanical
   writes and System Decisions — the check passes with program-user
   approval when the corresponding validator (mechanical-diff or
   template-conformance) passes: machine verification substitutes for
   role-pool approval on exactly these PRs and no others
   (per DEC-0033,
   DEC-0143).

## Component Impact

CMP-0004 — supplies
its `gate-policy` evaluation contract sections.

CMP-0016 —
supplies the shared role-membership/delegation evaluation the check's
role verification rides on
(per DEC-0234).

## Out of Scope

Structural validity — the tier-2 suite owns it
(ST-0007); conflict blocking
(ST-0015); producing
the staleness state this check consumes
(ST-0016).

## Notes for Implementers

Bulk recomputation and the reconciliation sweep share the single-item
evaluation path — one evaluator, three triggers (event, sweep,
governance merge).

Check activity is also an event source: registrations and every
recomputation — event-triggered, sweep, or governance-merge — land in
ST-0018's governance event log, which is where dashboards read this
check's behavior.
