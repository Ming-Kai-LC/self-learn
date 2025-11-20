terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ==================== Variables ====================

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "mlops-sentiment"
}

variable "environment" {
  description = "Environment (dev, staging, production)"
  type        = string
  default     = "production"
}

variable "endpoint_name" {
  description = "SageMaker endpoint name"
  type        = string
  default     = ""
}

variable "sns_topic_arn" {
  description = "SNS topic ARN for alerts"
  type        = string
  default     = ""
}

variable "latency_threshold_ms" {
  description = "Latency threshold in milliseconds"
  type        = number
  default     = 500
}

variable "error_rate_threshold" {
  description = "Error rate threshold (percentage)"
  type        = number
  default     = 5
}

variable "invocation_threshold" {
  description = "Minimum invocations per period"
  type        = number
  default     = 1
}

variable "cost_threshold_usd" {
  description = "Daily cost threshold in USD"
  type        = number
  default     = 50
}

# ==================== Local Variables ====================

locals {
  endpoint_name = var.endpoint_name != "" ? var.endpoint_name : "${var.project_name}-${var.environment}"
  sns_topic_arn = var.sns_topic_arn != "" ? var.sns_topic_arn : "arn:aws:sns:${var.aws_region}:${data.aws_caller_identity.current.account_id}:${var.project_name}-alerts-${var.environment}"
}

data "aws_caller_identity" "current" {}

# ==================== CloudWatch Alarms ====================

# Alarm: High Model Latency
resource "aws_cloudwatch_metric_alarm" "high_latency" {
  alarm_name          = "${var.project_name}-${var.environment}-high-latency"
  alarm_description   = "Alert when model latency exceeds ${var.latency_threshold_ms}ms"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "ModelLatency"
  namespace           = "AWS/SageMaker"
  period              = 300 # 5 minutes
  statistic           = "Average"
  threshold           = var.latency_threshold_ms
  treat_missing_data  = "notBreaching"

  dimensions = {
    EndpointName = local.endpoint_name
    VariantName  = "AllTraffic"
  }

  alarm_actions = [local.sns_topic_arn]
  ok_actions    = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Latency"
  }
}

# Alarm: P95 Model Latency
resource "aws_cloudwatch_metric_alarm" "p95_latency" {
  alarm_name          = "${var.project_name}-${var.environment}-p95-latency"
  alarm_description   = "Alert when P95 latency exceeds ${var.latency_threshold_ms}ms"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "ModelLatency"
  namespace           = "AWS/SageMaker"
  period              = 300
  extended_statistic  = "p95"
  threshold           = var.latency_threshold_ms
  treat_missing_data  = "notBreaching"

  dimensions = {
    EndpointName = local.endpoint_name
    VariantName  = "AllTraffic"
  }

  alarm_actions = [local.sns_topic_arn]
  ok_actions    = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Latency"
  }
}

# Alarm: High Error Rate (4xx errors)
resource "aws_cloudwatch_metric_alarm" "high_4xx_errors" {
  alarm_name          = "${var.project_name}-${var.environment}-high-4xx-errors"
  alarm_description   = "Alert when 4xx error rate exceeds ${var.error_rate_threshold}%"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  threshold           = var.error_rate_threshold
  treat_missing_data  = "notBreaching"

  metric_query {
    id          = "error_rate"
    expression  = "(m1 / m2) * 100"
    label       = "4xx Error Rate"
    return_data = true
  }

  metric_query {
    id = "m1"
    metric {
      metric_name = "Invocation4XXErrors"
      namespace   = "AWS/SageMaker"
      period      = 300
      stat        = "Sum"

      dimensions = {
        EndpointName = local.endpoint_name
        VariantName  = "AllTraffic"
      }
    }
  }

  metric_query {
    id = "m2"
    metric {
      metric_name = "Invocations"
      namespace   = "AWS/SageMaker"
      period      = 300
      stat        = "Sum"

      dimensions = {
        EndpointName = local.endpoint_name
        VariantName  = "AllTraffic"
      }
    }
  }

  alarm_actions = [local.sns_topic_arn]
  ok_actions    = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Errors"
  }
}

# Alarm: High Error Rate (5xx errors)
resource "aws_cloudwatch_metric_alarm" "high_5xx_errors" {
  alarm_name          = "${var.project_name}-${var.environment}-high-5xx-errors"
  alarm_description   = "Alert when 5xx error rate exceeds ${var.error_rate_threshold}%"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  threshold           = var.error_rate_threshold
  treat_missing_data  = "notBreaching"

  metric_query {
    id          = "error_rate"
    expression  = "(m1 / m2) * 100"
    label       = "5xx Error Rate"
    return_data = true
  }

  metric_query {
    id = "m1"
    metric {
      metric_name = "Invocation5XXErrors"
      namespace   = "AWS/SageMaker"
      period      = 300
      stat        = "Sum"

      dimensions = {
        EndpointName = local.endpoint_name
        VariantName  = "AllTraffic"
      }
    }
  }

  metric_query {
    id = "m2"
    metric {
      metric_name = "Invocations"
      namespace   = "AWS/SageMaker"
      period      = 300
      stat        = "Sum"

      dimensions = {
        EndpointName = local.endpoint_name
        VariantName  = "AllTraffic"
      }
    }
  }

  alarm_actions = [local.sns_topic_arn]
  ok_actions    = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Errors"
  }
}

# Alarm: Low Invocation Count (potential data drift or system issue)
resource "aws_cloudwatch_metric_alarm" "low_invocations" {
  alarm_name          = "${var.project_name}-${var.environment}-low-invocations"
  alarm_description   = "Alert when invocations drop below ${var.invocation_threshold} (potential issue)"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = 3
  metric_name         = "Invocations"
  namespace           = "AWS/SageMaker"
  period              = 1800 # 30 minutes
  statistic           = "Sum"
  threshold           = var.invocation_threshold
  treat_missing_data  = "breaching"

  dimensions = {
    EndpointName = local.endpoint_name
    VariantName  = "AllTraffic"
  }

  alarm_actions = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Traffic"
  }
}

# Alarm: High CPU Utilization
resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  alarm_name          = "${var.project_name}-${var.environment}-high-cpu"
  alarm_description   = "Alert when CPU utilization exceeds 80%"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "/aws/sagemaker/Endpoints"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  treat_missing_data  = "notBreaching"

  dimensions = {
    EndpointName = local.endpoint_name
    VariantName  = "AllTraffic"
  }

  alarm_actions = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Resources"
  }
}

# Alarm: High Memory Utilization
resource "aws_cloudwatch_metric_alarm" "high_memory" {
  alarm_name          = "${var.project_name}-${var.environment}-high-memory"
  alarm_description   = "Alert when memory utilization exceeds 85%"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "MemoryUtilization"
  namespace           = "/aws/sagemaker/Endpoints"
  period              = 300
  statistic           = "Average"
  threshold           = 85
  treat_missing_data  = "notBreaching"

  dimensions = {
    EndpointName = local.endpoint_name
    VariantName  = "AllTraffic"
  }

  alarm_actions = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Resources"
  }
}

# ==================== Cost Monitoring ====================

# Alarm: High Daily Cost
resource "aws_cloudwatch_metric_alarm" "high_cost" {
  alarm_name          = "${var.project_name}-${var.environment}-high-cost"
  alarm_description   = "Alert when estimated daily cost exceeds $${var.cost_threshold_usd}"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "EstimatedCharges"
  namespace           = "AWS/Billing"
  period              = 86400 # 1 day
  statistic           = "Maximum"
  threshold           = var.cost_threshold_usd
  treat_missing_data  = "notBreaching"

  dimensions = {
    Currency = "USD"
  }

  alarm_actions = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "Cost"
  }
}

# ==================== Custom Metrics ====================

# Alarm: Data Drift Detection (custom metric)
resource "aws_cloudwatch_metric_alarm" "data_drift" {
  alarm_name          = "${var.project_name}-${var.environment}-data-drift"
  alarm_description   = "Alert when data drift score exceeds threshold"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "DataDriftScore"
  namespace           = "MLOps"
  period              = 3600 # 1 hour
  statistic           = "Average"
  threshold           = 0.3
  treat_missing_data  = "notBreaching"

  dimensions = {
    Project     = var.project_name
    Environment = var.environment
  }

  alarm_actions = [local.sns_topic_arn]

  tags = {
    Project     = var.project_name
    Environment = var.environment
    Type        = "DataQuality"
  }
}

# ==================== CloudWatch Dashboard ====================

resource "aws_cloudwatch_dashboard" "main" {
  dashboard_name = "${var.project_name}-${var.environment}-dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric"
        properties = {
          metrics = [
            ["AWS/SageMaker", "ModelLatency", { stat = "Average" }],
            ["...", { stat = "p95" }],
            ["...", { stat = "p99" }]
          ]
          period = 300
          stat   = "Average"
          region = var.aws_region
          title  = "Model Latency"
          yAxis = {
            left = {
              label = "Milliseconds"
            }
          }
        }
      },
      {
        type = "metric"
        properties = {
          metrics = [
            ["AWS/SageMaker", "Invocations", { stat = "Sum" }],
            [".", "Invocation4XXErrors", { stat = "Sum" }],
            [".", "Invocation5XXErrors", { stat = "Sum" }]
          ]
          period = 300
          stat   = "Sum"
          region = var.aws_region
          title  = "Invocations and Errors"
        }
      },
      {
        type = "metric"
        properties = {
          metrics = [
            ["/aws/sagemaker/Endpoints", "CPUUtilization"],
            [".", "MemoryUtilization"]
          ]
          period = 300
          stat   = "Average"
          region = var.aws_region
          title  = "Resource Utilization"
          yAxis = {
            left = {
              label = "Percentage"
            }
          }
        }
      }
    ]
  })
}

# ==================== Outputs ====================

output "dashboard_url" {
  description = "CloudWatch Dashboard URL"
  value       = "https://console.aws.amazon.com/cloudwatch/home?region=${var.aws_region}#dashboards:name=${aws_cloudwatch_dashboard.main.dashboard_name}"
}

output "alarm_names" {
  description = "List of created CloudWatch alarms"
  value = [
    aws_cloudwatch_metric_alarm.high_latency.alarm_name,
    aws_cloudwatch_metric_alarm.p95_latency.alarm_name,
    aws_cloudwatch_metric_alarm.high_4xx_errors.alarm_name,
    aws_cloudwatch_metric_alarm.high_5xx_errors.alarm_name,
    aws_cloudwatch_metric_alarm.low_invocations.alarm_name,
    aws_cloudwatch_metric_alarm.high_cpu.alarm_name,
    aws_cloudwatch_metric_alarm.high_memory.alarm_name,
    aws_cloudwatch_metric_alarm.high_cost.alarm_name,
    aws_cloudwatch_metric_alarm.data_drift.alarm_name,
  ]
}
