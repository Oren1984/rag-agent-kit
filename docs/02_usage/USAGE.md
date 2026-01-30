# Usage

## Run (recommended)
1) Create `.env` from `.env.example`
2) Set `RAG_API_KEY`
3) Start with Docker:
   - `docker compose up -d --build`

## Run (local dev)
1) Create venv + install deps:
   - `python -m venv .venv`
   - activate venv
   - `pip install -U pip`
   - `pip install .`
2) Create `.env` from `.env.example`
3) Start via CLI (runs audit first):
   - `python -m src.cli serve --host 127.0.0.1 --port 8000`

## Call API
### Health
- `GET /health`

### Ask (requires API key)
- `POST /ask`
- Header: `X-API-Key: <RAG_API_KEY>`
- Body:
  `{ "question": "..." }`

## Optional: Web search
- Set `WEB_SEARCH_ENABLED=true`
- Set `WEB_SEARCH_PROVIDER=serper`
- Set `WEB_SEARCH_API_KEY=<your key>`
