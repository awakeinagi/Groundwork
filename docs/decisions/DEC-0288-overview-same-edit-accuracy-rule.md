---
id: DEC-0288
type: decision
title: Overview accuracy rides a same-edit rule and a gate-prep faithfulness check
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T4-T5"
overview: >-
  Any edit that changes an artifact's meaning updates its overview in
  the same edit, and gate preparation includes an explicit
  "overview still faithful to the body?" checklist item. Drift is a bug,
  not corruption — the body wins (DEC-0285) — but it is a bug the
  process actively prevents at the two moments meaning changes: the
  edit itself and the gate.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0285, DEC-0287]
---

# DEC-0288: Overview Accuracy — Same-Edit Rule and Gate Checklist

## Context

An overview duplicates the artifact's meaning, so every semantic body
edit is a drift opportunity. Mechanical faithfulness checking isn't
feasible; presence/length checks (DEC-0287) don't touch accuracy. A
stale overview silently misleads exactly the agents the feature
serves.

## Decision

Two process obligations keep overviews accurate:

1. **Same-edit rule** — any edit that changes an artifact's meaning
   updates the overview in the same edit; an edit that leaves the
   overview stale is an incomplete edit.
2. **Gate-prep checklist item** — preparing any artifact for a gate
   includes explicitly confirming the overview is still faithful to
   the body, recorded with the other gate-prep steps.

## Rationale

These are the two moments meaning changes or is ratified — enforcement
attaches there rather than to a scheduled audit that would find drift
late. Because overviews are non-normative (DEC-0285), residual drift
is recoverable (open the body), so process-level enforcement is
proportionate; heavier machinery (hashes, freshness stamps) would cost
more than the failure it prevents.

## Alternatives Considered

- **Presence-only enforcement, best-effort accuracy** — rejected:
  stale overviews undermine trust in the whole layer.
- **Mechanical drift detection (body hash vs overview stamp)** —
  rejected: flags every cosmetic edit, misses real semantic drift,
  adds bookkeeping.

## Implications

The skill's refinement-process reference and both AGENTS.md files
state the same-edit rule alongside the existing edit disciplines
(e.g. DEC-0246's same-edit parent updates); gate playbooks gain the
faithfulness item. Rule-type decision: apply as a checklist step at
edit and gate time, not by citation.
