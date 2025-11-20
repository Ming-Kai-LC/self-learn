#!/bin/bash
# Task completion notification hook
# Sends notification when Claude completes a task

# Configuration
NOTIFY_METHOD="terminal"  # Options: terminal, desktop, slack, email

# Get task info from environment
TASK_NAME="${TASK_NAME:-Unknown task}"
TASK_STATUS="${TASK_STATUS:-completed}"
DURATION="${DURATION:-unknown}"

# Colors for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Function: Terminal notification
notify_terminal() {
    echo ""
    echo "======================================"
    if [ "$TASK_STATUS" = "completed" ]; then
        echo "${GREEN}✅ Task Completed${NC}"
    elif [ "$TASK_STATUS" = "failed" ]; then
        echo "${RED}❌ Task Failed${NC}"
    else
        echo "${BLUE}ℹ️  Task Status: $TASK_STATUS${NC}"
    fi
    echo "Task: $TASK_NAME"
    echo "Time: $TIMESTAMP"
    echo "Duration: $DURATION"
    echo "======================================"
    echo ""
}

# Function: Desktop notification
notify_desktop() {
    local title="Claude Task: $TASK_STATUS"
    local message="$TASK_NAME (${DURATION})"

    # Try different notification systems
    if command -v notify-send &> /dev/null; then
        # Linux (notify-send)
        notify-send "$title" "$message" 2>/dev/null
    elif command -v osascript &> /dev/null; then
        # macOS (AppleScript)
        osascript -e "display notification \"$message\" with title \"$title\"" 2>/dev/null
    elif command -v terminal-notifier &> /dev/null; then
        # macOS (terminal-notifier)
        terminal-notifier -title "$title" -message "$message" 2>/dev/null
    else
        # Fallback to terminal
        notify_terminal
    fi
}

# Function: Slack notification
notify_slack() {
    SLACK_WEBHOOK_URL="${SLACK_WEBHOOK_URL:-}"

    if [ -z "$SLACK_WEBHOOK_URL" ]; then
        echo "Warning: SLACK_WEBHOOK_URL not set"
        return 1
    fi

    local emoji="✅"
    if [ "$TASK_STATUS" != "completed" ]; then
        emoji="❌"
    fi

    local payload=$(cat <<EOF
{
  "text": "$emoji Claude Task: $TASK_STATUS",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Task:* $TASK_NAME\n*Status:* $TASK_STATUS\n*Duration:* $DURATION\n*Time:* $TIMESTAMP"
      }
    }
  ]
}
EOF
)

    curl -X POST -H 'Content-type: application/json' \
         --data "$payload" \
         "$SLACK_WEBHOOK_URL" 2>/dev/null
}

# Function: Email notification
notify_email() {
    EMAIL_TO="${EMAIL_TO:-}"

    if [ -z "$EMAIL_TO" ]; then
        echo "Warning: EMAIL_TO not set"
        return 1
    fi

    local subject="Claude Task: $TASK_STATUS - $TASK_NAME"
    local body="Task: $TASK_NAME
Status: $TASK_STATUS
Duration: $DURATION
Time: $TIMESTAMP"

    # Try to send email
    if command -v mail &> /dev/null; then
        echo "$body" | mail -s "$subject" "$EMAIL_TO" 2>/dev/null
    elif command -v sendmail &> /dev/null; then
        echo -e "To: $EMAIL_TO\nSubject: $subject\n\n$body" | sendmail -t 2>/dev/null
    else
        echo "Warning: No mail command available"
        return 1
    fi
}

# Function: Log to file
log_completion() {
    LOG_FILE=".claude/logs/task-completions.log"
    mkdir -p "$(dirname "$LOG_FILE")"

    echo "[$TIMESTAMP] $TASK_STATUS | $TASK_NAME | Duration: $DURATION" >> "$LOG_FILE"
}

# Main notification logic
case "$NOTIFY_METHOD" in
    terminal)
        notify_terminal
        ;;
    desktop)
        notify_desktop
        ;;
    slack)
        notify_slack
        ;;
    email)
        notify_email
        ;;
    all)
        notify_terminal
        notify_desktop
        notify_slack
        notify_email
        ;;
    *)
        notify_terminal
        ;;
esac

# Always log to file
log_completion

# Play sound (optional)
if [ "$PLAY_SOUND" = "true" ]; then
    if command -v afplay &> /dev/null; then
        # macOS
        afplay /System/Library/Sounds/Glass.aiff 2>/dev/null &
    elif command -v paplay &> /dev/null; then
        # Linux (PulseAudio)
        paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null &
    fi
fi

exit 0
