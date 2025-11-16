# Real-World Skill Examples

Complete, production-ready skill examples with explanations of design choices.

---

## Example 1: Commit Message Generator

**Purpose**: Generate conventional commit messages from git diff
**Type**: Simple single-file generator skill
**Use Case**: Automating commit message creation

```markdown
---
name: commit-message-generator
description: Generates clear, conventional commit messages from git diffs. Use when writing commits, reviewing staged changes, or when user mentions "commit message", "git commit", or "conventional commits".
---

# Commit Message Generator

Generates conventional commit messages following best practices.

## Instructions

1. **Check Git Status**: Run `git status` to see staged files
2. **Review Changes**: Run `git diff --staged` to see what's changing
3. **Analyze Changes**: Determine the type of change:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Code style/formatting
   - `refactor`: Code restructuring
   - `test`: Adding/updating tests
   - `chore`: Maintenance tasks

4. **Generate Message**: Create message in format:
   ```
   type(scope): brief summary

   Detailed explanation of what changed and why.
   Focus on the motivation and impact, not the mechanics.
   ```

5. **Present to User**: Show the generated message and ask for approval

## Examples

**Example 1**: Adding authentication
```
feat(auth): add JWT authentication

Implement JWT-based authentication with refresh tokens.
Users can now log in securely and stay authenticated
across sessions.
```

**Example 2**: Fixing a bug
```
fix(api): handle null response in user endpoint

Add null check to prevent crashes when user data
is unavailable. Returns 404 instead of 500 error.
```
```

**Design Choices Explained**:
- **Description includes multiple trigger phrases**: "commit message", "git commit", "conventional commits" - covers various ways users ask
- **No tool restrictions**: Needs Bash to run git commands
- **Step-by-step process**: Clear workflow from status check to message generation
- **Type categorization**: Helps Claude choose appropriate commit type
- **Format specification**: Shows exact message structure
- **Real examples**: Demonstrates proper format with context

---

## Example 2: Code Reviewer

**Purpose**: Perform systematic code review
**Type**: Read-only analysis skill
**Use Case**: PR reviews, code quality checks

```markdown
---
name: code-reviewer
description: Review code for best practices, security issues, and maintainability. Use when reviewing code, checking PRs, analyzing code quality, or when user mentions "code review", "review PR", or "check code".
allowed-tools: Read, Grep, Glob
---

# Code Reviewer

Performs systematic code review against best practices.

## Review Checklist

### Code Organization
- [ ] Clear, descriptive names
- [ ] Appropriate file structure
- [ ] Logical module separation
- [ ] Consistent style

### Error Handling
- [ ] Try-catch blocks where needed
- [ ] Meaningful error messages
- [ ] Proper error propagation
- [ ] Edge cases handled

### Performance
- [ ] No unnecessary computations
- [ ] Efficient data structures
- [ ] Appropriate caching
- [ ] Resource cleanup

### Security
- [ ] Input validation
- [ ] No hardcoded secrets
- [ ] Safe data handling
- [ ] OWASP top 10 compliance

### Testing
- [ ] Testable code structure
- [ ] Tests exist for critical paths
- [ ] Good test coverage

## Instructions

1. **Identify Files**: Use Glob to find files to review
2. **Read Code**: Use Read to examine each file
3. **Search Patterns**: Use Grep to find specific patterns (security issues, anti-patterns)
4. **Apply Checklist**: Review against each category
5. **Report Findings**: Structure feedback by category with file:line references

## Output Format

```
## Code Review Summary

### Files Reviewed
- file1.js
- file2.py

### Findings

#### Code Organization
✓ Good: Clear naming throughout
⚠ Issue: Large function in file1.js:45 (60+ lines)

#### Security
✗ Critical: Hardcoded API key in file2.py:12

### Recommendations
1. Refactor large function (file1.js:45)
2. Move API key to environment variables (file2.py:12)

### Overall Assessment
[Summary of code quality]
```

## Examples

See [review-examples.md](review-examples.md) for detailed review scenarios.
```

**Design Choices Explained**:
- **allowed-tools restriction**: Prevents accidental modifications during review
- **Comprehensive checklist**: Covers all major review areas
- **Structured output**: Makes findings easy to act on
- **File:line references**: Helps users locate issues quickly
- **Severity levels**: ✓ (good), ⚠ (warning), ✗ (critical)
- **Glob → Read → Grep workflow**: Systematic approach using only allowed tools

---

## Example 3: Test Generator

**Purpose**: Generate unit tests for functions
**Type**: Generator skill with code analysis
**Use Case**: Improving test coverage

```markdown
---
name: test-generator
description: Generate unit tests for functions and classes with comprehensive test cases. Use when writing tests, improving coverage, or when user mentions "generate tests", "unit tests", "test coverage", or "write tests".
---

# Test Generator

Generates comprehensive unit tests following testing best practices.

## Test Generation Process

1. **Analyze Target Code**:
   - Read the source file
   - Identify functions/classes to test
   - Understand inputs, outputs, and side effects
   - Note edge cases and error conditions

2. **Ask Clarifications**:
   - Testing framework preference (Jest, Pytest, etc.)
   - Coverage requirements
   - Mock/stub needs
   - Specific scenarios to test

3. **Generate Test Structure**:
   ```
   describe/test suite for module
   ├── Happy path tests
   ├── Edge case tests
   ├── Error condition tests
   └── Integration tests (if needed)
   ```

4. **Write Tests**:
   - Clear test names describing what's tested
   - Arrange-Act-Assert pattern
   - One assertion per test (when possible)
   - Meaningful test data

5. **Add Test Documentation**:
   - Comment complex test scenarios
   - Document test data choices
   - Explain mocking decisions

## Test Template

```javascript
// For JavaScript/Jest
describe('functionName', () => {
  describe('happy path', () => {
    test('should [expected behavior] when [condition]', () => {
      // Arrange
      const input = validInput

      // Act
      const result = functionName(input)

      // Assert
      expect(result).toBe(expectedOutput)
    })
  })

  describe('edge cases', () => {
    test('should handle empty input', () => {
      const result = functionName('')
      expect(result).toBe(defaultValue)
    })
  })

  describe('error conditions', () => {
    test('should throw error for invalid input', () => {
      expect(() => functionName(null)).toThrow()
    })
  })
})
```

## Test Coverage Goals

- **Happy Path**: Normal operation with valid inputs
- **Edge Cases**: Boundary values, empty/null, extremes
- **Error Handling**: Invalid inputs, exceptions
- **Side Effects**: State changes, external calls
- **Integration**: Interaction with dependencies

## Examples

**Example 1**: Testing a calculator function
```javascript
describe('add', () => {
  test('should add two positive numbers', () => {
    expect(add(2, 3)).toBe(5)
  })

  test('should handle negative numbers', () => {
    expect(add(-2, 3)).toBe(1)
  })

  test('should handle zero', () => {
    expect(add(0, 5)).toBe(5)
  })
})
```

**Example 2**: Testing async function
```javascript
describe('fetchUser', () => {
  test('should return user data for valid id', async () => {
    const user = await fetchUser(123)
    expect(user).toHaveProperty('name')
  })

  test('should throw error for invalid id', async () => {
    await expect(fetchUser(-1)).rejects.toThrow()
  })
})
```
```

**Design Choices Explained**:
- **Multi-step process**: Ensures comprehensive test generation
- **Framework flexibility**: Asks user for preferences
- **Template included**: Shows concrete test structure
- **Coverage goals section**: Educates on what to test
- **Arrange-Act-Assert pattern**: Industry standard testing structure
- **Multiple examples**: Shows different testing scenarios
- **Clear test naming**: "should [behavior] when [condition]" format

---

## Example 4: Documentation Generator

**Purpose**: Generate API documentation from code
**Type**: Generator with code analysis
**Use Case**: Keeping documentation in sync with code

```markdown
---
name: doc-generator
description: Generate API documentation from source code with examples and usage. Use when documenting APIs, creating README sections, or when user mentions "generate docs", "API documentation", or "document code".
---

# Documentation Generator

Generates comprehensive API documentation from source code.

## Documentation Process

1. **Analyze Code Structure**:
   - Identify public APIs (exported functions, classes)
   - Extract function signatures and parameters
   - Find return types and values
   - Note exceptions and errors

2. **Gather Context**:
   - Read existing comments/docstrings
   - Understand purpose from implementation
   - Identify usage patterns
   - Note dependencies

3. **Ask User**:
   - Documentation format (JSDoc, Markdown, Sphinx)
   - Level of detail (brief, detailed, comprehensive)
   - Include examples (yes/no)
   - Target audience (developers, end-users)

4. **Generate Documentation**:
   - Function/class overview
   - Parameter descriptions
   - Return value details
   - Usage examples
   - Error handling notes

5. **Format Output**:
   - Follow chosen format conventions
   - Include table of contents if long
   - Add code examples with syntax highlighting
   - Link related functions/classes

## Documentation Template

```markdown
## `functionName(param1, param2)`

Brief one-line description of what this function does.

### Parameters

| Name | Type | Description |
|------|------|-------------|
| param1 | string | Description of param1 |
| param2 | number | Description of param2 (optional, default: 0) |

### Returns

`Promise<ResultType>` - Description of return value

### Throws

- `ValidationError` - When param1 is invalid
- `NetworkError` - When connection fails

### Example

```javascript
const result = await functionName('test', 42)
console.log(result) // { status: 'success' }
```

### Usage Notes

- Important consideration 1
- Important consideration 2

### See Also

- [relatedFunction](#relatedfunction)
- [RelatedClass](#relatedclass)
```

## Examples

**Example 1**: Simple function documentation
```markdown
## `calculateTotal(items, taxRate)`

Calculates the total price including tax.

### Parameters
- `items` (Array<Item>) - Array of items to sum
- `taxRate` (number) - Tax rate as decimal (0.1 = 10%)

### Returns
`number` - Total price with tax applied

### Example
```javascript
const total = calculateTotal([{price: 10}, {price: 20}], 0.1)
// returns 33 (30 + 10% tax)
```
```

**Example 2**: Class documentation
```markdown
## `class UserManager`

Manages user accounts and authentication.

### Constructor

```javascript
new UserManager(options)
```

**Parameters**:
- `options.database` (Database) - Database connection
- `options.cache` (Cache) - Optional cache instance

### Methods

#### `createUser(data)`

Creates a new user account.

**Parameters**:
- `data.email` (string) - User email (required)
- `data.name` (string) - User full name (required)
- `data.password` (string) - Password (required, min 8 chars)

**Returns**: `Promise<User>` - Created user object

**Throws**: `ValidationError` if data is invalid

**Example**:
```javascript
const user = await manager.createUser({
  email: 'user@example.com',
  name: 'John Doe',
  password: 'securepass123'
})
```
```

**Design Choices Explained**:
- **Structured analysis**: Systematic code examination
- **Format flexibility**: Supports multiple documentation standards
- **Rich templates**: Tables, code blocks, links
- **Complete examples**: Shows real usage patterns
- **Error documentation**: Important for users to handle errors
- **Cross-references**: Links to related documentation
- **Audience awareness**: Adjusts detail level based on target audience

---

## Example 5: Refactoring Assistant

**Purpose**: Guide code refactoring with safety checks
**Type**: Interactive workflow skill
**Use Case**: Improving code structure safely

```markdown
---
name: refactor-assistant
description: Guide safe code refactoring with step-by-step approach and validation. Use when refactoring code, improving structure, or when user mentions "refactor", "restructure", or "improve code".
---

# Refactoring Assistant

Guides safe, systematic code refactoring.

## Refactoring Workflow

### Phase 1: Analysis

1. **Read Target Code**: Understand current structure
2. **Identify Issues**: Find code smells and problems
3. **Run Tests**: Establish baseline (tests should pass)
4. **Check Dependencies**: Find what depends on this code

### Phase 2: Planning

5. **Propose Refactoring**: Suggest specific improvements
6. **Estimate Impact**: Identify affected files
7. **Get User Approval**: Confirm approach before changes

### Phase 3: Execution

8. **Make Changes**: Apply refactoring incrementally
9. **Run Tests After Each Step**: Ensure nothing breaks
10. **Fix Any Failures**: Address issues immediately

### Phase 4: Validation

11. **Final Test Run**: Verify all tests pass
12. **Code Review**: Check for unintended changes
13. **Document Changes**: Update comments/docs if needed

## Common Refactorings

### Extract Function
**When**: Function is too long or does multiple things
**How**: Identify logical block → Create new function → Replace with call

### Rename for Clarity
**When**: Name is unclear or misleading
**How**: Find all usages → Update name everywhere → Run tests

### Simplify Conditional
**When**: Complex nested if statements
**How**: Extract to named functions → Use early returns → Simplify logic

### Remove Duplication
**When**: Similar code in multiple places
**How**: Extract common code → Create shared function → Update call sites

### Extract Class
**When**: Class has too many responsibilities
**How**: Identify cohesive group → Create new class → Move related methods

## Safety Rules

1. **Always run tests before refactoring**
2. **Make one change at a time**
3. **Run tests after each change**
4. **Commit working states frequently**
5. **Never refactor and change behavior simultaneously**

## Example Refactoring Session

**Before**:
```javascript
function processOrder(order) {
  // Validate order
  if (!order.items || order.items.length === 0) {
    throw new Error('No items')
  }
  if (!order.customer) {
    throw new Error('No customer')
  }

  // Calculate total
  let total = 0
  for (let item of order.items) {
    total += item.price * item.quantity
  }
  if (order.discount) {
    total = total - (total * order.discount)
  }

  // Process payment
  if (order.paymentMethod === 'credit') {
    // credit card logic
  } else if (order.paymentMethod === 'debit') {
    // debit card logic
  }

  return { total, status: 'processed' }
}
```

**Refactoring Steps**:

1. Extract validation
2. Extract total calculation
3. Extract payment processing
4. Run tests after each extraction

**After**:
```javascript
function processOrder(order) {
  validateOrder(order)
  const total = calculateTotal(order)
  const payment = processPayment(order.paymentMethod, total)
  return { total, status: 'processed' }
}

function validateOrder(order) {
  if (!order.items?.length) throw new Error('No items')
  if (!order.customer) throw new Error('No customer')
}

function calculateTotal(order) {
  const subtotal = order.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  )
  return order.discount
    ? subtotal * (1 - order.discount)
    : subtotal
}

function processPayment(method, amount) {
  const handlers = {
    credit: () => processCreditCard(amount),
    debit: () => processDebitCard(amount)
  }
  return handlers[method]()
}
```

**Benefits**:
- Each function has single responsibility
- Easier to test individual pieces
- More readable main flow
- Payment methods extensible
```

**Design Choices Explained**:
- **Phased approach**: Analysis → Planning → Execution → Validation
- **Safety-first**: Tests at every step prevent breaking changes
- **User approval**: Get confirmation before major changes
- **Incremental changes**: One refactoring at a time
- **Complete example**: Shows before/after with step-by-step process
- **Benefits listed**: Helps user understand value
- **Common patterns**: Teaches standard refactoring techniques

---

## Key Patterns Across Examples

### 1. Clear Trigger Keywords
All examples include specific phrases users would naturally say:
- "commit message", "git commit"
- "code review", "review PR"
- "generate tests", "unit tests"

### 2. Appropriate Tool Restrictions
- Code Reviewer: Read-only (Glob, Grep, Read)
- Generators: Full access (need Write)
- Refactoring: Full access but cautious approach

### 3. Structured Workflows
Each skill has clear phases:
1. Analyze/Read
2. Plan/Decide
3. Execute/Generate
4. Validate/Verify

### 4. Rich Examples
Concrete code examples show:
- Input → Output transformations
- Before → After comparisons
- Multiple scenarios

### 5. User Interaction
Skills engage users when needed:
- Ask preferences (framework, format)
- Get approval (refactoring plan)
- Clarify requirements (test scenarios)

### 6. Safety Considerations
Skills that modify code include:
- Validation before changes
- Testing after changes
- Incremental approach
- Rollback capability

### 7. Output Formatting
Structured output helps users:
- Clear sections with headers
- Bullet points and checklists
- Code blocks with syntax highlighting
- File:line references for navigation

## Using These Examples

1. **Copy the structure** that matches your use case
2. **Customize the content** for your specific skill
3. **Keep the patterns** (workflow, safety, user interaction)
4. **Test thoroughly** with questions matching your description
5. **Iterate based on** how well Claude invokes your skill
