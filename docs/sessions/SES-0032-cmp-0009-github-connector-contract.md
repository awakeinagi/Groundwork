---
id: SES-0032
type: session
title: CMP-0009 GitHub Connector — contract refinement
status: closed
owner: eng-lead
created: 2026-07-08
overview: >-
  Refined CMP-0009 from stub to contract-complete after SES-0031
  established GitHub as v1 host. Grilled GitHub-specific implementation
  questions across four dependency-ordered clusters: credential
  separation (two Apps), wire-protocol conventions (REST primary,
  403-disambiguation), capability surface (team_sync introspection,
  review_dismissal), and element decomposition (single connector).
  Drafted contract with all eleven operation families. Found three
  approved artifacts still naming BBDC as implementation; corrected to
  name GitHub v1 alongside deferred BBDC. Produced DEC-0174-DEC-0177.
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Sonnet 5)
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0009, ST-0031, CMP-0005]
---

# SES-0032: CMP-0009 GitHub Connector — Contract Refinement

## Purpose

CMP-0009 was a stub
(Purpose only) after SES-0031
took the v1 host slot from Bitbucket Data Center. This session settles
the GitHub-specific implementation questions
CMP-0005's
protocol deliberately leaves to each adapter — credential
architecture, wire-protocol conventions, capability determination, and
element decomposition — so the contract can be drafted to
contract-complete. Already settled and not re-litigated: the protocol
itself (CMP-0005,
approved), GitHub as v1 host
(DEC-0172),
check-run-based check administration
(DEC-0173),
and ST-0031's acceptance
criteria.

## Transcript

**T1 — Facilitator.** Read CMP-0009,
ST-0031,
CMP-0005 in
full, and the sibling stub CMP-0006
plus the decisions CMP-0005
rests on (DEC-0043,
DEC-0045,
DEC-0049,
DEC-0141,
DEC-0142,
DEC-0145,
DEC-0153,
DEC-0167
through
DEC-0173).
Identified four dependency-ordered
question clusters: identity/credentials, wire-protocol conventions,
capability/administration surface, and element decomposition.

**T2 — Facilitator.** Round 1, four questions, each with a
recommendation: (1) credential separation for
CMP-0005's
`C-2` — recommending two GitHub Apps (Orchestrator, Reader) over one
App with two installations or code-enforced separation; (2) where
`provision_fork` forks land — recommending a dedicated service-owned
account over direct branches on the source repo; (3) the program-user
review identity for DEC-0043 —
recommending the Orchestrator App's own bot identity over a dedicated
machine-user account per role; (4) REST vs. GraphQL — recommending
REST primary with GraphQL for gaps (CODEOWNERS-derived reviewer
resolution, bulk team queries) over GraphQL primary.

**T3 — Product Owner.** Accepted all four recommendations as given.

**T4 — Facilitator.** Round 2, four questions: (1) how
`team_sync`'s capability flag gets set given GitHub's org-level
permission requirement — recommending runtime introspection over a
fixed-true, install-time-required contract; (2) GitHub's overloaded
`403` (permission-denied vs. secondary rate limiting) — recommending
header-based disambiguation (`X-RateLimit-Remaining: 0` /
`Retry-After` ⇒ `rate-limited`, else `permission-denied`) over always
mapping `403` to `permission-denied`; (3) idempotency mechanics for
creation operations given GitHub's lack of general idempotency-key
support — recommending check-before-create over create-then-catch-409;
(4) webhook signing-secret scope — recommending a per-installation
secret in the encrypted secret store over a single global secret.

**T5 — Product Owner.** Accepted all four recommendations as given.

**T6 — Facilitator.** Round 3, three questions: (1) Design Elements
decomposition — recommending a single `GitHubConnector` service
element, webhook translation folded in as an internal concern, over
splitting out a separate `GitHubEventTranslator` element; (2) which of
GitHub's two branch-protection systems backs `A-7` — recommending
classic per-branch branch protection over the newer repository
rulesets model; (3) whether `review_dismissal` is declared `true` for
v1 — recommending yes, since the API is stable and
DEC-0141's
recompute flows can use it.

**T7 — Product Owner.** Accepted all three recommendations as given.

**T8 — Facilitator.** Read back the eleven confirmed answers in plain
language, grouped into four decisions: identity architecture (two
Apps, dedicated fork account, bot-identity program reviews),
wire-protocol conventions (REST-primary, 403 disambiguation,
check-before-create idempotency), capability/administration surface
(`team_sync` introspection, `review_dismissal: true`, classic branch
protection, per-installation webhook secrets), and element
decomposition (single `GitHubConnector`, no graduation). Confirmed no
further amendments before recording.

**T9 — Product Owner.** Confirmed the read-back matched.

**T10 — Facilitator.** Drafted CMP-0009
to contract-complete: a single `GitHubConnector` service element
mapping every `CodeHostConnector` operation family onto concrete
GitHub REST/GraphQL endpoints, Component Invariants, Implementation
Guidance, Dependencies, Acceptance & Test Expectations, and Out of
Scope. Ran `groundwork_consistency.py sweep`/`terms` on
DEC-0174–DEC-0177
and, while reviewing the hits, found three approved artifacts still
naming CMP-0006/ST-0020
as *the* implementation of protocol operations GitHub now actually
implements for v1 — staleness gaps SES-0031's
sweep missed because their citations of the superseded
DEC-0050 were
indirect (via ST-0019/ST-0021/ST-0023's
own prose, not their frontmatter `cites`):
ST-0019's Out of
Scope named only the BBDC implementation;
ST-0021's
Out of Scope named only ST-0020
for "the host review API plumbing";
ST-0023's Component
Impact named only CMP-0006
as "the BBDC implementation" of the read-operation/allowlist sections.
Corrected all three to name the GitHub v1 implementation
(ST-0031/CMP-0009)
alongside the deferred Bitbucket Data Center one, rather than dropping
the BBDC reference. CMP-0009
set to `gated`, pending decision-recall audit and the Product Owner's
approval; the three story diffs are re-affirmations, presented
alongside the gate.

**T12 — Facilitator.** Ran the decision-recall audit
(`groundwork_search.py audit`, against
CMP-0009) and spawned a
Sonnet 5 judge fork over its 15 candidates. Verdict: nothing to add —
every candidate was either fully superseded and already carried
through a cited decision
(DEC-0166
by DEC-0173,
DEC-0050 by
DEC-0172), another
component's own citation obligation
(CMP-0005/CMP-0004/CMP-0001
decomposition decisions), meta/process decisions about the audit
tooling itself, or scoped to an unrelated component. Closest
near-miss, DEC-0036
(host branch protection + service `gate-policy` check), judged not
missing — CMP-0009's
role there is purely mechanical execution, already carried through its
citation of DEC-0142
and its `depends-on: [CMP-0005]`. The judge separately flagged a real
contract gap outside the candidate list: `A-11`'s local webhook
registration state (`(repo, event_types, callback_url)` filter tuples)
had no stated persistence story across a connector restart. Addressed
by adding `IG-8` (callers re-register on process start, idempotent;
any gap is bounded by
DEC-0145's
reconciliation sweep) and Acceptance & Test Expectations item 9 — no
new decision needed, since the resolution follows directly from
already-accepted DEC-0145
and DEC-0167.

**T13 — Product Owner.** Reviewed the gate summary — the
CMP-0009 contract plus
the bundled ST-0019/ST-0021/ST-0023
re-affirmation diffs — and approved.

**T14 — Facilitator.** Set CMP-0009
to `approved` (`approved-by: awakeinagi@gmail.com`, `approved-on:
2026-07-08`).
ST-0019,
ST-0021, and
ST-0023 remain
`approved` with their diffs re-affirmed — no re-gate needed, since
none of their contract shapes changed, only which adapter they name.

## Decisions Produced

- DEC-0174 —
  two GitHub Apps, dedicated fork account, bot-identity program
  reviews.
- DEC-0175 —
  REST-primary/GraphQL-for-gaps, 403 disambiguation, check-before-create
  idempotency.
- DEC-0176 —
  `team_sync` introspection, `review_dismissal: true`, classic branch
  protection, per-installation webhook secrets.
- DEC-0177 —
  single `GitHubConnector` service element, no graduation.

## Conflicts Raised

None.
