"""
Builder script for Module 18 Phase 1: Going To Future - Introduction
Target: 18-22 KB, 40-50 cells
"""

import nbformat as nbf


def create_notebook():
    nb = nbf.v4.new_notebook()
    cells = []

    # Title and Overview
    cells.append(nbf.v4.new_markdown_cell("""# Module 18: Going To Future - Phase 1: Introduction

## Learning Objectives
By the end of this module, you will be able to:
- Form sentences using "going to" for future plans and intentions
- Use affirmative, negative, and question forms correctly
- Express plans, intentions, and predictions with evidence
- Use appropriate time expressions with "going to"
- Distinguish between "going to" and "will" (basic introduction)
- Understand common contractions and avoid typical mistakes

**Target Level:** A1 (Elementary)
**Estimated Time:** 90-120 minutes"""))

    # Section 1: Introduction to "Going To" Future
    cells.append(nbf.v4.new_markdown_cell("""## 1. Introduction to "Going To" Future

The "going to" future is one of the most common ways to talk about the future in English. We use it to express:
- **Plans and intentions** - things we have already decided to do
- **Predictions based on evidence** - things we can see are going to happen

### Why Use "Going To"?
- It shows you have already thought about or planned something
- It connects present evidence to future results
- It's very common in everyday conversation
- It sounds more natural for personal plans than "will"

### Examples in Context:
- **Plan:** "I'm going to study English tonight." (I decided this already)
- **Prediction:** "Look at those clouds! It's going to rain." (Evidence: dark clouds)"""))

    cells.append(nbf.v4.new_code_cell("""# Let's see some examples
examples = [
    "I'm going to visit my parents this weekend.",
    "She's going to start a new job next month.",
    "We're going to have dinner at 7 PM.",
    "They're going to buy a new car soon."
]

print("Examples of 'going to' for plans:\\n")
for i, example in enumerate(examples, 1):
    print(f"{i}. {example}")"""))

    # Section 2: Forming "Going To"
    cells.append(nbf.v4.new_markdown_cell("""## 2. Forming "Going To"

### Structure:
**Subject + am/is/are + going to + base verb**

| Subject | Be Verb | Going To | Base Verb | Rest of Sentence |
|---------|---------|----------|-----------|------------------|
| I | am | going to | visit | my friend |
| You | are | going to | study | tonight |
| He/She/It | is | going to | work | tomorrow |
| We | are | going to | travel | next week |
| They | are | going to | cook | dinner |

### Important Points:
1. The verb "be" (am/is/are) must match the subject
2. "going to" never changes
3. The main verb stays in base form (no -ing, no -s)
4. Contractions are very common in speaking

### Common Contractions:
- I am -> I'm
- You are -> You're
- He is -> He's
- She is -> She's
- It is -> It's
- We are -> We're
- They are -> They're"""))

    cells.append(nbf.v4.new_code_cell("""# Practice forming "going to" sentences
def form_going_to(subject, verb, complement):
    # Determine the correct form of "be"
    be_forms = {
        "I": "am",
        "You": "are",
        "He": "is",
        "She": "is",
        "It": "is",
        "We": "are",
        "They": "are"
    }

    be_verb = be_forms.get(subject, "are")
    sentence = f"{subject} {be_verb} going to {verb} {complement}."

    return sentence

# Test the function
test_cases = [
    ("I", "study", "English tomorrow"),
    ("She", "buy", "a new phone"),
    ("They", "visit", "Paris next summer"),
    ("We", "have", "a meeting at 3 PM")
]

print("Formed sentences:\\n")
for subject, verb, complement in test_cases:
    print(form_going_to(subject, verb, complement))"""))

    # Section 3: Affirmative Sentences
    cells.append(nbf.v4.new_markdown_cell("""## 3. Affirmative Sentences

Affirmative sentences state what someone IS going to do.

### Structure:
**Subject + am/is/are + going to + base verb + (complement)**

### Examples by Subject:

#### With "I":
- I'm going to learn Spanish.
- I'm going to call my mother tonight.
- I'm going to wake up early tomorrow.

#### With "You":
- You're going to love this movie!
- You're going to meet interesting people.
- You're going to improve quickly.

#### With "He/She/It":
- He's going to play football on Saturday.
- She's going to start university in September.
- It's going to be a beautiful day.

#### With "We":
- We're going to have a party next Friday.
- We're going to move to a new apartment.
- We're going to celebrate your birthday.

#### With "They":
- They're going to arrive at 8 o'clock.
- They're going to open a new restaurant.
- They're going to travel around Europe."""))

    cells.append(nbf.v4.new_code_cell("""# Practice with affirmative sentences
affirmative_examples = {
    "Personal plans": [
        "I'm going to exercise every morning.",
        "I'm going to read more books this year.",
        "I'm going to save money for a vacation."
    ],
    "Other people's plans": [
        "My brother is going to get married in June.",
        "Our teacher is going to give us a test tomorrow.",
        "My friends are going to visit me next weekend."
    ],
    "Predictions": [
        "The concert is going to be amazing!",
        "This movie is going to make you cry.",
        "The match is going to be very exciting."
    ]
}

for category, examples in affirmative_examples.items():
    print(f"\\n{category.upper()}:")
    for example in examples:
        print(f"  * {example}")"""))

    # Section 4: Negative Sentences
    cells.append(nbf.v4.new_markdown_cell("""## 4. Negative Sentences

Negative sentences state what someone is NOT going to do.

### Structure:
**Subject + am/is/are + not + going to + base verb**

### Contractions:
- am not -> I'm not (no contraction for "am not")
- is not -> isn't OR 's not
- are not -> aren't OR 're not

### Examples:

#### Full Forms:
- I am not going to work tomorrow.
- He is not going to come to the party.
- We are not going to buy a new car.
- They are not going to watch the movie.

#### Contracted Forms (More Common):
- I'm not going to work tomorrow.
- He isn't going to come to the party. / He's not going to come.
- We aren't going to buy a new car. / We're not going to buy a new car.
- They aren't going to watch the movie. / They're not going to watch it.

### Important Note:
In speaking, we usually use contractions. "I'm not" is much more common than "I am not".
"""))

    cells.append(nbf.v4.new_code_cell("""# Practice negative sentences
def make_negative(sentence):
    """Convert affirmative 'going to' sentence to negative"""
    # This is a simplified version for demonstration
    replacements = {
        "I'm going to": "I'm not going to",
        "You're going to": "You're not going to / You aren't going to",
        "He's going to": "He's not going to / He isn't going to",
        "She's going to": "She's not going to / She isn't going to",
        "It's going to": "It's not going to / It isn't going to",
        "We're going to": "We're not going to / We aren't going to",
        "They're going to": "They're not going to / They aren't going to"
    }

    for affirm, neg in replacements.items():
        if affirm in sentence:
            return sentence.replace(affirm, neg)
    return sentence

# Examples
affirmative_sentences = [
    "I'm going to study tonight.",
    "She's going to call you tomorrow.",
    "We're going to have a meeting.",
    "They're going to arrive late."
]

print("Affirmative -> Negative:\\n")
for sentence in affirmative_sentences:
    print(f"[OK] {sentence}")
    print(f"[X] {make_negative(sentence)}\\n")"""))

    # Section 5: Questions
    cells.append(nbf.v4.new_markdown_cell("""## 5. Questions with "Going To"

To form questions, we put the verb "be" (am/is/are) BEFORE the subject.

### Structure:
**Am/Is/Are + subject + going to + base verb...?**

### Yes/No Questions:

| Be Verb | Subject | Going To | Base Verb | Rest |
|---------|---------|----------|-----------|------|
| Am | I | going to | see | you tomorrow? |
| Are | you | going to | study | tonight? |
| Is | he | going to | come | to the party? |
| Is | she | going to | call | me later? |
| Are | we | going to | have | a test? |
| Are | they | going to | visit | us? |

### Examples:
- **Are you going to watch the game tonight?**
- **Is she going to accept the job offer?**
- **Are they going to move to a new house?**
- **Is it going to rain tomorrow?**
- **Are we going to meet at 6 PM?**

### Wh- Questions:
Add question words (What, Where, When, Who, Why, How) at the beginning:

- **What are you going to do this weekend?**
- **Where is he going to work?**
- **When are they going to arrive?**
- **Who is going to help us?**
- **Why are you going to leave early?**
- **How are we going to get there?**"""))

    cells.append(nbf.v4.new_code_cell("""# Practice forming questions
def form_question(subject, verb, complement, question_word=None):
    # Determine be verb
    be_forms = {
        "I": "Am",
        "you": "Are",
        "he": "Is",
        "she": "Is",
        "it": "Is",
        "we": "Are",
        "they": "Are"
    }

    be_verb = be_forms.get(subject, "Are")

    if question_word:
        return f"{question_word} {be_verb.lower()} {subject} going to {verb} {complement}?"
    else:
        return f"{be_verb} {subject} going to {verb} {complement}?"

# Examples
questions = [
    ("you", "come", "to the party", None),
    ("she", "study", "abroad", None),
    ("they", "buy", "a new car", None),
    ("you", "do", "this weekend", "What"),
    ("he", "travel", "", "Where"),
    ("we", "meet", "", "When")
]

print("Formed Questions:\\n")
for question_data in questions:
    subject, verb, complement, qword = question_data
    print(f"* {form_question(subject, verb, complement, qword)}")"""))

    # Section 6: Short Answers
    cells.append(nbf.v4.new_markdown_cell("""## 6. Short Answers

Short answers use the verb "be" (am/is/are) - we don't repeat "going to" and the main verb.

### Affirmative Short Answers:
- **Are you going to study tonight?** -> Yes, I am.
- **Is he going to come?** -> Yes, he is.
- **Are they going to help?** -> Yes, they are.

### Negative Short Answers:
- **Are you going to study tonight?** -> No, I'm not.
- **Is he going to come?** -> No, he isn't. / No, he's not.
- **Are they going to help?** -> No, they aren't. / No, they're not.

### Complete Answer Table:

| Question | Yes (Affirmative) | No (Negative) |
|----------|-------------------|---------------|
| Am I going to...? | Yes, you are. | No, you aren't. |
| Are you going to...? | Yes, I am. | No, I'm not. |
| Is he going to...? | Yes, he is. | No, he isn't. |
| Is she going to...? | Yes, she is. | No, she isn't. |
| Is it going to...? | Yes, it is. | No, it isn't. |
| Are we going to...? | Yes, we are. | No, we aren't. |
| Are they going to...? | Yes, they are. | No, they aren't. |

### Important Notes:
- Don't say: "Yes, I'm going to." [X]
- Say: "Yes, I am." [OK]
- We can expand: "Yes, I am. I'm going to study at the library." [OK]"""))

    cells.append(nbf.v4.new_code_cell("""# Practice short answers
qa_pairs = [
    ("Are you going to watch the movie?", "Yes, I am.", "No, I'm not."),
    ("Is she going to call you?", "Yes, she is.", "No, she isn't."),
    ("Are they going to visit us?", "Yes, they are.", "No, they aren't."),
    ("Is he going to study tonight?", "Yes, he is.", "No, he's not."),
    ("Are we going to have a test?", "Yes, we are.", "No, we're not.")
]

print("QUESTION -> SHORT ANSWERS\\n")
for question, yes_answer, no_answer in qa_pairs:
    print(f"Q: {question}")
    print(f"[OK] {yes_answer}")
    print(f"[X] {no_answer}")
    print()"""))

    # Section 7: Uses of "Going To"
    cells.append(nbf.v4.new_markdown_cell("""## 7. Uses of "Going To"

### Use 1: Plans and Intentions
We use "going to" for things we have already decided or planned to do.

**Examples:**
- I'm going to study medicine at university. (decided plan)
- We're going to get married next year. (intention)
- They're going to open a restaurant. (planned)
- She's going to learn to drive this summer. (intention)

**Key Point:** The decision was made BEFORE speaking.

### Use 2: Predictions Based on Evidence
We use "going to" when we can see or know something will happen because of present evidence.

**Examples:**
- Look at those dark clouds! It's going to rain. (evidence: clouds)
- Be careful! You're going to fall! (evidence: person losing balance)
- She's going to have a baby. (evidence: she's pregnant)
- They're going to win the match. (evidence: they're playing very well)

**Key Point:** There is present evidence or signs.

### Use 3: Things That Are About to Happen
When something is very close to happening:

**Examples:**
- Hurry up! The train is going to leave!
- Watch out! That glass is going to break!
- Quick! The movie is going to start!

### Summary Table:

| Use | When | Example |
|-----|------|---------|
| Plans/Intentions | Already decided | I'm going to visit my parents. |
| Predictions | Present evidence | It's going to rain. (see clouds) |
| Imminent | About to happen | The bus is going to leave! |"""))

    cells.append(nbf.v4.new_code_cell("""# Categorize uses of "going to"
sentences_by_use = {
    "Plans and Intentions": [
        "I'm going to start a new course next month.",
        "We're going to move to a bigger apartment.",
        "He's going to change jobs soon.",
        "They're going to have a party on Saturday."
    ],
    "Predictions with Evidence": [
        "Look at the time! We're going to be late!",
        "Those boxes look unstable. They're going to fall!",
        "The sky is getting dark. It's going to storm.",
        "She looks tired. She's going to sleep early tonight."
    ],
    "Imminent Actions": [
        "Watch out! That car is going to hit us!",
        "Hurry! The store is going to close!",
        "Quick! The plane is going to take off!",
        "Be careful! You're going to drop that!"
    ]
}

for use_type, examples in sentences_by_use.items():
    print(f"\\n{use_type.upper()}:")
    print("=" * 50)
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")"""))

    # Section 8: Time Expressions
    cells.append(nbf.v4.new_markdown_cell("""## 8. Time Expressions with "Going To"

Time expressions help us specify WHEN something is going to happen.

### Common Time Expressions:

#### Near Future:
- **tonight** - I'm going to study tonight.
- **today** - We're going to visit the museum today.
- **this morning/afternoon/evening** - She's going to call this afternoon.
- **later** - They're going to arrive later.
- **soon** - He's going to finish soon.

#### Tomorrow:
- **tomorrow** - I'm going to see the doctor tomorrow.
- **tomorrow morning/afternoon/evening/night** - We're going to leave tomorrow morning.

#### Next... :
- **next week** - She's going to start her new job next week.
- **next month** - They're going to get married next month.
- **next year** - I'm going to travel to Japan next year.
- **next Monday/Tuesday/etc.** - We're going to have a meeting next Friday.
- **next summer/winter/etc.** - He's going to study abroad next summer.

#### In + time period:
- **in a few minutes** - The bus is going to arrive in a few minutes.
- **in an hour** - I'm going to call you in an hour.
- **in a week** - They're going to move in a week.
- **in two months** - She's going to have a baby in two months.
- **in five years** - We're going to retire in five years.

#### Other Expressions:
- **this weekend** - Are you going to do anything this weekend?
- **on Monday** - I'm going to see the dentist on Monday.
- **at 5 o'clock** - We're going to meet at 5 o'clock.
- **in the future** - Everything is going to be okay in the future.

### Position in Sentence:
Time expressions usually come at the END of the sentence:
- [OK] I'm going to study **tonight**.
- [OK] We're going to leave **tomorrow morning**.

But they can also come at the BEGINNING for emphasis:
- [OK] **Tomorrow**, I'm going to start my diet.
- [OK] **Next week**, we're going to move."""))

    cells.append(nbf.v4.new_code_cell("""# Practice with time expressions
time_expression_examples = {
    "Today/Tonight/Soon": [
        ("I'm going to finish this work", "tonight"),
        ("We're going to have lunch", "today"),
        ("She's going to arrive", "soon"),
        ("They're going to call us", "later")
    ],
    "Tomorrow": [
        ("I'm going to wake up early", "tomorrow"),
        ("He's going to have an interview", "tomorrow afternoon"),
        ("We're going to watch a movie", "tomorrow night")
    ],
    "Next...": [
        ("I'm going to start university", "next year"),
        ("She's going to visit her parents", "next weekend"),
        ("They're going to open their shop", "next month"),
        ("We're going to have a holiday", "next summer")
    ],
    "In + time": [
        ("The meeting is going to start", "in 10 minutes"),
        ("I'm going to graduate", "in two years"),
        ("They're going to arrive", "in an hour"),
        ("She's going to return", "in a few days")
    ]
}

for category, examples in time_expression_examples.items():
    print(f"\\n{category}:")
    print("-" * 60)
    for sentence, time_expr in examples:
        print(f"  {sentence} {time_expr}.")"""))

    # Section 9: Going To vs Will (Brief Intro)
    cells.append(nbf.v4.new_markdown_cell("""## 9. "Going To" vs "Will" - Brief Introduction

Both "going to" and "will" express future, but we use them differently.

### When to Use "GOING TO":

#### 1. Planned Decisions (decided before speaking)
- [OK] **I'm going to study medicine.** (I decided this last month)
- [X] I will study medicine. (sounds like deciding now)

#### 2. Predictions with Evidence
- [OK] **Look at those clouds! It's going to rain.** (I can see clouds)
- [X] It will rain. (prediction without visible evidence)

### When to Use "WILL":

#### 1. Spontaneous Decisions (deciding at the moment of speaking)
- A: The phone is ringing.
- B: **I'll answer it.** (deciding now) [OK]

#### 2. Promises and Offers
- **I'll help you with your homework.** (promise)
- **I'll carry those bags for you.** (offer)

#### 3. General Predictions (without evidence)
- **I think it will rain tomorrow.** (general opinion)
- **She'll probably come to the party.** (prediction)

### Quick Comparison:

| Situation | Going To | Will |
|-----------|----------|------|
| Planned in advance | [OK] | [X] |
| Spontaneous decision | [X] | [OK] |
| Evidence-based prediction | [OK] | [X] |
| General prediction | [X] | [OK] |
| Promises/Offers | [X] | [OK] |

### Examples:

**Going To (Planned):**
- I'm going to visit my grandparents this weekend. (already planned)

**Will (Spontaneous):**
- A: I don't have a pen.
- B: I'll lend you one. (deciding now)

**Going To (Evidence):**
- She looks tired. She's going to sleep soon. (I can see she's tired)

**Will (General Prediction):**
- I think we'll have a great time. (general feeling)

**Note:** We'll study "will" in detail in the next module!"""))

    cells.append(nbf.v4.new_code_cell("""# Compare going to vs will
comparisons = {
    "Scenario 1: Vacation Plans": {
        "going_to": "We're going to travel to Italy next summer. (planned months ago)",
        "will": "A: Where should we go? B: I know! We'll go to Italy! (deciding now)"
    },
    "Scenario 2: Weather": {
        "going_to": "Look at the sky! It's going to rain any minute. (dark clouds visible)",
        "will": "I think it will rain sometime this week. (general prediction)"
    },
    "Scenario 3: Job Change": {
        "going_to": "I'm going to quit my job next month. (already decided)",
        "will": "If I don't like it, I'll quit. (spontaneous thought)"
    },
    "Scenario 4: Help Offer": {
        "going_to": "I'm going to help you move next weekend. (planned to help)",
        "will": "Those boxes look heavy. I'll help you! (spontaneous offer)"
    }
}

print("GOING TO vs WILL - Contextual Differences\\n")
print("=" * 70)
for scenario, examples in comparisons.items():
    print(f"\\n{scenario}:")
    print(f"  GOING TO: {examples['going_to']}")
    print(f"  WILL:     {examples['will']}")"""))

    # Section 10: Common Contractions
    cells.append(nbf.v4.new_markdown_cell("""## 10. Common Contractions with "Going To"

Contractions make your English sound more natural and fluent. They're essential for everyday conversation!

### Standard Contractions with "Be":

| Full Form | Contraction | Example |
|-----------|-------------|---------|
| I am going to | I'm going to | I'm going to study. |
| You are going to | You're going to | You're going to love it! |
| He is going to | He's going to | He's going to call. |
| She is going to | She's going to | She's going to come. |
| It is going to | It's going to | It's going to rain. |
| We are going to | We're going to | We're going to leave. |
| They are going to | They're going to | They're going to win. |

### Negative Contractions:

| Full Form | Contraction 1 | Contraction 2 |
|-----------|---------------|---------------|
| I am not going to | I'm not going to | (no second form) |
| You are not going to | You're not going to | You aren't going to |
| He is not going to | He's not going to | He isn't going to |
| She is not going to | She's not going to | She isn't going to |
| It is not going to | It's not going to | It isn't going to |
| We are not going to | We're not going to | We aren't going to |
| They are not going to | They're not going to | They aren't going to |

### Informal Spoken Contraction: "Gonna"

In **very informal** speech, native speakers often say "gonna" instead of "going to":

- I'm gonna study. (informal) = I'm going to study. (standard)
- She's gonna call. (informal) = She's going to call. (standard)
- We're gonna leave. (informal) = We're going to leave. (standard)

**Important Notes about "Gonna":**
- [!] "Gonna" is only for speaking - NEVER write it in formal contexts
- [!] Only use "gonna" for casual conversation
- [!] In writing, always use "going to"
- [!] For exams and formal situations, use "going to"

### Pronunciation Tips:

**"Going to"** in connected speech:
- Written: going to -> Pronounced: /ˈɡoʊɪŋ tu/ or /ˈɡənə/ (gonna)
- The "t" in "to" often becomes soft or disappears
- It sounds like one word, not three

**Examples of natural pronunciation:**
- "I'm going to go" -> sounds like "I'm gonna go"
- "We're going to eat" -> sounds like "We're gonna eat"
- "She's going to come" -> sounds like "She's gonna come"

### Practice:
Try saying these quickly and naturally:
1. I'm going to study -> I'm gonna study
2. You're going to love this -> You're gonna love this
3. He's going to be late -> He's gonna be late
4. We're going to have fun -> We're gonna have fun"""))

    cells.append(nbf.v4.new_code_cell("""# Contraction practice
contractions_table = [
    ("I am going to visit my friend", "I'm going to visit my friend", "I'm gonna visit my friend"),
    ("She is going to call you later", "She's going to call you later", "She's gonna call you later"),
    ("We are going to watch a movie", "We're going to watch a movie", "We're gonna watch a movie"),
    ("They are going to help us", "They're going to help us", "They're gonna help us"),
    ("He is not going to come", "He's not going to come / He isn't going to come", "He's not gonna come")
]

print("CONTRACTION PRACTICE")
print("=" * 80)
print(f"{'Full Form':<35} {'Standard':<30} {'Informal (Spoken)'}")
print("-" * 80)

for full, standard, informal in contractions_table:
    print(f"{full:<35} {standard:<30} {informal}")

print("\\n[!]  Remember: Use 'gonna' only in casual spoken English!")
print("[NOTE] In writing and formal situations, always use 'going to'.")"""))

    # Section 11: Common Mistakes
    cells.append(nbf.v4.new_markdown_cell("""## 11. Common Mistakes with "Going To"

### Mistake 1: Wrong Verb Form After "Going To"
[X] **WRONG:** I'm going to studying English.
[OK] **CORRECT:** I'm going to study English.

[X] **WRONG:** She's going to goes to the party.
[OK] **CORRECT:** She's going to go to the party.

**Rule:** After "going to", use the BASE FORM of the verb (no -ing, no -s, no -ed).

### Mistake 2: Forgetting "To"
[X] **WRONG:** I'm going study.
[OK] **CORRECT:** I'm going to study.

[X] **WRONG:** We're going travel next week.
[OK] **CORRECT:** We're going to travel next week.

**Rule:** Don't forget the word "to" between "going" and the main verb.

### Mistake 3: Wrong Form of "Be"
[X] **WRONG:** He are going to come.
[OK] **CORRECT:** He is going to come.

[X] **WRONG:** They is going to help.
[OK] **CORRECT:** They are going to help.

**Rule:** Use the correct form of "be" (am/is/are) that matches the subject.

### Mistake 4: Using "Going To" for Spontaneous Decisions
[X] **WRONG:** A: The doorbell is ringing. B: I'm going to answer it.
[OK] **CORRECT:** A: The doorbell is ringing. B: I'll answer it.

**Rule:** Use "will" for spontaneous decisions made at the moment of speaking.

### Mistake 5: Word Order in Questions
[X] **WRONG:** You are going to do what?
[OK] **CORRECT:** What are you going to do?

[X] **WRONG:** He is going to where?
[OK] **CORRECT:** Where is he going to go?

**Rule:** In questions, put the "be" verb before the subject: Am/Is/Are + subject + going to...?

### Mistake 6: Using "Going To" with "Be" Verb
[X] **WRONG:** I'm going to be go there.
[OK] **CORRECT:** I'm going to go there.
OR
[OK] **CORRECT:** I'm going to be there.

**Rule:** Don't use two verbs after "going to". Choose one.

### Mistake 7: Double Negative
[X] **WRONG:** I'm not going to don't study.
[OK] **CORRECT:** I'm not going to study.

**Rule:** Don't use "not" twice. Put "not" after "be" only.

### Mistake 8: Writing "Gonna" in Formal Contexts
[X] **WRONG:** (In an essay) I am gonna study medicine.
[OK] **CORRECT:** I am going to study medicine.

**Rule:** Never write "gonna" in formal writing, emails, or academic work.

### Quick Reference - Common Errors:

| [X] Wrong | [OK] Correct |
|---------|-----------|
| I'm going to studying | I'm going to study |
| She going to come | She's going to come |
| He are going to go | He is going to go |
| You going study? | Are you going to study? |
| I'm going to be go | I'm going to go |
| I not going to come | I'm not going to come |
| What you going to do? | What are you going to do? |
| I gonna write (formal) | I am going to write |"""))

    cells.append(nbf.v4.new_code_cell("""# Common mistakes correction exercise
mistakes_and_corrections = [
    {
        "wrong": "I'm going to studying English tomorrow.",
        "error": "Wrong verb form after 'going to'",
        "correct": "I'm going to study English tomorrow.",
        "rule": "Use BASE FORM after 'going to'"
    },
    {
        "wrong": "She going to visit her parents.",
        "error": "Missing 'is'",
        "correct": "She is going to visit her parents. / She's going to visit her parents.",
        "rule": "Don't forget the 'be' verb"
    },
    {
        "wrong": "They is going to play football.",
        "error": "Wrong form of 'be'",
        "correct": "They are going to play football.",
        "rule": "Use 'are' with 'they'"
    },
    {
        "wrong": "What you are going to do?",
        "error": "Wrong word order",
        "correct": "What are you going to do?",
        "rule": "Question word + be + subject + going to + verb"
    },
    {
        "wrong": "I'm going visit my friend.",
        "error": "Missing 'to'",
        "correct": "I'm going to visit my friend.",
        "rule": "Don't forget 'to' in 'going to'"
    },
    {
        "wrong": "He not going to come.",
        "error": "Incomplete negative",
        "correct": "He is not going to come. / He isn't going to come.",
        "rule": "Use 'be + not' for negatives"
    }
]

print("COMMON MISTAKES - CORRECTION GUIDE")
print("=" * 80)

for i, mistake in enumerate(mistakes_and_corrections, 1):
    print(f"\\n{i}. ERROR TYPE: {mistake['error']}")
    print(f"   [X] Wrong:   {mistake['wrong']}")
    print(f"   [OK] Correct: {mistake['correct']}")
    print(f"   📌 Rule:    {mistake['rule']}")"""))

    # Section 12: Practice Conversations
    cells.append(nbf.v4.new_markdown_cell("""## 12. Practice Conversations

Practice these dialogues to improve your fluency with "going to".

### Conversation 1: Weekend Plans
**A:** What are you going to do this weekend?
**B:** I'm going to visit my grandparents on Saturday. What about you?
**A:** I'm not going to do anything special. I'm just going to relax at home.
**B:** That sounds nice! Are you going to watch any movies?
**A:** Yes, I'm going to watch the new action movie everyone is talking about.
**B:** Oh, I want to see that too! Maybe I'm going to watch it on Sunday.

### Conversation 2: Future Plans
**A:** So, what are you going to do after you graduate?
**B:** I'm going to look for a job in marketing. I'm also going to travel for a few months.
**A:** Wow! Where are you going to go?
**B:** I'm going to visit Thailand, Vietnam, and maybe Japan.
**A:** That's amazing! When are you going to leave?
**B:** I'm going to leave in June, right after graduation.
**A:** Are you going to travel alone?
**B:** No, my friend is going to come with me. We're going to travel together.

### Conversation 3: Making Predictions
**A:** Look at those dark clouds!
**B:** Yes, it's going to rain soon. We should go inside.
**A:** You're right. It's going to be a big storm, I think.
**B:** Do you have an umbrella?
**A:** No, I don't. I'm going to get wet!
**B:** Don't worry. I have two umbrellas. I'm going to lend you one.
**A:** Thanks! That's very kind of you.

### Conversation 4: Party Invitation
**A:** Are you going to come to my birthday party next Saturday?
**B:** Yes, definitely! I'm going to be there. What time is it going to start?
**A:** It's going to start at 7 PM. We're going to have dinner first, then dancing.
**B:** Great! What are you going to serve for dinner?
**A:** We're going to have pizza and salad. Is that okay?
**B:** Perfect! I love pizza. How many people are going to come?
**A:** About 20 people are going to come. It's going to be fun!
**B:** I'm sure it is! I'm going to bring a gift, of course.

### Conversation 5: Job Interview
**A:** I have a job interview tomorrow. I'm so nervous!
**B:** Don't worry. You're going to do great! What company is it?
**A:** It's at Tech Solutions. The interview is going to be at 10 AM.
**B:** What are you going to wear?
**A:** I'm going to wear my blue suit. I'm also going to prepare some questions tonight.
**B:** Good idea! Are you going to drive there?
**A:** No, I'm going to take the train. I don't want to worry about parking.
**B:** Smart! You're going to be fine. Just be confident!

### Conversation 6: Vacation Preparation
**A:** We're going to leave for our vacation tomorrow morning!
**B:** How exciting! Where are you going to stay?
**A:** We're going to stay at a hotel near the beach.
**B:** Sounds wonderful! How long are you going to be there?
**A:** We're going to stay for two weeks.
**B:** Two weeks! You're going to have a great time! What are you going to do there?
**A:** We're going to swim, relax, and explore the local restaurants. We're also going to visit some historical sites.
**B:** Have you packed yet?
**A:** Not yet. I'm going to pack tonight. My husband is going to help me.
**B:** Well, have an amazing trip! You're going to love it!"""))

    cells.append(nbf.v4.new_code_cell("""# Analyze conversations for "going to" usage
conversation_analysis = {
    "Conversation 1: Weekend Plans": {
        "going_to_count": 8,
        "main_uses": ["Plans", "Intentions"],
        "key_phrases": [
            "What are you going to do this weekend?",
            "I'm going to visit my grandparents",
            "I'm just going to relax at home"
        ]
    },
    "Conversation 2: Future Plans": {
        "going_to_count": 11,
        "main_uses": ["Plans", "Intentions", "Future arrangements"],
        "key_phrases": [
            "what are you going to do after you graduate?",
            "I'm going to look for a job",
            "Where are you going to go?"
        ]
    },
    "Conversation 3: Making Predictions": {
        "going_to_count": 7,
        "main_uses": ["Predictions with evidence", "Offers"],
        "key_phrases": [
            "it's going to rain soon",
            "It's going to be a big storm",
            "I'm going to get wet!"
        ]
    },
    "Conversation 4: Party Invitation": {
        "going_to_count": 12,
        "main_uses": ["Plans", "Arrangements", "Predictions"],
        "key_phrases": [
            "Are you going to come to my party?",
            "What time is it going to start?",
            "It's going to be fun!"
        ]
    },
    "Conversation 5: Job Interview": {
        "going_to_count": 10,
        "main_uses": ["Plans", "Intentions", "Predictions"],
        "key_phrases": [
            "I have a job interview tomorrow",
            "You're going to do great!",
            "What are you going to wear?"
        ]
    },
    "Conversation 6: Vacation Preparation": {
        "going_to_count": 13,
        "main_uses": ["Plans", "Future arrangements", "Predictions"],
        "key_phrases": [
            "Where are you going to stay?",
            "You're going to have a great time!",
            "What are you going to do there?"
        ]
    }
}

print("CONVERSATION ANALYSIS - 'GOING TO' USAGE")
print("=" * 70)

for conv_name, analysis in conversation_analysis.items():
    print(f"\\n{conv_name}")
    print(f"  'Going to' occurrences: {analysis['going_to_count']}")
    print(f"  Main uses: {', '.join(analysis['main_uses'])}")
    print(f"  Key phrases:")
    for phrase in analysis['key_phrases']:
        print(f"    * {phrase}")"""))

    # Summary and Review
    cells.append(nbf.v4.new_markdown_cell("""## Summary and Review

### Key Points to Remember:

#### 1. Formation
- **Structure:** Subject + am/is/are + going to + base verb
- **Example:** I'm going to study tonight.

#### 2. Uses
- **Plans and intentions** (decided before now)
- **Predictions with evidence** (we can see signs)
- **Things about to happen** (imminent)

#### 3. Forms
- **Affirmative:** I'm going to go.
- **Negative:** I'm not going to go. / I'm not gonna go.
- **Question:** Are you going to go?
- **Short answer:** Yes, I am. / No, I'm not.

#### 4. Important Rules
- [OK] Use BASE FORM after "going to"
- [OK] Match "be" verb with subject (am/is/are)
- [OK] Don't forget "to" in "going to"
- [OK] Use contractions in speaking
- [OK] "Gonna" is only for informal speaking

#### 5. Common Time Expressions
- tonight, today, tomorrow
- next week/month/year
- this weekend
- soon, later
- in + time period

#### 6. Going To vs Will (Quick)
- **Going to:** planned decisions, evidence-based predictions
- **Will:** spontaneous decisions, promises, general predictions

### What's Next?
In **Phase 2 (Controlled Practice)**, you'll do exercises to master:
- Forming sentences correctly
- Choosing between affirmative/negative/question
- Using time expressions appropriately
- Avoiding common mistakes

Keep practicing! [TARGET]"""))

    cells.append(nbf.v4.new_code_cell("""# Module summary statistics
summary_stats = {
    "Total sections": 12,
    "Main topics covered": [
        "Introduction to 'going to'",
        "Formation and structure",
        "Affirmative sentences",
        "Negative sentences",
        "Questions and short answers",
        "Uses (plans, predictions, imminent)",
        "Time expressions",
        "'Going to' vs 'will' (intro)",
        "Contractions and pronunciation",
        "Common mistakes",
        "Practice conversations"
    ],
    "Grammar points": 15,
    "Example sentences": "100+",
    "Practice conversations": 6,
    "Time to complete": "90-120 minutes"
}

print("MODULE 18 - PHASE 1 SUMMARY")
print("=" * 70)
print(f"\\nTotal Sections: {summary_stats['Total sections']}")
print(f"\\nTopics Covered:")
for i, topic in enumerate(summary_stats['Main topics covered'], 1):
    print(f"  {i}. {topic}")

print(f"\\nGrammar Points Covered: {summary_stats['Grammar points']}")
print(f"Example Sentences: {summary_stats['Example sentences']}")
print(f"Practice Conversations: {summary_stats['Practice conversations']}")
print(f"Estimated Completion Time: {summary_stats['Time to complete']}")

print("\\n" + "=" * 70)
print("[OK] Phase 1 Complete! Ready for Phase 2: Controlled Practice")
print("=" * 70)"""))

    # Add all cells to notebook
    nb['cells'] = cells
    return nb

if __name__ == "__main__":
    notebook = create_notebook()
    output_path = "01_introduction.ipynb"

    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(notebook, f)

    print(f"Notebook created successfully: {output_path}")
    print(f"Total cells: {len(notebook['cells'])}")
