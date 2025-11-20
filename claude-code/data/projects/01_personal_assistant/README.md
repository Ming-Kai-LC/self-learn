# Project 1: Personal AI Assistant

**Difficulty**: ⭐ Beginner
**Time**: 2-3 hours
**Modules**: 03-04

## Project Overview

Build a personal AI assistant using Claude Code skills and slash commands to automate your daily development workflow.

## Learning Goals

- Create custom slash commands for common tasks
- Build skills for domain expertise
- Organize your workflow
- Practice with real development scenarios

## What You'll Build

A personal assistant with:
- **Daily workflow commands**: Quick access to common tasks
- **Code review skills**: Automated quality checks
- **Documentation helpers**: Generate docs automatically
- **Git workflow shortcuts**: Streamlined version control

---

## Step 1: Plan Your Assistant (15 min)

### Identify Your Common Tasks

Think about what you do repeatedly:
- Code reviews?
- Writing tests?
- Creating documentation?
- Git operations?
- Debugging?

**Exercise**: List 5 tasks you do daily that could be automated.

```
My Top 5 Tasks:
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________
5. _________________________________
```

---

## Step 2: Create Your First Command (30 min)

### Command 1: Quick Code Review

**Create with Claude Code**:
```
"Create a slash command called 'quick-review' in .claude/commands/
that reviews code for:
- Basic code quality
- Common bugs
- Simple improvements
Keep it fast and concise for quick checks."
```

**Test it**:
```python
# test_code.py
def calculate(x,y):
    return x+y*2
```

```
/quick-review

[Paste the code above]
```

**Expected output**: Quick feedback on code quality

---

### Command 2: Generate Tests

**Create**:
```
"Create a slash command 'gen-tests' that accepts $ARGUMENTS
and generates pytest tests for the specified function/class.
Include:
- Happy path tests
- Edge cases
- Error handling"
```

**Test it**:
```
/gen-tests calculate function in test_code.py
```

---

### Command 3: Explain Code

**Create**:
```
"Create a command 'explain' that provides detailed explanation
of code, breaking down:
- What it does
- How it works
- Why it's structured this way
- Any potential issues"
```

---

## Step 3: Build Domain Skills (45 min)

### Skill 1: Python Best Practices

**Create with Claude Code**:
```
"Create a skill called 'python-expert' in .claude/skills/
that provides Python best practices guidance including:
- PEP 8 style guidelines
- Pythonic idioms
- Common patterns
- Performance tips
- Security considerations"
```

**File structure**:
```
.claude/skills/python-expert/
├── SKILL.md
└── examples/
    ├── good_patterns.py
    └── bad_patterns.py
```

**Test activation**:
```
"Show me the best way to read a CSV file in Python"
[Should activate python-expert skill]
```

---

### Skill 2: Testing Strategies

**Create**:
```
"Create a skill 'test-strategist' that helps with:
- Choosing what to test
- Test structure and organization
- Mocking strategies
- Test-driven development
- Coverage optimization"
```

---

## Step 4: Organize Into Namespaces (30 min)

### Create Command Structure

```
.claude/commands/
├── dev/
│   ├── review.md        → /dev/review
│   ├── test.md          → /dev/test
│   └── debug.md         → /dev/debug
├── docs/
│   ├── generate.md      → /docs/generate
│   ├── update.md        → /docs/update
│   └── api.md           → /docs/api
└── git/
    ├── commit.md        → /git/commit
    ├── pr.md            → /git/pr
    └── sync.md          → /git/sync
```

**Create with Claude Code**:
```
"Create a namespace structure for my commands:
1. 'dev' namespace for development tasks
2. 'docs' namespace for documentation
3. 'git' namespace for git operations"
```

---

## Step 5: Build Your Workflow (30 min)

### Morning Startup Routine

**Command**: `/morning-start`

```markdown
# .claude/commands/morning-start.md

Good morning! Let's start your dev session:

1. Show git status of current branch
2. Check for any uncommitted changes
3. Pull latest from remote
4. Run tests to ensure clean state
5. List any TODOs in the codebase

Ready to code! 🚀
```

---

### Pre-Commit Checklist

**Command**: `/pre-commit-check`

```markdown
# .claude/commands/pre-commit-check.md

Pre-commit checklist:

1. Run linter on changed files
2. Run tests on affected modules
3. Check for debugging code (print statements, breakpoints)
4. Verify documentation is updated
5. Check commit message follows conventions

When everything passes, commit with a clear message.
```

---

### End of Day Wrap-Up

**Command**: `/eod-wrap`

```markdown
# .claude/commands/eod-wrap.md

End of day wrap-up:

1. Show all uncommitted changes
2. List unfinished TODOs
3. Suggest what to commit vs continue tomorrow
4. Create summary of today's work
5. Push completed work to remote

Good work today! 👏
```

---

## Step 6: Test Your Assistant (30 min)

### Daily Workflow Test

**Morning**:
```
1. /morning-start
2. "Find all TODO comments in src/"
3. "Explain the authentication flow"
```

**During Work**:
```
1. Make some changes
2. /dev/review
3. /dev/test [function name]
4. /quick-review
```

**Before Commit**:
```
1. /pre-commit-check
2. Review changes
3. /git/commit "Your message"
```

**End of Day**:
```
1. /eod-wrap
2. Review summary
3. Push or defer
```

---

## Step 7: Customize and Expand (30+ min)

### Add Your Personal Touch

**Ideas for expansion**:

1. **Language-specific skills**
   - JavaScript expert
   - Go best practices
   - SQL optimization

2. **Project-type commands**
   - `/web/api-endpoint` - Create new API
   - `/web/component` - Create React component
   - `/data/notebook` - Create Jupyter notebook

3. **Team collaboration**
   - `/team/standup` - Generate standup notes
   - `/team/pr-review` - Review teammate's PR
   - `/team/pair` - Pair programming helper

4. **Learning helpers**
   - `/learn/concept [topic]` - Explain a concept
   - `/learn/example [topic]` - Show examples
   - `/learn/practice [topic]` - Practice exercises

---

## Bonus Features

### 1. Keyboard Shortcut Aliases

Create short aliases for frequent commands:
```
/qr  → /quick-review
/gt  → /gen-tests
/ex  → /explain
/ms  → /morning-start
```

### 2. Context-Aware Skills

Skills that activate automatically:
- When editing Python → python-expert
- When editing tests → test-strategist
- When creating docs → documentation-writer

### 3. Integration with Tools

Commands that use your favorite tools:
```
/lint      → Run linter
/format    → Run formatter
/coverage  → Check test coverage
/benchmark → Run performance tests
```

---

## Project Checklist

- [ ] Created at least 5 useful slash commands
- [ ] Built 2+ domain-specific skills
- [ ] Organized commands into namespaces
- [ ] Tested complete daily workflow
- [ ] Documented all commands
- [ ] Customized for your personal needs
- [ ] Used assistant for 1 full day
- [ ] Refined based on usage

---

## Success Criteria

Your personal assistant is successful when:
- ✅ You use it daily without thinking
- ✅ It saves you time on repetitive tasks
- ✅ Commands feel natural and intuitive
- ✅ Skills activate when expected
- ✅ You keep adding to it organically
- ✅ Other developers ask about it

---

## Next Steps

1. **Iterate**: Refine commands based on daily use
2. **Share**: Share useful commands with your team
3. **Expand**: Add more specialized skills
4. **Advanced**: Move to Project 2 (Code Reviewer)

---

## Troubleshooting

**Command not found?**
- Check spelling and location
- Run `/help` to see all commands
- Verify .claude/commands/ directory exists

**Skill not activating?**
- Check description field is clear
- Use explicit invocation: "Use [skill-name] skill"
- Review SKILL.md format

**Commands feel clunky?**
- Simplify the prompts
- Use $ARGUMENTS for flexibility
- Make commands more specific

---

## Examples and Templates

See `/data/sample/` directory for:
- Example command files
- Sample skill definitions
- Common patterns
- Template files

---

## Reflection Questions

1. Which commands do you use most?
2. Which skills activate most frequently?
3. What would make your assistant more useful?
4. What tasks still feel manual?
5. How has your workflow improved?

---

**Congratulations!** You've built your personal AI assistant. Keep refining it as you work, and it will become an indispensable part of your development workflow.

**Next**: Try [Project 2: Code Review Automator](../02_code_reviewer/README.md)
