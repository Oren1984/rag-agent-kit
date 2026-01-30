# Troubleshooting

## Service fails to start
- Ensure `.env` exists and contains `RAG_API_KEY`
- Ensure you are running from repo root

## 401 Invalid API key
- Send header: `X-API-Key: <your key>`
- Confirm `.env` key matches

## Port already in use
- Change port mapping in `docker-compose.yml` or stop the other service
