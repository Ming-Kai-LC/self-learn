# Troubleshooting Guide

This guide covers common issues you might encounter while learning Git and GitHub, along with their solutions.

---

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Authentication Problems](#authentication-problems)
3. [Git Command Errors](#git-command-errors)
4. [Merge Conflicts](#merge-conflicts)
5. [Push/Pull Issues](#pushpull-issues)
6. [Branch Problems](#branch-problems)
7. [GitHub-Specific Issues](#github-specific-issues)
8. [Jupyter Notebook Issues](#jupyter-notebook-issues)

---

## Installation Issues

### Git Not Found

**Problem**: `git: command not found` or `'git' is not recognized`

**Solutions**:
1. **Verify Installation**:
   ```bash
   git --version
   ```

2. **Install Git**:
   - **Windows**: Download from [git-scm.com](https://git-scm.com)
   - **Mac**: `brew install git` or download from git-scm.com
   - **Linux**: `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora)

3. **Add to PATH** (if installed but not found):
   - Windows: Add `C:\Program Files\Git\bin` to PATH
   - Restart terminal after installation

### Python/Jupyter Issues

**Problem**: Jupyter commands not working

**Solutions**:
```bash
# Ensure virtual environment is activated
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Install Jupyter if missing
pip install jupyter notebook

# Verify installation
jupyter --version
```

---

## Authentication Problems

### Permission Denied (publickey)

**Problem**: `Permission denied (publickey)` when pushing/pulling

**Solutions**:

1. **Check SSH key exists**:
   ```bash
   ls -la ~/.ssh
   ```

2. **Generate SSH key if missing**:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

3. **Add key to SSH agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

4. **Add public key to GitHub**:
   - Copy public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste and save

5. **Test connection**:
   ```bash
   ssh -T git@github.com
   ```

### HTTPS Authentication Failed

**Problem**: Authentication failed when using HTTPS

**Solutions**:

1. **Use Personal Access Token** (not password):
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate new token with `repo` scope
   - Use token as password when prompted

2. **Cache credentials**:
   ```bash
   # Windows:
   git config --global credential.helper wincred

   # Mac:
   git config --global credential.helper osxkeychain

   # Linux:
   git config --global credential.helper cache
   ```

3. **Switch to SSH** (recommended):
   ```bash
   # Change remote URL from HTTPS to SSH
   git remote set-url origin git@github.com:USERNAME/REPO.git
   ```

---

## Git Command Errors

### fatal: not a git repository

**Problem**: `fatal: not a git repository (or any of the parent directories): .git`

**Solution**:
```bash
# You're not in a Git repository
# Either:
# 1. Navigate to your repository:
cd path/to/your/repo

# 2. Or initialize a new repository:
git init
```

### fatal: refusing to merge unrelated histories

**Problem**: Cannot merge repositories with different histories

**Solution**:
```bash
# Allow unrelated histories (use with caution!)
git pull origin main --allow-unrelated-histories
```

### error: Your local changes would be overwritten

**Problem**: Cannot pull because of local changes

**Solutions**:

1. **Stash changes** (save for later):
   ```bash
   git stash
   git pull
   git stash pop
   ```

2. **Commit changes**:
   ```bash
   git add .
   git commit -m "Save local changes"
   git pull
   ```

3. **Discard changes** (careful!):
   ```bash
   git reset --hard
   git pull
   ```

---

## Merge Conflicts

### Understanding Conflict Markers

**What you see**:
```
<<<<<<< HEAD
Your current branch's code
=======
Incoming branch's code
>>>>>>> feature-branch
```

**How to resolve**:

1. **Open the file** and look for conflict markers

2. **Choose what to keep**:
   - Keep HEAD version (current branch)
   - Keep incoming version (merging branch)
   - Combine both
   - Write completely new code

3. **Remove markers**:
   ```
   # Remove these lines:
   <<<<<<< HEAD
   =======
   >>>>>>> feature-branch
   ```

4. **Stage and commit**:
   ```bash
   git add <file>
   git commit -m "Resolve merge conflict"
   ```

### Aborting a Merge

**Problem**: Want to cancel merge

**Solution**:
```bash
git merge --abort
```

### Using a Merge Tool

```bash
# Configure merge tool (VS Code example)
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Use merge tool
git mergetool
```

---

## Push/Pull Issues

### Updates were rejected

**Problem**: `Updates were rejected because the remote contains work that you do not have locally`

**Solutions**:

1. **Pull first** (recommended):
   ```bash
   git pull origin main
   # Resolve any conflicts
   git push origin main
   ```

2. **Rebase** (cleaner history):
   ```bash
   git pull --rebase origin main
   git push origin main
   ```

3. **Force push** (DANGEROUS - avoid on shared branches!):
   ```bash
   git push --force origin main
   ```

### Everything up-to-date (but nothing pushed)

**Problem**: `Everything up-to-date` but commits not on GitHub

**Solution**:
```bash
# Check current branch
git branch

# Set upstream branch
git push -u origin <branch-name>
```

### LFS (Large File) Errors

**Problem**: Push rejected due to large files

**Solutions**:

1. **Use Git LFS**:
   ```bash
   # Install Git LFS
   git lfs install

   # Track large files
   git lfs track "*.psd"
   git lfs track "*.mp4"

   # Add .gitattributes
   git add .gitattributes
   git commit -m "Add LFS tracking"
   ```

2. **Remove large file from history**:
   ```bash
   # Remove file from all commits
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch path/to/large/file" \
   --prune-empty --tag-name-filter cat -- --all
   ```

---

## Branch Problems

### Cannot delete branch

**Problem**: `error: Cannot delete branch 'feature' checked out at...`

**Solution**:
```bash
# Switch to a different branch first
git switch main
git branch -d feature
```

### Branch already exists

**Problem**: `fatal: A branch named 'feature' already exists`

**Solutions**:
```bash
# Use different name
git branch feature-v2

# Or delete existing branch
git branch -d feature
git branch feature
```

### Lost commits after deleting branch

**Problem**: Deleted branch but need commits back

**Solution**:
```bash
# Find lost commits
git reflog

# Create new branch from commit
git branch recovered-branch <commit-hash>
```

---

## GitHub-Specific Issues

### README not displaying

**Problem**: README.md not showing on GitHub

**Solutions**:
- Ensure file is named exactly `README.md` (case-sensitive)
- Check it's in the repository root
- Verify Markdown syntax is valid
- Push to GitHub: `git push origin main`

### Pull Request conflicts

**Problem**: PR has conflicts

**Solutions**:

1. **Update your branch**:
   ```bash
   git switch your-feature-branch
   git pull origin main
   # Resolve conflicts
   git push origin your-feature-branch
   ```

2. **Rebase** (cleaner):
   ```bash
   git switch your-feature-branch
   git rebase main
   # Resolve conflicts
   git push --force origin your-feature-branch
   ```

### Actions workflow failing

**Problem**: GitHub Actions workflow not running or failing

**Solutions**:
- Check YAML syntax (indentation matters!)
- View workflow logs in Actions tab
- Verify secrets are configured correctly
- Check branch protection rules
- Ensure workflow file is in `.github/workflows/`

---

## Jupyter Notebook Issues

### Kernel not starting

**Problem**: Jupyter kernel won't start

**Solutions**:
```bash
# Reinstall kernel
pip install ipykernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

### Git ignoring notebook outputs

**Problem**: Want to track or ignore notebook outputs

**Solution**:

1. **To ignore outputs** (recommended):
   ```bash
   # Install nbstripout
   pip install nbstripout

   # Set up for repository
   nbstripout --install
   ```

2. **To track outputs**:
   - Just commit normally
   - Note: Makes diffs harder to read

### Large notebook files

**Problem**: Notebook files are very large

**Solutions**:
- Clear outputs before committing: Cell → All Output → Clear
- Use nbstripout (see above)
- Store large data separately

---

## General Tips

### When Stuck

1. **Check status**:
   ```bash
   git status
   ```

2. **View recent commits**:
   ```bash
   git log --oneline -10
   ```

3. **Check remote configuration**:
   ```bash
   git remote -v
   ```

4. **See what changed**:
   ```bash
   git diff
   ```

### Undo Almost Anything

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Undo uncommitted changes
git restore <file>

# View reflog (history of HEAD)
git reflog
```

### Get Help

```bash
# General help
git help

# Command-specific help
git help <command>
# Example:
git help merge
```

---

## Still Stuck?

### Resources

- **Stack Overflow**: Search for your error message
- **GitHub Community**: [github.community](https://github.community)
- **Git Documentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Docs**: [docs.github.com](https://docs.github.com)

### Getting Support

1. **Search first**: Your problem has likely been solved before
2. **Include details**:
   - Exact error message
   - Commands you ran
   - Git version (`git --version`)
   - OS and version
3. **Share context**: What were you trying to do?
4. **Show attempts**: What have you already tried?

---

## Prevention

### Best Practices to Avoid Issues

1. **Commit often**: Small, frequent commits are easier to manage
2. **Pull before push**: Always pull latest changes first
3. **Use branches**: Don't work directly on main
4. **Test before commit**: Ensure code works
5. **Write clear messages**: Future you will thank you
6. **Backup important work**: Push to GitHub regularly
7. **Learn to read errors**: Error messages usually tell you what's wrong

---

*Last Updated: January 2025*
