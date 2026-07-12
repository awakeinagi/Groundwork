---
id: DEC-0390
type: decision
title: "The gw-read skill may self-trigger; the non-self-triggering mandate protects the write-bearing surface"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T9, T12"
overview: >-
  The DEC-0326 non-self-triggering rule is motivated by the mutation
  surface and continues to protect the artifact-interact skill
  unchanged. The read-only gw-read skill introduced by DEC-0389 may
  load freely from conversational context, since nothing it exposes
  can mutate the corpus. This narrows DEC-0326's motivation without
  superseding it. Decided at SES-0076.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0326, DEC-0388, DEC-0389]
---

# DEC-0390: The gw-read skill may self-trigger; the non-self-triggering mandate protects the write-bearing surface

The DEC-0326 non-self-triggering rule is motivated by the mutation surface and continues to protect the artifact-interact skill unchanged. The read-only `gw-read` skill may load freely from conversational context, since nothing it exposes can mutate the corpus. This narrows DEC-0326's motivation without superseding it.
