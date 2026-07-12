# Groundwork Mode Parity Matrix

Maintained per DEC-0433: skill-mode is the paradigm's core subset; the
Application is a superset. Anything achievable in skill-mode is achievable
in the Application with the same corpus outcome. Reviewed at releases.

| Capability | Skill-mode (solo) | Skill-mode (team) | Application |
|---|---|---|---|
| Artifact CRUD, gates, provenance (Groundwork Engine) | yes | yes | yes |
| Integrity checker | yes (pre-commit) | yes (pre-commit + CI on PRs) | yes (pre-commit + CI on PRs) |
| Session facilitation | agent, terminal | agent, terminal | app UI (DEC-0432: same process knowledge) |
| Approval record (frontmatter, DEC-0428/0435) | yes | yes | yes |
| Approval enforcement | agent discipline + checker | branch protection / CI (DEC-0429) | projected branch protection (DEC-0429) |
| ID allocation (DEC-0430) | file-sequential | reservation ref (first push wins) | app instance counter |
| Collaboration protocol | direct to main | branch-per-session + PR (DEC-0427) | branch-per-session + PR, app-managed |
| Governance config (DEC-0263/0436/0440) | yes (solo defaults) | yes | yes (+ host identity mapping UI) |
| Semantic + graph search | yes (gw / serve_docs) | yes | yes (derived projections, DEC-0424) |
| Team dashboards, cross-project views, notifications | — | — | app-only (additive; no corpus semantics) |
| Multi-user auth / roles UI | — | host-native | app-only |
