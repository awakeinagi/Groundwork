---
id: DEC-0044
type: decision
title: Jira drift is reverted and captured as a change proposal
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  On detecting a direct edit to a canonical-owned Jira field, the connector
  promptly restores the projection to canonical content and comments on the
  issue with explanation and links. The edit is not discarded; its diff is
  captured as a Change Proposal artifact (DEC-0047) routed to the item's
  refinement flow. The agent triages it—trivial changes become a mechanical-fix
  PR citing the CP; substantive changes trigger a refinement session invitation
  to the editor. This converts drift from an error into an input and makes the
  redirect respectful of the editor's work while maintaining canonical truth.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T2-T3"
links:
  derives-from: [SES-0005]
---

# DEC-0044: Drift → revert + capture as change proposal

## Context

DEC-0002 requires reconciling Jira edits
toward canon; the open question was what happens to the editor's work.

## Decision

On detecting a direct edit to a canonical-owned Jira field, the connector
promptly restores the projection to canonical content and comments on the
issue with an explanation and links. The edit is **not discarded**: its diff
is captured as a Change Proposal artifact
(DEC-0047) routed to the item's
refinement flow, where the agent triages it — trivial changes become a
mechanical-fix PR citing the CP; substantive changes trigger a refinement
session invitation to the editor.

## Rationale

Hard reverts teach users to distrust the system; leaving drift standing
violates canon. Capturing intent converts drift from an error into an input
and makes the redirect respectful of the editor's work.

## Alternatives Considered

- **Hard revert only**: lost work, adoption damage.
- **Soft drift flag**: Jira displays non-canonical content indefinitely.

## Implications

Drift detection needs the edit's before/after (webhook payload or
event-stream diff on Bitbucket/Jira Data Center); CP triage becomes session
-agent scope (EP-0002, via the EP-0005→EP-0002 impact edge).
