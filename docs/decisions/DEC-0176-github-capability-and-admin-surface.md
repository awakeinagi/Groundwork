---
id: DEC-0176
type: decision
title: CMP-0009 introspects team_sync at install time, declares review_dismissal true, backs branch protection with the classic API, and scopes webhook secrets per installation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0032 @ T4-T5"
links:
  derives-from: [SES-0032]
  relates-to: [DEC-0045, DEC-0141, DEC-0145, DEC-0152, DEC-0168, DEC-0169]
---

# DEC-0176: GitHub Capability and Administration Surface

## Context

Four remaining above-minimum-capability and administration questions
needed concrete GitHub answers for
CMP-0009 to be
contract-complete: how `team_sync`'s capability flag gets determined
given GitHub's org-level permission requirement; whether
`review_dismissal` is declared for v1; which of GitHub's two
overlapping branch-protection systems backs `CodeHostConnector.A-7`;
and how the webhook signing secret required by
DEC-0169 is scoped and
stored.

## Decision

1. **`team_sync` via runtime introspection.** On installation, the
   connector queries its actually-granted permissions and sets the
   manifest's `team_sync` flag to `true` only if org-level
   `members` permission was granted; a repo-only installation
   declares `false`, and CMP-0004's
   policy compiler emulates role routing instead
   (per DEC-0045).
2. **`review_dismissal: true`** — GitHub's
   `pulls/reviews/{id}/dismissals` endpoint is stable and available;
   declaring it lets the policy compiler use native dismissal instead
   of emulating it, including for
   DEC-0141's mid-flight
   recomputation flows.
3. **Classic branch protection backs `A-7`.** Per-branch
   `/branches/{branch}/protection` REST endpoints implement
   `protection.set`/`protection.get`, not the newer repository
   rulesets model.
4. **Per-installation webhook secrets.** Each App installation
   generates and stores its own HMAC-SHA256 signing secret
   (`X-Hub-Signature-256`) in the encrypted app-database secret store
   (per DEC-0152),
   rotated independently per installation.

## Rationale

Runtime introspection for `team_sync` keeps the capability manifest
honest against what a given deployment's App installation actually
received, rather than assuming org-admin cooperation as an install-time
precondition. `review_dismissal` costs nothing to declare true and
gives the policy compiler a native option for an operation
DEC-0141 already needs.
Classic branch protection matches `A-7`'s per-branch
`protection.set(repo, branch, rules)` shape directly and is the more
battle-tested surface; rulesets' extra bulk/org-wide power isn't
required by anything this contract currently needs. Per-installation
webhook secrets isolate blast radius — a single leaked secret
compromises only its own installation's webhook integrity, not every
deployment the Orchestrator App touches.

## Alternatives Considered

- **Fixed `team_sync: true`, install-time requirement**: simpler
  contract, but couples deployability to org admin cooperation and
  produces a manifest that lies about a specific deployment's actual
  capability.
- **`review_dismissal: false` for v1**: reduces v1 scope, but gives up
  a native mechanic DEC-0141's
  recompute story could use, for no cost saved (the API already
  exists and is stable).
- **Repository rulesets**: more powerful (bulk rules across repos,
  richer evaluation modes) but heavier to map onto `A-7`'s per-branch
  shape and less proven for this use case.
- **Single global webhook secret**: simpler to provision, but a single
  leak compromises every installation's webhook integrity at once.

## Implications

CMP-0009's Design
Elements and Implementation Guidance state all four as normative,
citing this decision.
