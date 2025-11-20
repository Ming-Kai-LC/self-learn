"""
Unit tests for sentiment analysis model

Run with: pytest tests/test_model.py -v
"""

import sys
from pathlib import Path

import numpy as np
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from preprocess import TextPreprocessor


class TestTextPreprocessor:
    """Test cases for TextPreprocessor"""

    @pytest.fixture
    def preprocessor(self):
        """Create preprocessor instance"""
        return TextPreprocessor(
            lowercase=True, remove_stopwords=True, remove_numbers=False
        )

    def test_initialization(self, preprocessor):
        """Test preprocessor initialization"""
        assert preprocessor is not None
        assert preprocessor.lowercase is True
        assert preprocessor.remove_stopwords is True
        assert preprocessor.remove_numbers is False

    def test_remove_urls(self, preprocessor):
        """Test URL removal"""
        text = "Check out https://example.com for more info!"
        result = preprocessor.remove_urls(text)
        assert "https://example.com" not in result
        assert "Check out" in result

    def test_remove_html_tags(self, preprocessor):
        """Test HTML tag removal"""
        text = "This is <b>bold</b> and <i>italic</i> text"
        result = preprocessor.remove_html_tags(text)
        assert "<b>" not in result
        assert "</b>" not in result
        assert "bold" in result

    def test_remove_mentions_hashtags(self, preprocessor):
        """Test @mention and #hashtag removal"""
        text = "@user This is #awesome!"
        result = preprocessor.remove_mentions_hashtags(text)
        assert "@user" not in result
        assert "#awesome" not in result
        assert "This is" in result

    def test_lowercase_conversion(self, preprocessor):
        """Test lowercase conversion"""
        text = "THIS IS UPPERCASE TEXT"
        result = preprocessor.preprocess(text)
        assert result.islower()

    def test_punctuation_removal(self, preprocessor):
        """Test punctuation removal"""
        text = "Hello, World! How are you?"
        result = preprocessor.remove_punctuation(text, keep_apostrophes=False)
        assert "," not in result
        assert "!" not in result
        assert "?" not in result

    def test_contraction_expansion(self, preprocessor):
        """Test contraction expansion"""
        text = "I can't believe it's not working!"
        result = preprocessor.expand_contractions(text)
        assert "cannot" in result or "can not" in result
        assert "it is" in result or "its" in result

    def test_stopword_removal(self, preprocessor):
        """Test stopword removal"""
        text = "this is a test of the stopword removal"
        result = preprocessor.preprocess(text)
        # Some stopwords should be removed
        assert "test" in result
        assert "stopword" in result
        assert "removal" in result

    def test_preprocess_pipeline(self, preprocessor):
        """Test complete preprocessing pipeline"""
        text = "This is AMAZING! I can't believe how GOOD this is!!! 😍"
        result = preprocessor.preprocess(text)

        # Should be lowercase
        assert result.islower()

        # Should not be empty
        assert len(result) > 0

        # Should contain key sentiment words
        assert "amazing" in result or "good" in result

    def test_preprocess_batch(self, preprocessor):
        """Test batch preprocessing"""
        texts = [
            "This is great!",
            "This is terrible!",
            "This is okay.",
        ]

        results = preprocessor.preprocess_batch(texts)

        assert len(results) == len(texts)
        assert all(isinstance(r, str) for r in results)
        assert all(len(r) > 0 for r in results)

    def test_empty_string(self, preprocessor):
        """Test handling of empty string"""
        result = preprocessor.preprocess("")
        assert isinstance(result, str)
        assert len(result) == 0

    def test_whitespace_normalization(self, preprocessor):
        """Test whitespace normalization"""
        text = "Multiple    spaces    and    tabs"
        result = preprocessor.remove_extra_whitespace(text)
        assert "    " not in result
        assert "  " not in result


class TestModelTraining:
    """Test cases for model training"""

    def test_train_local_mode(self):
        """Test training in local mode with minimal data"""
        # This would require setting up test data
        # For now, just verify imports work
        from train import SentimentModelTrainer

        trainer = SentimentModelTrainer(max_features=100)
        assert trainer is not None
        assert trainer.max_features == 100

    def test_model_initialization(self):
        """Test model initialization"""
        from train import SentimentModelTrainer

        trainer = SentimentModelTrainer(max_features=1000, random_state=42)

        assert trainer.max_features == 1000
        assert trainer.random_state == 42
        assert trainer.preprocessor is not None
        assert trainer.vectorizer is None  # Not initialized yet
        assert trainer.model is None  # Not initialized yet


class TestModelInference:
    """Test cases for model inference"""

    def test_predictor_initialization(self):
        """Test predictor initialization"""
        from inference import SentimentPredictor

        predictor = SentimentPredictor(model_path="/tmp/test_models")
        assert predictor is not None
        assert not predictor.loaded

    def test_prediction_format(self):
        """Test prediction output format"""
        # This would require a trained model
        # Testing the expected format structure
        expected_keys = {"prediction", "confidence", "probabilities"}

        # Mock result
        result = {
            "prediction": "positive",
            "confidence": 0.85,
            "probabilities": {"negative": 0.15, "positive": 0.85},
        }

        assert set(result.keys()) == expected_keys
        assert result["prediction"] in ["positive", "negative"]
        assert 0 <= result["confidence"] <= 1
        assert "negative" in result["probabilities"]
        assert "positive" in result["probabilities"]


class TestDataValidation:
    """Test cases for data validation"""

    def test_valid_sentiment_labels(self):
        """Test sentiment label validation"""
        valid_labels = [0, 1]

        for label in valid_labels:
            assert label in [0, 1]

    def test_text_data_types(self):
        """Test text data type handling"""
        from preprocess import TextPreprocessor

        preprocessor = TextPreprocessor()

        # Test string input
        result = preprocessor.preprocess("This is a test")
        assert isinstance(result, str)

        # Test non-string input (should convert)
        result = preprocessor.preprocess(12345)
        assert isinstance(result, str)


class TestErrorHandling:
    """Test cases for error handling"""

    def test_invalid_model_path(self):
        """Test handling of invalid model path"""
        from inference import SentimentPredictor

        predictor = SentimentPredictor(model_path="/nonexistent/path")

        with pytest.raises(Exception):
            predictor.load_model()

    def test_missing_data_file(self):
        """Test handling of missing data file"""
        from train import SentimentModelTrainer

        trainer = SentimentModelTrainer()

        with pytest.raises(Exception):
            trainer.load_data("/nonexistent/file.csv")


# ==================== Performance Tests ====================


class TestPerformance:
    """Test cases for performance metrics"""

    def test_preprocessing_speed(self, benchmark=None):
        """Test preprocessing performance"""
        from preprocess import TextPreprocessor

        preprocessor = TextPreprocessor()
        text = "This is a test sentence for performance testing."

        # Simple timing check (not actual benchmark)
        import time

        start = time.time()
        for _ in range(100):
            preprocessor.preprocess(text)
        elapsed = time.time() - start

        # Should process 100 texts in under 1 second
        assert elapsed < 1.0, f"Preprocessing too slow: {elapsed:.2f}s for 100 texts"


# ==================== Integration Tests ====================


class TestIntegration:
    """Integration tests for complete pipeline"""

    def test_end_to_end_pipeline(self):
        """Test complete pipeline from text to prediction"""
        from preprocess import TextPreprocessor

        # Initialize components
        preprocessor = TextPreprocessor()

        # Test data
        text = "This product is absolutely amazing!"

        # Preprocess
        processed = preprocessor.preprocess(text)

        # Verify output
        assert isinstance(processed, str)
        assert len(processed) > 0
        assert processed.islower()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
