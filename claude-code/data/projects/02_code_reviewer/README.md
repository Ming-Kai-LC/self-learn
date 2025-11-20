# Project 2: Code Review Automator

**Difficulty**: ⭐⭐ Intermediate
**Time**: 3-4 hours
**Modules**: 05-07 (Hooks, MCP, Subagents)

## Project Overview

Build an automated code review system using hooks, subagents, and MCP servers to ensure code quality before commits.

## Learning Goals

- Create validation hooks
- Build specialized subagents
- Integrate with GitHub via MCP
- Automate quality gates
- Design multi-agent workflows

## What You'll Build

A code review automation system with:
- **Pre-commit hooks**: Automatic validation
- **Code reviewer agent**: Quality analysis
- **Security scanner agent**: Vulnerability detection
- **Test coverage agent**: Coverage verification
- **GitHub integration**: PR automation

---

## Architecture

```
Code Change
    ↓
Pre-commit Hook (validation)
    ↓
Code Reviewer Agent (quality)
    ↓
Security Scanner Agent (security)
    ↓
Test Coverage Agent (tests)
    ↓
Generate Report
    ↓
Post to GitHub PR (optional)
```

---

## Step 1: Build the Code Reviewer Agent (60 min)

### Agent Definition

**Create with Claude Code**:
```
"Create a subagent called 'code-reviewer' in .claude/agents/
that analyzes code for:
- Code quality and readability
- Design patterns and architecture
- Error handling
- Performance considerations
- Best practices
Provide structured output with severity levels."
```

### Agent Structure

```markdown
# .claude/agents/code-reviewer.md

description: Reviews code for quality, patterns, and best practices

## Tools Available
- Read
- Grep
- Glob

## Instructions

Analyze the provided code thoroughly:

### Code Quality (High Priority)
- Variable naming (descriptive, consistent)
- Function length (< 50 lines ideal)
- Code duplication (DRY principle)
- Comments (why, not what)
- Magic numbers (use constants)

### Design & Architecture (Medium Priority)
- Separation of concerns
- Single responsibility principle
- Appropriate abstractions
- Dependency management
- Testability

### Error Handling (High Priority)
- Try-except blocks
- Error messages (clear, actionable)
- Resource cleanup
- Edge case handling
- Validation of inputs

### Performance (Low-Medium Priority)
- Algorithmic complexity
- Unnecessary loops
- Database queries (N+1 problem)
- Memory management
- Caching opportunities

## Output Format

### Summary
Brief overview (2-3 sentences)

### Critical Issues 🔴
Must fix before merge:
- [Issue 1 with file:line reference]
- [Issue 2 with file:line reference]

### Major Improvements 🟡
Should address soon:
- [Improvement 1]
- [Improvement 2]

### Minor Suggestions 🟢
Nice to have:
- [Suggestion 1]
- [Suggestion 2]

### Positive Highlights ✨
What's done well:
- [Positive 1]
- [Positive 2]

### Overall Score
[0-10] with justification
```

### Test the Agent

```
"Use the code-reviewer agent to review this file:

# calculator.py
def calc(x,y,z):
    return x+y*z+100

def process(data):
    result = []
    for item in data:
        if item:
            result.append(calc(item,2,3))
    return result
"
```

**Expected output**: Structured review with issues identified

---

## Step 2: Build Security Scanner Agent (45 min)

### Agent Definition

```markdown
# .claude/agents/security-scanner.md

description: Scans code for security vulnerabilities and unsafe practices

## Tools Available
- Read
- Grep

## Instructions

Scan for security issues:

### Injection Vulnerabilities
- SQL injection (string concatenation in queries)
- Command injection (os.system with user input)
- Path traversal (unchecked file paths)
- XSS (unescaped user input in HTML)

### Authentication & Authorization
- Hardcoded credentials
- Weak password policies
- Missing authentication checks
- Insufficient authorization

### Data Exposure
- Logging sensitive data
- API keys in code
- Unencrypted sensitive data
- Information disclosure

### Common Pitfalls
- Use of unsafe functions (eval, exec)
- Insecure randomness
- Missing input validation
- Unsafe deserialization

## Output Format

### Security Score: [0-10]

### Critical Vulnerabilities 🚨
Immediate action required:
- [Vuln with OWASP category and file:line]

### Moderate Risks ⚠️
Should address:
- [Risk with description]

### Best Practice Violations 📋
Consider fixing:
- [Violation with recommendation]

### Compliant Items ✅
Good security practices found:
- [What's done right]
```

### Test Security Scanner

```python
# test_security.py
import os

def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pass='{password}'"
    # SQL injection vulnerability!

    api_key = "sk-1234567890abcdef"  # Hardcoded secret!

    os.system(f"echo {username}")  # Command injection!

    return True
```

```
"Use the security-scanner agent to analyze test_security.py"
```

---

## Step 3: Build Test Coverage Agent (45 min)

### Agent Definition

```markdown
# .claude/agents/test-coverage.md

description: Analyzes test coverage and quality

## Tools Available
- Read
- Grep
- Bash (for running coverage tools)

## Instructions

Analyze test coverage:

### Coverage Metrics
- Line coverage percentage
- Branch coverage
- Function coverage
- Uncovered critical paths

### Test Quality
- Test naming (descriptive)
- Test independence (no ordering)
- Assertions (meaningful)
- Setup/teardown (proper)
- Mocking (appropriate)

### Missing Tests
- Edge cases
- Error conditions
- Boundary values
- Integration points
- Critical business logic

## Output Format

### Coverage Summary
- Overall: X%
- Critical paths: X%
- New code: X%

### Untested Critical Code 🔴
- [Function/module with explanation why critical]

### Test Quality Issues 🟡
- [Issue with test file:line]

### Coverage Recommendations
- [Specific areas needing tests]

### Test Strengths ✅
- [What's well tested]
```

---

## Step 4: Create Pre-Commit Hook (45 min)

### Hook Script

```bash
#!/bin/bash
# .claude/hooks/pre-commit-review.sh

echo "🔍 Running automated code review..."

# Get list of changed Python files
CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ -z "$CHANGED_FILES" ]; then
    echo "✅ No Python files changed"
    exit 0
fi

echo "Files to review:"
echo "$CHANGED_FILES"

# Check if Claude Code is available
if ! command -v claude &> /dev/null; then
    echo "⚠️  Claude Code not found, skipping review"
    exit 0
fi

# Create temporary review request
REVIEW_REQUEST=$(cat <<EOF
Use these agents in parallel to review the changed files:
1. code-reviewer - analyze code quality
2. security-scanner - check for vulnerabilities
3. test-coverage - verify test coverage

Changed files:
$CHANGED_FILES

Provide a summary with:
- Overall status (PASS/FAIL)
- Critical issues that must be fixed
- Approval or rejection recommendation
EOF
)

# Save request to temp file
echo "$REVIEW_REQUEST" > /tmp/claude-review-request.txt

# Log the review
echo "[$(date)] Pre-commit review triggered" >> .claude/logs/reviews.log

# Note: In real usage, this would integrate with Claude Code
# For now, we'll just log and allow the commit
echo "✅ Review logged. Run full review with: /review-commit"

exit 0
```

### Enable the Hook

```json
// .claude/settings.json
{
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": [
        "bash .claude/hooks/pre-commit-review.sh"
      ]
    }
  }
}
```

---

## Step 5: Create Review Command (30 min)

### Main Review Command

```markdown
# .claude/commands/review-commit.md

Run comprehensive code review on staged changes:

1. Identify all staged files
2. Launch parallel review agents:
   - code-reviewer for quality
   - security-scanner for vulnerabilities
   - test-coverage for test analysis
3. Aggregate results
4. Generate report
5. Provide commit recommendation

Format results as:
## Code Review Report

### Overall Assessment
[APPROVED / NEEDS WORK / REJECTED]

### Agent Reports
[Include each agent's findings]

### Recommendation
[Specific actions to take]

### Commit Message Suggestion
[Generated message if approved]
```

---

## Step 6: GitHub Integration (Optional - 60 min)

### Install GitHub MCP Server

```bash
npm install -g @modelcontextprotocol/server-github
```

### Configure

```json
// .claude/settings.local.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your_github_token_here"
      }
    }
  }
}
```

### PR Review Command

```markdown
# .claude/commands/review-pr.md

Review GitHub pull request $ARGUMENTS:

1. Fetch PR details from GitHub
2. Get list of changed files
3. Run parallel agent review
4. Generate review comment
5. Post to PR (if approved)

Review format:
## Automated Code Review

### Code Quality: [Score/10]
[Findings]

### Security: [Score/10]
[Findings]

### Test Coverage: [Score/10]
[Findings]

### Overall: [APPROVED/CHANGES REQUESTED]
[Summary and recommendations]
```

### Usage

```
/review-pr 123

# Or review current branch's PR
/review-pr current
```

---

## Step 7: Test the Complete System (60 min)

### Test Scenario 1: Good Code

```python
# good_example.py
"""User authentication module with secure password handling."""

import bcrypt
from typing import Optional

class UserAuthenticator:
    """Handles user authentication securely."""

    def __init__(self, db_connection):
        """Initialize with database connection.

        Args:
            db_connection: Active database connection
        """
        self.db = db_connection

    def authenticate_user(self, username: str, password: str) -> Optional[dict]:
        """Authenticate user with username and password.

        Args:
            username: User's username
            password: User's plaintext password

        Returns:
            User dict if authenticated, None otherwise
        """
        if not username or not password:
            return None

        # Use parameterized query to prevent SQL injection
        user = self.db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        if not user:
            return None

        # Verify password with bcrypt
        if bcrypt.checkpw(password.encode(), user['password_hash']):
            return {
                'id': user['id'],
                'username': user['username'],
                'email': user['email']
            }

        return None
```

**Test**:
```
1. Stage the file: git add good_example.py
2. Trigger review: /review-commit
3. Expected: Mostly positive feedback
```

---

### Test Scenario 2: Problematic Code

```python
# bad_example.py
import os

def login(user,pass):
    q="SELECT * FROM users WHERE name='"+user+"' AND password='"+pass+"'"
    os.system("echo Logged in: "+user)
    KEY="secret-api-key-12345"
    return True

def getData(id):
    f=open("/data/"+id+".txt")
    return f.read()
```

**Test**:
```
1. Stage: git add bad_example.py
2. Review: /review-commit
3. Expected: Multiple critical issues found
```

---

## Step 8: Generate Review Report (30 min)

### Report Template

```markdown
# .claude/commands/generate-review-report.md

Generate comprehensive review report for the last commit:

## Code Review Report
**Date**: [Date]
**Commit**: [Hash]
**Files Changed**: [Count]

### Executive Summary
[2-3 sentence overview]

### Code Quality Analysis
**Score**: [X/10]
- Critical Issues: [Count]
- Major Improvements: [Count]
- Minor Suggestions: [Count]

[Details]

### Security Analysis
**Score**: [X/10]
- Critical Vulnerabilities: [Count]
- Moderate Risks: [Count]
- Best Practice Violations: [Count]

[Details]

### Test Coverage Analysis
**Score**: [X/10]
- Overall Coverage: [X%]
- Untested Critical Code: [Count]
- Test Quality Issues: [Count]

[Details]

### Overall Recommendation
[APPROVED / NEEDS WORK / REJECTED]

[Specific actions required]

### Positive Highlights
[What was done well]

---
*Generated by Claude Code Review Automator*
```

---

## Project Checklist

- [ ] Built code-reviewer agent
- [ ] Built security-scanner agent
- [ ] Built test-coverage agent
- [ ] Created pre-commit hook
- [ ] Tested with good code
- [ ] Tested with bad code
- [ ] (Optional) Integrated with GitHub
- [ ] Created review commands
- [ ] Generated complete report
- [ ] Documented the system

---

## Success Criteria

Your code review automator is successful when:
- ✅ Catches security vulnerabilities automatically
- ✅ Identifies code quality issues
- ✅ Runs before every commit
- ✅ Provides actionable feedback
- ✅ Generates clear reports
- ✅ Integrates into workflow seamlessly
- ✅ Improves code quality over time

---

## Advanced Extensions

### 1. Customizable Rules

```yaml
# .claude/review-config.yaml
severity_threshold: medium
require_tests: true
coverage_minimum: 80
security_scan: true
performance_check: false
```

### 2. Team-Specific Patterns

```
"Create a skill 'team-standards' with our:
- Code style preferences
- Architecture patterns
- Naming conventions
- Review criteria"
```

### 3. Metrics Dashboard

Track over time:
- Code quality scores
- Security issues found
- Coverage improvements
- Review pass rate

### 4. CI/CD Integration

- Run on pull requests
- Block merges on failures
- Auto-comment on PRs
- Track metrics in CI

---

## Troubleshooting

**Agents not finding issues?**
- Provide example bad code
- Refine agent instructions
- Check tool permissions

**Hook not triggering?**
- Verify hooks enabled in settings
- Check script permissions: `chmod +x`
- Review hook logs

**GitHub integration failing?**
- Verify token has correct permissions
- Check MCP server is running
- Test with simple query first

---

## Next Steps

1. **Refine agents** based on false positives/negatives
2. **Add more agents** (performance, documentation, etc.)
3. **Integrate with CI/CD** pipeline
4. **Share with team** and gather feedback
5. **Move to Project 3**: Documentation Generator

---

**Congratulations!** You've built an automated code review system that will help maintain code quality across your projects.
