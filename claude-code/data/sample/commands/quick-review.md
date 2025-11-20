Perform a quick code review on staged files:

1. Check which files are staged: `git diff --cached --name-only`
2. For each staged file, review for:
   - Basic code quality (readability, naming)
   - Common bugs (off-by-one, null checks)
   - Simple improvements (DRY violations)
3. Provide a summary with:
   - ✅ Files that look good
   - ⚠️ Files with minor issues
   - ❌ Files with problems that should be fixed
4. Be concise - focus on the most important issues

Output format:
```
## Quick Review Summary

✅ **Approved (X files)**
- file1.py: Clean code, good practices
- file2.js: Well structured

⚠️ **Minor Issues (X files)**
- file3.py: Variable naming could be improved (line 42)

❌ **Needs Work (X files)**
- file4.py: Missing error handling (line 78)

**Recommendation:** [Fix critical issues / Ready to commit]
```
