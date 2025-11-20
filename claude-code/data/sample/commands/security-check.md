Perform security audit on $ARGUMENTS:

1. Read the specified files or directory: $ARGUMENTS
2. Scan for security vulnerabilities following OWASP Top 10
3. Check for common security issues in the specific language/framework

## Security Scan Process

### 1. Input Validation
- [ ] User input is validated
- [ ] Input length limits enforced
- [ ] Type checking performed
- [ ] Whitelisting used (not blacklisting)

### 2. Injection Vulnerabilities
- [ ] SQL: Parameterized queries used
- [ ] Command: No shell injection possible
- [ ] Path: No path traversal vulnerabilities
- [ ] XSS: User input escaped in output

### 3. Authentication & Authorization
- [ ] No hardcoded credentials
- [ ] Passwords properly hashed (bcrypt, Argon2)
- [ ] Authorization checks present
- [ ] Session management secure

### 4. Sensitive Data
- [ ] No secrets in code
- [ ] Sensitive data not logged
- [ ] Encryption for data at rest
- [ ] TLS/HTTPS for transmission

### 5. Dependencies
- [ ] No known vulnerable dependencies
- [ ] Dependencies up to date
- [ ] Minimal dependency footprint

### 6. Error Handling
- [ ] Errors don't leak sensitive info
- [ ] Proper exception handling
- [ ] Security logging enabled

## Security Report

### Critical Issues 🚨 (Count: X)
**Must fix immediately - actively exploitable**

#### [Issue Type] - [OWASP Category]
**Location:** `file.py:42`
**Severity:** Critical
**CWE:** [CWE-XXX]

**Vulnerability:**
```python
# Vulnerable code
```

**Attack Scenario:**
[How an attacker could exploit this]

**Impact:**
[What damage could occur: data breach, RCE, etc.]

**Fix:**
```python
# Secure code
```

**References:**
- [OWASP Guide](link)
- [CWE Details](link)

---

### High Priority Issues ⚠️ (Count: X)
**Fix soon - significant security risk**

[Similar format as Critical]

---

### Medium Priority Issues 📋 (Count: X)
**Should address - potential security concern**

- **[Issue]** at `file.py:line` - [Brief description]
- **[Issue]** at `file.py:line` - [Brief description]

---

### Low Priority Issues ℹ️ (Count: X)
**Consider improving - best practices**

- [Issue 1]
- [Issue 2]

---

### Security Strengths ✅ (Count: X)
**What's done well - reinforce good practices**

- ✅ Parameterized queries used throughout
- ✅ Input validation comprehensive
- ✅ No hardcoded secrets found
- ✅ Proper error handling

---

## Overall Security Score: [X/10]

### Risk Level: [Low / Medium / High / Critical]

### Immediate Actions Required:
1. [Critical fix 1]
2. [Critical fix 2]

### Recommended Timeline:
- **0-24 hours:** Fix critical issues
- **1-7 days:** Address high priority
- **1-4 weeks:** Improve medium/low items

---

## Security Best Practices Checklist

For future development:
- [ ] Security review before each release
- [ ] Automated security scanning in CI/CD
- [ ] Regular dependency updates
- [ ] Security training for team
- [ ] Incident response plan
- [ ] Regular penetration testing

---

**Tools Used:**
- Static analysis: [Bandit, Semgrep, etc.]
- Dependency scan: [Safety, npm audit, etc.]
- Manual review: OWASP guidelines

**Note:** This is a point-in-time assessment. Security requires ongoing vigilance.
