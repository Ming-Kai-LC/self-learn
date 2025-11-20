# Project 13: MLOps Cloud Pipeline with Docker & AWS

**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 8-12 hours
**Prerequisites**: ML fundamentals, Docker basics, AWS basics, CI/CD concepts

## Problem Statement

Deploy a production-ready sentiment analysis model to AWS cloud infrastructure with a complete MLOps pipeline including:
- Automated training and deployment
- Version control for models and data
- Continuous monitoring and alerting
- Infrastructure as Code (IaC)
- A/B testing capabilities
- Auto-scaling based on traffic
- Cost optimization

This project demonstrates enterprise-level ML deployment practices used by companies to serve models at scale.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         GitHub Repository                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │  src/        │  │  terraform/  │  │  .github/    │             │
│  │  train.py    │  │  main.tf     │  │  workflows/  │             │
│  │  inference.py│  │  variables.tf│  │  deploy.yml  │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ Git Push
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      GitHub Actions (CI/CD)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │   Linting    │→│   Testing    │→│   Docker     │             │
│  │   & Formatting│  │   pytest     │  │   Build      │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ Deploy
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          AWS Cloud                                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    S3 Buckets                                │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │  │
│  │  │  Raw Data    │  │  Model       │  │  Artifacts   │      │  │
│  │  │  Storage     │  │  Registry    │  │  & Logs      │      │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              SageMaker Training Jobs                        │  │
│  │  - Automated model training                                 │  │
│  │  - Hyperparameter tuning                                    │  │
│  │  - Model evaluation                                         │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              SageMaker Model Registry                       │  │
│  │  - Version control                                          │  │
│  │  - Model approval workflow                                  │  │
│  │  - A/B testing support                                      │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │           SageMaker Endpoints (Auto-scaling)                │  │
│  │  ┌──────────────┐  ┌──────────────┐                        │  │
│  │  │  Model A     │  │  Model B     │  (A/B Testing)         │  │
│  │  │  (90% traffic│  │  (10% traffic│                        │  │
│  │  └──────────────┘  └──────────────┘                        │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              CloudWatch Monitoring                          │  │
│  │  - Endpoint metrics (latency, errors)                       │  │
│  │  - Model performance tracking                               │  │
│  │  - Data drift detection                                     │  │
│  │  - Automated alerts (SNS)                                   │  │
│  │  - Cost tracking                                            │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ API Requests
                              ▼
                       ┌──────────────┐
                       │   End Users  │
                       │  (REST API)  │
                       └──────────────┘
```

## Cloud Platform: AWS

We use **AWS** with the following services:
- **Amazon SageMaker**: End-to-end ML platform (training, hosting, monitoring)
- **Amazon S3**: Data lake and model registry
- **Amazon ECR**: Docker container registry
- **Amazon CloudWatch**: Monitoring and alerting
- **AWS Lambda**: Serverless data preprocessing
- **Amazon SNS**: Notification service
- **AWS IAM**: Security and access management

## Project Structure

```
13_mlops_cloud_pipeline/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .github/
│   └── workflows/
│       └── deploy.yml                 # CI/CD pipeline
├── terraform/
│   ├── main.tf                        # Main infrastructure config
│   ├── variables.tf                   # Terraform variables
│   └── outputs.tf                     # Output values
├── docker/
│   └── Dockerfile                     # Container for model serving
├── src/
│   ├── train.py                       # Model training script
│   ├── inference.py                   # Model inference script
│   └── preprocess.py                  # Data preprocessing
├── notebooks/
│   └── model_development.ipynb        # Exploratory model development
├── tests/
│   └── test_model.py                  # Unit tests for model
└── monitoring/
    └── cloudwatch_alarms.tf           # CloudWatch alarm configurations
```

## Step-by-Step Deployment Guide

### Prerequisites

1. **AWS Account** with appropriate permissions
2. **AWS CLI** configured with credentials
3. **Terraform** installed (v1.0+)
4. **Docker** installed
5. **Python 3.8+** with virtual environment
6. **Git** and **GitHub** account

### Step 1: Local Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd 13_mlops_cloud_pipeline

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure AWS Credentials

```bash
# Configure AWS CLI
aws configure

# Enter your credentials when prompted:
# AWS Access Key ID: [your-access-key]
# AWS Secret Access Key: [your-secret-key]
# Default region: us-east-1
# Default output format: json

# Verify configuration
aws sts get-caller-identity
```

### Step 3: Initialize Terraform

```bash
cd terraform

# Initialize Terraform
terraform init

# Review the infrastructure plan
terraform plan -var="project_name=mlops-sentiment" \
               -var="environment=dev"

# Apply the infrastructure
terraform apply -var="project_name=mlops-sentiment" \
                -var="environment=dev"
```

This creates:
- S3 buckets for data, models, and artifacts
- SageMaker execution role with necessary permissions
- CloudWatch log groups
- SNS topics for alerts

### Step 4: Develop and Test Model Locally

```bash
# Run the model development notebook
jupyter notebook notebooks/model_development.ipynb

# Train the model locally
python src/train.py --data-path data/sample/reviews.csv \
                    --output-path models/local/

# Test the model
python src/inference.py --model-path models/local/model.pkl \
                        --text "This product is amazing!"

# Run unit tests
pytest tests/
```

### Step 5: Build and Push Docker Container

```bash
# Get AWS account ID
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=us-east-1

# Create ECR repository
aws ecr create-repository --repository-name mlops-sentiment-model

# Build Docker image
cd docker
docker build -t mlops-sentiment-model:latest .

# Authenticate Docker to ECR
aws ecr get-login-password --region $AWS_REGION | \
    docker login --username AWS --password-stdin \
    $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Tag and push image
docker tag mlops-sentiment-model:latest \
    $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/mlops-sentiment-model:latest

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/mlops-sentiment-model:latest
```

### Step 6: Upload Training Data to S3

```bash
# Upload training data
aws s3 cp data/train/ s3://mlops-sentiment-data-dev/train/ --recursive

# Upload validation data
aws s3 cp data/val/ s3://mlops-sentiment-data-dev/val/ --recursive
```

### Step 7: Run SageMaker Training Job

```bash
# Train model on SageMaker
python src/train.py --cloud \
                    --s3-input s3://mlops-sentiment-data-dev/train/ \
                    --s3-output s3://mlops-sentiment-models-dev/ \
                    --instance-type ml.m5.xlarge \
                    --max-runtime 3600

# Monitor training job
aws sagemaker describe-training-job --training-job-name <job-name>
```

### Step 8: Register Model

```bash
# Register model in SageMaker Model Registry
aws sagemaker create-model-package \
    --model-package-group-name sentiment-analysis-models \
    --model-package-description "Sentiment classifier v1.0" \
    --inference-specification file://model-spec.json

# Approve model for deployment
aws sagemaker update-model-package \
    --model-package-arn <model-package-arn> \
    --model-approval-status Approved
```

### Step 9: Deploy Model to SageMaker Endpoint

```bash
# Deploy model to endpoint
aws sagemaker create-endpoint-config \
    --endpoint-config-name sentiment-endpoint-config \
    --production-variants file://production-variants.json

aws sagemaker create-endpoint \
    --endpoint-name sentiment-analysis-endpoint \
    --endpoint-config-name sentiment-endpoint-config

# Wait for endpoint to be in service
aws sagemaker wait endpoint-in-service \
    --endpoint-name sentiment-analysis-endpoint
```

### Step 10: Test Endpoint

```bash
# Test the deployed endpoint
python src/inference.py --endpoint sentiment-analysis-endpoint \
                        --text "This product exceeded my expectations!"

# Or use AWS CLI
aws sagemaker-runtime invoke-endpoint \
    --endpoint-name sentiment-analysis-endpoint \
    --body '{"text": "Great product!"}' \
    --content-type application/json \
    output.json
```

### Step 11: Configure Auto-scaling

```bash
# Register scalable target
aws application-autoscaling register-scalable-target \
    --service-namespace sagemaker \
    --resource-id endpoint/sentiment-analysis-endpoint/variant/AllTraffic \
    --scalable-dimension sagemaker:variant:DesiredInstanceCount \
    --min-capacity 1 \
    --max-capacity 5

# Create scaling policy
aws application-autoscaling put-scaling-policy \
    --policy-name sentiment-scaling-policy \
    --service-namespace sagemaker \
    --resource-id endpoint/sentiment-analysis-endpoint/variant/AllTraffic \
    --scalable-dimension sagemaker:variant:DesiredInstanceCount \
    --policy-type TargetTrackingScaling \
    --target-tracking-scaling-policy-configuration file://scaling-policy.json
```

### Step 12: Set Up Monitoring and Alerts

```bash
# Apply CloudWatch alarms
cd monitoring
terraform apply

# This creates alarms for:
# - High model latency (> 500ms)
# - High error rate (> 5%)
# - Low invocation count (data drift indicator)
# - Cost threshold exceeded
```

### Step 13: Configure CI/CD Pipeline

1. **Add GitHub Secrets**:
   - Go to repository Settings > Secrets and variables > Actions
   - Add the following secrets:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_REGION`

2. **Push to trigger deployment**:
```bash
git add .
git commit -m "Update model training script"
git push origin main

# GitHub Actions will automatically:
# - Run linting and tests
# - Build Docker image
# - Push to ECR
# - Trigger SageMaker training
# - Deploy to staging endpoint
# - (Manual approval required for production)
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) includes:

1. **Continuous Integration**:
   - Code linting (flake8, black)
   - Unit tests (pytest)
   - Integration tests
   - Security scanning (bandit)

2. **Continuous Deployment**:
   - Build Docker image
   - Push to Amazon ECR
   - Trigger SageMaker training job
   - Run model evaluation
   - Deploy to staging endpoint
   - Run smoke tests
   - (Manual approval for production)
   - Deploy to production endpoint
   - Update CloudWatch dashboards

3. **Rollback Strategy**:
   - Automatic rollback on high error rate
   - Manual rollback to previous model version
   - Traffic shifting for gradual deployment

## Infrastructure as Code (Terraform)

The Terraform configuration creates:

### S3 Buckets
- `mlops-sentiment-data-{env}`: Training/validation data
- `mlops-sentiment-models-{env}`: Model artifacts
- `mlops-sentiment-logs-{env}`: Logs and metrics

### IAM Roles
- SageMaker execution role with S3, CloudWatch, ECR permissions
- Lambda execution role for preprocessing

### SageMaker Resources
- Model package group for versioning
- Endpoint configurations
- Auto-scaling policies

### CloudWatch Resources
- Log groups for training jobs and endpoints
- Custom metrics for model performance
- Alarms for latency, errors, cost

### SNS Topics
- Alert notifications for production issues
- Model approval workflow notifications

## Monitoring and Logging

### Key Metrics Tracked

1. **Model Performance**:
   - Accuracy, Precision, Recall, F1-score
   - Prediction distribution
   - Confidence scores

2. **Operational Metrics**:
   - Invocations per minute
   - Model latency (p50, p90, p99)
   - Error rate (4xx, 5xx)
   - Instance CPU/memory utilization

3. **Data Quality**:
   - Input data drift detection
   - Feature distribution changes
   - Missing value rates

4. **Business Metrics**:
   - Daily active users
   - API call patterns
   - Cost per prediction

### CloudWatch Dashboards

Custom dashboards display:
- Real-time endpoint metrics
- Model performance trends
- Cost tracking
- Alert history

### Alerting Rules

Alerts trigger when:
- Latency > 500ms for 5 minutes
- Error rate > 5% for 3 minutes
- Zero invocations for 30 minutes (potential issue)
- Daily cost > threshold
- Data drift score > 0.3

## A/B Testing Setup

Deploy multiple model versions with traffic splitting:

```python
# production-variants.json
[
  {
    "VariantName": "ModelA",
    "ModelName": "sentiment-model-v1",
    "InitialInstanceCount": 2,
    "InstanceType": "ml.m5.large",
    "InitialVariantWeight": 0.9  # 90% traffic
  },
  {
    "VariantName": "ModelB",
    "ModelName": "sentiment-model-v2",
    "InitialInstanceCount": 1,
    "InstanceType": "ml.m5.large",
    "InitialVariantWeight": 0.1  # 10% traffic
  }
]
```

Monitor comparative metrics in CloudWatch to determine winner.

## Cost Optimization Strategies

1. **Right-sizing Instances**:
   - Use smaller instances for low-traffic endpoints
   - Scale down during off-peak hours
   - Use Spot instances for training jobs (up to 70% savings)

2. **Data Lifecycle Management**:
   - Archive old training data to S3 Glacier
   - Delete intermediate artifacts after 30 days
   - Compress logs before storage

3. **Endpoint Management**:
   - Delete unused endpoints
   - Use serverless inference for sporadic traffic
   - Implement auto-scaling to minimize idle capacity

4. **Training Optimization**:
   - Use SageMaker Managed Spot Training
   - Enable early stopping for hyperparameter tuning
   - Cache preprocessed data

5. **Monitoring Costs**:
   - Set billing alarms
   - Use AWS Cost Explorer for insights
   - Tag all resources for cost allocation

### Estimated Monthly Costs (Low Traffic)

| Service | Configuration | Estimated Cost |
|---------|--------------|----------------|
| SageMaker Endpoint | 1x ml.m5.large (24/7) | ~$125 |
| SageMaker Training | 2 jobs/month, ml.m5.xlarge | ~$5 |
| S3 Storage | 10 GB data + models | ~$1 |
| CloudWatch | Logs + metrics | ~$5 |
| Data Transfer | < 1 GB/month | ~$0 |
| **Total** | | **~$136/month** |

For higher traffic, costs scale with endpoint instances and auto-scaling.

## Data Drift Detection

Implement monitoring for input data changes:

```python
# Monitor feature statistics
from scipy.stats import ks_2samp

def detect_drift(reference_data, current_data, threshold=0.05):
    """Kolmogorov-Smirnov test for distribution drift"""
    statistic, p_value = ks_2samp(reference_data, current_data)

    drift_detected = p_value < threshold
    return drift_detected, statistic, p_value
```

Set up CloudWatch custom metrics to track drift scores and trigger retraining when drift is detected.

## Model Versioning and Rollback

### Version Control
- Models are versioned in SageMaker Model Registry
- Each version tagged with:
  - Training date
  - Git commit SHA
  - Performance metrics
  - Approval status

### Rollback Procedure

```bash
# List model versions
aws sagemaker list-model-packages \
    --model-package-group-name sentiment-analysis-models

# Rollback to previous version
aws sagemaker update-endpoint \
    --endpoint-name sentiment-analysis-endpoint \
    --endpoint-config-name sentiment-endpoint-config-v1

# Monitor rollback
aws sagemaker describe-endpoint \
    --endpoint-name sentiment-analysis-endpoint
```

## Automated Retraining Pipeline

Trigger retraining when:
1. **Scheduled**: Weekly/monthly retraining
2. **Performance degradation**: Accuracy drops below threshold
3. **Data drift**: Input distribution changes significantly
4. **Manual trigger**: New training data available

```python
# Lambda function for scheduled retraining
def lambda_handler(event, context):
    """Trigger SageMaker training job"""
    sagemaker_client = boto3.client('sagemaker')

    response = sagemaker_client.create_training_job(
        TrainingJobName=f"sentiment-training-{timestamp}",
        AlgorithmSpecification={...},
        RoleArn=os.environ['SAGEMAKER_ROLE'],
        InputDataConfig=[...],
        OutputDataConfig={...},
        ResourceConfig={...}
    )

    return response
```

## Security Best Practices

1. **IAM Permissions**: Principle of least privilege
2. **Encryption**: Data encrypted at rest (S3) and in transit (HTTPS)
3. **VPC Configuration**: Deploy endpoints in private VPC
4. **Secret Management**: Use AWS Secrets Manager for credentials
5. **Audit Logging**: Enable CloudTrail for all API calls
6. **Model Validation**: Validate inputs to prevent injection attacks

## Troubleshooting

### Common Issues

**Training job fails**:
- Check CloudWatch logs: `/aws/sagemaker/TrainingJobs`
- Verify S3 permissions
- Confirm instance type availability in region

**Endpoint deployment timeout**:
- Check Docker container health check
- Verify model artifacts are in S3
- Review endpoint CloudWatch logs

**High latency**:
- Enable auto-scaling
- Use larger instance types
- Optimize model inference code
- Check network configuration

**Cost higher than expected**:
- Review CloudWatch cost metrics
- Check for orphaned endpoints
- Verify auto-scaling is working
- Consider spot instances

## Next Steps

1. **Production Readiness**:
   - Load testing with realistic traffic
   - Disaster recovery planning
   - Multi-region deployment for high availability

2. **Advanced Features**:
   - Multi-model endpoints (serve multiple models on one endpoint)
   - SageMaker Pipelines for end-to-end workflow
   - SageMaker Model Monitor for automated drift detection
   - Integration with data versioning (DVC)

3. **Optimization**:
   - Model compression and quantization
   - Batch transform for bulk predictions
   - Serverless inference for intermittent traffic
   - Edge deployment with SageMaker Neo

## Learning Resources

- [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [MLOps Best Practices](https://ml-ops.org/)
- [SageMaker Examples](https://github.com/aws/amazon-sagemaker-examples)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [GitHub Actions for AWS](https://github.com/aws-actions)

## Conclusion

This project demonstrates a production-grade MLOps pipeline with:
- ✅ Automated CI/CD
- ✅ Infrastructure as Code
- ✅ Model versioning and registry
- ✅ A/B testing capabilities
- ✅ Comprehensive monitoring
- ✅ Auto-scaling
- ✅ Cost optimization
- ✅ Data drift detection

You now have the skills to deploy and maintain ML models at enterprise scale!
