"""
Enhancement script for A1 Review: Modules 11-15
Covers: Question Words, Can/Can't, Demonstratives, Like/Love/Hate + -ing, Past Simple Was/Were
Target: 12-15 KB production-ready notebook
"""

import nbformat as nbf


def create_review_notebook():
    nb = nbf.v4.new_notebook()

    cells = []

    # Cell 0: Header and Introduction
    cells.append(
        nbf.v4.new_markdown_cell(
            """# A1 Review: Modules 11-15

## 🔄 Comprehensive Review Session

**Welcome to your second major review!** This session covers everything you learned in Modules 11-15.

### Modules Covered:
- ✅ **Module 11:** Question Words (who, what, where, when, why, how)
- ✅ **Module 12:** Can/Can't (ability and permission)
- ✅ **Module 13:** Demonstratives (this, that, these, those)
- ✅ **Module 14:** Like/Love/Hate + -ing (preferences and gerunds)
- ✅ **Module 15:** Past Simple Was/Were (past tense of "to be")

### Purpose of This Review:
This is **spaced repetition** - revisiting what you've learned helps move knowledge from short-term to long-term memory. This review introduces:
- Question formation skills
- Expressing abilities and preferences
- Talking about the past
- Combining different grammar structures

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

    # Cell 3: Exercise Set 1 - Question Words (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 1: Question Words (10 questions)

Complete each question with the correct question word."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.1: Question Words
exercises_1_1 = [
    create_multiple_choice(
        "___ is your name?",
        options=["What", "Who", "Where", "When"],
        correct_answer="What",
        hint="asking for a name"
    ),
    create_multiple_choice(
        "___ are you from?",
        options=["What", "Who", "Where", "When"],
        correct_answer="Where",
        hint="asking for a place"
    ),
    create_multiple_choice(
        "___ is your birthday?",
        options=["What", "Who", "Where", "When"],
        correct_answer="When",
        hint="asking for a time"
    ),
    create_multiple_choice(
        "___ is she?",
        options=["What", "Who", "Where", "How"],
        correct_answer="Who",
        hint="asking for a person's identity"
    ),
    create_multiple_choice(
        "___ are you?",
        options=["What", "Who", "Where", "How"],
        correct_answer="How",
        hint="asking about someone's state/condition"
    ),
    create_multiple_choice(
        "___ do you study English?",
        options=["What", "Who", "Why", "Where"],
        correct_answer="Why",
        hint="asking for a reason"
    ),
    create_multiple_choice(
        "___ old are you?",
        options=["What", "Who", "How", "When"],
        correct_answer="How",
        hint="asking about age"
    ),
    create_multiple_choice(
        "___ is your favorite color?",
        options=["What", "Who", "Where", "When"],
        correct_answer="What",
        hint="asking for information"
    ),
    create_multiple_choice(
        "___ do you live?",
        options=["What", "Who", "Where", "When"],
        correct_answer="Where",
        hint="asking for a place/location"
    ),
    create_multiple_choice(
        "___ is your teacher?",
        options=["What", "Who", "Where", "When"],
        correct_answer="Who",
        hint="asking for a person"
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

    # Cell 4: Exercise Set 2 - Can/Can't (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 2: Can/Can't (10 questions)

Complete with 'can' or 'can't' based on the context."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.2: Can/Can't
exercises_1_2 = [
    create_multiple_choice(
        "She ___ speak three languages.",
        options=["can", "can't", "cans", "no can"],
        correct_answer="can",
        hint="ability - positive"
    ),
    create_multiple_choice(
        "I ___ swim. I never learned.",
        options=["can", "can't", "cans", "no can"],
        correct_answer="can't",
        hint="lack of ability - negative"
    ),
    create_multiple_choice(
        "___ you drive a car?",
        options=["Can", "Do can", "Are can", "Can't"],
        correct_answer="Can",
        hint="question about ability"
    ),
    create_fill_in_blank(
        "He ___ play the piano very well.",
        answer="can",
        hint="positive ability"
    ),
    create_fill_in_blank(
        "We ___ see the mountains from here. It's too foggy.",
        answer="can't",
        hint="negative - unable to see"
    ),
    create_multiple_choice(
        "___ I use your phone?",
        options=["Can", "Do can", "Am can", "Can't"],
        correct_answer="Can",
        hint="asking permission"
    ),
    create_fill_in_blank(
        "They ___ come to the party tonight. They're busy.",
        answer="can't",
        hint="negative - unable to attend"
    ),
    create_fill_in_blank(
        "My dog ___ do many tricks.",
        answer="can",
        hint="positive ability"
    ),
    create_multiple_choice(
        "She ___ speak Arabic, but she ___ write it.",
        options=["can, can't", "can't, can", "can, can", "can't, can't"],
        correct_answer="can, can't",
        hint="positive then negative"
    ),
    create_fill_in_blank(
        "___ you help me with this?",
        answer="Can",
        hint="asking for help"
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

    # Cell 5: Exercise Set 3 - Demonstratives (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 3: Demonstratives (10 questions)

Choose this/that/these/those based on distance and number."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.3: Demonstratives
exercises_1_3 = [
    create_multiple_choice(
        "___ book (in my hand) is interesting.",
        options=["This", "That", "These", "Those"],
        correct_answer="This",
        hint="singular, near"
    ),
    create_multiple_choice(
        "___ books (over there) are expensive.",
        options=["This", "That", "These", "Those"],
        correct_answer="Those",
        hint="plural, far"
    ),
    create_multiple_choice(
        "___ pen (on the table near you) is mine.",
        options=["This", "That", "These", "Those"],
        correct_answer="That",
        hint="singular, far"
    ),
    create_multiple_choice(
        "___ shoes (I'm wearing) are new.",
        options=["This", "That", "These", "Those"],
        correct_answer="These",
        hint="plural, near"
    ),
    create_fill_in_blank(
        "___ is my car. (pointing to a car here)",
        answer="This",
        hint="singular, near"
    ),
    create_fill_in_blank(
        "___ are my friends. (people standing with me)",
        answer="These",
        hint="plural, near"
    ),
    create_fill_in_blank(
        "___ building (across the street) is very tall.",
        answer="That",
        hint="singular, far"
    ),
    create_fill_in_blank(
        "___ flowers (in the distance) are beautiful.",
        answer="Those",
        hint="plural, far"
    ),
    create_multiple_choice(
        "Is ___ your phone? (on the table near me)",
        options=["this", "that", "these", "those"],
        correct_answer="this",
        hint="singular, near"
    ),
    create_multiple_choice(
        "Are ___ your keys? (over there)",
        options=["this", "that", "these", "those"],
        correct_answer="those",
        hint="plural, far"
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

    # Cell 6: Exercise Set 4 - Like/Love/Hate + -ing (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 4: Like/Love/Hate + -ing (10 questions)

Add -ing to the verb after like/love/hate."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.4: Like/Love/Hate + -ing
exercises_1_4 = [
    create_fill_in_blank(
        "I love ___ (swim) in the ocean.",
        answer="swimming",
        hint="swim + -ing"
    ),
    create_fill_in_blank(
        "She hates ___ (cook).",
        answer="cooking",
        hint="cook + -ing"
    ),
    create_fill_in_blank(
        "Do you like ___ (read)?",
        answer="reading",
        hint="read + -ing"
    ),
    create_fill_in_blank(
        "They love ___ (dance) together.",
        answer="dancing",
        hint="dance - drop e, add -ing"
    ),
    create_fill_in_blank(
        "He doesn't like ___ (run).",
        answer="running",
        hint="run - double n, add -ing"
    ),
    create_fill_in_blank(
        "We enjoy ___ (play) video games.",
        answer="playing",
        hint="play + -ing"
    ),
    create_fill_in_blank(
        "I hate ___ (wait) in lines.",
        answer="waiting",
        hint="wait + -ing"
    ),
    create_fill_in_blank(
        "She loves ___ (shop) online.",
        answer="shopping",
        hint="shop - double p, add -ing"
    ),
    create_fill_in_blank(
        "Do they like ___ (travel)?",
        answer="traveling",
        hint="travel + -ing"
    ),
    create_fill_in_blank(
        "My brother hates ___ (study).",
        answer="studying",
        hint="study - change y to i? No! Just add -ing"
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

    # Cell 7: Exercise Set 5 - Was/Were (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 5: Past Simple Was/Were (10 questions)

Choose 'was' or 'were' for past tense."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.5: Was/Were
exercises_1_5 = [
    create_multiple_choice(
        "I ___ at home yesterday.",
        options=["was", "were"],
        correct_answer="was",
        hint="I + was"
    ),
    create_multiple_choice(
        "They ___ at the party last night.",
        options=["was", "were"],
        correct_answer="were",
        hint="they + were"
    ),
    create_multiple_choice(
        "She ___ very happy yesterday.",
        options=["was", "were"],
        correct_answer="was",
        hint="she + was"
    ),
    create_multiple_choice(
        "We ___ at school last week.",
        options=["was", "were"],
        correct_answer="were",
        hint="we + were"
    ),
    create_multiple_choice(
        "___ you at the meeting?",
        options=["Was", "Were"],
        correct_answer="Were",
        hint="you + were"
    ),
    create_fill_in_blank(
        "He ___ tired after work.",
        answer="was",
        hint="he + was"
    ),
    create_fill_in_blank(
        "The dogs ___ in the garden.",
        answer="were",
        hint="plural + were"
    ),
    create_fill_in_blank(
        "It ___ cold yesterday.",
        answer="was",
        hint="it + was"
    ),
    create_multiple_choice(
        "Where ___ you born?",
        options=["was", "were"],
        correct_answer="were",
        hint="you + were"
    ),
    create_multiple_choice(
        "The movie ___ very boring.",
        options=["was", "were"],
        correct_answer="was",
        hint="singular + was"
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

## Part 2: Error Correction (18 exercises)

Find and correct the errors in these sentences. Each sentence has ONE mistake.

### Common Error Types:
- Wrong question word
- Incorrect use of can/can't
- Wrong demonstrative
- Missing -ing after like/love/hate
- Wrong form of was/were

---"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 2.1: Error Correction
exercises_2_1 = [
    create_fill_in_blank(
        "What is your name? → ___ is your name?",
        answer="What",
        hint="Already correct! This checks understanding"
    ),
    create_fill_in_blank(
        "Where old are you? → ___ old are you?",
        answer="How",
        hint="Use 'How' for age"
    ),
    create_fill_in_blank(
        "She cans speak English. → She ___ speak English.",
        answer="can",
        hint="No 's' with can"
    ),
    create_fill_in_blank(
        "I don't can swim. → I ___ swim.",
        answer="can't",
        hint="Use can't, not don't can"
    ),
    create_fill_in_blank(
        "This books are mine. → ___ books are mine.",
        answer="These",
        hint="plural noun needs 'these'"
    ),
    create_fill_in_blank(
        "Those car is expensive. → ___ car is expensive.",
        answer="That",
        hint="singular noun needs 'that'"
    ),
    create_fill_in_blank(
        "I love read books. → I love ___ books.",
        answer="reading",
        hint="need -ing form"
    ),
    create_fill_in_blank(
        "She hates to cooking. → She hates ___.",
        answer="cooking",
        hint="no 'to' needed"
    ),
    create_fill_in_blank(
        "They was at home. → They ___ at home.",
        answer="were",
        hint="plural needs 'were'"
    ),
    create_fill_in_blank(
        "I were tired yesterday. → I ___ tired yesterday.",
        answer="was",
        hint="I + was"
    ),
    create_fill_in_blank(
        "Who is you from? → ___ are you from?",
        answer="Where",
        hint="asking about place"
    ),
    create_fill_in_blank(
        "Can you to help me? → Can you ___ me?",
        answer="help",
        hint="no 'to' after can"
    ),
    create_fill_in_blank(
        "These is my phone. → ___ is my phone.",
        answer="This",
        hint="singular noun needs 'this'"
    ),
    create_fill_in_blank(
        "I like swim. → I like ___.",
        answer="swimming",
        hint="add -ing"
    ),
    create_fill_in_blank(
        "He were at school. → He ___ at school.",
        answer="was",
        hint="he + was"
    ),
    create_fill_in_blank(
        "What you can do? → What ___ you do?",
        answer="can",
        hint="Question order: What can you"
    ),
    create_fill_in_blank(
        "That shoes are dirty. → ___ shoes are dirty.",
        answer="Those",
        hint="plural needs 'those'"
    ),
    create_fill_in_blank(
        "She loves runing. → She loves ___.",
        answer="running",
        hint="double n in running"
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

### Task 1: Interview Your Partner

Write 10 questions to interview someone about their abilities and preferences. Use:
- Question words (what, where, who, why, how)
- Can you...? questions
- Like/love/hate questions

**Example:**
- What's your favorite hobby?
- Can you play any musical instruments?
- Do you like traveling?
- Where were you born?
- Why do you study English?

**Your 10 questions:**

[Double-click to write your answer]

---

### Task 2: Describe Your Abilities and Preferences

Write a paragraph about yourself using:
- I can/can't (describe your abilities)
- I like/love/hate + -ing (describe your preferences)
- This/these (point to things near you)

**Example:**
- I can speak two languages, but I can't play any instruments. I love reading books and watching movies. I hate waking up early. This is my favorite book, and these are my favorite shoes.

**Your paragraph:**

[Double-click to write your answer]

---

### Task 3: Write About Your Childhood

Describe what you were like as a child using:
- Was/were (describe past states)
- Could (past ability - use 'could' as past of 'can')
- Question words in questions about your past

**Example:**
- When I was young, I was very shy. I was always with my sister. We were best friends. I could climb trees and run very fast. Where were you when you were a child?

**Your description:**

[Double-click to write your answer]

---

### Task 4: Compare Then and Now

Compare your past (when you were younger) with your present. Use:
- Was/were (for past)
- Am/is/are (for present)
- Can/can't and could/couldn't
- Like/love/hate + -ing

**Example:**
- When I was 10, I was very small. Now I am tall. I couldn't swim then, but I can swim now. I loved playing video games, and I still love playing them today.

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

### Module 11: Question Words
**My confidence:** ___/5

**What I need to review:**
- [ ] Who (asking about people)
- [ ] What (asking for information)
- [ ] Where (asking about places)
- [ ] When (asking about time)
- [ ] Why (asking for reasons)
- [ ] How (asking about manner/state)

**Notes:**

---

### Module 12: Can/Can't
**My confidence:** ___/5

**What I need to review:**
- [ ] Can for ability (I can swim)
- [ ] Can't for inability (I can't drive)
- [ ] Can for permission (Can I go?)
- [ ] Question form (Can you...?)
- [ ] No 's' with he/she/it (she can, not cans)

**Notes:**

---

### Module 13: Demonstratives
**My confidence:** ___/5

**What I need to review:**
- [ ] This (singular, near)
- [ ] That (singular, far)
- [ ] These (plural, near)
- [ ] Those (plural, far)

**Notes:**

---

### Module 14: Like/Love/Hate + -ing
**My confidence:** ___/5

**What I need to review:**
- [ ] Adding -ing to verbs
- [ ] Spelling changes (dance→dancing, run→running)
- [ ] Using with like/love/hate/enjoy
- [ ] Gerunds as nouns

**Notes:**

---

### Module 15: Past Simple Was/Were
**My confidence:** ___/5

**What I need to review:**
- [ ] I/he/she/it + was
- [ ] You/we/they + were
- [ ] Questions (Were you...? Was she...?)
- [ ] Negatives (wasn't, weren't)

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
    print("🌟 EXCELLENT! You've mastered Modules 11-15!")
    print("You're ready to continue to Module 16.")
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

Congratulations on completing the Modules 11-15 Review!

### What You've Reviewed:
✅ Question Words - Asking information questions
✅ Can/Can't - Expressing ability and permission
✅ Demonstratives - Pointing to things near and far
✅ Like/Love/Hate + -ing - Expressing preferences
✅ Past Simple Was/Were - Talking about the past

### Spaced Repetition Schedule:
For best retention, retake this review:
- **After 1 week** - Reinforce what you learned
- **After 1 month** - Long-term memory consolidation
- **Before moving to A2 level** - Final check

### Next Steps:

**If your score was 75% or higher:**
- ✅ Continue to **Module 16: Past Simple Regular Verbs**
- ✅ Come back to this review in 1 week

**If your score was below 75%:**
- 📚 Review the modules where you struggled
- 📝 Redo the practice exercises in those modules
- 🔄 Retake this review after 2-3 days

---

### Tips for Success:
1. **Practice questions** - Ask and answer questions daily
2. **Describe your abilities** - Think about what you can/can't do
3. **Express preferences** - Talk about what you like/hate doing
4. **Tell stories** - Practice using past tense
5. **Point and describe** - Use demonstratives for things around you

---

**Keep up the excellent work!** 🌟

You're making great progress through A1 level. Keep going!

---"""
        )
    )

    # Save notebook
    nb.cells = cells
    return nb


if __name__ == "__main__":
    nb = create_review_notebook()
    output_path = "A1_Review_Modules_11-15.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    print(f"✅ Created: {output_path}")

    # Check file size
    import os

    size_kb = os.path.getsize(output_path) / 1024
    print(f"📏 File size: {size_kb:.2f} KB")
