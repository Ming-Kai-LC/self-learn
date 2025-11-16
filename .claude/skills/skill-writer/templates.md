# Skill Templates

Ready-to-use templates for common skill patterns. Copy and customize based on your needs.

## Template 1: Minimal Single-File Skill

**Use when**: Creating a simple, focused skill with straightforward instructions.

```markdown
---
name: your-skill-name
description: Brief description of what it does and when to use it. Include trigger keywords like "generate", "analyze", "create", or specific terms users would mention.
---

# Your Skill Title

Brief explanation of the skill's purpose.

## Instructions

1. First step - what Claude should do first
2. Second step - next action
3. Third step - final action

## Examples

Example 1: Common use case
Example 2: Edge case
```

**Customization Notes**:
- Replace `your-skill-name` with lowercase-hyphenated name
- Fill description with specific capabilities and trigger words
- Keep instructions concise and actionable
- Provide at least 2 examples

---

## Template 2: Multi-File Skill with Supporting Documentation

**Use when**: Creating a complex skill that needs reference documentation, examples, or templates.

```markdown
---
name: complex-skill-name
description: Comprehensive description including what it does, when to use it, and specific keywords users would mention.
---

# Complex Skill Title

## Overview

Explain the skill's purpose and key capabilities.

## Instructions

### Step 1: Initial Setup
Detailed instructions for the first phase.

### Step 2: Main Processing
Core workflow steps.

### Step 3: Finalization
Wrap-up actions.

## Quick Reference

- Key point 1
- Key point 2
- Key point 3

## Examples

See [examples.md](examples.md) for detailed examples.

## Additional Resources

See [reference.md](reference.md) for technical details.
```

**File Structure**:
```
complex-skill-name/
├── SKILL.md (this file)
├── examples.md (detailed examples)
├── reference.md (technical documentation)
└── templates/
    └── template-file.txt (reusable template)
```

**Customization Notes**:
- Break complex workflows into subsections
- Reference supporting files using relative links
- Use forward slashes in all paths
- Create supporting files for better organization

---

## Template 3: Read-Only Analysis Skill

**Use when**: Creating a skill that should only read and analyze code, not modify it.

```markdown
---
name: code-analysis-skill
description: Analyzes code for [specific aspect]. Use when checking code quality, reviewing PRs, or when user mentions [specific keywords].
allowed-tools: Read, Grep, Glob
---

# Code Analysis Skill

This skill analyzes code for [specific purpose] without making modifications.

## Analysis Steps

1. **Identify Target Files**: Use Glob to find relevant files
2. **Search for Patterns**: Use Grep to find specific patterns
3. **Read File Contents**: Use Read to examine code
4. **Analyze**: Review findings against criteria
5. **Report Results**: Provide structured feedback

## Analysis Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Output Format

Provide analysis in this structure:
- **Files Analyzed**: List of files
- **Findings**: Issues or observations
- **Recommendations**: Suggested improvements
- **Summary**: Overall assessment

## Examples

Example 1: Analyzing error handling
Example 2: Checking code complexity
```

**Customization Notes**:
- `allowed-tools: Read, Grep, Glob` restricts to read-only operations
- Focus on analysis and reporting, not modification
- Use checklist format for systematic review
- Provide structured output format

---

## Template 4: Generator Skill

**Use when**: Creating a skill that generates new files or code.

```markdown
---
name: file-generator-skill
description: Generates [type of files] based on [inputs]. Use when creating new [files/code/docs] or when user mentions [keywords].
---

# File Generator

Generates [type of content] following best practices and conventions.

## Generation Process

1. **Gather Requirements**: Ask user for necessary inputs
   - Input 1: [description]
   - Input 2: [description]
   - Input 3: [description]

2. **Validate Inputs**: Ensure all required information is provided

3. **Generate Content**: Create file with proper structure

4. **Confirm Location**: Verify target directory exists

5. **Write File**: Use Write tool to create the file

## Template Structure

```
[Show the template structure here]
```

## Configuration Options

- Option 1: [description and when to use]
- Option 2: [description and when to use]
- Option 3: [description and when to use]

## Examples

Example 1: Basic generation
Example 2: Advanced generation with options
```

**Customization Notes**:
- Include clear template structure
- Validate inputs before generation
- Provide configuration options
- Use Write tool for file creation

---

## Template 5: Workflow Orchestration Skill

**Use when**: Creating a skill that coordinates multiple steps or checks.

```markdown
---
name: workflow-skill
description: Orchestrates [workflow name] with multiple steps and validations. Use when [context] or when user mentions [keywords].
---

# Workflow Skill

Coordinates a multi-step workflow for [purpose].

## Workflow Overview

```
Step 1: [Name] → Step 2: [Name] → Step 3: [Name] → Complete
```

## Workflow Steps

### Step 1: [Name]
**Purpose**: [What this step achieves]
**Actions**:
1. Action 1
2. Action 2
3. Action 3

**Success Criteria**: [How to know it's complete]

### Step 2: [Name]
**Purpose**: [What this step achieves]
**Actions**:
1. Action 1
2. Action 2
3. Action 3

**Success Criteria**: [How to know it's complete]

### Step 3: [Name]
**Purpose**: [What this step achieves]
**Actions**:
1. Action 1
2. Action 2
3. Action 3

**Success Criteria**: [How to know it's complete]

## Error Handling

If any step fails:
1. Identify the failing step
2. Report the specific error
3. Suggest corrective actions
4. Resume from failed step after correction

## Progress Tracking

Use TodoWrite to track workflow progress:
- [ ] Step 1: [Name]
- [ ] Step 2: [Name]
- [ ] Step 3: [Name]

## Examples

Example 1: Complete workflow execution
Example 2: Handling errors mid-workflow
```

**Customization Notes**:
- Define clear success criteria for each step
- Include error handling strategy
- Use TodoWrite for progress tracking
- Show workflow diagram for clarity

---

## Template 6: Interactive Question-Based Skill

**Use when**: Creating a skill that guides users through decisions.

```markdown
---
name: interactive-skill
description: Guides users through [process] with interactive questions. Use when helping users [task] or when user mentions [keywords].
---

# Interactive Skill

Guides users through [process] with step-by-step questions.

## Question Flow

### Question 1: [Topic]
**Purpose**: Determine [what]

Use AskUserQuestion tool:
- Option A: [Description]
- Option B: [Description]
- Option C: [Description]

**Next Step**: Based on answer, proceed to [appropriate next question]

### Question 2: [Topic]
**Purpose**: Determine [what]

Use AskUserQuestion tool:
- Option A: [Description]
- Option B: [Description]

**Next Step**: [What to do with answer]

### Question 3: [Topic]
**Purpose**: Finalize [what]

Use AskUserQuestion tool:
- Option A: [Description]
- Option B: [Description]

**Next Step**: Generate final output

## Decision Tree

```
Question 1
├── Option A → Question 2A → Result A
├── Option B → Question 2B → Result B
└── Option C → Question 2C → Result C
```

## Output Generation

Based on collected answers:
1. Validate all inputs
2. Apply selected options
3. Generate output
4. Present to user for confirmation

## Examples

Example 1: Full question flow
Example 2: Branching based on answers
```

**Customization Notes**:
- Use AskUserQuestion tool for gathering input
- Design logical question flow
- Handle different paths based on answers
- Show decision tree for clarity

---

## Template 7: Advanced Skill with Dependencies

**Use when**: Creating a skill that requires external tools or libraries.

```markdown
---
name: advanced-skill
description: [Description with capabilities and triggers]
---

# Advanced Skill

Uses [external tools/libraries] to [purpose].

## Dependencies

This skill requires:
- **Tool/Library 1**: `npm install package-name` or `pip install package-name`
- **Tool/Library 2**: [Installation instructions]
- **Tool/Library 3**: [Installation instructions]

## Pre-flight Check

Before running this skill, verify:
1. All dependencies are installed
2. Required environment variables are set
3. Necessary permissions are available

## Usage Instructions

### Step 1: Verify Dependencies
```bash
# Check if dependencies are available
[command to verify]
```

### Step 2: Execute Main Task
[Detailed instructions using the dependencies]

### Step 3: Handle Output
[What to do with results]

## Script Files

This skill includes helper scripts in `scripts/`:
- `scripts/helper.py`: [Description]
- `scripts/validator.js`: [Description]

Reference scripts using relative paths: `scripts/helper.py`

## Configuration

Optional configuration in [config file]:
```
[configuration example]
```

## Troubleshooting

**Issue**: Dependency not found
**Solution**: Run installation command

**Issue**: Permission denied
**Solution**: Check file permissions

## Examples

Example 1: Basic usage with all dependencies
Example 2: Handling missing dependencies
```

**File Structure**:
```
advanced-skill/
├── SKILL.md
├── scripts/
│   ├── helper.py
│   └── validator.js
└── templates/
    └── config-template.json
```

**Customization Notes**:
- List all dependencies with installation instructions
- Include pre-flight checks
- Provide troubleshooting guidance
- Organize scripts in `scripts/` directory

---

## Template Selection Guide

| Use Case | Recommended Template |
|----------|---------------------|
| Simple single-purpose task | Template 1: Minimal Single-File |
| Complex multi-step process | Template 2: Multi-File |
| Code review/analysis | Template 3: Read-Only Analysis |
| Creating new files/code | Template 4: Generator |
| Multi-step workflow | Template 5: Workflow Orchestration |
| User decision guidance | Template 6: Interactive |
| External tools needed | Template 7: Advanced with Dependencies |

## Quick Start

1. Copy the appropriate template
2. Replace placeholders with your specifics
3. Customize the description with trigger keywords
4. Add concrete examples
5. Test by asking questions matching your description
6. Refine based on testing
