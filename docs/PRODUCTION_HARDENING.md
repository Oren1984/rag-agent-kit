# Production Hardening (Recommended)

If you deploy publicly:
- Put behind reverse proxy (Nginx/Traefik) with TLS
- Add rate limiting at proxy layer
- Restrict allowed origins (CORS)
- Centralize logs + metrics (Prometheus/Grafana)
- Rotate API keys and store secrets securely
