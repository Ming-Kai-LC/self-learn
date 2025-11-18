# Windows - Educational Project

**A comprehensive educational portfolio for learning Windows automation, system administration, and development.**

## Project Overview

This project provides a structured learning path from beginner to advanced Windows user. It covers automation with PowerShell, Python scripting for Windows, system administration, and development tools. It follows the educational notebook standards defined in the repository's CLAUDE.md guidelines.

## Learning Objectives

By completing this educational series, you will:

1. **Master PowerShell scripting** - Cmdlets, pipelines, modules, and automation
2. **Automate Windows tasks** - File management, system monitoring, scheduled tasks
3. **Use Python for Windows** - pywin32, subprocess, automation libraries
4. **Understand Windows system administration** - Registry, services, permissions, networking
5. **Build practical tools** - Scripts for daily tasks, system utilities, monitoring tools

## Project Structure

```
windows/
├── notebooks/           # Educational Jupyter notebooks (numbered 00-10)
│   ├── 00_setup_introduction.ipynb
│   ├── 01_powershell_fundamentals.ipynb
│   ├── 02_python_windows_automation.ipynb
│   ├── 03_file_system_operations.ipynb
│   ├── 04_process_service_management.ipynb
│   ├── 05_registry_system_configuration.ipynb
│   ├── 06_networking_basics.ipynb
│   ├── 07_scheduled_tasks_automation.ipynb
│   ├── 08_windows_security_permissions.ipynb
│   ├── 09_advanced_scripting_techniques.ipynb
│   └── 10_final_automation_project.ipynb
├── data/
│   ├── raw/            # Original data (never modified)
│   ├── processed/      # Cleaned and prepared data
│   └── sample/         # Small example datasets (<10MB for repo)
├── docs/               # Additional documentation and guides
├── tests/              # Notebook validation and testing
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Quick Start

### Prerequisites

- Windows 10/11 or Windows Server 2016+
- Python 3.8 or higher
- PowerShell 5.1 or PowerShell Core 7+
- Basic understanding of Python
- Administrator access (for some lessons)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd /home/user/self-learn/windows
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/WSL:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Start with notebook 00** and progress sequentially

## Windows-Specific Topics Covered

### PowerShell Automation
- Cmdlets and pipelines
- Variables and data types
- Functions and modules
- Error handling
- Remote management

### Python for Windows
- pywin32 library
- subprocess module
- Windows API integration
- COM automation
- WMI (Windows Management Instrumentation)

### System Administration
- User and group management
- Service configuration
- Registry operations
- Event log management
- System monitoring

### File and Directory Operations
- Path manipulation
- File permissions (ACLs)
- Bulk operations
- Symbolic links and junctions
- File system monitoring

### Networking
- Network configuration
- Firewall rules
- Network troubleshooting
- Remote connections
- Port scanning and testing

## Learning Path

### Stage 1: Foundation (Notebooks 00-02)
- Environment setup
- PowerShell basics
- Python Windows integration

### Stage 2: Core Operations (Notebooks 03-05)
- File system management
- Process and service control
- Registry and system configuration

### Stage 3: Advanced Topics (Notebooks 06-08)
- Networking fundamentals
- Task scheduling and automation
- Security and permissions

### Stage 4: Mastery (Notebooks 09-10)
- Advanced scripting techniques
- Final comprehensive project
- Best practices and optimization

## Key Python Libraries

This project uses several Windows-specific Python libraries:

```python
import pywin32          # Windows API access
import subprocess       # Process management
import pathlib          # Modern path operations
import winreg           # Registry operations
import psutil           # System monitoring
import schedule         # Task scheduling
```

## Quality Standards

This project follows strict educational quality standards:

- ✅ **Markdown Ratio**: ≥30% explanatory content
- ✅ **Exercise Count**: ≥3 exercises per major concept
- ✅ **Execution**: All notebooks pass "Restart and Run All"
- ✅ **Code Quality**: PEP 8 compliant with educational exceptions
- ✅ **Learning Objectives**: Clearly stated in each notebook
- ✅ **Prerequisites**: Explicitly documented

## Testing Your Knowledge

Each notebook includes:

1. **Guided Examples** - Step-by-step demonstrations
2. **Practice Exercises** - Apply concepts independently
3. **Challenge Problems** - Test mastery
4. **Self-Assessment** - Validate understanding before progressing

## Additional Resources

### Recommended Reading

- *Learn Windows PowerShell in a Month of Lunches* by Don Jones
- *PowerShell Cookbook* by Lee Holmes
- *Windows Internals* by Mark Russinovich
- *Automate the Boring Stuff with Python* by Al Sweigart

### Online Resources

- [Microsoft PowerShell Documentation](https://docs.microsoft.com/powershell/)
- [Python on Windows FAQ](https://docs.python.org/3/faq/windows.html)
- [Windows Dev Center](https://developer.microsoft.com/windows/)
- [PowerShell Gallery](https://www.powershellgallery.com/)

### Useful Tools

- **PowerShell ISE** - Integrated scripting environment
- **VS Code** - Modern code editor with PowerShell extension
- **Windows Terminal** - Modern terminal application
- **Sysinternals Suite** - Advanced system utilities

## Common Use Cases

This project teaches you to automate common Windows tasks:

- **System Maintenance**: Disk cleanup, log rotation, backup automation
- **User Management**: Bulk user creation, permission assignment
- **Monitoring**: System health checks, performance monitoring, alerting
- **Deployment**: Software installation, configuration management
- **Reporting**: System inventory, audit reports, compliance checks

## Safety and Best Practices

**IMPORTANT**: When working with system automation:

- ✅ Always test scripts in a safe environment first
- ✅ Use version control for all scripts
- ✅ Implement proper error handling
- ✅ Log all important operations
- ✅ Follow principle of least privilege
- ❌ Never run untested scripts with admin privileges
- ❌ Don't disable security features without understanding implications
- ❌ Avoid hardcoding credentials

## Contributing

This is an educational project. Improvements welcome:

1. Enhanced explanations in notebooks
2. Additional exercises with solutions
3. New automation examples
4. Bug fixes or corrections

## Compatibility Notes

- Most scripts work on Windows 10/11
- Some features require administrator privileges
- PowerShell scripts tested on PowerShell 5.1 and 7+
- Python scripts tested on Python 3.8+
- WSL (Windows Subsystem for Linux) examples included where relevant

## Support

For questions or issues:

1. Review notebook comments and markdown explanations
2. Refer to the main project CLAUDE.md for standards
3. Consult Microsoft documentation for Windows-specific features
4. Check PowerShell community forums

---

**Start Date**: 2024
**Target Audience**: Beginners to intermediate learners
**Estimated Completion**: 2-4 months (at 5-10 hours/week)
**Difficulty**: ⭐⭐ (Progressive from ⭐ to ⭐⭐⭐)

**Remember**: "Automation applied to an inefficient operation will magnify the inefficiency." - Bill Gates
