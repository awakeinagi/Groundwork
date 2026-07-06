---
id: DEC-0049
type: decision
title: Agent codebase reads are governed by an allowlist in governance config
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T4-T5"
links:
  derives-from: [SES-0005]
---

# DEC-0049: Repo read allowlist in governance config

## Context

The agent's existing-context feeds include read-only codebase access
([DEC-0016](DEC-0016-agent-context-feeds.md)); the scope of that access
needed governance.

## Decision

`governance/repos.yaml` lists the repositories the agent may read, with
optional path excludes for secrets or sensitive areas; connector tokens are
read-only and scoped to the list; changes are PR-gated like all governance
([DEC-0037](DEC-0037-governance-as-code.md)). Any Decision influenced by
code the agent read cites repo + ref, keeping provenance intact.

## Rationale

Org-wide read effectively grants everyone who can prompt the agent access
to every repo; per-session grants are unusable friction. A gated allowlist
is the auditable middle.

## Alternatives Considered

- **Org-wide discovery**: over-broad, prompt-injection amplifier.
- **Per-session grants**: routine refinement stalls on approvals.

## Implications

The code-host connector's read operations take the allowlist as a hard
filter; repo+ref citation format is a story-level spec item.
