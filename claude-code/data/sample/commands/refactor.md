Refactor the code in $ARGUMENTS to improve quality and maintainability:

## Refactoring Process

1. **Analyze current code** ($ARGUMENTS)
   - Read and understand current implementation
   - Identify code smells and anti-patterns
   - Note what's already good

2. **Identify improvements**
   - Long functions (>50 lines)
   - Duplicated code (DRY violations)
   - Poor naming (unclear variables/functions)
   - Complex conditionals (high cyclomatic complexity)
   - Missing abstractions
   - Tight coupling

3. **Plan refactoring**
   - Prioritize changes by impact
   - Ensure backward compatibility (or note breaking changes)
   - Keep existing tests passing

4. **Apply refactorings** (common patterns):

### Extract Function
```python
# Before: Long function
def process_order(order):
    # 50 lines of validation
    # 30 lines of calculation
    # 20 lines of saving

# After: Extracted functions
def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    save_order(order, total)
```

### Extract Variable
```python
# Before: Complex expression
if user.age >= 18 and user.has_license and not user.suspended:

# After: Named boolean
is_eligible_driver = user.age >= 18 and user.has_license and not user.suspended
if is_eligible_driver:
```

### Replace Magic Numbers
```python
# Before
if speed > 120:

# After
SPEED_LIMIT_KMH = 120
if speed > SPEED_LIMIT_KMH:
```

### Simplify Conditionals
```python
# Before
if condition:
    return True
else:
    return False

# After
return condition
```

### Use Better Data Structures
```python
# Before: Multiple related variables
user_name = "Alice"
user_email = "alice@example.com"
user_age = 30

# After: Structured data
user = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}
```

## Refactoring Output

### Summary
[Brief description of changes made]

### Improvements Made
1. **[Refactoring Type]**: [Description]
   - Before: [Lines of code]
   - After: [Improved code]
   - Benefit: [Why it's better]

### Preserved Behavior
- [List of functionality that remains unchanged]
- All existing tests should still pass

### Breaking Changes
- [None / List any breaking changes]

### Suggested Next Steps
- [Additional improvements for the future]
- [Technical debt that could be addressed]

## Refactoring Principles Applied

✅ **Code is more readable**
- Descriptive names
- Clear structure
- Reduced complexity

✅ **Code is more maintainable**
- Smaller functions
- Better organization
- Less duplication

✅ **Code is more testable**
- Isolated logic
- Fewer dependencies
- Clear interfaces

---

**Important**: Run all tests after refactoring to ensure nothing broke!
