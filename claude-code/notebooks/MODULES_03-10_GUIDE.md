# Modules 03-10: Learning Guide

**Learn by Doing with Claude Code**

---

## How to Use This Guide

Modules 03-10 are designed for **hands-on learning with Claude Code**. Instead of reading through pre-written notebooks, you'll:

1. **Read the module objectives and concepts**
2. **Practice directly with Claude Code** using the provided exercises
3. **Build real projects** that demonstrate mastery
4. **Check your understanding** with self-assessment questions

This approach helps you:
- ✅ Learn through actual practice
- ✅ Build muscle memory with Claude Code
- ✅ Create real, useful components
- ✅ Get immediate feedback

---

## Module 03: Working with Skills

**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 120 minutes
**Prerequisites**: Modules 00-02

### Learning Objectives

By the end of this module, you will:
1. Understand skill architecture and lifecycle
2. Use existing skills effectively
3. Know when skills activate automatically
4. Create your first simple skill
5. Understand project vs personal skills
6. Read and interpret SKILL.md format

### Core Concepts

**What Are Skills?**
```
Skills = AI-invoked domain expertise

- Automatic activation based on context
- Provide specialized knowledge and patterns
- Located in .claude/skills/ (project) or ~/.claude/skills/ (personal)
- Different from slash commands (which are user-invoked)
```

**Skill vs Command**:
| Feature | Skill | Slash Command |
|---------|-------|---------------|
| **Activation** | Automatic (AI detects context) | Manual (you type /command) |
| **Purpose** | Domain expertise, patterns | Reusable prompts |
| **Complexity** | Can be comprehensive | Usually concise |
| **Example** | React best practices | `/review-pr` |

### Hands-On Exercises

#### Exercise 1: Explore Existing Skills ⭐

**Task**: Discover what skills are available in this project

With Claude Code:
```
1. "Show me all skill files in .claude/skills/"
2. "Read the data-science-educator skill"
3. "What skills are available in this project?"
```

**What to observe**:
- SKILL.md file structure
- Description field (triggers activation)
- Instructions section
- Examples and reference materials

---

#### Exercise 2: Trigger Skill Activation ⭐

**Task**: Make a skill activate automatically

With Claude Code:
```
1. "Explain how to use pandas groupby for aggregation"
   → Should activate data-science-educator skill

2. "Review this notebook for educational quality"
   → Should activate notebook-tester skill

3. "Help me create a new educational notebook"
   → Should activate notebook-creator skill
```

**What to observe**:
- How Claude mentions which skill activated
- How the response style changes
- Domain-specific guidance provided

---

#### Exercise 3: Create Your First Skill ⭐⭐

**Task**: Create a simple skill for code review

1. **Plan the skill**:
   ```
   Name: code-quality-reviewer
   Purpose: Review code for quality, style, and best practices
   Activation: When user asks for code review
   ```

2. **Create with Claude Code**:
   ```
   "Create a new skill in .claude/skills/ called code-quality-reviewer
    that reviews code for:
    - Code quality and readability
    - Following PEP 8 (Python) or style guides
    - Potential bugs
    - Best practices
    - Security issues"
   ```

3. **Test the skill**:
   ```
   "Review this Python function for code quality:

    def calc(x,y):
        return x+y*2
   "
   ```

**Expected outcome**: Claude should use your new skill and provide structured code review

---

#### Exercise 4: Project vs Personal Skills ⭐⭐

**Task**: Understand the difference

| Project Skills (`.claude/skills/`) | Personal Skills (`~/.claude/skills/`) |
|--------------------------------------|---------------------------------------|
| Shared with team via git | Not shared (gitignored) |
| Project-specific patterns | Your personal preferences |
| Example: "Our API conventions" | Example: "My code style" |

**Practice**:
```
1. "Create a project skill for our Python testing standards"
2. "Where would I put a skill for my personal code preferences?"
```

---

### Skill Best Practices

✅ **Do**:
- Write clear, specific descriptions
- Include examples in the skill
- Focus on one domain per skill
- Keep instructions actionable
- Test activation patterns

❌ **Don't**:
- Make skills too broad
- Overlap with existing skills
- Include secrets/credentials
- Make skills project-specific when they should be personal

### Self-Assessment

1. What's the difference between a skill and a slash command?
2. How does a skill know when to activate?
3. Where do project skills live vs personal skills?
4. Can you force a skill to activate explicitly?
5. What makes a good skill description?

---

## Module 04: Custom Slash Commands

**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 120 minutes
**Prerequisites**: Module 03

### Learning Objectives

By the end of this module, you will:
1. Create simple slash commands
2. Use $ARGUMENTS for parameterization
3. Organize commands with namespacing
4. Understand command scopes (project vs personal)
5. Build a library of useful commands
6. Know when to use commands vs skills

### Core Concepts

**What Are Slash Commands?**
```
Slash Commands = Reusable prompts you invoke manually

- Start with /
- Simple markdown files
- Can accept $ARGUMENTS
- Located in .claude/commands/ or ~/.claude/commands/
```

**Basic Structure**:
```markdown
# .claude/commands/review-pr.md

Review this pull request for:
- Code quality and style
- Potential bugs
- Security vulnerabilities
- Test coverage
- Documentation completeness

Provide actionable feedback.
```

**Usage**: Type `/review-pr` in Claude Code

### Hands-On Exercises

#### Exercise 1: Create Your First Command ⭐

**Task**: Create a simple code review command

With Claude Code:
```
"Create a slash command called 'review' in .claude/commands/
 that reviews code for quality, bugs, and best practices"
```

**Test it**:
```
/review

[Then provide some code to review]
```

---

#### Exercise 2: Parameterized Commands ⭐⭐

**Task**: Create a command that accepts arguments

**Create**:
```markdown
# .claude/commands/test.md

Create comprehensive tests for $ARGUMENTS including:
- Unit tests for all public methods
- Edge cases and boundary conditions
- Error handling scenarios
- Integration tests if applicable
- Mock external dependencies

Follow pytest conventions.
```

**Usage**:
```
/test UserService.py
/test calculate_total function
```

The `$ARGUMENTS` placeholder gets replaced with what you type after the command.

---

#### Exercise 3: Namespaced Commands ⭐⭐

**Task**: Organize commands into categories

**Structure**:
```
.claude/commands/
├── review/
│   ├── code.md          → /review/code
│   ├── security.md      → /review/security
│   └── performance.md   → /review/performance
├── generate/
│   ├── tests.md         → /generate/tests
│   ├── docs.md          → /generate/docs
│   └── types.md         → /generate/types
└── refactor/
    ├── extract.md       → /refactor/extract
    └── simplify.md      → /refactor/simplify
```

**Practice with Claude Code**:
```
"Create a namespace of commands for 'generate':
 - /generate/tests - creates tests
 - /generate/docs - creates documentation
 - /generate/types - creates TypeScript types"
```

---

#### Exercise 4: Build Your Command Library ⭐⭐⭐

**Task**: Create 5 useful commands for your workflow

Suggestions:
1. `/explain` - Explain code in detail
2. `/optimize` - Suggest optimizations
3. `/debug` - Help debug an error
4. `/document` - Add documentation
5. `/refactor` - Refactor code

**Create them all**:
```
"Create these 5 commands in .claude/commands/:
1. explain - explains code step by step
2. optimize - suggests performance improvements
3. debug - helps troubleshoot errors
4. document - adds comprehensive documentation
5. refactor - refactors code following best practices"
```

---

### Command vs Skill Decision

```
Use a Command when:
✅ Frequently repeat the same prompt
✅ Want manual control over when it activates
✅ Simple, focused task
✅ Need parameterization

Use a Skill when:
✅ Want automatic activation
✅ Complex domain expertise
✅ Context-dependent guidance
✅ Comprehensive patterns
```

### Self-Assessment

1. How do you invoke a slash command?
2. What does $ARGUMENTS do?
3. How do you organize commands into namespaces?
4. What's the difference between project and personal commands?
5. When would you use a command vs a skill?

---

## Module 05: Hooks and Automation

**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 150 minutes
**Prerequisites**: Modules 03-04

### Learning Objectives

By the end of this module, you will:
1. Understand hook types and events
2. Create validation hooks
3. Implement automated quality gates
4. Debug hook failures
5. Follow hook best practices
6. Build a pre-commit workflow

### Core Concepts

**What Are Hooks?**
```
Hooks = Event-driven automation

- Run automatically on events (tool_call, user_prompt_submit, etc.)
- Can validate, block, or enhance operations
- Bash scripts that exit 0 (allow) or non-zero (block)
- Configured in .claude/settings.json
```

**Hook Events**:
| Event | When It Triggers | Use Case |
|-------|-----------------|----------|
| `tool_call` | Before/after tool execution | Validate file operations |
| `user_prompt_submit` | When you send a message | Pre-process requests |
| `assistant_message` | When Claude responds | Post-process responses |

### Hands-On Exercises

#### Exercise 1: Create a Simple Hook ⭐

**Task**: Create a hook that logs all Bash tool usage

**Create the hook script**:
```bash
# .claude/hooks/log-bash.sh
#!/bin/bash

if [[ "$TOOL_NAME" == "Bash" ]]; then
  echo "[$(date)] Bash command: $TOOL_ARGS" >> .claude/logs/bash-history.log
fi

exit 0  # Always allow
```

**Enable in settings.json**:
```json
{
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": ["bash .claude/hooks/log-bash.sh"]
    }
  }
}
```

**Test**:
```
"Run ls command"
[Check .claude/logs/bash-history.log]
```

---

#### Exercise 2: Validation Hook ⭐⭐

**Task**: Block writes to production config

```bash
# .claude/hooks/protect-production.sh
#!/bin/bash

# Block writes to production.json
if [[ "$TOOL_NAME" == "Write" && "$TOOL_ARGS" == *"production.json"* ]]; then
  echo "❌ BLOCKED: Cannot write to production.json"
  echo "Use staging.json for testing"
  exit 1  # Block the operation
fi

exit 0  # Allow everything else
```

**Test**:
```
"Create a file config/production.json"
[Should be blocked by hook]

"Create a file config/staging.json"
[Should succeed]
```

---

#### Exercise 3: Pre-Commit Quality Gate ⭐⭐⭐

**Task**: Run linting before commits

```bash
# .claude/hooks/pre-commit-lint.sh
#!/bin/bash

if [[ "$TOOL_NAME" == "Bash" && "$TOOL_ARGS" == *"git commit"* ]]; then
  echo "Running linter before commit..."

  # Run your linter (example with Python)
  if command -v flake8 &> /dev/null; then
    flake8 . || {
      echo "❌ Linting failed! Fix issues before committing."
      exit 1
    }
  fi

  echo "✅ Linting passed"
fi

exit 0
```

**Test the workflow**:
```
1. "Make a small change to a Python file"
2. "Commit the changes"
   → Hook runs linter automatically
   → Blocks if linting fails
```

---

#### Exercise 4: Auto-Formatting Hook ⭐⭐⭐

**Task**: Format code before committing

```bash
# .claude/hooks/auto-format.sh
#!/bin/bash

if [[ "$TOOL_NAME" == "Bash" && "$TOOL_ARGS" == *"git commit"* ]]; then
  echo "Auto-formatting code..."

  # Format Python files
  if command -v black &> /dev/null; then
    black . --quiet
  fi

  # Format JavaScript files
  if command -v prettier &> /dev/null; then
    prettier --write "**/*.{js,ts,tsx}" --log-level silent
  fi

  echo "✅ Code formatted"
fi

exit 0
```

---

### Hook Best Practices

✅ **Do**:
- Keep hooks fast (<2 seconds)
- Provide clear error messages
- Make hooks optional (easy to disable)
- Log hook activity
- Test hooks thoroughly

❌ **Don't**:
- Block operations frivolously
- Make hooks too slow
- Forget to handle errors
- Require user input in hooks
- Skip testing before enabling

### Hook Debugging

```bash
# Add debugging to hooks
#!/bin/bash

# Log everything for debugging
{
  echo "=== Hook Debug ==="
  echo "Event: $HOOK_EVENT"
  echo "Tool: $TOOL_NAME"
  echo "Args: $TOOL_ARGS"
  echo "=================="
} >> .claude/logs/hook-debug.log

# Your hook logic here
exit 0
```

### Self-Assessment

1. What are the three hook events?
2. How do you block an operation in a hook?
3. Where are hooks configured?
4. What should a hook exit code be to allow an operation?
5. Name 3 use cases for hooks

---

## Module 06: MCP Servers and Integrations

**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 180 minutes
**Prerequisites**: Modules 03-05

### Learning Objectives

By the end of this module, you will:
1. Understand Model Context Protocol (MCP)
2. Install and configure MCP servers
3. Use MCP servers for external integrations
4. Know common MCP servers and their purposes
5. Configure authentication for MCP servers
6. Understand when to use MCP vs other approaches

### Core Concepts

**What is MCP?**
```
MCP (Model Context Protocol) = Standard for extending Claude Code

- Connects Claude to external services
- Provides additional tools and data sources
- Examples: GitHub API, databases, file systems, web scraping
- Configured in .claude/settings.json or settings.local.json
```

**Common MCP Servers**:
| Server | Purpose | Package |
|--------|---------|---------|
| filesystem | Access files outside project | `@modelcontextprotocol/server-filesystem` |
| github | GitHub API integration | `@modelcontextprotocol/server-github` |
| postgres | Database queries | `@modelcontextprotocol/server-postgres` |
| puppeteer | Browser automation | `@modelcontextprotocol/server-puppeteer` |

### Hands-On Exercises

#### Exercise 1: Install GitHub MCP Server ⭐⭐

**Task**: Set up GitHub integration

1. **Install**:
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Configure** (.claude/settings.local.json):
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_TOKEN": "your-token-here"
         }
       }
     }
   }
   ```

3. **Test**:
   ```
   "Fetch the latest issues from repository owner/repo"
   "Show me pull requests from my GitHub repository"
   ```

---

#### Exercise 2: Filesystem MCP Server ⭐⭐

**Task**: Access files outside your project directory

1. **Install and configure**:
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

2. **Configure**:
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": [
           "-y",
           "@modelcontextprotocol/server-filesystem",
           "/path/to/allowed/directory"
         ]
       }
     }
   }
   ```

3. **Test**:
   ```
   "List files in /path/to/allowed/directory"
   "Read a file from outside this project"
   ```

---

#### Exercise 3: Database Integration ⭐⭐⭐

**Task**: Query a PostgreSQL database

1. **Setup**:
   ```bash
   npm install -g @modelcontextprotocol/server-postgres
   ```

2. **Configure**:
   ```json
   {
     "mcpServers": {
       "postgres": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-postgres"],
         "env": {
           "DATABASE_URL": "postgresql://user:pass@localhost/db"
         }
       }
     }
   }
   ```

3. **Query**:
   ```
   "Show me all tables in the database"
   "Query the users table for recent signups"
   "Explain the schema of the orders table"
   ```

---

### MCP Security Best Practices

✅ **Do**:
- Store tokens in `.claude/settings.local.json` (gitignored)
- Use environment variables for secrets
- Limit MCP server permissions
- Review what data servers can access
- Use read-only access when possible

❌ **Don't**:
- Commit credentials to git
- Give MCP servers unnecessary permissions
- Trust third-party MCP servers blindly
- Skip reviewing MCP server code

### When to Use MCP

**Use MCP when**:
- Need to access external APIs
- Want to query databases
- Need browser automation
- Integrating with third-party services
- Accessing files outside project

**Don't use MCP when**:
- Built-in tools suffice (Read, Write, etc.)
- Simple terminal commands work (Bash tool)
- Can be done with skills/commands

### Self-Assessment

1. What does MCP stand for?
2. Name 3 common MCP servers
3. Where should you store MCP server credentials?
4. How do you test if an MCP server is working?
5. When would you use MCP vs a Bash command?

---

## Module 07: Subagents and Orchestration

**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 180 minutes
**Prerequisites**: Modules 03-06

### Learning Objectives

By the end of this module, you will:
1. Understand subagent architecture
2. Use the Task tool to delegate work
3. Create custom subagent definitions
4. Run agents in parallel
5. Design multi-agent workflows
6. Understand agent tool permissions

### Core Concepts

**What Are Subagents?**
```
Subagents = Specialized AI assistants for specific tasks

- Run independently with their own tool access
- Can execute in parallel
- Defined in .claude/agents/
- Stateless (all context in initial prompt)
- Return results to main conversation
```

**When to Use Subagents**:
- Complex, multi-step tasks
- Tasks requiring specialized focus
- Operations that benefit from parallel execution
- Code reviews, testing, refactoring

### Hands-On Exercises

#### Exercise 1: Use Built-in Task Tool ⭐

**Task**: Delegate a code review

With Claude Code:
```
"Use the Task tool to review src/auth.py for:
 - Code quality
 - Security issues
 - Best practices
 - Potential bugs"
```

**Observe**:
- How the task is delegated
- The agent's focused analysis
- Structured results returned

---

#### Exercise 2: Create a Code Reviewer Agent ⭐⭐

**Task**: Define a custom subagent for code review

**Create** (`.claude/agents/code-reviewer.md`):
```markdown
# code-reviewer

description: Reviews code for quality, security, and best practices

## Tools Available
- Read
- Grep
- Glob

## Instructions
Review code thoroughly for:

1. **Code Quality**
   - Readability and clarity
   - Proper naming conventions
   - Code organization
   - Comments and documentation

2. **Security**
   - SQL injection vulnerabilities
   - XSS vulnerabilities
   - Authentication/authorization issues
   - Sensitive data exposure

3. **Best Practices**
   - DRY principle
   - SOLID principles
   - Language-specific idioms
   - Error handling

4. **Potential Bugs**
   - Null pointer exceptions
   - Off-by-one errors
   - Race conditions
   - Resource leaks

## Output Format
Provide:
- **Summary**: Overall assessment
- **Critical Issues**: Must-fix problems
- **Improvements**: Suggestions for better code
- **Positive**: What's done well
```

**Use it**:
```
"Use the code-reviewer agent to review src/utils.py"
```

---

#### Exercise 3: Test Generator Agent ⭐⭐⭐

**Task**: Create an agent that generates tests

**Create** (`.claude/agents/test-generator.md`):
```markdown
# test-generator

description: Generates comprehensive test suites

## Tools Available
- Read
- Write
- Grep

## Instructions
Generate comprehensive tests including:

1. **Unit Tests**
   - Test all public methods
   - Test with valid inputs
   - Test return values
   - Test side effects

2. **Edge Cases**
   - Boundary values
   - Empty inputs
   - Maximum values
   - Minimum values

3. **Error Handling**
   - Invalid inputs
   - Exception cases
   - Error messages
   - Recovery behavior

4. **Integration Tests**
   - Component interactions
   - External dependencies (mocked)
   - End-to-end scenarios

Use pytest conventions:
- Descriptive test names
- Arrange-Act-Assert pattern
- Fixtures for setup
- Parametrize for multiple cases

## Output Format
Create test file with:
- Test class/module
- Setup and teardown
- Well-documented tests
- Clear assertions
```

**Use it**:
```
"Use the test-generator agent to create tests for src/calculator.py"
```

---

#### Exercise 4: Parallel Agent Execution ⭐⭐⭐

**Task**: Run multiple agents simultaneously

With Claude Code:
```
"Run these agents in parallel:
1. code-reviewer - review src/api.py
2. test-generator - create tests for src/api.py
3. Use another agent to check documentation completeness"
```

**Observe**:
- Parallel execution
- Faster completion
- Independent results
- How results are aggregated

---

### Subagent Best Practices

✅ **Do**:
- Give agents clear, focused tasks
- Limit tool access to what's needed
- Provide structured output format
- Make agents reusable
- Test agents individually first

❌ **Don't**:
- Give agents too broad a task
- Grant unnecessary tool access
- Forget agents are stateless
- Make agents interactive (they can't ask questions)
- Skip defining output format

### Agent Orchestration Patterns

**Sequential** (one after another):
```
1. Code-reviewer analyzes code
2. Test-generator creates tests based on findings
3. Documentation agent updates docs
```

**Parallel** (simultaneously):
```
[Code-reviewer] + [Test-generator] + [Doc-updater]
→ All run at once, results combined
```

**Hierarchical** (sub-delegation):
```
Main agent
├─ Code-reviewer agent
│  ├─ Security-checker sub-agent
│  └─ Style-checker sub-agent
└─ Test-generator agent
```

### Self-Assessment

1. What is a subagent?
2. How do you invoke a subagent?
3. Can subagents access all tools?
4. What's the difference between sequential and parallel execution?
5. When should you create a custom subagent?

---

## Module 08: Advanced Workflows

**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 240 minutes
**Prerequisites**: Modules 03-07

### Learning Objectives

By the end of this module, you will:
1. Design multi-step automation workflows
2. Combine skills, commands, hooks, and agents
3. Implement error handling and recovery
4. Build production-ready workflows
5. Optimize workflow performance
6. Document and maintain workflows

### Core Concepts

**Workflow Design**:
```
Workflow = Skills + Commands + Hooks + Agents + Tools

Components work together:
- Skills provide domain expertise
- Commands trigger workflows
- Hooks validate and automate
- Agents handle complex sub-tasks
- Tools execute operations
```

### Hands-On Projects

#### Project 1: Automated Code Review Workflow ⭐⭐

**Goal**: Complete PR review automation

**Components**:
1. Slash command: `/review-pr`
2. Hook: Pre-review validation
3. Subagent: Code reviewer
4. Subagent: Test coverage checker
5. Final report generation

**Build it**:
```
"Help me build an automated PR review workflow that:
1. Is triggered with /review-pr
2. Runs a hook to validate the PR has description
3. Uses code-reviewer agent for code analysis
4. Uses test-coverage agent to check tests
5. Generates a markdown report
6. Posts findings as PR comment (if gh CLI available)"
```

---

#### Project 2: Documentation Pipeline ⭐⭐⭐

**Goal**: Auto-generate and update documentation

**Workflow**:
```
Code Change → Hook Triggers → Doc Generator → Review → Commit
```

**Build it**:
```
"Create a documentation pipeline that:
1. Detects when code changes (hook on git commit)
2. Analyzes changed files
3. Uses doc-generator agent to update docs
4. Reviews docs for completeness
5. Commits docs with code changes"
```

---

#### Project 3: Testing Automation Suite ⭐⭐⭐

**Goal**: Comprehensive testing workflow

**Components**:
- Command: `/test-all`
- Agents: Unit test generator, integration test generator
- Hook: Pre-commit test runner
- Skill: Testing best practices

**Build it**:
```
"Build a testing automation suite:
1. /test-all command triggers full test generation
2. Unit test agent generates unit tests
3. Integration test agent generates integration tests
4. Pre-commit hook runs all tests
5. Blocks commit if tests fail
6. Testing skill provides guidance"
```

---

#### Project 4: Release Management Workflow ⭐⭐⭐

**Goal**: Automated release process

**Workflow**:
```
/release → Version Bump → Changelog → Tests → Build → Tag → Push
```

**Build it**:
```
"Create a release management workflow:
1. /release command starts process
2. Bump version numbers
3. Generate changelog from commits
4. Run full test suite
5. Build production bundle
6. Create git tag
7. Push to repository
8. Optionally create GitHub release"
```

---

### Error Handling Patterns

**Graceful Degradation**:
```bash
# Hook with fallback
if ! command -v linter &> /dev/null; then
  echo "⚠️  Linter not found, skipping"
  exit 0  # Continue without linting
fi
```

**Retry Logic**:
```bash
# Retry failed operations
for i in {1..3}; do
  npm test && break
  echo "Test failed, retrying ($i/3)..."
  sleep 2
done
```

**User Notification**:
```bash
# Clear error messages
if [ $? -ne 0 ]; then
  echo "❌ Operation failed!"
  echo "Reason: Test suite returned errors"
  echo "Action: Fix failing tests and try again"
  exit 1
fi
```

### Workflow Optimization

✅ **Do**:
- Run independent tasks in parallel
- Cache results when possible
- Fail fast on critical errors
- Provide progress indicators
- Log detailed execution info

❌ **Don't**:
- Make workflows too complex
- Forget error handling
- Skip testing workflows
- Hard-code values
- Ignore performance

### Self-Assessment Project

**Build a complete workflow** that demonstrates:
1. Slash command integration
2. Hook validation
3. Subagent delegation
4. Error handling
5. Parallel execution where applicable
6. Comprehensive documentation

---

## Module 09: Best Practices and Optimization

**Difficulty**: ⭐⭐⭐ Expert
**Estimated Time**: 180 minutes
**Prerequisites**: Modules 03-08

### Learning Objectives

By the end of this module, you will:
1. Master prompt engineering for Claude Code
2. Optimize token usage effectively
3. Implement security best practices
4. Design team collaboration patterns
5. Monitor and measure effectiveness
6. Follow industry standards

### Key Topics

#### 1. Prompt Engineering

**Effective Prompts**:
```
❌ Bad: "Fix the code"
✅ Good: "Fix the authentication bug in src/auth.py line 45 where
         null users aren't handled properly"

❌ Bad: "Add tests"
✅ Good: "Add pytest unit tests for the login() function covering:
         - Successful login
         - Invalid credentials
         - Null username
         - Null password"
```

**Providing Context**:
```
✅ Include:
- What you're trying to achieve
- Relevant background
- Constraints or requirements
- Expected outcome
- Code style preferences

❌ Avoid:
- Vague requests
- Missing context
- Assuming Claude remembers everything
- Unclear success criteria
```

---

#### 2. Token Management

**Token Optimization Strategies**:

1. **Use `/clear` Between Tasks**:
   ```
   Task A: Feature implementation ✅
   /clear
   Task B: Bug fix in different module
   ```

2. **Concise Output Style**:
   ```json
   {
     "output_style": "concise"
   }
   ```

3. **Read Selectively**:
   ```
   ❌ "Read all Python files"
   ✅ "Read src/auth.py lines 45-60"
   ```

4. **Break Large Tasks**:
   ```
   Instead of: "Refactor entire authentication system"

   Break into:
   Session 1: "Refactor login function"
   Session 2: "Refactor token management"
   Session 3: "Update tests"
   ```

---

#### 3. Security Best Practices

**Never Commit**:
- API keys, tokens, passwords
- .claude/settings.local.json
- Private credentials in skills/commands

**Always**:
- Use environment variables
- Store secrets in local settings
- Review hooks before enabling
- Audit MCP server permissions
- Use read-only access when possible

**Security Checklist**:
```
✅ API keys in environment variables
✅ settings.local.json in .gitignore
✅ Hooks validated and tested
✅ MCP servers from trusted sources
✅ Regular security audits
✅ Principle of least privilege
```

---

#### 4. Team Collaboration

**Project Structure**:
```
.claude/
├── skills/              # Shared team expertise
├── commands/            # Team workflows
├── agents/              # Shared subagents
├── hooks/               # Quality gates
├── settings.json        # Team defaults
└── .gitignore          # Ignore local settings
```

**What to Share** (commit to git):
- Project skills
- Team commands
- Shared agents
- Documentation
- Standard hooks

**What to Keep Local** (gitignore):
- settings.local.json
- Personal preferences
- API credentials
- Cache files

**Team Standards Document**:
```markdown
# Team Claude Code Standards

## Commit Message Format
[Component] Action: Description

## Code Review Command
/review-pr for all PRs

## Required Hooks
- pre-commit: linting
- pre-commit: tests

## Naming Conventions
- Commands: kebab-case
- Skills: descriptive-name
- Agents: noun-role
```

---

#### 5. Performance Monitoring

**What to Track**:
- Token usage per session
- Common command usage
- Hook execution time
- Agent success rate
- User satisfaction

**Optimization Metrics**:
```
Good Performance:
- Most sessions < 50k tokens
- Hooks complete in < 2s
- Agents succeed > 90%
- Clear error messages
- Fast command response

Needs Improvement:
- Frequent token limit hits
- Slow hooks (> 5s)
- Agent failures > 20%
- Unclear error messages
- Slow tool selection
```

---

### Best Practices Checklist

**Daily Operations**:
- [ ] Use `/clear` between unrelated tasks
- [ ] Read files before editing
- [ ] Review diffs before committing
- [ ] Provide specific, clear prompts
- [ ] Test changes before pushing

**Weekly Maintenance**:
- [ ] Review and update skills
- [ ] Clean up unused commands
- [ ] Update documentation
- [ ] Test all hooks
- [ ] Review MCP server permissions

**Monthly Review**:
- [ ] Audit security practices
- [ ] Optimize workflows
- [ ] Update team standards
- [ ] Review token usage patterns
- [ ] Update Claude Code

---

## Module 10: Final Project - Building a Custom Plugin

**Difficulty**: ⭐⭐⭐ Expert
**Estimated Time**: 300+ minutes
**Prerequisites**: Modules 03-09

### Learning Objectives

By the end of this module, you will:
1. Design a complete plugin architecture
2. Package skills, commands, hooks, and agents
3. Implement comprehensive documentation
4. Test and validate your plugin
5. Version and distribute your plugin
6. Maintain and update your plugin

### Project Requirements

Build a complete plugin that includes:
- ✅ At least 2 skills
- ✅ At least 3 slash commands
- ✅ At least 1 hook
- ✅ At least 1 subagent
- ✅ Comprehensive README
- ✅ Usage examples
- ✅ Test suite
- ✅ Installation instructions

### Project Options

Choose one (or design your own):

#### Option A: Development Workflow Plugin ⭐⭐⭐

**Goal**: Automate development workflows

**Components**:
- Skills: Code review patterns, testing strategies
- Commands: /review, /test, /deploy
- Hooks: Pre-commit linting, test runner
- Agents: Code reviewer, test generator

---

#### Option B: Data Science Assistant Plugin ⭐⭐⭐

**Goal**: Educational notebook quality automation

**Components**:
- Skills: Pandas best practices, visualization standards
- Commands: /check-quality, /add-exercises, /test-notebook
- Hooks: Validate notebook before commit
- Agents: Quality checker, exercise generator

---

#### Option C: Documentation Generator Plugin ⭐⭐⭐

**Goal**: Automatic documentation generation

**Components**:
- Skills: Documentation patterns, API doc standards
- Commands: /gen-docs, /update-readme, /api-docs
- Hooks: Sync docs with code changes
- Agents: Doc generator, API documenter

---

#### Option D: Custom Domain Plugin ⭐⭐⭐

**Goal**: Build for your specific use case

Design and implement a plugin for:
- Your domain expertise
- Your workflow needs
- Your team's requirements
- Your project type

---

### Plugin Structure

```
my-awesome-plugin/
├── .claude/
│   ├── skills/
│   │   ├── skill-1/
│   │   │   ├── SKILL.md
│   │   │   └── examples/
│   │   └── skill-2/
│   │       └── SKILL.md
│   ├── commands/
│   │   ├── command-1.md
│   │   ├── command-2.md
│   │   └── namespace/
│   │       └── command-3.md
│   ├── agents/
│   │   ├── agent-1.md
│   │   └── agent-2.md
│   ├── hooks/
│   │   ├── pre-commit.sh
│   │   └── validate.sh
│   └── settings.json
├── docs/
│   ├── README.md
│   ├── USAGE.md
│   └── EXAMPLES.md
├── tests/
│   └── test-plugin.sh
├── examples/
│   └── sample-project/
├── .gitignore
├── LICENSE
└── CHANGELOG.md
```

### Deliverables

1. **Complete Plugin Codebase**
   - All skills, commands, hooks, agents
   - Properly organized
   - Well-documented

2. **README.md**
   - What the plugin does
   - Installation instructions
   - Quick start guide
   - Complete feature list

3. **USAGE.md**
   - Detailed usage for each component
   - Common workflows
   - Troubleshooting guide

4. **EXAMPLES.md**
   - Real-world use cases
   - Step-by-step tutorials
   - Best practices

5. **Test Suite**
   - Test all components
   - Validation scripts
   - Example test cases

6. **CHANGELOG.md**
   - Version history
   - Breaking changes
   - Migration guides

### Success Criteria

Your plugin is complete when:
- ✅ All components work independently
- ✅ Components work together seamlessly
- ✅ Documentation is comprehensive
- ✅ Tests pass successfully
- ✅ Examples are clear and functional
- ✅ Installation is straightforward
- ✅ You've dogfooded it yourself
- ✅ Ready to share with others

---

## Conclusion

**Congratulations!** You've completed the Claude Code Mastery learning path.

You now know how to:
- ✅ Use all core tools effectively
- ✅ Create and use skills
- ✅ Build custom slash commands
- ✅ Implement hooks for automation
- ✅ Integrate with external services via MCP
- ✅ Orchestrate subagents
- ✅ Build complex workflows
- ✅ Follow best practices
- ✅ Create production-ready plugins

### Next Steps

1. **Build Your Plugin**: Complete the final project
2. **Share with Community**: Publish your work
3. **Keep Learning**: Explore advanced MCP servers
4. **Contribute**: Help others learn Claude Code
5. **Stay Updated**: Follow Claude Code releases

### Resources

- 📖 [CommandReference.md](../docs/CommandReference.md) - Quick reference
- 📚 [Official Docs](https://docs.anthropic.com/claude-code)
- 💬 [Discord Community](https://discord.gg/claude-developers)
- 🐙 [GitHub](https://github.com/anthropics/claude-code)

---

**Happy Building with Claude Code!** 🚀
