# Claude Code Auto-Approval Hooks

This directory contains PreToolUse hooks for Claude Code that implement full auto-approval.

## Available Hooks

### 1. `smart-approve.py` (Currently Active)

**Simple auto-approval hook - approves everything**

#### Behavior

**✅ Auto-approves ALL operations**
- Works in all modes: normal, plan, acceptEdits, etc.
- All tools approved: Bash, Edit, Write, Read, WebFetch, etc.
- Zero interruptions - complete automation
- Maximum productivity and workflow speed

#### Why This Approach?

Maximum automation:
- Complete trust in Claude Code
- No manual approvals needed
- Fastest possible workflow
- Simplest implementation

#### The Code

The entire hook logic is just ~15 lines:

```python
def should_approve(hook_input):
    tool_name = hook_input.get("tool", {}).get("name", "")

    # Auto-approve everything
    return True, f"✅ Auto-approved: {tool_name}"
```

### 2. `auto-approve.py` (Original version)

Earlier version with similar simple logic.

## Installation

The hook is already configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/smart-approve.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

## How It Works

1. Hook receives tool information from Claude Code
2. Immediately returns "allow" for all tools
3. No checks, no restrictions - pure automation

## Customization

To change the behavior, edit `smart-approve.py`:

**Make it always ask for approval (disable auto-approve):**
```python
def should_approve(hook_input):
    return False, "Manual approval required"
```

**Add specific tools that need approval:**
```python
def should_approve(hook_input):
    tool_name = hook_input.get("tool", {}).get("name", "")

    # Always ask for these tools
    if tool_name in ["Bash", "Write", "Edit"]:
        return False, f"Manual approval required for {tool_name}"

    # Auto-approve everything else
    return True, f"Auto-approved: {tool_name}"
```

## Testing

All operations auto-approve in any mode:
```bash
ls
git status
whoami
rm test.txt
echo "test" > file.txt
```

All commands execute without prompts, regardless of mode.

## Troubleshooting

**Hook not working?**
1. Check Python: `python --version`
2. Test manually:
   ```bash
   echo '{"tool":{"name":"Read","input":{}},"permission_mode":"default"}' | python .claude/hooks/smart-approve.py
   ```
3. Should output: `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow", ...}}`

**Want to disable the hook?**
Empty the hooks object in `.claude/settings.json`:
```json
{
  "hooks": {
  }
}
```

**Want to re-enable the hook?**
Copy the configuration from `.claude/settings.json.backup` back to `.claude/settings.json`

## References

- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code Settings Reference](https://code.claude.com/docs/en/settings)

---

**Last Updated**: 2025-11-14
**Version**: 1.0 (Simple plan-mode aware hook)
