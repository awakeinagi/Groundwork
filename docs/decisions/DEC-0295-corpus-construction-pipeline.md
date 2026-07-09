---
id: DEC-0295
type: decision
title: The knowledge corpus is constructed by an extraction → 10-Haiku-swarm → assembly pipeline with a ≥7/≥7 inclusion bar, stakeholder-ratified before first use, refreshed on demand
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0054 @ T8-T12"
overview: >-
  Stakeholder-designed pipeline (SES-0054 T8) for building the
  system-architecture-bp corpus: an extraction agent builds an
  exploration list from the CC0 awesome-software-architecture index
  plus seeded free-to-read canon (c4model.com, martinfowler.com,
  microservices.io, AWS and Azure Well-Architected); a swarm of 10
  Haiku subagents (model passed explicitly at every spawn) explores
  the sources in parallel, each reporting per source: URL, a ≤200-word
  high-level summary, a relevancy score /10 for our needs, and a
  content-quality score /10. The facilitator assembles the reference
  material from the reports, with a generator subagent at the
  facilitator's model class drafting reference docs. Inclusion bar:
  relevancy ≥7 AND quality ≥7; borderline sources become appendix
  pointers. The stakeholder reviews and signs off on the corpus before
  the agent goes live. Refresh is on demand only — no schedule, no
  trigger — with corpus dates stamped so staleness stays visible. The
  pipeline ran in SES-0054's apply step.
links:
  derives-from: [SES-0054]
  relates-to: [DEC-0294, DEC-0292]
---

# DEC-0295: Corpus Construction Pipeline

## Context

DEC-0294 fixes what the corpus is and where it lives; this decision
fixes how it gets built. The stakeholder amended the facilitator's
"author a distillation" recommendation into an explicit multi-agent
research pipeline (SES-0054 T8).

## Decision

The `system-architecture-bp` corpus is constructed by this pipeline:

1. **Extraction** — an agent extracts from the vendored CC0
   awesome-software-architecture index a list of relevant
   docs/articles to explore, seeded additionally with the
   free-to-read canon: c4model.com, martinfowler.com architecture
   catalogs, microservices.io, and the AWS and Azure Well-Architected
   frameworks.
2. **Swarm exploration** — the list is handed to a swarm of **10
   Haiku subagents** (the Haiku model specified explicitly at every
   spawn), exploring sources in parallel. Each agent reports back,
   per source: the source URL, a high-level summary of **≤200
   words**, a **relevancy score /10** for our needs, and a
   **content-quality score /10**.
3. **Assembly** — the facilitator constructs the agent's reference
   material from those reports, with a generator subagent (inheriting
   the facilitator's model class) drafting the reference docs it
   judges helpful.

**Inclusion bar**: relevancy **≥7 AND** quality **≥7**; borderline
sources (a score of 5–6) are kept as appendix pointers only.

**Ratification**: the stakeholder reviews and signs off on the
constructed corpus **before the agent goes live**; the agent
definition and corpus land together.

**Refresh**: on demand only — re-run via normal intake when instructed
or when consultations visibly miss current practice. Corpus dates are
stamped so staleness stays visible. The initial run happens in
SES-0054's apply step.

## Rationale

Parallel cheap-model exploration scales source coverage at bounded
cost while keeping scoring per-source and comparable; the explicit
report format makes assembly mechanical and auditable. The double-7
bar keeps the distillation sharp with a graceful degradation path
(appendix pointers). Sign-off before first use follows from the
agent's whole value riding on this content. On-demand refresh avoids
standing maintenance burden that a schedule or armed trigger would
create.

## Alternatives Considered

- **Facilitator-authored distillation, no pipeline** — the original
  recommendation; superseded by the stakeholder's pipeline design.
- **Sum ≥14 or facilitator-judgment inclusion** — rejected for the
  mechanical, repeatable double-7 bar.
- **Post-hoc spot-check or no ratification** — rejected: a bad corpus
  would surface mid-refinement-session.
- **Scheduled or trigger-based refresh** — rejected: recurring cost
  whether or not anything changed.

## Implications

The system-architect agent (DEC-0292) cannot be used until the
initial pipeline run completes and the stakeholder signs off on the
corpus. Every pipeline run spawns ~12 subagents (extraction, 10 Haiku
explorers, generator) and its swarm reports are working material, not
corpus artifacts — only the assembled reference material lands in the
system-architecture-bp skill (DEC-0294), stamped with construction
dates. Re-runs enter via normal change intake.
