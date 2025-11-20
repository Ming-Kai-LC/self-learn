# Claude Code Command Reference

**Comprehensive quick reference guide for all Claude Code commands, tools, and patterns**

Last Updated: 2025-11-20
Version: 2.0 - Complete Reference

---

## Table of Contents

1. [Built-in Slash Commands](#built-in-slash-commands)
2. [Core Tools](#core-tools)
3. [Tool Selection Guide](#tool-selection-guide)
4. [Common Patterns](#common-patterns)
5. [Git Workflows](#git-workflows)
6. [Skills](#skills)
7. [Custom Slash Commands](#custom-slash-commands)
8. [Hooks](#hooks)
9. [MCP Servers](#mcp-servers)
10. [Subagents](#subagents)
11. [Configuration](#configuration)
12. [Troubleshooting](#troubleshooting)

---

## Built-in Slash Commands

### Session Management

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/help` | Show available commands | Learning, seeing custom commands |
| `/clear` | Clear conversation history | Switching tasks, managing tokens |
| `/rewind` | Undo last exchange (your message + Claude's response) | Fixing mistakes, trying different approach |
| `/version` | Show Claude Code version | Checking compatibility, troubleshooting |
| `/bug` | Report a bug to Anthropic | Encountering Claude Code issues |

### Usage Guidelines

**`/help`** - Display Commands
```
Shows all available slash commands (built-in + custom)
Useful for: Discovering features, checking custom commands
```

**`/clear`** - Start Fresh
```
Clears entire conversation history
Resets token usage to zero
Useful for: Task switches, token management, getting unstuck
Warning: Loses all context from current conversation
```

**`/rewind`** - Undo Last Exchange
```
Removes your last message AND Claude's response
Preserves all earlier context
Useful for: Quick fixes, typos, trying different approach
Note: Removes TWO messages (yours + Claude's)
```

**`/version`** - Check Version
```
Displays Claude Code version number
Useful for: Troubleshooting, reporting bugs, checking compatibility
```

**`/bug`** - Report Issues
```
Opens bug report process
Include: Version, OS, steps to reproduce, error messages
```

### Slash Command Best Practices

✅ **Do**:
- Use `/clear` between unrelated tasks
- Use `/rewind` for quick mistake fixes
- Check `/help` to discover custom commands
- Include `/version` in bug reports

❌ **Don't**:
- Use `/clear` mid-task (loses context)
- Forget `/rewind` removes BOTH messages
- Overuse `/help` once you've learned commands

---

## Core Tools

### 1. Read Tool 📖

**Purpose**: View file contents with line numbers

**Parameters**:
```
file_path (required) - Path to file
offset (optional)    - Start reading from line N
limit (optional)     - Read only N lines
```

**Usage Examples**:
```
"Read src/auth.py"
"Show me the contents of config.json"
"Read the first 100 lines of large_file.py"
"What's in the README?"
"Read lines 50-150 of data.csv"
```

**When to Use**:
- ✅ Understanding existing code
- ✅ Analyzing configuration files
- ✅ Reviewing documentation
- ✅ Before editing (best practice)
- ✅ Verifying file contents

**Output Format**:
```
   1→# Authentication Module
   2→import bcrypt
   3→from flask import request
   4→
   5→def login(username, password):
```

**Special Features**:
- Line numbers for easy reference
- Works with text files, images, PDFs
- Can read specific line ranges
- Handles large files efficiently

**Pro Tips**:
- Always read before editing
- Use offset/limit for large files (>1000 lines)
- Line numbers help with precise Edit operations
- Works with any text-based file format

---

### 2. Write Tool ✍️

**Purpose**: Create new files (overwrites if exists!)

**Parameters**:
```
file_path (required) - Where to create file
content (required)   - File contents
```

**Usage Examples**:
```
"Create src/utils/logger.py with logging setup"
"Write a config file for the database connection"
"Generate a README.md file for this project"
"Create a new test file test_utils.py"
```

**When to Use**:
- ✅ Creating new modules or files
- ✅ Generating configuration files
- ✅ Writing documentation from scratch
- ✅ Initializing new components
- ✅ Complete file rewrites (90%+ changes)

**When NOT to Use**:
- ❌ Modifying existing files (use Edit)
- ❌ Making small changes (use Edit)
- ❌ Appending to files (use Edit)
- ❌ Adding functions to existing files (use Edit)

**⚠️ Critical Warning**:
```
Write OVERWRITES existing files completely!
Always use Edit for modifications to preserve content.
```

**Pro Tips**:
- Creates parent directories automatically
- Good for complete rewrites only
- Check if file exists before writing
- Prefer Edit over Write for modifications

---

### 3. Edit Tool ✏️

**Purpose**: Make precise, targeted changes to existing files

**Parameters**:
```
file_path (required)   - File to edit
old_string (required)  - Exact text to find
new_string (required)  - Replacement text
replace_all (optional) - Replace all occurrences (default: false)
```

**Usage Examples**:
```
"Fix the bug in auth.py line 45"
"Add error handling to the login function"
"Rename variable 'temp' to 'user_data'"
"Add a new function to utils.py"
"Update the API endpoint to v2"
```

**When to Use**:
- ✅ Bug fixes in existing code
- ✅ Refactoring functions
- ✅ Adding new functions to files
- ✅ Updating configuration values
- ✅ Renaming variables/functions

**Critical Rules**:

1. **Exact Matching Required**
   - Whitespace must match exactly
   - Case sensitive
   - Indentation must be identical (tabs vs spaces)
   - Include line breaks if present

2. **Uniqueness Matters**
   - `old_string` must be unique unless using `replace_all`
   - Include enough context to ensure uniqueness
   - If ambiguous, Edit will fail

3. **Read First**
   - Always read the file before editing
   - Use line numbers from Read output
   - Copy exact formatting

**Example**:
```python
# Original file content:
def calculate_total(price, tax_rate):
    return price * (1 + tax_rate)

# Edit parameters:
old_string: "def calculate_total(price, tax_rate):"
new_string: "def calculate_total(price, tax_rate, discount=0):"

# Result:
def calculate_total(price, tax_rate, discount=0):
    return price * (1 + tax_rate)
```

**Common Pitfalls**:
- ❌ Not matching whitespace exactly
- ❌ Forgetting to read file first
- ❌ Including line numbers in old_string
- ❌ Non-unique old_string without replace_all

**Pro Tips**:
- Include context lines for uniqueness
- Use `replace_all=True` for variable renames
- Test with single replacement first
- Verify with Read after Edit

---

### 4. Glob Tool 🔍

**Purpose**: Find files by name pattern (like `find` but better)

**Parameters**:
```
pattern (required) - Glob pattern to match
path (optional)    - Directory to search
```

**Pattern Syntax**:

| Pattern | Matches | Example Files |
|---------|---------|---------------|
| `*.py` | Python files (current dir) | `auth.py`, `utils.py` |
| `**/*.py` | Python files (all subdirs) | `src/auth.py`, `tests/test.py` |
| `test_*.py` | Test files starting with test_ | `test_auth.py`, `test_utils.py` |
| `*.{js,ts}` | JavaScript OR TypeScript | `app.js`, `app.ts` |
| `src/**/*.test.js` | Test files in src tree | `src/components/Button.test.js` |
| `**/config.*` | Config files anywhere | `config.json`, `api/config.yaml` |

**Usage Examples**:
```
"Find all Python files"
"Show me all test files"
"Find configuration files"
"Locate all React components in src/"
"Find all JSON files"
```

**When to Use**:
- ✅ Discovering project structure
- ✅ Finding files by name or extension
- ✅ Locating test files
- ✅ Finding configuration files
- ✅ File discovery and exploration

**Glob vs Grep**:
```
Glob - Find files by NAME
  "Find all *.py files" → Glob

Grep - Search file CONTENTS
  "Find files containing 'login'" → Grep
```

**Pro Tips**:
- Use `**` for recursive search in subdirectories
- Combine patterns with `{ext1,ext2,ext3}`
- Results sorted by modification time (newest first)
- Fast pattern matching, works on any codebase size

---

### 5. Grep Tool 🔎

**Purpose**: Search file contents for code patterns

**Parameters**:
```
pattern (required)       - Regex pattern to search
path (optional)          - File/directory to search
glob (optional)          - Filter files (e.g., "*.py")
output_mode (optional)   - content | files_with_matches | count
-i (optional)            - Case insensitive search
-A, -B, -C (optional)    - Context lines (after, before, around)
```

**Pattern Examples (Regex)**:

| Pattern | Matches | Use Case |
|---------|---------|----------|
| `login` | Literal "login" | Find login references |
| `def \w+` | Function definitions | Find all Python functions |
| `@app\.route` | Flask route decorators | Find API endpoints |
| `TODO\|FIXME` | TODO or FIXME comments | Find action items |
| `import.*numpy` | Numpy import statements | Find dependencies |
| `class \w+\(` | Class definitions | Find all classes |

**Usage Examples**:
```
"Search for 'login' function usage"
"Find all TODO comments in the project"
"Where is the authenticate decorator used?"
"Find all API endpoints in Python files"
"Search for function definitions"
"Find all imports of React"
```

**Output Modes**:

1. **content** (default) - Shows matching lines with context
   ```
   src/auth.py:45:    def login(username, password):
   src/api.py:12:     result = login(user, pass)
   ```

2. **files_with_matches** - Lists files only
   ```
   src/auth.py
   src/api.py
   tests/test_auth.py
   ```

3. **count** - Shows match counts per file
   ```
   src/auth.py: 3 matches
   src/api.py: 1 match
   ```

**When to Use**:
- ✅ Finding function calls/usages
- ✅ Locating API endpoints
- ✅ Searching for code patterns
- ✅ Finding TODOs/FIXMEs/NOTEs
- ✅ Dependency analysis
- ✅ Understanding code structure

**Pro Tips**:
- Use regex for powerful pattern matching
- Filter by file type with `glob: "*.py"`
- Use `-i` for case-insensitive searches
- Use `-C 3` to see 3 lines of context around matches
- Combine with Glob to narrow search scope

---

### 6. Bash Tool 💻

**Purpose**: Execute terminal/shell commands

**Parameters**:
```
command (required)         - Shell command to execute
timeout (optional)         - Max time (default: 2min, max: 10min)
run_in_background (optional) - Run asynchronously
description (recommended)  - What this command does
```

**Usage Examples**:
```
"Run npm install"
"Execute pytest"
"Show git status"
"Build the project with npm run build"
"Install dependencies from requirements.txt"
"Run the test suite"
```

**When to Use**:
- ✅ Git operations (`git status`, `commit`, `push`)
- ✅ Package management (`npm install`, `pip install`)
- ✅ Running tests (`pytest`, `npm test`, `jest`)
- ✅ Build commands (`npm run build`, `make`)
- ✅ Other terminal operations

**When NOT to Use**:
- ❌ Reading files → use **Read** tool
- ❌ Creating files → use **Write** tool
- ❌ Editing files → use **Edit** tool
- ❌ Finding files → use **Glob** tool
- ❌ Searching code → use **Grep** tool

### The Golden Rule

**Always prefer specialized tools over Bash for file operations!**

Why? Specialized tools are:
- More reliable
- Better error handling
- Platform independent
- Designed for Claude Code
- Easier to use

**Best Practices**:

1. **Quote paths with spaces**:
   ```bash
   cd "My Documents"          # ✅ Correct
   cd My Documents            # ❌ Wrong - will fail
   python "path with spaces/script.py"  # ✅ Correct
   ```

2. **Chain commands with &&**:
   ```bash
   npm install && npm test    # ✅ Second runs only if first succeeds
   npm install; npm test      # ❌ Second runs even if first fails
   ```

3. **Prefer absolute paths over cd**:
   ```bash
   pytest /project/tests               # ✅ Better
   cd /project && pytest tests         # ❌ Avoid changing directory
   ```

4. **Use timeouts for long operations**:
   ```bash
   npm run build  # May need timeout: 300000 (5 minutes)
   ```

**Common Bash Commands**:
```bash
# Git
git status
git diff
git add .
git commit -m "message"
git push origin main

# npm
npm install
npm test
npm run build
npm run dev

# Python
pip install -r requirements.txt
pytest
python -m pytest tests/

# Build
make
make test
```

---

## Tool Selection Guide

### Quick Decision Matrix

| Your Goal | Tool | Example Command |
|-----------|------|-----------------|
| **View file contents** | Read | "Read src/auth.py" |
| **Create new file** | Write | "Create utils/logger.py" |
| **Modify existing file** | Edit | "Fix bug in config.json" |
| **Find files by name** | Glob | "Find all *.test.js files" |
| **Search code contents** | Grep | "Search for 'login' function" |
| **Run terminal command** | Bash | "Run pytest" |
| **Git operations** | Bash | "Show git status" |
| **Install packages** | Bash | "npm install" |

### Decision Tree

```
What do you need to do?
│
├─ File Operation
│  ├─ View file contents? → Read
│  ├─ Create brand new file? → Write
│  └─ Modify existing file? → Edit
│
├─ Search / Find
│  ├─ Find files by name? → Glob
│  └─ Search file contents? → Grep
│
└─ Terminal Command
   ├─ Git operation? → Bash
   ├─ Package management? → Bash
   ├─ Run tests? → Bash
   └─ Build project? → Bash
```

### Edit vs Write Decision

```
Need to change a file?
├─ File doesn't exist yet? → Write
├─ Need complete rewrite (90%+ changes)? → Write
├─ Small targeted change? → Edit
├─ Add function to existing file? → Edit
├─ Fix a bug? → Edit
└─ Update configuration? → Edit
```

**Rule of thumb**: Write for creation, Edit for modification

---

## Common Patterns

### Pattern 1: Exploring New Codebase

```
Step 1: Get high-level overview
  → "Show me the project structure"
  Uses: Glob to find key files, Read README

Step 2: Understand purpose and architecture
  → "What does this project do?"
  Uses: Read package.json, README, main files

Step 3: Find specific features
  → "How does authentication work?"
  Uses: Grep to find auth code, Read auth files

Step 4: Deep dive on implementation
  → "Explain the login function in detail"
  Uses: Read specific files, analyze code
```

**Tool Flow**: `Glob → Read → Grep → Read`

---

### Pattern 2: Making Code Changes

```
Step 1: Understand current implementation
  → "Read src/auth.py"
  Uses: Read tool

Step 2: Make targeted changes
  → "Fix the security bug on line 45"
  Uses: Edit tool (precise change)

Step 3: Verify changes
  → "Read src/auth.py again to verify"
  Uses: Read tool

Step 4: Test the changes
  → "Run the authentication tests"
  Uses: Bash tool (pytest)
```

**Tool Flow**: `Read → Edit → Read → Bash`

---

### Pattern 3: Creating New Features

```
Step 1: Find similar existing code
  → "Find other utility modules"
  Uses: Glob tool

Step 2: Understand the pattern
  → "Read src/utils/logger.py"
  Uses: Read tool

Step 3: Create new module following pattern
  → "Create src/utils/validator.py with email validation"
  Uses: Write tool

Step 4: Add tests
  → "Create tests/test_validator.py"
  Uses: Write tool

Step 5: Run tests
  → "Run pytest on the new module"
  Uses: Bash tool
```

**Tool Flow**: `Glob → Read → Write → Write → Bash`

---

### Pattern 4: Refactoring Code

```
Step 1: Find all usages
  → "Find where calculate_total is called"
  Uses: Grep tool

Step 2: Read affected files
  → "Read src/billing.py and src/cart.py"
  Uses: Read tool

Step 3: Update function signature
  → "Update calculate_total to accept discount parameter"
  Uses: Edit tool (with replace_all for function name)

Step 4: Update all call sites
  → "Update all calls to include discount parameter"
  Uses: Edit tool (multiple times or replace_all)

Step 5: Run tests to verify
  → "Run all tests"
  Uses: Bash tool
```

**Tool Flow**: `Grep → Read → Edit → Edit → Bash`

---

### Pattern 5: Bug Investigation

```
Step 1: Reproduce the issue
  → "Run the failing test"
  Uses: Bash tool

Step 2: Find related code
  → "Search for error message in codebase"
  Uses: Grep tool

Step 3: Analyze the code
  → "Read the file where error occurs"
  Uses: Read tool

Step 4: Fix the bug
  → "Fix the null pointer error on line 67"
  Uses: Edit tool

Step 5: Verify fix
  → "Run the test again"
  Uses: Bash tool
```

**Tool Flow**: `Bash → Grep → Read → Edit → Bash`

---

## Git Workflows

### Basic Git Workflow

```
1. Check current status
   → "Show me git status"
   Command: git status

2. View what changed
   → "What changed in src/auth.py?"
   Command: git diff src/auth.py

3. Stage changes
   → "Stage all changes in src/ directory"
   Command: git add src/

4. Commit with message
   → "Commit with message: Add authentication module"
   Command: git commit -m "Add authentication module"

5. Push to remote
   → "Push to origin main"
   Command: git push origin main
```

### Creating Pull Requests

```
1. Check current branch
   → "What branch am I on?"
   Command: git branch

2. Create feature branch (if needed)
   → "Create and switch to feature/auth branch"
   Command: git checkout -b feature/auth

3. Make your changes
   [Use Read, Edit, Write tools]

4. Review changes
   → "Show me all changes"
   Command: git diff

5. Commit changes
   → "Stage and commit all changes"
   Commands: git add . && git commit -m "message"

6. Push feature branch
   → "Push feature branch to remote"
   Command: git push -u origin feature/auth

7. Create PR (if gh CLI available)
   → "Create a pull request"
   Command: gh pr create --title "..." --body "..."
```

### Commit Message Format

**Recommended Format**:
```
[Component] Action: Description

Examples:
[Auth] Add: JWT token authentication
[API] Fix: Rate limiting bug in login endpoint
[Tests] Update: Add integration tests for auth module
[Docs] Improve: README installation instructions
[Refactor] Simplify: User authentication logic
```

### Git Best Practices

✅ **Do**:
- Check `git status` before committing
- Review `git diff` to verify changes
- Write descriptive commit messages
- Commit logical chunks (not everything at once)
- Push to feature branches (not directly to main)
- Use Claude Code for entire git workflow

❌ **Don't**:
- Commit without reviewing changes
- Use vague messages like "fix stuff" or "updates"
- Push directly to main in team projects
- Force push (`--force`) without understanding why
- Skip viewing the diff before commit
- Commit secrets or sensitive data

---

## Skills

### Understanding Skills

**Skills vs Commands**:
```
Skills:
- AI-invoked based on context
- Automatic activation
- Provide domain expertise
- Located in .claude/skills/

Commands:
- User-invoked explicitly
- Manual activation with /command
- Reusable prompts
- Located in .claude/commands/
```

### Skill Structure

**SKILL.md Format**:
```markdown
# SKILL.md

description: Brief description for AI to know when to activate this skill

## Instructions
Detailed instructions for Claude on how to use this skill

## Examples
Usage examples to demonstrate the skill

## Reference
Additional context, links, documentation
```

### Skill Activation

**Automatic (based on context)**:
```
User: "Analyze this technical analysis chart"
→ Automatically activates: technical-analysis-educator skill

User: "Review this notebook for educational quality"
→ Automatically activates: notebook-tester skill
```

**Explicit Invocation**:
```
"Use the data-science-educator skill to explain pandas groupby"
"Apply the code-reviewer skill to this module"
```

### Skill Scopes

**Project Skills**: `.claude/skills/`
- Specific to current project
- Shared with team via git
- Project-specific patterns and standards

**Personal Skills**: `~/.claude/skills/`
- Available across all projects
- Your personal preferences and workflows
- Not shared with team

---

## Custom Slash Commands

### Creating Commands

**Basic Command**:
```markdown
# .claude/commands/review.md
Review this code for:
- Code quality and style
- Best practices
- Potential bugs
- Security issues
- Performance considerations
```

**Usage**: `/review`

**Parameterized Command**:
```markdown
# .claude/commands/test.md
Create comprehensive tests for $ARGUMENTS including:
- Unit tests for all functions
- Edge cases and boundary conditions
- Error handling scenarios
- Integration tests if applicable
```

**Usage**: `/test UserService.ts`

### Namespacing Commands

**Directory Structure**:
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

### Command Best Practices

✅ **Good Commands**:
- Specific and focused
- Include $ARGUMENTS for flexibility
- Clear instructions
- Reusable across projects

❌ **Bad Commands**:
- Too vague or generic
- No parameterization when needed
- Overly complex (use skills instead)
- Project-specific hardcoded values

---

## Hooks

### Hook Types

**Available Events**:
- `tool_call` - Before/after tool execution
- `user_prompt_submit` - When user submits message
- `assistant_message` - When assistant responds

### Hook Configuration

**Enable in settings.json**:
```json
{
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": [
        "bash .claude/hooks/validate.sh",
        "bash .claude/hooks/security-check.sh"
      ]
    }
  }
}
```

### Hook Script Example

**Validation Hook** (`.claude/hooks/validate.sh`):
```bash
#!/bin/bash
# Hook runs before tool execution
# Exit 0 to allow, non-zero to block

# Block writes to production config
if [[ "$TOOL_NAME" == "Write" && "$TOOL_ARGS" == *"production.json"* ]]; then
  echo "❌ Blocked: Cannot write to production.json"
  exit 1
fi

# Log all bash commands
if [[ "$TOOL_NAME" == "Bash" ]]; then
  echo "ℹ️  Bash command: $TOOL_ARGS" >> .claude/logs/bash-commands.log
fi

# Allow the operation
exit 0
```

### Hook Use Cases

**Quality Gates**:
```bash
# Run linter before commits
if [[ "$TOOL_NAME" == "Bash" && "$TOOL_ARGS" == *"git commit"* ]]; then
  npm run lint || exit 1
fi
```

**Security Checks**:
```bash
# Prevent committing secrets
if grep -r "API_KEY\|SECRET\|PASSWORD" staged_files; then
  echo "❌ Potential secrets detected!"
  exit 1
fi
```

**Auto-formatting**:
```bash
# Format code before committing
if [[ "$TOOL_NAME" == "Bash" && "$TOOL_ARGS" == *"git commit"* ]]; then
  npm run format
fi
```

---

## MCP Servers

### Installing MCP Servers

**Via NPM**:
```bash
npm install -g @modelcontextprotocol/server-github
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-postgres
```

### MCP Configuration

**In settings.json or settings.local.json**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    }
  }
}
```

### Common MCP Servers

| Server | Purpose | Package |
|--------|---------|---------|
| **filesystem** | File system access beyond project | `@modelcontextprotocol/server-filesystem` |
| **github** | GitHub API integration | `@modelcontextprotocol/server-github` |
| **postgres** | PostgreSQL database access | `@modelcontextprotocol/server-postgres` |
| **puppeteer** | Browser automation | `@modelcontextprotocol/server-puppeteer` |
| **slack** | Slack integration | `@modelcontextprotocol/server-slack` |

### Using MCP Servers

**Once configured, use naturally**:
```
"Fetch issues from GitHub repository owner/repo"
→ Uses GitHub MCP server

"Query the users table in the database"
→ Uses Postgres MCP server

"Take a screenshot of example.com"
→ Uses Puppeteer MCP server
```

---

## Subagents

### Using the Task Tool

**Basic Delegation**:
```
"Use the Task tool to delegate code review to specialized agent"
"Create a subagent to handle testing"
```

**Parallel Execution**:
```
"Run code-reviewer and test-runner agents in parallel"
"Launch multiple agents for comprehensive analysis"
```

### Creating Custom Subagents

**Agent Definition** (`.claude/agents/my-agent.md`):
```markdown
# my-agent

description: Specialized agent for [specific task]

## Tools Available
- Read
- Grep
- Bash (read-only)

## Instructions
[Detailed task instructions for this agent]
Focus on [specific domain/task]

## Output Format
Return structured results:
- Summary
- Findings
- Recommendations
```

### Subagent Use Cases

**Code Review Agent**:
```markdown
description: Reviews code for quality, security, and best practices

Analyzes code and reports:
- Code quality issues
- Security vulnerabilities
- Performance concerns
- Best practice violations
```

**Test Generator Agent**:
```markdown
description: Generates comprehensive test suites

Creates tests including:
- Unit tests for all functions
- Edge cases and boundaries
- Error handling scenarios
- Integration tests
```

---

## Configuration

### Main Settings: `.claude/settings.json`

```json
{
  "output_style": "concise",
  "experimental": {
    "extended_thinking": true
  },
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": []
    }
  },
  "mcpServers": {}
}
```

### Configuration Options

**output_style**:
- `"concise"` - Brief, to-the-point responses
- `"balanced"` - Moderate detail (default)
- `"verbose"` - Detailed explanations

**experimental.extended_thinking**:
- `true` - More thorough reasoning (recommended)
- `false` - Faster responses

**hooks**:
- Configure event-driven automation
- Enable/disable per event type

### Local Settings: `.claude/settings.local.json`

```json
{
  "output_style": "verbose",
  "mcpServers": {
    "my-local-server": {
      "command": "node",
      "args": ["server.js"],
      "env": {
        "API_KEY": "your-secret-key-here"
      }
    }
  }
}
```

**Critical**: Always gitignore!
```gitignore
.claude/settings.local.json
.claude/cache/
```

---

## Troubleshooting

### Installation Issues

**Problem**: `command not found: claude`

**Solutions**:
```bash
# Check if installed
which claude
npm list -g @anthropic-ai/claude-code

# Verify Node.js version (needs 18+)
node --version

# Reinstall
npm install -g @anthropic-ai/claude-code

# Check PATH
echo $PATH | grep npm
```

---

### File Operation Errors

**Problem**: "File not found"

**Solutions**:
```bash
# Use absolute paths
/full/path/to/file

# Check current directory
pwd

# Verify file exists
ls -la path/to/file

# Check permissions
ls -l file
```

---

### Edit Tool Failures

**Problem**: "String not found in file"

**Solutions**:
1. Read the file first: `"Read src/file.py"`
2. Copy exact text including whitespace
3. Check tabs vs spaces in indentation
4. Include more context for uniqueness
5. Verify case sensitivity

**Example**:
```python
# ❌ Wrong - doesn't match whitespace
old_string: "def login():"

# ✅ Correct - matches exactly
old_string: "    def login():"  # Includes indentation
```

---

### Performance Issues

**Problem**: Slow responses

**Solutions**:
```json
// Use concise output
{
  "output_style": "concise"
}
```

```bash
# Clear cache
rm -rf .claude/cache/

# Use /clear to reset tokens
/clear

# Break into smaller tasks
```

---

### Token Limit Warnings

**Problem**: "Approaching token limit"

**Solutions**:
1. Use `/clear` to reset conversation
2. Break tasks into smaller chunks
3. Use `"concise"` output style
4. Avoid reading very large files
5. Use offset/limit when reading

---

### Git Operation Failures

**Problem**: Git commands failing

**Solutions**:
```bash
# Check git status
git status

# Verify git config
git config --list

# Check remote
git remote -v

# Review error message carefully
```

---

## Quick Reference Card

### Most Used Commands
```
View file         → "Read src/file.py"
Edit file         → "Edit src/file.py to fix bug"
Create file       → "Create src/new.py"
Find files        → "Find all *.test.js"
Search code       → "Search for 'function'"
Run tests         → "Run pytest"
Git status        → "Show git status"
Commit            → "Commit with message '...'"
Undo              → /rewind
Start fresh       → /clear
Get help          → /help
```

### Emergency Commands
```
Undo last action  → /rewind or ESC ESC
Stop execution    → Ctrl+C
Exit Claude Code  → Ctrl+D or 'exit'
Report bug        → /bug
Check version     → /version
```

### Best Practices Checklist

✅ **Always Do**:
- Read files before editing
- Use specialized tools (not Bash for files)
- Review git diff before committing
- Provide specific, clear requests
- Test changes before committing
- Use `/clear` between unrelated tasks

❌ **Never Do**:
- Edit without reading first
- Commit without reviewing changes
- Use absolute paths (use relative)
- Store secrets in commands/skills
- Ignore error messages
- Skip testing

---

**Version 2.0 Updates** (2025-11-20):
- Expanded all tool documentation
- Added comprehensive examples
- Included decision trees and matrices
- Added common workflow patterns
- Enhanced troubleshooting section
- Added configuration details
- Included hooks and MCP documentation
- Added subagent information

---

**Pro Tip**: Bookmark this reference! The more you use Claude Code naturally, the more these patterns will become second nature. Start with the basics (Read, Edit, Write) and gradually incorporate advanced features (Skills, Hooks, MCP).

