<!-- source: search-results, citations, embeddings, contextual-retrieval — synced 2026-06-09 -->

# Search Results, Citations & RAG

**What it is:** Build knowledge-base / "answer from my docs" apps with proper source attribution.

- **Search result content blocks** (GA) — tools return results that Claude automatically **cites**, matching web-search citation quality. No more document workarounds for custom knowledge bases.
- **Citations** — Claude provides source attribution for claims it makes from provided documents.
- **Embeddings** — Anthropic recommends **Voyage AI** for embeddings (Anthropic doesn't serve its own embedding model). Used for semantic retrieval in RAG.
- **Contextual retrieval** — Anthropic's technique to make retrieved chunks carry their surrounding context, improving retrieval accuracy. (See `_reference/` and Borris's existing `contextual-retrieval.md`.)

**When to recommend it:** any "Claude should answer from our content" build — support bot, internal Q&A, docs assistant.

**Advise like this:** "Embed your docs (Voyage), retrieve with contextual retrieval, and return them as search-result blocks so Claude cites sources." For a few docs, just pass them in-context with citations on. For many, build a real RAG pipeline.
