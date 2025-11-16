# Claude Code Quick Reference Guide

A comprehensive quick reference for all Claude Code features.

## Table of Contents
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Essential Commands](#essential-commands)
- [Sub-agents](#sub-agents)
- [Hooks](#hooks)
- [Skills](#skills)
- [Slash Commands](#slash-commands)
- [MCP](#mcp)
- [Tools](#tools)
- [Git Workflows](#git-workflows)

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Tab` (2x) | Enter Plan Mode (read-only) |
| `Escape` | Stop Claude (don't use Ctrl+C!) |
| `Escape` (2x) | View message history / Rewind |
| `Ctrl+V` | Paste images from clipboard |
| `Shift+Drag` | Reference files in prompt |

---

## Essential Commands

### Conversation Management
```bash
/clear          # Clear conversation history
/compact        # Condense history (~70% token reduction)
/rewind         # Roll back conversation and code
/export         # Export conversation
```

### Configuration
```bash
/config         # View/edit settings
/model          # Change AI model
/status         # Check session status
/privacy        # Privacy settings
```

### Development
```bash
/review         # Code review
/bug            # Bug analysis
/sandbox        # Safe testing environment
```

### Context & Usage
```bash
/context        # View token usage
/cost           # Check API costs
/usage          # Usage statistics
```

### Integration
```bash
/mcp            # MCP server management
/hooks          # View/configure hooks
/agents         # Manage sub-agents
/skills         # List available skills
```

---

## Sub-agents

### Creating a Sub-agent

**File Location:**
- Project: `.claude/agents/agent-name.md`
- User: `~/.claude/agents/agent-name.md`

**Template:**
```markdown
---
name: agent-name
description: Detailed description including when to invoke
allowed-tools: [Read, Write, Edit, Grep, Glob]
model: sonnet
---

Your custom instructions for the agent...
```

### Tool Permissions

**Read-Only (Reviewers, Auditors):**
```yaml
allowed-tools: [Read, Grep, Glob, LS]
```

**Write Access (Implementers):**
```yaml
allowed-tools: [Read, Write, Edit, Grep, Glob]
```

**Execution Access (Test Runners):**
```yaml
allowed-tools: [Read, Write, Edit, "Bash(pytest:*)", "Bash(npm test:*)"]
```

**Full Access (Use Sparingly):**
```yaml
allowed-tools: ["*"]
```

### Model Selection

| Model | Best For |
|-------|----------|
| `opus` | Complex reasoning, critical decisions |
| `sonnet` | Most tasks, balanced performance |
| `haiku` | Quick searches, simple tasks |
| `inherit` | Use parent session's model |

---

## Hooks

### Hook Types

| Hook Event | When It Triggers |
|------------|------------------|
| `PreToolUse` | Before tool execution |
| `PostToolUse` | After successful tool completion |
| `UserPromptSubmit` | When user submits prompt |
| `SessionStart` | Session initialization |
| `SessionEnd` | Session cleanup |
| `Stop` | Main agent finishes |
| `SubagentStop` | Subagent finishes |
| `PreCompact` | Before context compaction |

### Configuration Location

**Hierarchy (highest to lowest):**
1. Local: `.claude/settings.local.json` (not in git)
2. Project: `.claude/settings.json` (in git)
3. User: `~/.claude/settings.json`

### Hook Examples

**Auto-format Python on Write:**
```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": "Write(*.py:*)",
      "type": "bash",
      "command": "black $FILE_PATH"
    }
  ]
}
```

**Run tests after Edit:**
```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": "Edit(*test*.py:*)",
      "type": "bash",
      "command": "pytest $FILE_PATH -v"
    }
  ]
}
```

**Block sensitive file access:**
```json
{
  "hooks": [
    {
      "event": "PreToolUse",
      "matcher": "Read(.env:*)",
      "type": "bash",
      "command": "exit 2"
    }
  ]
}
```

### Exit Codes
- **0**: Success (stdout shown in transcript)
- **2**: Blocking error (stderr fed to Claude)
- **Other**: Non-blocking error (stderr shown to user)

---

## Skills

### Creating a Skill

**File Location:**
- Personal: `~/.claude/skills/skill-name/SKILL.md`
- Project: `.claude/skills/skill-name/SKILL.md`

**SKILL.md Template:**
```markdown
---
name: my-skill-name
description: What it does and when to use (include trigger keywords!)
allowed-tools: [Read, Write, Bash]
---

Your skill instructions...

## Additional Files
Skills can include supporting files:
- reference.md
- scripts/
- templates/
```

### Skill vs Slash Command

| Feature | Skills | Slash Commands |
|---------|--------|----------------|
| Invocation | Model-invoked (automatic) | User-invoked (explicit) |
| Complexity | Multi-file, complex | Single-file, simple |
| Structure | Directory with SKILL.md + files | Single .md file |
| Use Case | Reusable capabilities | Quick prompts |

---

## Slash Commands

### Creating Custom Commands

**File Location:**
- Project: `.claude/commands/command-name.md`
- Personal: `~/.claude/commands/command-name.md`

**Basic Command:**
```markdown
Analyze this code for performance issues and suggest optimizations.
```

**With Frontmatter:**
```markdown
---
description: Review code for security issues
allowed-tools: [Bash(git status:*), Bash(git diff:*)]
argument-hint: [file-path] [severity-level]
model: sonnet
---

Identify security vulnerabilities in $ARGUMENTS
```

### Advanced Features

**Arguments:**
```markdown
Fix issue #$ARGUMENTS
Review PR #$1 with priority $2
```

**Bash Execution (! prefix):**
```markdown
---
allowed-tools: [Bash(git status:*), Bash(git diff:*)]
---

Current status: !`git status`
Current diff: !`git diff HEAD`

Create a commit based on these changes.
```

**File References (@ prefix):**
```markdown
Review the implementation in @src/utils/helpers.js
```

---

## MCP (Model Context Protocol)

### What is MCP?
Connects Claude Code to external tools and data sources.

### Installation

**Check available servers:**
```bash
/mcp
```

**Install a server:**
```bash
claude mcp install @modelcontextprotocol/server-linear
```

### Popular MCP Servers

**Project Management:**
- Linear, Asana, Monday, Jira, Notion

**Development:**
- GitHub, GitLab, Vercel, Netlify

**Data:**
- PostgreSQL, MongoDB, Airtable

**Design:**
- Figma, Canva

**Monitoring:**
- Sentry, Datadog

### Configuration Scopes

| Scope | Location | Use Case |
|-------|----------|----------|
| Local | Default | Personal, project-specific |
| Project | `.mcp.json` | Shared team settings |
| User | Global config | Cross-project access |

---

## Tools

### File Operations

**Read** - Read files (supports images, PDFs, notebooks)
```
"Read the configuration file at config/app.json"
```

**Write** - Create or overwrite files
```
"Create a new file utils/helper.py with [code]"
```

**Edit** - Targeted string replacement
```
"Change the timeout value from 30 to 60 in server.js"
```

### Search & Navigation

**Glob** - File pattern matching
```
"Find all TypeScript files: **/*.ts"
"List Python test files: tests/**/*_test.py"
```

**Grep** - Content searching
```
"Search for 'TODO' comments in all files"
"Find all database queries containing 'SELECT'"
```

### Execution

**Bash** - Execute shell commands
```
"Run the test suite"
"Check git status"
"Install dependencies"
```

### Best Practices

✅ **Use specialized tools:**
- File search → Glob (not `find`)
- Content search → Grep (not `grep`/`rg`)
- Read files → Read (not `cat`)
- Edit files → Edit (not `sed`)

✅ **Parallel execution:**
```
Make independent tool calls in one message
```

✅ **Sequential execution:**
```
Use && for dependent commands
```

---

## Git Workflows

### Creating Commits

**Process:**
1. Claude reviews `git status` and `git diff`
2. Analyzes changes
3. Drafts commit message following your style
4. Creates commit with standard format

**Commit Message Format:**
```
Brief description of changes

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Request Examples:**
```
"Create a commit for these authentication changes"
"Commit the refactoring work with a descriptive message"
```

### Creating Pull Requests

**Process:**
1. Reviews all commits in branch
2. Analyzes full diff from divergence
3. Generates comprehensive PR description
4. Creates PR using `gh pr create`

**PR Format:**
```markdown
## Summary
- Bullet point summaries

## Test plan
- [ ] Testing checklist

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

**Request Examples:**
```
"Create a PR for this feature branch"
"Open a pull request with the authentication changes"
```

### Git Safety Protocol

**NEVER:**
- Force push to main/master
- Skip hooks without permission
- Amend other developers' commits
- Update git config

**ALWAYS:**
- Work on branches
- Review changes before committing
- Get explicit permission for commits
- Check authorship before amending

### Git Worktrees

**Enable parallel work:**
```bash
git worktree add ../project-feature-a -b feature-a
claude  # In worktree 1
claude  # In worktree 2 (separate instance)
```

**Benefits:**
- Independent file states
- No interference between sessions
- Shared git history

---

## Project Setup

### CLAUDE.md Files

**Purpose:** Automatically loaded context at session start

**Best Practices:**
- Document repository structure
- Explain setup procedures
- Define coding standards
- List architecture decisions
- Include common workflows

**Multiple CLAUDE.md:**
- Root: General project info
- Subdirectories: Specific context (frontend/, backend/)

### Settings Hierarchy

**Priority (highest to lowest):**
1. `.claude/settings.local.json` (not in git)
2. `.claude/settings.json` (in git, shared)
3. `~/.claude/settings.json` (user global)

**Example settings.json:**
```json
{
  "allowed-tools": [
    "Read",
    "Write",
    "Edit",
    "Bash(git:*)",
    "Bash(npm:*)",
    "Bash(pytest:*)"
  ],
  "hooks": [],
  "model": "sonnet"
}
```

### Directory Structure

```
.claude/
├── settings.json           # Shared project settings
├── settings.local.json     # Local overrides (gitignored)
├── agents/                 # Project-specific sub-agents
│   ├── code-reviewer.md
│   └── test-generator.md
├── commands/               # Custom slash commands
│   ├── deploy.md
│   └── review.md
└── skills/                 # Project skills
    └── my-skill/
        └── SKILL.md
```

---

## Common Workflows

### Workflow: Explore New Codebase
```
1. [Shift+Tab 2x] - Plan Mode
2. "What's the project structure?"
3. "How is authentication implemented?"
4. "Where are the tests?"
5. "What's the build process?"
```

### Workflow: Debug Issue
```
1. "I'm getting this error: [paste]"
2. Claude analyzes code
3. "Here's the fix: [suggestion]"
4. Review and approve
5. "Create a commit"
```

### Workflow: Add Feature
```
1. "Create branch feature/new-auth"
2. [Plan Mode] "Plan implementation for [feature]"
3. [Execute Mode] "Implement the plan"
4. "Run tests"
5. "Create commit and PR"
```

### Workflow: Code Review
```
1. "What changed since last commit?"
2. "/review"
3. Address issues
4. "Create commit"
```

---

## Troubleshooting

### Running Out of Tokens
```bash
/context        # Check usage
/compact        # Condense history (~70% reduction)
/clear          # Nuclear option (fresh start)
```

### Claude Doesn't Understand Project
```
1. Create CLAUDE.md in root
2. Use Plan Mode to explore
3. Be specific about file locations
```

### Unwanted Changes
```bash
/rewind         # Roll back conversation
git reset       # Reset file changes
```

### Slow Responses
```bash
/model haiku    # Faster model
# Or be more specific in requests
```

---

## Tips & Best Practices

### General
1. ✅ Start with Plan Mode for exploration
2. ✅ Be specific in requests
3. ✅ Work on git branches
4. ✅ Review before committing
5. ✅ Clear context between tasks
6. ✅ Ask for explanations

### Token Management
1. ✅ Use `/clear` when switching tasks
2. ✅ Use `/compact` when low on tokens
3. ✅ Monitor with `/context`

### Safety
1. ✅ Always review Claude's changes
2. ✅ Test before committing
3. ✅ Use branches for safety
4. ✅ Don't commit secrets

### Efficiency
1. ✅ Pre-approve safe tools
2. ✅ Create custom commands for repeated tasks
3. ✅ Use sub-agents for specialized work
4. ✅ Set up hooks for automation

---

## Cheat Sheet

### Most Used Commands
```bash
/clear          # Start fresh
/compact        # Free tokens
/context        # Check usage
/review         # Code review
/model          # Change model
```

### Most Used Shortcuts
```
Shift+Tab 2x    # Plan Mode
Escape          # Stop
Escape 2x       # Rewind
```

### Common Requests
```
"Explain how [feature] works"
"Fix the bug in [file]"
"Add [feature] to [component]"
"Create tests for [module]"
"Review my changes"
"Create a commit"
"Create a PR"
```

---

**For detailed guides, see the full notebooks (01-10) in the notebooks/ directory!**
