# VS Code Mastery - Project Structure

This document provides a detailed overview of the project's directory organization and file purposes.

## Directory Tree

```
vscode-mastery/
├── README.md                           # Main project documentation
├── PROJECT_STRUCTURE.md                # This file
├── requirements.txt                    # Python package dependencies
│
├── notebooks/                          # Interactive learning modules
│   ├── README.md                      # Module descriptions and learning path
│   ├── 00_setup_and_introduction.ipynb
│   ├── 01_interface_and_navigation.ipynb
│   ├── 02_core_editing_features.ipynb
│   ├── 03_extensions_ecosystem.ipynb
│   ├── 04_python_development.ipynb
│   ├── 05_debugging_basics.ipynb
│   ├── 06_git_integration.ipynb
│   ├── 07_productivity_shortcuts.ipynb
│   ├── 08_workspace_customization.ipynb
│   ├── 09_real_world_workflow.ipynb
│   └── outputs/                       # Generated files from exercises
│       ├── screenshots/               # VS Code screenshots
│       ├── config_examples/           # Example settings files
│       └── practice_files/            # Student-generated files
│
├── sample_workspace/                   # Practice workspace for hands-on exercises
│   ├── python_examples/               # Python practice projects
│   │   ├── hello_world.py            # Basic Python script
│   │   ├── calculator.py             # Simple calculator for debugging
│   │   ├── data_processor.py         # Data manipulation examples
│   │   └── test_module.py            # Practice debugging and testing
│   ├── web_examples/                  # Web development examples
│   │   ├── index.html                # HTML practice file
│   │   ├── styles.css                # CSS styling examples
│   │   └── script.js                 # JavaScript practice
│   └── sample_configs/                # Example configuration files
│       ├── settings.json.example     # VS Code settings examples
│       ├── launch.json.example       # Debug configurations
│       ├── tasks.json.example        # Task automation examples
│       └── keybindings.json.example  # Custom keybindings
│
├── scripts/                           # Utility scripts
│   ├── settings_generator.py          # Generate common settings.json configurations
│   └── extension_recommender.py       # Recommend and manage extensions
│
└── docs/                              # Reference documentation
    ├── KEYBOARD_SHORTCUTS_REFERENCE.md # Comprehensive keyboard shortcuts
    └── EXTENSION_GUIDE.md             # Recommended extensions and usage
```

## Directory Purposes

### Root Level

**README.md**
- Main entry point for the project
- Overview, features, installation instructions
- Learning path and module descriptions
- Troubleshooting and resources

**PROJECT_STRUCTURE.md** (this file)
- Detailed directory organization
- File purposes and relationships
- Navigation guide

**requirements.txt**
- Python package dependencies
- Jupyter notebook requirements
- Development tools

### notebooks/

The core learning content organized as interactive Jupyter notebooks.

**Organization Principles:**
- **Sequential numbering**: `00` through `09` for ordered learning
- **Descriptive names**: Clear indication of module content
- **Progressive difficulty**: Each module builds on previous concepts
- **Self-contained**: Each notebook can be studied independently

**Module Breakdown:**

| Number | Topic | Key Learning Outcomes |
|--------|-------|----------------------|
| 00 | Setup and Introduction | Install VS Code, understand interface basics, learn navigation |
| 01 | Interface and Navigation | Master Command Palette, Explorer, panels, and views |
| 02 | Core Editing Features | Multi-cursor editing, selections, find/replace, IntelliSense |
| 03 | Extensions Ecosystem | Discover, install, and manage extensions |
| 04 | Python Development | Configure Python environment, linting, formatting |
| 05 | Debugging Basics | Set breakpoints, inspect variables, step through code |
| 06 | Git Integration | Source control, commits, branches, merging |
| 07 | Productivity Shortcuts | Essential keyboard shortcuts, snippets, Emmet |
| 08 | Workspace Customization | Settings, themes, keybindings, layouts |
| 09 | Real-World Workflow | Projects, tasks, terminal, workflow optimization |

**notebooks/README.md**
- Detailed module descriptions
- Time estimates for each module
- Prerequisites and dependencies
- Learning objectives

**notebooks/outputs/**
- Generated during notebook exercises
- Screenshots for documentation
- Configuration file examples
- Practice files created by learners
- Gitignored to keep repo clean

### sample_workspace/

A dedicated workspace for hands-on practice with real files.

**python_examples/**
- Python scripts demonstrating various concepts
- Files for debugging exercises
- Code samples for editing practice
- Testing scenarios

**web_examples/**
- HTML files for structure practice
- CSS files for styling exercises
- JavaScript files for debugging
- Multi-file project examples

**sample_configs/**
- Example VS Code configuration files
- Templates for common setups
- Reference implementations
- Starting points for customization

**Purpose**: Provide realistic files to practice VS Code features without risk to actual projects.

### scripts/

Python utilities to enhance the learning experience.

**settings_generator.py**
- Generates common `settings.json` configurations
- Creates language-specific settings
- Builds workspace settings templates
- Explains each setting option

**extension_recommender.py**
- Recommends extensions based on use case
- Generates extension lists
- Helps manage installed extensions
- Provides extension configuration examples

**Purpose**: Automate common setup tasks and provide learning tools.

### docs/

Quick reference documentation for frequent lookup.

**KEYBOARD_SHORTCUTS_REFERENCE.md**
- Comprehensive keyboard shortcut guide
- Organized by category (editing, navigation, debugging, etc.)
- Platform-specific shortcuts (Windows, macOS, Linux)
- Tips for customizing shortcuts

**EXTENSION_GUIDE.md**
- Curated list of recommended extensions
- Extension descriptions and use cases
- Installation and configuration instructions
- Language-specific extension recommendations

**Purpose**: Provide quick reference materials separate from learning modules.

## File Naming Conventions

### Notebooks
- Format: `##_descriptive_name.ipynb`
- Two-digit numbering (00-09)
- Lowercase with underscores
- Descriptive but concise names

### Python Scripts
- Lowercase with underscores: `script_name.py`
- Descriptive function names
- Clear purpose indicated by name

### Configuration Examples
- Match VS Code naming: `settings.json.example`
- `.example` suffix to prevent overwriting real configs
- JSON format for VS Code configurations

### Documentation
- Uppercase with underscores: `REFERENCE_GUIDE.md`
- Markdown format (.md)
- Clear, descriptive titles

## Navigation Tips

### For Beginners
1. Start with `README.md` in the project root
2. Follow installation instructions
3. Read `notebooks/README.md` for module overview
4. Begin with `notebooks/00_setup_and_introduction.ipynb`
5. Work through notebooks sequentially

### For Reference
- **Keyboard shortcuts**: `docs/KEYBOARD_SHORTCUTS_REFERENCE.md`
- **Extension help**: `docs/EXTENSION_GUIDE.md`
- **Practice files**: `sample_workspace/`
- **Configuration examples**: `sample_workspace/sample_configs/`

### For Advanced Users
- Utility scripts in `scripts/` for automation
- Configuration templates in `sample_workspace/sample_configs/`
- Advanced topics in later notebooks (07-09)

## File Relationships

```
README.md
    ├─→ notebooks/README.md (module details)
    │       ├─→ 00_setup_and_introduction.ipynb
    │       ├─→ 01_interface_and_navigation.ipynb
    │       └─→ ... (sequential learning path)
    │
    ├─→ sample_workspace/ (practice files)
    │       ├─→ Used in notebook exercises
    │       └─→ Referenced in examples
    │
    ├─→ scripts/ (utilities)
    │       ├─→ Generate configs for notebooks
    │       └─→ Support learning activities
    │
    └─→ docs/ (references)
            ├─→ Quick lookup during learning
            └─→ Referenced in notebooks
```

## Maintenance Notes

### Adding New Modules
1. Create notebook with next sequential number
2. Update `notebooks/README.md` with module description
3. Add any required sample files to `sample_workspace/`
4. Update main `README.md` module table
5. Test notebook end-to-end

### Updating Documentation
1. Keep `README.md` as primary entry point
2. Update `PROJECT_STRUCTURE.md` when adding directories
3. Maintain reference docs (`docs/`) separately from tutorials
4. Version control all changes

### Managing Sample Files
1. Keep `sample_workspace/` organized by language/purpose
2. Include comments in sample code
3. Ensure examples are beginner-friendly
4. Avoid overly complex scenarios

## Questions?

If you can't find something:
1. Check the main `README.md`
2. Look in `notebooks/README.md` for module-specific info
3. Search `docs/` for reference materials
4. Review this file for directory purposes

---

**Last Updated**: 2025-11-15
**Version**: 1.0
