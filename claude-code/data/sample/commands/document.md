Generate comprehensive documentation for $ARGUMENTS:

1. Read the code in $ARGUMENTS
2. Generate appropriate documentation based on file type
3. Follow language-specific documentation standards

## Documentation Generation

### For Python Functions/Classes

```python
def function_name(param1: type1, param2: type2) -> return_type:
    """Brief one-line summary of what the function does.

    More detailed explanation of the function's purpose and behavior.
    Explain any important implementation details or algorithms used.

    Args:
        param1 (type1): Description of first parameter.
            Can span multiple lines if needed.
        param2 (type2): Description of second parameter.

    Returns:
        return_type: Description of return value.

    Raises:
        ValueError: When param1 is negative.
        TypeError: When param2 is not a string.

    Examples:
        >>> function_name(42, "test")
        expected_output

        >>> function_name(-1, "test")
        Traceback (most recent call last):
        ValueError: param1 must be positive

    Note:
        Any important notes about usage or behavior.

    See Also:
        related_function: Related functionality.
    """
```

### For JavaScript Functions

```javascript
/**
 * Brief one-line summary of what the function does.
 *
 * More detailed explanation of the function's purpose and behavior.
 *
 * @param {type1} param1 - Description of first parameter
 * @param {type2} param2 - Description of second parameter
 * @returns {returnType} Description of return value
 * @throws {Error} When param1 is invalid
 *
 * @example
 * functionName(42, "test")
 * // Returns: expected_output
 *
 * @example
 * functionName(-1, "test")
 * // Throws: Error: param1 must be positive
 */
```

### For Files/Modules

Create or update README.md:

```markdown
# [Module/Package Name]

Brief one-line description.

## Overview

Detailed explanation of what this module does and why it exists.

## Installation

```bash
pip install package-name
# or
npm install package-name
```

## Quick Start

```python
from module import function

# Basic usage example
result = function(param)
print(result)
```

## Usage Examples

### Example 1: Basic Usage
```python
# Code example with explanation
```

### Example 2: Advanced Usage
```python
# More complex example
```

## API Reference

### Functions

#### `function_name(param1, param2)`

Description of function.

**Parameters:**
- `param1` (type): Description
- `param2` (type): Description

**Returns:**
- `type`: Description

**Example:**
```python
result = function_name("test", 42)
```

### Classes

#### `ClassName`

Description of class.

**Attributes:**
- `attr1` (type): Description
- `attr2` (type): Description

**Methods:**
- `method1()`: Description
- `method2()`: Description

**Example:**
```python
obj = ClassName()
obj.method1()
```

## Configuration

If applicable, document configuration options:

```python
config = {
    "option1": "default_value",  # Description
    "option2": 42,               # Description
}
```

## Error Handling

Common errors and how to handle them:

### Error 1: ValueError
**Cause:** Invalid input
**Solution:** Validate input before calling

### Error 2: FileNotFoundError
**Cause:** Missing configuration file
**Solution:** Create config.json with required fields

## Performance Considerations

- Time complexity: O(n)
- Space complexity: O(1)
- Best practices for optimal performance

## Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=module tests/
```

## Contributing

Guidelines for contributors (if applicable).

## License

[License information]

## Changelog

### Version X.Y.Z (YYYY-MM-DD)
- Added: New feature
- Fixed: Bug fix
- Changed: Breaking change
```

---

## Documentation Checklist

When documenting code, ensure:

- [ ] **Purpose** is clear (what and why)
- [ ] **Parameters** are described with types
- [ ] **Return values** are documented
- [ ] **Exceptions** are listed
- [ ] **Examples** are provided
- [ ] **Edge cases** are explained
- [ ] **Dependencies** are noted
- [ ] **Usage** is demonstrated
- [ ] **Assumptions** are stated
- [ ] **Trade-offs** are explained (if relevant)

---

## Documentation Quality Guidelines

### ✅ Good Documentation:
- Explains WHY, not just WHAT
- Includes practical examples
- Covers edge cases and errors
- Uses clear, simple language
- Is up-to-date with code

### ❌ Bad Documentation:
- Just restates the code
- No examples
- Out of sync with code
- Assumes too much knowledge
- Too verbose or too terse

---

## Special Documentation Needs

### Complex Algorithms
```python
def complex_algorithm(data):
    """Implements [Algorithm Name] for [Purpose].

    This algorithm works by:
    1. [Step 1 explanation]
    2. [Step 2 explanation]
    3. [Step 3 explanation]

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Algorithm source: [Citation or reference]
    """
```

### API Endpoints (REST)
```markdown
## POST /api/users

Create a new user.

**Request:**
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response (201 Created):**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Errors:**
- 400: Invalid input
- 409: User already exists
```

---

After generating documentation:
1. Check that it's accurate
2. Verify examples work
3. Ensure formatting is correct
4. Update any related documentation
