---
id: ST-0023
type: story
title: Read-only codebase context access under the repo allowlist
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019, ST-0012]
  impacted-by: [ST-0019]
cites: [DEC-0014, DEC-0016, DEC-0049, DEC-0079]
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
   (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
2. Per-repository path excludes are enforced on every operation —
   excluded paths never appear in listings, search results, or file
   reads (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
3. Connector tokens used for context reads are read-only and scoped to
   the allowlisted repositories
   (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
4. A published repo+ref citation format lets Decisions influenced by
   code reads record exactly what was read; the session agent's context
   feed surfaces it with every read result
   (per [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md),
   [DEC-0016](../decisions/DEC-0016-agent-context-feeds.md)).
5. No write operation to any codebase is expressible through the
   context-access surface (per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).
6. The allowlist and path-exclude enforcement suite passes hermetically
   against the local-git fake connector
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).

## Component Impact

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md) —
supplies the read-operation and allowlist-filter contract sections;
[CMP-0006](../components/CMP-0006-bitbucket-data-center-connector.md) —
the BBDC implementation of both.

## Out of Scope

What the agent does with the context — retrieval, prompting, overlap
detection ([EP-0002](../epics/EP-0002-refinement-session-agent.md));
the `repos.yaml` schema, owned by
[ST-0012](ST-0012-governance-config-schemas.md); the work-management
backlog read feed
([ST-0027](ST-0027-work-management-backlog-read-feed.md), deferred).
