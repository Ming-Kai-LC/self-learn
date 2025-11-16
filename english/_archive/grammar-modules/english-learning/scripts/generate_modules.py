"""
Module Generation Script for English Learning Notebooks
Generates A1 modules 2-10 with consistent structure
"""

import json
import os
from pathlib import Path

# Module definitions with specific content
MODULES = {
    "Module_02": {
        "title": "Personal Pronouns",
        "subtitle": "Subject and Object Pronouns",
        "time": "6-8 hours",
        "description": "Master subject pronouns (I, you, he, she, it, we, they) and object pronouns (me, you, him, her, it, us, them)",
        "key_points": [
            "Subject pronouns (I, you, he, she, it, we, they)",
            "Object pronouns (me, you, him, her, it, us, them)",
            "When to use subject vs object pronouns",
            "Pronoun-verb agreement",
            "Using pronouns in sentences",
        ],
        "examples": [
            ("I love pizza.", "Subject pronoun: I"),
            ("She likes coffee.", "Subject pronoun: She"),
            ("Give it to me.", "Object pronoun: me"),
            ("We know them.", "Subject: We, Object: them"),
        ],
    },
    "Module_03": {
        "title": "Present Simple - Affirmative",
        "subtitle": "Positive Statements and Third-Person -s",
        "time": "10-15 hours",
        "description": "Learn to form positive statements in Present Simple tense, with special focus on third-person -s",
        "key_points": [
            "Present Simple formation for all persons",
            "Third-person -s (he/she/it walks)",
            "Spelling rules for -s/-es/-ies",
            "When to use Present Simple (habits, facts, routines)",
            "Adverbs of frequency with Present Simple",
        ],
        "examples": [
            ("I work in an office.", "First person"),
            ("You play football.", "Second person"),
            ("He walks to school.", "Third person -s"),
            ("She studies English.", "Third person -ies"),
            ("They live in Paris.", "Plural"),
        ],
    },
    "Module_04": {
        "title": "Present Simple - Negatives and Questions",
        "subtitle": "Using Do/Does for Questions and Negatives",
        "time": "8-10 hours",
        "description": "Learn to form negative sentences and questions in Present Simple using do/does",
        "key_points": [
            "Negatives with don't/doesn't",
            "Questions with Do/Does",
            "Word order in questions",
            "Short answers (Yes, I do / No, I don't)",
            "Wh-questions (What do you...?)",
        ],
        "examples": [
            ("I don't like coffee.", "Negative with don't"),
            ("She doesn't work here.", "Negative with doesn't"),
            ("Do you speak English?", "Yes/No question"),
            ("Does he live in Tokyo?", "Third person question"),
            ("Where do they work?", "Wh-question"),
        ],
    },
    "Module_05": {
        "title": "Articles and Demonstratives",
        "subtitle": "A/An, The, This/That/These/Those",
        "time": "6-8 hours",
        "description": "Master the use of indefinite articles (a/an), definite article (the), and demonstratives",
        "key_points": [
            "A vs An (a book, an apple)",
            "When to use 'the'",
            "This/that for singular (near/far)",
            "These/those for plural (near/far)",
            "Zero article (no article needed)",
        ],
        "examples": [
            ("I have a car.", "Indefinite article a"),
            ("She eats an orange.", "Indefinite article an"),
            ("The sun is bright.", "Definite article"),
            ("This book is interesting.", "Near singular"),
            ("Those trees are tall.", "Far plural"),
        ],
    },
    "Module_06": {
        "title": "Nouns and Plurals",
        "subtitle": "Regular and Irregular Plural Forms",
        "time": "6-8 hours",
        "description": "Learn to form plural nouns, both regular (-s/-es) and irregular forms",
        "key_points": [
            "Regular plurals (-s: cats, dogs)",
            "Plurals with -es (box→boxes, dish→dishes)",
            "Plurals with -ies (city→cities)",
            "Irregular plurals (man→men, child→children)",
            "Countable vs uncountable nouns",
        ],
        "examples": [
            ("One cat, two cats", "Regular plural"),
            ("One box, two boxes", "Plural -es"),
            ("One city, two cities", "Plural -ies"),
            ("One child, two children", "Irregular"),
            ("Water is uncountable", "No plural form"),
        ],
    },
    "Module_07": {
        "title": "Possessives",
        "subtitle": "Possessive Adjectives and 's",
        "time": "5-7 hours",
        "description": "Learn to show possession using possessive adjectives and possessive 's",
        "key_points": [
            "Possessive adjectives (my, your, his, her, its, our, their)",
            "Possessive 's (John's book)",
            "Possessive with plural nouns (the students' books)",
            "Whose...? questions",
            "Its vs It's distinction",
        ],
        "examples": [
            ("This is my book.", "Possessive adjective"),
            ("That's John's car.", "Possessive 's"),
            ("Her name is Sarah.", "Possessive adjective"),
            ("The teachers' room", "Plural possessive"),
            ("Whose pen is this?", "Question"),
        ],
    },
    "Module_08": {
        "title": "Adjectives",
        "subtitle": "Describing People, Places, and Things",
        "time": "5-7 hours",
        "description": "Learn to use adjectives before nouns and after 'be' to describe things",
        "key_points": [
            "Adjectives before nouns (a big house)",
            "Adjectives after 'be' (She is happy)",
            "Common opposites (big/small, hot/cold)",
            "Color adjectives",
            "Basic adjective order",
        ],
        "examples": [
            ("A beautiful garden", "Adjective before noun"),
            ("The car is red.", "Adjective after 'be'"),
            ("She is tall.", "Describing person"),
            ("It's a cold day.", "Describing weather"),
            ("They are happy.", "Describing feeling"),
        ],
    },
    "Module_09": {
        "title": "There Is / There Are",
        "subtitle": "Expressing Existence and Location",
        "time": "5-7 hours",
        "description": "Learn to use 'there is' and 'there are' to talk about existence and location",
        "key_points": [
            "There is for singular",
            "There are for plural",
            "Questions: Is there...? / Are there...?",
            "Negatives: There isn't / There aren't",
            "Using with prepositions of place",
        ],
        "examples": [
            ("There is a book on the table.", "Singular"),
            ("There are three chairs.", "Plural"),
            ("Is there a bank nearby?", "Question"),
            ("There aren't any apples.", "Negative"),
            ("There's a cat under the bed.", "With preposition"),
        ],
    },
    "Module_10": {
        "title": "Prepositions of Place and Time",
        "subtitle": "In, On, At for Location and Time",
        "time": "6-8 hours",
        "description": "Master basic prepositions to describe location and time",
        "key_points": [
            "In/on/at for place (in the room, on the table, at home)",
            "In/on/at for time (in May, on Monday, at 3pm)",
            "Other place prepositions (under, behind, next to, between)",
            "Common expressions with prepositions",
            "Preposition usage rules",
        ],
        "examples": [
            ("The book is on the table.", "Place"),
            ("I live in London.", "Place - city"),
            ("The meeting is at 5 o'clock.", "Time"),
            ("My birthday is in June.", "Time - month"),
            ("The cat is under the chair.", "Place"),
        ],
    },
}


def create_introduction_notebook(module_num, module_data):
    """Create Phase 1: Introduction notebook"""

    examples_md = "\n\n".join(
        [
            f"### Example {i+1}: {example}\n**{note}**"
            for i, (example, note) in enumerate(module_data["examples"])
        ]
    )

    key_points_md = "\n".join([f"- {point}" for point in module_data["key_points"]])

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Module {module_num[7:]}: {module_data['title']} - Introduction\n\n"
                    f"## 📚 Phase 1: Introduction (15% of learning time)\n\n"
                    f"**{module_data['subtitle']}**\n\n"
                    f"### Learning Objectives\n\n"
                    f"{key_points_md}\n\n"
                    f"### Time Requirement\n"
                    f"⏱️ Estimated time: {module_data['time']}\n\n"
                    f"---"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Setup: Import utilities\n"
                    "import sys\n"
                    "sys.path.append('../../../utils')\n\n"
                    "from audio_generator import AudioGenerator, create_pronunciation_guide\n"
                    "from IPython.display import display, HTML\n\n"
                    'audio = AudioGenerator(audio_dir="audio")\n'
                    'print("✅ Setup complete!")'
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## What You'll Learn\n\n"
                    f"{module_data['description']}\n\n"
                    f"---\n\n"
                    f"## Key Concepts\n\n"
                    f"{key_points_md}\n\n"
                    f"---\n\n"
                    f"## Examples\n\n"
                    f"{examples_md}\n\n"
                    f"---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 What's Next?\n\n"
                    "Continue to **02_controlled_practice.ipynb** for exercises!\n\n"
                    "---"
                ],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def create_controlled_practice_notebook(module_num, module_data):
    """Create Phase 2: Controlled Practice notebook"""

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Module {module_num[7:]}: {module_data['title']} - Controlled Practice\n\n"
                    f"## 📝 Phase 2: Controlled Practice (20% of learning time)\n\n"
                    f"Complete exercises with immediate feedback.\n\n"
                    f"⏱️ **Estimated time:** 90-120 minutes\n\n"
                    f"---"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Setup\n"
                    "import sys\n"
                    "sys.path.append('../../../utils')\n\n"
                    "from feedback_system import ExerciseValidator, InteractiveExercise\n"
                    "from IPython.display import display, HTML\n\n"
                    "validator = ExerciseValidator()\n"
                    "exercise = InteractiveExercise(validator)\n"
                    'print("✅ Ready to practice!")'
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Exercise Set 1: Fill in the Blank\n\n"
                    "Complete these exercises using the grammar you learned.\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "*Note: In a full implementation, this would contain 20-30 interactive exercises*\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# Display score\n" "validator.display_score()"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 What's Next?\n\n"
                    "Continue to **03_meaningful_practice.ipynb**\n\n"
                    "---"
                ],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def create_meaningful_practice_notebook(module_num, module_data):
    """Create Phase 3: Meaningful Practice notebook"""

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Module {module_num[7:]}: {module_data['title']} - Meaningful Practice\n\n"
                    f"## 🎨 Phase 3: Meaningful Practice (25% of learning time)\n\n"
                    f"Use {module_data['title'].lower()} to talk about YOUR life!\n\n"
                    f"⏱️ **Estimated time:** 2-3 hours\n\n"
                    f"---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Activity 1: About You\n\n"
                    "Write sentences about yourself using the grammar from this module.\n\n"
                    "**Double-click to edit and write your answers!**\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Activity 2: Personalized Exercises\n\n"
                    "*Create your own examples and practice!*\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 What's Next?\n\n"
                    "Continue to **04_communicative_practice.ipynb**\n\n"
                    "---"
                ],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def create_communicative_practice_notebook(module_num, module_data):
    """Create Phase 4: Communicative Practice notebook"""

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Module {module_num[7:]}: {module_data['title']} - Communicative Practice\n\n"
                    f"## 💬 Phase 4: Communicative Practice (30% of learning time)\n\n"
                    f"Use {module_data['title'].lower()} in real communication!\n\n"
                    f"⏱️ **Estimated time:** 2-3 hours\n\n"
                    f"---"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Setup\n"
                    "import sys\n"
                    "sys.path.append('../../../utils')\n\n"
                    "from spaced_repetition import SpacedRepetitionScheduler\n"
                    'scheduler = SpacedRepetitionScheduler(data_file="../../../data/progress.json")\n'
                    'print("✅ Ready for communication!")'
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Task 1: Role-Play\n\n"
                    "Practice real conversations using this grammar.\n\n"
                    "**Double-click to write!**\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Task 2: Creative Writing\n\n"
                    "Write a story or description using the grammar.\n\n"
                    "---"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Mark module complete (uncomment when finished)\n"
                    f"# scheduler.mark_module_complete(\n"
                    f'#     module_id="A1_{module_num}",\n'
                    f"#     module_name=\"{module_data['title']}\",\n"
                    f"#     score=85.0\n"
                    f"# )"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 Module Complete!\n\n"
                    f"Great job! You've finished Module {module_num[7:]}: {module_data['title']}\n\n"
                    "Continue to the next module!\n\n"
                    "---"
                ],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def generate_module(module_num, module_data, base_path):
    """Generate all 4 phases for a module"""
    module_path = Path(base_path) / "notebooks" / "A1" / module_num
    module_path.mkdir(parents=True, exist_ok=True)

    # Create audio directory
    (module_path / "audio").mkdir(exist_ok=True)

    # Generate all 4 notebooks
    notebooks = {
        "01_introduction.ipynb": create_introduction_notebook(module_num, module_data),
        "02_controlled_practice.ipynb": create_controlled_practice_notebook(
            module_num, module_data
        ),
        "03_meaningful_practice.ipynb": create_meaningful_practice_notebook(
            module_num, module_data
        ),
        "04_communicative_practice.ipynb": create_communicative_practice_notebook(
            module_num, module_data
        ),
    }

    for filename, notebook in notebooks.items():
        filepath = module_path / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)

    print(f"Generated {module_num}: {module_data['title']}")


def main():
    """Generate all modules 2-10"""
    base_path = Path(__file__).parent

    print("Generating English Learning Modules 2-10...\n")

    for module_num, module_data in MODULES.items():
        generate_module(module_num, module_data, base_path)

    print(f"\nAll modules generated successfully!")
    print(f"Location: {base_path / 'notebooks' / 'A1'}")


if __name__ == "__main__":
    main()
