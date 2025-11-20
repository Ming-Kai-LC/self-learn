variable "aws_region" {
  description = "AWS region for all resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for naming resources"
  type        = string
  default     = "mlops-sentiment"

  validation {
    condition     = can(regex("^[a-z0-9-]+$", var.project_name))
    error_message = "Project name must contain only lowercase letters, numbers, and hyphens"
  }
}

variable "environment" {
  description = "Environment (dev, staging, production)"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production"
  }
}

variable "alert_email" {
  description = "Email address for CloudWatch alerts"
  type        = string
  default     = ""
}

variable "enable_autoscaling" {
  description = "Enable auto-scaling for SageMaker endpoints"
  type        = bool
  default     = true
}

variable "min_instance_count" {
  description = "Minimum number of instances for endpoint auto-scaling"
  type        = number
  default     = 1

  validation {
    condition     = var.min_instance_count >= 1
    error_message = "Minimum instance count must be at least 1"
  }
}

variable "max_instance_count" {
  description = "Maximum number of instances for endpoint auto-scaling"
  type        = number
  default     = 5

  validation {
    condition     = var.max_instance_count >= var.min_instance_count
    error_message = "Maximum instance count must be greater than or equal to minimum"
  }
}

variable "target_invocations_per_instance" {
  description = "Target number of invocations per instance for auto-scaling"
  type        = number
  default     = 1000
}

variable "enable_scheduled_retraining" {
  description = "Enable scheduled model retraining"
  type        = bool
  default     = false
}

variable "retraining_schedule" {
  description = "Cron expression for scheduled retraining (e.g., 'cron(0 2 ? * SUN *)')"
  type        = string
  default     = "cron(0 2 ? * SUN *)"  # Every Sunday at 2 AM UTC
}

variable "model_instance_type" {
  description = "Instance type for model endpoint"
  type        = string
  default     = "ml.m5.large"

  validation {
    condition     = can(regex("^ml\\.", var.model_instance_type))
    error_message = "Instance type must start with 'ml.'"
  }
}

variable "training_instance_type" {
  description = "Instance type for training jobs"
  type        = string
  default     = "ml.m5.xlarge"

  validation {
    condition     = can(regex("^ml\\.", var.training_instance_type))
    error_message = "Instance type must start with 'ml.'"
  }
}

variable "enable_model_monitoring" {
  description = "Enable SageMaker Model Monitor for data drift detection"
  type        = bool
  default     = true
}

variable "cloudwatch_retention_days" {
  description = "Number of days to retain CloudWatch logs"
  type        = number
  default     = 30

  validation {
    condition     = contains([1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653], var.cloudwatch_retention_days)
    error_message = "Retention days must be a valid CloudWatch retention period"
  }
}

variable "s3_lifecycle_transition_days" {
  description = "Number of days before transitioning S3 objects to cheaper storage"
  type        = number
  default     = 30
}

variable "s3_lifecycle_expiration_days" {
  description = "Number of days before expiring S3 objects"
  type        = number
  default     = 365
}

variable "enable_versioning" {
  description = "Enable versioning for S3 buckets"
  type        = bool
  default     = true
}

variable "enable_encryption" {
  description = "Enable encryption for S3 buckets"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags to apply to all resources"
  type        = map(string)
  default     = {}
}

variable "endpoint_initial_instance_count" {
  description = "Initial instance count for endpoint deployment"
  type        = number
  default     = 1
}

variable "enable_data_capture" {
  description = "Enable data capture for endpoint monitoring"
  type        = bool
  default     = true
}

variable "data_capture_percentage" {
  description = "Percentage of requests to capture for monitoring (0-100)"
  type        = number
  default     = 10

  validation {
    condition     = var.data_capture_percentage >= 0 && var.data_capture_percentage <= 100
    error_message = "Data capture percentage must be between 0 and 100"
  }
}

variable "cost_alert_threshold" {
  description = "Monthly cost threshold for billing alerts (USD)"
  type        = number
  default     = 200
}

variable "enable_vpc_config" {
  description = "Enable VPC configuration for SageMaker resources"
  type        = bool
  default     = false
}

variable "vpc_security_group_ids" {
  description = "Security group IDs for VPC configuration"
  type        = list(string)
  default     = []
}

variable "vpc_subnet_ids" {
  description = "Subnet IDs for VPC configuration"
  type        = list(string)
  default     = []
}
