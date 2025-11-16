"""
Enhancement script for A1 Review: Modules 16-20 (FINAL A1 REVIEW!)
Covers: Past Simple Regular/Irregular, Going To Future, Will Future, Adverbs of Frequency
Target: 12-15 KB production-ready notebook
"""

import nbformat as nbf


def create_review_notebook():
    nb = nbf.v4.new_notebook()

    cells = []

    # Cell 0: Header and Introduction
    cells.append(
        nbf.v4.new_markdown_cell(
            """# A1 Review: Modules 16-20

## 🎓 FINAL A1 COMPREHENSIVE REVIEW

**Welcome to your FINAL A1 review!** This session covers the last five modules of A1 level.

### Modules Covered:
- ✅ **Module 16:** Past Simple Regular Verbs (-ed endings)
- ✅ **Module 17:** Past Simple Irregular Verbs (went, ate, saw, etc.)
- ✅ **Module 18:** Going To Future (plans and intentions)
- ✅ **Module 19:** Will Future (predictions and decisions)
- ✅ **Module 20:** Adverbs of Frequency (always, usually, sometimes, never)

### Purpose of This Review:
This is your **final checkpoint** for A1 level! This review tests:
- Your ability to talk about past, present, and future
- Complete story-telling skills
- Time expressions and frequency
- All three main tenses working together

⏱️ **Estimated time:** 2-3 hours

---

### How to Use This Notebook:
1. Work through all sections in order
2. Check answers immediately after each exercise
3. Review modules where you make mistakes
4. Complete the self-assessment at the end
5. Celebrate completing A1 level!

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

print("✅ Final A1 review ready! Let's complete A1 level!")
print("🎯 This is your last A1 review - you can do this!")

# Initialize score tracking
total_score = 0
max_score = 0"""
        )
    )

    # Cell 2: Part 1 - Mixed Grammar Review Introduction
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## Part 1: Mixed Grammar Review (50 exercises)

This section mixes all five modules together. Each exercise tests a different grammar point.

### Instructions:
- Complete each sentence with the correct form
- Pay attention to time markers (yesterday, tomorrow, always, etc.)
- Think about which tense is needed

---"""
        )
    )

    # Cell 3: Exercise Set 1 - Past Simple Regular (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 1: Past Simple Regular Verbs (10 questions)

Add -ed to create past tense (watch for spelling changes!)."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.1: Past Simple Regular Verbs
exercises_1_1 = [
    create_fill_in_blank(
        "I ___ (walk) to school yesterday.",
        answer="walked",
        hint="walk + -ed"
    ),
    create_fill_in_blank(
        "She ___ (watch) a movie last night.",
        answer="watched",
        hint="watch + -ed"
    ),
    create_fill_in_blank(
        "They ___ (play) soccer on Saturday.",
        answer="played",
        hint="play + -ed"
    ),
    create_fill_in_blank(
        "We ___ (visit) our grandparents last week.",
        answer="visited",
        hint="visit + -ed"
    ),
    create_fill_in_blank(
        "He ___ (study) English for two hours.",
        answer="studied",
        hint="study: y→i + -ed"
    ),
    create_fill_in_blank(
        "I ___ (clean) my room this morning.",
        answer="cleaned",
        hint="clean + -ed"
    ),
    create_fill_in_blank(
        "She ___ (stop) at the red light.",
        answer="stopped",
        hint="stop: double p + -ed"
    ),
    create_fill_in_blank(
        "They ___ (work) late yesterday.",
        answer="worked",
        hint="work + -ed"
    ),
    create_fill_in_blank(
        "We ___ (cook) dinner together.",
        answer="cooked",
        hint="cook + -ed"
    ),
    create_fill_in_blank(
        "He ___ (call) me last night.",
        answer="called",
        hint="call + -ed"
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

    # Cell 4: Exercise Set 2 - Past Simple Irregular (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 2: Past Simple Irregular Verbs (10 questions)

Use the irregular past form (no -ed!)."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.2: Past Simple Irregular Verbs
exercises_1_2 = [
    create_fill_in_blank(
        "I ___ (go) to the park yesterday.",
        answer="went",
        hint="go→went"
    ),
    create_fill_in_blank(
        "She ___ (eat) pizza for lunch.",
        answer="ate",
        hint="eat→ate"
    ),
    create_fill_in_blank(
        "We ___ (see) a great movie.",
        answer="saw",
        hint="see→saw"
    ),
    create_fill_in_blank(
        "They ___ (come) to the party.",
        answer="came",
        hint="come→came"
    ),
    create_fill_in_blank(
        "He ___ (take) the bus to work.",
        answer="took",
        hint="take→took"
    ),
    create_fill_in_blank(
        "I ___ (make) a cake yesterday.",
        answer="made",
        hint="make→made"
    ),
    create_fill_in_blank(
        "She ___ (buy) a new phone.",
        answer="bought",
        hint="buy→bought"
    ),
    create_fill_in_blank(
        "We ___ (have) a wonderful time.",
        answer="had",
        hint="have→had"
    ),
    create_fill_in_blank(
        "They ___ (write) a letter.",
        answer="wrote",
        hint="write→wrote"
    ),
    create_fill_in_blank(
        "He ___ (give) me a gift.",
        answer="gave",
        hint="give→gave"
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

    # Cell 5: Exercise Set 3 - Going To Future (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 3: Going To Future (10 questions)

Use 'am/is/are going to + verb' for plans and intentions."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.3: Going To Future
exercises_1_3 = [
    create_fill_in_blank(
        "I ___ (go) to the cinema tomorrow.",
        answer="am going to go",
        hint="I am going to + verb"
    ),
    create_fill_in_blank(
        "She ___ (study) tonight.",
        answer="is going to study",
        hint="she is going to + verb"
    ),
    create_fill_in_blank(
        "They ___ (visit) Paris next month.",
        answer="are going to visit",
        hint="they are going to + verb"
    ),
    create_fill_in_blank(
        "We ___ (have) a party on Saturday.",
        answer="are going to have",
        hint="we are going to + verb"
    ),
    create_multiple_choice(
        "___ you going to come?",
        options=["Are", "Is", "Am", "Do"],
        correct_answer="Are",
        hint="you + are"
    ),
    create_fill_in_blank(
        "He ___ (not/come) to work tomorrow.",
        answer="is not going to come",
        hint="negative: is not going to"
    ),
    create_fill_in_blank(
        "What ___ you ___ to do? (you/do)",
        answer="are going",
        hint="question form: What are you going to"
    ),
    create_fill_in_blank(
        "It ___ (rain) soon. Look at those clouds!",
        answer="is going to rain",
        hint="prediction based on evidence"
    ),
    create_fill_in_blank(
        "I ___ (not/eat) dinner tonight.",
        answer="am not going to eat",
        hint="negative with I"
    ),
    create_fill_in_blank(
        "They ___ (move) to a new house.",
        answer="are going to move",
        hint="they are going to + verb"
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

    # Cell 6: Exercise Set 4 - Will Future (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 4: Will Future (10 questions)

Use 'will + verb' for predictions, promises, and spontaneous decisions."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.4: Will Future
exercises_1_4 = [
    create_fill_in_blank(
        "I ___ (help) you with that.",
        answer="will help",
        hint="will + verb (no 'to')"
    ),
    create_fill_in_blank(
        "She ___ (call) you later.",
        answer="will call",
        hint="promise: will + verb"
    ),
    create_fill_in_blank(
        "It ___ (be) sunny tomorrow.",
        answer="will be",
        hint="prediction"
    ),
    create_fill_in_blank(
        "They ___ (arrive) at 6 PM.",
        answer="will arrive",
        hint="will + verb"
    ),
    create_fill_in_blank(
        "___ you help me? (question)",
        answer="Will",
        hint="question starts with Will"
    ),
    create_fill_in_blank(
        "I ___ (not/go) to the party.",
        answer="will not go",
        hint="negative: will not (won't)"
    ),
    create_fill_in_blank(
        "We ___ (see) you tomorrow.",
        answer="will see",
        hint="will + verb"
    ),
    create_multiple_choice(
        "I think it ___ rain.",
        options=["will", "going to", "is", "are"],
        correct_answer="will",
        hint="opinion/prediction uses 'will'"
    ),
    create_fill_in_blank(
        "He ___ (not/forget) your birthday.",
        answer="will not forget",
        hint="promise - negative"
    ),
    create_fill_in_blank(
        "When ___ you finish? (question)",
        answer="will",
        hint="question: When will you"
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

    # Cell 7: Exercise Set 5 - Adverbs of Frequency (10 exercises)
    cells.append(
        nbf.v4.new_markdown_cell(
            """### Exercise Set 5: Adverbs of Frequency (10 questions)

Place adverbs correctly (usually before main verb, after 'be')."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1.5: Adverbs of Frequency
exercises_1_5 = [
    create_multiple_choice(
        "I ___ eat breakfast.",
        options=["always", "Always", "am always", "always am"],
        correct_answer="always",
        hint="adverb before main verb"
    ),
    create_multiple_choice(
        "She is ___ late.",
        options=["never", "never is", "is never", "not never"],
        correct_answer="never",
        hint="adverb after 'be'"
    ),
    create_fill_in_blank(
        "They ___ go to the gym. (usually)",
        answer="usually",
        hint="before main verb"
    ),
    create_fill_in_blank(
        "I am ___ tired in the morning. (always)",
        answer="always",
        hint="after 'be'"
    ),
    create_multiple_choice(
        "How often do you exercise? - ___",
        options=["Sometimes", "Never", "Usually", "All answers correct"],
        correct_answer="All answers correct",
        hint="all are frequency adverbs"
    ),
    create_fill_in_blank(
        "We ___ watch TV in the evening. (often)",
        answer="often",
        hint="before main verb"
    ),
    create_fill_in_blank(
        "He is ___ happy. (always)",
        answer="always",
        hint="after 'be'"
    ),
    create_multiple_choice(
        "Order from 100% to 0%: always, never, sometimes, usually",
        options=["always-usually-sometimes-never", "always-sometimes-usually-never", "never-sometimes-usually-always", "usually-always-sometimes-never"],
        correct_answer="always-usually-sometimes-never",
        hint="100% to 0%"
    ),
    create_fill_in_blank(
        "I ___ eat fast food. (rarely)",
        answer="rarely",
        hint="before main verb"
    ),
    create_fill_in_blank(
        "They are ___ late for class. (seldom)",
        answer="seldom",
        hint="after 'be'"
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

## Part 2: Error Correction (20 exercises)

Find and correct the errors in these sentences. Each sentence has ONE mistake.

### Common Error Types:
- Wrong past tense form
- Incorrect future structure
- Wrong adverb position
- Tense confusion

---"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 2.1: Error Correction
exercises_2_1 = [
    create_fill_in_blank(
        "I goed to school yesterday. → I ___ to school yesterday.",
        answer="went",
        hint="irregular: go→went"
    ),
    create_fill_in_blank(
        "She eated pizza. → She ___ pizza.",
        answer="ate",
        hint="irregular: eat→ate"
    ),
    create_fill_in_blank(
        "I am going to going home. → I am going to ___ home.",
        answer="go",
        hint="going to + base verb"
    ),
    create_fill_in_blank(
        "I will to help you. → I will ___ you.",
        answer="help",
        hint="will + base verb (no 'to')"
    ),
    create_fill_in_blank(
        "He always is late. → He ___ late.",
        answer="is always",
        hint="'be' + adverb"
    ),
    create_fill_in_blank(
        "They buyed a car. → They ___ a car.",
        answer="bought",
        hint="irregular: buy→bought"
    ),
    create_fill_in_blank(
        "She studyed yesterday. → She ___ yesterday.",
        answer="studied",
        hint="y→i + -ed"
    ),
    create_fill_in_blank(
        "I going to travel. → I ___ to travel.",
        answer="am going",
        hint="need 'am'"
    ),
    create_fill_in_blank(
        "He will comes soon. → He will ___ soon.",
        answer="come",
        hint="will + base verb (no 's')"
    ),
    create_fill_in_blank(
        "I never am tired. → I ___ tired.",
        answer="am never",
        hint="'be' + adverb"
    ),
    create_fill_in_blank(
        "We seed a movie. → We ___ a movie.",
        answer="saw",
        hint="irregular: see→saw"
    ),
    create_fill_in_blank(
        "He stoped the car. → He ___ the car.",
        answer="stopped",
        hint="double p + -ed"
    ),
    create_fill_in_blank(
        "They will going. → They will ___.",
        answer="go",
        hint="will + base verb"
    ),
    create_fill_in_blank(
        "She is going study. → She is going ___ study.",
        answer="to",
        hint="going to + verb"
    ),
    create_fill_in_blank(
        "I usually am happy. → I ___ happy.",
        answer="am usually",
        hint="'be' + adverb"
    ),
    create_fill_in_blank(
        "We writed a letter. → We ___ a letter.",
        answer="wrote",
        hint="irregular: write→wrote"
    ),
    create_fill_in_blank(
        "He plaied soccer. → He ___ soccer.",
        answer="played",
        hint="just add -ed to 'play'"
    ),
    create_fill_in_blank(
        "Are you going visit? → Are you going ___ visit?",
        answer="to",
        hint="going to + verb"
    ),
    create_fill_in_blank(
        "I will am there. → I will ___ there.",
        answer="be",
        hint="will + be (not 'will am')"
    ),
    create_fill_in_blank(
        "She often drinks coffee. → Already correct! (Type 'often')",
        answer="often",
        hint="This is correct as is"
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

These activities combine multiple grammar points and all three tenses.

---

### Task 1: Tell Your Life Story

Write about your past, present, and future using all tenses:
- Past Simple (what you did)
- Present Simple (what you do now)
- Going to/Will (what you'll do)
- Adverbs of frequency (how often)

**Example:**
- I was born in 1995. I went to school in my hometown. I studied hard and learned English. Now I work as a teacher. I usually wake up at 6 AM. I am always busy during the week. Next year, I'm going to travel to Europe. I will visit many countries. I think it will be amazing!

**Your story (12-15 sentences):**

[Double-click to write your answer]

---

### Task 2: Describe Your Daily Routine and Plans

Combine present habits with future plans:
- Use adverbs of frequency
- Describe what you usually do
- Share what you're going to do differently

**Example:**
- I usually wake up at 7 AM. I always have breakfast. I often go to the gym. I sometimes work late. But next week, I'm going to change my routine. I will wake up earlier. I'm going to exercise every morning.

**Your routine and plans:**

[Double-click to write your answer]

---

### Task 3: Write a Story (Past, Present, Future)

Tell a complete story using:
- Past Simple (what happened)
- Present Simple (the situation now)
- Future tenses (what will happen)

**Example topic:** A memorable trip

**Example:**
- Last summer, I went to Italy. I visited Rome and Venice. I saw the Colosseum and ate delicious pasta. It was amazing. Now I have many photos from that trip. I often look at them. I always remember that wonderful time. Next year, I'm going to return to Italy. I will visit Florence and Milan. I think I will love it even more!

**Your story:**

[Double-click to write your answer]

---

### Task 4: Compare Past and Future Self

Write about:
- How you were in the past
- Your habits and routines now
- Your plans for the future

**Example:**
- Five years ago, I was a student. I studied every day. I rarely traveled. Now I have a job. I usually work from home. I often meet friends. In the future, I'm going to start my own business. I will work hard. I think I will be successful.

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

### Module 16: Past Simple Regular Verbs
**My confidence:** ___/5

**What I need to review:**
- [ ] Adding -ed to regular verbs
- [ ] Spelling changes (study→studied, stop→stopped)
- [ ] Using with time expressions (yesterday, last week)
- [ ] Negative form (didn't + base verb)

**Notes:**

---

### Module 17: Past Simple Irregular Verbs
**My confidence:** ___/5

**What I need to review:**
- [ ] Common irregular verbs (go→went, see→saw, eat→ate)
- [ ] Not adding -ed to irregular verbs
- [ ] Memorizing irregular forms
- [ ] Using correctly in context

**Notes:**

---

### Module 18: Going To Future
**My confidence:** ___/5

**What I need to review:**
- [ ] Structure: am/is/are going to + verb
- [ ] Using for plans and intentions
- [ ] Using for predictions with evidence
- [ ] Question and negative forms

**Notes:**

---

### Module 19: Will Future
**My confidence:** ___/5

**What I need to review:**
- [ ] Structure: will + base verb
- [ ] Using for predictions
- [ ] Using for promises and offers
- [ ] Difference from 'going to'

**Notes:**

---

### Module 20: Adverbs of Frequency
**My confidence:** ___/5

**What I need to review:**
- [ ] Position before main verb
- [ ] Position after 'be'
- [ ] Order (always → usually → often → sometimes → rarely → never)
- [ ] Using with present simple

**Notes:**

---

### Overall A1 Reflection:

**What was the easiest part of A1 for you?**

[Your answer]

**What was the most challenging part of A1?**

[Your answer]

**How do you feel about completing A1 level?**

[Your answer]

**What are you most proud of learning?**

[Your answer]

---"""
        )
    )

    # Cell 11: Progress Display
    cells.append(
        nbf.v4.new_code_cell(
            """# Display Final Score
print("="*60)
print("🎓 FINAL A1 REVIEW COMPLETE!")
print("="*60)
print(f"\\nYour Score: {total_score}/{max_score}")
percentage = (total_score/max_score) * 100 if max_score > 0 else 0
print(f"Percentage: {percentage:.1f}%")
print()

if percentage >= 90:
    print("🌟🌟🌟 OUTSTANDING! You've MASTERED A1 level!")
    print("You're absolutely ready for A2 level!")
    print("\\n🎉 CONGRATULATIONS on completing A1! 🎉")
elif percentage >= 75:
    print("👏 EXCELLENT! You have strong A1 skills!")
    print("Review any weak areas, then move to A2.")
    print("\\n🎉 CONGRATULATIONS on completing A1! 🎉")
elif percentage >= 60:
    print("👍 GOOD! You're ready for A2 with some review.")
    print("Spend more time on challenging modules.")
    print("You've completed A1 - well done!")
else:
    print("💪 Keep practicing! Review the difficult modules.")
    print("Retake this review after more practice.")
    print("You're close to completing A1!")

print()
print("="*60)"""
        )
    )

    # Cell 12: Completion and CELEBRATION!
    cells.append(
        nbf.v4.new_markdown_cell(
            """---

## 🎉🎊🎓 CONGRATULATIONS! 🎓🎊🎉

# YOU HAVE COMPLETED A1 LEVEL!

---

## 🌟 What You've Accomplished

You have successfully learned and practiced:

### Grammar Foundations (Modules 1-5):
✅ Verb "to be" in all forms
✅ Personal pronouns (subject and object)
✅ Present Simple tense
✅ Articles (a, an, the)
✅ Basic sentence structure

### Nouns and Descriptions (Modules 6-10):
✅ Nouns and plurals (regular and irregular)
✅ Possessives (apostrophe 's and of)
✅ Adjectives (describing words)
✅ There is/are (existence and location)
✅ Prepositions (in, on, at, and more)

### Questions and Abilities (Modules 11-15):
✅ Question words (who, what, where, when, why, how)
✅ Can/Can't (ability and permission)
✅ Demonstratives (this, that, these, those)
✅ Like/Love/Hate + -ing (preferences)
✅ Past Simple was/were

### Past and Future (Modules 16-20):
✅ Past Simple regular verbs
✅ Past Simple irregular verbs
✅ Going to future
✅ Will future
✅ Adverbs of frequency

---

## 📊 Your A1 Achievement Summary

**Total Modules Completed:** 20 modules (80 notebooks!)

**Grammar Points Mastered:** 20+ essential structures

**Skills Gained:**
- 💬 Basic conversation ability
- 📖 Reading simple texts
- ✍️ Writing simple paragraphs
- 🎧 Understanding basic English
- 🗣️ Expressing yourself in English

---

## 🎯 What's Next: A2 Level

You're now ready to move to **A2 level**, where you'll learn:

- More complex tenses (Present Perfect, Past Continuous)
- Comparative and superlative adjectives
- Modal verbs (should, must, might)
- Conditional sentences (if clauses)
- More advanced vocabulary and expressions

---

## 💡 Tips for Continuing Your Journey

1. **Review regularly** - Come back to A1 material monthly
2. **Practice daily** - Even 15 minutes a day helps
3. **Use English in real life** - Watch movies, read books, talk to people
4. **Don't fear mistakes** - They're part of learning!
5. **Stay motivated** - You've proven you can do this!
6. **Keep a learning journal** - Track your progress
7. **Celebrate small wins** - You've already won big by completing A1!

---

## 🏆 Your A1 Certificate of Completion

```
╔════════════════════════════════════════════════╗
║                                                ║
║         CERTIFICATE OF COMPLETION              ║
║                                                ║
║              A1 ENGLISH LEVEL                  ║
║                                                ║
║           Successfully Completed               ║
║                                                ║
║              20 Modules                        ║
║              80 Lessons                        ║
║           Hundreds of Exercises                ║
║                                                ║
║     You are now ready for A2 level!            ║
║                                                ║
║           Congratulations! 🌟                  ║
║                                                ║
╚════════════════════════════════════════════════╝
```

---

## 🙏 Final Words

Learning a language is a journey, not a destination. You've taken important first steps, and you should be **incredibly proud** of yourself!

Every exercise you completed, every mistake you made and learned from, every time you practiced - all of that has built your English foundation.

**You didn't just learn grammar rules. You gained the ability to communicate in English!**

---

## 🚀 Ready for A2?

When you're ready to continue:
1. Review any A1 modules where you felt less confident
2. Take a short break (a few days) to let everything settle
3. Start A2 Level Module 1 when you're ready
4. Come back to A1 reviews every month for spaced repetition

---

# 🎊 WELL DONE! 🎊

## You completed A1 English level!

**Keep learning, keep practicing, keep growing!**

**Your English journey has just begun!**

---

*Generated with the English Learning Interactive Notebook System*

---"""
        )
    )

    # Save notebook
    nb.cells = cells
    return nb


if __name__ == "__main__":
    nb = create_review_notebook()
    output_path = "A1_Review_Modules_16-20.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    print(f"✅ Created: {output_path}")

    # Check file size
    import os

    size_kb = os.path.getsize(output_path) / 1024
    print(f"📏 File size: {size_kb:.2f} KB")
