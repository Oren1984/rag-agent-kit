# terraform/envs/dev/main.tf
# ECR Module for Dev Environment

# Create an ECR repository for the rag-agent-kit application
module "ecr" {
  source = "../../modules/ecr"
  name   = "rag-agent-kit"
}

# Output the ECR repository URL
output "ecr_url" {
  value = module.ecr.repository_url
}
