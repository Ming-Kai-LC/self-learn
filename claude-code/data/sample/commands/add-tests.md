Generate comprehensive tests for $ARGUMENTS:

1. Read the specified file: $ARGUMENTS
2. Analyze the code to understand:
   - What functions/classes exist
   - What they do (input/output)
   - Edge cases to test
   - Error conditions
3. Create a test file following conventions:
   - Python: `test_[filename].py` using pytest
   - JavaScript: `[filename].test.js` using Jest
   - Use descriptive test names: `test_function_with_condition_returns_expected()`
4. Include tests for:
   - Happy path (normal usage)
   - Edge cases (empty, null, boundary values)
   - Error cases (invalid input)
5. Use appropriate fixtures/mocks for dependencies

Test structure (pytest example):
```python
import pytest
from module import function_to_test

class TestFunctionName:
    """Test suite for function_name."""

    def test_function_with_valid_input_returns_expected_result(self):
        # Arrange
        input_data = "test"

        # Act
        result = function_to_test(input_data)

        # Assert
        assert result == expected_value

    def test_function_with_empty_input_raises_value_error(self):
        with pytest.raises(ValueError):
            function_to_test("")

    def test_function_with_boundary_value_handles_correctly(self):
        # Test edge case
        result = function_to_test(max_value)
        assert result is not None
```

After generating tests:
1. Save to appropriate test file
2. Explain what each test covers
3. Suggest any additional test cases
4. Note coverage percentage estimate
