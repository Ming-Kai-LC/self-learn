"""
VS Code Settings Generator
===========================
Generate common VS Code settings.json configurations for different use cases.
"""

import json
import os


class SettingsGenerator:
    """Generate VS Code settings configurations."""

    def __init__(self):
        self.base_settings = {
            "editor.fontSize": 14,
            "editor.tabSize": 4,
            "files.autoSave": "afterDelay",
            "files.trimTrailingWhitespace": True,
            "files.insertFinalNewline": True,
        }

    def generate_python_settings(self):
        """Generate settings optimized for Python development."""
        settings = self.base_settings.copy()
        settings.update(
            {
                "python.linting.enabled": True,
                "python.linting.pylintEnabled": True,
                "python.formatting.provider": "black",
                "python.analysis.typeCheckingMode": "basic",
                "[python]": {
                    "editor.formatOnSave": True,
                    "editor.codeActionsOnSave": {"source.organizeImports": "explicit"},
                },
            }
        )
        return settings

    def generate_web_dev_settings(self):
        """Generate settings for web development."""
        settings = self.base_settings.copy()
        settings.update(
            {
                "emmet.includeLanguages": {"javascript": "javascriptreact"},
                "[javascript]": {
                    "editor.formatOnSave": True,
                    "editor.defaultFormatter": "esbenp.prettier-vscode",
                },
                "[html]": {
                    "editor.formatOnSave": True,
                    "editor.defaultFormatter": "vscode.html-language-features",
                },
                "[css]": {"editor.formatOnSave": True},
            }
        )
        return settings

    def generate_minimal_settings(self):
        """Generate minimal distraction-free settings."""
        return {
            "editor.fontSize": 16,
            "editor.lineNumbers": "on",
            "workbench.statusBar.visible": True,
            "workbench.activityBar.visible": False,
            "editor.minimap.enabled": False,
            "breadcrumbs.enabled": False,
            "editor.renderWhitespace": "none",
        }

    def save_settings(self, settings, filename):
        """Save settings to a JSON file."""
        output_dir = "../sample_workspace/outputs"
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            json.dump(settings, f, indent=4)

        print(f"Settings saved to: {filepath}")


def main():
    """Main function to generate settings."""
    generator = SettingsGenerator()

    print("VS Code Settings Generator")
    print("=" * 50)
    print("\n1. Python Development Settings")
    print("2. Web Development Settings")
    print("3. Minimal Settings")
    print("4. Generate All")

    choice = input("\nSelect an option (1-4): ")

    if choice == "1":
        settings = generator.generate_python_settings()
        generator.save_settings(settings, "python_settings.json")
    elif choice == "2":
        settings = generator.generate_web_dev_settings()
        generator.save_settings(settings, "web_dev_settings.json")
    elif choice == "3":
        settings = generator.generate_minimal_settings()
        generator.save_settings(settings, "minimal_settings.json")
    elif choice == "4":
        generator.save_settings(generator.generate_python_settings(), "python_settings.json")
        generator.save_settings(generator.generate_web_dev_settings(), "web_dev_settings.json")
        generator.save_settings(generator.generate_minimal_settings(), "minimal_settings.json")
        print("\nAll settings files generated!")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
