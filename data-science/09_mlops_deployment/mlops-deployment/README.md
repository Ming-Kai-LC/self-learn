# MLOps and Deployment

**Status**: ✅ Complete - All 15 modules ready
**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 60-80 hours
**Roadmap Alignment**: Advanced Phase (Months 10-12)

## Overview

This project covers MLOps practices and model deployment techniques. According to the DataScience_SelfLearnPath.md: **"MLOps expertise makes you invaluable. Only 30% of ML models ever reach production"** and **"MLOps and deployment skills separate academic data scientists from industry professionals."**

## Learning Objectives

By completing this project, you will be able to:

1. **Containerization**
   - Build Docker containers for ML applications
   - Create reproducible environments
   - Use Docker Compose for multi-container apps
   - Optimize container images

2. **Orchestration**
   - Deploy with Kubernetes basics
   - Use Helm charts
   - Manage ML workloads at scale
   - Implement auto-scaling

3. **Experiment Tracking**
   - Track experiments with MLflow
   - Use Weights & Biases
   - Version models and datasets
   - Compare experiment runs

4. **Model Deployment**
   - Deploy with FastAPI and Flask
   - Create REST APIs for models
   - Implement batch prediction
   - Deploy with Streamlit for demos

5. **CI/CD for ML**
   - Set up GitHub Actions workflows
   - Automate testing and deployment
   - Implement model validation pipelines
   - Monitor model performance

6. **Monitoring and Maintenance**
   - Monitor model performance in production
   - Detect model drift
   - Implement retraining pipelines
   - Set up alerting systems

## Prerequisites

- **machine-learning-fundamentals** (ML model building)
- **deep-learning-fundamentals** (optional, for DL deployment)
- Basic command-line and Git knowledge

## Planned Content Structure

### Module 00: Introduction to MLOps
- What is MLOps?
- ML lifecycle overview
- DevOps vs MLOps
- MLOps maturity model

### Module 01: Docker Fundamentals
- Docker basics and architecture
- Creating Dockerfiles
- Building ML containers
- Docker Compose
- Best practices for ML images

### Module 02: Experiment Tracking with MLflow
- MLflow Tracking
- MLflow Projects
- MLflow Models
- Model Registry
- Integration with existing workflows

### Module 03: Model Serving
- FastAPI for ML APIs
- Flask alternatives
- Request/response handling
- Input validation
- Error handling

### Module 04: Streamlit for ML Apps
- Building interactive ML apps
- Dashboards and visualizations
- User input handling
- Deployment considerations

### Module 05: Kubernetes for ML
- Kubernetes basics
- Deploying ML models
- Scaling strategies
- Resource management
- Helm charts for ML

### Module 06: CI/CD Pipelines
- GitHub Actions for ML
- Automated testing
- Model validation gates
- Automated deployment
- Rolling updates

### Module 07: Monitoring and Observability
- Performance monitoring
- Model drift detection
- Data drift detection
- Logging and alerting
- Prometheus and Grafana

### Module 08: Advanced Topics
- A/B testing for models
- Shadow deployments
- Canary releases
- Model versioning strategies
- Multi-model serving

### Module 09: Final Project
- End-to-end MLOps pipeline
- From training to production
- Monitoring and maintenance
- Documentation and handoff

## Recommended Learning Resources

### Primary Resources
- **MLflow documentation**
- **Docker official tutorials**
- **Kubernetes documentation**
- **AWS MLOps Engineering on AWS** (3-day training)

### Supplementary Resources
- **"Designing Machine Learning Systems"** by Chip Huyen
- **"Machine Learning Engineering"** by Andriy Burkov
- **Full Stack Deep Learning** course (free)
- **Made With ML** MLOps course

## Key Technologies

- **Docker**: Containerization (essential)
- **Kubernetes**: Orchestration (increasingly common)
- **MLflow**: Experiment tracking and model registry
- **Weights & Biases**: Alternative to MLflow
- **FastAPI/Flask**: Model serving
- **GitHub Actions/GitLab CI**: CI/CD pipelines
- **Prometheus/Grafana**: Monitoring

## Time Allocation

- **Weeks 1-2**: Docker and containerization (12-15 hours)
- **Weeks 3-4**: MLflow and experiment tracking (12-15 hours)
- **Weeks 5-6**: Model serving (FastAPI, Streamlit) (12-15 hours)
- **Weeks 7-8**: Kubernetes and orchestration (12-15 hours)
- **Weeks 9-10**: CI/CD and monitoring (12-15 hours)
- **Weeks 11-12**: Final project (12-15 hours)

Total: 12 weeks at 10-12 hours per week

## Success Criteria

You're ready to move on when you can:
- Containerize ML applications with Docker
- Deploy models as APIs with FastAPI
- Track experiments systematically with MLflow
- Set up CI/CD pipelines for ML
- Monitor model performance in production
- Implement model retraining workflows
- Understand Kubernetes basics for ML deployment

## Next Steps

After completing this project, proceed to:
- **cloud-platforms** (cloud-specific MLOps services)
- Apply MLOps practices to all future ML projects
- Consider cloud certifications (AWS ML Specialty, Azure DP-100)

## Project Status

This project is complete with:
- [x] 15 comprehensive Jupyter notebooks (Modules 00-14)
- [x] Docker examples and Dockerfiles (simple and optimized)
- [x] Docker Compose for full stack setup
- [x] MLflow tracking examples throughout
- [x] FastAPI model serving templates and production examples
- [x] GitHub Actions workflow examples (CI/CD and auto-retraining)
- [x] Prometheus configuration for monitoring
- [x] Complete end-to-end pipeline example (Module 14)
- [x] Batch inference and monitoring scripts
- [x] Best practices and anti-patterns documentation

## What's Included

### 📓 Notebooks (15 modules)

All notebooks in `notebooks/` directory:

**Foundation (Modules 00-04)**
- `00_introduction_to_mlops_and_ml_lifecycle.ipynb` - MLOps overview, lifecycle, maturity model
- `01_experiment_tracking_with_mlflow.ipynb` - MLflow tracking, logging, comparison
- `02_model_versioning_and_registry.ipynb` - Model registry, lifecycle management
- `03_model_serialization.ipynb` - Pickle, joblib, ONNX serialization
- `04_creating_ml_apis_with_fastapi.ipynb` - REST APIs, validation, documentation

**Deployment (Modules 05-07)**
- `05_containerization_with_docker.ipynb` - Dockerfiles, optimization, Docker Compose
- `06_model_serving_patterns.ipynb` - Batch, real-time, streaming patterns
- `07_model_monitoring_and_logging.ipynb` - Logging, Prometheus, alerting

**Advanced Operations (Modules 08-11)**
- `08_data_drift_detection.ipynb` - Drift types, Evidently, statistical tests
- `09_model_retraining_pipelines.ipynb` - Automation, triggers, validation
- `10_cicd_for_ml_with_github_actions.ipynb` - Workflows, testing, deployment
- `11_ab_testing_and_model_evaluation.ipynb` - A/B testing, statistical significance

**Integration (Modules 12-14)**
- `12_infrastructure_as_code_basics.ipynb` - IaC principles, reproducibility
- `13_mlops_best_practices_and_antipatterns.ipynb` - Common pitfalls, checklists
- `14_final_project_end_to_end_mlops_pipeline.ipynb` - Complete integration project

### 🐳 Docker Examples

In `docker/` directory:
- `Dockerfile.simple` - Basic ML model serving
- `Dockerfile.optimized` - Production-ready multi-stage build
- `docker-compose.yml` - Full stack (API + MLflow + Prometheus + Grafana)
- `.dockerignore` - Optimized build context

### 🔧 CI/CD Examples

In `ci-cd/` directory:
- `ml-ci-cd.yml` - Complete ML CI/CD pipeline
- `model-retraining.yml` - Scheduled retraining workflow
- `prometheus.yml` - Prometheus monitoring configuration

### 💻 Production Examples

In `examples/` directory:
- `fastapi_app.py` - Production FastAPI application with monitoring
- `batch_inference.py` - Batch prediction script
- `model_monitoring.py` - Performance monitoring and alerting

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start with Module 00

```bash
jupyter notebook notebooks/00_introduction_to_mlops_and_ml_lifecycle.ipynb
```

### 3. Progress Through Modules Sequentially

Each module builds on previous concepts and includes:
- Clear learning objectives
- Comprehensive explanations (30%+ markdown)
- Executable code examples
- Hands-on exercises
- Summary and next steps

### 4. Try the Production Examples

**Run FastAPI Application:**
```bash
cd examples/
uvicorn fastapi_app:app --reload
# Visit http://localhost:8000/docs for interactive API documentation
```

**Run Batch Inference:**
```bash
python batch_inference.py --input data.csv --output predictions.csv --model model.pkl
```

**Monitor Model Performance:**
```bash
python model_monitoring.py --predictions predictions.csv --ground-truth labels.csv
```

### 5. Deploy with Docker

**Single Container:**
```bash
docker build -f docker/Dockerfile.optimized -t ml-model:latest .
docker run -p 8000:8000 ml-model:latest
```

**Full Stack:**
```bash
cd docker/
docker-compose up
# Access:
# - API: http://localhost:8000
# - MLflow: http://localhost:5000
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000
```

## References

- DataScience_SelfLearnPath.md - Advanced Expertise (Months 10-12)
- MLflow documentation: https://mlflow.org/docs/latest/index.html
- Docker documentation: https://docs.docker.com/
- Kubernetes documentation: https://kubernetes.io/docs/
- FastAPI documentation: https://fastapi.tiangolo.com/
