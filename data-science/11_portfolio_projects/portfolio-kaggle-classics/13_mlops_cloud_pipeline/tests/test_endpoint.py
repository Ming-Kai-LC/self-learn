"""
Endpoint tests for SageMaker deployment

Tests the deployed model endpoint for functionality and performance.

Usage:
    python tests/test_endpoint.py --endpoint sentiment-analysis-production
"""

import argparse
import json
import time
from typing import Dict, List

import boto3
import requests


class EndpointTester:
    """Test deployed SageMaker endpoint"""

    def __init__(self, endpoint_name: str, region: str = "us-east-1"):
        """
        Initialize endpoint tester

        Args:
            endpoint_name: Name of SageMaker endpoint
            region: AWS region
        """
        self.endpoint_name = endpoint_name
        self.region = region
        self.runtime_client = boto3.client("sagemaker-runtime", region_name=region)
        self.sagemaker_client = boto3.client("sagemaker", region_name=region)

    def check_endpoint_status(self) -> Dict:
        """
        Check endpoint status

        Returns:
            Endpoint status information
        """
        print(f"\nChecking endpoint status: {self.endpoint_name}")

        try:
            response = self.sagemaker_client.describe_endpoint(
                EndpointName=self.endpoint_name
            )

            status = {
                "name": response["EndpointName"],
                "status": response["EndpointStatus"],
                "creation_time": str(response["CreationTime"]),
                "last_modified": str(response["LastModifiedTime"]),
            }

            print(f"✓ Endpoint Status: {status['status']}")
            print(f"  Created: {status['creation_time']}")
            print(f"  Modified: {status['last_modified']}")

            return status

        except Exception as e:
            print(f"✗ Error checking endpoint: {e}")
            raise

    def test_single_prediction(self, text: str) -> Dict:
        """
        Test single text prediction

        Args:
            text: Input text to classify

        Returns:
            Prediction result
        """
        print(f"\n--- Single Prediction Test ---")
        print(f"Input: {text}")

        payload = json.dumps({"text": text})

        try:
            start_time = time.time()

            response = self.runtime_client.invoke_endpoint(
                EndpointName=self.endpoint_name,
                ContentType="application/json",
                Body=payload,
            )

            latency = (time.time() - start_time) * 1000  # Convert to ms

            result = json.loads(response["Body"].read().decode())

            print(f"✓ Prediction: {result['prediction']}")
            print(f"  Confidence: {result['confidence']:.2%}")
            print(f"  Latency: {latency:.2f}ms")

            result["latency_ms"] = latency

            return result

        except Exception as e:
            print(f"✗ Prediction failed: {e}")
            raise

    def test_batch_predictions(self, texts: List[str]) -> List[Dict]:
        """
        Test batch predictions

        Args:
            texts: List of input texts

        Returns:
            List of prediction results
        """
        print(f"\n--- Batch Prediction Test ---")
        print(f"Testing {len(texts)} samples...")

        payload = json.dumps({"texts": texts})

        try:
            start_time = time.time()

            response = self.runtime_client.invoke_endpoint(
                EndpointName=self.endpoint_name,
                ContentType="application/json",
                Body=payload,
            )

            latency = (time.time() - start_time) * 1000

            results = json.loads(response["Body"].read().decode())

            print(f"✓ Processed {len(results)} predictions")
            print(f"  Total latency: {latency:.2f}ms")
            print(f"  Average latency: {latency/len(texts):.2f}ms per sample")

            return results

        except Exception as e:
            print(f"✗ Batch prediction failed: {e}")
            raise

    def test_latency(self, num_requests: int = 10) -> Dict:
        """
        Test endpoint latency with multiple requests

        Args:
            num_requests: Number of requests to send

        Returns:
            Latency statistics
        """
        print(f"\n--- Latency Test ({num_requests} requests) ---")

        test_text = "This is a test for latency measurement."
        latencies = []

        for i in range(num_requests):
            try:
                start_time = time.time()

                payload = json.dumps({"text": test_text})
                self.runtime_client.invoke_endpoint(
                    EndpointName=self.endpoint_name,
                    ContentType="application/json",
                    Body=payload,
                )

                latency = (time.time() - start_time) * 1000
                latencies.append(latency)

            except Exception as e:
                print(f"✗ Request {i+1} failed: {e}")

        if latencies:
            stats = {
                "count": len(latencies),
                "mean": sum(latencies) / len(latencies),
                "min": min(latencies),
                "max": max(latencies),
                "p50": sorted(latencies)[len(latencies) // 2],
                "p95": sorted(latencies)[int(len(latencies) * 0.95)],
                "p99": sorted(latencies)[int(len(latencies) * 0.99)],
            }

            print(f"\nLatency Statistics:")
            print(f"  Mean: {stats['mean']:.2f}ms")
            print(f"  Min:  {stats['min']:.2f}ms")
            print(f"  Max:  {stats['max']:.2f}ms")
            print(f"  P50:  {stats['p50']:.2f}ms")
            print(f"  P95:  {stats['p95']:.2f}ms")
            print(f"  P99:  {stats['p99']:.2f}ms")

            # Check latency SLA
            if stats["p95"] > 500:
                print(f"⚠ WARNING: P95 latency ({stats['p95']:.2f}ms) exceeds 500ms SLA")
            else:
                print(f"✓ P95 latency within SLA")

            return stats

        else:
            raise Exception("No successful requests")

    def test_error_handling(self) -> None:
        """Test endpoint error handling"""
        print(f"\n--- Error Handling Test ---")

        # Test with invalid JSON
        print("\nTesting invalid JSON...")
        try:
            self.runtime_client.invoke_endpoint(
                EndpointName=self.endpoint_name,
                ContentType="application/json",
                Body="invalid json",
            )
            print("✗ Should have raised error for invalid JSON")
        except Exception:
            print("✓ Correctly handled invalid JSON")

        # Test with missing field
        print("\nTesting missing required field...")
        try:
            response = self.runtime_client.invoke_endpoint(
                EndpointName=self.endpoint_name,
                ContentType="application/json",
                Body=json.dumps({"wrong_field": "value"}),
            )

            result = json.loads(response["Body"].read().decode())
            if "error" in result:
                print("✓ Correctly returned error for missing field")
            else:
                print("⚠ Expected error response for missing field")

        except Exception as e:
            print(f"✓ Correctly handled missing field: {e}")

    def test_prediction_quality(self) -> None:
        """Test prediction quality with known examples"""
        print(f"\n--- Prediction Quality Test ---")

        test_cases = [
            {
                "text": "This product is absolutely amazing! Best purchase ever!",
                "expected": "positive",
            },
            {
                "text": "Terrible quality. Complete waste of money.",
                "expected": "negative",
            },
            {
                "text": "Excellent service and great value for money!",
                "expected": "positive",
            },
            {
                "text": "Very disappointed. Would not recommend.",
                "expected": "negative",
            },
        ]

        correct = 0
        total = len(test_cases)

        for i, case in enumerate(test_cases, 1):
            result = self.test_single_prediction(case["text"])
            prediction = result["prediction"]
            expected = case["expected"]

            if prediction == expected:
                print(f"✓ Test {i}: Correct ({prediction})")
                correct += 1
            else:
                print(f"✗ Test {i}: Incorrect (predicted {prediction}, expected {expected})")

        accuracy = correct / total
        print(f"\n{'='*60}")
        print(f"Quality Test Accuracy: {accuracy:.1%} ({correct}/{total})")
        print(f"{'='*60}")

        if accuracy < 0.75:
            print("⚠ WARNING: Accuracy below 75%")
        else:
            print("✓ Quality test passed")

    def run_all_tests(self) -> None:
        """Run complete test suite"""
        print("\n" + "=" * 80)
        print(f"ENDPOINT TEST SUITE: {self.endpoint_name}")
        print("=" * 80)

        try:
            # 1. Check endpoint status
            self.check_endpoint_status()

            # 2. Test single prediction
            self.test_single_prediction("This is a test review for the endpoint.")

            # 3. Test batch predictions
            batch_texts = [
                "Great product!",
                "Terrible experience.",
                "Average quality.",
            ]
            self.test_batch_predictions(batch_texts)

            # 4. Test latency
            self.test_latency(num_requests=20)

            # 5. Test error handling
            self.test_error_handling()

            # 6. Test prediction quality
            self.test_prediction_quality()

            print("\n" + "=" * 80)
            print("✓ ALL TESTS COMPLETED SUCCESSFULLY")
            print("=" * 80)

        except Exception as e:
            print("\n" + "=" * 80)
            print(f"✗ TESTS FAILED: {e}")
            print("=" * 80)
            raise


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Test SageMaker endpoint")

    parser.add_argument(
        "--endpoint",
        type=str,
        required=True,
        help="SageMaker endpoint name",
    )
    parser.add_argument(
        "--region",
        type=str,
        default="us-east-1",
        help="AWS region",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Run quick smoke test only",
    )

    args = parser.parse_args()

    # Create tester
    tester = EndpointTester(endpoint_name=args.endpoint, region=args.region)

    if args.quick:
        # Quick smoke test
        print("\nRunning quick smoke test...")
        tester.check_endpoint_status()
        tester.test_single_prediction("This is a quick test.")
        print("\n✓ Smoke test passed")
    else:
        # Full test suite
        tester.run_all_tests()


if __name__ == "__main__":
    main()
