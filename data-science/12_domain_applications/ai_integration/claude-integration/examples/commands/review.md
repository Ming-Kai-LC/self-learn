---
description: Comprehensive code review of recent changes
allowed-tools: [Bash(git:*), Read, Grep]
model: sonnet
---

# Code Review

Perform a comprehensive code review of recent changes.

## What Changed

**Git Status:**
!`git status --short`

**Modified Files:**
!`git diff --name-only`

**Full Diff:**
!`git diff`

## Review Checklist

Please review the changes for:

### 1. **Security**
- Input validation
- SQL injection risks
- XSS vulnerabilities
- Authentication/authorization
- Sensitive data exposure

### 2. **Code Quality**
- Clear, descriptive naming
- Function length and complexity
- Code duplication
- Proper error handling
- Appropriate comments

### 3. **Best Practices**
- Language/framework conventions
- Design patterns
- Error handling
- Resource management
- Type safety

### 4. **Performance**
- Efficient algorithms
- Database query optimization
- Unnecessary operations
- Memory management

### 5. **Testing**
- Test coverage
- Edge cases handled
- Error conditions tested

### 6. **Documentation**
- Code comments where needed
- README updates
- API documentation
- Changelog updates

## Output Format

For each issue found:
1. **Severity**: Critical / High / Medium / Low / Info
2. **File and Line**: Exact location
3. **Issue**: What's wrong
4. **Recommendation**: How to fix it

## Summary

Provide:
- Overall assessment
- Number of issues by severity
- Recommendations for improvement
- Positive observations
