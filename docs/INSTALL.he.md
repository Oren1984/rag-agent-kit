# התקנה

## אפשרות A  Docker (מומלץ)
1) צור `.env` מתוך `.env.example`
2) הגדר `RAG_API_KEY` (חובה)
3) הרץ:
   - `docker compose up -d --build`
4) בדיקה:
   - `GET http://127.0.0.1:8000/health`
   - Swagger: `http://127.0.0.1:8000/docs`

## אפשרות B  ללא Docker (Dev בלבד)
1) `python -m venv .venv`
2) הפעל venv
3) `pip install -U pip`
4) `pip install .`
5) צור `.env` והגדר `RAG_API_KEY`
6) `uvicorn src.main:app --host 127.0.0.1 --port 8000`
