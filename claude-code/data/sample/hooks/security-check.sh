#!/bin/bash
# Security check hook
# Validates that code changes don't introduce security issues

set -e

echo "🔒 Running security checks..."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SECURITY_ISSUES=0

# Get changed files
CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || echo "")

if [ -z "$CHANGED_FILES" ]; then
    echo "${GREEN}✅ No files to check${NC}"
    exit 0
fi

# Check 1: Hardcoded secrets
echo "Checking for hardcoded secrets..."
SECRET_PATTERNS=(
    'password\s*=\s*["\047][^"\047]+["\047]'
    'api[_-]?key\s*=\s*["\047][^"\047]+["\047]'
    'secret\s*=\s*["\047][^"\047]+["\047]'
    'token\s*=\s*["\047][^"\047]+["\047]'
    'private[_-]?key\s*=\s*["\047][^"\047]+["\047]'
    'sk-[a-zA-Z0-9]{32,}'
    'ghp_[a-zA-Z0-9]{36}'
    'AKIA[0-9A-Z]{16}'
)

for pattern in "${SECRET_PATTERNS[@]}"; do
    MATCHES=$(echo "$CHANGED_FILES" | xargs grep -iEn "$pattern" 2>/dev/null || true)
    if [ -n "$MATCHES" ]; then
        echo "${RED}❌ Potential secret found:${NC}"
        echo "$MATCHES"
        SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
    fi
done

# Check 2: SQL injection vulnerabilities
echo ""
echo "Checking for SQL injection risks..."
SQL_PATTERNS=(
    'execute\s*\(\s*f["\047].*SELECT'
    'execute\s*\(\s*["\047].*\+.*["\047]'
    'query\s*=\s*f["\047].*SELECT'
    'query\s*\+.*WHERE'
)

PY_FILES=$(echo "$CHANGED_FILES" | grep "\.py$" || true)
if [ -n "$PY_FILES" ]; then
    for pattern in "${SQL_PATTERNS[@]}"; do
        MATCHES=$(echo "$PY_FILES" | xargs grep -iEn "$pattern" 2>/dev/null || true)
        if [ -n "$MATCHES" ]; then
            echo "${YELLOW}⚠️  Possible SQL injection:${NC}"
            echo "$MATCHES"
            echo "Use parameterized queries instead"
            SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
        fi
    done
fi

# Check 3: Command injection
echo ""
echo "Checking for command injection risks..."
CMD_PATTERNS=(
    'os\.system\s*\(\s*f["\047]'
    'os\.system\s*\(.*\+.*\)'
    'subprocess\..*shell=True.*\+.*'
    'eval\s*\('
    'exec\s*\('
)

if [ -n "$PY_FILES" ]; then
    for pattern in "${CMD_PATTERNS[@]}"; do
        MATCHES=$(echo "$PY_FILES" | xargs grep -En "$pattern" 2>/dev/null || true)
        if [ -n "$MATCHES" ]; then
            echo "${YELLOW}⚠️  Possible command injection:${NC}"
            echo "$MATCHES"
            echo "Use subprocess with list arguments instead"
            SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
        fi
    done
fi

# Check 4: XSS vulnerabilities (JavaScript/TypeScript)
echo ""
echo "Checking for XSS risks..."
JS_FILES=$(echo "$CHANGED_FILES" | grep -E "\.(js|jsx|ts|tsx)$" || true)

if [ -n "$JS_FILES" ]; then
    XSS_PATTERNS=(
        'innerHTML\s*=.*\+.*'
        'innerHTML\s*=.*\$\{.*\}'
        'dangerouslySetInnerHTML'
    )

    for pattern in "${XSS_PATTERNS[@]}"; do
        MATCHES=$(echo "$JS_FILES" | xargs grep -En "$pattern" 2>/dev/null || true)
        if [ -n "$MATCHES" ]; then
            echo "${YELLOW}⚠️  Possible XSS vulnerability:${NC}"
            echo "$MATCHES"
            echo "Sanitize user input before rendering"
            SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
        fi
    done
fi

# Check 5: Insecure dependencies (if package files changed)
echo ""
echo "Checking dependencies..."

if echo "$CHANGED_FILES" | grep -q "package.json"; then
    if command -v npm &> /dev/null; then
        echo "Running npm audit..."
        if ! npm audit --audit-level=high 2>/dev/null; then
            echo "${RED}❌ Vulnerable dependencies found${NC}"
            echo "Run: npm audit fix"
            SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
        fi
    fi
fi

if echo "$CHANGED_FILES" | grep -q "requirements.txt"; then
    if command -v pip &> /dev/null && command -v safety &> /dev/null; then
        echo "Running safety check..."
        if ! safety check -r requirements.txt 2>/dev/null; then
            echo "${RED}❌ Vulnerable Python packages found${NC}"
            echo "Run: safety check -r requirements.txt"
            SECURITY_ISSUES=$((SECURITY_ISSUES + 1))
        fi
    fi
fi

# Check 6: Weak cryptography
echo ""
echo "Checking for weak cryptography..."
CRYPTO_PATTERNS=(
    'md5\('
    'sha1\('
    'random\.randint'
    'Math\.random\(\)'
)

for pattern in "${CRYPTO_PATTERNS[@]}"; do
    MATCHES=$(echo "$CHANGED_FILES" | xargs grep -En "$pattern" 2>/dev/null || true)
    if [ -n "$MATCHES" ]; then
        echo "${YELLOW}⚠️  Weak cryptography found:${NC}"
        echo "$MATCHES"
        echo "Use cryptographically secure alternatives (secrets module, crypto library)"
    fi
done

# Summary
echo ""
echo "============================================"
if [ $SECURITY_ISSUES -gt 0 ]; then
    echo "${RED}❌ Found $SECURITY_ISSUES security issue(s)${NC}"
    echo ""
    echo "Options:"
    echo "1. Fix the issues before committing"
    echo "2. Add exceptions to .security-exceptions (with justification)"
    echo "3. Skip hook: git commit --no-verify (NOT RECOMMENDED)"
    echo ""
    exit 1
else
    echo "${GREEN}✅ No security issues detected${NC}"
    exit 0
fi
