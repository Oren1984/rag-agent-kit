# Deployment

This project is a **headless RAG API (API-only service)**.
Deployment options are intentionally **limited and local-first**,
as this is a **junior-level, educational project**.

The goal is to demonstrate correct runtime setup, configuration,
and validation — **not full cloud deployment**.

---

## Supported Runtime Modes

### 1. Local Development (Python)
- Python virtual environment
- `python -m src.cli serve`
- Intended for development and debugging only

### 2. Docker (Single Container)
- Build using the provided `Dockerfile`
- Useful for local testing and isolated runs

### 3. Docker Compose (Recommended)
- Multi-container local setup
- API + PostgreSQL (pgvector)
- Used for verification, testing, and CI
- **Default runtime for this project**

---

## Explicitly Out of Scope

The following are intentionally **not included**:

- Cloud deployment (ECS, EKS, EC2, App Runner)
- Kubernetes manifests
- Production ingress, load balancers, or autoscaling
- Managed observability or SaaS platforms

Infrastructure work is limited to **infra-only Terraform**
(see `AWS_INFRA_ONLY.md`) and is **not used at runtime**.

---

## Configuration & Secrets
- All configuration is via environment variables
- `.env.example` is provided
- Secrets must never be committed

---

## Notes
- No UI is included (API-only service)
- Reverse proxy can be added externally if required
- Observability is provided via a **local stack**
  (Phoenix + OpenTelemetry, infra-level only)
