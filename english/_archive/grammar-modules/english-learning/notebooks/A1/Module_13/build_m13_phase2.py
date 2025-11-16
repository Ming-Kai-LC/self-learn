"""
Builder script for Module 13 Phase 2: This, That, These, Those - Controlled Practice
Target: 25-30 KB, 90-100 cells, 70+ exercises in 10 sets
"""

import json
import os


def create_cell(cell_type, content, cell_id):
    """Create a notebook cell"""
    if cell_type == "markdown":
        return {"cell_type": "markdown", "id": cell_id, "metadata": {}, "source": [content]}
    else:  # code
        return {
            "cell_type": "code",
            "execution_count": None,
            "id": cell_id,
            "metadata": {},
            "outputs": [],
            "source": [content],
        }


def build_phase2_notebook():
    """Build the complete Phase 2 notebook"""
    cells = []
    cell_counter = 0

    # Cell 0: Title and Introduction
    cells.append(
        create_cell(
            "markdown",
            """# Module 13: This, That, These, Those - Controlled Practice

## 📝 Phase 2: Controlled Practice (20% of learning time)

Welcome to the practice phase! Here you'll complete exercises with **immediate feedback** to master demonstratives.

### What You'll Do:
- [OK] Choose between THIS and THAT (singular forms)
- [OK] Choose between THESE and THOSE (plural forms)
- [OK] Practice singular vs plural forms
- [OK] Decide on near vs far distance
- [OK] Complete sentences with correct demonstratives
- [OK] Ask questions with demonstratives
- [OK] Use time expressions correctly
- [OK] Correct common mistakes
- [OK] Apply demonstratives in context

⏱️ **Estimated time:** 90-120 minutes

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 1: Setup
    cells.append(
        create_cell(
            "code",
            """# Setup
import sys
sys.path.append('../../../utils')

from feedback_system import ExerciseValidator, InteractiveExercise, create_progress_bar
from IPython.display import display, HTML

# Initialize validator and exercise system
validator = ExerciseValidator()
exercise = InteractiveExercise(validator)

print("[OK] Ready to practice! Complete all exercises below.")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 1: Choose THIS or THAT (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 1: Choose THIS or THAT (Singular Forms)

Complete each sentence with THIS or THAT based on the distance clue.

### Instructions:
- Use THIS for things near you
- Use THAT for things far from you
- Type: this or that (lowercase)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set1 = [
        ("1. ___ book in my hand is interesting. (in your hand)", "this"),
        ("2. ___ car over there is expensive. (across the street)", "that"),
        ("3. ___ pen I'm holding doesn't work. (holding it)", "this"),
        ("4. ___ building in the distance is tall. (far away)", "that"),
        ("5. ___ coffee I'm drinking is delicious. (drinking it now)", "this"),
        ("6. ___ restaurant we went to yesterday was good. (past place)", "that"),
        ("7. ___ chair I'm sitting on is comfortable. (sitting on it)", "this"),
        ("8. ___ mountain far away is beautiful. (in the distance)", "that"),
        ("9. ___ phone in my pocket is new. (in your pocket)", "this"),
        ("10. ___ house on the hill is mine. (far away on a hill)", "that"),
    ]

    for prompt, answer in exercises_set1:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 1.{exercises_set1.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 2: Choose THESE or THOSE (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 2: Choose THESE or THOSE (Plural Forms)

Complete each sentence with THESE or THOSE based on the distance clue.

### Instructions:
- Use THESE for things near you (plural)
- Use THOSE for things far from you (plural)
- Type: these or those (lowercase)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set2 = [
        ("1. ___ books on my desk are mine. (on your desk)", "these"),
        ("2. ___ cars in the parking lot are new. (far away)", "those"),
        ("3. ___ shoes I'm wearing are comfortable. (wearing them)", "these"),
        ("4. ___ people over there are tourists. (far away)", "those"),
        ("5. ___ cookies on this plate are delicious. (near you)", "these"),
        ("6. ___ buildings in the distance are tall. (far away)", "those"),
        ("7. ___ keys in my pocket are mine. (in your pocket)", "these"),
        ("8. ___ mountains we can see are beautiful. (distant)", "those"),
        ("9. ___ papers I'm holding are important. (holding them)", "these"),
        ("10. ___ houses on that street are old. (far street)", "those"),
    ]

    for prompt, answer in exercises_set2:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 2.{exercises_set2.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 3: Singular vs Plural forms (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 3: Singular vs Plural Forms

Change the demonstrative to match the number (singular ↔ plural).

### Instructions:
- THIS → THESE (singular to plural, near)
- THAT → THOSE (singular to plural, far)
- THESE → THIS (plural to singular, near)
- THOSE → THAT (plural to singular, far)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set3 = [
        ("1. This book → ___ books", "These"),
        ("2. That car → ___ cars", "Those"),
        ("3. These pens → ___ pen", "This"),
        ("4. Those houses → ___ house", "That"),
        ("5. This apple → ___ apples", "These"),
        ("6. That student → ___ students", "Those"),
        ("7. These chairs → ___ chair", "This"),
        ("8. Those flowers → ___ flower", "That"),
    ]

    for prompt, answer in exercises_set3:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 3.{exercises_set3.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 4: Near vs Far decisions (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 4: Near vs Far Distance Decisions

Read the context and choose the correct demonstrative.

### Instructions:
Choose based on whether the object is near or far from the speaker.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set4 = [
        ("1. (Pointing to a book in your hand) ___ book is mine.", "This"),
        ("2. (Pointing to a car across the street) ___ car is red.", "That"),
        ("3. (Showing photos you're holding) ___ photos are beautiful.", "These"),
        ("4. (Pointing to people in the distance) ___ people are waiting.", "Those"),
        ("5. (Holding a cup of coffee) ___ coffee is hot.", "This"),
        ("6. (Looking at a distant building) ___ building is the hospital.", "That"),
        ("7. (Touching shoes you're wearing) ___ shoes are new.", "These"),
        ("8. (Pointing to mountains far away) ___ mountains are high.", "Those"),
    ]

    for prompt, answer in exercises_set4:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 4.{exercises_set4.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 5: Complete with correct demonstrative (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 5: Complete with Correct Demonstrative

Complete each sentence with THIS, THAT, THESE, or THOSE.

### Instructions:
Consider both number (singular/plural) and distance (near/far).

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set5 = [
        ("1. ___ is my house. (pointing to a nearby house)", "This"),
        ("2. ___ are my keys. (holding them)", "These"),
        ("3. ___ was a great movie. (movie you watched yesterday)", "That"),
        ("4. ___ people over there are my friends. (far away)", "Those"),
        ("5. ___ pen doesn't work. (pen in your hand)", "This"),
        ("6. ___ were happy days. (talking about the past)", "Those"),
        ("7. ___ flowers smell nice. (flowers near you)", "These"),
        ("8. ___ building is very old. (building in the distance)", "That"),
        ("9. ___ is my favorite restaurant. (pointing to nearby restaurant)", "This"),
        ("10. ___ cars in the parking lot are new. (far away)", "Those"),
    ]

    for prompt, answer in exercises_set5:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 5.{exercises_set5.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 6: Questions with demonstratives (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 6: Questions with Demonstratives

Complete the questions with the correct demonstrative.

### Instructions:
Use the context clue to choose THIS, THAT, THESE, or THOSE.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set6 = [
        ("1. What is ___? (pointing to something in your hand)", "this"),
        ("2. What are ___? (pointing to things near you)", "these"),
        ("3. What is ___ over there? (pointing to something far)", "that"),
        ("4. Whose are ___ books? (books on your desk)", "these"),
        ("5. Whose is ___ car? (car in the distance)", "that"),
        ("6. What are ___ things? (things far away)", "those"),
        ("7. Is ___ your phone? (phone near you)", "this"),
        ("8. Are ___ your keys? (keys you're holding)", "these"),
    ]

    for prompt, answer in exercises_set6:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 6.{exercises_set6.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 7: Time expressions (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 7: Time Expressions

Complete each sentence with THIS, THAT, THESE, or THOSE for time references.

### Instructions:
- THIS/THESE for present/current time
- THAT/THOSE for past time

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set7 = [
        ("1. I'm very busy ___ week. (current week)", "this"),
        ("2. ___ day was special. (a day in the past)", "That"),
        ("3. I woke up early ___ morning. (today's morning)", "this"),
        ("4. ___ were happy times. (period in the past)", "Those"),
        ("5. ___ days I feel great. (currently)", "These"),
        ("6. I remember ___ summer very well. (past summer)", "that"),
        ("7. I have a meeting ___ afternoon. (today's afternoon)", "this"),
        ("8. ___ year has been wonderful. (current year)", "This"),
    ]

    for prompt, answer in exercises_set7:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 7.{exercises_set7.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 8: Error correction (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 8: Error Correction

Find and correct the error in each sentence.

### Instructions:
Identify the wrong demonstrative and write the correct one.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set8 = [
        ("1. Incorrect: This books are good. → Correct: ___ books are good.", "These"),
        ("2. Incorrect: That cars are expensive. → Correct: ___ cars are expensive.", "Those"),
        ("3. Incorrect: These is my pen. → Correct: ___ is my pen.", "This"),
        ("4. Incorrect: Those is interesting. → Correct: ___ is interesting.", "That"),
        (
            "5. Incorrect: This morning (yesterday) was cold. → Correct: ___ morning was cold.",
            "That",
        ),
        ("6. Incorrect: Those day was fun. → Correct: ___ day was fun.", "That"),
        ("7. Incorrect: This days I'm busy. → Correct: ___ days I'm busy.", "These"),
        ("8. Incorrect: These book is mine. → Correct: ___ book is mine.", "This"),
    ]

    for prompt, answer in exercises_set8:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 8.{exercises_set8.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 9: Multiple choice (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 9: Multiple Choice

Choose the correct demonstrative for each situation.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Multiple choice exercises
    mc_exercises = [
        (
            "___ book in my hand is interesting.",
            {"A": "This", "B": "That", "C": "These"},
            "A",
            "'This' is correct for a singular object near you.",
        ),
        (
            "___ cars over there are expensive.",
            {"A": "This", "B": "That", "C": "Those"},
            "C",
            "'Those' is correct for plural objects far away.",
        ),
        (
            "___ is my friend Sarah. (introducing someone next to you)",
            {"A": "This", "B": "That", "C": "These"},
            "A",
            "'This' is used for introductions.",
        ),
        (
            "___ were happy days. (talking about the past)",
            {"A": "This", "B": "That", "C": "Those"},
            "C",
            "'Those' refers to plural past times.",
        ),
        (
            "Hello, ___ is John speaking. (on the phone)",
            {"A": "this", "B": "that", "C": "I"},
            "A",
            "Use 'this' to identify yourself on the phone.",
        ),
        (
            "___ week has been very busy. (current week)",
            {"A": "This", "B": "That", "C": "These"},
            "A",
            "'This' refers to the current time period.",
        ),
        (
            "___ shoes I'm wearing are comfortable.",
            {"A": "This", "B": "These", "C": "Those"},
            "B",
            "'These' is correct for plural items you're wearing.",
        ),
        (
            "___ mountain in the distance is beautiful.",
            {"A": "This", "B": "These", "C": "That"},
            "C",
            "'That' is correct for a singular object far away.",
        ),
    ]

    for i, (question, options, correct, feedback) in enumerate(mc_exercises, 1):
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 9.{i}
exercise.create_multiple_choice(
    "{question}",
    {options},
    "{correct}",
    "{feedback}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 10: Context practice (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 10: Context Practice

Complete the dialogues with the correct demonstrative.

### Instructions:
Read the full context before choosing your answer.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set10 = [
        ("1. A: What is ___ in your hand? B: This is my new phone.", "this"),
        ("2. A: Look at ___ mountains! (pointing far away) B: They're beautiful!", "those"),
        ("3. A: Are ___ your keys? (keys on the table near you) B: Yes, they are.", "these"),
        ("4. A: ___ was a great party yesterday. B: Yes, it was fun!", "That"),
        ("5. A: Hello, ___ is Sarah speaking. B: Hi Sarah!", "this"),
        ("6. A: ___ building over there is my office. B: It's very modern!", "That"),
        ("7. A: ___ days I wake up early. B: That's good! (talking about currently)", "These"),
        ("8. A: How much are ___ shoes? (shoes you're holding) B: They're fifty dollars.", "these"),
    ]

    for prompt, answer in exercises_set10:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 10.{exercises_set10.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Final score display
    cells.append(
        create_cell(
            "markdown",
            """---

## 📊 Your Score""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Display final score
validator.display_score()""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # What's Next section
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

### If your score is:
- **80%+**: Excellent! Move to **03_meaningful_practice.ipynb** [OK]
- **60-79%**: Good progress! Review the demonstratives rules, then continue 👍
- **Below 60%**: Review **01_introduction.ipynb** and retry these exercises 📚

### Key Points to Remember:
- **THIS** = singular, near (This book)
- **THAT** = singular, far (That car)
- **THESE** = plural, near (These books)
- **THOSE** = plural, far (Those cars)
- Ask yourself: **How many?** and **How far?**
- **Time**: THIS/THESE = present, THAT/THOSE = past
- **Phone**: Use THIS to identify yourself
- **Verb agreement**: This/That IS, These/Those ARE

---

### Continue to:
**03_meaningful_practice.ipynb** - Personal activities using demonstratives!

---

**Great work!** 🌟 You've completed the controlled practice phase!""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.8.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    return notebook


def main():
    """Main function to build and save the notebook"""
    # Build the notebook
    notebook = build_phase2_notebook()

    # Define output path
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "02_controlled_practice.ipynb")

    # Save the notebook
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    # Get file size
    file_size = os.path.getsize(output_file)
    file_size_kb = file_size / 1024

    print(f"[OK] Phase 2 notebook created successfully!")
    print(f"📁 Location: {output_file}")
    print(f"📊 File size: {file_size_kb:.2f} KB")
    print(f"📝 Total cells: {len(notebook['cells'])}")

    # Check if size is within target range
    if 25 <= file_size_kb <= 30:
        print("[OK] File size is within target range (25-30 KB)")
    else:
        print(
            f"Warning: File size is outside target range. Target: 25-30 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
