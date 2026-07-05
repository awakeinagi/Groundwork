---
id: DEC-0001
type: decision
title: Groundwork is a standalone application
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T2-T3"
links:
  derives-from: [SES-0001]
---

# DEC-0001: Groundwork is a standalone application

## Context

The described capabilities (pluggable Q&A UI, doc storage, Jira and code-host
connectors) could be delivered either as Claude Code skills operating on a git
repo with thin adapters, or as a real application with services, storage, and
a web UI.

## Decision

Groundwork is built as a standalone application: web UI for refinement
sessions, backend services, and connector integrations.

## Rationale

Business stakeholders must interact with the system directly and unsupervised
([DEC-0003](DEC-0003-unsupervised-sessions.md)); they will not work in a
terminal. A skills-first approach cannot deliver that experience.

## Alternatives Considered

- **Skills + git docs first** (agent's recommendation): cheapest path to
  validating the process, but leaves business users without an interface.
- **Hybrid from day one**: skills for agent logic behind a minimal web UI;
  rejected as an awkward halfway point.

## Implications

Real application concerns arrive early: auth ([DEC-0024](DEC-0024-pluggable-auth.md)),
roles and gates in the UI ([DEC-0006](DEC-0006-gate-every-stage.md)), and a
production-quality session experience.
