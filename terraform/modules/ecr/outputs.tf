# terraform/modules/ecr/outputs.tf
# Output the ECR repository URL

output "repository_url" {
  value = aws_ecr_repository.this.repository_url
}
