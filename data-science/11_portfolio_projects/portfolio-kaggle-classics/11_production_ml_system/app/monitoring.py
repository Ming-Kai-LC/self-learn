"""
Prometheus metrics for monitoring ML API
Tracks: requests, latency, predictions, errors, model drift indicators
"""

from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response
import time

# Request metrics
request_count = Counter(
    'ml_api_requests_total',
    'Total number of API requests',
    ['endpoint', 'method', 'status']
)

# Latency metrics
request_latency = Histogram(
    'ml_api_request_latency_seconds',
    'API request latency in seconds',
    ['endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0]
)

prediction_latency = Histogram(
    'ml_prediction_latency_seconds',
    'Model prediction latency in seconds',
    buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
)

# Prediction metrics
predictions_total = Counter(
    'ml_predictions_total',
    'Total number of predictions made',
    ['model_version']
)

prediction_distribution = Histogram(
    'ml_prediction_values',
    'Distribution of prediction values',
    buckets=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
)

# Model drift metrics
prediction_mean = Gauge(
    'ml_prediction_mean',
    'Rolling mean of predictions',
    ['model_version']
)

prediction_std = Gauge(
    'ml_prediction_std',
    'Rolling standard deviation of predictions',
    ['model_version']
)

# Error metrics
prediction_errors = Counter(
    'ml_prediction_errors_total',
    'Total number of prediction errors',
    ['error_type']
)

# Cache metrics
cache_hits = Counter(
    'ml_cache_hits_total',
    'Total number of cache hits'
)

cache_misses = Counter(
    'ml_cache_misses_total',
    'Total number of cache misses'
)


def metrics_endpoint():
    """
    FastAPI endpoint handler for Prometheus metrics
    Returns metrics in Prometheus format
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


class MetricsMiddleware:
    """
    Middleware to automatically track request metrics
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        start_time = time.time()

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                # Track request count and latency
                latency = time.time() - start_time
                endpoint = scope["path"]
                method = scope["method"]
                status = message["status"]

                request_count.labels(
                    endpoint=endpoint,
                    method=method,
                    status=status
                ).inc()

                request_latency.labels(endpoint=endpoint).observe(latency)

            await send(message)

        await self.app(scope, receive, send_wrapper)
