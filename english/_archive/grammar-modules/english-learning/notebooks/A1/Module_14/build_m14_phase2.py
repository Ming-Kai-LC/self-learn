"""
Builder script for Module 14 Phase 2: Like/Love/Hate + -ing - Controlled Practice
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
            """# Module 14: Like, Love, Hate + -ing - Controlled Practice

## 📝 Phase 2: Controlled Practice (20% of learning time)

Welcome to the practice phase! Here you'll complete exercises with **immediate feedback** to master expressing preferences with -ing verbs.

### What You'll Do:
- [OK] Add -ing to verbs correctly (spelling practice)
- [OK] Use LIKE + -ing in sentences
- [OK] Use LOVE + -ing in sentences
- [OK] Use HATE + -ing in sentences
- [OK] Practice with mixed preference verbs
- [OK] Create negative sentences
- [OK] Form questions correctly
- [OK] Choose between preference verbs
- [OK] Correct common errors
- [OK] Complete sentences in context

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

    # Exercise Set 1: Add -ing to verbs correctly (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 1: Add -ing to Verbs Correctly (Spelling Rules)

Add -ing to each verb following the correct spelling rules.

### Instructions:
- Apply the spelling rules from Phase 1
- Type the complete -ing form (e.g., "reading", "running")

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set1 = [
        ("1. read → ___", "reading"),
        ("2. make → ___ (drop e)", "making"),
        ("3. run → ___ (double n)", "running"),
        ("4. watch → ___", "watching"),
        ("5. dance → ___ (drop e)", "dancing"),
        ("6. swim → ___ (double m)", "swimming"),
        ("7. play → ___", "playing"),
        ("8. write → ___ (drop e)", "writing"),
        ("9. sit → ___ (double t)", "sitting"),
        ("10. listen → ___", "listening"),
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

    # Exercise Set 2: LIKE + -ing sentences (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 2: LIKE + -ing Sentences

Complete each sentence with LIKE/LIKES + the -ing form of the verb in parentheses.

### Instructions:
- Use "like" or "likes" depending on the subject
- Add the verb in -ing form
- Example: She ___ (read) books. → She likes reading books.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set2 = [
        ("1. I ___ (watch) movies on weekends.", "like watching"),
        ("2. She ___ (read) mystery novels.", "likes reading"),
        ("3. They ___ (play) football after school.", "like playing"),
        ("4. He ___ (cook) Italian food.", "likes cooking"),
        ("5. We ___ (listen) to music in the car.", "like listening"),
        ("6. Sarah ___ (swim) in the ocean.", "likes swimming"),
        ("7. You ___ (spend) time with friends.", "like spending"),
        ("8. My brother ___ (play) video games.", "likes playing"),
        ("9. I ___ (walk) in the park.", "like walking"),
        ("10. My parents ___ (travel) abroad.", "like traveling"),
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

    # Exercise Set 3: LOVE + -ing sentences (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 3: LOVE + -ing Sentences

Complete each sentence with LOVE/LOVES + the -ing form of the verb.

### Instructions:
- Use "love" or "loves" depending on the subject
- Add the verb in -ing form

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set3 = [
        ("1. I ___ (dance) at parties!", "love dancing"),
        ("2. She ___ (sing) in the shower.", "loves singing"),
        ("3. They ___ (eat) at new restaurants.", "love eating"),
        ("4. He ___ (run) in the morning.", "loves running"),
        ("5. We ___ (watch) the sunset.", "love watching"),
        ("6. Maria ___ (paint) landscapes.", "loves painting"),
        ("7. I ___ (learn) new languages.", "love learning"),
        ("8. My sister ___ (bake) cakes.", "loves baking"),
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

    # Exercise Set 4: HATE + -ing sentences (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 4: HATE + -ing Sentences

Complete each sentence with HATE/HATES + the -ing form of the verb.

### Instructions:
- Use "hate" or "hates" depending on the subject
- Add the verb in -ing form

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set4 = [
        ("1. I ___ (wait) in long lines.", "hate waiting"),
        ("2. She ___ (wake) up early on Mondays.", "hates waking"),
        ("3. They ___ (clean) the house.", "hate cleaning"),
        ("4. He ___ (do) homework.", "hates doing"),
        ("5. We ___ (be) late for meetings.", "hate being"),
        ("6. Tom ___ (wash) dishes.", "hates washing"),
        ("7. I ___ (sit) in traffic.", "hate sitting"),
        ("8. My roommate ___ (iron) clothes.", "hates ironing"),
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

    # Exercise Set 5: Mixed preference verbs (10 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 5: Mixed Preference Verbs

Complete with the correct form: ENJOY/ENJOYS, PREFER/PREFERS, or DON'T MIND/DOESN'T MIND + -ing.

### Instructions:
- Read the context to choose the right verb
- Use correct subject-verb agreement
- Add -ing form

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set5 = [
        ("1. I ___ (read) before bed. [neutral, willing]", "don't mind reading"),
        ("2. She ___ (swim) to running. [comparison]", "prefers swimming"),
        ("3. They ___ (cook) together. [active pleasure]", "enjoy cooking"),
        ("4. He ___ (help) with housework. [neutral]", "doesn't mind helping"),
        ("5. We ___ (walk) to driving. [comparison]", "prefer walking"),
        ("6. Sarah ___ (play) tennis. [active pleasure]", "enjoys playing"),
        ("7. I ___ (work) late occasionally. [neutral]", "don't mind working"),
        ("8. My friends ___ (go) to concerts. [active pleasure]", "enjoy going"),
        ("9. She ___ (stay) home to going out. [comparison]", "prefers staying"),
        ("10. They ___ (wait) a few minutes. [neutral]", "don't mind waiting"),
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

    # Exercise Set 6: Negative forms (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 6: Negative Forms

Rewrite each sentence in the negative form using DON'T or DOESN'T.

### Instructions:
- Use don't/doesn't + verb + -ing
- Keep the -ing form after the verb

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set6 = [
        ("1. I like running. → I ___ running.", "don't like"),
        ("2. She loves cooking. → She ___ cooking.", "doesn't love"),
        ("3. They enjoy swimming. → They ___ swimming.", "don't enjoy"),
        ("4. He likes waiting. → He ___ waiting.", "doesn't like"),
        ("5. We love dancing. → We ___ dancing.", "don't love"),
        ("6. Maria enjoys studying. → Maria ___ studying.", "doesn't enjoy"),
        ("7. I like cleaning. → I ___ cleaning.", "don't like"),
        ("8. They love shopping. → They ___ shopping.", "don't love"),
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

    # Exercise Set 7: Questions formation (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 7: Questions Formation

Form questions using the words provided.

### Instructions:
- Start with Do or Does
- Use correct word order
- Keep -ing form

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set7 = [
        ("1. you / like / read / books? → ___", "Do you like reading books?"),
        ("2. she / love / dance? → ___", "Does she love dancing?"),
        ("3. they / enjoy / cook? → ___", "Do they enjoy cooking?"),
        ("4. he / hate / wait? → ___", "Does he hate waiting?"),
        ("5. you / prefer / walk / or / drive? → ___", "Do you prefer walking or driving?"),
        ("6. she / like / swim? → ___", "Does she like swimming?"),
        ("7. they / mind / help? → ___", "Do they mind helping?"),
        ("8. he / enjoy / travel? → ___", "Does he enjoy traveling?"),
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

    # Exercise Set 8: Choose correct form (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 8: Choose the Correct Form

Choose the correct preference verb for each situation.

### Instructions:
- Read the context carefully
- Choose: like, love, hate, enjoy, prefer, or don't mind

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set8 = [
        ("1. I really, really enjoy this! I ___ doing it! [very strong positive]", "love"),
        ("2. It's okay with me. I ___ doing it. [neutral]", "don't mind"),
        ("3. I think it's nice. I ___ doing it. [positive]", "like"),
        ("4. I really dislike this! I ___ doing it! [very strong negative]", "hate"),
        ("5. I get active pleasure from this. I ___ doing it. [active enjoyment]", "enjoy"),
        ("6. Between two options, I choose this one. I ___ this to that. [comparison]", "prefer"),
        ("7. This is terrible! I absolutely ___ it! [extreme negative]", "hate"),
        ("8. This is wonderful! I absolutely ___ it! [extreme positive]", "love"),
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

    # Exercise Set 9: Error correction (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 9: Error Correction

Find and correct the error in each sentence. Write the corrected sentence.

### Instructions:
- Identify what's wrong (missing -ing, wrong verb form, spelling, etc.)
- Write the complete correct sentence

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set9 = [
        ("1. I like read books. → ___", "I like reading books."),
        ("2. She loves to dancing. → ___", "She loves dancing."),
        ("3. They enjoys cooking. → ___", "They enjoy cooking."),
        ("4. He don't like waiting. → ___", "He doesn't like waiting."),
        ("5. Does you love swimming? → ___", "Do you love swimming?"),
        ("6. I hate do homework. → ___", "I hate doing homework."),
        ("7. She like playing tennis. → ___", "She likes playing tennis."),
        ("8. We prefer walk to drive. → ___", "We prefer walking to driving."),
    ]

    for prompt, answer in exercises_set9:
        cells.append(
            create_cell(
                "code",
                f"""# Exercise 9.{exercises_set9.index((prompt, answer)) + 1}
exercise.create_fill_in_blank(
    "{prompt}",
    "{answer}"
)""",
                f"cell-{cell_counter}",
            )
        )
        cell_counter += 1

    # Exercise Set 10: Context completion (8 exercises)
    cells.append(
        create_cell(
            "markdown",
            """---

## Exercise Set 10: Context Completion

Complete the conversations with the correct preference verb + -ing form.

### Instructions:
- Read the full context
- Choose the appropriate preference verb
- Use correct form with -ing

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    exercises_set10 = [
        ("1. A: What do you do for fun? B: I ___ (play) guitar. [hobby]", "like playing"),
        (
            "2. A: Do you want to go shopping? B: Not really. I ___ (shop). [strong negative]",
            "hate shopping",
        ),
        (
            "3. A: Can you help me? B: Sure! I ___ (help) people. [neutral/willing]",
            "don't mind helping",
        ),
        (
            "4. A: What's your passion? B: I ___ (paint)! It's amazing! [strong positive]",
            "love painting",
        ),
        (
            "5. A: Do you like coffee or tea? B: I ___ (drink) tea. [comparison implied]",
            "prefer drinking",
        ),
        ("6. A: How do you relax? B: I ___ (read) novels. [active pleasure]", "enjoy reading"),
        (
            "7. A: What's the worst chore? B: I absolutely ___ (clean) the bathroom! [extreme negative]",
            "hate cleaning",
        ),
        (
            "8. A: What do you do on weekends? B: I ___ (spend) time with family. [positive]",
            "like spending",
        ),
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
- **60-79%**: Good progress! Review the rules, then continue 👍
- **Below 60%**: Review **01_introduction.ipynb** and retry these exercises 📚

### Key Points to Remember:
- **Always use -ing form** after preference verbs
- **Spelling rules**: drop -e, double consonants for CVC patterns
- **Subject-verb agreement**: I like / She likes
- **Negatives**: don't/doesn't + verb + -ing
- **Questions**: Do/Does + subject + verb + -ing?
- **LOVE** = very positive, **LIKE** = positive, **HATE** = very negative
- **ENJOY** = active pleasure, **PREFER** = comparison, **DON'T MIND** = neutral
- **ENJOY** only takes -ing (never infinitive!)

---

### Continue to:
**03_meaningful_practice.ipynb** - Personal activities about YOUR preferences and hobbies!

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

    # Count exercises
    exercise_count = sum(
        1
        for cell in notebook["cells"]
        if cell["cell_type"] == "code" and "exercise.create" in str(cell.get("source", ""))
    )
    print(f"🎯 Total exercises: {exercise_count}")

    # Check if size is within target range
    if 25 <= file_size_kb <= 30:
        print("[OK] File size is within target range (25-30 KB)")
    else:
        print(
            f"⚠️ File size is outside target range. Target: 25-30 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
