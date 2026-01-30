# Supported Deployment

This project is **secure-by-default** when used as documented.

## Supported (official)
- Docker Compose provided in this repository
- Environment variables configured via `.env` (based on `.env.example`)
- API access protected by `X-API-Key`

## Unsupported (user responsibility)
If you modify any of the following, you are responsible for security and reliability:
- Exposing ports publicly (0.0.0.0) without auth/TLS
- Replacing the reverse proxy, networking rules, or CORS policies
- Changing providers/connectors/vector stores beyond documented configurations
- Running in production without a proper deployment hardening (TLS, rate limiting, monitoring)

See:
- `docs/SECURITY.md`
- `docs/PRODUCTION_HARDENING.md`
