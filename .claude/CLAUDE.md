# Educational Notebook Portfolio - Project Instructions

## Project Overview

This is a comprehensive portfolio of educational Jupyter notebooks covering multiple domains: technical analysis, data science, language learning, image processing, automation, and more. All notebooks follow consistent quality standards and pedagogical best practices.

## Sub-Agent Orchestration System

### Available Sub-Agents

This project uses specialized sub-agents for educational notebook creation. Located in `.claude/agents/`:

1. **content-generator**: Creates notebook cells, explanations, and exercises
2. **code-reviewer**: Enforces quality standards and educational best practices
3. **notebook-tester**: Validates execution and checks quality metrics
4. **documentation-writer**: Creates README files, glossaries, and learning paths

### Using Sub-Agents

Delegate tasks to appropriate sub-agents using the Task tool:

```markdown
Use content-generator for:
- Creating new notebook modules
- Generating exercises and solutions
- Writing educational explanations

Use code-reviewer for:
- Checking code quality
- Validating educational appropriateness
- Ensuring PEP 8 compliance with educational exceptions

Use notebook-tester for:
- Executing notebooks to verify they run
- Checking quality metrics (markdown ratio, exercise count)
- Validating learning objectives and prerequisites

Use documentation-writer for:
- Creating project README files
- Writing FAQ and glossary documents
- Generating learning path guides
```

### Output Styles for Different Contexts

Switch output styles based on the teaching context:

- **notebook-educator-verbose**: For beginner-level content (A1, A2, ⭐)
  - Extensive comments and explanations
  - Step-by-step guidance
  - Encouraging tone

- **notebook-educator-concise**: For advanced content (B2+, ⭐⭐⭐)
  - Methodology and trade-offs focus
  - Assumes foundational knowledge
  - Professional, efficient tone

- **notebook-orchestrator**: For planning and coordination
  - Strategic thinking about learning progressions
  - Delegation to sub-agents
  - Quality assurance oversight

## Notebook Quality Standards

### Structural Requirements

**Every educational notebook MUST have**:

1. **Metadata Cell** (first markdown cell):
   ```markdown
   # Module XX: Topic Name

   **Difficulty**: ⭐/⭐⭐/⭐⭐⭐
   **Estimated Time**: XX minutes
   **Prerequisites**: [Links to previous modules]

   ## Learning Objectives
   By the end of this notebook, you will be able to:
   1. [Specific objective]
   2. [Specific objective]
   3. [Specific objective]
   ```

2. **Setup Section**:
   - All imports in one cell
   - Configuration (`%matplotlib inline`, random seeds)
   - Helper function definitions

3. **Content Sections**:
   - Concept introduction (markdown)
   - Code demonstration
   - Explanation of results
   - At least 3 exercises per major concept

4. **Summary Section**:
   - Key concepts recap
   - What's next preview
   - Additional resources

### Quality Metrics

**Minimum Standards** (enforced by automated testing):

- ✅ **Markdown Ratio**: ≥30% of content (by character count)
- ✅ **Exercise Count**: ≥3 exercises per major concept
- ✅ **Execution**: "Restart and Run All" must pass without errors
- ✅ **Cell Length**: Code cells ≤15 lines (for readability)
- ✅ **Learning Objectives**: Clearly stated and measurable
- ✅ **Prerequisites**: Explicitly documented

### Code Quality Standards

**Educational code should**:

- Use descriptive variable names (never `df2`, `x`, `temp`)
- Include comments explaining WHY, not WHAT
- Show intermediate results (print statements, head() calls)
- Handle errors gracefully with helpful messages
- Follow PEP 8 with educational exceptions:
  - Line length: 100 characters (vs strict 79)
  - Allow longer lines when clarity demands it
  - Comments can exceed line limits

**Example of Good Educational Code**:

```python
# Load sales data for analysis
# Using relative path so notebook works on any computer
sales_data = pd.read_csv('data/sample/sales.csv')

# Validate that data loaded correctly
print(f"Loaded {len(sales_data)} rows, {len(sales_data.columns)} columns")
assert len(sales_data) > 0, "Data file is empty! Check the path."

# Display first few rows to understand structure
sales_data.head()
```

**Example of Bad Code** (don't do this):

```python
# Load data
df = pd.read_csv('data/sample/sales.csv')  # Non-descriptive name
df.head()  # No validation or explanation
```

## Skills Available

### Generic Skills (All Projects)

- **notebook-creator**: Structural standards, templates, scaffolding patterns
- **notebook-tester**: Validation scripts, quality metrics, execution testing
- **quality-checker**: Code formatting, linting, style enforcement

### Domain-Specific Skills

- **technical-analysis-educator**: Stock market, trading indicators, Malaysian stocks
- **data-science-educator**: Pandas, ML, visualization, statistical analysis
- **language-learning-educator**: English/ESL, CEFR levels, audio generation

Skills auto-activate based on keywords, or invoke explicitly:

```python
# Auto-activation: mention keywords
"Create a notebook teaching RSI indicator"  # Activates technical-analysis-educator

# Explicit activation via skill name
"Use the data-science-educator skill to explain pandas groupby"
```

## Project Structure

```
self-learn/
├── .claude/
│   ├── agents/              # Sub-agent definitions
│   ├── output-styles/       # Teaching mode configurations
│   ├── skills/              # Domain expertise and patterns
│   ├── templates/           # Project templates
│   ├── scripts/             # Utility scripts
│   ├── CLAUDE.md           # This file (project instructions)
│   └── settings.local.json  # Local configuration
├── data-science/            # Data science topic (12 subcategories)
│   ├── 00_tools_and_foundations/
│   ├── 01_mathematics/
│   ├── 02_data_manipulation/
│   ├── 03_visualization/
│   └── ... (other subcategories)
├── malaysia-stock/          # Stock market technical analysis
│   ├── notebooks/           # Educational notebooks (00-10)
│   ├── data/                # Sample datasets
│   │   ├── raw/             # Original data
│   │   ├── processed/       # Cleaned data
│   │   └── sample/          # Small examples (<10MB)
│   ├── requirements.txt     # Dependencies
│   └── README.md            # Project documentation
├── english/                 # English language learning
├── first-principle/         # First principles thinking
├── research-methodology/    # Research methods and skills
├── earn-money/              # Business and income projects
├── music/                   # Music-related projects
├── n8n/                     # n8n automation workflows
├── .gitignore              # Ignore patterns
├── COMPLETION_PROMPTS.md    # Project completion templates
├── PROJECT_TRACKING.md      # Project status tracking
└── Jupyter-Notebook.md      # Jupyter notebook guidelines
```

**Repository Organization Rule**: The root folder contains only topic-specific folders. Each topic folder contains its own projects, notebooks, data, and documentation.

## File Naming Conventions

### Notebooks

Format: `NN_descriptive_topic_name.ipynb`

Examples:
- `00_setup_introduction.ipynb`
- `01_introduction_to_technical_analysis.ipynb`
- `02_understanding_price_charts.ipynb`
- `10_final_project.ipynb`

### Data Files

- **Raw data**: `data/raw/original_filename.csv` (never modify)
- **Processed**: `data/processed/cleaned_filename.csv`
- **Samples**: `data/sample/small_example.csv` (<10MB for repo inclusion)

### Test Files

- **Tested notebooks**: `notebook_name_tested.ipynb` (gitignored)
- **Test reports**: `tests/test_notebook_name.txt`

## Data Handling Rules

### ALWAYS Use Relative Paths

```python
# ✅ GOOD - Works on any computer
data = pd.read_csv('data/sample/sales.csv')
data = pd.read_csv('../data/sample/sales.csv')  # From notebooks/ directory

# ❌ BAD - Only works on your computer
data = pd.read_csv('D:/Users/USER/Documents/.../sales.csv')
data = pd.read_csv('/home/user/project/data/sales.csv')
```

### Validate Data Loading

```python
from pathlib import Path

# Check file exists before loading
data_file = Path('data/sample/sales.csv')
if not data_file.exists():
    raise FileNotFoundError(
        f"Data file not found: {data_file}\n"
        f"Please ensure the file exists in the data/ directory."
    )

# Load and validate
data = pd.read_csv(data_file)
print(f"Loaded {len(data)} rows, {len(data.columns)} columns")
assert len(data) > 0, "Data file is empty!"
```

### Reproducibility

```python
# ALWAYS set random seeds at notebook start
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# For ML libraries
# import tensorflow as tf
# tf.random.set_seed(42)
# import torch
# torch.manual_seed(42)
```

## Testing and Quality Assurance

### Before Committing a Notebook

Run these checks:

1. **Execution Test**:
   ```bash
   # Restart kernel and run all cells
   jupyter nbconvert --to notebook --execute notebook.ipynb \
       --output tested.ipynb
   ```

2. **Quality Metrics**:
   ```bash
   python .claude/skills/notebook-tester/scripts/calculate_quality.py notebook.ipynb
   ```

3. **Code Quality**:
   ```bash
   nbqa black notebook.ipynb    # Format code
   nbqa isort notebook.ipynb    # Organize imports
   nbqa flake8 notebook.ipynb   # Check style
   ```

### Automated Tests

Pre-commit hooks automatically run before git commits:
- Remove notebook outputs (nbstripout)
- Format code with Black
- Organize imports with isort
- Check style with flake8

## Common Workflows

### Creating a New Notebook

1. **Use orchestrator mode** to plan structure:
   ```
   /output-style notebook-orchestrator
   "Plan a notebook teaching [topic] for [level] learners"
   ```

2. **Delegate to content-generator**:
   ```
   Use Task tool with content-generator sub-agent
   Provide: learning objectives, difficulty level, target concepts
   ```

3. **Review with code-reviewer**:
   ```
   Use Task tool with code-reviewer sub-agent
   Provide: generated notebook path, quality criteria
   ```

4. **Validate with notebook-tester**:
   ```
   Use Task tool with notebook-tester sub-agent
   Provide: notebook path, expected metrics
   ```

### Updating Existing Notebook

1. **Read current notebook** to understand structure
2. **Identify issues** or areas for improvement
3. **Make targeted edits** using Edit or NotebookEdit tool
4. **Re-test** to ensure still executes correctly
5. **Update documentation** if learning objectives changed

### Creating Multi-Level Content

1. **Use orchestrator** to design learning progression
2. **Generate beginner version** with verbose output-style
3. **Generate advanced version** with concise output-style
4. **Ensure progression** is logical between levels
5. **Cross-link** modules with clear prerequisites

## Git Workflow

### What Gets Committed

- ✅ Notebook files WITHOUT outputs (.ipynb)
- ✅ Small sample data (<10MB)
- ✅ Requirements.txt and environment.yml
- ✅ README and documentation
- ✅ Helper scripts
- ✅ Configuration files

### What Gets Ignored

- ❌ Notebook outputs (stripped by nbstripout)
- ❌ `_tested.ipynb` files
- ❌ Large datasets (>10MB)
- ❌ Virtual environments (venv/, env/)
- ❌ `__pycache__/`, `.ipynb_checkpoints/`
- ❌ OS files (`.DS_Store`, `Thumbs.db`)

### Commit Messages

Follow format: `[Project] Action: Description`

Examples:
- `[Malaysia-Stock-TA] Add: Module 08 Advanced Oscillators`
- `[Data-Science] Fix: Correct pandas groupby example in Module 03`
- `[English-Learning] Update: Add audio files to A2 Batch 1`

## Domain-Specific Notes

### Malaysia Stock Technical Analysis

- Stock codes: `XXXX.KL` format (e.g., `1155.KL` for Maybank)
- Use yfinance for data: `yf.download('1155.KL', start='2020-01-01')`
- Currency: Malaysian Ringgit (MYR)
- Trading hours: 9:00 AM - 5:00 PM MYT
- Common stocks for examples: Maybank (1155.KL), Top Glove (5225.KL), CIMB (1023.KL)

### Data Science Projects

- Always split train/test before any transformations (avoid data leakage)
- Check for class imbalance in classification tasks
- Use cross-validation for robust evaluation
- Explain feature engineering choices
- Visualizations must have complete labels (title, axes, legend)

### English Learning

- Follow CEFR levels (A1, A2, B1, B2)
- Include audio for pronunciation (use gTTS or pyttsx3)
- Provide immediate feedback on exercises
- Progress from controlled to free practice
- Address common learner errors explicitly

## Troubleshooting

### Notebook Won't Execute

1. Check imports - are all libraries installed?
2. Check data paths - do files exist?
3. Check for cells that depend on out-of-order execution
4. Try "Restart Kernel and Run All" from Jupyter

### Quality Checks Failing

- **Markdown ratio low**: Add more explanation cells
- **Exercise count low**: Add practice exercises
- **Flake8 errors**: Run `nbqa black` and `nbqa isort` first
- **Execution timeout**: Increase timeout or use smaller sample data

### Git Issues

- **Large files rejected**: Move to data/raw/ and add to .gitignore
- **Merge conflicts in notebooks**: Use nbdime for notebook-aware diff/merge
- **Hooks failing**: Run commands manually to see specific errors

## Best Practices Summary

1. **Always start with learning objectives** - know what students should achieve
2. **Show, don't just tell** - demonstrate with code, explain with comments
3. **Test everything** - run "Restart and Run All" before committing
4. **Use descriptive names** - code should be self-documenting
5. **Provide context** - explain WHY, not just WHAT
6. **Progressive difficulty** - easy → medium → hard exercises
7. **Include validation** - assert statements, expected outputs
8. **Document assumptions** - prerequisites, data requirements
9. **Make it reproducible** - random seeds, relative paths
10. **Keep it accessible** - clear language, proper structure

## Getting Help

- Review relevant skill documentation in `.claude/skills/`
- Check sub-agent guidelines in `.claude/agents/`
- Refer to output-style examples in `.claude/output-styles/`
- Consult project README files for project-specific guidance
- Use the notebook-creator templates as starting points

---

**Remember**: The goal is creating educational content that helps learners progress from novice to expert. Quality, clarity, and pedagogy come first.
