---
id: DEC-0090
type: decision
title: Body cross-references must be resolvable markdown links
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0014 @ T2-T3"
links:
  derives-from: [SES-0014]
  relates-to: [DEC-0009]
---

# DEC-0090: Body cross-references must be resolvable markdown links

## Context

[SPEC-artifact-common](../specs/SPEC-artifact-common.md) prescribed inline
references as `[<ID>](relative/path.md)` but nothing enforced it, and the
corpus drifted into a mix of markdown links and bare IDs. Bare IDs make
readers hunt for files, and unvalidated links rot silently when slugs
change (IDs are immutable; filenames are not). Frontmatter reference
semantics are separately governed by
[DEC-0009](DEC-0009-typed-links-stable-ids.md).

## Decision

In artifact **bodies**, every cross-reference to another artifact must be
an inline markdown link `[<ID>](relative/path.md)`. Bare artifact IDs in
body prose — outside fenced code blocks and inline code spans, and
excluding the artifact's own ID — are integrity violations. Frontmatter
link and `cites` values remain bare IDs per
[DEC-0009](DEC-0009-typed-links-stable-ids.md). `tools/check_links.py`
enforces three checks: relative links in bodies resolve to existing files;
a link whose text begins with an artifact ID targets that artifact's file;
no bare artifact IDs appear in body prose.

## Rationale

Clickable references make the provenance chain navigable where humans
actually read it, while keeping machine semantics exactly where
[DEC-0009](DEC-0009-typed-links-stable-ids.md) put them — prose links stay
navigational sugar with no graph meaning. Enforcement is what turns the
existing convention from aspiration into an invariant; without it the
corpus demonstrably drifts.

## Alternatives Considered

- **Keep links optional**: the pre-existing state; drift across the corpus
  showed a non-enforced convention does not hold.
- **Clickable frontmatter links too**: would require superseding
  [DEC-0009](DEC-0009-typed-links-stable-ids.md) and rewriting the Graph
  Index builder and checker parsers, for no machine benefit — rejected for
  blast radius.
- **Resolve-only enforcement** (validate existing links, tolerate bare
  IDs): leaves the readability half of the problem unsolved.

## Implications

[SPEC-artifact-common](../specs/SPEC-artifact-common.md) Body conventions
and Integrity rules updated; `tools/check_links.py` (and the skill's
bundled copy) gains the enforcement rule; artifact templates show the
linked citation form. The existing corpus is brought into compliance via
[DEC-0091](DEC-0091-formatting-only-linkification-pass.md). Future gate
tooling that parses `(per DEC-nnnn)` citations must accept the linked form.
