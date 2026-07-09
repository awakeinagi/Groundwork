---
id: DEC-0279
type: decision
title: A session that modified approved artifacts cannot close until the staleness cascade is marked; re-affirmation rides the existing queue machinery
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0279 constrains session close to require that sessions modifying
  approved artifacts cannot close until the staleness sweep has run and
  superseding decisions and stale marks are durably written. Re-affirmation
  is presented in-session when the participant holds approval rights;
  otherwise stale marks feed ST-0017's existing re-affirmation PRs and
  impact-ranked queues. The cascade is marked, never unwalked, and the
  corpus is never left mid-cascade.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T6-T7"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0038, DEC-0265, DEC-0267]
---

# DEC-0279: Cascade marked before close

## Context

DEC-0267 (paradigm) requires modifications to complete their
supersession/staleness cascade inside the session. In the application,
re-affirmation is an asynchronous PR-and-queue flow (ST-0017) — the
strongest reading ("full re-affirmation before close, always") would
hold sessions open indefinitely waiting on absent approvers, which
DEC-0265's carve-out explicitly rejects.

## Decision

ST-0032's close contract gains the invariant: a session that modified
approved artifacts cannot close until the staleness sweep has run and
the superseding DECs and stale marks are durably written — the cascade
is *marked*, never unwalked. Re-affirmation is presented in-session
when the participant holds the approval right (the solo case — it
resolves before close); otherwise the stale marks feed ST-0017's
existing re-affirmation PRs and impact-ranked queues. ST-0032 gains
impact edges to ST-0016 and ST-0017; EP-0003's contracts are
unchanged.

## Rationale

Stale marks are the durable record DEC-0267 demands; a post-close
cascade job recreates exactly the forgotten-inconsistency queue the
decision exists to prevent (a crash between close and job leaves the
corpus mid-cascade).

## Alternatives Considered

- **Full re-affirmation before close, always**: impossible
  multi-party.
- **Cascade as a post-close job**: directly contradicts DEC-0267's
  "never left mid-cascade at close".

## Implications

The engine invokes ST-0016's sweep and the `mark-stale` typed
operation synchronously at close time; ST-0016/ST-0017 list the new
`impacted-by` edge, with the impactor prose in ST-0032.
