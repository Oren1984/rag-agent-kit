# terraform/modules/ecr/main.tf
# ECR Module to create an ECR repository with lifecycle policy

# Create the ECR repository
resource "aws_ecr_repository" "this" {
  name         = var.name
  force_delete = true
}

# Lifecycle policy to retain only the last 10 images
resource "aws_ecr_lifecycle_policy" "this" {
  repository = aws_ecr_repository.this.name
  policy = jsonencode({
    rules = [{
      rulePriority = 1
      description  = "Keep last 10 images"
      selection = {
        tagStatus   = "any"
        countType   = "imageCountMoreThan"
        countNumber = 10
      }
      action = { type = "expire" }
    }]
  })
}
