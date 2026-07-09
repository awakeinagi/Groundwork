---
id: DEC-0249
type: decision
title: The impactor's body must explain each of its impacts edges
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T8-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0026, DEC-0248]
---

# DEC-0249: Impactor-Side Impact Prose Is Blocking

## Context

Impact edges (`impacts`/`impacted-by`, directional per DEC-0026) are
reciprocity-checked in frontmatter but nothing required prose: the
sweep found 8 epic-side and 30 story-side impact edges whose impactor
never mentions the impactee in its body. An impact edge with no
explanation forces readers back through session archaeology to learn
*how* one item shapes another. The stakeholder: "having a proper
explanation of how one system item impacts another is vital."

## Decision

Any epic, story, or component carrying an `impacts` edge must
reference each impact target by bare ID in its body prose — the
impactor explains how it shapes the impactee. This is a blocking rule
in `check_links.py` (both copies). The impactee side carries no prose
obligation. Frontmatter edge reciprocity (both nodes recording the
pair) remains blocking under the existing rule 6; a known
impactor→impactee relationship with a missing or one-sided edge pair
is a violation at either node.

## Rationale

The impactor is where the causal knowledge lives — its refinement
produced the constraint — so that is where the explanation belongs.
The impactee side stays silent because obligating both sides would
duplicate every explanation and generate boilerplate. Mechanical
scope is honest: the checker verifies the mention exists; whether the
explanation is *proper* remains a gate-review concern.

## Alternatives Considered

- **Warning for epics, silent for stories** (facilitator's
  recommendation, rejected by the stakeholder): treats a 64–71%
  convention as too weak to block on — but the stakeholder judged the
  missing 36% a real comprehension gap, not tolerable variance.
- **Blocking both sides**: symmetric but redundant; every explanation
  would exist twice and drift.

## Implications

~38 prose explanations (30 story-side, 8 epic-side) are written in
the adopting session, each grounded in the sessions and decisions
that drew the edge, added under DEC-0248's sanction. Future impact
edges require accompanying prose at derivation time; the derivation
playbooks say so.
