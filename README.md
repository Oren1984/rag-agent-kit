# RAG Agent Kit (Secure-by-Default)

A modular, open-source **RAG agent** you can plug into any application.
Designed to be:
- **Secure-by-default** (won’t start without auth)
- **Modular** (LLM providers, connectors, vector stores)
- **Easy to install** (Docker recommended)

> No UI. API-only. Autonomous operation with built-in checks.

---

## Features
- Core RAG API: `POST /ask`
- Health/Readiness: `GET /health`, `GET /ready`
- Provider adapters (pluggable): OpenAI / Gemini / Anthropic *(Copilot optional/experimental)*
- Connectors (pluggable): REST / Files *(extendable)*
- Web Search (optional): OFF by default
- Built-in: basic `audit` + `smoke test` scripts
- CI: runs audit + tests
- - **Automation Ready**: Easy integration with workflow engines such as n8n or custom webhooks
- **Live Intelligence (Optional)**: External web search via Tavily / Serper for real-time context enrichment

---

## Quickstart (Docker - Recommended)
1) Clone:
   - `git clone <your-repo-url>`
2) Create `.env`:
   - `cp .env.example .env` *(Windows: copy manually)*
   - Set `RAG_API_KEY` to a strong value
3) Run:
   - `docker compose up -d --build`
4) Open docs:
   - http://127.0.0.1:8000/docs

---

## Quickstart (No Docker - Dev only)
1) `python -m venv .venv`
2) Activate venv
3) `pip install -U pip`
4) `pip install .`
5) Copy `.env.example`  `.env` and set `RAG_API_KEY`
6) `uvicorn src.main:app --host 127.0.0.1 --port 8000`

---

## Security (Important)
- **AUTH is mandatory**: requests require `X-API-Key`
- Docker compose binds to **localhost only** by default
- Web search is **OFF by default**
- Do not expose to the public internet without a reverse proxy + TLS

See: `docs/SECURITY.md` and `docs/SECURITY_MODEL.md`

---

## Docs
- Install: `docs/INSTALL.md`
- Config: `docs/CONFIG.md`
- Security: `docs/SECURITY.md`
- Troubleshooting: `docs/TROUBLESHOOTING.md`
- Supported deployment: `SUPPORTED_DEPLOYMENT.md`

Hebrew docs:
- `README.he.md`
- `docs/*he.md`

---

## License
MIT (see `LICENSE`)
