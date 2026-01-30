# Installation

## Option A  Docker (Recommended)
1) Copy env:
   - Create `.env` from `.env.example`
2) Set `RAG_API_KEY` (required)
3) Run:
   - `docker compose up -d --build`
4) Verify:
   - `GET http://127.0.0.1:8000/health`
   - Open: `http://127.0.0.1:8000/docs`

## Option B  No Docker (Dev only)
1) `python -m venv .venv`
2) Activate venv
3) `pip install -U pip`
4) `pip install .`
5) Create `.env` and set `RAG_API_KEY`
6) `uvicorn src.main:app --host 127.0.0.1 --port 8000`
