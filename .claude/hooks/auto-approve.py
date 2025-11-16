#!/usr/bin/env python3
"""
Context-aware auto-approval hook for Claude Code
Automatically approves tool operations based on context:
- Normal mode: Auto-approve
- Plan mode: Ask user for confirmation
"""
import json
import sys

try:
    # Read hook input from stdin
    hook_input = json.load(sys.stdin)

    # Get the tool being used
    tool_name = hook_input.get("tool", {}).get("name", "")

    # Check if we're in plan mode by looking at the tool
    # ExitPlanMode tool indicates we're in planning phase
    is_plan_mode = tool_name == "ExitPlanMode"

    # You can also check for other planning-related tools
    planning_tools = ["ExitPlanMode", "AskUserQuestion"]

    # Decision logic
    if is_plan_mode or tool_name in planning_tools:
        # In plan mode or using planning tools - ask user
        decision = "ask"
        reason = f"Manual approval required for {tool_name} (planning context)"
    else:
        # Normal mode - auto-approve
        decision = "allow"
        reason = "Auto-approved in normal execution mode"

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
