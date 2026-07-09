---
id: ST-0023
type: story
title: Read-only codebase context access under the repo allowlist
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019, ST-0012]
  impacted-by: [ST-0019]
cites: [DEC-0014, DEC-0016, DEC-0049, DEC-0079, DEC-0172]
---

# ST-0023: Read-Only Codebase Context Access

## Summary

The agent's window onto existing code, governed: browse and search
across exactly the repositories `governance/repos.yaml` allows, path
excludes enforced, tokens scoped read-only, and every code-influenced
decision citing repo + ref.

## Acceptance Criteria

1. Browse/search operations return content only from repositories
   listed in `governance/repos.yaml`; a repository absent from the
   allowlist is indistinguishable from one that doesn't exist
   (per DEC-0049).
2. Per-repository path excludes are enforced on every operation —
   excluded paths never appear in listings, search results, or file
   reads (per DEC-0049).
3. Connector tokens used for context reads are read-only and scoped to
   the allowlisted repositories
   (per DEC-0049).
4. A published repo+ref citation format lets Decisions influenced by
   code reads record exactly what was read; the session agent's context
   feed surfaces it with every read result
   (per DEC-0049,
   DEC-0016).
5. No write operation to any codebase is expressible through the
   context-access surface (per DEC-0014).
6. The allowlist and path-exclude enforcement suite passes hermetically
   against the local-git fake connector
   (per DEC-0079).

## Component Impact

CMP-0005 —
supplies the read-operation and allowlist-filter contract sections;
CMP-0009 — the GitHub
(v1) implementation of both, per
DEC-0172;
CMP-0006 —
the deferred Bitbucket Data Center implementation.

## Out of Scope

What the agent does with the context — retrieval, prompting, overlap
detection (EP-0002);
the `repos.yaml` schema, owned by
ST-0012; the work-management
backlog read feed
(ST-0027, deferred).
