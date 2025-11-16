# Claude Code Examples

This directory contains practical examples of Claude Code configurations.

## Directory Structure

```
examples/
├── subagents/      # Sub-agent configurations
├── hooks/          # Hook examples
├── skills/         # Skill packages
├── commands/       # Custom slash commands
└── README.md       # This file
```

## Sub-agents

Located in `subagents/`

### code-reviewer.md
Expert code reviewer for security and best practices.

**Usage:**
```
"Review this code for security issues"
"Can you audit the authentication module?"
```

**Tools:** Read-only (Read, Grep, Glob)
**Model:** Sonnet

### test-generator.md
Generates comprehensive unit and integration tests.

**Usage:**
```
"Generate tests for the User class"
"Create test coverage for api/routes.py"
```

**Tools:** Read, Write, Edit, Bash (pytest/npm test)
**Model:** Sonnet

### How to Use
1. Copy to your project: `.claude/agents/`
2. Or install globally: `~/.claude/agents/`
3. Claude will automatically invoke based on your requests

## Hooks

Located in `hooks/`

### settings-example.json
Complete hooks configuration showing:
- Auto-formatting (Black for Python, Prettier for JS)
- Test running after edits
- Linting on file write
- Blocking sensitive file access
- Session welcome messages

### How to Use
1. Copy relevant hooks to `.claude/settings.json`
2. Customize matchers and commands for your project
3. Test hooks before deploying to team

### Common Hook Patterns

**Auto-format on write:**
```json
{
  "event": "PostToolUse",
  "matcher": "Write(*.py:*)",
  "type": "bash",
  "command": "black \"$FILE_PATH\""
}
```

**Run tests after edit:**
```json
{
  "event": "PostToolUse",
  "matcher": "Edit(*test*.py:*)",
  "type": "bash",
  "command": "pytest \"$FILE_PATH\" -v"
}
```

**Block sensitive files:**
```json
{
  "event": "PreToolUse",
  "matcher": "Read(.env:*)",
  "type": "bash",
  "command": "echo 'Blocked' >&2 && exit 2"
}
```

## Skills

Located in `skills/`

### api-docs-generator/
Generates comprehensive API documentation.

**Structure:**
```
api-docs-generator/
└── SKILL.md        # Main skill definition
```

**Usage:**
```
"Generate API documentation for all endpoints"
"Document the user authentication API"
```

**Tools:** Read, Write, Grep, Glob
**Model:** Sonnet

### How to Use
1. Copy entire folder to `.claude/skills/`
2. Claude will auto-invoke based on description
3. Add supporting files as needed (templates, scripts)

## Commands

Located in `commands/`

### deploy.md
Deployment workflow with safety checks.

**Usage:**
```bash
/deploy production
/deploy staging
```

**Features:**
- Pre-deployment validation
- Git status checks
- Test execution
- Safety confirmations

### review.md
Comprehensive code review of changes.

**Usage:**
```bash
/review
```

**Features:**
- Shows git diff
- Reviews for security, quality, performance
- Provides severity ratings
- Actionable recommendations

### How to Use
1. Copy to `.claude/commands/` in your project
2. Use by typing `/command-name`
3. Customize for your workflow

## Quick Start

### Setting Up a New Project

1. **Create .claude/ directory:**
```bash
mkdir -p .claude/{agents,commands,skills}
```

2. **Copy examples:**
```bash
cp examples/subagents/* .claude/agents/
cp examples/commands/* .claude/commands/
cp examples/hooks/settings-example.json .claude/settings.json
```

3. **Customize for your project:**
- Edit tool permissions
- Adjust hook commands
- Update descriptions

### Testing Your Configuration

1. **Test sub-agents:**
```
"Review this code" (should trigger code-reviewer)
```

2. **Test hooks:**
```
Write a Python file and check if Black runs
```

3. **Test commands:**
```
/review
/deploy staging
```

## Best Practices

### Sub-agents
- ✅ Give clear, specific descriptions
- ✅ Use read-only tools for reviewers
- ✅ Choose appropriate model for task
- ❌ Don't give excessive tool permissions

### Hooks
- ✅ Test hooks in isolation first
- ✅ Use exit code 2 to block operations
- ✅ Quote file paths properly
- ❌ Don't create complex hook logic (use scripts instead)

### Skills
- ✅ Include trigger keywords in description
- ✅ Provide clear instructions
- ✅ Add supporting files for complex skills
- ❌ Don't make skills too broad (keep focused)

### Commands
- ✅ Add descriptions for documentation
- ✅ Use argument-hint for user guidance
- ✅ Include safety checks for risky operations
- ❌ Don't put sensitive data in commands

## Customization Tips

### Adapting for Your Stack

**Python Projects:**
- Use `black` for formatting
- Use `pytest` for testing
- Use `pylint` or `flake8` for linting

**JavaScript Projects:**
- Use `prettier` for formatting
- Use `jest` or `mocha` for testing
- Use `eslint` for linting

**Ruby Projects:**
- Use `rubocop` for formatting
- Use `rspec` for testing

### Team Sharing

**Project-level** (shared with team):
- `.claude/settings.json` (commit to git)
- `.claude/agents/` (commit to git)
- `.claude/commands/` (commit to git)

**Personal** (your machine only):
- `.claude/settings.local.json` (gitignored)
- `~/.claude/agents/` (global)
- `~/.claude/commands/` (global)

## Troubleshooting

### Agent Not Invoking
- Check description includes trigger keywords
- Verify file is in correct location
- Try explicit invocation: "Use code-reviewer to review this"

### Hook Not Running
- Check matcher pattern is correct
- Verify command has correct permissions
- Check exit code (use `echo $?` to debug)
- Test command manually first

### Command Not Found
- Ensure file is in `.claude/commands/`
- Check filename matches command name
- Verify YAML frontmatter is valid

## Further Reading

- See `notebooks/` for detailed learning guides
- See `docs/quick-reference.md` for command reference
- See `templates/` for starter templates
- See official docs at https://docs.claude.com/claude-code
