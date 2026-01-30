# Deployment

This project is a **headless RAG API** and can be deployed in multiple ways,
depending on the target environment.

## Supported Deployment Options

### 1. Local Development
- Python virtual environment
- `python -m src.cli serve`
- Intended for development and debugging only

### 2. Docker (Single Container)
- Build using `Dockerfile`
- Suitable for local testing and simple deployments

### 3. Docker Compose
- Multi-container setup
- API + PostgreSQL (pgvector)
- Recommended for production-like environments

## Environment Configuration
- All configuration is done via environment variables
- `.env.example` provided as a reference
- Secrets must never be committed

## Notes
- No UI is included (API-only service)
- Reverse proxy (NGINX, Traefik) can be added externally
- Kubernetes deployment is possible but not included
