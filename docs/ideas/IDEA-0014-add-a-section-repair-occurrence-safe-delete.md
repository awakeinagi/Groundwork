---
id: IDEA-0014
type: idea
title: "Add a section-repair / occurrence-safe delete operation to the write API"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  The write API's edit-section operation matches the FIRST heading
  with the given text and replaces up to the NEXT heading — it
  cannot target a specific occurrence among duplicates, and no
  operation exists to delete a stray/duplicate heading line.
  Surfaced during SES-0060 when a facilitator drafting error
  produced a duplicate '## Conflicts & Tensions' heading in
  BG-0002.md that the write API could not repair; fixed via a
  stakeholder-authorized one-off manual exception outside the sole-
  sanctioned-write-path rule. A future session should design either
  an occurrence-index parameter for edit-section, or a dedicated
  section-repair/delete operation, so this class of defect never
  again requires bypassing DEC-0312.
links:
  derives-from: [SES-0060]
---

## The Idea

The write API's edit-section operation matches the FIRST heading with
the given text and replaces up to the NEXT heading — it cannot target
a specific occurrence among duplicates, and no operation exists to
delete a stray/duplicate heading line. Add a section-repair /
occurrence-safe delete operation to the write API.

## Spark Context

Surfaced during SES-0060 when a facilitator drafting error produced a
duplicate "## Conflicts & Tensions" heading in BG-0002.md that the
write API could not repair; fixed via a stakeholder-authorized one-off
manual exception outside the sole-sanctioned-write-path rule set by
DEC-0312. A future session should design either an occurrence-index
parameter for edit-section, or a dedicated section-repair/delete
operation, so this class of defect never again requires bypassing
DEC-0312.

## Disposition

Pending.
