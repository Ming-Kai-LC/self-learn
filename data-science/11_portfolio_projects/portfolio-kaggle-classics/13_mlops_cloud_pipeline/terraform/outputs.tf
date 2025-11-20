# ==================== IAM Outputs ====================

output "sagemaker_execution_role_arn" {
  description = "ARN of the SageMaker execution role"
  value       = aws_iam_role.sagemaker_execution.arn
}

output "sagemaker_execution_role_name" {
  description = "Name of the SageMaker execution role"
  value       = aws_iam_role.sagemaker_execution.name
}

output "lambda_retraining_role_arn" {
  description = "ARN of the Lambda retraining role"
  value       = aws_iam_role.lambda_retraining.arn
}

# ==================== S3 Outputs ====================

output "data_bucket_name" {
  description = "Name of the S3 bucket for training data"
  value       = aws_s3_bucket.data.id
}

output "data_bucket_arn" {
  description = "ARN of the S3 bucket for training data"
  value       = aws_s3_bucket.data.arn
}

output "models_bucket_name" {
  description = "Name of the S3 bucket for model artifacts"
  value       = aws_s3_bucket.models.id
}

output "models_bucket_arn" {
  description = "ARN of the S3 bucket for model artifacts"
  value       = aws_s3_bucket.models.arn
}

output "logs_bucket_name" {
  description = "Name of the S3 bucket for logs and artifacts"
  value       = aws_s3_bucket.logs.id
}

output "logs_bucket_arn" {
  description = "ARN of the S3 bucket for logs and artifacts"
  value       = aws_s3_bucket.logs.arn
}

# ==================== ECR Outputs ====================

output "ecr_repository_url" {
  description = "URL of the ECR repository for model containers"
  value       = aws_ecr_repository.model_container.repository_url
}

output "ecr_repository_arn" {
  description = "ARN of the ECR repository"
  value       = aws_ecr_repository.model_container.arn
}

output "ecr_repository_name" {
  description = "Name of the ECR repository"
  value       = aws_ecr_repository.model_container.name
}

# ==================== SageMaker Outputs ====================

output "model_package_group_name" {
  description = "Name of the SageMaker model package group"
  value       = aws_sagemaker_model_package_group.models.model_package_group_name
}

output "model_package_group_arn" {
  description = "ARN of the SageMaker model package group"
  value       = aws_sagemaker_model_package_group.models.arn
}

# ==================== CloudWatch Outputs ====================

output "training_jobs_log_group_name" {
  description = "Name of CloudWatch log group for training jobs"
  value       = aws_cloudwatch_log_group.training_jobs.name
}

output "training_jobs_log_group_arn" {
  description = "ARN of CloudWatch log group for training jobs"
  value       = aws_cloudwatch_log_group.training_jobs.arn
}

output "endpoints_log_group_name" {
  description = "Name of CloudWatch log group for endpoints"
  value       = aws_cloudwatch_log_group.endpoints.name
}

output "endpoints_log_group_arn" {
  description = "ARN of CloudWatch log group for endpoints"
  value       = aws_cloudwatch_log_group.endpoints.arn
}

# ==================== SNS Outputs ====================

output "sns_topic_arn" {
  description = "ARN of the SNS topic for alerts"
  value       = aws_sns_topic.alerts.arn
}

output "sns_topic_name" {
  description = "Name of the SNS topic for alerts"
  value       = aws_sns_topic.alerts.name
}

# ==================== Auto-scaling Outputs ====================

output "autoscaling_enabled" {
  description = "Whether auto-scaling is enabled"
  value       = var.enable_autoscaling
}

output "autoscaling_min_instances" {
  description = "Minimum number of instances for auto-scaling"
  value       = var.min_instance_count
}

output "autoscaling_max_instances" {
  description = "Maximum number of instances for auto-scaling"
  value       = var.max_instance_count
}

# ==================== Configuration Outputs ====================

output "project_name" {
  description = "Project name"
  value       = var.project_name
}

output "environment" {
  description = "Environment name"
  value       = var.environment
}

output "aws_region" {
  description = "AWS region"
  value       = var.aws_region
}

# ==================== Helpful Commands ====================

output "helpful_commands" {
  description = "Helpful AWS CLI commands for using these resources"
  value = {
    upload_training_data = "aws s3 cp data/train/ s3://${aws_s3_bucket.data.id}/train/ --recursive"
    list_models          = "aws sagemaker list-model-packages --model-package-group-name ${aws_sagemaker_model_package_group.models.model_package_group_name}"
    view_logs            = "aws logs tail ${aws_cloudwatch_log_group.training_jobs.name} --follow"
    ecr_login            = "aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${aws_ecr_repository.model_container.repository_url}"
  }
}

# ==================== Infrastructure Summary ====================

output "infrastructure_summary" {
  description = "Summary of deployed infrastructure"
  value = {
    s3_buckets = {
      data   = aws_s3_bucket.data.id
      models = aws_s3_bucket.models.id
      logs   = aws_s3_bucket.logs.id
    }
    sagemaker = {
      execution_role       = aws_iam_role.sagemaker_execution.arn
      model_package_group  = aws_sagemaker_model_package_group.models.model_package_group_name
    }
    ecr = {
      repository_url = aws_ecr_repository.model_container.repository_url
    }
    monitoring = {
      sns_topic          = aws_sns_topic.alerts.arn
      training_logs      = aws_cloudwatch_log_group.training_jobs.name
      endpoint_logs      = aws_cloudwatch_log_group.endpoints.name
    }
    autoscaling = {
      enabled       = var.enable_autoscaling
      min_instances = var.min_instance_count
      max_instances = var.max_instance_count
    }
  }
}
