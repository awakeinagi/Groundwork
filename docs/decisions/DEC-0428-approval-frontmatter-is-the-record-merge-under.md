---
id: DEC-0428
type: decision
title: "Approval: frontmatter is the record; merge under branch protection is team-mode enforcement"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T14, T19, T20, T21, T31"
accepted-in: SES-0082
overview: >-
  The approval record is the artifact's approved-by/approved-on
  frontmatter in every mode. In team mode, gated changes reach main
  only via a pull request merged per the recorded approver's
  authority, with approver-merger match enforced by branch
  protection or a CI check. Approval on an unmerged branch has no
  effect; main is ground truth. Solo god-mode retains direct commit;
  PRs are a host feature, not paradigm core.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0263, DEC-0136, DEC-0265, DEC-0174]
---

# DEC-0428: Approval — frontmatter is the record; merge under branch protection is team-mode enforcement

## Context

DEC-H established branch-per-session with a pull request at close, but SES-0082 still needed to say precisely what "approved" means across modes, and how the approver-of-record is enforced when a pull request, not a direct commit, is what lands a change.

## Decision

The approval record is the artifact's approved-by and approved-on frontmatter fields in every mode. In team mode, gated changes reach main only through a pull request merged in accordance with the recorded approver's authority, with the approver-merger match enforced by projected branch protection where the host supports it and by a continuous-integration check otherwise. Approval frontmatter on an unmerged branch has no effect; main is ground truth. Solo god-mode retains direct commit. Pull requests are a git-host feature, not part of the paradigm core, so no paradigm semantics depend on a specific host.

## Rationale

Keeping the frontmatter fields as the single approval record across every mode preserves the corpus's self-sufficiency — an artifact's approval status is legible from the file itself, without needing to consult a specific git host's UI or API. Layering host-level enforcement (branch protection, CI checks) on top, rather than inside, the paradigm keeps the paradigm portable across git hosts while still giving teams real enforcement.

## Alternatives Considered

Making the git host's own approval mechanism (e.g. a platform's PR-approval feature) the record of truth was rejected — it would tie paradigm semantics to a specific host, violating DEC-0263's host-agnostic governance-as-code stance. Treating an unmerged branch's frontmatter as provisionally approved was rejected — DEC-0252-style ambiguity about "what's approved" was exactly what branch-per-session (DEC-H) was designed to eliminate.

## Implications

Governance configuration (DEC-J) must be able to declare which enforcement level a given host deployment actually provides. Solo god-mode is explicitly unaffected — no PR requirement, no host dependency, direct commit as today.
