# Claude Code Hook Examples

This directory contains example hook scripts for Claude Code. Hooks allow you to automate actions in response to Claude Code events.

## Available Hooks

### 1. `validate-commit.sh` - Pre-commit Validation

**When it runs:** Before every git commit

**What it does:**
- ✅ Checks for hardcoded secrets (API keys, passwords)
- ✅ Validates Python/JavaScript syntax
- ✅ Prevents committing large files (>10MB)
- ✅ Warns about TODO/FIXME comments
- ✅ Ensures code quality before commits

**Setup:**
```bash
# Copy to your project
cp validate-commit.sh /your/project/.claude/hooks/

# Make executable
chmod +x /your/project/.claude/hooks/validate-commit.sh

# Configure as git pre-commit hook
ln -s .claude/hooks/validate-commit.sh .git/hooks/pre-commit
```

**Usage:**
Runs automatically on `git commit`. Will block commit if issues found.

---

### 2. `tool-call-logger.sh` - Tool Call Logging

**When it runs:** Every time Claude uses a tool

**What it does:**
- 📝 Logs every tool call to `.claude/logs/tool-calls.log`
- 📊 Creates detailed JSON logs for analysis
- 🔔 Sends desktop notifications (optional)
- 📈 Helps debug and track Claude's actions

**Setup:**
```bash
cp tool-call-logger.sh /your/project/.claude/hooks/
chmod +x /your/project/.claude/hooks/tool-call-logger.sh
```

**Configuration in `.claude/settings.json`:**
```json
{
  "hooks": {
    "tool_call": {
      "enabled": true,
      "commands": ["bash .claude/hooks/tool-call-logger.sh"]
    }
  }
}
```

**Usage:**
Runs automatically. Check logs:
```bash
tail -f .claude/logs/tool-calls.log
```

---

### 3. `security-check.sh` - Security Audit

**When it runs:** Before commits (as pre-commit hook)

**What it does:**
- 🔒 Detects SQL injection vulnerabilities
- 🔒 Finds command injection risks
- 🔒 Checks for XSS vulnerabilities
- 🔒 Scans for hardcoded secrets
- 🔒 Audits dependencies for vulnerabilities
- 🔒 Identifies weak cryptography

**Setup:**
```bash
cp security-check.sh /your/project/.claude/hooks/
chmod +x /your/project/.claude/hooks/security-check.sh

# As pre-commit hook
ln -s .claude/hooks/security-check.sh .git/hooks/pre-commit

# Or run manually
bash .claude/hooks/security-check.sh
```

**Requirements:**
- `npm audit` (for Node.js projects)
- `safety` (for Python: `pip install safety`)

**Usage:**
```bash
# Automatic on commit
git commit -m "message"

# Manual security scan
bash .claude/hooks/security-check.sh

# Skip hook temporarily (not recommended)
git commit --no-verify
```

---

### 4. `format-code.sh` - Auto Code Formatting

**When it runs:** Before commits

**What it does:**
- 🎨 Auto-formats Python with Black
- 🎨 Sorts Python imports with isort
- 🎨 Formats JavaScript/TypeScript with Prettier
- 🎨 Fixes ESLint issues automatically
- 🎨 Formats JSON, YAML, Markdown
- 🎨 Formats Go, Rust code

**Setup:**
```bash
cp format-code.sh /your/project/.claude/hooks/
chmod +x /your/project/.claude/hooks/format-code.sh

# As pre-commit hook
ln -s .claude/hooks/format-code.sh .git/hooks/pre-commit
```

**Requirements:**
```bash
# Python
pip install black isort

# JavaScript/TypeScript
npm install -g prettier eslint

# JSON
brew install jq  # or apt-get install jq

# Other languages' formatters
# Go: gofmt (built-in)
# Rust: rustfmt (built-in)
```

**Usage:**
Runs automatically on commit. Formats staged files and re-stages them.

---

### 5. `notify-completion.sh` - Task Completion Notifications

**When it runs:** After Claude completes a task

**What it does:**
- 🔔 Sends completion notifications
- 📱 Multiple notification methods (terminal, desktop, Slack, email)
- 📊 Logs completion history
- 🔊 Plays sound (optional)

**Setup:**
```bash
cp notify-completion.sh /your/project/.claude/hooks/
chmod +x /your/project/.claude/hooks/notify-completion.sh
```

**Configuration in `.claude/settings.json`:**
```json
{
  "hooks": {
    "assistant_message": {
      "enabled": true,
      "commands": [
        "NOTIFY_METHOD=desktop bash .claude/hooks/notify-completion.sh"
      ]
    }
  }
}
```

**Notification Methods:**
- `terminal` - Console output (default)
- `desktop` - System notifications
- `slack` - Slack webhook
- `email` - Email notifications
- `all` - All methods

**Slack Setup:**
```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

**Email Setup:**
```bash
export EMAIL_TO="your@email.com"
```

---

## Creating Your Own Hooks

### Hook Template

```bash
#!/bin/bash
# Description of what this hook does

set -e  # Exit on error

echo "Running my custom hook..."

# Your hook logic here

# Exit 0 to allow action, exit 1 to block
exit 0
```

### Hook Types

**Available in Claude Code:**

1. **`tool_call`** - Before Claude uses a tool
   ```json
   {
     "hooks": {
       "tool_call": {
         "enabled": true,
         "commands": ["bash .claude/hooks/your-hook.sh"]
       }
     }
   }
   ```

2. **`user_prompt_submit`** - When user sends a message
   ```json
   {
     "hooks": {
       "user_prompt_submit": {
         "enabled": true,
         "commands": ["bash .claude/hooks/your-hook.sh"]
       }
     }
   }
   ```

3. **`assistant_message`** - After Claude responds
   ```json
   {
     "hooks": {
       "assistant_message": {
         "enabled": true,
         "commands": ["bash .claude/hooks/your-hook.sh"]
       }
     }
   }
   ```

### Hook Environment Variables

Hooks receive context via environment variables:

- `TOOL_NAME` - Name of the tool being called
- `TOOL_ARGS` - Arguments passed to the tool
- `TASK_NAME` - Current task name
- `TASK_STATUS` - Task status (completed, failed, etc.)
- `CLAUDE_SESSION_ID` - Current session ID
- `PWD` - Current working directory

### Testing Hooks

```bash
# Make executable
chmod +x your-hook.sh

# Test manually
bash your-hook.sh

# Check for syntax errors
bash -n your-hook.sh

# Debug with verbose output
bash -x your-hook.sh
```

### Hook Best Practices

1. **Always exit with status code:**
   - `exit 0` - Success (allow action)
   - `exit 1` - Failure (block action)

2. **Make scripts executable:**
   ```bash
   chmod +x your-hook.sh
   ```

3. **Use absolute paths or check for commands:**
   ```bash
   if command -v python3 &> /dev/null; then
       python3 script.py
   fi
   ```

4. **Add error handling:**
   ```bash
   set -e  # Exit on error
   set -u  # Exit on undefined variable
   ```

5. **Provide feedback:**
   ```bash
   echo "✅ Hook completed successfully"
   ```

6. **Log for debugging:**
   ```bash
   LOG_FILE=".claude/logs/hook.log"
   echo "[$(date)] Hook executed" >> "$LOG_FILE"
   ```

### Disabling Hooks

**Temporarily (single command):**
```bash
git commit --no-verify  # Skip git hooks
```

**Permanently:**
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

## Troubleshooting

**Hook not running?**
1. Check it's executable: `chmod +x hook.sh`
2. Verify configuration in settings.json
3. Check for syntax errors: `bash -n hook.sh`
4. Look at logs: `.claude/logs/`

**Hook blocks action unexpectedly?**
1. Test manually: `bash hook.sh`
2. Check exit code: `echo $?`
3. Add debug output: `bash -x hook.sh`

**Permission denied?**
```bash
chmod +x .claude/hooks/*.sh
```

---

## Examples by Use Case

### Daily Development

1. **Code Quality:** `validate-commit.sh` + `format-code.sh`
2. **Security:** `security-check.sh`
3. **Awareness:** `tool-call-logger.sh`

### Team Projects

1. **Standards Enforcement:** `validate-commit.sh` + `format-code.sh`
2. **Security Compliance:** `security-check.sh`
3. **Notifications:** `notify-completion.sh` (Slack)

### Learning/Experimentation

1. **Track Actions:** `tool-call-logger.sh`
2. **Light Validation:** `validate-commit.sh` (warnings only)

---

## Additional Resources

- **Claude Code Docs:** https://docs.claude.com/claude-code
- **Hook Documentation:** https://docs.claude.com/claude-code/hooks
- **GitHub Issues:** https://github.com/anthropics/claude-code/issues

---

**Last Updated:** 2025-11-20
