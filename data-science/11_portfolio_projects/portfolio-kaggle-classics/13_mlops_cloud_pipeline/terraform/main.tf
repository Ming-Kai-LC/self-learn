terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Optional: Configure S3 backend for remote state
  # backend "s3" {
  #   bucket = "mlops-terraform-state"
  #   key    = "sentiment-analysis/terraform.tfstate"
  #   region = "us-east-1"
  # }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
      Purpose     = "MLOps"
    }
  }
}

# ==================== Data Storage ====================

# S3 bucket for training/validation data
resource "aws_s3_bucket" "data" {
  bucket = "${var.project_name}-data-${var.environment}"

  tags = {
    Name = "Training Data Storage"
  }
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# S3 bucket for model artifacts
resource "aws_s3_bucket" "models" {
  bucket = "${var.project_name}-models-${var.environment}"

  tags = {
    Name = "Model Artifacts Storage"
  }
}

resource "aws_s3_bucket_versioning" "models" {
  bucket = aws_s3_bucket.models.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "models" {
  bucket = aws_s3_bucket.models.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# S3 bucket for logs and artifacts
resource "aws_s3_bucket" "logs" {
  bucket = "${var.project_name}-logs-${var.environment}"

  tags = {
    Name = "Logs and Artifacts Storage"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "logs" {
  bucket = aws_s3_bucket.logs.id

  rule {
    id     = "archive-old-logs"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }
  }
}

# ==================== IAM Roles and Policies ====================

# SageMaker execution role
resource "aws_iam_role" "sagemaker_execution" {
  name = "${var.project_name}-sagemaker-execution-${var.environment}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "sagemaker.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Name = "SageMaker Execution Role"
  }
}

# SageMaker execution policy
resource "aws_iam_role_policy" "sagemaker_execution" {
  name = "sagemaker-execution-policy"
  role = aws_iam_role.sagemaker_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.data.arn,
          "${aws_s3_bucket.data.arn}/*",
          aws_s3_bucket.models.arn,
          "${aws_s3_bucket.models.arn}/*",
          aws_s3_bucket.logs.arn,
          "${aws_s3_bucket.logs.arn}/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "ecr:GetDownloadUrlForLayer",
          "ecr:BatchGetImage",
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetAuthorizationToken"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "cloudwatch:PutMetricData",
          "cloudwatch:GetMetricData",
          "cloudwatch:GetMetricStatistics",
          "cloudwatch:ListMetrics"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogStreams"
        ]
        Resource = "arn:aws:logs:${var.aws_region}:*:log-group:/aws/sagemaker/*"
      },
      {
        Effect = "Allow"
        Action = [
          "sagemaker:DescribeTrainingJob",
          "sagemaker:DescribeEndpoint",
          "sagemaker:DescribeEndpointConfig",
          "sagemaker:DescribeModel"
        ]
        Resource = "*"
      }
    ]
  })
}

# ==================== ECR Repository ====================

resource "aws_ecr_repository" "model_container" {
  name                 = "${var.project_name}-model"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "AES256"
  }

  tags = {
    Name = "Model Container Repository"
  }
}

resource "aws_ecr_lifecycle_policy" "model_container" {
  repository = aws_ecr_repository.model_container.name

  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Keep last 10 images"
        selection = {
          tagStatus     = "tagged"
          tagPrefixList = ["v"]
          countType     = "imageCountMoreThan"
          countNumber   = 10
        }
        action = {
          type = "expire"
        }
      },
      {
        rulePriority = 2
        description  = "Remove untagged images after 7 days"
        selection = {
          tagStatus   = "untagged"
          countType   = "sinceImagePushed"
          countUnit   = "days"
          countNumber = 7
        }
        action = {
          type = "expire"
        }
      }
    ]
  })
}

# ==================== SageMaker Model Package Group ====================

resource "aws_sagemaker_model_package_group" "models" {
  model_package_group_name        = "${var.project_name}-models"
  model_package_group_description = "Sentiment analysis models for ${var.project_name}"

  tags = {
    Name = "Model Registry"
  }
}

# ==================== CloudWatch Log Groups ====================

resource "aws_cloudwatch_log_group" "training_jobs" {
  name              = "/aws/sagemaker/TrainingJobs/${var.project_name}"
  retention_in_days = 30

  tags = {
    Name = "Training Jobs Logs"
  }
}

resource "aws_cloudwatch_log_group" "endpoints" {
  name              = "/aws/sagemaker/Endpoints/${var.project_name}"
  retention_in_days = 30

  tags = {
    Name = "Endpoint Logs"
  }
}

# ==================== SNS Topics for Alerts ====================

resource "aws_sns_topic" "alerts" {
  name = "${var.project_name}-alerts-${var.environment}"

  tags = {
    Name = "MLOps Alert Notifications"
  }
}

resource "aws_sns_topic_subscription" "alerts_email" {
  count     = var.alert_email != "" ? 1 : 0
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = var.alert_email
}

# ==================== Lambda for Scheduled Retraining ====================

# Lambda execution role
resource "aws_iam_role" "lambda_retraining" {
  name = "${var.project_name}-lambda-retraining-${var.environment}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Name = "Lambda Retraining Role"
  }
}

resource "aws_iam_role_policy" "lambda_retraining" {
  name = "lambda-retraining-policy"
  role = aws_iam_role.lambda_retraining.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sagemaker:CreateTrainingJob",
          "sagemaker:DescribeTrainingJob"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "arn:aws:logs:${var.aws_region}:*:log-group:/aws/lambda/*"
      },
      {
        Effect = "Allow"
        Action = [
          "iam:PassRole"
        ]
        Resource = aws_iam_role.sagemaker_execution.arn
      }
    ]
  })
}

# ==================== EventBridge Rule for Scheduled Retraining ====================

resource "aws_cloudwatch_event_rule" "scheduled_retraining" {
  count               = var.enable_scheduled_retraining ? 1 : 0
  name                = "${var.project_name}-scheduled-retraining-${var.environment}"
  description         = "Trigger model retraining weekly"
  schedule_expression = var.retraining_schedule

  tags = {
    Name = "Scheduled Retraining Rule"
  }
}

# ==================== Application Auto Scaling ====================

# Auto-scaling target for SageMaker endpoint
resource "aws_appautoscaling_target" "endpoint" {
  count              = var.enable_autoscaling ? 1 : 0
  max_capacity       = var.max_instance_count
  min_capacity       = var.min_instance_count
  resource_id        = "endpoint/${var.project_name}-${var.environment}/variant/AllTraffic"
  scalable_dimension = "sagemaker:variant:DesiredInstanceCount"
  service_namespace  = "sagemaker"

  depends_on = [
    aws_iam_role.sagemaker_execution
  ]
}

# Auto-scaling policy
resource "aws_appautoscaling_policy" "endpoint" {
  count              = var.enable_autoscaling ? 1 : 0
  name               = "${var.project_name}-autoscaling-policy-${var.environment}"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.endpoint[0].resource_id
  scalable_dimension = aws_appautoscaling_target.endpoint[0].scalable_dimension
  service_namespace  = aws_appautoscaling_target.endpoint[0].service_namespace

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "SageMakerVariantInvocationsPerInstance"
    }

    target_value       = var.target_invocations_per_instance
    scale_in_cooldown  = 300
    scale_out_cooldown = 60
  }
}

# ==================== Outputs ====================

output "sagemaker_execution_role_arn" {
  description = "ARN of SageMaker execution role"
  value       = aws_iam_role.sagemaker_execution.arn
}

output "data_bucket_name" {
  description = "Name of S3 bucket for training data"
  value       = aws_s3_bucket.data.id
}

output "models_bucket_name" {
  description = "Name of S3 bucket for model artifacts"
  value       = aws_s3_bucket.models.id
}

output "logs_bucket_name" {
  description = "Name of S3 bucket for logs"
  value       = aws_s3_bucket.logs.id
}

output "ecr_repository_url" {
  description = "URL of ECR repository"
  value       = aws_ecr_repository.model_container.repository_url
}

output "model_package_group_name" {
  description = "Name of SageMaker model package group"
  value       = aws_sagemaker_model_package_group.models.model_package_group_name
}

output "sns_topic_arn" {
  description = "ARN of SNS topic for alerts"
  value       = aws_sns_topic.alerts.arn
}
