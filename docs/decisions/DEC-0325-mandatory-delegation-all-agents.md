---
id: DEC-0325
type: decision
title: Librarian delegation is mandatory for all artifact interaction, by all agents
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T4-T5"
overview: >-
  Delegating to the artifact-librarian (DEC-0324) is the sole
  sanctioned way for any agent — main-loop agents and the
  design-session facilitator alike — to interact with corpus
  artifacts: reads, searches, graph queries, and writes. This extends
  DEC-0312's sole-sanctioned-path stance one layer up: DEC-0312 fixed
  WHICH tool may touch artifact files (the typed write API); this
  decision fixes WHO may run the tools (the librarian, on behalf of
  callers). The stakeholder chose everything-mandatory over the
  facilitator-recommended writes-mandatory/reads-discretionary split,
  accepting the cost that even cheap targeted reads become subagent
  tasks in exchange for one uniform rule and maximum caller-context
  isolation. The rule binds agents; the human operator is outside its
  scope. Sanctioned exceptions exist only via the manual-load escape
  hatch (DEC-0327) and agent-definition charters (DEC-0328);
  enforcement mechanism is DEC-0326.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0312, DEC-0326, DEC-0327, DEC-0328]
---

# DEC-0325: Everything-Mandatory Delegation

## Context

With the librarian created (DEC-0324), the binding force needed
fixing: sole sanctioned path, or bypassable default? DEC-0312 already
made the write API the only sanctioned write path; the question was
whether agent-level delegation carries the same force, and for reads
too.

## Decision

For every agent working in a Groundwork project, delegating to the
artifact-librarian is the sole sanctioned way to interact with corpus
artifacts — reads, searches, graph queries, and writes alike. The
facilitator is not exempt. The only sanctioned direct use of the
artifact-interact tooling is under the manual-load escape hatch
(DEC-0327) or an explicit agent-definition charter (DEC-0328).

## Rationale

The stakeholder chose uniformity and maximum context isolation over
the finer-grained writes-only mandate the facilitator recommended:
one rule, no per-operation judgment calls about what counts as a
"cheap" read, and guardrails that live in one place. Task-level
granularity (DEC-0324) mitigates the read-latency cost — a caller
batches its needs into one intent rather than paying a spawn per
lookup.

## Alternatives Considered

- **Writes mandatory, reads discretionary** (facilitator
  recommendation) — matches where the risk is, but two rules and
  per-call judgment; rejected at T5.
- **Advisory default** — discipline-based guardrails, which SES-0057
  explicitly moved away from; rejected.

## Implications

DEC-0321's facilitator Step-0 load of artifact-interact cannot stand
as written — superseded by DEC-0326. Specialized agents that cannot
spawn subagents need charters (DEC-0328). Session recording,
recall-audit packet prep, and gate prep all become librarian tasks.
