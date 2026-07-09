---
id: SES-0020
type: session
title: Pluggable infrastructure ports — swappable embedding model, vector store, app database, graph store
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0001, EP-0004, EP-0007, DEC-0102, DEC-0067, SP-0002]
---

# SES-0020: Pluggable Infrastructure Ports

## Purpose

The participant raised a new architectural requirement: the design must
be modular so that the embedding model (local or external via REST
APIs), the vector DB, and the app DB are each easily
swappable/pluggable. This session reconciles that requirement with the
accepted embedded v1 stack
(DEC-0102) and the
deferred graduation path
(SP-0002), and
pins where the seams live and how strong "easily swappable" is.

## Transcript

**T1 — awakeinagi.** "Let's make it a requirement for the design to be
modular so that each of the following are easily swappable/pluggable:
embedding model — either a local model or an external model via REST
APIs, etc.; vector DB; app DB."

**T2 — facilitator.** Recapped the settled ground (embedded v1 stack per
DEC-0102; graduation
triggers `TRG-0001`–`TRG-0004`; Protocol elements as capability seams
and Connector as the existing pluggable-adapter concept), noted the
requirement strengthens rather than conflicts with graduation, and asked
four questions, recommendations first: (1) include the Graph Index
engine (LadybugDB) as a fourth swappable seam — it is the engine
SP-0002 most
explicitly targets (recommended) vs. only the three named;
(2) mechanism strength — Protocol-element ports with config-selected
adapters and a shared conformance suite per port (recommended) vs.
clean seams with code-level wiring vs. runtime plugin discovery;
(3) vector store and app database as two separate ports even though one
DuckDB engine backs both in v1 (recommended) vs. one storage port;
(4) scope — the requirement binds the Groundwork product only, skill
tooling stays hard-wired (recommended) vs. product and skill tooling.

**T3 — awakeinagi.** Accepted all four recommendations: graph engine
included (four ports total); ports + config-selected adapters;
two separate ports for vector store and app database; product only.

**T4 — facilitator.** Asked three follow-ups on contract consequences,
recommendations first: (1) terminology — new glossary terms **Port**
(Protocol-typed seam for a swappable infrastructure capability) and
**Adapter** (config-selected implementation of a Port), keeping
Connector reserved for external-system integrations (recommended) vs.
extending Connector; (2) embedder-swap safety — the embedding port must
expose model identity + dimensionality, the vector store stamps them on
the index, and a mismatch refuses to serve stale vectors and requires a
full re-embed (recommended) vs. leaving it to adapter docs;
(3) v1 adapter set — embedded defaults only for storage/graph ports
(second adapters arrive with the
SP-0002
graduation) but two embedding
adapters from day one, local model + REST client, proving the seam the
participant explicitly named (recommended) vs. local-only vs. a second
adapter for every port.

**T5 — awakeinagi.** Accepted all three recommendations: Port + Adapter
as new terms; model-identity stamping with forced rebuild on mismatch;
embedded defaults plus a REST embedding adapter in v1.

**T6 — facilitator.** Played back the five decision points in plain
language: four infrastructure ports as Protocol seams (product only);
config-selected adapters with per-port conformance suites; embedding
identity stamped on the vector index with mismatch forcing re-embed;
v1 ships embedded storage adapters plus local + REST embedding
adapters; Port/Adapter glossary terms. Flagged that
EP-0001,
EP-0004, and
EP-0007 would be
amended and go stale, needing re-affirmation.

**T7 — awakeinagi.** Confirmed all five points for recording.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  the embedding and vector-store ports made swappable here underpin
  the full-text and semantic search that DEC-0067 assigns to the
  retrieval layer.

## Decisions Produced

- DEC-0121 — four
  infrastructure ports (app database, vector store, embedding, graph
  store) as Protocol-element seams; binds the product only
- DEC-0122 —
  adapters are deployment-config-selected; every port carries a
  conformance test suite adapters must pass
- DEC-0123 —
  embedding model identity + dimensionality stamped on the vector
  index; mismatch refuses service and forces a full re-embed
- DEC-0124 — v1 ships the
  embedded adapters per
  DEC-0102 plus two
  embedding adapters (local model and REST client)

## Conflicts Raised

None — the requirement strengthens the accepted graduation path
(DEC-0102,
DEC-0105) rather
than contradicting it.
