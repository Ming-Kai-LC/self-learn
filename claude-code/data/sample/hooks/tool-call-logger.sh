#!/bin/bash
# Tool call logging hook
# Logs all Claude tool calls for debugging and analysis

# Configuration
LOG_DIR=".claude/logs"
LOG_FILE="$LOG_DIR/tool-calls.log"
DETAILED_LOG="$LOG_DIR/tool-calls-detailed.json"

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Tool call info is passed as environment variables:
# - TOOL_NAME: Name of the tool being called
# - TOOL_ARGS: Arguments passed to the tool (JSON)
# - CONTEXT: Current working directory

# Simple log entry
echo "[$TIMESTAMP] Tool: ${TOOL_NAME:-UNKNOWN}" >> "$LOG_FILE"

# Detailed JSON log (useful for analysis)
cat >> "$DETAILED_LOG" <<EOF
{
  "timestamp": "$TIMESTAMP",
  "tool": "${TOOL_NAME:-UNKNOWN}",
  "cwd": "$(pwd)",
  "user": "$USER",
  "session_id": "${CLAUDE_SESSION_ID:-unknown}"
}
EOF

# Optional: Show notification (requires terminal-notifier or notify-send)
if command -v notify-send &> /dev/null; then
    notify-send "Claude Tool Call" "Tool: ${TOOL_NAME:-UNKNOWN}" 2>/dev/null || true
fi

# Print to console (visible to Claude)
echo "✓ Logged tool call: ${TOOL_NAME:-UNKNOWN}"

# Always allow the tool to execute
exit 0
