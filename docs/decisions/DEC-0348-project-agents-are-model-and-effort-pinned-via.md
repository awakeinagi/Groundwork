---
id: DEC-0348
type: decision
title: "Project agents are model- and effort-pinned via frontmatter alone; explicit spawn-time model params are no longer mandated"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0063 @ T13"
overview: >-
  Empirical verification (24 probe spawns across 8 arms, SES-0063,
  2026-07-10) refutes the shared premise of DEC-0292 and DEC-0329
  that a frontmatter model pin alone doesn't take effect.
  Frontmatter model and effort both take effect on their own;
  frontmatter effort survives explicit spawn-time model overrides,
  same-family and cross-family; effort is a documented agent
  frontmatter field but the Agent tool has no per-spawn effort
  parameter, so frontmatter is the only carrier; the historical
  "doesn't take effect" observations were caused by startup
  definition caching (DEC-0347). Therefore project agents are pinned
  via frontmatter alone; callers no longer pass a matching explicit
  model param, reserving explicit overrides for deliberate one-off
  deviations that change the model but never the effort. This
  corrects the explicit-override mandate clauses of DEC-0292 and
  DEC-0329 via relates-to cross-reference, not full supersession,
  since both decisions carry surviving content (the agents'
  existence, consultation moments, and model-tier choices) this
  finding does not disturb.
links:
  derives-from: [SES-0063]
  relates-to: [DEC-0292, DEC-0329, DEC-0347, DEC-0291, DEC-0419, DEC-0418]
cites: [DEC-0292, DEC-0329, DEC-0347]
---

# DEC-0348: Project Agents Are Model- and Effort-Pinned via Frontmatter Alone; Explicit Spawn-Time Model Params Are No Longer Mandated

## Context

DEC-0292 (system-architect) and DEC-0329 (artifact-librarian) both
mandate pinning a project agent's model in its frontmatter AND passing
that model explicitly at every spawn, on the shared premise that "the
frontmatter pin alone has been observed not to take effect." SES-0062
first cast doubt on this premise with three live diagnostic spawns;
SES-0063 was opened (via IDEA-0023) to verify it at a larger sample.
Twenty-four probe spawns across eight arms (T4, T6, T10) now settle
the question, and the caching behavior recorded in DEC-0347 explains
why the earlier premise looked true.

## Decision

Empirical verification (24 probe spawns across 8 arms, SES-0063,
2026-07-10) refutes the shared premise of DEC-0292 and DEC-0329.
Findings:

1. Frontmatter `model:` and `effort:` both take effect on their own.
   A frontmatter `effort: low` agent (effort-probe-sonnet-low) ran at
   ~10/100 (arm G) even under a session-wide effort of high.
2. Frontmatter effort survives explicit spawn-time model overrides,
   both same-family (sonnet→sonnet, arm H: still ~10/100) and
   cross-family (sonnet→opus, arm J: still ~15/100).
3. `effort` is a documented agent frontmatter field
   (low/medium/high/xhigh/max per official Claude Code docs, T4), and
   the Agent tool has no per-spawn effort parameter at all — frontmatter
   is the only carrier of effort into a spawned agent.
4. The historical "frontmatter pin alone doesn't take effect"
   observations were caused by definition caching at Claude Code
   startup (DEC-0347), not a genuine failure of the frontmatter
   mechanism.

Therefore: project agents (system-architect, artifact-librarian,
overview-writer, and any future agents) are pinned via frontmatter
alone. Callers no longer pass a matching explicit `model` param at
spawn time to enforce the pin — frontmatter already carries it, and
reliably. Explicit spawn-time model params are reserved for deliberate
one-off deviations from an agent's normal pin, with the caveat that
they change only the model, never the effort (per finding 3, there is
no way to pass effort explicitly through the Agent tool).

This corrects the explicit-override mandate clauses of DEC-0292 and
DEC-0329 specifically. It does not touch the rest of either decision:
DEC-0292's charter of the system-architect agent (its two consultation
moments, its required-at-EP/ST/CMP placement, and its strongest-
available-model tier choice) and DEC-0329's charter of the
artifact-librarian (its Sonnet-class tier choice and rationale) stand
unchanged. Because both decisions carry this surviving, still-correct
content, this is recorded as a new decision cross-referenced via
`relates-to` rather than a full `supersede` of either — a full
supersession would incorrectly imply the agents' existence, gates, and
tier choices are also being redecided.

## Rationale

A 24-spawn, 8-arm sample is a large enough base to trust over the
3-spawn sample that originally motivated DEC-0292/DEC-0329's
explicit-override practice. The mechanism is now understood
end-to-end (frontmatter caching at startup, not an override
requirement) rather than inferred from a spawn or two, and the same
mechanism cleanly explains why the mandated override was believed
necessary: engineers testing frontmatter-only spawns mid-session, after
just editing the frontmatter, were still seeing stale cached behavior
and concluded the mechanism itself was broken.

## Alternatives Considered

- **Keep the explicit param as belt-and-suspenders** — rejected as
  redundant when it matches the frontmatter pin, and actively harmful
  when it doesn't: an explicit model param that drifts from the
  frontmatter silently changes which model runs, with no error, and
  per finding 3 it can never carry effort regardless.
- **Route high-effort needs through Workflow's `agent()`** — considered
  as an alternative fix in IDEA-0023's original framing; not needed
  now that frontmatter effort is confirmed to survive spawn-time model
  overrides on its own (findings 1-2).
- **Full supersession of DEC-0292 and DEC-0329** — rejected as
  disproportionate; both decisions carry substantial surviving content
  (the agents' existence, consultation moments, gate placement, and
  model-tier choices) that this finding does not disturb. A relates-to
  cross-reference plus a consistency sweep is the narrower, sanctioned
  correction (precedent: DEC-0346 narrowing DEC-0338 the same way).

## Implications

DEC-0292 and DEC-0329 receive a `relates-to` enrichment link to this
decision (DEC-0348), DEC-0347, and DEC-0349, per the sanctioned
accepted-decision enrichment path (DEC-0248); their bodies are not
edited. A consistency `sweep`/`terms` check is run over all three new
DEC IDs as part of this same session to surface any other stale
references to the explicit-override mandate. IDEA-0023, which
originated this investigation, is updated to `taken-up` with its
headline finding recorded as refuted by the larger sample. Any future
agent-invocation practice documentation in this project should cite
DEC-0348 (pinning practice) and DEC-0347 (why the old premise was
wrong), not DEC-0292/DEC-0329's original explicit-override clauses.
