"""
Hello World - Basic Python Script
==================================
This is a simple Python script for practicing VS Code features.
"""


def greet(name="World"):
    """
    Returns a greeting message.

    Args:
        name (str): Name to greet. Defaults to "World".

    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the program."""
    # Simple greeting
    message = greet()
    print(message)

    # Personalized greeting
    user_name = "VS Code Learner"
    personalized = greet(user_name)
    print(personalized)

    # List of names
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(greet(name))


if __name__ == "__main__":
    main()
