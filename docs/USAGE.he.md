# שימוש

## הרצה (מומלץ)
1) צור `.env` מתוך `.env.example`
2) הגדר `RAG_API_KEY`
3) הרצה בדוקר:
   - `docker compose up -d --build`

## הרצה (Dev מקומי)
1) צור venv והתקן תלויות:
   - `python -m venv .venv`
   - הפעל venv
   - `pip install -U pip`
   - `pip install .`
2) צור `.env` מתוך `.env.example`
3) הרץ דרך CLI (מריץ audit לפני עלייה):
   - `python -m src.cli serve --host 127.0.0.1 --port 8000`

## קריאה ל־API
### בדיקת מצב
- `GET /health`

### שאילתא (חובה API key)
- `POST /ask`
- כותרת: `X-API-Key: <RAG_API_KEY>`
- גוף:
  `{ "question": "..." }`

## אופציונלי: Web search
- `WEB_SEARCH_ENABLED=true`
- `WEB_SEARCH_PROVIDER=serper`
- `WEB_SEARCH_API_KEY=<key>`
