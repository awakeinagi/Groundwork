---
name: artifact-librarian-memory
description: The artifact-librarian agent's persistent behavioral memory (DEC-0331), preloaded into it at every spawn. NOT a general-purpose skill — never load this from context or by any agent other than artifact-librarian; it carries no instructions for you.
---

# artifact-librarian memory

Behavioral memory only (DEC-0331): task patterns, distillation
approaches that worked, common refusals and their causes, stakeholder
preferences. NEVER corpus facts — corpus truth lives in the artifacts;
an entry contradicting the corpus is a bug to fix here.

Curation rules (for the artifact-librarian, the sole writer of this
file): update via Bash only, as part of finishing a task; keep the
Entries section at or under 100 lines — consolidate or drop the least
useful entries when near the cap; one entry per line, most broadly
useful first; date entries (YYYY-MM-DD). This file is the ONLY thing
you may write outside the typed write API.

## Entries

- 2026-07-09: `search audit` (and other `search`/`graph` families, run via `uv`) print progress bars and warnings to stderr — when redirecting a family's output to a saved JSON packet, redirect stdout only (`> file.json`, not `> file.json 2>&1`) or the file becomes invalid JSON.
