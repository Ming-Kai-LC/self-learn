# Claude Code Troubleshooting Guide

A comprehensive guide to diagnosing and solving common Claude Code issues.

---

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Authentication & Connection](#authentication--connection)
3. [Tool Errors](#tool-errors)
4. [Hooks Not Working](#hooks-not-working)
5. [Skills Not Activating](#skills-not-activating)
6. [MCP Server Issues](#mcp-server-issues)
7. [Performance Problems](#performance-problems)
8. [Context & Token Issues](#context--token-issues)
9. [Git Integration Problems](#git-integration-problems)
10. [General Debugging](#general-debugging)

---

## Installation Issues

### Claude Code Command Not Found

**Symptoms:**
```bash
claude --version
# bash: claude: command not found
```

**Diagnosis:**
```bash
# Check if Claude is installed
which claude

# Check PATH
echo $PATH
```

**Solutions:**

1. **Reinstall Claude Code:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   # or
   curl -fsSL https://claude.ai/install.sh | sh
   ```

2. **Add to PATH (if installed but not in PATH):**
   ```bash
   # For npm global installs
   export PATH="$PATH:$(npm root -g)/../bin"

   # Add to shell profile
   echo 'export PATH="$PATH:$(npm root -g)/../bin"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Check Node.js version:**
   ```bash
   node --version  # Should be v16+
   npm --version
   ```

---

### Permission Errors During Installation

**Symptoms:**
```
EACCES: permission denied
```

**Solutions:**

1. **Use npx without global install:**
   ```bash
   npx @anthropic-ai/claude-code
   ```

2. **Fix npm permissions:**
   ```bash
   mkdir ~/.npm-global
   npm config set prefix '~/.npm-global'
   export PATH=~/.npm-global/bin:$PATH
   ```

3. **Avoid sudo (not recommended):**
   ```bash
   # Last resort only
   sudo npm install -g @anthropic-ai/claude-code
   ```

---

## Authentication & Connection

### "API Key Invalid" Error

**Symptoms:**
```
Error: Invalid API key
Authentication failed
```

**Diagnosis:**
```bash
# Check if API key is set
echo $ANTHROPIC_API_KEY

# Check Claude settings
cat ~/.claude/settings.json | grep apiKey
```

**Solutions:**

1. **Set API key:**
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."

   # Make permanent
   echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
   source ~/.bashrc
   ```

2. **Update settings.local.json:**
   ```json
   {
     "apiKey": "sk-ant-..."
   }
   ```

3. **Check key format:**
   - Should start with `sk-ant-`
   - No extra spaces or quotes
   - Not expired (check Claude dashboard)

---

### Connection Timeout

**Symptoms:**
```
Error: Request timeout
Failed to connect to API
```

**Diagnosis:**
```bash
# Test internet connection
ping api.anthropic.com

# Check firewall
curl -I https://api.anthropic.com
```

**Solutions:**

1. **Check network connection**
2. **Configure proxy if needed:**
   ```bash
   export HTTPS_PROXY="http://proxy.company.com:8080"
   ```

3. **Increase timeout in settings:**
   ```json
   {
     "timeout": 60000
   }
   ```

---

## Tool Errors

### "Tool Failed: Read" Error

**Symptoms:**
```
Error: Failed to read file
Permission denied
File not found
```

**Diagnosis:**
```bash
# Check file exists
ls -la /path/to/file

# Check permissions
stat /path/to/file

# Check if Claude has access
```

**Solutions:**

1. **Use absolute paths:**
   ```
   Read /home/user/project/file.py
   # Not: Read ~/project/file.py
   ```

2. **Fix permissions:**
   ```bash
   chmod 644 file.py  # Read/write for owner
   ```

3. **Check if file exists:**
   ```bash
   # Create if missing
   touch file.py
   ```

---

### "Tool Failed: Write" Error

**Symptoms:**
```
Error: Failed to write file
Must read file first
Permission denied
```

**Diagnosis:**
- Did you read the file first? (Required for existing files)
- Check directory exists and is writable
- Check disk space

**Solutions:**

1. **Read file before writing (if it exists):**
   ```
   # First
   Read existing_file.py

   # Then
   Write existing_file.py with content
   ```

2. **Create directory first:**
   ```bash
   mkdir -p /path/to/directory
   ```

3. **Check disk space:**
   ```bash
   df -h
   ```

---

### "Tool Failed: Bash" Error

**Symptoms:**
```
Error: Command failed
Command timed out
Permission denied
```

**Diagnosis:**
```bash
# Test command manually
bash -c "your command here"

# Check if command exists
which command_name

# Check PATH
echo $PATH
```

**Solutions:**

1. **Use full paths:**
   ```bash
   /usr/bin/python3 script.py
   # Not: python script.py
   ```

2. **Increase timeout:**
   - Default: 2 minutes
   - Max: 10 minutes
   ```
   Bash command with timeout=600000
   ```

3. **Check permissions:**
   ```bash
   chmod +x script.sh
   ```

---

### "Tool Failed: Grep" Error

**Symptoms:**
```
Error: No matches found
Pattern invalid
Permission denied
```

**Diagnosis:**
```bash
# Test pattern with ripgrep
rg "pattern" /path

# Check regex syntax
echo "test" | grep -E "pattern"
```

**Solutions:**

1. **Escape special characters:**
   ```
   # For literal braces
   Grep "interface\\{\\}" --type go
   ```

2. **Use correct output mode:**
   ```
   Grep "pattern" --output_mode content
   # For: files_with_matches, content, count
   ```

3. **Check file type filter:**
   ```
   Grep "pattern" --type py
   # Supported: py, js, rs, go, java, etc.
   ```

---

## Hooks Not Working

### Hook Not Triggering

**Symptoms:**
- Hook script exists but doesn't run
- No output from hook

**Diagnosis:**
```bash
# Check hooks are enabled
cat .claude/settings.json | grep hooks

# Check script permissions
ls -la .claude/hooks/

# Test script manually
bash .claude/hooks/your-hook.sh
```

**Solutions:**

1. **Enable hooks in settings:**
   ```json
   {
     "hooks": {
       "tool_call": {
         "enabled": true,
         "commands": ["bash .claude/hooks/tool-call.sh"]
       }
     }
   }
   ```

2. **Make script executable:**
   ```bash
   chmod +x .claude/hooks/*.sh
   ```

3. **Check script syntax:**
   ```bash
   bash -n .claude/hooks/your-hook.sh  # Check for syntax errors
   ```

4. **Add debug logging:**
   ```bash
   #!/bin/bash
   echo "Hook triggered" >> /tmp/claude-hook.log
   echo "Args: $@" >> /tmp/claude-hook.log
   ```

---

### Hook Blocks Execution

**Symptoms:**
```
Error: Hook validation failed
Hook returned non-zero exit code
```

**Solutions:**

1. **Check exit code:**
   ```bash
   # Hook should exit 0 for success
   exit 0  # Allow
   exit 1  # Block
   ```

2. **Add error handling:**
   ```bash
   #!/bin/bash
   set -e  # Exit on error

   # Your hook logic

   exit 0  # Explicitly succeed
   ```

3. **Disable temporarily for debugging:**
   ```json
   {
     "hooks": {
       "tool_call": {
         "enabled": false
       }
     }
   }
   ```

---

## Skills Not Activating

### Skill Doesn't Trigger Automatically

**Symptoms:**
- Skill exists but Claude doesn't use it
- Wrong skill activates

**Diagnosis:**
```bash
# Check skill file exists
ls -la .claude/skills/

# Check skill format
cat .claude/skills/your-skill.md
```

**Solutions:**

1. **Check skill has proper header:**
   ```markdown
   description: Clear description of when to activate

   ## Instructions
   [Your instructions here]
   ```

2. **Use clear activation keywords:**
   ```markdown
   description: Activates when user asks about Python best practices

   Keywords: python, PEP 8, pythonic, code quality
   ```

3. **Invoke explicitly:**
   ```
   "Use the python-expert skill to review this code"
   ```

---

### Skill Format Invalid

**Symptoms:**
```
Warning: Skill file malformed
Skill ignored
```

**Solutions:**

1. **Validate skill format:**
   - Must be markdown (.md)
   - Must have `description:` front matter
   - Must have `## Instructions` section

2. **Use skill template:**
   ```markdown
   description: One-line description

   ## Instructions

   Your detailed instructions here.

   ## When to Activate

   List conditions for activation.
   ```

3. **Check for syntax errors:**
   - No missing closing tags
   - Proper markdown formatting
   - Valid JSON in code blocks (if any)

---

## MCP Server Issues

### MCP Server Won't Start

**Symptoms:**
```
Error: Failed to start MCP server
Connection refused
Server timeout
```

**Diagnosis:**
```bash
# Check server is installed
npm list -g @modelcontextprotocol/server-github

# Try starting manually
npx @modelcontextprotocol/server-github
```

**Solutions:**

1. **Install MCP server:**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Check configuration:**
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_TOKEN": "ghp_..."
         }
       }
     }
   }
   ```

3. **Check environment variables:**
   ```bash
   echo $GITHUB_TOKEN
   ```

4. **View server logs:**
   ```bash
   # Check Claude logs
   cat ~/.claude/logs/mcp-server-github.log
   ```

---

### MCP Tools Not Available

**Symptoms:**
- MCP server starts but tools not accessible
- "Tool not found" errors

**Solutions:**

1. **Restart Claude Code**

2. **Check server status:**
   ```
   /mcp status
   ```

3. **Reinstall MCP server:**
   ```bash
   npm uninstall -g @modelcontextprotocol/server-github
   npm install -g @modelcontextprotocol/server-github
   ```

---

## Performance Problems

### Claude Code is Slow

**Symptoms:**
- Long response times
- Hangs during execution
- High memory usage

**Diagnosis:**
```bash
# Check system resources
top
htop

# Check Claude process
ps aux | grep claude

# Check disk I/O
iostat
```

**Solutions:**

1. **Reduce context size:**
   ```
   /clear  # Clear conversation history
   /rewind 5  # Go back 5 messages
   ```

2. **Use smaller models for simple tasks:**
   ```json
   {
     "defaultModel": "haiku"  # Faster for simple tasks
   }
   ```

3. **Close unnecessary files:**
   - Don't keep large files open
   - Use Grep instead of reading huge files

4. **Increase timeout:**
   ```json
   {
     "timeout": 120000  # 2 minutes
   }
   ```

---

### Context Too Large

**Symptoms:**
```
Error: Context window exceeded
Token limit reached
```

**Solutions:**

1. **Clear conversation:**
   ```
   /clear
   ```

2. **Use more targeted commands:**
   ```
   # Instead of
   "Read all files in project"

   # Do
   "Read src/main.py"
   ```

3. **Use Grep/Glob instead of Read:**
   ```
   # Find specific content
   Grep "function_name" --output_mode files_with_matches

   # Then read only relevant files
   Read src/specific_file.py
   ```

---

## Context & Token Issues

### "Token Limit Exceeded"

**Solutions:**

1. **Use /rewind:**
   ```
   /rewind 10  # Remove last 10 messages
   ```

2. **Use /clear:**
   ```
   /clear  # Start fresh (keeps project context)
   ```

3. **Be more specific:**
   - Don't ask to read entire directories
   - Use Grep to find relevant files first
   - Read only what you need

---

### Claude "Forgets" Earlier Context

**Symptoms:**
- Claude asks for information already provided
- Repeats previous mistakes

**Solutions:**

1. **Save important info in files:**
   ```
   "Write these requirements to requirements.md"
   ```

2. **Use slash commands for summaries:**
   ```
   /summary  # Get summary of conversation
   ```

3. **Re-provide context:**
   - Copy-paste important decisions
   - Reference earlier messages

---

## Git Integration Problems

### Git Commands Failing

**Symptoms:**
```
Error: git command failed
fatal: not a git repository
Permission denied (publickey)
```

**Diagnosis:**
```bash
# Check git is available
which git
git --version

# Check repo status
git status

# Check remote
git remote -v
```

**Solutions:**

1. **Initialize repo:**
   ```bash
   git init
   ```

2. **Configure git:**
   ```bash
   git config user.name "Your Name"
   git config user.email "your@email.com"
   ```

3. **Setup SSH key for GitHub:**
   ```bash
   ssh-keygen -t ed25519 -C "your@email.com"
   cat ~/.ssh/id_ed25519.pub  # Add to GitHub
   ```

4. **Use HTTPS instead of SSH:**
   ```bash
   git remote set-url origin https://github.com/user/repo.git
   ```

---

### Push Failed

**Symptoms:**
```
Error: failed to push
rejected (non-fast-forward)
Permission denied
```

**Solutions:**

1. **Pull first:**
   ```bash
   git pull --rebase origin main
   ```

2. **Check branch name:**
   ```bash
   # Branch must start with 'claude/' for Claude Code
   git checkout -b claude/your-branch-name
   ```

3. **Check permissions:**
   - Verify GitHub token has write access
   - Check repository permissions

---

## General Debugging

### Enable Debug Logging

**In settings.json:**
```json
{
  "logLevel": "debug",
  "logFile": "~/.claude/debug.log"
}
```

**View logs:**
```bash
tail -f ~/.claude/debug.log
```

---

### Check Claude Code Version

```bash
claude --version
```

**Update to latest:**
```bash
npm update -g @anthropic-ai/claude-code
```

---

### Reset Configuration

**Backup first:**
```bash
cp -r ~/.claude ~/.claude.backup
```

**Reset:**
```bash
rm -rf ~/.claude/settings.json
# Claude will recreate with defaults
```

---

### Still Having Issues?

1. **Check GitHub Issues:**
   - https://github.com/anthropics/claude-code/issues
   - Search for similar problems

2. **Report a Bug:**
   - Use `/feedback` command
   - Or file issue on GitHub
   - Include:
     - Claude Code version
     - Operating system
     - Steps to reproduce
     - Error messages
     - Logs (if available)

3. **Community Support:**
   - Discord: [Claude Code community]
   - Forum: [Anthropic forum]

---

## Quick Reference: Common Fixes

| Problem | Quick Fix |
|---------|-----------|
| Command not found | `npm install -g @anthropic-ai/claude-code` |
| Auth error | `export ANTHROPIC_API_KEY="sk-ant-..."` |
| Tool failed | Check file exists, use absolute paths |
| Hook not working | `chmod +x .claude/hooks/*.sh` |
| Skill not activating | Check description and keywords |
| MCP server error | Check `env` variables in settings |
| Too slow | Use `/clear` or `/rewind` |
| Token limit | Be more specific in requests |
| Git push fails | Check branch starts with `claude/` |
| All else fails | `claude --version` then update |

---

## Diagnostic Checklist

When troubleshooting, check:

- [ ] Claude Code is latest version
- [ ] API key is valid and set
- [ ] Internet connection is working
- [ ] File/directory permissions are correct
- [ ] Git repository is properly configured
- [ ] Hooks are executable (chmod +x)
- [ ] Skills have proper format
- [ ] MCP server environment variables set
- [ ] Sufficient disk space available
- [ ] No firewall blocking connections

---

**Last Updated:** 2025-11-20
**Version:** 1.0

For latest troubleshooting tips, check: https://docs.claude.com/claude-code
