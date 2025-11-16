"""
Enhancement script for A1 Review: Modules 6-10
Covers: Nouns/Plurals, Possessives, Adjectives, There Is/Are, Prepositions
Target: 12-15 KB production-ready notebook
"""

import nbformat as nbf


def create_review_notebook():
    nb = nbf.v4.new_notebook()

    cells = []

    # Cell 0: Header and Introduction
    cells.append(
        nbf.v4.new_markdown_cell(
            """# A1 Review: Modules 6-10

## 🔄 Comprehensive Review Session

**Welcome to your first major review!** This session covers everything you learned in Modules 6-10.

### Modules Covered:
- ✅ **Module 6:** Nouns and Plurals (regular and irregular)
- ✅ **Module 7:** Possessives (apostrophe 's and of)
- ✅ **Module 8:** Adjectives (descriptive words)
- ✅ **Module 9:** There Is/Are (describing existence)
- ✅ **Module 10:** Prepositions (in, on, at, from, to, with, etc.)

### Purpose of This Review:
This is **spaced repetition** - revisiting what you've learned helps move knowledge from short-term to long-term memory. Expect to:
- Mix different grammar points together
- Apply rules in new contexts
- Identify areas that need more practice

⏱️ **Estimated time:** 2-3 hours

---

### How to Use This Notebook:
1. Work through all sections in order
2. Check answers immediately after each exercise
3. Review modules where you make mistakes
4. Complete the self-assessment at the end
5. Retake this review after 1 week for best results

---"""
        )
    )

    # Cell 1: Setup
    cells.append(
        nbf.v4.new_code_cell(
            """# Setup
import sys
sys.path.append('../../../utils')

from exercise_validator import ExerciseValidator, create_fill_in_blank, create_multiple_choice
from interactive_exercise import InteractiveExercise
from IPython.display import display, HTML

print("✅ Review session ready! Let's test your knowledge!")

# Initialize score tracking
total_score = 0
max_score = 0"""
        )
    )

    # Cell 2: Part 1 - Mixed Grammar Review Introduction
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## Part 1: Mixed Grammar Review (40 exercises)

This section mixes all five modules together. Each exercise tests a different grammar point.

### Instructions:
- Complete each sentence with the correct form
- Pay attention to context clues
- Think about which grammar rule applies

---"""
        )
    )

    # Cell 3: Exercise Set 1 - Nouns and Plurals (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 1: Nouns and Plurals (10 questions)

Complete with the correct singular or plural form."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.1: Nouns and Plurals
exercises_1_1 = [
    create_fill_in_blank(
        "There are three ___ on the table.",
        answer="books",
        hint="plural of book"
    ),
    create_fill_in_blank(
        "The ___ are playing in the garden.",
        answer="children",
        hint="irregular plural of child"
    ),
    create_fill_in_blank(
        "I have two ___ at home.",
        answer="cats",
        hint="plural of cat"
    ),
    create_fill_in_blank(
        "She has many ___ in different countries.",
        answer="friends",
        hint="plural of friend"
    ),
    create_fill_in_blank(
        "The ___ are swimming in the lake.",
        answer="fish",
        hint="plural form same as singular"
    ),
    create_fill_in_blank(
        "Those ___ are very expensive.",
        answer="watches",
        hint="plural of watch"
    ),
    create_fill_in_blank(
        "I can see five ___ in the field.",
        answer="sheep",
        hint="irregular plural - same as singular"
    ),
    create_fill_in_blank(
        "The ___ of the city are very tall.",
        answer="buildings",
        hint="plural of building"
    ),
    create_fill_in_blank(
        "My ___ hurt after walking.",
        answer="feet",
        hint="irregular plural of foot"
    ),
    create_fill_in_blank(
        "There are many ___ in the box.",
        answer="toys",
        hint="plural of toy"
    ),
]

validator_1_1 = ExerciseValidator(exercises_1_1)
validator_1_1.display_exercises()

# Add to score tracking
exercise_score = validator_1_1.get_score()
total_score += exercise_score
max_score += len(exercises_1_1)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 4: Exercise Set 2 - Possessives (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 2: Possessives (10 questions)

Use 's or of to show possession."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.2: Possessives
exercises_1_2 = [
    create_fill_in_blank(
        "This is my ___ car.",
        answer="father's",
        hint="singular possession - father"
    ),
    create_fill_in_blank(
        "The ___ of the book is very interesting.",
        answer="story",
        hint="use 'of' for things"
    ),
    create_fill_in_blank(
        "Those are the ___ toys.",
        answer="children's",
        hint="plural irregular possession - children"
    ),
    create_fill_in_blank(
        "My ___ house is near the beach.",
        answer="sister's",
        hint="singular possession - sister"
    ),
    create_fill_in_blank(
        "The ___ of this building is amazing.",
        answer="design",
        hint="use 'of' for things"
    ),
    create_fill_in_blank(
        "The ___ room is upstairs.",
        answer="teachers'",
        hint="plural possession - teachers"
    ),
    create_fill_in_blank(
        "I love the ___ of the ocean.",
        answer="sound",
        hint="use 'of' for things"
    ),
    create_fill_in_blank(
        "This is ___ laptop.",
        answer="James's",
        hint="name ending in s - add 's"
    ),
    create_fill_in_blank(
        "The ___ tails are long.",
        answer="dogs'",
        hint="plural possession - dogs"
    ),
    create_fill_in_blank(
        "The ___ of my country is beautiful.",
        answer="flag",
        hint="use 'of' for things"
    ),
]

validator_1_2 = ExerciseValidator(exercises_1_2)
validator_1_2.display_exercises()

exercise_score = validator_1_2.get_score()
total_score += exercise_score
max_score += len(exercises_1_2)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 5: Exercise Set 3 - Adjectives (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 3: Adjectives (10 questions)

Choose the correct adjective to describe each noun."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.3: Adjectives
exercises_1_3 = [
    create_multiple_choice(
        "The coffee is ___.",
        options=["hot", "hotly", "hots", "hotness"],
        correct_answer="hot",
        hint="adjective describing coffee"
    ),
    create_multiple_choice(
        "She has ___ hair.",
        options=["beauty", "beautiful", "beautifully", "beautify"],
        correct_answer="beautiful",
        hint="adjective before noun"
    ),
    create_fill_in_blank(
        "The ___ cat is sleeping.",
        answer="black",
        hint="color adjective"
    ),
    create_fill_in_blank(
        "This is a ___ book.",
        answer="interesting",
        hint="adjective describing the book"
    ),
    create_fill_in_blank(
        "My ___ brother lives in London.",
        answer="older",
        hint="comparative adjective for age"
    ),
    create_multiple_choice(
        "The movie was very ___.",
        options=["boring", "bored", "bore", "boringly"],
        correct_answer="boring",
        hint="-ing adjective describes the movie"
    ),
    create_fill_in_blank(
        "They live in a ___ house.",
        answer="big",
        hint="size adjective"
    ),
    create_fill_in_blank(
        "The ___ news made everyone happy.",
        answer="good",
        hint="positive adjective"
    ),
    create_multiple_choice(
        "I feel ___ today.",
        options=["tire", "tired", "tiring", "tiredly"],
        correct_answer="tired",
        hint="-ed adjective for how you feel"
    ),
    create_fill_in_blank(
        "She wore a ___ dress to the party.",
        answer="red",
        hint="color adjective"
    ),
]

validator_1_3 = ExerciseValidator(exercises_1_3)
validator_1_3.display_exercises()

exercise_score = validator_1_3.get_score()
total_score += exercise_score
max_score += len(exercises_1_3)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 6: Exercise Set 4 - There Is/Are (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 4: There Is/Are (10 questions)

Choose 'is' or 'are' based on singular or plural."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.4: There Is/Are
exercises_1_4 = [
    create_multiple_choice(
        "There ___ a book on the table.",
        options=["is", "are"],
        correct_answer="is",
        hint="singular noun - book"
    ),
    create_multiple_choice(
        "There ___ many people in the park.",
        options=["is", "are"],
        correct_answer="are",
        hint="plural noun - people"
    ),
    create_multiple_choice(
        "There ___ some water in the bottle.",
        options=["is", "are"],
        correct_answer="is",
        hint="uncountable noun - water"
    ),
    create_multiple_choice(
        "___ there any apples in the fridge?",
        options=["Is", "Are"],
        correct_answer="Are",
        hint="plural noun - apples"
    ),
    create_multiple_choice(
        "There ___ a problem with my computer.",
        options=["is", "are"],
        correct_answer="is",
        hint="singular noun - problem"
    ),
    create_multiple_choice(
        "There ___ three cats in the garden.",
        options=["is", "are"],
        correct_answer="are",
        hint="plural noun - cats"
    ),
    create_multiple_choice(
        "___ there a meeting today?",
        options=["Is", "Are"],
        correct_answer="Is",
        hint="singular noun - meeting"
    ),
    create_multiple_choice(
        "There ___ no chairs in this room.",
        options=["is", "are"],
        correct_answer="are",
        hint="plural noun - chairs"
    ),
    create_multiple_choice(
        "There ___ a lot of traffic today.",
        options=["is", "are"],
        correct_answer="is",
        hint="uncountable noun - traffic"
    ),
    create_multiple_choice(
        "There ___ two restaurants near my house.",
        options=["is", "are"],
        correct_answer="are",
        hint="plural noun - restaurants"
    ),
]

validator_1_4 = ExerciseValidator(exercises_1_4)
validator_1_4.display_exercises()

exercise_score = validator_1_4.get_score()
total_score += exercise_score
max_score += len(exercises_1_4)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 7: Exercise Set 5 - Prepositions (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 5: Prepositions (10 questions)

Choose the correct preposition for each context."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.5: Prepositions
exercises_1_5 = [
    create_multiple_choice(
        "I live ___ New York.",
        options=["in", "on", "at"],
        correct_answer="in",
        hint="use 'in' for cities"
    ),
    create_multiple_choice(
        "The meeting is ___ 3 o'clock.",
        options=["in", "on", "at"],
        correct_answer="at",
        hint="use 'at' for specific times"
    ),
    create_multiple_choice(
        "My birthday is ___ May.",
        options=["in", "on", "at"],
        correct_answer="in",
        hint="use 'in' for months"
    ),
    create_multiple_choice(
        "She is ___ the office.",
        options=["in", "on", "at"],
        correct_answer="in",
        hint="use 'in' for enclosed spaces"
    ),
    create_multiple_choice(
        "The book is ___ the table.",
        options=["in", "on", "at"],
        correct_answer="on",
        hint="use 'on' for surfaces"
    ),
    create_multiple_choice(
        "I'm going ___ the store.",
        options=["to", "at", "in"],
        correct_answer="to",
        hint="use 'to' for direction/destination"
    ),
    create_multiple_choice(
        "He's ___ home.",
        options=["in", "on", "at"],
        correct_answer="at",
        hint="use 'at' for home"
    ),
    create_multiple_choice(
        "The picture is ___ the wall.",
        options=["in", "on", "at"],
        correct_answer="on",
        hint="use 'on' for surfaces"
    ),
    create_multiple_choice(
        "I come ___ Brazil.",
        options=["from", "to", "at"],
        correct_answer="from",
        hint="use 'from' for origin"
    ),
    create_multiple_choice(
        "She goes to work ___ bus.",
        options=["by", "with", "on"],
        correct_answer="by",
        hint="use 'by' for transportation method"
    ),
]

validator_1_5 = ExerciseValidator(exercises_1_5)
validator_1_5.display_exercises()

exercise_score = validator_1_5.get_score()
total_score += exercise_score
max_score += len(exercises_1_5)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 8: Part 2 - Error Correction
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## Part 2: Error Correction (15 exercises)

Find and correct the errors in these sentences. Each sentence has ONE mistake.

### Common Error Types:
- Wrong plural form
- Incorrect possessive
- Adjective in wrong position
- Wrong form of there is/are
- Wrong preposition

---"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 2.1: Error Correction
exercises_2_1 = [
    create_fill_in_blank(
        "There is many people in the room. → There ___ many people in the room.",
        answer="are",
        hint="plural noun needs 'are'"
    ),
    create_fill_in_blank(
        "The childs are playing outside. → The ___ are playing outside.",
        answer="children",
        hint="irregular plural of child"
    ),
    create_fill_in_blank(
        "This is my fathers car. → This is my ___ car.",
        answer="father's",
        hint="need apostrophe for possession"
    ),
    create_fill_in_blank(
        "She is a very beautifully woman. → She is a very ___ woman.",
        answer="beautiful",
        hint="adjective, not adverb"
    ),
    create_fill_in_blank(
        "I live in London in England. → I live ___ London ___ England.",
        answer="in in",
        hint="both use 'in' for cities and countries"
    ),
    create_fill_in_blank(
        "There are a book on the shelf. → There ___ a book on the shelf.",
        answer="is",
        hint="singular noun needs 'is'"
    ),
    create_fill_in_blank(
        "The womans are talking. → The ___ are talking.",
        answer="women",
        hint="irregular plural of woman"
    ),
    create_fill_in_blank(
        "This is the cars of my friend. → This is my ___ car.",
        answer="friend's",
        hint="use apostrophe 's for people"
    ),
    create_fill_in_blank(
        "I have two foots. → I have two ___.",
        answer="feet",
        hint="irregular plural of foot"
    ),
    create_fill_in_blank(
        "The movie was very bored. → The movie was very ___.",
        answer="boring",
        hint="-ing for describing things"
    ),
    create_fill_in_blank(
        "She arrives at 9 o'clock in the morning. → She arrives ___ 9 o'clock ___ the morning.",
        answer="at in",
        hint="'at' for time, 'in' for part of day"
    ),
    create_fill_in_blank(
        "There is three apples in the basket. → There ___ three apples in the basket.",
        answer="are",
        hint="plural noun needs 'are'"
    ),
    create_fill_in_blank(
        "The students books are heavy. → The ___ books are heavy.",
        answer="students'",
        hint="plural possessive - apostrophe after s"
    ),
    create_fill_in_blank(
        "I am interesting in music. → I am ___ in music.",
        answer="interested",
        hint="-ed for how people feel"
    ),
    create_fill_in_blank(
        "The book is in the table. → The book is ___ the table.",
        answer="on",
        hint="use 'on' for surfaces"
    ),
]

validator_2_1 = ExerciseValidator(exercises_2_1)
validator_2_1.display_exercises()

exercise_score = validator_2_1.get_score()
total_score += exercise_score
max_score += len(exercises_2_1)
print(f"\\nCurrent Score: {total_score}/{max_score}")"""
        )
    )

    # Cell 9: Part 3 - Integrated Communication Tasks
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## Part 3: Integrated Communication Tasks (4 activities)

These activities combine multiple grammar points in real-world scenarios.

---

### Task 1: Describe Your Classroom

Write 8-10 sentences describing a classroom. Use:
- There is/are (to describe what exists)
- Adjectives (to describe things)
- Prepositions (to say where things are)
- Plurals (for multiple items)

**Example:**
- There is a big whiteboard on the wall.
- There are twenty students in the class.
- The teacher's desk is at the front.
- There are many books on the shelves.

**Your description:**

[Double-click to write your answer]

---

### Task 2: Describe Your Family's Possessions

Write about what different family members own. Use:
- Possessives (apostrophe 's)
- Adjectives (to describe the items)
- Plurals (if they own multiple items)

**Example:**
- My father's car is black and very fast.
- My sister's books are on the big shelf.
- My mother's garden has beautiful flowers.

**Your description:**

[Double-click to write your answer]

---

### Task 3: Write About Your Neighborhood

Describe your neighborhood using:
- There is/are
- Prepositions (location words)
- Adjectives (descriptive words)
- Plurals

**Example:**
- There is a small park near my house.
- There are many restaurants on Main Street.
- The coffee shop is next to the bookstore.

**Your description:**

[Double-click to write your answer]

---

### Task 4: Compare Two Places

Compare two places you know (two cities, two rooms, two restaurants, etc.). Use:
- Adjectives (to describe differences)
- There is/are (to say what each has)
- Prepositions (to describe locations)

**Example:**
- London is bigger than Oxford.
- There are more people in London.
- Oxford is more beautiful in my opinion.
- There are many old buildings in both cities.

**Your comparison:**

[Double-click to write your answer]

---"""
        )
    )

    # Cell 10: Part 4 - Self-Assessment
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## Part 4: Self-Assessment

Rate your confidence in each module (1-5 scale):
- 1 = I don't understand this
- 2 = I understand but make many mistakes
- 3 = I understand but sometimes make mistakes
- 4 = I understand and rarely make mistakes
- 5 = I completely understand and use confidently

### Module 6: Nouns and Plurals
**My confidence:** ___/5

**What I need to review:**
- [ ] Regular plurals (-s, -es)
- [ ] Irregular plurals (child→children, foot→feet, etc.)
- [ ] Plurals that don't change (fish, sheep)
- [ ] Plurals of words ending in -y, -f, -fe

**Notes:**

---

### Module 7: Possessives
**My confidence:** ___/5

**What I need to review:**
- [ ] Apostrophe 's for singular (John's car)
- [ ] Apostrophe after s for plural (students' books)
- [ ] Using 'of' for things (the color of the car)
- [ ] Names ending in s (James's or James')

**Notes:**

---

### Module 8: Adjectives
**My confidence:** ___/5

**What I need to review:**
- [ ] Adjective position (before nouns)
- [ ] -ing adjectives (boring, interesting)
- [ ] -ed adjectives (bored, interested)
- [ ] Common adjectives (big, small, beautiful, etc.)

**Notes:**

---

### Module 9: There Is/Are
**My confidence:** ___/5

**What I need to review:**
- [ ] There is + singular
- [ ] There are + plural
- [ ] There is + uncountable nouns
- [ ] Questions with there is/are

**Notes:**

---

### Module 10: Prepositions
**My confidence:** ___/5

**What I need to review:**
- [ ] in, on, at (time)
- [ ] in, on, at (place)
- [ ] to, from (direction/origin)
- [ ] by, with (transportation/accompaniment)

**Notes:**

---

### Overall Reflection:

**Which module was easiest for you?**

[Your answer]

**Which module was most challenging?**

[Your answer]

**What will you practice more?**

[Your answer]

---"""
        )
    )

    # Cell 11: Progress Display
    cells.append(
        nbf.v4.new_code_cell(
            """# Display Final Score
print("="*50)
print("📊 REVIEW SESSION COMPLETE!")
print("="*50)
print(f"\\nYour Score: {total_score}/{max_score}")
percentage = (total_score/max_score) * 100 if max_score > 0 else 0
print(f"Percentage: {percentage:.1f}%")
print()

if percentage >= 90:
    print("🌟 EXCELLENT! You've mastered Modules 6-10!")
    print("You're ready to continue to Module 11.")
elif percentage >= 75:
    print("👏 GREAT JOB! You have a strong understanding.")
    print("Review the questions you missed, then continue.")
elif percentage >= 60:
    print("👍 GOOD WORK! You're making progress.")
    print("Spend more time reviewing the challenging modules.")
else:
    print("💪 KEEP PRACTICING! Review is important.")
    print("Go back to the modules where you struggled most.")
    print("Retake this review after more practice.")

print()
print("="*50)"""
        )
    )

    # Cell 12: Completion and Next Steps
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## 🎉 Completion & Next Steps

Congratulations on completing the Modules 6-10 Review!

### What You've Reviewed:
✅ Nouns and Plurals - Regular and irregular forms
✅ Possessives - Showing ownership correctly
✅ Adjectives - Describing people, places, and things
✅ There Is/Are - Describing existence and location
✅ Prepositions - Time and place expressions

### Spaced Repetition Schedule:
For best retention, retake this review:
- **After 1 week** - Reinforce what you learned
- **After 1 month** - Long-term memory consolidation
- **Before moving to A2 level** - Final check

### Next Steps:

**If your score was 75% or higher:**
- ✅ Continue to **Module 11: Question Words**
- ✅ Come back to this review in 1 week

**If your score was below 75%:**
- 📚 Review the modules where you struggled
- 📝 Redo the practice exercises in those modules
- 🔄 Retake this review after 2-3 days

---

### Tips for Success:
1. **Don't just memorize** - Understand the rules
2. **Practice daily** - Even 15 minutes helps
3. **Use it in real life** - Describe things around you
4. **Make mistakes** - That's how you learn!
5. **Review regularly** - Spaced repetition works!

---

**Keep up the excellent work!** 🌟

You're building a strong foundation in English grammar. Every review makes you stronger!

---"""
        )
    )

    # Save notebook
    nb.cells = cells
    return nb


if __name__ == "__main__":
    nb = create_review_notebook()
    output_path = "A1_Review_Modules_6-10.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    print(f"✅ Created: {output_path}")

    # Check file size
    import os

    size_kb = os.path.getsize(output_path) / 1024
    print(f"📏 File size: {size_kb:.2f} KB")
