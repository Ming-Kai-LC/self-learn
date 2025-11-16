#!/usr/bin/env python3
"""
Simple auto-approval hook for Claude Code
Auto-approves ALL operations in all modes
"""
import json
import sys

def should_approve(hook_input):
    """
    Determine if the tool use should be auto-approved
    Returns: (should_allow: bool, reason: str)
    """
    tool_name = hook_input.get("tool", {}).get("name", "")

    # Auto-approve everything
    return True, f"✅ Auto-approved: {tool_name}"

try:
    # Read hook input from stdin
    hook_input = json.load(sys.stdin)

    # Determine approval
    should_allow, reason = should_approve(hook_input)

    decision = "allow" if should_allow else "ask"

    response = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason
        }
    }

    # Output JSON response
    print(json.dumps(response))
    sys.exit(0)

except Exception as e:
    # If anything goes wrong, default to asking user
    error_response = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": f"Hook error: {str(e)}"
        }
    }
    print(json.dumps(error_response))
    sys.exit(0)
