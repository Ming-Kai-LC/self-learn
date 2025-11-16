"""
VS Code Extension Recommender
==============================
Recommend extensions based on your development needs.
"""


class ExtensionRecommender:
    """Recommend VS Code extensions for different use cases."""

    def __init__(self):
        self.extensions = {
            "python": [
                {
                    "name": "Python",
                    "id": "ms-python.python",
                    "description": "Python language support with IntelliSense, linting, debugging",
                    "essential": True,
                },
                {
                    "name": "Pylance",
                    "id": "ms-python.vscode-pylance",
                    "description": "Fast, feature-rich Python language support",
                    "essential": True,
                },
                {
                    "name": "Jupyter",
                    "id": "ms-toolsai.jupyter",
                    "description": "Jupyter notebook support",
                    "essential": False,
                },
                {
                    "name": "Python Docstring Generator",
                    "id": "njpwerner.autodocstring",
                    "description": "Automatically generate docstrings",
                    "essential": False,
                },
            ],
            "web": [
                {
                    "name": "ESLint",
                    "id": "dbaeumer.vscode-eslint",
                    "description": "JavaScript linting",
                    "essential": True,
                },
                {
                    "name": "Prettier",
                    "id": "esbenp.prettier-vscode",
                    "description": "Code formatter",
                    "essential": True,
                },
                {
                    "name": "Live Server",
                    "id": "ritwickdey.liveserver",
                    "description": "Launch local development server with live reload",
                    "essential": False,
                },
                {
                    "name": "Auto Rename Tag",
                    "id": "formulahendry.auto-rename-tag",
                    "description": "Automatically rename paired HTML/XML tags",
                    "essential": False,
                },
            ],
            "general": [
                {
                    "name": "GitLens",
                    "id": "eamodio.gitlens",
                    "description": "Enhanced Git capabilities",
                    "essential": True,
                },
                {
                    "name": "Path Intellisense",
                    "id": "christian-kohler.path-intellisense",
                    "description": "Autocomplete filenames",
                    "essential": False,
                },
                {
                    "name": "Bracket Pair Colorizer",
                    "id": "coenraads.bracket-pair-colorizer-2",
                    "description": "Color matching brackets",
                    "essential": False,
                },
                {
                    "name": "TODO Highlight",
                    "id": "wayou.vscode-todo-highlight",
                    "description": "Highlight TODO, FIXME comments",
                    "essential": False,
                },
            ],
            "themes": [
                {
                    "name": "One Dark Pro",
                    "id": "zhuangtongfa.material-theme",
                    "description": "Atom's iconic One Dark theme",
                    "essential": False,
                },
                {
                    "name": "Material Icon Theme",
                    "id": "pkief.material-icon-theme",
                    "description": "Material Design icons",
                    "essential": False,
                },
                {
                    "name": "Dracula Official",
                    "id": "dracula-theme.theme-dracula",
                    "description": "Dark theme based on Dracula",
                    "essential": False,
                },
            ],
        }

    def recommend_for_category(self, category):
        """Recommend extensions for a specific category."""
        if category not in self.extensions:
            print(f"Unknown category: {category}")
            return

        print(f"\n{category.upper()} Development Extensions")
        print("=" * 60)

        extensions = self.extensions[category]
        for ext in extensions:
            essential = " [ESSENTIAL]" if ext["essential"] else ""
            print(f"\n{ext['name']}{essential}")
            print(f"ID: {ext['id']}")
            print(f"Description: {ext['description']}")

    def generate_install_command(self, category):
        """Generate command to install all essential extensions."""
        if category not in self.extensions:
            return

        essential_exts = [ext["id"] for ext in self.extensions[category] if ext["essential"]]

        if essential_exts:
            print(f"\n\nInstall command for essential {category} extensions:")
            print("-" * 60)
            for ext_id in essential_exts:
                print(f"code --install-extension {ext_id}")

    def recommend_all(self):
        """Recommend extensions for all categories."""
        for category in self.extensions.keys():
            self.recommend_for_category(category)
            print("\n" + "=" * 60)


def main():
    """Main function."""
    recommender = ExtensionRecommender()

    print("VS Code Extension Recommender")
    print("=" * 60)
    print("\n1. Python Development")
    print("2. Web Development")
    print("3. General Productivity")
    print("4. Themes")
    print("5. Show All")
    print("6. Generate Install Commands")

    choice = input("\nSelect an option (1-6): ")

    category_map = {"1": "python", "2": "web", "3": "general", "4": "themes"}

    if choice in category_map:
        category = category_map[choice]
        recommender.recommend_for_category(category)
        recommender.generate_install_command(category)
    elif choice == "5":
        recommender.recommend_all()
    elif choice == "6":
        print("\nGenerate install commands for which category?")
        print("1. Python  2. Web  3. General  4. All")
        sub_choice = input("Choice: ")
        if sub_choice in category_map:
            recommender.generate_install_command(category_map[sub_choice])
        elif sub_choice == "4":
            for cat in category_map.values():
                if cat != "themes":
                    recommender.generate_install_command(cat)
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
