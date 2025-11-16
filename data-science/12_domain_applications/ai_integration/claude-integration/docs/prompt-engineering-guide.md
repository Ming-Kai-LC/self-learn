# Prompt Engineering Guide for Claude

Learn how to write effective prompts to get the best results from Claude.

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [Prompt Structure](#prompt-structure)
3. [Advanced Techniques](#advanced-techniques)
4. [Common Patterns](#common-patterns)
5. [Examples](#examples)

## Fundamentals

### What is Prompt Engineering?

Prompt engineering is the practice of crafting inputs to AI models to get desired outputs. With Claude, well-structured prompts lead to more accurate, relevant, and useful responses.

### Core Principles

#### 1. Be Clear and Specific
```
Bad:  "Make it better"
Good: "Refactor this function to use list comprehensions and add type hints"
```

#### 2. Provide Context
```
Bad:  "Fix the bug"
Good: "The user registration function throws a ValidationError when the email
       field is empty. Here's the error traceback: [paste traceback]"
```

#### 3. Set Expectations
```
Bad:  "Write some tests"
Good: "Write unit tests for the User class that cover initialization, validation,
       and the save() method. Use pytest and aim for 90% coverage."
```

## Prompt Structure

### Basic Template

```
[Context] - What Claude needs to know
[Task] - What you want Claude to do
[Constraints] - Any limitations or requirements
[Format] - How you want the output structured
```

### Example

```
Context: I have a Flask API that handles user authentication.

Task: Add rate limiting to prevent brute force attacks on the login endpoint.

Constraints:
- Use Flask-Limiter library
- Limit to 5 attempts per minute per IP
- Return appropriate error messages

Format: Provide the updated code with inline comments explaining the changes.
```

## Advanced Techniques

### 1. Chain of Thought

Encourage Claude to think step-by-step:

```
"Explain how to implement a caching layer for this API. Walk through:
1. What data should be cached
2. Which caching strategy to use
3. How to invalidate the cache
4. Implementation steps"
```

### 2. Few-Shot Learning

Provide examples of desired output:

```
"Generate API endpoint documentation following this format:

Example:
GET /api/users/:id
Description: Retrieve a user by ID
Parameters:
  - id (string): User unique identifier
Response: User object with id, name, email
Errors: 404 if user not found

Now document these endpoints:
[list your endpoints]"
```

### 3. Role Assignment

Give Claude a specific role:

```
"Act as a senior Python developer reviewing this code for a junior developer.
Provide constructive feedback on:
- Code organization
- Best practices
- Potential improvements
- Learning resources"
```

### 4. Iterative Refinement

Break complex tasks into steps:

```
First request: "Outline the architecture for a task queue system"
Second request: "Implement the task creation and enqueueing logic"
Third request: "Add worker processes to consume and execute tasks"
```

## Common Patterns

### Code Review Pattern

```
"Review this code for:
1. Security vulnerabilities (SQL injection, XSS, etc.)
2. Performance bottlenecks
3. Code clarity and maintainability
4. Best practices adherence

[paste code]

Provide specific line numbers for issues found."
```

### Debugging Pattern

```
"I'm experiencing [describe problem].

Expected behavior: [what should happen]
Actual behavior: [what is happening]

Error message: [paste error]
Relevant code: [paste code]

Help me identify the root cause and suggest a fix."
```

### Implementation Pattern

```
"Implement [feature] with these requirements:

Functional requirements:
- [requirement 1]
- [requirement 2]

Technical requirements:
- Use [technology/library]
- Follow [design pattern]

Include:
- Implementation code
- Unit tests
- Usage example
- Documentation"
```

### Refactoring Pattern

```
"Refactor this code to:
1. Improve readability
2. Reduce complexity
3. Follow DRY principle
4. Add proper error handling

[paste code]

Explain the changes you make and why."
```

## Examples

### Example 1: Database Design

```
Prompt:
"Design a database schema for a blog platform with these entities:
- Users (can write posts and comments)
- Posts (have title, content, publish date)
- Comments (belong to posts and users)
- Tags (posts can have multiple tags)

Provide:
1. Entity relationship diagram (text format)
2. SQL CREATE TABLE statements
3. Explanation of relationships and indexing decisions"
```

### Example 2: API Development

```
Prompt:
"Create a RESTful API endpoint for user registration with:

Requirements:
- Accept email, password, username
- Validate email format and password strength
- Hash password before storage
- Return JWT token on success
- Return validation errors with 400 status

Technology: FastAPI
Include: Endpoint code, Pydantic models, error handling"
```

### Example 3: Testing

```
Prompt:
"Write comprehensive tests for this authentication function:

[paste function]

Include:
- Happy path test
- Invalid credentials test
- Missing parameters test
- Database error handling test
- Edge cases

Use pytest with fixtures for database setup."
```

### Example 4: Documentation

```
Prompt:
"Generate user-facing documentation for this API:

[paste API code]

Format:
- Overview section
- Authentication requirements
- Endpoint descriptions with examples
- Request/response formats
- Error codes and meanings
- Code examples in Python and JavaScript"
```

## Tips for Better Prompts

### 1. Use Structured Formats

Use lists, bullet points, and sections:
```
"Create a todo list API with:
Features:
- Create todo
- Mark complete
- Delete todo
- List all todos

Tech stack:
- Node.js + Express
- MongoDB
- JWT auth"
```

### 2. Specify Programming Language/Framework

```
Bad:  "Create a web server"
Good: "Create a web server using Python Flask with routes for health check and user management"
```

### 3. Include Quality Criteria

```
"Write a function that:
- Has descriptive variable names
- Includes docstring
- Handles edge cases
- Uses type hints
- Has O(n) time complexity or better"
```

### 4. Request Explanations

```
"Implement quicksort algorithm and explain:
- How it works
- Time/space complexity
- When to use vs other sorting algorithms
- Potential pitfalls"
```

### 5. Set Constraints

```
"Optimize this database query, but:
- Don't change the table structure
- Maintain backward compatibility
- Keep the same return format
- Use only standard SQL (no database-specific features)"
```

## Anti-Patterns to Avoid

### 1. Vague Requests
```
Bad:  "Make it faster"
Good: "Optimize this function to reduce time complexity from O(n²) to O(n log n)"
```

### 2. Assuming Context
```
Bad:  "Use the database we discussed"
Good: "Use PostgreSQL with SQLAlchemy ORM"
```

### 3. Overly Complex Single Requests
```
Bad:  "Build a complete e-commerce platform with user auth, product catalog,
       shopping cart, payment processing, and admin dashboard"

Good: Break into steps:
       "First, design the database schema for an e-commerce platform with users,
        products, orders, and cart tables"
```

### 4. No Success Criteria
```
Bad:  "Write some tests"
Good: "Write unit tests that achieve >90% code coverage and test all edge cases"
```

## Measuring Prompt Effectiveness

Good prompts should result in:
- ✅ Relevant, actionable responses
- ✅ Minimal back-and-forth clarification
- ✅ Code that works on first try (or close to it)
- ✅ Appropriate level of detail
- ✅ Proper error handling and edge cases

Poor prompts often lead to:
- ❌ Generic, unhelpful responses
- ❌ Multiple clarification questions
- ❌ Code with bugs or missing requirements
- ❌ Too brief or too verbose output
- ❌ Missing important considerations

## Practice Exercises

### Exercise 1: Code Review
Try crafting a prompt for reviewing a piece of code. Include:
- What aspects to review
- What format you want feedback in
- What level of detail you need

### Exercise 2: Feature Implementation
Create a prompt for implementing a new feature. Include:
- Clear requirements
- Technical constraints
- Expected deliverables
- Quality criteria

### Exercise 3: Debugging
Write a debugging prompt that includes:
- Problem description
- Expected vs actual behavior
- Relevant code and errors
- What you've already tried

## Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Claude API Documentation](https://docs.anthropic.com/en/api)
- [Prompt Library](https://docs.anthropic.com/en/prompt-library)

## Conclusion

Effective prompt engineering is about clear communication. Treat Claude like a highly skilled colleague: provide context, be specific about what you need, and set clear expectations. With practice, you'll develop an intuition for crafting prompts that consistently produce excellent results.
