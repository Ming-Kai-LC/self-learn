# VS Code Extension Guide

Curated list of recommended extensions for different development workflows.

## Essential Extensions for Everyone

### Python Extension Pack
**ID**: `ms-python.python`
**Description**: Complete Python language support including IntelliSense, linting, debugging, code navigation, code formatting, refactoring, and more.

**Installation**:
```bash
code --install-extension ms-python.python
```

**Key Features**:
- IntelliSense (Pylance)
- Linting (Pylint, flake8, mypy)
- Debugging
- Code formatting (Black, autopep8, yapf)
- Refactoring
- Jupyter notebook support

### GitLens
**ID**: `eamodio.gitlens`
**Description**: Supercharges Git capabilities. Visualize code authorship, explore Git history, and gain valuable insights.

**Features**:
- Blame annotations
- File history
- Branch comparison
- Commit search
- Interactive rebase editor

### Prettier - Code Formatter
**ID**: `esbenp.prettier-vscode`
**Description**: Opinionated code formatter supporting JavaScript, TypeScript, CSS, HTML, JSON, and more.

**Configuration**:
```json
{
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
}
```

## Python Development

### Pylance
**ID**: `ms-python.vscode-pylance`
**Description**: Fast, feature-rich language support for Python.

**Features**:
- Type checking
- Auto-imports
- Enhanced IntelliSense
- Code navigation

### Python Docstring Generator
**ID**: `njpwerner.autodocstring`
**Description**: Automatically generates detailed docstrings for Python functions.

**Usage**: Type `"""` below a function and press Enter.

### Jupyter
**ID**: `ms-toolsai.jupyter`
**Description**: Full Jupyter notebook support in VS Code.

**Features**:
- Run Jupyter notebooks
- Interactive window
- Variable explorer
- Plot viewer

## Web Development

### ESLint
**ID**: `dbaeumer.vscode-eslint`
**Description**: Integrates ESLint JavaScript linting into VS Code.

**Installation**:
```bash
npm install -g eslint
code --install-extension dbaeumer.vscode-eslint
```

### Live Server
**ID**: `ritwickdey.liveserver`
**Description**: Launch a local development server with live reload feature.

**Usage**: Right-click HTML file → "Open with Live Server"

### Auto Rename Tag
**ID**: `formulahendry.auto-rename-tag`
**Description**: Automatically rename paired HTML/XML tags.

### CSS Peek
**ID**: `pranaygp.vscode-css-peek`
**Description**: Peek and navigate to CSS definitions from HTML.

## Productivity

### Path Intellisense
**ID**: `christian-kohler.path-intellisense`
**Description**: Autocompletes filenames in your code.

### Bracket Pair Colorizer 2
**ID**: `coenraads.bracket-pair-colorizer-2`
**Description**: Colors matching brackets for better code readability.

**Note**: VS Code now has built-in bracket pair colorization. Enable with:
```json
{
    "editor.bracketPairColorization.enabled": true
}
```

### TODO Highlight
**ID**: `wayou.vscode-todo-highlight`
**Description**: Highlights TODO, FIXME, and other annotations in your code.

**Configuration**:
```json
{
    "todohighlight.keywords": [
        "TODO:",
        "FIXME:",
        "NOTE:"
    ]
}
```

### Better Comments
**ID**: `aaron-bond.better-comments`
**Description**: Color-codes comments based on type (alerts, queries, TODOs, highlights).

## Themes and Icons

### One Dark Pro
**ID**: `zhuangtongfa.material-theme`
**Description**: Atom's iconic One Dark theme for VS Code.

### Dracula Official
**ID**: `dracula-theme.theme-dracula`
**Description**: Official Dracula theme - dark theme based on Dracula colors.

### Material Icon Theme
**ID**: `pkief.material-icon-theme`
**Description**: Material Design icons for VS Code.

**Activation**: File → Preferences → File Icon Theme → Material Icon Theme

### Night Owl
**ID**: `sdras.night-owl`
**Description**: Fine-tuned theme for those who code at night.

## Git and Version Control

### Git Graph
**ID**: `mhutchie.git-graph`
**Description**: View a Git Graph of your repository and perform Git actions.

**Features**:
- Interactive graph visualization
- Commit details
- Branch operations
- Compare commits

### GitHub Pull Requests and Issues
**ID**: `github.vscode-pull-request-github`
**Description**: Review and manage GitHub pull requests and issues.

## Remote Development

### Remote - SSH
**ID**: `ms-vscode-remote.remote-ssh`
**Description**: Open folders on remote machines using SSH.

### Remote - WSL
**ID**: `ms-vscode-remote.remote-wsl`
**Description**: Open folders in Windows Subsystem for Linux.

### Remote - Containers
**ID**: `ms-vscode-remote.remote-containers`
**Description**: Open folders inside Docker containers.

## Data Science

### Data Wrangler
**ID**: `ms-toolsai.datawrangler`
**Description**: Data viewing and cleaning for pandas DataFrames.

### Jupyter Notebook Renderers
**ID**: `ms-toolsai.jupyter-renderers`
**Description**: Renderers for outputs of Jupyter notebooks.

## Markdown

### Markdown All in One
**ID**: `yzhang.markdown-all-in-one`
**Description**: All-in-one Markdown support (keyboard shortcuts, TOC, auto preview).

**Features**:
- Keyboard shortcuts
- Table of contents
- Auto preview
- Math support

### Markdown Preview Enhanced
**ID**: `shd101wyy.markdown-preview-enhanced`
**Description**: Enhanced Markdown preview with many additional features.

## Docker

### Docker
**ID**: `ms-azuretools.vscode-docker`
**Description**: Makes it easy to create, manage, and debug containerized applications.

**Features**:
- Dockerfile and docker-compose support
- Image management
- Container management
- Registry explorer

## Database

### SQLTools
**ID**: `mtxr.sqltools`
**Description**: Database management for multiple database systems.

**Supported Databases**:
- PostgreSQL
- MySQL
- SQLite
- SQL Server

## Installation Commands

### Essential Setup (Beginner)
```bash
code --install-extension ms-python.python
code --install-extension eamodio.gitlens
code --install-extension esbenp.prettier-vscode
code --install-extension pkief.material-icon-theme
```

### Python Developer Setup
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension njpwerner.autodocstring
code --install-extension eamodio.gitlens
```

### Web Developer Setup
```bash
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension ritwickdey.liveserver
code --install-extension formulahendry.auto-rename-tag
code --install-extension pranaygp.vscode-css-peek
```

## Extension Settings

### Configuring Extensions

Extensions can be configured in `settings.json`:

```json
{
    // Python
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",

    // Prettier
    "prettier.singleQuote": true,
    "prettier.semi": false,

    // GitLens
    "gitlens.codeLens.enabled": true,
    "gitlens.hovers.enabled": true,

    // Auto Save
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000
}
```

## Finding More Extensions

### Browse in VS Code
1. Click Extensions icon (`Ctrl+Shift+X`)
2. Use search bar
3. Filter by:
   - Featured
   - Most Popular
   - Recently Added
   - Recommended

### Online Marketplace
Visit: https://marketplace.visualstudio.com/vscode

### Categories
- Programming Languages
- Snippets
- Linters
- Themes
- Debuggers
- Formatters
- Keymaps
- Other

## Managing Extensions

### Disable Extension
1. Right-click extension
2. Select "Disable"
3. Or disable for specific workspace

### Uninstall Extension
1. Right-click extension
2. Select "Uninstall"

### Extension Recommendations
Create `.vscode/extensions.json` in your workspace:

```json
{
    "recommendations": [
        "ms-python.python",
        "eamodio.gitlens",
        "esbenp.prettier-vscode"
    ]
}
```

## Troubleshooting

### Extension Not Working
1. Check extension is enabled
2. Reload window: `Ctrl+Shift+P` → "Reload Window"
3. Check extension output: Output panel → Select extension
4. Update extension to latest version

### Conflicts Between Extensions
1. Disable all extensions
2. Enable one by one to identify conflict
3. Check extension documentation for known issues

### Performance Issues
Too many extensions can slow VS Code:
1. Disable unused extensions
2. Use workspace-specific extensions
3. Check extension performance: `Ctrl+Shift+P` → "Developer: Show Running Extensions"

---

**Remember**: Quality over quantity! Install extensions you actually need.
