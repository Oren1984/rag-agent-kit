# RAG Agent Kit (ברירת מחדל מאובטחת)

ערכת קוד פתוח לבניית **סוכן RAG** שמתחבר לכל אפליקציה דרך מחברים (Connectors) ומנועי LLM (Providers).

מאפיינים:
- **מאובטח כברירת מחדל** (השירות לא יעלה בלי AUTH)
- **מודולרי וגמיש** (ספקי LLM / מחברים / Vector Store)
- **הפעלה קלה** (Docker מומלץ)

> בלי UI. API בלבד. ריצה אוטונומית עם בדיקות בסיסיות.

## התחלה מהירה (Docker - מומלץ)
1) שיבוט הריפו
2) העתק `.env.example` ל־`.env`
3) הגדר `RAG_API_KEY` לערך חזק
4) הרץ: `docker compose up -d --build`
5) תיעוד Swagger: http://127.0.0.1:8000/docs

## אבטחה (חשוב)
- חובה `X-API-Key`
- ברירת מחדל מאזינה רק ל־localhost
- Web Search כבוי כברירת מחדל

מסמכים:
- `docs/SECURITY.md`
- `docs/SECURITY_MODEL.md`
