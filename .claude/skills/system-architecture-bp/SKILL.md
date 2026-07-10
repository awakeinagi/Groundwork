---
name: system-architecture-bp
description: Knowledge corpus for the Groundwork system-architect agent (DEC-0294) — curated, cited software/system architecture and design best practices plus vendored open texts (arc42 CC-BY-SA 4.0, awesome-software-architecture CC0). Load when advising on architecture styles, system/service/component decomposition and seams, interface and contract design, quality attributes and trade-offs, architecture evaluation and review, or documentation practices (arc42, C4, ADRs). Constructed per DEC-0295; content changes only via that pipeline and stakeholder ratification.
---

# System Architecture Best Practices (corpus)

This skill is the preloaded knowledge of the `system-architect`
project agent (DEC-0292..DEC-0296 of the Groundwork
project-documentation-system corpus). It is a **reference corpus, not
a workflow** — read the reference that matches the consultation topic
and cite it in your analysis.

Corpus constructed: 2026-07-09 (DEC-0295 pipeline). Refresh is
on-demand only; if consultations visibly miss current practice, raise
it — a re-run enters via change intake.

## Reading order

1. [references/INDEX.md](references/INDEX.md) — map of the curated
   reference docs by topic, with the source scorecard (what was
   explored, scores, what made the cut and what is appendix-only).
2. The topical reference docs under `references/` — original, cited
   distillations (each claim traceable to its source URL).
3. Vendored primary texts under `vendored/`:
   - `vendored/arc42/arc42-template-EN.md` — the arc42 architecture
     documentation template with guidance (CC-BY-SA 4.0; see
     `vendored/NOTICE.md` for obligations).
   - `vendored/awesome-software-architecture/` — CC0 curated indexes
     of the wider literature; use as pointers, not as content.

## Rules

- Cite the reference (and its underlying source URL) behind every
  substantive recommendation; where you advise beyond the corpus, say
  so explicitly.
- Copyrighted canon (ISO/IEC/IEEE 42010/42020/42030, books) is cited
  as pointers only — never reproduce it here.
- `vendored/NOTICE.md` travels with any copy of the vendored texts;
  adaptations of arc42 material must remain CC-BY-SA 4.0.
