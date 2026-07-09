---
id: DEC-0199
type: decision
title: The cross-epic coupling check is generalized to story/spike siblings
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0037 @ T2, T6"
links:
  derives-from: [SES-0037]
  relates-to: [DEC-0196, DEC-0198, DEC-0200]
  supersedes: []
---

# DEC-0199: The Cross-Epic Coupling Check Is Generalized to Story/Spike Siblings

## Context

DEC-0196's coupling check
already does most of what a story-level version needs: parse
`impacts`/`impacted-by`, group by parent, flag mutual coupling. INVEST's
"Independent" criterion makes this signal arguably more important at
story grain than at epic grain, since stories are supposed to be more
independently shippable than epics.

## Decision

`scripts/groundwork_epic_coupling.py` is extended with a `--type
{epic,story}` flag (default `epic`, so
DEC-0196's documented CLI
behavior and output are unchanged). Story mode groups stories and
spikes together, keyed by their parent epic's `derives-from` link, since
they're derived together as one step and can legitimately impact each
other. The same mutual-coupling-only, fan-out-as-context design from
DEC-0196 carries over
unchanged — no new heuristic was needed.

## Rationale

Extending the existing script avoids duplicating its frontmatter-parsing
and mutual-coupling logic for a second artifact type. Regression-testing
epic mode against this project's real epic set produced output
byte-identical to the pre-extension script, confirming the extension is
backward compatible. Smoke-testing story mode against every one of this
project's existing epics' story/spike sets found zero mutual coupling
anywhere — a clean, independent validation of both the tool (no false
positives, unlike the epic check's first ratio-based design) and this
project's existing story-level slicing.

## Alternatives Considered

- **A separate, duplicate script for stories**: rejected — the
  frontmatter-parsing and mutual-coupling-detection logic is identical;
  duplicating it would mean fixing the same bug (like
  DEC-0196's density-display
  bug) twice going forward.
- **Rename the script to something generic** (e.g.
  `groundwork_slice_coupling.py`): rejected — the current filename is
  already cited by ID/path in
  DEC-0196, an accepted
  decision; renaming it would mean updating an already-ratified citation
  rather than additively extending it.

## Implications

`refinement-process.md`'s Story playbook and `SKILL.md`'s coupling-check
paragraph are updated to cover both epic and story usage of the same
script.
