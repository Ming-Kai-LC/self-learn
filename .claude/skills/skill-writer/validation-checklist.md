# Skill Validation Checklist

Comprehensive checklist for validating Claude Code skills to ensure proper format, functionality, and best practices compliance.

---

## Quick Validation Checklist

Use this for rapid validation:

- [ ] YAML frontmatter starts on line 1 with `---`
- [ ] YAML frontmatter ends with `---` before content
- [ ] No tabs in YAML (spaces only)
- [ ] Name is lowercase with hyphens only
- [ ] Name is 64 characters or less
- [ ] Description exists and includes triggers
- [ ] Description is 1024 characters or less
- [ ] Markdown content is well-structured
- [ ] Examples are included
- [ ] Referenced files exist

---

## Detailed Validation Guide

### 1. YAML Frontmatter Structure

#### ✅ Check Opening Delimiter
```yaml
---
```
**Requirements**:
- Must be on line 1 (no blank lines before)
- Exactly three hyphens
- No spaces before or after
- No other content on line 1

**Common Issues**:
- ❌ Blank line before `---`
- ❌ Four hyphens `----`
- ❌ Spaces: `  ---` or `---  `

#### ✅ Check Closing Delimiter
```yaml
---
name: skill-name
description: Description here
---

# Markdown content starts here
```
**Requirements**:
- Exactly three hyphens
- Appears before any Markdown content
- No YAML content after closing delimiter

**Common Issues**:
- ❌ Missing closing delimiter
- ❌ Markdown mixed with YAML
- ❌ Extra delimiters

#### ✅ Check Indentation
**Requirements**:
- Use spaces, never tabs
- Consistent indentation (2 or 4 spaces)
- No mixed spacing

**How to Check**:
```bash
# Search for tabs in YAML
cat SKILL.md | head -20 | grep -P '\t'
```

**Common Issues**:
- ❌ Tabs instead of spaces
- ❌ Inconsistent indentation (2 spaces then 4 spaces)

---

### 2. Required YAML Fields

#### ✅ Name Field

**Format Requirements**:
- Lowercase letters only
- Numbers allowed
- Hyphens allowed for separation
- No spaces, underscores, or special characters
- Maximum 64 characters
- Must be unique within scope (project/personal/plugin)

**Valid Examples**:
```yaml
name: commit-message-generator
name: code-reviewer
name: test-generator-v2
name: pdf-processor
```

**Invalid Examples**:
```yaml
name: Commit_Message_Generator  # uppercase, underscores
name: code reviewer             # spaces
name: test.generator            # periods
name: my-very-long-skill-name-that-exceeds-the-maximum-character-limit  # > 64 chars
```

**Validation Steps**:
1. Check length: `len(name) <= 64`
2. Check format: matches `^[a-z0-9-]+$`
3. Check uniqueness: no other skill with same name in scope

#### ✅ Description Field

**Content Requirements**:
- Explain WHAT the skill does (capabilities)
- Explain WHEN to use it (triggers and context)
- Include specific keywords users would mention
- Maximum 1024 characters
- Clear and concise language

**Structure Pattern**:
```
[What it does]. Use when [triggers/contexts] or when user mentions [keywords].
```

**Good Examples**:
```yaml
description: Generates clear commit messages from git diffs. Use when writing commits or reviewing staged changes, or when user mentions "commit message" or "git commit".

description: Reviews code for best practices and security. Use when checking PRs, analyzing code quality, or when user mentions "code review" or "review PR".

description: Extract text and tables from PDF files. Use when working with PDFs or when user mentions "PDF extraction" or "read PDF".
```

**Poor Examples**:
```yaml
description: Helps with commits  # Too vague, no triggers

description: A skill for code    # Incomplete, no when/triggers

description: [2000 character description...]  # Too long (> 1024)

description: Does stuff          # Not specific enough
```

**Validation Steps**:
1. Check length: `len(description) <= 1024`
2. Check includes capabilities (what)
3. Check includes trigger keywords (when)
4. Check for specific user-facing terms
5. Check clarity (would Claude know when to use it?)

#### ✅ Allowed-Tools Field (Optional)

**When to Use**:
- Read-only operations (code review, analysis)
- Security-sensitive workflows
- Preventing accidental modifications

**Valid Tools**:
- `Read` - Reading files
- `Grep` - Searching content
- `Glob` - Finding files by pattern
- `Bash` - Running commands
- `Edit` - Editing files
- `Write` - Writing files
- Any other available Claude Code tool

**Format**:
```yaml
allowed-tools: Read, Grep, Glob
```

**Requirements**:
- Comma-separated list
- Correct tool names (case-sensitive)
- No trailing comma

**Common Issues**:
- ❌ `allowed-tools: Read Grep Glob` (missing commas)
- ❌ `allowed-tools: Read, Grep, Glob,` (trailing comma)
- ❌ `allowed-tools: read, grep` (wrong case)

---

### 3. Markdown Content Validation

#### ✅ Structure and Headers

**Recommended Structure**:
```markdown
# Skill Title

Brief description of purpose.

## Instructions

Step-by-step guidance.

## Examples

Concrete examples.

## Additional Sections (Optional)
- Configuration
- Dependencies
- Troubleshooting
- Best Practices
```

**Validation Steps**:
1. Has H1 title (`# Title`)
2. Has Instructions section
3. Has Examples section
4. Logical flow and organization
5. No broken header hierarchy (H1 → H3 skip)

#### ✅ Instructions Quality

**Good Instructions**:
- Clear action verbs (Read, Search, Generate, etc.)
- Numbered steps when sequential
- Specific tool usage (Use Read tool, Run Bash command)
- Decision points when needed
- Success criteria

**Poor Instructions**:
- Vague descriptions
- No clear steps
- Missing tool references
- Ambiguous flow

**Example - Good**:
```markdown
## Instructions

1. **Read the target file**: Use Read tool to examine contents
2. **Search for patterns**: Use Grep to find specific code
3. **Analyze findings**: Check against criteria
4. **Report results**: Structure feedback with file:line references
```

**Example - Poor**:
```markdown
## Instructions

Look at the code and find issues. Then tell the user.
```

#### ✅ Examples Quality

**Good Examples**:
- Concrete and specific
- Show input and output
- Cover common scenarios
- Include code blocks with syntax highlighting
- Demonstrate key features

**Poor Examples**:
- Abstract or generic
- Missing context
- No clear demonstration
- Too simple or too complex

**Example - Good**:
```markdown
## Examples

Example 1: Generate test for add function
```javascript
describe('add', () => {
  test('should add two numbers', () => {
    expect(add(2, 3)).toBe(5)
  })
})
```
```

**Example - Poor**:
```markdown
## Examples

Example: Use the skill to do the thing.
```

---

### 4. File References Validation

#### ✅ Supporting Files

**If Skill References Files**:
```markdown
See [examples.md](examples.md) for more examples.
Use scripts in `scripts/` directory.
```

**Validation Steps**:
1. Verify referenced files exist
2. Check paths use forward slashes
3. Verify relative paths are correct
4. Test that links work

**Commands**:
```bash
# Check if referenced files exist
ls .claude/skills/skill-name/examples.md
ls .claude/skills/skill-name/scripts/
```

#### ✅ Path Format

**Requirements**:
- Always use forward slashes: `scripts/helper.py`
- Never backslashes: `scripts\helper.py`
- Use relative paths from SKILL.md location
- No absolute paths unless necessary

**Valid Examples**:
```markdown
[examples.md](examples.md)
scripts/helper.py
templates/config.json
../shared/utils.md
```

**Invalid Examples**:
```markdown
scripts\helper.py                              # backslash
C:/absolute/path/file.md                       # absolute path
/home/user/.claude/skills/skill-name/file.md   # absolute path
```

---

### 5. Dependencies and Requirements

#### ✅ External Dependencies

**If Skill Requires External Tools**:
- List all dependencies clearly
- Provide installation instructions
- Specify versions if critical
- Include verification commands

**Example**:
```markdown
## Dependencies

This skill requires:
- **Python 3.8+**: `python --version`
- **PyPDF2**: `pip install PyPDF2`
- **pdfplumber**: `pip install pdfplumber`

Verify installation:
```bash
python -c "import PyPDF2; import pdfplumber"
```
```

#### ✅ Pre-flight Checks

**Good Practice**:
```markdown
## Pre-flight Check

Before using this skill:
1. Verify dependencies: [commands]
2. Check permissions: [requirements]
3. Ensure environment: [variables]
```

---

### 6. Testing and Validation

#### ✅ Functional Testing

**Steps**:
1. **Restart Claude Code**: Reload skill changes
   ```bash
   # Restart the Claude Code process
   ```

2. **Test Invocation**: Ask questions matching the description
   ```
   User: "Generate a commit message for my changes"
   User: "Review this code for issues"
   User: "Create tests for this function"
   ```

3. **Verify Behavior**:
   - Skill is invoked correctly
   - Instructions are followed
   - Output matches expectations
   - Tools are used appropriately

4. **Test Edge Cases**:
   - Missing files
   - Invalid inputs
   - Error conditions
   - Unusual requests

#### ✅ Description Testing

**Test If Description Is Effective**:
1. Ask question with exact trigger keywords
2. Ask question with synonyms/variations
3. Ask similar question without keywords
4. Check if skill is invoked appropriately

**Example**:
```
Skill: commit-message-generator
Description includes: "commit message", "git commit"

Test 1: "Generate a commit message" → Should invoke ✓
Test 2: "Write a git commit" → Should invoke ✓
Test 3: "Create commit text" → Should invoke ✓
Test 4: "Help me with git" → May not invoke (too vague)
```

---

### 7. Best Practices Validation

#### ✅ Skill Focus

**Single Responsibility**:
- ✅ Skill does one thing well
- ❌ Skill tries to do everything

**Examples**:
- ✅ `commit-message-generator` - Focused on commit messages
- ✅ `code-reviewer` - Focused on code review
- ❌ `git-helper` - Too broad (commits, branches, merges, etc.)
- ❌ `developer-assistant` - Way too broad

#### ✅ Description Specificity

**Specific vs Generic**:
- ✅ "Extract text from PDF files using pdfplumber"
- ❌ "Work with documents"

**Trigger Clarity**:
- ✅ "Use when user mentions 'commit message' or 'git commit'"
- ❌ "Use when helping with git"

#### ✅ Tool Usage Appropriateness

**Read-Only Skills**:
```yaml
allowed-tools: Read, Grep, Glob
```
For: Analysis, review, search, information gathering

**Write Skills**:
No `allowed-tools` restriction
For: Generating files, modifying code, creating content

**Interactive Skills**:
No `allowed-tools` restriction
For: Workflows, guided processes, user decisions

---

### 8. Common Issues and Fixes

#### Issue: Skill Not Invoked

**Possible Causes**:
1. Description doesn't match user's language
2. Missing trigger keywords
3. Description too vague
4. Competing skill with better match
5. Haven't restarted Claude Code

**Fixes**:
1. Add more specific trigger keywords
2. Include natural user phrases
3. Make description more specific
4. Differentiate from similar skills
5. Restart Claude Code

#### Issue: YAML Parse Error

**Possible Causes**:
1. Tabs instead of spaces
2. Missing closing `---`
3. Special characters not quoted
4. Incorrect indentation

**Fixes**:
1. Replace tabs with spaces
2. Add closing `---` delimiter
3. Quote strings with special chars
4. Fix indentation consistency

#### Issue: Wrong Tool Usage

**Possible Causes**:
1. `allowed-tools` too restrictive
2. Instructions unclear about tool usage
3. Skill needs tool not in allowed list

**Fixes**:
1. Expand allowed-tools list
2. Specify exact tools in instructions
3. Remove allowed-tools if needed

#### Issue: Skill Conflicts

**Possible Causes**:
1. Multiple skills with similar descriptions
2. Overlapping trigger keywords
3. Non-specific descriptions

**Fixes**:
1. Make each skill more specific
2. Use domain-specific language
3. Narrow skill scope

**Example**:
```yaml
# Too similar
name: doc-helper
description: Help with documents

name: file-processor
description: Process files

# Better - specific and distinct
name: pdf-extractor
description: Extract text from PDF files. Use when working with PDFs or extracting text.

name: markdown-formatter
description: Format Markdown documentation. Use when editing MD files or formatting docs.
```

---

## Complete Validation Workflow

### Step-by-Step Validation Process

1. **Read the SKILL.md file**
   ```bash
   cat .claude/skills/skill-name/SKILL.md
   ```

2. **Check YAML Structure**
   - Line 1 is `---`
   - Closing `---` exists
   - No tabs (only spaces)

3. **Validate Required Fields**
   - `name`: lowercase-hyphenated, ≤64 chars
   - `description`: clear, with triggers, ≤1024 chars
   - `allowed-tools` (if present): correct format

4. **Review Markdown Content**
   - Has Instructions section
   - Has Examples section
   - Clear and actionable
   - Well-structured

5. **Verify File References**
   - All referenced files exist
   - Paths use forward slashes
   - Links work correctly

6. **Check Dependencies**
   - Listed clearly
   - Installation instructions provided
   - Versions specified if needed

7. **Test Functionality**
   - Restart Claude Code
   - Ask questions matching description
   - Verify skill is invoked
   - Check behavior is correct

8. **Validate Best Practices**
   - Single responsibility
   - Specific description
   - Appropriate tool usage
   - No conflicts with other skills

---

## Validation Report Template

Use this template when validating a skill:

```markdown
## Skill Validation Report

**Skill Name**: [skill-name]
**Validation Date**: [date]
**Validator**: [name]

### YAML Frontmatter
- [ ] Opening delimiter on line 1
- [ ] Closing delimiter present
- [ ] No tabs in YAML
- [ ] Name format valid (lowercase-hyphenated)
- [ ] Name length ≤ 64 characters
- [ ] Description includes capabilities
- [ ] Description includes triggers
- [ ] Description length ≤ 1024 characters
- [ ] allowed-tools format correct (if present)

### Markdown Content
- [ ] Has H1 title
- [ ] Has Instructions section
- [ ] Has Examples section
- [ ] Instructions are clear and actionable
- [ ] Examples are concrete and useful
- [ ] Well-structured and organized

### File References
- [ ] All referenced files exist
- [ ] Paths use forward slashes
- [ ] Relative paths are correct
- [ ] Links work

### Dependencies
- [ ] All dependencies listed
- [ ] Installation instructions provided
- [ ] Versions specified (if critical)
- [ ] Verification commands included

### Functional Testing
- [ ] Skill invoked with trigger keywords
- [ ] Skill invoked with variations
- [ ] Behavior matches expectations
- [ ] Edge cases handled

### Best Practices
- [ ] Single, focused responsibility
- [ ] Specific, clear description
- [ ] Appropriate tool restrictions
- [ ] No conflicts with other skills

### Issues Found
[List any issues discovered]

### Recommendations
[Suggestions for improvement]

### Overall Assessment
[Pass/Fail with summary]
```

---

## Quick Reference Commands

```bash
# Check for tabs in YAML
grep -P '\t' .claude/skills/skill-name/SKILL.md | head -20

# Validate YAML syntax (requires yq)
yq eval '.claude/skills/skill-name/SKILL.md' 2>&1 | head

# Check name length
grep "^name:" .claude/skills/skill-name/SKILL.md | wc -c

# Check description length
grep "^description:" .claude/skills/skill-name/SKILL.md | wc -c

# Find all referenced files
grep -oP '\[.*?\]\(\K[^)]+' .claude/skills/skill-name/SKILL.md

# List all skills
ls -la .claude/skills/

# View skill structure
tree .claude/skills/skill-name/
```

---

## Summary

A well-validated skill should:

1. ✅ Have perfect YAML syntax (no tabs, proper delimiters)
2. ✅ Meet all name and description requirements
3. ✅ Include clear instructions and examples
4. ✅ Reference only existing files
5. ✅ Document all dependencies
6. ✅ Be invoked correctly when tested
7. ✅ Follow best practices (focus, specificity, appropriate tools)
8. ✅ Not conflict with other skills

Use this checklist every time you create or modify a skill to ensure quality and functionality.
