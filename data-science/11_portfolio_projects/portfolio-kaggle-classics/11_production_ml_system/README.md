# Project 11: Production ML System with Monitoring

**Difficulty**: ⭐⭐⭐ Advanced
**Domain**: MLOps, Production Machine Learning, System Design

## Problem Statement

Deploy a production-grade machine learning system that goes beyond model training to include:
- Model versioning and tracking
- Real-time predictions via REST API
- Request/response logging
- Performance monitoring
- Caching for improved latency
- Automated testing
- Containerized deployment

This project demonstrates end-to-end MLOps capabilities essential for deploying ML models in production environments.

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Production ML System                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐   ┌──────────┐   │
│  │  Client  │───▶│ FastAPI  │───▶│  Model   │   │  Redis   │   │
│  │ Request  │    │   API    │    │ (Scikit) │   │  Cache   │   │
│  └──────────┘    └────┬─────┘    └──────────┘   └──────────┘   │
│                       │                                           │
│                       ├──────────▶ PostgreSQL (Logging)          │
│                       │                                           │
│                       ├──────────▶ MLflow (Versioning)           │
│                       │                                           │
│                       └──────────▶ Prometheus (Metrics)          │
│                                          │                        │
│                                          ▼                        │
│                                    Grafana (Visualization)        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Features

### 🚀 Core ML Features
- **Model Training**: Jupyter notebook with MLflow tracking
- **REST API**: FastAPI with automatic documentation
- **Predictions**: Real-time inference with probability scores
- **Versioning**: Model versioning with MLflow
- **Hot Reload**: Update models without restarting service

### 📊 Monitoring & Observability
- **Prometheus Metrics**: Request rate, latency, throughput, errors
- **Grafana Dashboards**: Real-time visualization
- **Model Drift Detection**: Track prediction distribution changes
- **Health Checks**: Database and cache connectivity monitoring

### ⚡ Performance
- **Redis Caching**: Cache predictions for repeated requests
- **PostgreSQL Logging**: Store all predictions for audit/analysis
- **Async Operations**: Background logging to minimize latency
- **Load Balancing Ready**: Stateless design for horizontal scaling

### 🧪 Testing & Quality
- **Unit Tests**: Comprehensive API testing with pytest
- **Integration Tests**: Full workflow testing
- **Error Handling**: Graceful degradation when services unavailable
- **Input Validation**: Pydantic models for request validation

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| API Framework | FastAPI | High-performance REST API |
| ML Framework | Scikit-learn | Model training and inference |
| Model Tracking | MLflow | Experiment tracking and versioning |
| Database | PostgreSQL | Request/response logging |
| Caching | Redis | Low-latency prediction caching |
| Monitoring | Prometheus | Metrics collection |
| Visualization | Grafana | Dashboard and alerting |
| Containerization | Docker Compose | Multi-service orchestration |
| Testing | Pytest | Unit and integration testing |

## Project Structure

```
11_production_ml_system/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Multi-service orchestration
├── Dockerfile                  # API container definition
│
├── app/                        # FastAPI application
│   ├── __init__.py
│   ├── main.py                 # API endpoints and routing
│   ├── model.py                # Model loading and prediction
│   ├── database.py             # PostgreSQL connection
│   └── monitoring.py           # Prometheus metrics
│
├── models/                     # Trained model artifacts
│   └── model.pkl              # Serialized model (created by notebook)
│
├── notebooks/                  # Training notebooks
│   └── model_training.ipynb   # Train model with MLflow
│
├── tests/                      # Test suite
│   ├── __init__.py
│   └── test_api.py            # API unit tests
│
└── monitoring/                 # Monitoring configuration
    ├── prometheus.yml          # Prometheus scrape config
    └── grafana_dashboard.json  # Pre-built dashboard
```

## Installation and Setup

### Prerequisites

- Docker and Docker Compose installed
- Python 3.10+ (for local development)
- 4GB RAM minimum for running all services

### Quick Start

1. **Clone the repository**
   ```bash
   cd data-science/11_portfolio_projects/portfolio-kaggle-classics/11_production_ml_system
   ```

2. **Train the model**
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Run training notebook
   jupyter notebook notebooks/model_training.ipynb

   # Execute all cells to train and save model to models/model.pkl
   ```

3. **Start all services**
   ```bash
   docker-compose up --build
   ```

   This starts:
   - FastAPI on http://localhost:8000
   - PostgreSQL on port 5432
   - Redis on port 6379
   - MLflow on http://localhost:5000
   - Prometheus on http://localhost:9090
   - Grafana on http://localhost:3000

4. **Verify services are running**
   ```bash
   curl http://localhost:8000/health
   ```

### Manual Setup (Without Docker)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start PostgreSQL and Redis**
   ```bash
   # Using your preferred method (Docker, local install, etc.)
   ```

3. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### `GET /`
Root endpoint with API information.

**Response:**
```json
{
  "name": "Production ML System",
  "version": "1.0.0",
  "endpoints": {...}
}
```

#### `POST /predict`
Make a prediction with the ML model.

**Request:**
```json
{
  "features": {
    "tenure_months": 24,
    "monthly_charges": 75.5,
    "total_charges": 1800.0,
    "contract_length": 12,
    "num_products": 2,
    "support_tickets": 1,
    "satisfaction_score": 4.5
  },
  "use_cache": true
}
```

**Response:**
```json
{
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "prediction": 0,
  "probability": 0.1234,
  "model_version": "v1.0",
  "latency_ms": 5.23,
  "cached": false,
  "timestamp": "2025-11-20T10:30:00"
}
```

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "model_version": "v1.0",
  "database_connected": true,
  "redis_connected": true,
  "timestamp": "2025-11-20T10:30:00"
}
```

#### `GET /metrics`
Prometheus metrics in text format.

**Response:**
```
# HELP ml_predictions_total Total number of predictions made
# TYPE ml_predictions_total counter
ml_predictions_total{model_version="v1.0"} 1234.0
...
```

#### `GET /model/info`
Get loaded model information.

**Response:**
```json
{
  "version": "v1.0",
  "model_path": "models/model.pkl",
  "feature_names": ["tenure_months", "monthly_charges", ...],
  "feature_count": 7,
  "drift_metrics": {
    "mean": 0.4567,
    "std": 0.2345,
    "count": 1000
  }
}
```

#### `POST /model/reload`
Reload model from disk (hot reload).

**Response:**
```json
{
  "status": "success",
  "message": "Model reloaded successfully"
}
```

## Usage Examples

### Python Client

```python
import requests

# Make a prediction
url = "http://localhost:8000/predict"
data = {
    "features": {
        "tenure_months": 36,
        "monthly_charges": 89.99,
        "total_charges": 3240.0,
        "contract_length": 24,
        "num_products": 3,
        "support_tickets": 0,
        "satisfaction_score": 4.8
    },
    "use_cache": True
}

response = requests.post(url, json=data)
result = response.json()

print(f"Prediction: {result['prediction']}")
print(f"Probability: {result['probability']:.2%}")
print(f"Latency: {result['latency_ms']:.2f}ms")
```

### cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": {
      "tenure_months": 48,
      "monthly_charges": 120.0,
      "total_charges": 5760.0,
      "contract_length": 24,
      "num_products": 4,
      "support_tickets": 2,
      "satisfaction_score": 3.5
    },
    "use_cache": false
  }'
```

## Monitoring and Observability

### Prometheus

Access at http://localhost:9090

**Key Metrics:**
- `ml_api_requests_total` - Total API requests by endpoint
- `ml_api_request_latency_seconds` - Request latency histogram
- `ml_predictions_total` - Total predictions made
- `ml_prediction_latency_seconds` - Model inference latency
- `ml_prediction_mean` - Rolling mean of predictions (drift detection)
- `ml_prediction_errors_total` - Prediction errors
- `ml_cache_hits_total` / `ml_cache_misses_total` - Cache performance

**Example Queries:**
```promql
# Request rate
rate(ml_api_requests_total[5m])

# P95 latency
histogram_quantile(0.95, rate(ml_api_request_latency_seconds_bucket[5m]))

# Cache hit rate
ml_cache_hits_total / (ml_cache_hits_total + ml_cache_misses_total)
```

### Grafana

Access at http://localhost:3000
**Default credentials**: admin / admin

**Pre-configured Dashboard includes:**
- API request rate and latency
- Prediction throughput
- Cache hit rate
- Error rates
- Prediction distribution
- Model drift indicators

**Setting up the dashboard:**
1. Login to Grafana
2. Add Prometheus data source: http://prometheus:9090
3. Import dashboard from `monitoring/grafana_dashboard.json`

### MLflow

Access at http://localhost:5000

**Features:**
- View all training experiments
- Compare model metrics
- Track parameters and artifacts
- Model registry

## Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Classes

```bash
# Test health endpoint
pytest tests/test_api.py::TestHealthEndpoint -v

# Test predictions
pytest tests/test_api.py::TestPredictEndpoint -v
```

### Test Coverage

```bash
pytest tests/ --cov=app --cov-report=html
```

## Performance Benchmarking

### Load Testing with Locust

```python
from locust import HttpUser, task, between

class MLAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def predict(self):
        self.client.post("/predict", json={
            "features": {
                "tenure_months": 24,
                "monthly_charges": 75.5,
                "total_charges": 1800.0,
                "contract_length": 12,
                "num_products": 2,
                "support_tickets": 1,
                "satisfaction_score": 4.5
            }
        })
```

Run: `locust -f locustfile.py --host=http://localhost:8000`

### Expected Performance

- **Latency**: <10ms (cached), <50ms (uncached)
- **Throughput**: 100+ req/s on single instance
- **Cache Hit Rate**: 60-80% in typical workloads

## Model Deployment Workflow

### 1. Train New Model

```bash
jupyter notebook notebooks/model_training.ipynb
# Train model, save to models/model.pkl
```

### 2. Test Locally

```bash
python -c "from app.model import MLModel; m = MLModel(); print(m.predict({'tenure_months': 24, ...}))"
```

### 3. Deploy to Production

**Option A: Hot Reload (No Downtime)**
```bash
# Copy new model to production
cp models/model_new.pkl models/model.pkl

# Reload via API
curl -X POST http://localhost:8000/model/reload
```

**Option B: Full Restart**
```bash
docker-compose restart api
```

### 4. Verify Deployment

```bash
# Check new version is loaded
curl http://localhost:8000/model/info

# Test prediction
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '...'
```

### 5. Monitor Performance

- Check Grafana dashboards for anomalies
- Monitor prediction distribution for drift
- Review error rates in Prometheus

## Troubleshooting

### Model Not Loading

**Error**: `FileNotFoundError: Model file not found`

**Solution**: Train model first using `notebooks/model_training.ipynb`

### Database Connection Failed

**Error**: `database_connected: false` in health check

**Solution**:
```bash
# Check PostgreSQL is running
docker-compose ps postgres

# View logs
docker-compose logs postgres
```

### Redis Not Available

**Error**: `redis_connected: false` in health check

**Solution**: API continues to work but without caching. Redis is optional.
```bash
# Check Redis
docker-compose ps redis
docker-compose logs redis
```

### High Latency

**Causes**:
- Database logging overhead
- Model complexity
- No caching (Redis down)

**Solutions**:
- Enable Redis caching
- Use background tasks for logging
- Consider model optimization

### Prometheus Not Scraping

**Check**:
1. Prometheus config: `monitoring/prometheus.yml`
2. API metrics endpoint: http://localhost:8000/metrics
3. Prometheus targets: http://localhost:9090/targets

## Production Considerations

### Security
- [ ] Add authentication (JWT, API keys)
- [ ] Enable HTTPS/TLS
- [ ] Sanitize inputs for SQL injection
- [ ] Rate limiting
- [ ] CORS configuration

### Scalability
- [ ] Horizontal scaling (multiple API instances)
- [ ] Load balancer (Nginx, HAProxy)
- [ ] Database connection pooling
- [ ] Redis cluster for high availability
- [ ] Model serving optimization (ONNX, TensorRT)

### Monitoring
- [ ] Alert rules in Prometheus
- [ ] Log aggregation (ELK, Loki)
- [ ] Distributed tracing (Jaeger, Zipkin)
- [ ] Error tracking (Sentry)

### CI/CD
- [ ] Automated testing on commit
- [ ] Docker image build pipeline
- [ ] Blue-green deployment
- [ ] Canary releases
- [ ] Rollback procedures

## Learning Outcomes

After completing this project, you will understand:

✅ **MLOps Best Practices**
- Model versioning and tracking
- Production deployment patterns
- Monitoring and observability

✅ **System Design**
- Microservices architecture
- Caching strategies
- Asynchronous processing

✅ **API Development**
- REST API design
- Input validation
- Error handling
- Documentation

✅ **DevOps Skills**
- Docker containerization
- Multi-service orchestration
- Configuration management

✅ **Performance Engineering**
- Latency optimization
- Caching strategies
- Load testing

## Next Steps

### Enhancements
1. **A/B Testing**: Deploy multiple model versions simultaneously
2. **Feature Store**: Centralized feature management
3. **Real-time Retraining**: Automated model updates
4. **Advanced Monitoring**: Drift detection, data quality checks
5. **Model Explainability**: SHAP, LIME integration

### Alternative Models
- Replace with deep learning model (TensorFlow, PyTorch)
- Use different ML tasks (regression, multi-class classification)
- Implement ensemble models

### Scaling
- Deploy on Kubernetes
- Add message queue (RabbitMQ, Kafka)
- Implement batch prediction API
- Add model serving (TensorFlow Serving, Seldon)

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/naming/)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [Docker Compose](https://docs.docker.com/compose/)

## License

This project is part of the Data Science Portfolio and is available for educational purposes.

---

**Project Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 8-12 hours
**Prerequisites**: Python, ML basics, Docker, REST APIs

*Part of the Data Science Portfolio - Project 11*
