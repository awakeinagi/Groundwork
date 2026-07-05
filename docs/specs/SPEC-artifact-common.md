# SPEC: Common Artifact Format

Every artifact in the Canonical Store is a markdown file with YAML frontmatter,
obeying this spec plus its type-specific spec. This spec is language-agnostic:
any implementation of Groundwork (Python, TypeScript, or otherwise) must
produce and validate exactly this format ([DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).

## Identity

- Every artifact has an immutable ID: `<PREFIX>-<4-digit zero-padded number>`.
- Prefixes: `BG` (Business Goal), `EP` (Epic), `ST` (Story), `SP` (Spike),
  `CMP` (Component Doc), `SES` (Session), `DEC` (Decision), `CFL` (Conflict),
  `CON` (Consolidation).
- Numbers are allocated sequentially per prefix and never reused, even for
  deleted artifacts.
- Filename: `<ID>-<kebab-case-slug>.md` in the type's directory. The slug may
  change; the ID may not.

## Frontmatter

```yaml
---
id: EP-0002
type: epic            # business-goal | epic | story | spike | component |
                      # session | decision | conflict | consolidation
title: Refinement Session Agent
status: draft
owner: eng-lead       # role or named person accountable for the gate
created: 2026-07-05
links:
  derives-from: [BG-0001]     # immediate parent(s) in the pipeline
  satisfies: [BG-0001]        # business goal(s) ultimately served
  depends-on: []              # artifacts this one requires (e.g. CMP contracts)
  conflicts-with: []          # open conflicts (paired with a CFL artifact)
  supersedes: []              # earlier artifact(s) this replaces
  relates-to: []              # weak association (context, not derivation)
  impacts: [EP-0004]          # same-type siblings whose decisions this
                              # artifact's refinement will shape
  impacted-by: [EP-0001]      # inverse: siblings whose refinement shapes this
cites: [DEC-0015, DEC-0021]   # decisions that shaped this artifact
---
```

Rules ([DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)):

- All link values are bare artifact IDs. Link types are closed vocabulary:
  `derives-from`, `satisfies`, `depends-on`, `conflicts-with`, `supersedes`,
  `relates-to`, `impacts`, `impacted-by`. Decision citations use the
  top-level `cites` field.
- **Impact links** ([DEC-0026](../decisions/DEC-0026-directional-impact-links.md)):
  "X impacts Y" means decisions recorded while refining X are expected to
  constrain, shape, or invalidate decisions in Y. Impact links connect
  same-type artifacts only, and both endpoints record the relationship —
  `impacts` on X, `impacted-by` on Y. Refinement order among siblings is
  ranked over this graph ([DEC-0027](../decisions/DEC-0027-impact-ranked-refinement-order.md)).
- Empty link lists may be omitted.
- The Graph Index is built solely from frontmatter; prose wiki-links are
  navigational sugar and carry no semantics.

## Status lifecycle

```
draft ──▶ in-refinement ──▶ gated ──▶ approved ──▶ (stale ⇄ approved)
                                          │
                                          ├──▶ superseded
                                          └──▶ archived
```

- `draft` — generated or authored, not yet in active refinement.
- `in-refinement` — under active Q&A / editing.
- `gated` — refinement complete, awaiting Approver sign-off per the Gate
  Policy ([DEC-0006](../decisions/DEC-0006-gate-every-stage.md),
  [DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md)).
- `approved` — human-ratified; may feed the next pipeline stage.
- `stale` — upstream basis changed after approval
  ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md)). Blocks
  new downstream generation until re-ratified back to `approved`.
- `superseded` / `archived` — terminal. A superseding artifact must link
  `supersedes: [<old id>]`.

Decisions and Sessions use reduced lifecycles defined in their own specs.

## Body conventions

- Body sections are defined per type-spec. Required sections must be present
  even if brief; "N/A — <reason>" is acceptable and auditable.
- Reference other artifacts inline as `[<ID>](relative/path.md)`; the
  authoritative relationship still lives in frontmatter.
- Convert relative dates to absolute dates.
- Use glossary terms from [CONTEXT.md](../../CONTEXT.md) exactly. If a needed
  term is missing or contested, resolve it in the glossary first
  ([DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).

## Integrity rules (enforced by `tools/check_links.py`)

1. IDs are unique; frontmatter `id` matches the filename prefix.
2. Every linked or cited ID resolves to an existing artifact.
3. Every `epic | story | spike | component` traces to at least one
   Business Goal through `derives-from`/`satisfies` chains.
4. Every Decision has a `derives-from` pointing at a Session or Spike.
5. No approved artifact links `conflicts-with` an open Conflict.
6. Impact links are reciprocal and same-type: `X.impacts ∋ Y` iff
   `Y.impacted-by ∋ X`, and X and Y share an artifact type.
