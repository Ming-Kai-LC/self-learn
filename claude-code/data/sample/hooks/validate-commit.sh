#!/bin/bash
# Pre-commit validation hook
# Runs before every git commit to ensure code quality

set -e  # Exit on error

echo "🔍 Running pre-commit validation..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get list of staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

if [ -z "$STAGED_FILES" ]; then
    echo "${GREEN}✅ No files to validate${NC}"
    exit 0
fi

echo "Files to validate:"
echo "$STAGED_FILES"
echo ""

# Track if any checks fail
HAS_ERRORS=0

# Check 1: No secrets in code
echo "🔐 Checking for secrets..."
SECRET_PATTERNS=(
    "password\s*=\s*['\"][^'\"]+['\"]"
    "api[_-]?key\s*=\s*['\"][^'\"]+['\"]"
    "secret\s*=\s*['\"][^'\"]+['\"]"
    "token\s*=\s*['\"][^'\"]+['\"]"
    "sk-[a-zA-Z0-9]{32,}"
)

for pattern in "${SECRET_PATTERNS[@]}"; do
    if echo "$STAGED_FILES" | xargs grep -iE "$pattern" 2>/dev/null; then
        echo "${RED}❌ Potential secret found!${NC}"
        echo "Pattern: $pattern"
        HAS_ERRORS=1
    fi
done

if [ $HAS_ERRORS -eq 0 ]; then
    echo "${GREEN}✅ No secrets found${NC}"
fi

# Check 2: Python files - syntax check
echo ""
echo "🐍 Checking Python syntax..."
PY_FILES=$(echo "$STAGED_FILES" | grep "\.py$" || true)

if [ -n "$PY_FILES" ]; then
    for file in $PY_FILES; do
        if [ -f "$file" ]; then
            if ! python3 -m py_compile "$file" 2>/dev/null; then
                echo "${RED}❌ Syntax error in: $file${NC}"
                HAS_ERRORS=1
            else
                echo "${GREEN}✅ $file${NC}"
            fi
        fi
    done
else
    echo "${YELLOW}⊘ No Python files to check${NC}"
fi

# Check 3: JavaScript/TypeScript files - syntax check
echo ""
echo "📜 Checking JavaScript/TypeScript syntax..."
JS_FILES=$(echo "$STAGED_FILES" | grep -E "\.(js|ts|jsx|tsx)$" || true)

if [ -n "$JS_FILES" ]; then
    if command -v node &> /dev/null; then
        for file in $JS_FILES; do
            if [ -f "$file" ]; then
                if ! node --check "$file" 2>/dev/null; then
                    echo "${RED}❌ Syntax error in: $file${NC}"
                    HAS_ERRORS=1
                else
                    echo "${GREEN}✅ $file${NC}"
                fi
            fi
        done
    else
        echo "${YELLOW}⊘ Node.js not found, skipping JS check${NC}"
    fi
else
    echo "${YELLOW}⊘ No JavaScript files to check${NC}"
fi

# Check 4: Large files
echo ""
echo "📦 Checking file sizes..."
MAX_SIZE_MB=10
MAX_SIZE_BYTES=$((MAX_SIZE_MB * 1024 * 1024))

for file in $STAGED_FILES; do
    if [ -f "$file" ]; then
        FILE_SIZE=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        if [ $FILE_SIZE -gt $MAX_SIZE_BYTES ]; then
            SIZE_MB=$((FILE_SIZE / 1024 / 1024))
            echo "${RED}❌ File too large: $file (${SIZE_MB}MB > ${MAX_SIZE_MB}MB)${NC}"
            echo "   Consider adding to .gitignore or using Git LFS"
            HAS_ERRORS=1
        fi
    fi
done

if [ $HAS_ERRORS -eq 0 ]; then
    echo "${GREEN}✅ All files under size limit${NC}"
fi

# Check 5: TODO/FIXME comments
echo ""
echo "📝 Checking for TODO/FIXME..."
TODO_COUNT=$(echo "$STAGED_FILES" | xargs grep -iE "(TODO|FIXME)" 2>/dev/null | wc -l || echo 0)

if [ $TODO_COUNT -gt 0 ]; then
    echo "${YELLOW}⚠️  Found $TODO_COUNT TODO/FIXME comments${NC}"
    echo "Consider addressing these before committing:"
    echo "$STAGED_FILES" | xargs grep -inE "(TODO|FIXME)" 2>/dev/null || true
fi

# Final result
echo ""
echo "============================================"
if [ $HAS_ERRORS -eq 1 ]; then
    echo "${RED}❌ Validation failed! Please fix errors before committing.${NC}"
    echo "To bypass this check (not recommended): git commit --no-verify"
    exit 1
else
    echo "${GREEN}✅ All checks passed! Ready to commit.${NC}"
    exit 0
fi
