# Getting Started with Claude Code Learning Project

Welcome! This guide will help you get the most out of this learning project.

## What You'll Learn

This project teaches you to master **Claude Code** - Anthropic's CLI tool for AI-assisted development. You'll learn:

- ✅ **Sub-agents**: Specialized AI assistants for different tasks
- ✅ **Hooks**: Automated workflows triggered by events
- ✅ **Skills**: Reusable capability packages
- ✅ **Slash Commands**: Custom commands for your workflow
- ✅ **MCP Integration**: Connect to external tools and services
- ✅ **Tools Mastery**: File operations, search, git automation
- ✅ **Git Workflows**: Automated commits and pull requests
- ✅ **Advanced Techniques**: Context management and optimization

## Prerequisites

### Required
- **Claude Code CLI** installed ([installation guide](https://docs.claude.com/claude-code))
- **Python 3.8+** (for Jupyter notebooks)
- **Git** (for git workflow examples)
- **Basic command line knowledge**

### Optional
- Node.js/npm (for JavaScript examples)
- Docker (for containerization examples)
- Your favorite code editor

## Quick Start (5 minutes)

### Step 1: Install Dependencies

```bash
cd projects/claude-integration
pip install jupyter ipykernel notebook
```

### Step 2: Launch Jupyter

```bash
jupyter notebook
```

This opens your browser with the notebook interface.

### Step 3: Start Learning

Open `notebooks/01_claude_code_basics.ipynb` and begin!

## Learning Paths

### Path 1: Complete Beginner (Week 1)

**Goal**: Understand Claude Code fundamentals

1. **Day 1-2**: Notebook 01 - Claude Code Basics
   - Learn the interface
   - Master keyboard shortcuts
   - Understand Plan vs Execute mode
   - Practice with built-in commands

2. **Day 3-4**: Notebook 02 - Sub-agents
   - Learn what sub-agents are
   - Create your first sub-agent
   - Understand tool permissions

3. **Day 5-7**: Notebook 03 - Hooks
   - Set up automated workflows
   - Create your first hook
   - Configure project settings

### Path 2: Intermediate User (Week 2)

**Goal**: Customize Claude Code for your workflow

1. **Day 1-2**: Notebook 04 - Skills Development
   - Create reusable skills
   - Build skill packages
   - Share skills across projects

2. **Day 3-4**: Notebook 05 - Slash Commands
   - Build custom commands
   - Use arguments and file references
   - Create project-specific workflows

3. **Day 5-7**: Notebook 06 - MCP Integrations
   - Connect external tools
   - Set up popular integrations
   - Build custom MCP servers

### Path 3: Advanced User (Week 3-4)

**Goal**: Master advanced features

1. **Week 3**: Notebooks 07-09
   - Tool mastery
   - Git workflow automation
   - Optimal project setup

2. **Week 4**: Notebook 10 + Real Projects
   - Advanced techniques
   - Apply to your actual projects
   - Build comprehensive workflows

## Alternative: Topic-Based Learning

Jump to what you need:

### "I want to automate repetitive tasks"
→ Start with Notebook 03 (Hooks) and 05 (Slash Commands)

### "I need better code reviews"
→ Check Notebook 02 (Sub-agents) and `examples/subagents/code-reviewer.md`

### "I want to improve my git workflow"
→ Go to Notebook 08 (Git Workflows)

### "I need to connect external tools"
→ Begin with Notebook 06 (MCP Integrations)

### "I want to understand everything"
→ Follow the sequential path: Notebooks 01-10

## Using the Examples

### Sub-agents

**Try the code reviewer:**
```bash
# Copy to your project
cp examples/subagents/code-reviewer.md .claude/agents/

# Then in Claude Code:
"Review this file for security issues"
```

### Hooks

**Add auto-formatting:**
```bash
# Copy hooks example
cp examples/hooks/settings-example.json .claude/settings.json

# Edit to match your tools
# Now Claude will auto-format files on write!
```

### Commands

**Use the review command:**
```bash
# Copy command
cp examples/commands/review.md .claude/commands/

# Use it
/review
```

## Hands-On Exercises

### Exercise 1: Create Your First Sub-agent (20 min)

1. Create `.claude/agents/` in a project
2. Copy `templates/subagent-template.md`
3. Customize for your needs
4. Test it with Claude Code

### Exercise 2: Set Up a Hook (15 min)

1. Create `.claude/settings.json`
2. Add a post-write formatting hook
3. Write a file and watch it auto-format
4. Experiment with different hooks

### Exercise 3: Build a Custom Command (15 min)

1. Create `.claude/commands/`
2. Copy a template
3. Create a command for your workflow
4. Use it with `/command-name`

## Quick Reference

### Essential Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `GETTING_STARTED.md` | This file |
| `docs/quick-reference.md` | Command cheat sheet |
| `examples/README.md` | Example configurations |
| `notebooks/01-10` | Learning materials |

### Essential Commands

```bash
# Start Claude Code
claude

# Plan Mode (read-only)
[Shift+Tab twice]

# Stop Claude
[Escape]

# Clear history
/clear

# Check token usage
/context

# Code review
/review
```

## Tips for Success

### 1. Start Small
Don't try to learn everything at once. Master one concept before moving on.

### 2. Practice Actively
Actually create the sub-agents, hooks, and commands. Don't just read about them.

### 3. Use Real Projects
Apply what you learn to your actual work. Real problems = real learning.

### 4. Experiment Safely
Always work on git branches. Use Plan Mode when exploring.

### 5. Build Incrementally
Add one feature at a time to your workflow.

### 6. Review the Quick Reference
Keep `docs/quick-reference.md` open for quick lookups.

### 7. Join the Community
Share your learnings and custom configurations!

## Troubleshooting

### "I can't find Claude Code"
Make sure it's installed: `claude --version`

### "Jupyter won't start"
Install it: `pip install jupyter notebook`

### "Sub-agent isn't working"
Check the file is in `.claude/agents/` and YAML is valid.

### "Hook isn't triggering"
Verify the matcher pattern and command are correct.

### "I'm overwhelmed"
Start with just Notebook 01. Master basics first!

## Next Steps

Once you've completed the learning path:

1. **Apply to Real Projects**: Set up Claude Code in your actual work
2. **Create Custom Configurations**: Build sub-agents/hooks for your team
3. **Share Your Knowledge**: Teach others what you've learned
4. **Contribute Back**: Add your examples to this project!

## Resources

- **Official Docs**: https://docs.claude.com/claude-code
- **Quick Reference**: `docs/quick-reference.md`
- **Examples**: `examples/` directory
- **Templates**: `templates/` directory

## Support

Having trouble?

1. Check the `docs/quick-reference.md`
2. Review relevant notebook
3. Look at examples in `examples/`
4. Consult official documentation
5. Experiment in Plan Mode safely

## Ready?

**Start here**: Open `notebooks/01_claude_code_basics.ipynb`

Have fun learning! 🚀
