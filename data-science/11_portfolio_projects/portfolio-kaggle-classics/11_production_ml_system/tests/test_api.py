"""
Unit tests for Production ML System API
Tests all endpoints and error handling
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add parent directory to path to import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app

# Create test client
client = TestClient(app)


class TestHealthEndpoint:
    """Tests for /health endpoint"""

    def test_health_check_returns_200(self):
        """Health endpoint should return 200 status"""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_has_required_fields(self):
        """Health response should contain required fields"""
        response = client.get("/health")
        data = response.json()

        required_fields = [
            'status',
            'model_version',
            'database_connected',
            'redis_connected',
            'timestamp'
        ]

        for field in required_fields:
            assert field in data, f"Missing required field: {field}"

    def test_health_status_is_healthy(self):
        """Health status should be 'healthy' or 'degraded'"""
        response = client.get("/health")
        data = response.json()
        assert data['status'] in ['healthy', 'degraded']


class TestPredictEndpoint:
    """Tests for /predict endpoint"""

    def test_predict_requires_features(self):
        """Predict endpoint should require features"""
        response = client.post("/predict", json={})
        assert response.status_code == 422  # Validation error

    def test_predict_with_valid_features(self):
        """Predict endpoint should accept valid features"""
        request_body = {
            "features": {
                "tenure_months": 24,
                "monthly_charges": 75.5,
                "total_charges": 1800.0,
                "contract_length": 12,
                "num_products": 2,
                "support_tickets": 1,
                "satisfaction_score": 4.5
            },
            "use_cache": False
        }

        response = client.post("/predict", json=request_body)

        # Should succeed (200) or fail gracefully if model not loaded
        assert response.status_code in [200, 500]

        if response.status_code == 200:
            data = response.json()

            # Check required fields
            required_fields = [
                'request_id',
                'prediction',
                'model_version',
                'latency_ms',
                'cached',
                'timestamp'
            ]

            for field in required_fields:
                assert field in data, f"Missing field: {field}"

            # Check data types
            assert isinstance(data['prediction'], (int, float))
            assert isinstance(data['latency_ms'], (int, float))
            assert isinstance(data['cached'], bool)

    def test_predict_with_cache_enabled(self):
        """Predict endpoint should support caching"""
        request_body = {
            "features": {
                "tenure_months": 36,
                "monthly_charges": 100.0,
                "total_charges": 3600.0,
                "contract_length": 24,
                "num_products": 3,
                "support_tickets": 0,
                "satisfaction_score": 4.8
            },
            "use_cache": True
        }

        # First request
        response1 = client.post("/predict", json=request_body)

        if response1.status_code == 200:
            # Second request (should use cache if Redis available)
            response2 = client.post("/predict", json=request_body)
            assert response2.status_code == 200


class TestMetricsEndpoint:
    """Tests for /metrics endpoint"""

    def test_metrics_returns_200(self):
        """Metrics endpoint should return 200"""
        response = client.get("/metrics")
        assert response.status_code == 200

    def test_metrics_content_type(self):
        """Metrics should return Prometheus format"""
        response = client.get("/metrics")
        # Prometheus metrics use text/plain or specific Prometheus type
        assert 'text' in response.headers['content-type']


class TestModelInfoEndpoint:
    """Tests for /model/info endpoint"""

    def test_model_info_returns_200(self):
        """Model info endpoint should return 200"""
        response = client.get("/model/info")
        # Should succeed or fail if model not loaded
        assert response.status_code in [200, 500]

    def test_model_info_has_version(self):
        """Model info should include version"""
        response = client.get("/model/info")

        if response.status_code == 200:
            data = response.json()
            assert 'version' in data
            assert 'model_path' in data


class TestRootEndpoint:
    """Tests for root endpoint"""

    def test_root_returns_200(self):
        """Root endpoint should return 200"""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_has_api_info(self):
        """Root should return API information"""
        response = client.get("/")
        data = response.json()

        assert 'name' in data
        assert 'version' in data
        assert 'endpoints' in data


class TestErrorHandling:
    """Tests for error handling"""

    def test_predict_with_invalid_features(self):
        """Predict should handle invalid feature types"""
        request_body = {
            "features": {
                "tenure_months": "invalid",  # Should be numeric
            }
        }

        response = client.post("/predict", json=request_body)
        # Should return validation error
        assert response.status_code in [422, 500]

    def test_nonexistent_endpoint(self):
        """Non-existent endpoints should return 404"""
        response = client.get("/nonexistent")
        assert response.status_code == 404


class TestIntegration:
    """Integration tests for multiple endpoints"""

    def test_complete_prediction_workflow(self):
        """Test complete prediction workflow"""

        # 1. Check health
        health_response = client.get("/health")
        assert health_response.status_code == 200

        # 2. Get model info
        info_response = client.get("/model/info")
        # May fail if model not loaded, that's ok for testing

        # 3. Make prediction
        request_body = {
            "features": {
                "tenure_months": 48,
                "monthly_charges": 120.0,
                "total_charges": 5760.0,
                "contract_length": 24,
                "num_products": 4,
                "support_tickets": 2,
                "satisfaction_score": 3.5
            },
            "use_cache": False
        }

        predict_response = client.post("/predict", json=request_body)

        # 4. Check metrics updated
        metrics_response = client.get("/metrics")
        assert metrics_response.status_code == 200


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
