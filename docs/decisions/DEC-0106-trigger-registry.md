---
id: DEC-0106
type: decision
title: Trigger registry — docs/TRIGGERS.md with parseable entries, armed-only context loading
status: superseded
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T3-T5"
links:
  derives-from: [SES-0017]
  relates-to: [DEC-0105, DEC-0107, DEC-0108]
---

# DEC-0106: The Trigger Registry

## Context

Deferred work needs watchable revival conditions
(SES-0017 @ T3:
"tracked triggers... in a tracked file"). The design constraint from the
participant: the file must be easily parsable so tooling can retrieve
trigger conditions into an agent's context without excessive token use —
and only the active ones.

## Decision

A single tracked registry, **`docs/TRIGGERS.md`**, holds all triggers.
Each entry follows a strict, regex-extractable format:

```markdown
## TRG-0001 (armed)
**Condition:** <observable, human-testable statement>
**Consequence:** <action> <markdown-linked target artifact(s)>
**Cites:** <markdown link to the decision that armed it>
```

- Entry heading: `## TRG-<4-digit n> (armed|fired|retired)`. TRG numbers
  are sequential and never reused.
- A fired or retired entry additionally carries
  `**Fired:**`/`**Retired:**` with the date, a markdown link to the
  firing/retiring decision, and the outcome.
- **Armed-only context loading**: tooling that feeds agent context pulls
  only `(armed)` entries — a few lines each; fired/retired entries are
  history, read on demand.

## Rationale

A registry file gives one reviewable home and, with the strict format,
machine-parseability comparable to the `**Releases:**` list — without
minting a full artifact type (specs, templates, frontmatter, lifecycle)
for entries that are typically two sentences. The armed-only loading
rule keeps the standing context cost proportional to live conditions,
not accumulated history.

## Alternatives Considered

- **Full TRG- artifact type**: maximum consistency, disproportionate
  machinery for the content size.
- **Frontmatter `triggers:` on the deferred artifact**: no home for
  conditions not tied to one artifact; discovering all armed triggers
  means scanning every file.

## Implications

[SPEC-triggers](../specs/SPEC-triggers.md) defines the format; the
checker validates it (DEC-0108); the
status report and skill tooling parse armed entries. The registry is not
an artifact (no frontmatter, no artifact ID); `TRG-` IDs are
registry-scoped.
