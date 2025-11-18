# Windows for Data Science Students - Complete Learning Guide

**Last Updated**: November 2024
**Target Audience**: Data Science Students
**Difficulty**: ⭐ to ⭐⭐⭐ (Progressive)

---

## Table of Contents

1. [Why Windows Skills Matter for Data Scientists](#why-windows-skills-matter)
2. [Essential Windows Command Line Tools](#essential-command-line-tools)
3. [PowerShell for Data Science](#powershell-for-data-science)
4. [Windows Subsystem for Linux (WSL2)](#wsl2-setup)
5. [Windows Terminal Configuration](#windows-terminal)
6. [Package Managers](#package-managers)
7. [Automation & Scripting](#automation-scripting)
8. [Environment Management](#environment-management)
9. [Recommended Learning Path](#learning-path)
10. [Practical Projects](#practical-projects)

---

## Why Windows Skills Matter for Data Scientists {#why-windows-skills-matter}

As a data science student, mastering Windows tools will help you:

- **Automate repetitive tasks** - Save hours on data processing workflows
- **Manage environments efficiently** - Handle Python versions, dependencies, virtual environments
- **Integrate with enterprise systems** - Most corporate environments run Windows
- **Boost productivity** - Command line proficiency speeds up daily tasks
- **Deploy solutions** - Package and distribute your data science applications
- **Collaborate effectively** - Work seamlessly with cross-platform teams

### Key Statistics (2024)

- **70%+ of enterprise desktops** run Windows
- **WSL2 adoption** has grown 300% among developers since 2020
- **PowerShell** is the #1 scripting language for Windows automation
- **Windows Terminal** is now the default terminal in Windows 11

---

## Essential Windows Command Line Tools {#essential-command-line-tools}

### 1. Core Command Prompt (CMD) Commands

#### File & Directory Operations
```batch
# Navigation
cd C:\Users\YourName\Projects      # Change directory
dir                                 # List directory contents
dir /s                              # List recursively
tree /F                             # Show directory tree with files

# File operations
copy source.csv destination.csv     # Copy files
xcopy /E /I source_dir dest_dir    # Copy directories
move file.txt new_location\        # Move files
del file.txt                        # Delete file
rename old.csv new.csv              # Rename file

# Create/Remove directories
mkdir new_folder                    # Create directory
rmdir /S /Q old_folder             # Remove directory and contents
```

#### System Information
```batch
systeminfo                          # System details
tasklist                           # Running processes
taskkill /IM python.exe /F         # Kill process
ipconfig /all                      # Network configuration
ping google.com                    # Test connectivity
```

#### Data Science Specific
```batch
# Check Python installation
python --version
where python                       # Find Python location

# Check pip packages
pip list                           # List installed packages
pip freeze > requirements.txt      # Export dependencies

# Environment variables
set PATH                           # View PATH variable
setx VARIABLE_NAME "value"         # Set permanent variable
```

### 2. Modern Command Line Tools for Data Science

#### File Searching & Processing
- **findstr**: Windows version of grep
  ```batch
  findstr /S /I "error" *.log       # Search for "error" in log files
  findstr /R "^[0-9]" data.csv      # Regex search in CSV
  ```

- **more/type**: View file contents
  ```batch
  type data.csv                     # Display file
  more large_file.txt               # Page through file
  ```

#### Batch File Processing
```batch
# Process multiple CSV files
for %f in (*.csv) do python process.py "%f"

# Batch rename files
for %f in (*.txt) do ren "%f" "%f.bak"
```

### 3. Essential Unix-Style Tools for Windows

These tools are available through:
- Git Bash (comes with Git for Windows)
- WSL (Windows Subsystem for Linux)
- Cygwin
- GnuWin32

**Recommended for Data Science:**
- `grep`: Search text patterns
- `awk`: Text processing and data extraction
- `sed`: Stream editing
- `cut`: Extract columns from files
- `sort`: Sort data
- `uniq`: Remove duplicates
- `wc`: Count lines, words, characters
- `head`/`tail`: View file beginning/end

---

## PowerShell for Data Science {#powershell-for-data-science}

### Why PowerShell Over CMD?

✅ **Object-oriented** - Commands pass objects, not just text
✅ **Rich scripting language** - Variables, loops, functions, error handling
✅ **Cross-platform** - PowerShell Core runs on Windows, Linux, macOS
✅ **Better integration** - .NET framework, COM objects, WMI
✅ **Pipeline power** - Chain commands efficiently
✅ **AI integration** - New AI Shell announced in Nov 2024

### PowerShell Basics for Data Scientists

#### 1. Essential Cmdlets

```powershell
# Navigation (aliases work: cd, ls, pwd)
Get-Location                        # Current directory
Set-Location C:\Projects            # Change directory
Get-ChildItem                       # List files (alias: ls, dir)
Get-ChildItem -Recurse -Filter *.csv  # Find all CSV files

# File operations
Copy-Item source.csv dest.csv
Move-Item file.txt new_location\
Remove-Item file.txt
Rename-Item old.csv new.csv
New-Item -ItemType Directory -Name "data"  # Create folder
```

#### 2. Working with CSV/Data Files

```powershell
# Import and analyze CSV
$data = Import-Csv "sales_data.csv"
$data | Get-Member                  # See available properties
$data | Select-Object -First 5      # View first 5 rows
$data | Where-Object {$_.Revenue -gt 1000}  # Filter rows
$data | Measure-Object Revenue -Average -Sum  # Statistics

# Export results
$data | Export-Csv "filtered_data.csv" -NoTypeInformation

# Convert between formats
$data | ConvertTo-Json | Out-File "data.json"
Get-Content "data.json" | ConvertFrom-Json
```

#### 3. Automation Scripts for Data Science Workflows

**Example: Automated Data Processing Pipeline**
```powershell
# process_data.ps1
param(
    [string]$InputFolder = ".\data\raw",
    [string]$OutputFolder = ".\data\processed"
)

# Create output folder if not exists
New-Item -ItemType Directory -Force -Path $OutputFolder

# Process each CSV file
Get-ChildItem -Path $InputFolder -Filter *.csv | ForEach-Object {
    Write-Host "Processing: $($_.Name)"

    # Activate Python environment and run script
    & conda activate myenv
    python process_csv.py $_.FullName "$OutputFolder\processed_$($_.Name)"

    # Log completion
    Add-Content -Path ".\logs\processing_log.txt" `
        -Value "$(Get-Date) - Processed $($_.Name)"
}

Write-Host "All files processed successfully!"
```

**Example: Environment Setup Script**
```powershell
# setup_environment.ps1
# Automate creation of data science environment

# Check Python installation
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Python found: $(python --version)"
} else {
    Write-Error "Python not installed!"
    exit 1
}

# Create virtual environment
python -m venv venv

# Activate environment
.\venv\Scripts\Activate.ps1

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
pip list

Write-Host "Environment setup complete!"
```

#### 4. System Monitoring for ML Training

```powershell
# Monitor GPU usage during training
while ($true) {
    Clear-Host
    nvidia-smi
    Start-Sleep -Seconds 2
}

# Monitor CPU and Memory
Get-Process python | Select-Object CPU, WorkingSet, ProcessName

# Disk space check before large downloads
Get-PSDrive C | Select-Object Used, Free
```

#### 5. Scheduled Tasks for Automation

```powershell
# Create scheduled task to run data collection daily
$action = New-ScheduledTaskAction -Execute "python" `
    -Argument "C:\Projects\collect_data.py"

$trigger = New-ScheduledTaskTrigger -Daily -At 2am

Register-ScheduledTask -TaskName "DailyDataCollection" `
    -Action $action -Trigger $trigger
```

### Advanced PowerShell Features

#### Working with APIs
```powershell
# Fetch data from REST API
$response = Invoke-RestMethod -Uri "https://api.example.com/data"
$response | ConvertTo-Json -Depth 10 | Out-File "api_data.json"
```

#### Parallel Processing
```powershell
# Process files in parallel (PowerShell 7+)
$files = Get-ChildItem *.csv
$files | ForEach-Object -Parallel {
    python process.py $_.FullName
} -ThrottleLimit 4  # Use 4 cores
```

### New AI Shell (2024)

Microsoft announced **AI Shell** in November 2024:
- AI-powered command suggestions
- Azure OpenAI integration
- Natural language to PowerShell commands
- Context-aware assistance

```powershell
# Install AI Shell (when available)
Install-Module -Name AIShell
```

---

## Windows Subsystem for Linux (WSL2) {#wsl2-setup}

### Why WSL2 for Data Science?

✅ **Native Linux environment** - Run Ubuntu, Debian, etc. on Windows
✅ **Full CUDA support** - GPU acceleration for ML (94% bare metal performance)
✅ **Docker integration** - Containerize ML models
✅ **Best of both worlds** - Windows tools + Linux command line
✅ **File system access** - Access Windows files from Linux (`/mnt/c/`)
✅ **VS Code integration** - Seamless remote development

### WSL2 Setup Guide

#### 1. Installation (Windows 10/11)

```powershell
# Enable WSL (requires admin)
wsl --install

# Or install specific distribution
wsl --install -d Ubuntu-22.04

# List available distributions
wsl --list --online

# Set WSL 2 as default
wsl --set-default-version 2
```

#### 2. Ubuntu Setup for Data Science

```bash
# Update package list
sudo apt update && sudo apt upgrade -y

# Install Python development tools
sudo apt install python3-pip python3-venv python3-dev

# Install build essentials
sudo apt install build-essential git curl wget

# Install common data science libraries system dependencies
sudo apt install libhdf5-dev libatlas-base-dev

# Install Miniconda (recommended for data science)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

#### 3. VS Code Integration

```powershell
# Install VS Code WSL extension
code --install-extension ms-vscode-remote.remote-wsl

# Open WSL from VS Code
# Press F1, type "WSL: Connect to WSL"

# Or from command line
wsl code .  # Opens current directory in VS Code
```

#### 4. Jupyter Notebook Setup

```bash
# In WSL Ubuntu
pip install jupyter notebook

# Generate config
jupyter notebook --generate-config

# Edit config to disable redirect (required for WSL)
# In ~/.jupyter/jupyter_notebook_config.py, add:
# c.NotebookApp.use_redirect_file = False

# Start Jupyter (access from Windows browser)
jupyter notebook --no-browser
```

#### 5. Accessing Windows Files

```bash
# Windows C:\ drive is at /mnt/c/
cd /mnt/c/Users/YourName/Projects

# Create symbolic link for easy access
ln -s /mnt/c/Users/YourName/Projects ~/projects
cd ~/projects
```

#### 6. GPU Support for Deep Learning

```bash
# Install NVIDIA drivers on Windows (not WSL)
# Download from NVIDIA website

# Install CUDA toolkit in WSL
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt update
sudo apt install cuda

# Verify CUDA
nvidia-smi  # Should show GPU info

# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### WSL2 Best Practices

1. **Store project files in Linux filesystem** for better performance
   ```bash
   # Good: ~/projects/my_project
   # Avoid: /mnt/c/Users/YourName/projects/my_project
   ```

2. **Use Git in WSL** for better performance
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Backup WSL distributions**
   ```powershell
   wsl --export Ubuntu-22.04 D:\Backups\ubuntu-backup.tar
   wsl --import Ubuntu-Restored D:\WSL\Ubuntu D:\Backups\ubuntu-backup.tar
   ```

4. **Resource limits** (create `.wslconfig` in `C:\Users\YourName\`)
   ```ini
   [wsl2]
   memory=8GB
   processors=4
   swap=2GB
   ```

---

## Windows Terminal Configuration {#windows-terminal}

### Why Windows Terminal?

✅ **Multiple tabs** - PowerShell, CMD, WSL, Git Bash in one window
✅ **Customizable** - Themes, fonts, keybindings
✅ **GPU acceleration** - Fast text rendering
✅ **Unicode support** - Emojis, special characters
✅ **Split panes** - Multi-terminal view

### Installation

```powershell
# Via winget (recommended)
winget install Microsoft.WindowsTerminal

# Or from Microsoft Store
# Search for "Windows Terminal"
```

### Configuration for Data Science

**Open settings**: `Ctrl + ,` or Settings button

#### 1. Set Default Profile

```json
{
    "defaultProfile": "{guid-of-powershell-7}"
}
```

#### 2. Add Anaconda Prompt Profile

```json
{
    "profiles": {
        "list": [
            {
                "name": "Anaconda Prompt",
                "commandline": "cmd.exe /K C:\\Users\\YourName\\anaconda3\\Scripts\\activate.bat",
                "icon": "C:\\Users\\YourName\\anaconda3\\Menu\\anaconda-navigator.ico",
                "startingDirectory": "%USERPROFILE%\\Projects"
            }
        ]
    }
}
```

#### 3. Useful Keybindings

```json
{
    "actions": [
        { "command": "newTab", "keys": "ctrl+t" },
        { "command": "closeTab", "keys": "ctrl+w" },
        { "command": "nextTab", "keys": "ctrl+tab" },
        { "command": "prevTab", "keys": "ctrl+shift+tab" },
        {
            "command": { "action": "splitPane", "split": "horizontal" },
            "keys": "alt+shift+-"
        },
        {
            "command": { "action": "splitPane", "split": "vertical" },
            "keys": "alt+shift+plus"
        }
    ]
}
```

#### 4. Productivity Setup

**Typical Data Science Layout:**
- Top left: PowerShell (main work)
- Top right: Python REPL or Jupyter
- Bottom: WSL Ubuntu terminal
- Separate tab: Git operations

---

## Package Managers {#package-managers}

### Windows Package Manager (winget)

**Built into Windows 11**, official Microsoft tool.

#### Basic Usage

```powershell
# Search for packages
winget search python
winget search "visual studio code"

# Install packages
winget install Python.Python.3.11
winget install Microsoft.VisualStudioCode
winget install Git.Git
winget install Anaconda.Miniconda3

# List installed packages
winget list

# Upgrade all packages
winget upgrade --all

# Upgrade specific package
winget upgrade Python.Python.3.11
```

#### Version Pinning (2024 Feature)

```powershell
# Pin Python to prevent auto-upgrade
winget pin add --id Python.Python.3.11

# List pinned packages
winget pin list

# Remove pin
winget pin remove --id Python.Python.3.11
```

#### Export/Import Environment

```powershell
# Export installed apps
winget export -o packages.json

# Import on new machine
winget import -i packages.json
```

**Data Science Winget Setup Script:**
```powershell
# setup_datascience_env.ps1
$packages = @(
    "Python.Python.3.11",
    "Microsoft.VisualStudioCode",
    "Git.Git",
    "GitHub.GitHubDesktop",
    "Anaconda.Miniconda3",
    "Docker.DockerDesktop",
    "Microsoft.WindowsTerminal",
    "Microsoft.PowerShell"
)

foreach ($package in $packages) {
    Write-Host "Installing $package..."
    winget install $package --silent --accept-source-agreements
}
```

### Chocolatey

**Community-driven**, largest package repository (10,000+ packages).

#### Installation

```powershell
# Run as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

#### Basic Usage

```powershell
# Search packages
choco search python

# Install packages
choco install python --version=3.11.0
choco install vscode git anaconda3 -y

# Upgrade all
choco upgrade all -y

# List installed
choco list --local-only
```

#### Chocolatey for Data Science

```powershell
# Install complete data science stack
choco install python --version=3.11.0 -y
choco install git vscode anaconda3 -y
choco install r r.studio -y
choco install nodejs -y
choco install postgresql -y
choco install docker-desktop -y
```

### Comparison: winget vs Chocolatey

| Feature | winget | Chocolatey |
|---------|--------|------------|
| **Packages** | 8,000+ | 10,000+ |
| **Installation** | Pre-installed (Win11) | Manual install |
| **Speed** | Fast | Moderate |
| **GUI** | No (CLI only) | Chocolatey GUI available |
| **Pinning** | ✅ (2024) | ✅ |
| **Export/Import** | ✅ JSON | ✅ Packages.config |
| **Pre-release** | Limited | ✅ Extensive |
| **Best for** | Modern Windows setup | Power users, CI/CD |

**Recommendation for Data Science Students:**
- Start with **winget** (simpler, built-in)
- Add **Chocolatey** if you need packages not in winget
- Use both together (they don't conflict)

---

## Automation & Scripting {#automation-scripting}

### Batch Files (.bat) vs PowerShell (.ps1)

#### When to Use Batch Files

✅ Simple, sequential commands
✅ Legacy system compatibility
✅ Quick one-off scripts
✅ No dependencies

**Example: Quick environment activation**
```batch
@echo off
REM activate_env.bat
call conda activate myenv
jupyter notebook
```

#### When to Use PowerShell

✅ Complex logic (conditionals, loops)
✅ Object manipulation
✅ Error handling
✅ Cross-platform scripts
✅ Integration with .NET/APIs

**Example: Data backup automation**
```powershell
# backup_data.ps1
param(
    [string]$SourcePath = "C:\Projects\data",
    [string]$BackupPath = "D:\Backups",
    [int]$DaysToKeep = 7
)

# Create timestamped backup
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFolder = Join-Path $BackupPath "backup_$timestamp"

# Copy files
Copy-Item -Path $SourcePath -Destination $backupFolder -Recurse

# Compress
Compress-Archive -Path $backupFolder -DestinationPath "$backupFolder.zip"
Remove-Item -Path $backupFolder -Recurse

# Clean old backups
Get-ChildItem $BackupPath -Filter "backup_*.zip" |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-$DaysToKeep) } |
    Remove-Item -Force

Write-Host "Backup completed: $backupFolder.zip"
```

### Calling Python from Scripts

#### From Batch File
```batch
@echo off
REM run_analysis.bat
echo Starting data analysis...
python analyze_data.py --input data\sales.csv --output results\
if %ERRORLEVEL% EQU 0 (
    echo Analysis completed successfully!
) else (
    echo Analysis failed with error code %ERRORLEVEL%
)
```

#### From PowerShell
```powershell
# run_pipeline.ps1
try {
    Write-Host "Step 1: Data collection"
    python collect_data.py

    Write-Host "Step 2: Data cleaning"
    python clean_data.py

    Write-Host "Step 3: Model training"
    python train_model.py

    Write-Host "Pipeline completed successfully!"
}
catch {
    Write-Error "Pipeline failed: $_"
    exit 1
}
```

### Task Scheduler Integration

```powershell
# Schedule daily model retraining
$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-File C:\Projects\retrain_model.ps1"

$trigger = New-ScheduledTaskTrigger -Daily -At 3am

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "DailyModelRetraining" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -User "SYSTEM" `
    -RunLevel Highest
```

---

## Environment Management {#environment-management}

### Python Virtual Environments on Windows

#### 1. venv (Built-in)

```batch
REM Create environment
python -m venv myenv

REM Activate (CMD)
myenv\Scripts\activate.bat

REM Activate (PowerShell)
myenv\Scripts\Activate.ps1

REM Deactivate
deactivate
```

**PowerShell Execution Policy Issue:**
```powershell
# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2. Conda/Miniconda (Recommended for Data Science)

```batch
REM Create environment with specific Python version
conda create -n ml_env python=3.11 -y

REM Activate
conda activate ml_env

REM Install packages
conda install numpy pandas scikit-learn matplotlib

REM Export environment
conda env export > environment.yml

REM Create from environment file
conda env create -f environment.yml

REM List environments
conda env list

REM Remove environment
conda env remove -n ml_env
```

#### 3. Environment Automation Script

**PowerShell script to create standardized data science environment:**

```powershell
# create_ds_env.ps1
param(
    [string]$EnvName = "datascience",
    [string]$PythonVersion = "3.11"
)

Write-Host "Creating conda environment: $EnvName"

# Create environment
conda create -n $EnvName python=$PythonVersion -y

# Activate environment
conda activate $EnvName

# Core data science packages
$packages = @(
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "jupyter",
    "notebook",
    "ipykernel",
    "scipy",
    "statsmodels"
)

Write-Host "Installing packages..."
conda install $packages -y

# Additional pip packages
pip install jupyterlab
pip install black isort flake8  # Code quality

# Add kernel to Jupyter
python -m ipykernel install --user --name=$EnvName --display-name "Python ($EnvName)"

Write-Host "Environment created successfully!"
Write-Host "To activate: conda activate $EnvName"
```

### Managing Multiple Python Versions

```powershell
# List installed Python versions
py --list

# Run specific version
py -3.11 script.py
py -3.10 script.py

# Create venv with specific version
py -3.11 -m venv myenv_311
```

### PATH Management

```powershell
# View PATH
$env:Path -split ";"

# Add to PATH (current session)
$env:Path += ";C:\MyTools"

# Add permanently (requires admin)
[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path", "Machine") + ";C:\MyTools",
    "Machine"
)

# Verify Python in PATH
where.exe python
Get-Command python
```

---

## Recommended Learning Path {#learning-path}

### Phase 1: Foundations (Weeks 1-2)

**Notebook 00: Setup & Introduction**
- Install Windows Terminal
- Install winget/Chocolatey
- Install Python, Git, VS Code
- Configure PowerShell profile
- Learn basic CMD commands

**Notebook 01: PowerShell Fundamentals**
- Cmdlets and aliases
- Pipelines and object manipulation
- Variables and data types
- File system navigation
- Help system (`Get-Help`)

**Notebook 02: Python-Windows Integration**
- Running Python from command line
- Virtual environments (venv)
- Installing packages with pip
- subprocess module basics
- Batch file basics

### Phase 2: Core Skills (Weeks 3-4)

**Notebook 03: File System Operations**
- Working with paths (pathlib)
- Reading/writing files
- Directory traversal
- File permissions
- Batch file operations

**Notebook 04: Process & Service Management**
- Task Manager via CLI
- psutil library
- Monitoring system resources
- Killing processes
- Background jobs

**Notebook 05: Registry & System Configuration**
- Understanding Windows Registry
- Reading registry with winreg
- Environment variables
- System settings
- Configuration management

### Phase 3: Advanced Topics (Weeks 5-6)

**Notebook 06: Networking Basics**
- Network configuration
- Testing connectivity
- HTTP requests (requests library)
- API interactions
- Web scraping considerations

**Notebook 07: Scheduled Tasks & Automation**
- Task Scheduler
- Cron-like scheduling
- Email notifications
- Log file management
- Error handling

**Notebook 08: Windows Security & Permissions**
- User permissions
- ACLs (Access Control Lists)
- Running as administrator
- Credential management
- Security best practices

### Phase 4: Mastery (Weeks 7-8)

**Notebook 09: WSL2 Deep Dive**
- WSL installation and configuration
- File system integration
- Docker on WSL2
- GPU acceleration
- Cross-platform workflows

**Notebook 10: Advanced Scripting & Final Project**
- Parallel processing
- Error handling patterns
- Logging frameworks
- Testing scripts
- Complete automation project

### Bonus: WSL2 Integration
**Notebook 11: WSL2 for Data Science**
- Setup Ubuntu for data science
- VS Code Remote development
- Jupyter in WSL
- Docker containers
- Best practices

---

## Practical Projects {#practical-projects}

### Project 1: Automated Data Pipeline
**Skills**: PowerShell, Python, Task Scheduler

Build a script that:
1. Downloads data from API daily
2. Cleans and processes data
3. Trains ML model
4. Generates report
5. Sends email notification

### Project 2: Environment Manager
**Skills**: Conda, PowerShell, Configuration

Create a tool to:
1. List all conda environments
2. Export environment specs
3. Create new environments from template
4. Clean unused environments
5. Generate documentation

### Project 3: System Monitor Dashboard
**Skills**: Python, PowerShell, Visualization

Build a monitoring tool:
1. Track CPU/RAM/Disk usage
2. Monitor running Python processes
3. Display GPU utilization
4. Log metrics to database
5. Create real-time dashboard

### Project 4: Batch File Processor
**Skills**: File operations, Parallel processing

Create a utility to:
1. Process CSV files in bulk
2. Apply transformations
3. Handle errors gracefully
4. Generate summary reports
5. Archive processed files

### Project 5: Development Environment Setup
**Skills**: Package managers, Automation

Build a script to:
1. Install required software (Python, Git, VS Code)
2. Configure Git settings
3. Create standard directory structure
4. Set up conda environments
5. Install VS Code extensions

---

## Additional Resources

### Official Documentation
- [PowerShell Documentation](https://docs.microsoft.com/powershell/)
- [WSL Documentation](https://docs.microsoft.com/windows/wsl/)
- [Windows Terminal Documentation](https://docs.microsoft.com/windows/terminal/)
- [Python on Windows](https://docs.python.org/3/using/windows.html)

### Books
- *Learn Windows PowerShell in a Month of Lunches* - Don Jones
- *PowerShell Cookbook* - Lee Holmes
- *Data Science at the Command Line* - Jeroen Janssens
- *Automate the Boring Stuff with Python* - Al Sweigart

### Online Courses
- Microsoft Learn: PowerShell modules
- Coursera: Command Line Tools for Data Science
- YouTube: PowerShell for Data Scientists

### Communities
- [r/PowerShell](https://reddit.com/r/PowerShell)
- [PowerShell.org Forums](https://powershell.org/forums/)
- [Stack Overflow: PowerShell](https://stackoverflow.com/questions/tagged/powershell)

### Tools & Extensions
- **VS Code Extensions**:
  - PowerShell
  - Remote - WSL
  - Python
  - Jupyter
- **PowerShell Modules**:
  - PSReadLine (better CLI experience)
  - posh-git (Git integration)
  - oh-my-posh (prompt customization)

---

## Quick Reference

### Common PowerShell Commands for Data Science

```powershell
# File operations
Get-ChildItem -Recurse -Filter *.csv
Copy-Item -Recurse source\ dest\
Move-Item *.csv processed\

# CSV manipulation
Import-Csv data.csv | Where-Object {$_.Sales -gt 1000} | Export-Csv filtered.csv

# System info
Get-Process python
Get-PSDrive
Get-NetIPAddress

# Package management
pip list | Select-String "numpy"
conda env list

# Environment
$env:PYTHONPATH
[Environment]::GetEnvironmentVariable("PATH")
```

### Common Troubleshooting

**Issue**: PowerShell script won't run
**Solution**: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Issue**: Python not found in PATH
**Solution**: Add Python to PATH or use `py` launcher

**Issue**: Conda activate doesn't work in PowerShell
**Solution**: `conda init powershell` then restart terminal

**Issue**: WSL slow file access
**Solution**: Store files in Linux filesystem (`~`) not Windows (`/mnt/c/`)

---

## Conclusion

Mastering Windows tools will significantly boost your productivity as a data science student. Start with the foundations, practice regularly, and build real projects to solidify your skills.

**Next Steps:**
1. Complete Phase 1 notebooks (00-02)
2. Build your first automation script
3. Set up WSL2 for Linux compatibility
4. Join PowerShell community for support

Happy learning! 🚀

---

**Document Version**: 1.0
**Last Updated**: November 2024
**Maintained By**: Educational Notebook Portfolio Project
