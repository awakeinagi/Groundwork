# Specification: Bundled Scripts

> **Home note (DEC-0310).** This spec lives with the `artifact-interact`
> skill: all artifact tooling scripts moved out of the
> `groundwork-design-session` skill into
> `.claude/skills/artifact-interact/scripts/`, and this document moved
> with them.

Language-agnostic behavioral specification for two of the executable
tools bundled with the `artifact-interact` skill
(`.claude/skills/artifact-interact/scripts/check_links.py` and
`.claude/skills/artifact-interact/scripts/status_report.py`; both also
reachable as the `check` and `status` families of the unified `gw.py`
CLI). An agent with no other
context should be able to reimplement both from this document alone, in
any language. The reference implementations happen to be Python 3 with a
YAML-parsing library as the only third-party dependency, but nothing below
requires that.

Read the `groundwork-design-session` skill's
`references/groundwork-system.md` for the artifact model
these tools operate on; this spec restates the parts they depend on so it
stands alone.

---

## Shared foundations (both scripts)

### Invocation

- Each script is a standalone command-line program taking one optional
  positional argument: the **project root** directory. Default: the
  current working directory.
- Output is plain text to stdout, designed to be read by both humans and
  agents. No flags are required for normal operation.
- Exit codes: `0` = success, `1` = validation failure (checker only),
  `2` = setup problem (missing dependency, wrong directory, no `docs/`
  tree where one is required).
- If the YAML-parsing dependency is unavailable, print a one-line
  instruction for installing it and exit `2` — never crash with a raw
  import traceback.

### Artifact discovery

- Artifacts are Markdown files (`*.md`) found by recursive search under
  `<project-root>/docs/`.
- Skip any file whose immediate parent directory is named `specs`
  (projects may keep format-specification documents under `docs/specs/`;
  those are documentation, not artifacts).
- Sort discovered paths for deterministic output ordering.

### Artifact parsing

- An artifact begins with a YAML frontmatter block: the file's very first
  characters are `---` followed by a newline, then YAML content, then a
  line consisting of `---`. Everything after is the body (ignored by both
  scripts).
- Parse the YAML into a mapping. Three failure cases must be handled
  distinctly and must never abort the whole run:
  - no frontmatter block at all,
  - YAML that fails to parse,
  - YAML that parses to something other than a mapping (e.g. empty).
- Track each parsed artifact's path relative to the project root for use
  in messages.

### The artifact model (fields both scripts read)

- `id`: string of the form `<PREFIX>-<4 digits>` where PREFIX is one of:
  `BG`, `EP`, `ST`, `SP`, `CMP`, `SES`, `DEC`, `CFL`, `CON`, `CP`.
- `type`: one of `business-goal`, `epic`, `story`, `spike`, `component`,
  `session`, `decision`, `conflict`, `consolidation`, `change-proposal` —
  with a fixed one-to-one mapping to the prefixes above (in that order:
  BG, EP, ST, SP, CMP, SES, DEC, CFL, CON, CP).
- `status`: lifecycle string (see each script for which values matter).
- `links`: optional mapping from link-type to a list of artifact IDs. The
  closed link-type vocabulary: `derives-from`, `satisfies`, `depends-on`,
  `conflicts-with`, `supersedes`, `relates-to`, `impacts`, `impacted-by`.
- `cites`: optional top-level list of decision IDs.
- `triage`: on change-proposals only — `pending`, `mechanical`, `session`,
  or `rejected`.
- **Normalization rule**: anywhere a list is expected (`links` values,
  `cites`), a scalar value must be treated as a one-element list and a
  missing/null value as an empty list. Authors hand-write this YAML;
  tolerate the scalar shorthand.

---

## Script 1: `check_links.py` — graph integrity checker

### Purpose

The gatekeeper of the artifact graph. It validates every structural
invariant the Groundwork method depends on, so that "the checker passes"
is a sufficient condition for the graph being sound. The method requires
running it **before every commit**; it is also installed into each
bootstrapped project as `tools/check_links.py`, so it must be fully
self-contained (no imports from the skill).

### Setup behavior

If `<project-root>/docs/` does not exist, print a message saying this is
not a Groundwork project (or the wrong root) and exit `2`.

### Registration pass (per discovered file)

Each violation appends one human-readable error line (`<relative path>:
<message>`) to a running list; processing always continues so a single run
reports **all** violations, not just the first.

1. Missing frontmatter, unparseable YAML, or non-mapping frontmatter →
   error; skip the file for later passes.
2. `id` missing or not matching the ID pattern → error; skip the file.
3. Filename must begin with the artifact's ID followed by a hyphen
   (`EP-0003-some-slug.md`) → error if not (but still register).
4. Duplicate ID across files → error; the first occurrence stays
   registered, the duplicate is skipped.
5. Unknown `type` (not in the ten-value vocabulary) → error.
6. `type`/prefix mismatch (e.g. `type: epic` with id `ST-0004`) → error.

### Validation rules (over the registered set)

**Rule A — references resolve.** For every artifact, every ID in every
`links` list and in `cites` must be a registered artifact ID. Unknown
link-type keys inside `links` are themselves violations. Report each
unresolved reference with its link type and target.

**Rule B — work traces to a goal.** Every artifact of type `epic`,
`story`, `spike`, or `component` must reach at least one artifact of type
`business-goal` by following `derives-from` and `satisfies` edges upward,
transitively. The traversal must guard against cycles (track visited
nodes). Missing parents simply fail the trace (they were already reported
by Rule A).

**Rule C — decisions have provenance.** Every artifact of type `decision`
must have at least one `derives-from` target whose registered type is
`session` or `spike`.

**Rule D — approvals are conflict-free.** Every artifact with
`status: approved` must not list, under `conflicts-with`, any conflict
artifact whose status is not `resolved`. (A missing target was already
reported by Rule A; this rule only judges resolved-ness.)

**Rule E — impact links are reciprocal and same-type.** For every
artifact X listing Y under `impacts`: Y must be the same `type` as X, and
Y's `impacted-by` list must contain X. Symmetrically for `impacted-by`
against `impacts`. Report the direction and the missing inverse
explicitly. Skip targets that failed to resolve (Rule A covered them).

### Output contract

- All violations: print a first line
  `FAIL: <n> violation(s) across <m> artifacts`, a blank line, then one
  indented line per violation; exit `1`.
- No violations: print `OK: <m> artifacts, graph is sound`; exit `0`.
- The `OK:` / `FAIL:` prefixes are load-bearing — agents and CI grep for
  them. Do not restyle them.

---

## Script 2: `status_report.py` — project state assessment

### Purpose

The design-session facilitator's Step-0 assessment tool (run for it by
the artifact-librarian as a status task): given a project root, produce
a concise census of
the design's state and recommend which operating mode the facilitator
should enter — Mode 1 (bootstrap), Mode 2 (begin the design), or Mode 3
(continue). It must be safe to run on anything: an empty directory, a
non-Groundwork repo, a half-built project, or a large healthy one. It
only reads; it never writes.

### Robustness posture

Unlike the checker, this tool is diagnostic, not judgmental: files that
fail to parse or lack an `id` are silently skipped rather than reported
(the checker is the place for that). It must never crash on malformed
input.

### Inputs examined

1. Whether `<project-root>/docs/` exists.
2. Whether `<project-root>/AGENTS.md` exists **and** contains the
   substring `groundwork` case-insensitively (the "Groundwork marker" —
   evidence the standing instructions are installed).
3. All parseable artifacts under `docs/` (same discovery/parsing/
   normalization rules as the checker).

### Report sections, in order

1. **Header**: the resolved project root; whether the Groundwork
   AGENTS.md marker is present; total artifact count.
   - Special case: if `docs/` is missing entirely, print that fact (and
     the marker status), recommend **Mode 1 (bootstrap), then 2**, and
     exit `0` — nothing else applies.
2. **Census**: one line per artifact `type` present, sorted, showing the
   total for that type and a breakdown by `status` (e.g.
   `epic  7  (approved: 5, gated: 2)`).
3. **Open items** — five fixed rows, each listing matching artifact IDs
   or a dash when empty:
   - *gated (awaiting approval)*: `status: gated`.
   - *stale (awaiting re-affirmation)*: `status: stale`.
   - *draft/in-refinement*: status `draft` or `in-refinement`, excluding
     types `session` and `decision` (their drafts aren't actionable work
     items).
   - *open conflicts (BLOCKING)*: type `conflict` with status other than
     `resolved`.
   - *untriaged change proposals*: type `change-proposal` whose `triage`
     is `pending` or absent.
4. **Frontier**: artifacts that are `approved`, of a type that can have
   derived children (`business-goal` → epics; `epic` → stories/spikes),
   and that currently have **no** children — where a child is any
   registered artifact (excluding types `session` and `decision`) whose
   `derives-from` includes the parent. Print each as
   `<ID> (approved, no <expected-children> derived yet)`; dash if none.
   This is "where derivation work can start next."
5. **Component readiness** (only when components exist): `approved`
   count out of total component docs — the design's doneness measure.
6. **Mode recommendation**, derived as:
   - no artifact of type `business-goal` at all → Mode **2** ("structure
     exists, no business goal yet");
   - business goal(s) exist but none `approved` → Mode **2/3** with the
     instruction to finish goal refinement and gate it;
   - at least one `approved` business goal → Mode **3** (continue).
7. **Next-ID helper**: for every prefix present in the project, the next
   free ID (max existing number + 1, zero-padded to 4 digits), e.g.
   `Next IDs: BG-0002, DEC-0005, EP-0003, SES-0002`. This exists because
   ID collision is a common agent error; allocation must scan, never
   guess.

Always exit `0` when the report was produced (even for empty or messy
projects); `2` only for setup problems (missing dependency).

### Fidelity notes for reimplementers

- The `RECOMMENDED MODE:` line prefix and the `Next IDs:` prefix are
  grepped by agents following the skill; keep them stable.
- Keep the report under ~40 lines for typical projects — it is meant to
  be pasted into an agent's context, not to replace reading artifacts.

---

## Acceptance checks for a reimplementation

A rebuilt pair of scripts should demonstrably:

1. Report `OK` and the correct artifact count on a known-good Groundwork
   project, and exit `0`.
2. Detect each violation class when introduced singly into a fixture:
   dangling link, missing frontmatter, duplicate ID, type/prefix
   mismatch, goal-orphaned epic, decision without session/spike parent,
   approved artifact with an open conflict, one-sided or cross-type
   impact edge — each producing an actionable message naming the file.
3. Report all violations in one run (no fail-fast).
4. Recommend Mode 1 on an empty directory, Mode 2 on a bootstrapped-but-
   goalless project, and Mode 3 on a project with an approved goal.
5. List gated/stale/conflict/frontier items correctly on a mixed-state
   fixture, and compute next IDs as max+1 per prefix across **all** of
   `docs/`, not just one subdirectory.
6. Never modify any file in the project under either script.
