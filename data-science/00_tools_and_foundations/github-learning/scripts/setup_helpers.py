#!/usr/bin/env python3
"""
Git and GitHub Learning - Setup Helper Script

This script provides utilities to help set up and configure Git for the course.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, capture_output=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=capture_output, text=True, check=False
        )
        return result
    except Exception as e:
        print(f"Error running command: {e}")
        return None


def check_git_installed():
    """Check if Git is installed."""
    print("Checking Git installation...")
    result = run_command("git --version")
    if result and result.returncode == 0:
        print(f"✓ Git is installed: {result.stdout.strip()}")
        return True
    else:
        print("✗ Git is not installed or not in PATH")
        print("Please install Git from: https://git-scm.com/downloads")
        return False


def check_git_config():
    """Check if Git user configuration is set."""
    print("\nChecking Git configuration...")

    # Check user.name
    result = run_command("git config --global user.name")
    if result and result.stdout.strip():
        print(f"✓ user.name: {result.stdout.strip()}")
        name_configured = True
    else:
        print("✗ user.name is not configured")
        name_configured = False

    # Check user.email
    result = run_command("git config --global user.email")
    if result and result.stdout.strip():
        print(f"✓ user.email: {result.stdout.strip()}")
        email_configured = True
    else:
        print("✗ user.email is not configured")
        email_configured = False

    return name_configured and email_configured


def configure_git():
    """Interactive Git configuration."""
    print("\n" + "=" * 60)
    print("GIT CONFIGURATION SETUP")
    print("=" * 60)

    print("\nThis will configure your Git user information.")
    print("This information will be attached to your commits.")

    # Get user name
    current_name = run_command("git config --global user.name")
    if current_name and current_name.stdout.strip():
        default_name = current_name.stdout.strip()
        print(f"\nCurrent name: {default_name}")
        name = input(f"Enter your name (press Enter to keep current): ").strip()
        if not name:
            name = default_name
    else:
        name = input("\nEnter your name: ").strip()

    # Get user email
    current_email = run_command("git config --global user.email")
    if current_email and current_email.stdout.strip():
        default_email = current_email.stdout.strip()
        print(f"Current email: {default_email}")
        email = input(f"Enter your email (press Enter to keep current): ").strip()
        if not email:
            email = default_email
    else:
        email = input("Enter your email: ").strip()

    # Set configuration
    if name:
        run_command(f'git config --global user.name "{name}"')
        print(f"✓ Set user.name to: {name}")

    if email:
        run_command(f'git config --global user.email "{email}"')
        print(f"✓ Set user.email to: {email}")

    # Set other useful defaults
    print("\nSetting recommended Git defaults...")
    run_command("git config --global init.defaultBranch main")
    print("✓ Set default branch name to 'main'")

    run_command("git config --global color.ui auto")
    print("✓ Enabled colored output")

    run_command("git config --global pull.rebase false")
    print("✓ Set pull strategy to merge (safer for beginners)")

    print("\n✓ Git configuration complete!")


def check_ssh_keys():
    """Check if SSH keys exist."""
    print("\nChecking SSH keys...")
    ssh_dir = Path.home() / ".ssh"

    if not ssh_dir.exists():
        print("✗ No .ssh directory found")
        return False

    key_files = ["id_ed25519", "id_rsa", "id_ecdsa"]
    found_keys = []

    for key_file in key_files:
        key_path = ssh_dir / key_file
        if key_path.exists():
            found_keys.append(key_file)

    if found_keys:
        print(f"✓ Found SSH keys: {', '.join(found_keys)}")
        return True
    else:
        print("✗ No SSH keys found")
        print("You can generate one with:")
        print('  ssh-keygen -t ed25519 -C "your.email@example.com"')
        return False


def test_github_connection():
    """Test SSH connection to GitHub."""
    print("\nTesting GitHub SSH connection...")
    result = run_command("ssh -T git@github.com")

    if result:
        # GitHub returns exit code 1 for successful auth (no shell access)
        if "successfully authenticated" in result.stderr.lower():
            print("✓ Successfully authenticated with GitHub via SSH")
            return True
        else:
            print("✗ Could not authenticate with GitHub")
            print("Make sure you've:")
            print("  1. Generated an SSH key")
            print("  2. Added it to your GitHub account")
            print("  3. Started ssh-agent and added your key")
            return False
    return False


def check_python_packages():
    """Check if required Python packages are installed."""
    print("\nChecking Python packages...")

    required_packages = [
        "jupyter",
        "notebook",
        "git",  # GitPython
        "github",  # PyGithub
        "pandas",
        "matplotlib",
    ]

    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package:20s} - installed")
        except ImportError:
            print(f"✗ {package:20s} - NOT INSTALLED")
            missing_packages.append(package)

    if missing_packages:
        print(f"\n✗ Missing packages: {', '.join(missing_packages)}")
        print("Install with: pip install -r requirements.txt")
        return False
    else:
        print("\n✓ All required packages are installed!")
        return True


def display_git_config():
    """Display current Git configuration."""
    print("\n" + "=" * 60)
    print("CURRENT GIT CONFIGURATION")
    print("=" * 60)
    result = run_command("git config --global --list")
    if result:
        print(result.stdout)


def setup_sample_repo():
    """Create a sample repository for practice."""
    print("\n" + "=" * 60)
    print("CREATE SAMPLE PRACTICE REPOSITORY")
    print("=" * 60)

    repo_path = Path("practice_repo")

    if repo_path.exists():
        print(f"\n✗ Directory '{repo_path}' already exists")
        overwrite = input("Delete and recreate? (y/n): ").strip().lower()
        if overwrite == "y":
            import shutil

            shutil.rmtree(repo_path)
        else:
            print("Cancelled.")
            return

    # Create directory
    repo_path.mkdir()
    print(f"✓ Created directory: {repo_path}")

    # Initialize Git
    os.chdir(repo_path)
    run_command("git init")
    print("✓ Initialized Git repository")

    # Create sample files
    with open("README.md", "w") as f:
        f.write("# Practice Repository\n\nThis is a practice repository for learning Git.\n")
    print("✓ Created README.md")

    with open(".gitignore", "w") as f:
        f.write("# Python\n__pycache__/\n*.pyc\n*.pyo\n\n# Virtual environments\nvenv/\nenv/\n")
    print("✓ Created .gitignore")

    with open("hello.py", "w") as f:
        f.write('#!/usr/bin/env python3\n\nprint("Hello, Git!")\n')
    print("✓ Created hello.py")

    # Make initial commit
    run_command("git add .")
    run_command('git commit -m "Initial commit: Add README, .gitignore, and hello.py"')
    print("✓ Made initial commit")

    os.chdir("..")
    print(f"\n✓ Sample repository created at: {repo_path.absolute()}")
    print("\nTo use it:")
    print(f"  cd {repo_path}")
    print("  git log")
    print("  git status")


def main():
    """Main function."""
    print("=" * 60)
    print("GIT & GITHUB LEARNING - SETUP HELPER")
    print("=" * 60)

    while True:
        print("\nWhat would you like to do?")
        print("1. Check system setup (Git, Python packages)")
        print("2. Configure Git (name, email, defaults)")
        print("3. Check SSH keys")
        print("4. Test GitHub connection")
        print("5. Display current Git configuration")
        print("6. Create sample practice repository")
        print("7. Run all checks")
        print("8. Exit")

        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            git_ok = check_git_installed()
            if git_ok:
                check_git_config()
            check_python_packages()

        elif choice == "2":
            if check_git_installed():
                configure_git()

        elif choice == "3":
            check_ssh_keys()

        elif choice == "4":
            test_github_connection()

        elif choice == "5":
            display_git_config()

        elif choice == "6":
            setup_sample_repo()

        elif choice == "7":
            print("\nRunning all checks...\n")
            git_ok = check_git_installed()
            if git_ok:
                check_git_config()
            check_ssh_keys()
            test_github_connection()
            check_python_packages()

        elif choice == "8":
            print("\nGoodbye! Happy learning!")
            sys.exit(0)

        else:
            print("\n✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        sys.exit(0)
