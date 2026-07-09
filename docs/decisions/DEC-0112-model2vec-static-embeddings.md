---
id: DEC-0112
type: decision
title: Embeddings come from model2vec static potion-base-8M, not transformer or API models
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T3-T4, T9"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0111]
---

# DEC-0112: Embeddings via model2vec Static potion-base-8M

## Context

The reference blog post uses BGE-M3 via FlagEmbedding — a PyTorch
dependency stack with a ~2.3 GB model — far too heavy for a skill
script run through uv ephemeral venvs. An embedding backend was needed
that keeps the tool as lightweight as the sibling graph script.

## Decision

The search tool embeds with **model2vec static embeddings, model
`minishlab/potion-base-8M`** (256-dim): numpy-only, no PyTorch, ~30 MB
one-time model fetch, fully local afterward.

## Rationale

POC-measured on the real corpus: the full 922-chunk corpus embeds in
0.14 s and cold start is sub-second — fast enough to make
auto-refresh-on-search (DEC-0117)
viable. Static-embedding quality is below transformer models but proved
sufficient in POC retrieval tests; the known paraphrase weakness showed
up only in the rejected trigger-matching capability
(DEC-0120).

## Alternatives Considered

- **BGE-M3 / FlagEmbedding (per the blog)**: best quality, multilingual,
  1024-dim — but PyTorch + 2.3 GB of weights to search ~150 markdown
  files.
- **sentence-transformers all-MiniLM-L6-v2**: middle ground, still pulls
  ~800 MB of torch wheels and a slower cold start.
- **API embeddings (Voyage/OpenAI)**: best quality, but requires a key
  and network — breaks the fully-local property every other skill tool
  has.

## Implications

Embedding dimension (256) is read from the model at runtime, not
hard-coded. A model swap means a full re-index — cheap at current scale;
at graduated scale this is one of
SP-0002's existing
evaluation points.
