---
id: SES-0003
type: session
title: EP-0001 refinement — git model, access, concurrency, validation
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0001, SP-0001]
---

# SES-0003: EP-0001 Refinement Session

## Purpose

Refine EP-0001
(Artifact Store & Format Engine) to gate-readiness: settle the git model,
access paths, concurrency contract, ID allocation, gate surface, mechanical
writes, validation tiers, and transcript enforcement. Also captured sponsor
guidance extending SP-0001.

## Transcript

**T1 — Sponsor.** Additional context for SP-0001: investigate whether
"subject to change" decisions or best guesses are made on the *impacted*
items first (by the agent, with humans involved as needed) to provide
guidance and boundaries for the item that will impact them. Then: proceed
with EP-0001's refinement.

**T2 — Agent.** Folded provisional-bounding-decisions into SP-0001's method
(including interaction with staleness machinery and whether a `provisional`
decision status is needed). Opened EP-0001 round 1: (a) git model
(recommended trunk-only + status field); (b) access paths (recommended API
writes, sanctioned git reads); (c) concurrency (recommended optimistic
versioning); (d) ID allocation (recommended committed counter file).

**T3 — Sponsor.** (a) Neither recommended option — a **fork-pull model**:
the application/agent owns a local fork of the upstream doc repo; the agent
opens a branch per item (BG, EP, story, spike, …), committing changes as the
item is refined, including associated sessions and decisions; opening the
branch also opens a PR against upstream main; **approving the PR is the
human-in-the-loop sign-off** for the associated designs; post-merge changes
to the same item reuse the branch with a new PR; when conflicts arise,
consider per-user branches (e.g. `EP-0010-epic_desc-user1`,
`EP-0010-epic_desc-user2`). (b) API writes with sanctioned read-only git
access, as recommended. (c) A **worktree per user session**: if the
session's worktree is the only version of the item, it merges into the
generic item branch; if multiple versions or a conflict exist, user-suffixed
branches are used. (d) ID allocation serialized by a thread/process-safe
lock on the API server.

**T4 — Agent.** Round 2, probing the frictions the PR-gate model creates:
(a) gate surface — where approvers click approve, given DEC-0002 says users
interface via the Groundwork UI (recommended: UI wraps the PR via the
code-host connector); (b) whether mechanical writes (stale marks, jira-keys,
transcript appends, counters) bypass PR gates (recommended: direct commit
from an allowlist); (c) validation timing (recommended two-tier: schema on
every write, completeness at the PR gate); (d) transcript append-only
enforcement and where session artifacts live (recommended: store-enforced,
riding the item branch).

**T5 — Sponsor.** (a) UI wraps the PR. (b) Direct commit preferred, with two
concerns: enterprise rules may forbid direct commits to upstream main
(perhaps a program-user that can approve), and safeguards are needed so the
agent can only commit metadata/append-only mutations and cannot bypass the
approval process — everything-through-PRs would guarantee that but creates
approval spam. (c) Two-tier validation. (d) Store-enforced append-only, on
the item branch.

**T6 — Agent (synthesis).** Resolved T5(b) with credential separation plus
typed operations: the LLM agent holds no git credentials; all writes are
typed storage-service operations (append-turn, mark-stale, set-jira-key, …),
so the service constructs every commit and an arbitrary diff is
inexpressible through the mechanical path. Where branch protection forbids
direct pushes, the service falls back to auto-PRs approved by a program
user, with a deterministic mechanical-diff CI check (diff touches only
allowlisted fields/append regions) as a required check — machine
verification replaces human spam. EP-0001 updated accordingly and moved to
`gated`, awaiting sponsor sign-off.

## Decisions Produced

DEC-0028,
DEC-0029,
DEC-0030,
DEC-0031,
DEC-0032,
DEC-0033,
DEC-0034,
DEC-0035

## Conflicts Raised

None.
