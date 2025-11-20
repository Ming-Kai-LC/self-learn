# Skill Library & Patterns

**Common skills, templates, and patterns for Claude Code**

Last Updated: 2025-11-20

---

## Table of Contents

1. [Skill Basics](#skill-basics)
2. [Skill Templates](#skill-templates)
3. [Common Skill Patterns](#common-skill-patterns)
4. [Domain-Specific Skills](#domain-specific-skills)
5. [Best Practices](#best-practices)
6. [Troubleshooting](#troubleshooting)

---

## Skill Basics

### What Makes a Good Skill?

**Good skills are**:
- ✅ Focused on one domain
- ✅ Have clear activation triggers
- ✅ Provide actionable guidance
- ✅ Include examples
- ✅ Well-documented

**Bad skills are**:
- ❌ Too broad or generic
- ❌ Vague activation criteria
- ❌ Just lists of information
- ❌ No practical examples
- ❌ Poorly structured

### Skill Structure

```markdown
# SKILL.md

description: Clear, specific description for activation (1-2 sentences)

## Instructions
Detailed instructions for Claude on how to apply this skill

## Examples
Concrete examples showing the skill in action

## Reference
Links, documentation, additional context

## Patterns (optional)
Common patterns or templates

## Anti-patterns (optional)
What to avoid
```

---

## Skill Templates

### Template 1: Programming Language Expert

```markdown
# python-expert

description: Provides Python best practices, idioms, and expert guidance

## Instructions

Provide expert Python guidance covering:

### Code Style & Idioms
- Follow PEP 8 conventions
- Use Pythonic idioms (list comprehensions, context managers, etc.)
- Prefer explicit over implicit
- Write readable, self-documenting code

### Common Patterns
- Use `with` for resource management
- Use `@property` for computed attributes
- Use `@dataclass` for data containers
- Use type hints for clarity
- Use `enum` for constants

### Performance
- Use generators for large datasets
- Profile before optimizing
- Use appropriate data structures
- Avoid premature optimization

### Error Handling
- Use specific exceptions
- Provide meaningful error messages
- Clean up resources in finally blocks
- Fail fast with assertions

## Examples

### Good Python Code
\`\`\`python
from pathlib import Path
from typing import List
from contextlib import contextmanager

@contextmanager
def open_file(path: Path):
    """Context manager for safe file handling."""
    file = path.open()
    try:
        yield file
    finally:
        file.close()

def process_data(items: List[int]) -> List[int]:
    """Process items using list comprehension."""
    return [x * 2 for x in items if x > 0]
\`\`\`

### Anti-patterns to Avoid
\`\`\`python
# ❌ Don't do this
def bad_example():
    file = open("data.txt")  # No context manager
    data = []
    for item in items:        # Use comprehension
        if item > 0:
            data.append(item * 2)
    return data
\`\`\`

## Reference
- PEP 8: https://pep8.org
- Python Style Guide
- Effective Python by Brett Slatkin
```

---

### Template 2: Testing Strategist

```markdown
# test-strategist

description: Provides testing strategies, patterns, and best practices

## Instructions

Guide testing decisions:

### What to Test
- Public interfaces (API contracts)
- Business logic and algorithms
- Error handling and edge cases
- Integration points
- Critical user flows

### What Not to Test
- Private implementation details
- Third-party libraries (trust them)
- Trivial getters/setters
- Auto-generated code

### Test Structure
**Arrange-Act-Assert Pattern**:
\`\`\`python
def test_user_login():
    # Arrange: Set up test data
    user = User(username="test", password="secret")
    auth_service = AuthService()

    # Act: Execute the operation
    result = auth_service.login(user)

    # Assert: Verify the outcome
    assert result.is_authenticated
    assert result.token is not None
\`\`\`

### Test Organization
- One test file per module
- Group related tests in classes
- Use descriptive test names
- Keep tests independent
- Use fixtures for setup

### Mocking Strategy
- Mock external dependencies
- Mock at interface boundaries
- Don't mock what you don't own (wrap first)
- Use dependency injection for testability

## Examples

### Well-Structured Test
\`\`\`python
import pytest
from unittest.mock import Mock

class TestUserAuthentication:
    """Tests for user authentication."""

    @pytest.fixture
    def auth_service(self):
        """Provide auth service with mocked DB."""
        db = Mock()
        return AuthService(db)

    def test_successful_login(self, auth_service):
        """User can log in with valid credentials."""
        # Arrange
        user = User("john", "password123")
        auth_service.db.find_user.return_value = user

        # Act
        result = auth_service.login("john", "password123")

        # Assert
        assert result.success is True
        assert result.user.username == "john"

    def test_login_with_invalid_password(self, auth_service):
        """Login fails with incorrect password."""
        # Arrange
        user = User("john", "password123")
        auth_service.db.find_user.return_value = user

        # Act
        result = auth_service.login("john", "wrongpass")

        # Assert
        assert result.success is False
        assert result.error == "Invalid credentials"
\`\`\`

## Reference
- Test-Driven Development (TDD)
- pytest documentation
- unittest.mock guide
```

---

### Template 3: Security Auditor

```markdown
# security-auditor

description: Reviews code for security vulnerabilities and provides security guidance

## Instructions

Check for common security issues:

### OWASP Top 10
1. **Injection** - SQL, command, LDAP injection
2. **Broken Authentication** - Weak passwords, session management
3. **Sensitive Data Exposure** - Unencrypted data, logging secrets
4. **XML External Entities** - XXE attacks
5. **Broken Access Control** - Missing authorization
6. **Security Misconfiguration** - Default configs, unnecessary features
7. **Cross-Site Scripting (XSS)** - Unescaped output
8. **Insecure Deserialization** - Untrusted data deserialization
9. **Using Components with Known Vulnerabilities**
10. **Insufficient Logging & Monitoring**

### Input Validation
- Validate all user input
- Use allow lists, not deny lists
- Sanitize before processing
- Never trust user data

### Authentication & Authorization
- Use strong password hashing (bcrypt, Argon2)
- Implement proper session management
- Check authorization on every request
- Use principle of least privilege

### Data Protection
- Encrypt sensitive data at rest
- Use HTTPS for data in transit
- Never log sensitive information
- Use environment variables for secrets

## Examples

### Secure Code
\`\`\`python
import bcrypt
from typing import Optional

def authenticate_user(username: str, password: str) -> Optional[User]:
    """Securely authenticate user."""
    # Use parameterized queries to prevent SQL injection
    user = db.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if not user:
        return None

    # Use bcrypt for password verification
    if bcrypt.checkpw(password.encode(), user.password_hash):
        return user

    return None

def get_user_data(user_id: int, current_user: User) -> dict:
    """Get user data with authorization check."""
    # Check authorization before allowing access
    if not current_user.can_access_user(user_id):
        raise PermissionError("Unauthorized access")

    # Use parameterized query
    return db.execute(
        "SELECT * FROM user_data WHERE id = ?",
        (user_id,)
    ).fetchone()
\`\`\`

### Insecure Code (DON'T DO THIS)
\`\`\`python
# ❌ Multiple security issues
def bad_authentication(username, password):
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE name='{username}' AND pass='{password}'"

    # Hardcoded secret
    api_key = "sk-1234567890"

    # Command injection vulnerability
    os.system(f"echo Logged in: {username}")

    # Storing password in plain text
    user.password = password

    # Logging sensitive data
    logger.info(f"Password: {password}")

    return True
\`\`\`

## Reference
- OWASP Top 10
- Security coding guidelines
- CWE Common Weakness Enumeration
```

---

### Template 4: Performance Optimizer

```markdown
# performance-optimizer

description: Analyzes code for performance issues and provides optimization guidance

## Instructions

Identify and suggest performance improvements:

### Algorithmic Complexity
- Analyze time complexity (Big O)
- Identify nested loops (O(n²))
- Suggest better algorithms
- Consider space-time tradeoffs

### Database Performance
- Identify N+1 query problems
- Suggest indexing strategies
- Recommend query optimization
- Use connection pooling

### Caching Strategies
- Identify cacheable operations
- Suggest cache keys
- Recommend TTL values
- Consider cache invalidation

### Resource Management
- Check for memory leaks
- Identify excessive allocations
- Suggest lazy loading
- Recommend batching operations

## Examples

### Performance Issues & Fixes

#### Issue 1: N+1 Query Problem
\`\`\`python
# ❌ Bad - N+1 queries
def get_posts_with_authors_bad():
    posts = Post.query.all()  # 1 query
    for post in posts:
        print(post.author.name)  # N queries

# ✅ Good - Single query with join
def get_posts_with_authors_good():
    posts = Post.query.options(
        joinedload(Post.author)
    ).all()  # 1 query total
    for post in posts:
        print(post.author.name)
\`\`\`

#### Issue 2: Inefficient Algorithm
\`\`\`python
# ❌ Bad - O(n²) duplicate check
def has_duplicates_bad(items):
    for i, item in enumerate(items):
        for j, other in enumerate(items):
            if i != j and item == other:
                return True
    return False

# ✅ Good - O(n) using set
def has_duplicates_good(items):
    return len(items) != len(set(items))
\`\`\`

#### Issue 3: Missing Caching
\`\`\`python
# ❌ Bad - Recalculates every time
def get_user_stats(user_id):
    stats = expensive_calculation(user_id)  # Slow!
    return stats

# ✅ Good - Cache with TTL
from functools import lru_cache
from datetime import timedelta

@cache_with_ttl(ttl=timedelta(minutes=5))
def get_user_stats_cached(user_id):
    stats = expensive_calculation(user_id)
    return stats
\`\`\`

## Reference
- Algorithm complexity analysis
- Database query optimization
- Caching strategies
- Profiling tools (cProfile, line_profiler)
```

---

### Template 5: Documentation Writer

```markdown
# documentation-writer

description: Generates comprehensive documentation following best practices

## Instructions

Create clear, useful documentation:

### Docstring Format
Use consistent format (Google, NumPy, or Sphinx style):
\`\`\`python
def function_name(param1: type, param2: type) -> return_type:
    """Brief description in one line.

    Longer description explaining what the function does,
    when to use it, and any important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ErrorType: When this error occurs

    Example:
        >>> function_name(value1, value2)
        expected_result
    """
\`\`\`

### Module Documentation
- Purpose and scope
- Main classes/functions
- Usage examples
- Dependencies
- Known limitations

### README Structure
1. Project title and description
2. Installation instructions
3. Quick start guide
4. Usage examples
5. API reference
6. Contributing guidelines
7. License

### API Documentation
- Endpoint path and method
- Request parameters
- Request body schema
- Response schema
- Status codes
- Error responses
- Example requests/responses

## Examples

### Well-Documented Function
\`\`\`python
from typing import List, Optional
from datetime import datetime

def calculate_user_metrics(
    user_id: int,
    start_date: datetime,
    end_date: datetime,
    include_inactive: bool = False
) -> dict:
    """Calculate comprehensive metrics for a user over a date range.

    Computes various metrics including activity count, engagement rate,
    and average session duration for the specified user and time period.

    Args:
        user_id: Unique identifier for the user
        start_date: Start of the date range (inclusive)
        end_date: End of the date range (inclusive)
        include_inactive: Whether to include inactive sessions in calculations

    Returns:
        Dictionary containing:
        - activity_count: Total number of activities
        - engagement_rate: Percentage of days with activity
        - avg_session_duration: Average session length in minutes

    Raises:
        ValueError: If start_date is after end_date
        UserNotFoundError: If user_id doesn't exist

    Example:
        >>> from datetime import datetime
        >>> metrics = calculate_user_metrics(
        ...     user_id=123,
        ...     start_date=datetime(2024, 1, 1),
        ...     end_date=datetime(2024, 1, 31)
        ... )
        >>> print(metrics['activity_count'])
        45

    Note:
        This function makes multiple database queries and may be slow
        for large date ranges. Consider using caching for frequently
        accessed metrics.
    """
    # Implementation...
\`\`\`

### API Endpoint Documentation
\`\`\`markdown
## POST /api/users

Create a new user account.

### Request Headers
\`\`\`
Content-Type: application/json
Authorization: Bearer {token}
\`\`\`

### Request Body
\`\`\`json
{
  "username": "string (required, 3-50 chars)",
  "email": "string (required, valid email)",
  "password": "string (required, min 8 chars)",
  "full_name": "string (optional)"
}
\`\`\`

### Response: 201 Created
\`\`\`json
{
  "id": 123,
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "created_at": "2024-01-15T10:30:00Z"
}
\`\`\`

### Error Responses

**400 Bad Request** - Invalid input
\`\`\`json
{
  "error": "validation_error",
  "details": {
    "username": "Username already exists"
  }
}
\`\`\`

**401 Unauthorized** - Missing or invalid token
\`\`\`json
{
  "error": "unauthorized",
  "message": "Valid authentication token required"
}
\`\`\`

### Example Request
\`\`\`bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
\`\`\`
\`\`\`

## Reference
- Documentation style guides
- API documentation standards (OpenAPI/Swagger)
- README best practices
```

---

## Common Skill Patterns

### Pattern 1: Code Review Skill

**When to use**: Automatic code quality feedback

**Structure**:
```markdown
description: Reviews code for [specific aspect]

## Instructions
- Check for [criteria 1]
- Verify [criteria 2]
- Ensure [criteria 3]

## Output Format
- Issues found
- Severity levels
- Recommendations
```

**Examples**: code-reviewer, security-auditor, performance-optimizer

---

### Pattern 2: Generator Skill

**When to use**: Automating code/doc creation

**Structure**:
```markdown
description: Generates [type of content] following [standards]

## Instructions
1. Analyze requirements
2. Generate structure
3. Fill in content
4. Validate output

## Templates
[Provide templates to follow]
```

**Examples**: test-generator, doc-writer, api-creator

---

### Pattern 3: Expert Advisor Skill

**When to use**: Domain-specific guidance

**Structure**:
```markdown
description: Provides expert guidance on [domain]

## Instructions
- Recommend best practices
- Explain rationale
- Provide examples
- Warn about pitfalls

## Patterns
[Common patterns in this domain]

## Anti-patterns
[Things to avoid]
```

**Examples**: python-expert, react-patterns, sql-optimizer

---

### Pattern 4: Validator Skill

**When to use**: Checking compliance/correctness

**Structure**:
```markdown
description: Validates [thing] against [standards]

## Instructions
1. Check requirement 1
2. Check requirement 2
3. Report violations
4. Suggest fixes

## Validation Rules
[Specific rules to check]
```

**Examples**: style-validator, api-validator, schema-validator

---

## Domain-Specific Skills

### Web Development

```markdown
# react-patterns

description: React best practices and common patterns

## Instructions
- Use functional components and hooks
- Implement proper error boundaries
- Follow composition over inheritance
- Use proper state management
- Optimize rendering with memo/useMemo/useCallback
```

```markdown
# api-design

description: RESTful API design best practices

## Instructions
- Use proper HTTP methods
- Implement consistent URL patterns
- Version your API
- Handle errors consistently
- Provide clear documentation
```

---

### Data Science

```markdown
# pandas-expert

description: Pandas best practices and efficient operations

## Instructions
- Use vectorized operations
- Avoid iterating with .iterrows()
- Use appropriate data types
- Handle missing data properly
- Optimize memory usage
```

```markdown
# ml-advisor

description: Machine learning best practices and guidance

## Instructions
- Check for data leakage
- Validate train/test split
- Recommend appropriate metrics
- Suggest cross-validation strategies
- Warn about overfitting
```

---

### DevOps

```markdown
# docker-expert

description: Docker best practices and optimization

## Instructions
- Use multi-stage builds
- Minimize layer count
- Order layers by change frequency
- Use .dockerignore
- Avoid running as root
```

```markdown
# ci-cd-advisor

description: CI/CD pipeline best practices

## Instructions
- Implement proper testing stages
- Use caching effectively
- Parallelize where possible
- Implement proper secrets management
- Monitor pipeline performance
```

---

## Best Practices

### Writing Effective Skills

1. **Clear Description**
   ```markdown
   ✅ Good: "Provides Python PEP 8 style guidance and Pythonic patterns"
   ❌ Bad: "Helps with Python"
   ```

2. **Actionable Instructions**
   ```markdown
   ✅ Good: "Check for SQL injection by looking for string concatenation in queries"
   ❌ Bad: "Be careful about security"
   ```

3. **Concrete Examples**
   ```markdown
   ✅ Include: Code examples showing good and bad patterns
   ❌ Avoid: Just listing rules without examples
   ```

4. **Proper Scope**
   ```markdown
   ✅ Good: One skill for Python style, another for Python security
   ❌ Bad: One mega-skill trying to cover everything
   ```

### Organizing Skills

**Project Skills** (.claude/skills/):
- Team coding standards
- Project-specific patterns
- Domain knowledge
- Architecture decisions

**Personal Skills** (~/.claude/skills/):
- Your preferences
- Personal workflows
- Learning notes
- Experimental patterns

### Testing Skills

1. **Test Activation**
   ```
   "Write a Python function that reads a file"
   [Should activate python-expert]
   ```

2. **Test Guidance Quality**
   - Is advice actionable?
   - Are examples clear?
   - Does it match your expectations?

3. **Refine Based on Usage**
   - Too broad? → Split into multiple skills
   - Not activating? → Improve description
   - Wrong guidance? → Update instructions

---

## Troubleshooting

### Skill Not Activating

**Problem**: Skill doesn't trigger when expected

**Solutions**:
1. Check description is clear and specific
2. Use explicit invocation: "Use [skill-name] skill"
3. Add more trigger keywords
4. Test with direct activation

### Skill Gives Wrong Guidance

**Problem**: Skill provides incorrect or outdated advice

**Solutions**:
1. Update instructions section
2. Add counter-examples
3. Include caveats and notes
4. Test with various scenarios

### Skills Conflicting

**Problem**: Multiple skills activate and conflict

**Solutions**:
1. Make descriptions more specific
2. Narrow each skill's scope
3. Remove overlapping skills
4. Explicitly invoke desired skill

### Skill Too Broad

**Problem**: Skill tries to do too much

**Solutions**:
1. Split into multiple focused skills
2. Create skill hierarchy
3. Use sub-skills for specific areas
4. Keep each skill single-purpose

---

## Skill Maintenance

### Regular Review

**Monthly**:
- Review skill usage
- Update outdated guidance
- Add new patterns discovered
- Remove unused skills

**Quarterly**:
- Major updates for new language versions
- Add new best practices
- Reorganize if needed
- Share improvements with team

### Version Control

```
.claude/skills/
├── python-expert/
│   ├── SKILL.md
│   ├── CHANGELOG.md    # Track changes
│   └── examples/
```

### Documentation

Document your skills:
- Purpose and scope
- When to use
- Example activations
- Maintenance notes

---

## Skill Library Index

### General Programming
- code-reviewer
- test-strategist
- documentation-writer
- performance-optimizer
- security-auditor

### Languages
- python-expert
- javascript-patterns
- typescript-advisor
- go-best-practices
- rust-guide

### Frameworks
- react-patterns
- django-advisor
- flask-best-practices
- fastapi-guide

### Data & ML
- pandas-expert
- numpy-advisor
- ml-strategist
- data-validation

### DevOps
- docker-expert
- kubernetes-guide
- ci-cd-advisor
- terraform-patterns

### Databases
- sql-optimizer
- postgres-advisor
- mongodb-patterns
- redis-guide

---

**Remember**: Skills are most effective when they're:
- Focused on one domain
- Provide actionable guidance
- Include concrete examples
- Regularly updated
- Well-tested

Start with a few essential skills and grow your library organically based on actual needs.
