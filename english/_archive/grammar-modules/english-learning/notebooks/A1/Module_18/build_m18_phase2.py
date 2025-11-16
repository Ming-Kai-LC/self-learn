"""
Builder script for Module 18 Phase 2: Going To Future - Controlled Practice
Target: 70+ exercises
"""

import nbformat as nbf


def create_notebook():
    nb = nbf.v4.new_notebook()
    cells = []

    # Title
    cells.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 2: Controlled Practice

## Overview
This phase contains **70+ controlled exercises** to help you master the "going to" future tense.

**Exercise Types:**
- Formation exercises
- Affirmative/Negative/Question conversion
- Error correction
- Gap-filling
- Sentence completion
- Multiple choice
- Time expression practice
- Usage selection (going to vs will preview)

**Target Level:** A1 (Elementary)
**Estimated Time:** 90-120 minutes"""
        )
    )

    # Exercise Set 1: Basic Formation
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 1: Basic Formation (10 exercises)

Form correct sentences using "going to" with the given elements."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 1-10: Form sentences with "going to"
exercises_1_10 = [
    {"subject": "I", "verb": "study", "complement": "English tonight"},
    {"subject": "She", "verb": "visit", "complement": "her parents tomorrow"},
    {"subject": "They", "verb": "buy", "complement": "a new car"},
    {"subject": "We", "verb": "have", "complement": "dinner at 7 PM"},
    {"subject": "He", "verb": "start", "complement": "his new job next week"},
    {"subject": "You", "verb": "love", "complement": "this movie"},
    {"subject": "It", "verb": "rain", "complement": "soon"},
    {"subject": "I", "verb": "call", "complement": "you later"},
    {"subject": "They", "verb": "travel", "complement": "to Japan next summer"},
    {"subject": "She", "verb": "learn", "complement": "to drive this year"}
]

print("EXERCISE 1-10: Form sentences with 'going to'\\n")
print("Instructions: Form correct sentences using the given elements.\\n")

for i, ex in enumerate(exercises_1_10, 1):
    print(f"{i}. {ex['subject']} / {ex['verb']} / {ex['complement']}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

# Answers
def form_sentence(subject, verb, complement):
    be_verbs = {"I": "am", "You": "are", "He": "is", "She": "is",
                "It": "is", "We": "are", "They": "are"}
    be = be_verbs[subject]
    return f"{subject} {be} going to {verb} {complement}."

for i, ex in enumerate(exercises_1_10, 1):
    answer = form_sentence(ex['subject'], ex['verb'], ex['complement'])
    print(f"{i}. {answer}")"""
        )
    )

    # Exercise Set 2: Affirmative to Negative
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 2: Affirmative to Negative (10 exercises)

Convert the affirmative sentences to negative."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 11-20: Convert to negative
exercises_11_20 = [
    "I'm going to work tomorrow.",
    "She's going to call you tonight.",
    "They're going to come to the party.",
    "We're going to watch the game.",
    "He's going to study medicine.",
    "You're going to like this restaurant.",
    "It's going to be easy.",
    "I'm going to wake up early.",
    "She's going to accept the offer.",
    "They're going to move to London."
]

print("EXERCISE 11-20: Convert to negative\\n")
print("Instructions: Change these affirmative sentences to negative.\\n")

for i, sentence in enumerate(exercises_11_20, 11):
    print(f"{i}. {sentence}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

# Answers
negative_forms = [
    "I'm not going to work tomorrow.",
    "She's not going to call you tonight. / She isn't going to call you tonight.",
    "They're not going to come to the party. / They aren't going to come to the party.",
    "We're not going to watch the game. / We aren't going to watch the game.",
    "He's not going to study medicine. / He isn't going to study medicine.",
    "You're not going to like this restaurant. / You aren't going to like this restaurant.",
    "It's not going to be easy. / It isn't going to be easy.",
    "I'm not going to wake up early.",
    "She's not going to accept the offer. / She isn't going to accept the offer.",
    "They're not going to move to London. / They aren't going to move to London."
]

for i, answer in enumerate(negative_forms, 11):
    print(f"{i}. {answer}")"""
        )
    )

    # Exercise Set 3: Questions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 3: Form Questions (10 exercises)

Convert the statements to yes/no questions."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 21-30: Form questions
exercises_21_30 = [
    "You're going to study tonight.",
    "She's going to visit her grandparents.",
    "They're going to buy a house.",
    "He's going to change his job.",
    "We're going to have a test tomorrow.",
    "It's going to rain this afternoon.",
    "You're going to come to the meeting.",
    "She's going to cook dinner tonight.",
    "They're going to travel next month.",
    "He's going to call you later."
]

print("EXERCISE 21-30: Form questions\\n")
print("Instructions: Convert these statements to yes/no questions.\\n")

for i, sentence in enumerate(exercises_21_30, 21):
    print(f"{i}. {sentence}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

# Answers
question_forms = [
    "Are you going to study tonight?",
    "Is she going to visit her grandparents?",
    "Are they going to buy a house?",
    "Is he going to change his job?",
    "Are we going to have a test tomorrow?",
    "Is it going to rain this afternoon?",
    "Are you going to come to the meeting?",
    "Is she going to cook dinner tonight?",
    "Are they going to travel next month?",
    "Is he going to call you later?"
]

for i, answer in enumerate(question_forms, 21):
    print(f"{i}. {answer}")"""
        )
    )

    # Exercise Set 4: Short Answers
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 4: Short Answers (10 exercises)

Provide short answers to these questions (both affirmative and negative)."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 31-40: Short answers
exercises_31_40 = [
    "Are you going to study tonight?",
    "Is she going to call you?",
    "Are they going to come to the party?",
    "Is he going to buy a new car?",
    "Are we going to have lunch together?",
    "Is it going to rain tomorrow?",
    "Are you going to watch the movie?",
    "Is she going to visit her parents?",
    "Are they going to help us?",
    "Is he going to study abroad?"
]

print("EXERCISE 31-40: Short answers\\n")
print("Instructions: Give both YES and NO short answers.\\n")

for i, question in enumerate(exercises_31_40, 31):
    print(f"{i}. {question}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

# Answers
short_answers = [
    ("Yes, I am.", "No, I'm not."),
    ("Yes, she is.", "No, she isn't. / No, she's not."),
    ("Yes, they are.", "No, they aren't. / No, they're not."),
    ("Yes, he is.", "No, he isn't. / No, he's not."),
    ("Yes, we are.", "No, we aren't. / No, we're not."),
    ("Yes, it is.", "No, it isn't. / No, it's not."),
    ("Yes, I am.", "No, I'm not."),
    ("Yes, she is.", "No, she isn't. / No, she's not."),
    ("Yes, they are.", "No, they aren't. / No, they're not."),
    ("Yes, he is.", "No, he isn't. / No, he's not.")
]

for i, (yes_ans, no_ans) in enumerate(short_answers, 31):
    print(f"{i}. YES: {yes_ans}  |  NO: {no_ans}")"""
        )
    )

    # Exercise Set 5: Error Correction
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 5: Error Correction (10 exercises)

Find and correct the mistakes in these sentences."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 41-50: Error correction
exercises_41_50 = [
    "I'm going to studying English.",
    "She going to visit her parents.",
    "They is going to buy a car.",
    "He are going to come tomorrow.",
    "We going study tonight.",
    "You're going to goes to the party?",
    "I'm going to be go there.",
    "She's not going to doesn't come.",
    "What you going to do tomorrow?",
    "He's going play football."
]

print("EXERCISE 41-50: Error correction\\n")
print("Instructions: Find and correct the mistake in each sentence.\\n")

for i, sentence in enumerate(exercises_41_50, 41):
    print(f"{i}. {sentence}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

# Answers
corrections = [
    ("I'm going to studying English.", "I'm going to study English.", "Wrong verb form"),
    ("She going to visit her parents.", "She's going to visit her parents.", "Missing 'is'"),
    ("They is going to buy a car.", "They are going to buy a car.", "Wrong 'be' form"),
    ("He are going to come tomorrow.", "He is going to come tomorrow.", "Wrong 'be' form"),
    ("We going study tonight.", "We're going to study tonight.", "Missing 'are' and 'to'"),
    ("You're going to goes to the party?", "Are you going to go to the party?", "Question form + verb form"),
    ("I'm going to be go there.", "I'm going to go there.", "Extra 'be'"),
    ("She's not going to doesn't come.", "She's not going to come.", "Double negative"),
    ("What you going to do tomorrow?", "What are you going to do tomorrow?", "Missing 'are'"),
    ("He's going play football.", "He's going to play football.", "Missing 'to'")
]

for i, (wrong, correct, error_type) in enumerate(corrections, 41):
    print(f"{i}. [X] {wrong}")
    print(f"    [OK] {correct}")
    print(f"    Error: {error_type}\\n")"""
        )
    )

    # Exercise Set 6: Gap Filling
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 6: Gap Filling (10 exercises)

Complete the sentences with the correct form of "going to" and the verb in parentheses."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 51-60: Gap filling
exercises_51_60 = [
    ("I _______ (study) for my exam tonight.", "I'm going to study"),
    ("She _______ (not/come) to the party.", "She's not going to come / She isn't going to come"),
    ("_______ (you/watch) the game tonight?", "Are you going to watch"),
    ("They _______ (travel) to Spain next summer.", "They're going to travel"),
    ("He _______ (not/buy) a new phone.", "He's not going to buy / He isn't going to buy"),
    ("_______ (it/rain) tomorrow?", "Is it going to rain"),
    ("We _______ (have) dinner at 7 PM.", "We're going to have"),
    ("_______ (she/call) you later?", "Is she going to call"),
    ("I _______ (not/go) to work tomorrow.", "I'm not going to go"),
    ("What _______ (you/do) this weekend?", "What are you going to do")
]

print("EXERCISE 51-60: Gap filling\\n")
print("Instructions: Complete with the correct form of 'going to' + verb.\\n")

for i, (question, _) in enumerate(exercises_51_60, 51):
    print(f"{i}. {question}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

for i, (question, answer) in enumerate(exercises_51_60, 51):
    print(f"{i}. {answer}")"""
        )
    )

    # Exercise Set 7: Wh- Questions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 7: Wh- Questions (10 exercises)

Form questions using the question words provided."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 61-70: Wh- questions
exercises_61_70 = [
    ("What / you / do / tonight", "What are you going to do tonight?"),
    ("Where / she / go / on vacation", "Where is she going to go on vacation?"),
    ("When / they / arrive", "When are they going to arrive?"),
    ("Who / help / us", "Who is going to help us?"),
    ("Why / he / leave / early", "Why is he going to leave early?"),
    ("How / you / get / there", "How are you going to get there?"),
    ("What time / the meeting / start", "What time is the meeting going to start?"),
    ("Where / we / meet", "Where are we going to meet?"),
    ("When / you / finish / this project", "When are you going to finish this project?"),
    ("How long / they / stay", "How long are they going to stay?")
]

print("EXERCISE 61-70: Form Wh- questions\\n")
print("Instructions: Use the words to form questions with 'going to'.\\n")

for i, (words, _) in enumerate(exercises_61_70, 61):
    print(f"{i}. {words}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

for i, (_, answer) in enumerate(exercises_61_70, 61):
    print(f"{i}. {answer}")"""
        )
    )

    # Exercise Set 8: Time Expressions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 8: Time Expressions (5 exercises)

Add appropriate time expressions to complete the sentences."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 71-75: Time expressions
exercises_71_75 = [
    ("I'm going to visit my parents _______.", ["this weekend", "next month", "tomorrow"]),
    ("She's going to start her new job _______.", ["next week", "in September", "soon"]),
    ("They're going to travel to Europe _______.", ["next summer", "in two months", "next year"]),
    ("We're going to have a meeting _______.", ["at 3 PM", "this afternoon", "tomorrow morning"]),
    ("He's going to call you _______.", ["later", "tonight", "in an hour"])
]

print("EXERCISE 71-75: Time expressions\\n")
print("Instructions: Choose or add an appropriate time expression.\\n")

for i, (sentence, options) in enumerate(exercises_71_75, 71):
    print(f"{i}. {sentence}")
    print(f"   Options: {', '.join(options)}\\n")

print("="*70)
print("POSSIBLE ANSWERS (many variations are correct):")
print("="*70 + "\\n")

for i, (sentence, options) in enumerate(exercises_71_75, 71):
    example_answer = sentence.replace("_______", options[0])
    print(f"{i}. {example_answer}")
    print(f"   (Also correct: {', '.join(options[1:])})")"""
        )
    )

    # Exercise Set 9: Plans vs Predictions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 9: Plans vs Predictions (5 exercises)

Identify whether each sentence expresses a PLAN or a PREDICTION."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 76-80: Plans vs Predictions
exercises_76_80 = [
    ("I'm going to study engineering at university.", "PLAN"),
    ("Look at those clouds! It's going to rain.", "PREDICTION"),
    ("We're going to have a baby next year.", "PLAN"),
    ("Be careful! You're going to fall!", "PREDICTION"),
    ("They're going to open a new restaurant.", "PLAN")
]

print("EXERCISE 76-80: Plans vs Predictions\\n")
print("Instructions: Identify if each sentence is a PLAN or PREDICTION.\\n")

for i, (sentence, _) in enumerate(exercises_76_80, 76):
    print(f"{i}. {sentence}")

print("\\n" + "="*70)
print("ANSWERS:")
print("="*70 + "\\n")

for i, (sentence, answer) in enumerate(exercises_76_80, 76):
    print(f"{i}. {answer} - {sentence}")"""
        )
    )

    # Exercise Set 10: Going To vs Will (Preview)
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Exercise Set 10: Going To vs Will - Preview (5 exercises)

Choose the better option (going to or will) for each situation."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Exercise 81-85: Going to vs will
exercises_81_85 = [
    {
        "situation": "A: The phone is ringing. B: I _______ answer it.",
        "options": ["'ll (will)", "'m going to"],
        "correct": "'ll (will)",
        "reason": "Spontaneous decision made at the moment"
    },
    {
        "situation": "I've decided. I _______ study medicine.",
        "options": ["'ll (will)", "'m going to"],
        "correct": "'m going to",
        "reason": "Already decided plan"
    },
    {
        "situation": "Look at the sky! It _______ storm.",
        "options": ["'ll (will)", "'s going to"],
        "correct": "'s going to",
        "reason": "Prediction based on evidence (dark sky)"
    },
    {
        "situation": "A: I don't have a pen. B: I _______ lend you one.",
        "options": ["'ll (will)", "'m going to"],
        "correct": "'ll (will)",
        "reason": "Spontaneous offer made now"
    },
    {
        "situation": "We _______ travel to Japan next summer. (booked tickets)",
        "options": ["'ll (will)", "'re going to"],
        "correct": "'re going to",
        "reason": "Already planned and arranged"
    }
]

print("EXERCISE 81-85: Going to vs Will\\n")
print("Instructions: Choose the better option for each situation.\\n")

for i, ex in enumerate(exercises_81_85, 81):
    print(f"{i}. {ex['situation']}")
    print(f"   Options: a) {ex['options'][0]}  b) {ex['options'][1]}\\n")

print("="*70)
print("ANSWERS:")
print("="*70 + "\\n")

for i, ex in enumerate(exercises_81_85, 81):
    print(f"{i}. Correct answer: {ex['correct']}")
    print(f"   Reason: {ex['reason']}\\n")"""
        )
    )

    # Summary
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Phase 2 Complete!

### Exercises Completed: 85

**You have practiced:**
- [OK] Forming "going to" sentences (10 exercises)
- [OK] Converting to negative (10 exercises)
- [OK] Forming questions (10 exercises)
- [OK] Short answers (10 exercises)
- [OK] Error correction (10 exercises)
- [OK] Gap filling (10 exercises)
- [OK] Wh- questions (10 exercises)
- [OK] Time expressions (5 exercises)
- [OK] Plans vs predictions (5 exercises)
- [OK] Going to vs will preview (5 exercises)

### What's Next?
In **Phase 3 (Meaningful Practice)**, you'll apply "going to" in meaningful contexts and real-life situations.

Great work! [TARGET]"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Phase 2 summary
summary = {
    "Total exercises": 85,
    "Exercise types": 10,
    "Skills practiced": [
        "Formation and structure",
        "Affirmative, negative, question forms",
        "Short answers",
        "Error identification and correction",
        "Gap filling",
        "Wh- questions",
        "Time expressions",
        "Usage distinction (plans vs predictions)",
        "Going to vs will (preview)"
    ],
    "Estimated time": "90-120 minutes"
}

print("PHASE 2 COMPLETION SUMMARY")
print("=" * 70)
print(f"\\nTotal Exercises Completed: {summary['Total exercises']}")
print(f"Exercise Types: {summary['Exercise types']}")
print(f"\\nSkills Practiced:")
for i, skill in enumerate(summary['Skills practiced'], 1):
    print(f"  {i}. {skill}")
print(f"\\nEstimated Time: {summary['Estimated time']}")
print("\\n" + "=" * 70)
print("[OK] Ready for Phase 3: Meaningful Practice!")
print("=" * 70)"""
        )
    )

    # Add all cells to notebook
    nb["cells"] = cells
    return nb


if __name__ == "__main__":
    notebook = create_notebook()
    output_path = "02_controlled_practice.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(notebook, f)

    print(f"Notebook created successfully: {output_path}")
    print(f"Total cells: {len(notebook['cells'])}")
    print(f"Total exercises: 85")
