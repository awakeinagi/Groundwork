---
id: DEC-0137
type: decision
title: A decision-recall audit is a required refinement-stage step — retrieval plus a strict judge subagent
status: superseded
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  After drafting or amending any artifact and at gate preparation, facilitator
  runs decision-recall audit: retrieval ranks accepted decisions relevant to
  artifact but absent from considered set (top-15 by rank); subagent judges
  candidates strictly (at most 4 findings or exactly "Nothing to add");
  findings addressed before gating. Catches content-relevant misses (~60% per
  stage at k=15); complements DEC-0136 checklists for rule-type decisions.
  Topology: Sonnet-class agents for >15 lists, Opus otherwise; comparative
  judgment within batch prevents acquiescence bias. Superseded.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0024 @ T1-T5"
links:
  derives-from: [SES-0024]
  relates-to: [DEC-0136, DEC-0111, DEC-0119]
---

# DEC-0137: The Decision-Recall Audit Step

## Context

SES-0023 showed a
relevant decision can go unapplied; its complement — a relevant
decision absent from context entirely — had no systematic catch. The
participant proposed an exploratory-subagent audit at each stage,
refined through a POC
(SES-0024).

## Decision

After drafting or materially amending any artifact, and again at gate
preparation, the facilitator runs a **decision-recall audit**:

1. **Retrieval** — the search tool's `audit` command ranks accepted
   decisions relevant to the artifact but absent from its considered
   set (frontmatter cites + inline references, superseded-redirected;
   top-15 by rank; absolute score thresholds are forbidden — static
   embeddings compress the range).
2. **Judgment** — a subagent judges the candidates strictly and reports
   at most 4 findings or exactly "Nothing to add" plus the closest
   near-miss; contract gaps noticed en route are reported separately.
   Topology: one **Opus-class** judge for lists ≤15 (a fork when the
   facilitator runs an Opus-class model — forks inherit the parent
   model — otherwise a fresh Opus agent fed the packet); lists >15
   shard into batches of ~8 on **Sonnet-class** agents. **One
   candidate per agent is forbidden**: isolated relevance judges
   over-flag (acquiescence bias); comparative judgment within a batch
   is what makes reports trustworthy.
3. **Disposition** — findings are addressed in the session before
   gating; "Nothing to add" is a valid outcome recorded in the session.

The audit catches *content-relevant* misses only (POC-measured ~60%
per stage at k=15, compounding across stages). Rule-type decisions
that govern structure do not surface — POC replay showed
DEC-0080 scrubbed from
CMP-0001 ranks
nowhere — so this step complements, never replaces, the
DEC-0136 checklists.

## Rationale

POC evidence end to end: retrieval is ~2 s and local; the demo judge
returned a correct "Nothing to add" with a defensible near-miss
analysis and surfaced a real contract gap as a side effect. The
topology follows from the demo: strictness came from seeing the whole
list; parallel per-candidate judges add cost and false flags while
saving no meaningful latency.

## Alternatives Considered

- **Per-candidate parallel agents (24×1), cheap models** — maximum
  isolation; rejected for acquiescence bias and re-adjudication burden.
- **Cascade always (cheap prune → strong final)** — most
  token-efficient at large k; kept as an available variant, not the
  default, since single-judge handles today's list sizes.
- **No audit; rely on facilitator recall** — the status quo the
  SES-0023
  lesson argues against.

## Implications

The skill's playbook, SKILL.md, and semantic-search reference carry the
step (synced to vendored and installed copies). When
EP-0002 (Refinement
Session Agent) derives stories, the audit capability must be considered
for the product's session agent — this decision is design input there.
