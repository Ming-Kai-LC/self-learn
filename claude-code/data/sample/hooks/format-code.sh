#!/bin/bash
# Code formatting hook
# Auto-formats code before committing

set -e

echo "🎨 Running code formatters..."

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

if [ -z "$STAGED_FILES" ]; then
    echo "${GREEN}✅ No files to format${NC}"
    exit 0
fi

FILES_FORMATTED=0

# Format Python files
PY_FILES=$(echo "$STAGED_FILES" | grep "\.py$" || true)

if [ -n "$PY_FILES" ]; then
    echo "${BLUE}Formatting Python files...${NC}"

    # Black formatter
    if command -v black &> /dev/null; then
        echo "$PY_FILES" | xargs black --quiet 2>/dev/null || true
        echo "${GREEN}✓ Black formatted${NC}"
        FILES_FORMATTED=1
    fi

    # isort (import sorting)
    if command -v isort &> /dev/null; then
        echo "$PY_FILES" | xargs isort --quiet 2>/dev/null || true
        echo "${GREEN}✓ Imports sorted${NC}"
        FILES_FORMATTED=1
    fi

    # autopep8 (fallback if black not available)
    if ! command -v black &> /dev/null && command -v autopep8 &> /dev/null; then
        echo "$PY_FILES" | xargs autopep8 --in-place 2>/dev/null || true
        echo "${GREEN}✓ autopep8 formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format JavaScript/TypeScript files
JS_FILES=$(echo "$STAGED_FILES" | grep -E "\.(js|jsx|ts|tsx)$" || true)

if [ -n "$JS_FILES" ]; then
    echo "${BLUE}Formatting JavaScript/TypeScript files...${NC}"

    # Prettier
    if command -v prettier &> /dev/null; then
        echo "$JS_FILES" | xargs prettier --write 2>/dev/null || true
        echo "${GREEN}✓ Prettier formatted${NC}"
        FILES_FORMATTED=1
    fi

    # ESLint with --fix
    if command -v eslint &> /dev/null; then
        echo "$JS_FILES" | xargs eslint --fix 2>/dev/null || true
        echo "${GREEN}✓ ESLint auto-fixed${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format JSON files
JSON_FILES=$(echo "$STAGED_FILES" | grep "\.json$" || true)

if [ -n "$JSON_FILES" ]; then
    echo "${BLUE}Formatting JSON files...${NC}"

    if command -v jq &> /dev/null; then
        for file in $JSON_FILES; do
            if [ -f "$file" ]; then
                jq '.' "$file" > "$file.tmp" && mv "$file.tmp" "$file" 2>/dev/null || true
            fi
        done
        echo "${GREEN}✓ JSON formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format YAML files
YAML_FILES=$(echo "$STAGED_FILES" | grep -E "\.(yaml|yml)$" || true)

if [ -n "$YAML_FILES" ]; then
    echo "${BLUE}Formatting YAML files...${NC}"

    if command -v yamlfmt &> /dev/null; then
        echo "$YAML_FILES" | xargs yamlfmt -w 2>/dev/null || true
        echo "${GREEN}✓ YAML formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format Markdown files
MD_FILES=$(echo "$STAGED_FILES" | grep "\.md$" || true)

if [ -n "$MD_FILES" ]; then
    echo "${BLUE}Formatting Markdown files...${NC}"

    if command -v prettier &> /dev/null; then
        echo "$MD_FILES" | xargs prettier --write 2>/dev/null || true
        echo "${GREEN}✓ Markdown formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format Go files
GO_FILES=$(echo "$STAGED_FILES" | grep "\.go$" || true)

if [ -n "$GO_FILES" ]; then
    echo "${BLUE}Formatting Go files...${NC}"

    if command -v gofmt &> /dev/null; then
        echo "$GO_FILES" | xargs gofmt -w 2>/dev/null || true
        echo "${GREEN}✓ gofmt formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Format Rust files
RS_FILES=$(echo "$STAGED_FILES" | grep "\.rs$" || true)

if [ -n "$RS_FILES" ]; then
    echo "${BLUE}Formatting Rust files...${NC}"

    if command -v rustfmt &> /dev/null; then
        echo "$RS_FILES" | xargs rustfmt 2>/dev/null || true
        echo "${GREEN}✓ rustfmt formatted${NC}"
        FILES_FORMATTED=1
    fi
fi

# Re-stage formatted files
if [ $FILES_FORMATTED -eq 1 ]; then
    echo ""
    echo "${BLUE}Re-staging formatted files...${NC}"
    echo "$STAGED_FILES" | xargs git add 2>/dev/null || true
    echo "${GREEN}✅ Code formatting complete${NC}"
else
    echo "${YELLOW}⊘ No formatters available or files to format${NC}"
    echo ""
    echo "Install formatters:"
    echo "  Python: pip install black isort"
    echo "  JavaScript: npm install -g prettier eslint"
    echo "  JSON: brew install jq (or apt-get install jq)"
fi

exit 0
