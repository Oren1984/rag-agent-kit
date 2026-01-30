# Configuration

## Core
- `RAG_API_KEY` (required)

## LLM
- `LLM_PROVIDER` = openai|gemini|anthropic
- OpenAI:
  - `OPENAI_API_KEY`
  - `OPENAI_CHAT_MODEL`
  - `OPENAI_EMBED_MODEL` (used for pgvector embeddings)
- Gemini:
  - `GEMINI_API_KEY`
  - `GEMINI_MODEL`
- Anthropic:
  - `ANTHROPIC_API_KEY`
  - `ANTHROPIC_MODEL`

## Vector Store
- `VECTORSTORE` = memory|pgvector
- When `pgvector`:
  - `PG_DSN`
  - `PG_COLLECTION`
  - Requires `OPENAI_API_KEY` for embeddings (fail-fast)

## Web Search
- `WEB_SEARCH_ENABLED` = true|false (default false)
- `WEB_SEARCH_PROVIDER` = serper|tavily
- `WEB_SEARCH_API_KEY` (required when enabled)

See `.env.example` for the full list.
