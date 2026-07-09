# Groundwork

Groundwork is a documentation-first system that refines raw business ideas into
contract-complete component specifications an implementation swarm (AI agents or
developers) can build in parallel — while keeping every artifact traceably
grounded in the business intent that motivated it.

An AI agent conducts unsupervised 1:1 refinement sessions with stakeholders,
product owners, and engineering/data-science leads. Each stage of refinement is
human-gated, every decision is provenance-linked back to the conversation that
produced it, and the whole artifact graph is validated for integrity.

**The docs are the product.** Groundwork's responsibility ends at approved,
contract-complete component docs plus a machine-readable handoff manifest.
Orchestrating the implementation swarm is out of scope (see
[DEC-0014](docs/decisions/DEC-0014-docs-are-the-product.md)).

## The pipeline

```
Idea ──▶ Refinement Sessions ──▶ Business Goal ──▶ Epics ──▶ Stories / Spikes ──▶ Component Docs ──▶ Handoff Manifest
              (SES)                  (BG)            (EP)         (ST / SP)            (CMP)
                │                     ▲               ▲               ▲                  ▲
                └── Decisions (DEC) ──┴───────────────┴───────────────┴──────────────────┘
                     every artifact cites the decisions that shaped it
```

Each stage transition passes a human **approval gate**. Conflicts between
stakeholder requests become first-class Conflict artifacts that block downstream
generation until resolved.

## Repository layout

| Path | Contents |
|---|---|
| `CONTEXT.md` | System-wide glossary (the ubiquitous language) |
| `docs/specs/` | Format specifications for every artifact type |
| `docs/goals/` | Business Goals (`BG-*`) |
| `docs/epics/` | Epics (`EP-*`) |
| `docs/stories/` | Stories (`ST-*`) |
| `docs/spikes/` | Spikes (`SP-*`) |
| `docs/components/` | Component docs (`CMP-*`) |
| `docs/sessions/` | Refinement session records (`SES-*`) |
| `docs/decisions/` | Decision records (`DEC-*`) |
| `docs/conflicts/` | Conflict artifacts (`CFL-*`) |
| `docs/change-proposals/` | Change proposals (`CP-*`) |
| `docs/consolidations/` | Curated context consolidations (`CON-*`) |
| `tools/` | Validation tooling (link/graph integrity checker) |

## Core rules

1. **This repo is canonical.** Jira and any other surface are projections;
   drift is detected and reconciled back here, never the reverse.
2. **Typed links + stable IDs.** Every artifact has an immutable ID and
   declares typed relationships in YAML frontmatter. See
   [SPEC-artifact-common](docs/specs/SPEC-artifact-common.md).
3. **Provenance.** Requirements and contracts cite Decision records; Decisions
   cite the session (or spike) that produced them.
4. **Gates.** No artifact feeds the next stage until its gate is approved.
5. **Staleness.** When an upstream artifact changes, impact analysis marks
   descendants `stale`; stale artifacts block new downstream generation.

Validate the graph at any time:

```
python3 tools/check_links.py
```

Browse the docs with rendered markdown, clickable cross-references,
backlinks, and semantic/graph search (per DEC-0244):

```
python3 tools/serve_docs.py     # then open http://127.0.0.1:8420/tools/viewer.html
```

## Dogfooding

Groundwork is specified using its own artifact formats. The grilling session
that produced this design is [SES-0001](docs/sessions/SES-0001-groundwork-inception.md);
the system's own business goal is [BG-0001](docs/goals/BG-0001-groundwork.md).

## Acknowledgements

Groundwork's interview technique — grilling — is an elaboration of
[Matt Pocock](https://github.com/mattpocock)'s
[`grilling` skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md).
Thanks, Matt, for the original description of the technique; see
[.agents/skills/groundwork-design-session/references/grilling.md](.agents/skills/groundwork-design-session/references/grilling.md)
for how it's cited and applied here.
