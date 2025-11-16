"""
Simple Calculator - For Debugging Practice
==========================================
This calculator contains intentional bugs for debugging exercises.
"""


class Calculator:
    """A simple calculator class for basic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base**exponent


def run_calculations():
    """Run sample calculations for debugging practice."""
    calc = Calculator()

    # Set breakpoint here to start debugging
    result1 = calc.add(10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calc.subtract(20, 8)
    print(f"20 - 8 = {result2}")

    result3 = calc.multiply(6, 7)
    print(f"6 * 7 = {result3}")

    result4 = calc.divide(100, 4)
    print(f"100 / 4 = {result4}")

    result5 = calc.power(2, 8)
    print(f"2 ^ 8 = {result5}")

    # This will raise an exception - good for debugging
    try:
        result6 = calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_calculations()
