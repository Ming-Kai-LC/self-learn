# Claude Code Command Reference

**Quick reference guide for Claude Code commands, tools, and patterns**

## Built-in Slash Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/help` | Display available commands and help | `/help` |
| `/clear` | Clear conversation history | `/clear` |
| `/rewind` | Undo to previous conversation state | `/rewind` or double ESC |
| `/bug` | Report a bug in Claude Code | `/bug` |

## Core Tools

### File Operations

**Read** - Read file contents
```
"Read the file src/app.ts"
"Show me the contents of README.md"
```

**Write** - Create new files
```
"Write a new file src/utils.ts with helper functions"
"Create a new component Button.tsx"
```

**Edit** - Modify existing files
```
"Edit src/app.ts to add error handling"
"Change the function name to calculateTotal"
```

### Search and Navigation

**Glob** - Find files by pattern
```
"Find all TypeScript files in src/"
"Show me all test files"
Pattern examples: *.ts, **/*.test.js, src/**/*.tsx
```

**Grep** - Search file contents
```
"Search for 'import React' across the project"
"Find all TODO comments"
```

### Terminal Operations

**Bash** - Execute shell commands
```
"Run npm test"
"Show git status"
"Install dependencies with npm install"
```

### Git Workflows

**Git Operations** - Automated git workflows
```
"Commit these changes with message 'Add feature X'"
"Create a pull request for this feature"
"Show me the git diff"
"Push changes to remote"
```

## Custom Slash Commands

### Creating Commands

**Location:**
- Project: `.claude/commands/`
- Personal: `~/.claude/commands/`

**Basic Command:**
```markdown
# .claude/commands/review.md
Review this code for:
- Code quality
- Best practices
- Potential bugs
- Security issues
```

**Parameterized Command:**
```markdown
# .claude/commands/test.md
Create comprehensive tests for $ARGUMENTS including:
- Unit tests
- Edge cases
- Error handling
```

**Usage:**
```
/review
/test UserService.ts
```

### Namespacing

**Structure:**
```
.claude/commands/
├── review/
│   ├── code.md
│   ├── security.md
│   └── performance.md
└── generate/
    ├── tests.md
    └── docs.md
```

**Usage:**
```
/review/code
/review/security
/generate/tests
```

## Skills

### Understanding Skills

**Skills vs Commands:**
- **Skills**: AI-invoked based on context
- **Commands**: User-invoked explicitly

**Skill Structure:**
```markdown
# SKILL.md

description: Brief description for skill activation

## Instructions
Detailed instructions for Claude

## Examples
Usage examples

## Reference
Additional context
```

### Invoking Skills

**Automatic Activation:**
```
"Analyze this technical analysis chart"
→ Activates technical-analysis-educator skill

"Review this notebook for quality"
→ Activates notebook-tester skill
```

**Explicit Invocation:**
```
"Use the data-science-educator skill to explain pandas groupby"
```

## Hooks

### Hook Types

**Events:**
- `tool_call` - Before/after tool execution
- `user_prompt_submit` - When user submits message
- `assistant_message` - When assistant responds

### Configuration

**settings.json:**
```json
{
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": [
        "bash .claude/hooks/validate.sh"
      ]
    }
  }
}
```

### Hook Script Example

```bash
#!/bin/bash
# .claude/hooks/validate.sh

# Exit 0 to allow, non-zero to block
if [[ "$TOOL_NAME" == "Bash" ]]; then
  echo "Bash tool called with: $TOOL_ARGS"
fi

exit 0
```

## MCP Servers

### Installing MCP Servers

**Via NPM:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Configuration:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Common MCP Servers

| Server | Purpose | Install |
|--------|---------|---------|
| filesystem | File system access | `@modelcontextprotocol/server-filesystem` |
| github | GitHub API | `@modelcontextprotocol/server-github` |
| postgres | PostgreSQL | `@modelcontextprotocol/server-postgres` |
| puppeteer | Browser automation | `@modelcontextprotocol/server-puppeteer` |

## Subagents

### Using the Task Tool

**Basic Usage:**
```
"Use the Task tool to delegate code review to the code-reviewer agent"
```

**Parallel Execution:**
```
"Run code-reviewer and test-runner agents in parallel"
```

### Creating Subagents

**Location:** `.claude/agents/`

**Structure:**
```markdown
# .claude/agents/my-agent.md

description: What this agent does

## Tools Available
- Read
- Grep

## Instructions
Detailed task instructions

## Output Format
Expected output structure
```

## Common Patterns

### Code Review Workflow

```
1. "Show me the changes since last commit"
2. "Review these changes for quality and security"
3. "Add tests for the new functionality"
4. "Update documentation"
5. "Commit with message 'Add feature X with tests and docs'"
```

### Feature Development

```
1. "Read the existing UserService implementation"
2. "Add a new method to handle password reset"
3. "Create tests for the new method"
4. "Update the README with the new feature"
5. "Run the test suite"
6. "Commit and create a PR"
```

### Bug Fix Workflow

```
1. "Find all files related to authentication"
2. "Search for the login bug in issue #123"
3. "Fix the bug in auth.ts"
4. "Add a regression test"
5. "Verify the fix works"
6. "Commit with message 'Fix: Login bug #123'"
```

### Documentation Generation

```
1. "Analyze the API endpoints in this project"
2. "Generate API documentation in Markdown"
3. "Create usage examples for each endpoint"
4. "Update the README with API section"
```

## Prompt Engineering Tips

### Effective Prompts

**❌ Vague:**
```
"Fix the code"
"Make it better"
"Add tests"
```

**✅ Specific:**
```
"Fix the authentication bug in auth.ts line 45"
"Refactor the UserService to use async/await"
"Add unit tests for the calculateTotal function"
```

### Context Providing

**Good Context:**
```
"I'm working on a React app with TypeScript.
Add a new Button component in src/components/
that accepts onClick, children, and variant props.
Follow the existing pattern in Input.tsx."
```

### Multi-Step Tasks

**Clear Steps:**
```
"I need to add a new feature:
1. Create a new UserProfile component
2. Add it to the routes
3. Create tests
4. Update the navigation menu
Please do these in order."
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| ESC ESC | Trigger /rewind |
| Ctrl+C | Cancel current operation |
| Ctrl+D | Exit Claude Code |

## Configuration Files

### .claude/settings.json

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

### .claude/settings.local.json

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["server.js"],
      "env": {
        "API_KEY": "secret-key-here"
      }
    }
  }
}
```

**Note:** Always gitignore `settings.local.json` for secrets!

## Troubleshooting Commands

### Debugging

```
"Show me the current configuration"
"What tools do you have access to?"
"List all available skills"
"What slash commands are available?"
```

### Performance

```
"How many tokens have we used?"
"/rewind to reduce context"
"/clear to start fresh"
```

### Errors

```
"Explain the last error"
"Show me the full error message"
"What went wrong with the last command?"
```

## Best Practices

### Do's ✅

- Be specific in requests
- Provide context for changes
- Review changes before committing
- Use /rewind when things go wrong
- Test changes before pushing
- Document custom components

### Don'ts ❌

- Don't commit without reviewing
- Don't skip testing
- Don't use absolute paths
- Don't store secrets in commands/skills
- Don't ignore hook warnings
- Don't batch too many unrelated changes

## Quick Reference Card

### Most Used Commands
```
Read file               → "Read src/app.ts"
Edit file              → "Edit src/app.ts to..."
Search code            → "Find all instances of..."
Run tests              → "Run npm test"
Git status             → "Show git status"
Commit                 → "Commit with message '...'"
Create PR              → "Create a pull request"
Undo                   → /rewind or ESC ESC
Clear history          → /clear
Get help               → /help
```

### Emergency Commands
```
Undo last action       → /rewind
Stop execution         → Ctrl+C
Exit Claude Code       → Ctrl+D
Report bug             → /bug
```

---

**Pro Tip:** Save this reference for quick lookups during development. The more you use Claude Code, the more natural these patterns will become!
