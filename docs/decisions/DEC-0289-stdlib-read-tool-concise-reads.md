---
id: DEC-0289
type: decision
title: A stdlib read tool owns ID-addressed concise reads with eight affordances
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T6-T9"
overview: >-
  A new stdlib-only skill script, groundwork_read.py, owns all
  ID-addressed concise reads with eight v1 subcommands: batch overview
  (by IDs or type/status filter), outline (headings + CMP element
  inventory), section (one body section), element (one CMP design
  element's block), item (one contract item by scoped ID), turns (a
  session turn span), term (one CONTEXT.md glossary entry), and citers
  (artifacts referencing an ID, index-free). Division of labor: search
  answers "what's relevant", the graph answers "how is it connected",
  the read tool answers "what does it say, cheaply". AGENTS.md gains the
  overview-first reading discipline.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0284, DEC-0286, DEC-0081]
---

# DEC-0289: A Stdlib Read Tool Owns Concise Reads

## Context

The overview field (DEC-0284) needs a consumption surface, and common
small-information needs — one acceptance-criteria list, one contract
item, one turn span, one glossary term — today cost whole-file reads.
Existing tools have adjacent jobs: semantic search finds what's
relevant; the graph tool answers structure. Neither should carry
plain ID-addressed reads, which must work with no index, no uv, no
dependencies.

## Decision

A new **stdlib-only** skill script, `groundwork_read.py`, owns all
ID-addressed concise reads. V1 subcommands:

1. `overview <ID>... | --type T --status S` — batch overviews for
   explicit IDs or filtered sets; the core triage primitive.
2. `outline <ID>` — headings, plus for CMPs the element inventory
   with types and `Implements:` lines; the middle disclosure layer.
3. `section <ID> <heading>` — one body section.
4. `element <CMP-ID> <name>` — one design element's heading,
   Implements line, and contract block.
5. `item <CMP-ID> <item-ID>` — one contract item (e.g.
   `StorageService.B-3`, `C-2`, `IG-1`).
6. `turns <SES-ID> <T-span>` — a session turn span (serves
   source-span verification).
7. `term <name>` — one CONTEXT.md glossary entry.
8. `citers <ID>` — artifacts whose cites/links/body reference the ID,
   grep-cheap and index-free.

AGENTS.md (project and skill asset) directs agents to read overviews
(and outlines) before opening bodies, and to prefer the read tool for
these needs over whole-file reads.

## Rationale

One script with a clean charter beats bolting reads onto tools that
need an index (search) or a managed venv (graph): the cheap path must
be the most dependency-free path. The eight affordances map to the
observed read patterns of real sessions: triage, orientation,
citation verification, contract lookup, glossary discipline.
`citers` duplicates a graph capability deliberately — index-free
coverage for the most common provenance question.

## Alternatives Considered

- **Extend search/graph instead of a new script** — fewer scripts;
  rejected: makes cheap reads depend on heavy tools (that enrichment
  happens *additionally*, DEC-0290).
- **Fewer affordances (drop citers/term)** — rejected by the
  stakeholder; full set selected.

## Implications

The skill gains the script (synced to the vendored copy); SKILL.md
and both AGENTS.md files document the overview-first discipline and
the tool's charter. Session outlines depend only on standard heading
structure; `item` and `element` depend on the CMP element heading
convention already enforced by the checker.
