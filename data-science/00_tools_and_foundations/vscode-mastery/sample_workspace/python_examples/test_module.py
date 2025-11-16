"""
Test Module - For Testing and IntelliSense Practice
==================================================
Practice using IntelliSense, code completion, and testing features.
"""

import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Unit tests for Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        """Test subtraction."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.multiply(6, 7)
        self.assertEqual(result, 42)

    def test_divide(self):
        """Test division."""
        result = self.calc.divide(15, 3)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
