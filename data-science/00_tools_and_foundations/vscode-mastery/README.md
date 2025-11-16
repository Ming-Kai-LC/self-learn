# VS Code Mastery: From Beginner to Power User

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)
![VS Code](https://img.shields.io/badge/VS%20Code-1.80+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A comprehensive, hands-on learning project designed to transform you from a VS Code beginner into a productive power user through interactive Jupyter notebooks and practical exercises.

## Overview

Visual Studio Code has become one of the most popular code editors in the world, but most users only scratch the surface of its capabilities. This project provides a structured learning path that covers everything from basic navigation to advanced productivity features, debugging, and workspace customization.

**What makes this project unique:**
- Interactive learning through Jupyter notebooks
- Hands-on exercises with a dedicated practice workspace
- Real-world examples and workflows
- Progressive difficulty with clear learning objectives
- Comprehensive coverage of essential VS Code features

## Features

- **10 Progressive Modules**: Structured learning path from setup to advanced features
- **Interactive Exercises**: Practice directly in Jupyter notebooks with immediate feedback
- **Sample Workspace**: Ready-to-use practice files for hands-on learning
- **Utility Scripts**: Helper tools for managing settings and extensions
- **Quick Reference Guides**: Keyboard shortcuts and extension recommendations
- **Beginner-Friendly**: No prior VS Code experience required
- **Multi-Language Focus**: Python, JavaScript, and general development workflows

## Project Structure

```
vscode-mastery/
├── README.md                           # This file
├── PROJECT_STRUCTURE.md                # Detailed directory guide
├── requirements.txt                    # Python dependencies
├── notebooks/                          # Learning modules
│   ├── README.md                      # Module navigation guide
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
│   └── outputs/                       # Generated files, screenshots
├── sample_workspace/                   # Practice files
│   ├── python_examples/               # Python practice projects
│   ├── web_examples/                  # HTML/CSS/JS examples
│   └── sample_configs/                # Example configuration files
├── scripts/                           # Utility tools
│   ├── settings_generator.py          # Generate common settings.json
│   └── extension_recommender.py       # Extension management
└── docs/                              # Reference documentation
    ├── KEYBOARD_SHORTCUTS_REFERENCE.md
    └── EXTENSION_GUIDE.md
```

## Installation

### Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **VS Code 1.80 or higher** - [Download VS Code](https://code.visualstudio.com/)
- **Git** (recommended) - [Download Git](https://git-scm.com/downloads)
- **Basic command line knowledge**

### Setup Instructions

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd python-projects-portfolio/projects/vscode-mastery
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

5. **Open your browser** and navigate to `http://localhost:8888`

6. **Start with Module 00** (`notebooks/00_setup_and_introduction.ipynb`)

## Getting Started

### Recommended Learning Path

Work through the notebooks sequentially for the best learning experience:

1. **Start Here**: Module 00 - Setup and Introduction
2. **Build Foundation**: Modules 01-02 (Interface, Core Editing)
3. **Extend Your Editor**: Modules 03-04 (Extensions, Python Setup)
4. **Master Development**: Modules 05-06 (Debugging, Git)
5. **Boost Productivity**: Modules 07-09 (Shortcuts, Customization, Workflow)

### Study Tips

- **Take Your Time**: Each module takes 30-60 minutes to complete
- **Practice Actively**: Complete all exercises in the sample workspace
- **Customize**: Adapt settings and shortcuts to your preferences
- **Experiment**: Try features in your own projects
- **Revisit**: Use reference guides for quick lookups

## Learning Modules

| Module | Topic | Focus Areas | Duration |
|--------|-------|-------------|----------|
| 00 | Setup and Introduction | Installation, first steps, basic concepts | 30 min |
| 01 | Interface and Navigation | Command Palette, Explorer, Search, panels | 45 min |
| 02 | Core Editing Features | Multi-cursor, selections, find/replace, IntelliSense | 60 min |
| 03 | Extensions Ecosystem | Marketplace, essential extensions, management | 45 min |
| 04 | Python Development | Python setup, linting, formatting, running code | 60 min |
| 05 | Debugging Basics | Breakpoints, debug console, watch expressions | 60 min |
| 06 | Git Integration | Source control panel, commits, branches, merging | 45 min |
| 07 | Productivity Shortcuts | Keyboard shortcuts, snippets, Emmet | 45 min |
| 08 | Workspace Customization | Settings, themes, layouts, keybindings | 45 min |
| 09 | Real-World Workflow | Projects, tasks, integrated terminal, tips | 60 min |

**Total Learning Time**: ~8 hours

## What You'll Learn

### Core Skills
- Navigate VS Code efficiently with keyboard shortcuts
- Master multi-cursor editing and advanced selections
- Configure and manage extensions for your workflow
- Set up Python development environment with linting and formatting
- Debug Python applications with breakpoints and step execution
- Use integrated Git features for version control
- Customize settings, themes, and keybindings
- Create and use code snippets for common patterns
- Organize workspaces and manage multiple projects

### Advanced Techniques
- Build custom tasks and launch configurations
- Use workspace-specific settings effectively
- Leverage the integrated terminal for development workflows
- Create productivity shortcuts for repetitive tasks
- Optimize VS Code performance and appearance
- Integrate external tools and command-line utilities

## Real-World Applications

This project prepares you for:
- **Python Development**: Data science, web development, automation
- **Web Development**: HTML, CSS, JavaScript projects
- **DevOps**: Configuration management, scripting, CI/CD
- **Data Analysis**: Jupyter notebooks, data visualization
- **General Programming**: Any language supported by VS Code
- **Team Collaboration**: Git workflows, code reviews, pair programming

## Technical Details

### Technologies Covered
- **Editor**: Visual Studio Code
- **Languages**: Python, JavaScript, HTML/CSS
- **Tools**: Git, Integrated Terminal, Task Runner
- **Extensions**: Python, Jupyter, GitLens, and more
- **Formats**: JSON (settings), Markdown (documentation)

### Learning Approach
- **Theory**: Markdown cells explain concepts clearly
- **Demonstration**: Code examples show features in action
- **Practice**: Hands-on exercises in sample workspace
- **Reference**: Quick guides for keyboard shortcuts and settings
- **Real-World**: Practical workflows and use cases

## Troubleshooting

### Common Issues

**Jupyter notebook won't start**
- Ensure virtual environment is activated
- Verify Jupyter is installed: `pip list | grep jupyter`
- Try reinstalling: `pip install --upgrade jupyter`

**VS Code extensions not working**
- Check VS Code version (must be 1.80+)
- Reload window: Ctrl+Shift+P → "Reload Window"
- Check extension compatibility in Extensions panel

**Python IntelliSense not working**
- Install Python extension in VS Code
- Select correct Python interpreter
- Check Pylance language server status

**Keyboard shortcuts not working**
- Check for keybinding conflicts
- Review shortcuts in docs/KEYBOARD_SHORTCUTS_REFERENCE.md
- Customize shortcuts to avoid system conflicts

## Additional Resources

### Official Documentation
- [VS Code Documentation](https://code.visualstudio.com/docs)
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Keyboard Shortcuts Reference](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

### Extension Recommendations
- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

### Community
- [VS Code GitHub](https://github.com/microsoft/vscode)
- [Stack Overflow - VS Code Tag](https://stackoverflow.com/questions/tagged/visual-studio-code)
- [VS Code Reddit](https://www.reddit.com/r/vscode/)

## Future Enhancements

Planned additions to this project:
- Advanced debugging scenarios (remote debugging, Docker)
- Extension development tutorial
- Workspace configuration templates for different languages
- Advanced Git workflows (rebasing, stashing, cherry-picking)
- Remote development (SSH, WSL, containers)
- Live Share collaboration features
- Performance optimization techniques
- Advanced search with regex patterns
- Custom task automation examples
- Integration with cloud services

## Contributing

Contributions are welcome! If you have:
- Bug fixes or improvements
- Additional exercises or examples
- New module suggestions
- Documentation enhancements

Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- VS Code team at Microsoft for creating an amazing editor
- The open-source community for extensions and documentation
- Contributors to this learning project

---

**Ready to become a VS Code power user?** Start with `notebooks/00_setup_and_introduction.ipynb` and begin your journey!

**Questions or feedback?** Open an issue or reach out to the maintainers.

**Happy Coding!**
