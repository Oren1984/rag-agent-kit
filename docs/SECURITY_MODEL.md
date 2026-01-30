# Security Model

This project aims to be **secure-by-default**.

## Defaults
- API auth is mandatory (`X-API-Key`)
- Localhost binding in compose
- Web search off by default

## Responsibility boundaries
- The repository provides a safe baseline configuration.
- Deployment, exposure to the internet, and any modifications are the user's responsibility.

See `SUPPORTED_DEPLOYMENT.md`
