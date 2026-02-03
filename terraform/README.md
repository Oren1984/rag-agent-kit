# Terraform (Infra-Only)

This folder contains **AWS infra-only** Terraform that creates an **ECR repository** and minimal IAM outputs.
It does **NOT** deploy any runtime services to AWS.

- Local runtime is **Docker Compose** (default)
- AWS Terraform is **optional** and infra-only (ECR + outputs)

See:
- docs/AWS_INFRA_ONLY.md
- docs/COSTS_AND_CLEANUP.md
