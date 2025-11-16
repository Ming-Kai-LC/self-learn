# Claude Code Learning Series

A comprehensive, beginner-friendly guide to mastering Claude Code - Anthropic's official CLI for AI-assisted development.

## 📚 About This Series

This learning series takes you from Claude Code basics to advanced automation techniques through 10 hands-on Jupyter notebooks. Each notebook includes:
- Clear explanations and concepts
- Real-world examples
- Practical exercises
- Troubleshooting guides
- Best practices
- Quick reference cards

## 🎯 Learning Paths

### Fast Track (Essential - ~4 hours)
Get productive quickly with the minimum essential knowledge:

1. **Notebook 01: Claude Code Basics** ⭐ (45-60 min)
   - Installation and setup
   - Interface and commands
   - Basic workflows

2. **Notebook 05: Slash Commands** ⭐ (30-45 min)
   - Built-in commands
   - Creating custom commands

3. **Notebook 07a: Essential Tools** ⭐ (30-45 min)
   - Core file and search tools
   - Basic bash execution
   - Simple workflows

4. **Notebook 09: Project Setup** ⭐ (45-60 min)
   - Project configuration
   - Team collaboration

### Full Path (Recommended - ~12 hours)
Complete learning experience covering all features:

1. **Notebook 01: Claude Code Basics** - ⭐ Beginner (45-60 min)
2. **Notebook 02: Sub-agents Guide** - ⭐ Beginner (45-60 min)
3. **Notebook 03: Hooks and Automation** - ⭐⭐ Intermediate (60-75 min)
4. **Notebook 04: Skills Development** - ⭐⭐ Intermediate (90-120 min)
5. **Notebook 05: Slash Commands** - ⭐ Beginner (30-45 min)
6. **Notebook 06: MCP Integrations** - ⭐⭐⭐ Advanced (90-120 min)
7. **Notebook 07a: Essential Tools** - ⭐ Beginner (30-45 min)
8. **Notebook 07b: Advanced Tools** - ⭐⭐ Intermediate (45-60 min)
9. **Notebook 08: Git Workflows** - ⭐⭐ Intermediate (60-75 min)
10. **Notebook 09: Project Setup** - ⭐⭐ Intermediate (45-60 min)
11. **Notebook 10: Advanced Techniques** - ⭐⭐⭐⭐ Advanced (90-120 min)

### By Use Case
**"I want to automate my development workflow"**
→ Notebooks 01, 03, 05, 09

**"I want to integrate external tools"**
→ Notebooks 01, 06, 09

**"I want better Git workflows"**
→ Notebooks 01, 08, 09

**"I want team collaboration features"**
→ Notebooks 01, 04, 05, 09

**"I'm an experienced developer, skip the basics"**
→ Notebooks 04, 06, 07, 10

## 📖 Notebook Details

### 01: Claude Code Basics (⭐ Beginner)
**What you'll learn:**
- Install and configure Claude Code
- Use the interface and keyboard shortcuts
- Execute built-in commands
- Manage conversations and tokens
- Work with files and projects

**Prerequisites:** None
**Estimated time:** 45-60 minutes

---

### 02: Sub-agents Guide (⭐ Beginner)
**What you'll learn:**
- What sub-agents are and when to use them
- Built-in sub-agents (Plan, Explore, General-Purpose)
- Create custom sub-agents
- Configure tool permissions
- Choose the right AI model

**Prerequisites:** Notebook 01
**Estimated time:** 45-60 minutes

---

### 03: Hooks and Automation (⭐⭐ Intermediate)
**What you'll learn:**
- Automate workflows with hooks
- Hook types (session, tool, git)
- Create hooks for different languages
- Best practices and security
- Real-world automation examples

**Prerequisites:** Notebook 01, basic shell scripting helpful
**Estimated time:** 60-75 minutes

---

### 04: Skills Development (⭐⭐ Intermediate)
**What you'll learn:**
- Create reusable skills
- Skills vs Sub-agents vs Hooks (when to use which)
- Skill file structure
- Real-world skill examples
- Organize and share skills

**Prerequisites:** Notebooks 01, 02
**Estimated time:** 90-120 minutes

---

### 05: Slash Commands (⭐ Beginner)
**What you'll learn:**
- Built-in slash commands overview
- Create custom commands
- Command parameters and arguments
- Command chaining
- Team command organization

**Prerequisites:** Notebook 01
**Estimated time:** 30-45 minutes

---

### 06: MCP Integrations (⭐⭐⭐ Advanced)
**What you'll learn:**
- Model Context Protocol (MCP) fundamentals
- Connect Claude Code to external services
- Available MCP servers (GitHub, Slack, databases)
- Create custom MCP servers
- Security best practices

**Prerequisites:**
- Notebooks 01, 05, 09
- Basic understanding of APIs, environment variables, JSON
- Comfort with npm/Node.js

**Estimated time:** 90-120 minutes

**⚠️ Note:** This is an advanced topic. Consider skipping initially and returning when you need external integrations.

---

### 07a: Essential Tools (⭐ Beginner)
**What you'll learn:**
- Core file tools: Read, Write, Edit
- Search tools: Grep, Glob
- Basic Bash command execution
- Simple tool workflows
- Essential best practices

**Prerequisites:** Notebook 01
**Estimated time:** 30-45 minutes

**Note:** Complete this before moving to 07b!

---

### 07b: Advanced Tools & Workflows (⭐⭐ Intermediate)
**What you'll learn:**
- TodoWrite for task management
- Web tools (WebFetch, WebSearch)
- Notebook editing (NotebookEdit)
- Background processes (BashOutput, KillShell)
- Advanced workflow patterns
- Tool permissions and security
- Performance optimization

**Prerequisites:** Notebook 01, **07a Essential Tools (required!)**
**Estimated time:** 45-60 minutes

---

### 08: Git Workflows (⭐⭐ Intermediate)
**What you'll learn:**
- Git integration in Claude Code
- Creating commits and pull requests
- Code review workflows
- Branch management
- Best practices for git operations

**Prerequisites:**
- Notebook 01
- **Basic Git knowledge required** (commits, branches, push/pull)

**Estimated time:** 60-75 minutes

**📚 Git Resources:**
- [GitHub Git Guide](https://guides.github.com/introduction/git-handbook/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

---

### 09: Project Setup (⭐⭐ Intermediate)
**What you'll learn:**
- Configure Claude Code for your project
- Project configuration files
- Set up hooks, skills, and commands
- Team collaboration setup
- Environment-specific configurations

**Prerequisites:** Notebooks 01, 03, 04, 05
**Estimated time:** 45-60 minutes

---

### 10: Advanced Techniques (⭐⭐⭐⭐ Advanced)
**What you'll learn:**
- Advanced prompt engineering
- Complex multi-step workflows
- Combine all features (hooks + skills + commands + MCP)
- Performance optimization
- Token management strategies
- Real-world advanced use cases

**Prerequisites:** All previous notebooks (01-09)
**Estimated time:** 90-120 minutes

---

## 🚀 Getting Started

### Prerequisites
- **Claude Code CLI** installed ([Installation Guide](https://docs.claude.com/claude-code))
- Python 3.8+ (for running Jupyter notebooks)
- Git (for git workflow examples)
- Basic command line knowledge

### Setup

**Option 1: Jupyter Notebook**
```bash
# Install Jupyter
pip install jupyter

# Navigate to the notebooks directory
cd projects/claude-integration/notebooks/

# Start Jupyter
jupyter notebook

# Open 01_claude_code_basics.ipynb
```

**Option 2: VS Code**
```bash
# Install Python extension for VS Code
# Open the notebooks/ directory in VS Code
# Click on any .ipynb file to view
```

**Option 3: JupyterLab**
```bash
# Install JupyterLab
pip install jupyterlab

# Start JupyterLab
jupyter lab

# Navigate to notebooks/
```

## 🎓 How to Use This Series

### For Complete Beginners
1. Start with **Notebook 01** (Claude Code Basics)
2. Complete all exercises in each notebook before moving on
3. Follow the **Full Path** in order
4. Don't skip the troubleshooting sections - they're valuable!
5. Experiment as you learn - create your own examples

### For Experienced Developers
1. Skim **Notebook 01** to understand Claude Code specifics
2. Focus on **Notebooks 04, 06, 07, 10** for advanced features
3. Reference other notebooks as needed
4. Jump directly to topics that interest you

### For Team Leads
1. Complete **Notebooks 01, 04, 05, 09** to understand configuration
2. Set up project standards using Notebook 09
3. Share skills and commands with your team (Notebooks 04, 05)
4. Establish team hooks for quality control (Notebook 03)

## 📊 Progress Tracking

Use this checklist to track your progress:

- [ ] 01: Claude Code Basics
- [ ] 02: Sub-agents Guide
- [ ] 03: Hooks and Automation
- [ ] 04: Skills Development
- [ ] 05: Slash Commands
- [ ] 06: MCP Integrations
- [ ] 07a: Essential Tools
- [ ] 07b: Advanced Tools
- [ ] 08: Git Workflows
- [ ] 09: Project Setup
- [ ] 10: Advanced Techniques

## 🤔 Decision Guides

### When to Use What?

#### Sub-agents vs Skills vs Hooks
```
┌─────────────────────────────────────────────────────┐
│ Need automated response to an event?               │
│ (e.g., format on save, test on commit)            │
└──────────────────────┬──────────────────────────────┘
                       │ YES → Use HOOKS (Notebook 03)
                       │
┌──────────────────────▼──────────────────────────────┐
│ Need reusable task/workflow with custom prompts?   │
│ (e.g., code review, documentation generation)      │
└──────────────────────┬──────────────────────────────┘
                       │ YES → Use SKILLS (Notebook 04)
                       │
┌──────────────────────▼──────────────────────────────┐
│ Need specialized AI with different tools/model?    │
│ (e.g., security auditor, performance analyzer)     │
└──────────────────────┬──────────────────────────────┘
                       │ YES → Use SUB-AGENTS (Notebook 02)
                       │
                       │ NONE OF THE ABOVE
                       ▼
          Use SLASH COMMANDS (Notebook 05)
```

#### Which Notebook Should I Read Next?
```
Start: Notebook 01 (Always start here)
   │
   ├─ Want automation? → Notebook 03 → Notebook 05 → Notebook 09
   │
   ├─ Want AI customization? → Notebook 02 → Notebook 04
   │
   ├─ Want external tools? → Notebook 06
   │
   ├─ Want Git help? → Notebook 08
   │
   └─ Ready for advanced? → Notebook 10 (after completing 01-09)
```

## 🆘 Getting Help

### Common Issues

**"Claude isn't doing what I want"**
- Review advanced prompt engineering (Notebook 10)
- Check your tool permissions (Notebook 09)
- Try Plan Mode for exploration (Notebook 01)

**"I'm overwhelmed by the options"**
- Follow the Fast Track path
- Start with Notebooks 01, 05, 09
- Add features as you need them

**"My hooks/skills/commands aren't working"**
- Check troubleshooting sections in respective notebooks
- Verify file locations and syntax
- Test components individually

### Resources
- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [MCP Protocol Docs](https://modelcontextprotocol.io)
- [Community Forum](https://github.com/anthropics/claude-code/discussions)

## 📁 Project Structure

```
claude-integration/
├── notebooks/          # 11 comprehensive learning notebooks
│   ├── 01_claude_code_basics.ipynb
│   ├── 02_subagents_guide.ipynb
│   ├── 03_hooks_automation.ipynb
│   ├── 04_skills_development.ipynb
│   ├── 05_slash_commands.ipynb
│   ├── 06_mcp_integrations.ipynb
│   ├── 07a_essential_tools.ipynb
│   ├── 07b_advanced_tools.ipynb
│   ├── 08_git_workflows.ipynb
│   ├── 09_project_setup.ipynb
│   └── 10_advanced_techniques.ipynb
├── examples/           # Sample configurations
│   ├── hooks/
│   ├── skills/
│   ├── subagents/
│   └── commands/
└── README.md           # This file
```

## 💡 Tips for Success

1. **Start Simple** - Don't try to learn everything at once
2. **Practice Actively** - Try each example in the notebooks
3. **Build Incrementally** - Add one feature at a time to your workflow
4. **Use Plan Mode** - When unsure, explore before executing
5. **Read CLAUDE.md** - Keep project context files updated
6. **Clear Often** - Use `/clear` to manage token usage
7. **Create Branches** - Always work on git branches for safety
8. **Review Changes** - Always review Claude's suggestions before accepting

## ⚠️ Common Pitfalls to Avoid

- ❌ Don't skip the basics - understanding fundamentals is crucial
- ❌ Don't give too much tool access without understanding implications
- ❌ Don't forget to test hooks and skills before deploying
- ❌ Don't commit sensitive data - use .gitignore and environment variables
- ❌ Don't amend other developers' commits
- ❌ Don't force push to main/master branches

## 🤝 Contributing

Found an issue or have a suggestion?
1. Check existing issues in the repository
2. Create a detailed bug report or feature request
3. Submit a pull request with improvements

## 📝 License

This learning series is part of the python-projects-portfolio repository.

## 🙏 Acknowledgments

Built to help developers learn and master Claude Code efficiently, based on:
- Official Anthropic documentation
- Claude Code community best practices
- Real-world development workflows
- Continuous experimentation and learning

---

**Ready to start?** Open `notebooks/01_claude_code_basics.ipynb` and begin your journey! 🚀
