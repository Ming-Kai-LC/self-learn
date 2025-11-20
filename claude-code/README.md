# Claude Code Mastery - Educational Project

**A comprehensive educational portfolio for mastering Claude Code from beginner to advanced user.**

## Project Overview

This project provides a structured learning path to become proficient with Claude Code, Anthropic's agentic coding tool. From basic commands to building custom plugins, you'll learn to leverage Claude Code's full potential for software development, automation, and workflow optimization.

## Learning Objectives

By completing this educational series, you will:

1. **Master Core Concepts** - Understand tools, skills, slash commands, hooks, and MCP servers
2. **Build Custom Workflows** - Create automated workflows tailored to your development needs
3. **Develop Skills and Commands** - Write reusable skills and slash commands for your projects
4. **Integrate External Services** - Connect Claude Code with APIs, databases, and tools via MCP
5. **Orchestrate Subagents** - Delegate complex tasks to specialized AI agents
6. **Optimize Productivity** - Apply best practices and advanced patterns for maximum efficiency

## Project Structure

```
claude-code/
├── notebooks/           # Educational Jupyter notebooks (numbered 00-10)
│   ├── 00_setup_introduction.ipynb
│   ├── 01_basic_commands_navigation.ipynb
│   ├── 02_file_operations_tools.ipynb
│   ├── 03_working_with_skills.ipynb
│   ├── 04_custom_slash_commands.ipynb
│   ├── 05_hooks_automation.ipynb
│   ├── 06_mcp_servers_integrations.ipynb
│   ├── 07_subagents_orchestration.ipynb
│   ├── 08_advanced_workflows.ipynb
│   ├── 09_best_practices_optimization.ipynb
│   └── 10_final_project_custom_plugin.ipynb
├── data/
│   ├── sample/          # Example files, configs, and templates
│   └── projects/        # Sample projects for practice
├── docs/
│   ├── ClaudeCode-LearningPath.md     # Detailed learning roadmap
│   ├── CommandReference.md            # Quick reference guide
│   ├── SkillLibrary.md               # Skill examples and patterns
│   └── Troubleshooting.md            # Common issues and solutions
├── projects/            # Hands-on project examples
│   ├── 01_personal_assistant/
│   ├── 02_code_reviewer/
│   ├── 03_documentation_generator/
│   └── 04_workflow_automator/
├── tests/              # Validation and testing scripts
├── requirements.txt    # Python dependencies (for notebooks)
└── README.md          # This file
```

## Quick Start

### Prerequisites

- **Claude Code installed** - See [installation guide](https://github.com/anthropics/claude-code)
- **Basic terminal knowledge** - Familiarity with command line
- **Text editor** - VS Code, Vim, or your preferred editor
- **Git basics** - Understanding of version control
- **Python 3.8+** (for Jupyter notebooks)

### Installation

1. **Install Claude Code**:
   ```bash
   # MacOS/Linux
   curl -fsSL https://claude.ai/install.sh | bash

   # Windows PowerShell
   irm https://claude.ai/install.ps1 | iex

   # NPM (all platforms)
   npm install -g @anthropic-ai/claude-code
   ```

2. **Navigate to this project**:
   ```bash
   cd /home/user/self-learn/claude-code
   ```

3. **Set up Python environment** (for notebooks):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Start with notebook 00** and progress sequentially

## Learning Path

### Stage 1: Foundation (Modules 00-02) ⭐
**Difficulty**: Beginner
**Estimated Time**: 4-6 hours

- **Module 00**: Setup and Introduction
  - Installing and configuring Claude Code
  - Understanding the interface and basic concepts
  - Your first conversation with Claude Code

- **Module 01**: Basic Commands and Navigation
  - Using built-in slash commands
  - File and directory navigation
  - Reading and understanding codebases

- **Module 02**: File Operations and Tools
  - Read, Write, Edit tools
  - Glob and Grep for searching
  - Bash tool for terminal operations
  - Managing git workflows

### Stage 2: Customization (Modules 03-05) ⭐⭐
**Difficulty**: Intermediate
**Estimated Time**: 6-8 hours

- **Module 03**: Working with Skills
  - Understanding skill architecture
  - Using existing skills effectively
  - When skills activate automatically
  - Skill scopes (project vs personal)

- **Module 04**: Custom Slash Commands
  - Creating simple slash commands
  - Using $ARGUMENTS in commands
  - Organizing commands with namespacing
  - MCP-exposed commands

- **Module 05**: Hooks and Automation
  - Understanding hook types and events
  - Creating validation hooks
  - Automated quality gates
  - Best practices for hook development

### Stage 3: Advanced Integration (Modules 06-08) ⭐⭐⭐
**Difficulty**: Advanced
**Estimated Time**: 8-12 hours

- **Module 06**: MCP Servers and Integrations
  - Understanding Model Context Protocol
  - Installing and configuring MCP servers
  - Creating custom MCP servers
  - Connecting to external services (APIs, databases)

- **Module 07**: Subagents and Orchestration
  - Delegating tasks to specialized agents
  - Creating custom subagent definitions
  - Agent communication patterns
  - Parallel vs sequential execution

- **Module 08**: Advanced Workflows
  - Combining skills, commands, and hooks
  - Multi-step automation patterns
  - Error handling and recovery
  - Performance optimization

### Stage 4: Mastery (Modules 09-10) ⭐⭐⭐
**Difficulty**: Expert
**Estimated Time**: 10-15 hours

- **Module 09**: Best Practices and Optimization
  - Prompt engineering for Claude Code
  - Token optimization strategies
  - Security and privacy considerations
  - Team collaboration patterns

- **Module 10**: Final Project - Building a Custom Plugin
  - Plugin architecture and structure
  - Packaging skills, commands, and MCP servers
  - Distribution and versioning
  - Real-world plugin examples

## Key Concepts

### Core Components

1. **Tools**: Built-in capabilities (Read, Write, Edit, Bash, Grep, etc.)
2. **Skills**: AI-invoked, context-aware capabilities (project or personal)
3. **Slash Commands**: User-invoked prompts (simple markdown files)
4. **Hooks**: Event-driven automation (quality gates, auto-actions)
5. **MCP Servers**: External service integrations (APIs, databases, tools)
6. **Subagents**: Specialized AI agents for delegated tasks
7. **Plugins**: Packaged collections of the above components

### Decision Matrix: When to Use What

| Use Case | Tool Type | Example |
|----------|-----------|---------|
| Frequently used prompts | Slash Command | `/review-pr`, `/add-tests` |
| Context-aware expertise | Skill | Domain knowledge, frameworks |
| Automated quality checks | Hook | Pre-commit validation |
| External data access | MCP Server | Database queries, API calls |
| Complex multi-step tasks | Subagent | Code reviews, migrations |
| Shareable workflow | Plugin | Team automation bundles |

## Hands-On Projects

### Project 1: Personal AI Assistant (⭐)
Build a custom assistant with:
- Slash commands for daily workflows
- Skills for domain expertise
- Hooks for automatic organization

### Project 2: Code Review Automator (⭐⭐)
Create an automated code reviewer:
- Subagent for review delegation
- Hooks for pre-commit checks
- MCP integration with GitHub

### Project 3: Documentation Generator (⭐⭐)
Develop a doc generation system:
- Skills for documentation patterns
- Slash commands for templates
- Automated doc updates via hooks

### Project 4: Full-Stack Workflow Plugin (⭐⭐⭐)
Build a complete plugin combining:
- Multiple specialized skills
- Custom slash commands
- MCP server for external services
- Orchestrated subagents
- Event-driven hooks

## Quality Standards

This project follows strict educational quality standards:

- ✅ **Markdown Ratio**: ≥30% explanatory content
- ✅ **Exercise Count**: ≥3 exercises per major concept
- ✅ **Execution**: All notebooks runnable (code cells execute)
- ✅ **Code Quality**: Clear, commented, best-practice examples
- ✅ **Learning Objectives**: Clearly stated in each module
- ✅ **Prerequisites**: Explicitly documented
- ✅ **Practical Application**: Real-world examples and use cases

## Testing Your Knowledge

Each notebook includes:

1. **Conceptual Explanations** - Understanding the "why"
2. **Guided Examples** - Step-by-step demonstrations
3. **Practice Exercises** - Hands-on application
4. **Challenge Problems** - Advanced scenarios
5. **Project Integration** - Building toward final project

## Additional Resources

### Official Documentation

- [Claude Code GitHub Repository](https://github.com/anthropics/claude-code)
- [Anthropic Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

### Community Resources

- [Claude Developers Discord](https://discord.gg/claude-developers)
- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) - Curated resources
- [Claude Code Cheatsheet](https://awesomeclaude.ai/code-cheatsheet)

### Best Practices Guides

- [Claude Code Best Practices by Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Plugin Development Guide](https://www.anthropic.com/news/claude-code-plugins)

### Tutorial Series

- *Cooking with Claude Code: The Complete Guide* - Comprehensive tutorial
- *Understanding Claude Code's Full Stack* - Architecture deep dive

## Configuration Files

### Example .claude/settings.json

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
  }
}
```

### Example .gitignore Additions

```gitignore
# Claude Code
.claude/settings.local.json
*_tested.ipynb
.claude/cache/
```

## Tips for Success

1. **Start Simple** - Master basics before advanced features
2. **Experiment Safely** - Use test projects for learning
3. **Read Examples** - Study existing skills and commands
4. **Iterate Quickly** - Test, learn, improve
5. **Document Learnings** - Keep notes on what works
6. **Join Community** - Learn from others' experiences
7. **Think in Workflows** - Design end-to-end solutions
8. **Optimize Gradually** - Start working, then optimize
9. **Secure by Design** - Consider security from the start
10. **Share Knowledge** - Contribute back to community

## Common Pitfalls to Avoid

❌ **Don't**: Create too many skills that overlap
✅ **Do**: Create focused, single-purpose skills

❌ **Don't**: Use hooks for tasks requiring user input
✅ **Do**: Use hooks for automated validations only

❌ **Don't**: Hard-code paths in slash commands
✅ **Do**: Use relative paths and $ARGUMENTS

❌ **Don't**: Create complex MCP servers without testing
✅ **Do**: Start simple and add features incrementally

❌ **Don't**: Ignore token usage in long conversations
✅ **Do**: Use /rewind and start fresh when needed

## Troubleshooting

### Common Issues

**Claude Code won't start**
- Check installation: `claude --version`
- Verify Node.js version: `node --version` (18+)
- Review logs: `~/.claude/logs/`

**Skills not activating**
- Check SKILL.md format and description field
- Verify file location (.claude/skills/)
- Test with explicit skill invocation

**Hooks not running**
- Enable in settings.json
- Check hook script permissions
- Review hook logs for errors

**MCP server connection fails**
- Verify server configuration in settings
- Test server independently
- Check network/firewall settings

See `docs/Troubleshooting.md` for detailed solutions.

## Contributing

Improvements welcome:

1. Enhanced explanations and examples
2. Additional exercises and projects
3. New use cases and patterns
4. Bug fixes and corrections
5. Translation to other languages

## License

Educational use only. See repository root for license details.

## Support

For questions or issues:

1. Review module notebooks and explanations
2. Check `docs/` folder for detailed guides
3. Consult official Claude Code documentation
4. Join Claude Developers Discord community
5. Refer to main project CLAUDE.md for standards

---

**Start Date**: 2025
**Target Audience**: Developers, automation enthusiasts, AI power users
**Estimated Completion**: 30-40 hours (over 4-8 weeks)
**Difficulty**: ⭐ to ⭐⭐⭐ (Progressive)
**Prerequisites**: Basic terminal and programming knowledge

**Remember**: "The best way to learn is by doing. Start with simple commands, build confidence, then tackle advanced features." - Claude Code Philosophy
