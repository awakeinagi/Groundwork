---
id: EP-0015
type: epic
title: "Collaboration, Concurrency & Browsing"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Collaboration, Concurrency & Browsing covers multi-actor access to
  a shared corpus — multiple agents, users, and sessions writing
  concurrently — plus the human browsing surface as its read-only
  human face, merged into one epic by DEC-0468. Serves BG-0002
  outcome 1's consistent-concurrent-access implication and the
  skill-mode user who needs corpus browsing without the Application
  (DEC-0443's tension note). In scope: the collaboration/concurrency
  model over the corpus, continuing the already-built concurrent-
  write path under governance; multi-session coordination
  (relationship to SP-0018, currently under EP-0009, to reconcile at
  refinement); team governance configuration (DEC-0443); the human
  browsing surface — rendered markdown, bare-ID cross-reference
  navigation, backlinks, semantic+graph search UI (human_docs.html,
  serve_docs.py). Out of scope: the Application's team-facing
  features and hosting, baseline single-writer corruption safety
  (Engine Core & Artifact Model's definition-of-done), and the
  write-path mechanics themselves (the Engine Core & Artifact Model
  / EP-0009 seam). No outgoing impact edges among current siblings;
  impacted-by Engine Core & Artifact Model and EP-0009. Open risks:
  the SP-0018 ownership seam against EP-0009, and the multi-
  session/multi-user concurrency model beyond the current single-
  repo model as a candidate spike. Derives from BG-0002; draft
  status.
links:
  impacted-by: [EP-0010, EP-0009]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0468, DEC-0443, DEC-0244, DEC-0030, DEC-0427, DEC-0310, DEC-0469]
---

# EP-0015: Collaboration, Concurrency & Browsing

## Summary

Multi-actor access to a shared corpus — multiple agents, users, and
sessions writing concurrently — plus the human browsing surface as
its read-only human face, merged into one epic per DEC-0468.

## Why (Goal Alignment)

Serves BG-0002 outcome 1's consistent-concurrent-access implication
and the skill-mode user who needs corpus browsing without the
Application (DEC-0443's tension note). DEC-0468 merged the
collaboration/concurrency model and the human browsing surface into
one epic since the browsing surface is the read-only human face of
the same shared-corpus model.

## Scope

**In:**
- The collaboration and concurrency model over the corpus — the
  already-built concurrent-write path continues under governance
  here, as documentation/contract obligations per Self-Governance &
  Dogfooding's outcome 4, including the already-built branch-per-
  session-with-PR-at-close protocol DEC-0427 established.
- Multi-session coordination (relationship to SP-0018, currently
  under EP-0009, to reconcile at refinement).
- Team governance configuration (DEC-0443).
- The human browsing surface — rendered markdown, bare-ID
  cross-reference navigation, backlinks, semantic+graph search UI
  (human_docs.html, serve_docs.py), the viewer and API server DEC-0244
  created.

**Out:**
- The Application's team-facing features and hosting (BG-0001).
- Baseline single-writer corruption safety — definition-of-done
  inside Engine Core & Artifact Model, not deferred here.
- The write-path mechanics themselves — the Engine Core & Artifact
  Model / EP-0009 seam (the EP-0010→EP-0015 impact edge: the
  concurrency-safe write path and corpus invariants bound the
  collaboration model this epic builds).

## Domain Context

Bounded context: **Groundwork collaboration, concurrency & browsing**
(per DEC-0462, DEC-0468, DEC-0443). Consumes the concurrency-safe
write path from Engine Core & Artifact Model and the lifecycle domain
from EP-0009; has no outgoing impact edges among current siblings.

## Interfaces & Contracts to Define

- The multi-actor collaboration/concurrency contract: what
  consistency guarantees hold across concurrent agents, users, and
  sessions.
- Team governance configuration schema (DEC-0443).
- The human browsing surface's contract: rendering, navigation,
  backlinks, and search UI.
- The multi-session coordination contract, reconciled against
  EP-0009's SP-0018 relationship.
- The governance-configuration seam with EP-0014: this epic owns the
  team governance-configuration schema — roles, domains,
  gate-policies, and people (DEC-0443) — while EP-0014 owns its
  evaluation as rule families on the Engine-hosted checker (DEC-0469).

## Risks & Open Questions

- Seam against EP-0009's lifecycle domain — SP-0018 (multi-session
  worktrees) currently sits under EP-0009; ownership needs
  reconciling at refinement, including serve_docs.py and
  check_links.py, whose ownership DEC-0310 assigned to the
  artifact-interact tooling under EP-0009 — existing EP-0009-owned
  browsing-surface scripts that are part of the same seam to
  reconcile.
- The concurrency model for multi-session/multi-user access beyond
  the current single-repo model (worktrees, branch-per-session, merge
  semantics) is a candidate spike, informed by SP-0018, building on
  the worktree-per-session collaboration model DEC-0030 established.

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
