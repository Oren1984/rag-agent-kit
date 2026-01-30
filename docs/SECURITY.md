# Security

## Secure-by-default rules
- Service will not start without `RAG_API_KEY`
- All requests to protected endpoints require `X-API-Key`
- Docker compose binds to `127.0.0.1` by default (not public)
- Web search is OFF by default

## Do NOT do this
- Do not expose the API publicly without a reverse proxy + TLS
- Do not set CORS to `*` in production
- Do not run with debug settings in production

## Recommended hardening (production)
See `docs/PRODUCTION_HARDENING.md`
