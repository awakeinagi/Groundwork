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

### Browsing the docs (human-readable rendering)

Artifact bodies store cross-references as bare IDs (per DEC-0242), so
raw markdown is optimized for agent context, not human reading. The
single-page viewer at `docs/human_docs.html` is the human surface
(per DEC-0244, DEC-0245): rendered markdown, clickable
cross-references, per-artifact backlinks ("referenced by"), status
badges, frontmatter chips, full-text search, and Mermaid diagrams.

```
python3 tools/serve_docs.py         # default port 8420
# then open http://127.0.0.1:8420/docs/human_docs.html
```

`serve_docs.py` also exposes the skill's semantic search and graph
tools as `/api` endpoints — the viewer's "Advanced search" panel
(requires `uv` on PATH). Any static server with directory listings
works for plain browsing (`python3 -m http.server` from the repo
root); the advanced panel simply hides itself. Internet access is
needed at view time for the Tailwind/Mermaid CDNs.

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
