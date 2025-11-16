"""
Builder script for Module 17 Phase 1: Past Simple - Irregular Verbs - Introduction
Target: 18-22 KB, 40-50 cells, 11 comprehensive sections
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
            "source": content,
        }


def build_phase1_notebook():
    """Build the complete Phase 1 notebook"""
    cells = []
    cell_counter = 0

    # Cell 0: Title and Introduction
    cells.append(
        create_cell(
            "markdown",
            """# Module 17: Past Simple - Irregular Verbs - Introduction

## 📚 Phase 1: Introduction (15% of learning time)

**Welcome to Module 17!** 🎉

In this module, you'll learn the **Past Simple tense** using **WAS** and **WERE** - the past forms of the verb TO BE. This is your first step into talking about the past in English!

### Learning Objectives
By the end of this module, you will be able to:
- ✅ Use WAS/WERE to describe past states and situations
- ✅ Form affirmative sentences (I was, you were, etc.)
- ✅ Form negative sentences (wasn't, weren't)
- ✅ Ask questions in the past (Was I...? Were you...?)
- ✅ Give short answers (Yes, I was / No, I wasn't)
- ✅ Use time expressions with the past (yesterday, last week, ago)
- ✅ Use WAS/WERE for descriptions, locations, and states
- ✅ Use there was / there were
- ✅ Understand when to use WAS vs WERE
- ✅ Avoid common mistakes
- ✅ Have conversations about the past

### Time Requirement
⏱️ Estimated time: 6-8 hours (spread across multiple sessions)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 1: Setup
    cells.append(
        create_cell(
            "code",
            """# Setup: Import utilities
import sys
sys.path.append('../../../utils')

from audio_generator import AudioGenerator, create_pronunciation_guide
from IPython.display import display, HTML

# Initialize audio generator
audio = AudioGenerator(audio_dir="audio")

print("✅ Setup complete! Let's learn about Past Simple irregular verbs!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 2: Section 1 - Introduction to Past Simple with Irregular Verbs
    cells.append(
        create_cell(
            "markdown",
            """## 1. Introduction to Past Simple with Irregular Verbs ⏰

**WAS** and **WERE** are the **past forms** of the verb **TO BE**.

### Present vs Past:
| Present | Past | Use |
|---------|------|-----|
| I **am** | I **was** | First person singular |
| You **are** | You **were** | Second person |
| He/She/It **is** | He/She/It **was** | Third person singular |
| We **are** | We **were** | First person plural |
| They **are** | They **were** | Third person plural |

### When do we use WAS/WERE?
We use WAS/WERE to talk about:
1. **States in the past**: I was tired yesterday.
2. **Descriptions in the past**: She was beautiful.
3. **Locations in the past**: They were at home.
4. **Ages in the past**: I was 10 years old.
5. **Weather in the past**: It was sunny.
6. **Feelings in the past**: We were happy.

### Key Point:
🎯 **WAS** = singular (I, he, she, it)
🎯 **WERE** = plural (you, we, they) + you (singular and plural)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 3: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Past Simple examples
audio.play_audio("I was at school yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They were very happy.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She was my teacher.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 6: Section 2 - Irregular Verbs Forms and Usage
    cells.append(
        create_cell(
            "markdown",
            """## 2. Irregular Verbs - Forms and Usage 📝

### Complete Conjugation:

| Subject | Past Form | Example |
|---------|-----------|---------|
| I | was | I was at home. |
| You | were | You were late. |
| He | was | He was tired. |
| She | was | She was happy. |
| It | was | It was cold. |
| We | were | We were students. |
| They | were | They were here. |

### Structure:
```
Subject + WAS/WERE + complement
```

### Important Rules:
1. **WAS** is used with: I, he, she, it
2. **WERE** is used with: you, we, they
3. **WERE** is always used with "you" (even for one person)

### Examples:
✅ I **was** a student.
✅ You **were** my friend.
✅ He **was** a doctor.
✅ She **was** beautiful.
✅ It **was** expensive.
✅ We **were** at the park.
✅ They **were** teachers.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 7: Section 3 - Affirmative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## 3. Affirmative Sentences (Positive Statements) ✅

### Structure:
```
Subject + WAS/WERE + complement
```

### Examples with Different Complements:

**With Adjectives (descriptions):**
- I **was** happy yesterday.
- She **was** beautiful.
- They **were** tired.
- It **was** hot.

**With Nouns (occupations, relationships):**
- I **was** a teacher.
- He **was** my friend.
- We **were** students.
- They **were** classmates.

**With Locations (where):**
- I **was** at home.
- She **was** in London.
- We **were** at the beach.
- They **were** in the park.

**With Ages:**
- I **was** 10 years old.
- She **was** very young.
- We **were** teenagers.

**With Time:**
- It **was** Monday.
- It **was** 3 o'clock.
- It **was** morning.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 8-10: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Affirmative sentence examples
audio.play_audio("I was happy yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She was at the library.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We were best friends.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 11: Section 4 - Negative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## 4. Negative Sentences 🚫

### Structure:
```
Subject + WAS/WERE + NOT + complement
Subject + WASN'T/WEREN'T + complement (contraction)
```

### Full Forms and Contractions:
| Full Form | Contraction | Example |
|-----------|-------------|---------|
| was not | wasn't | I wasn't there. |
| were not | weren't | They weren't happy. |

### Examples:

**Full Forms:**
- I **was not** at home.
- She **was not** tired.
- We **were not** ready.
- They **were not** students.

**Contractions (more common in speaking):**
- I **wasn't** at home.
- She **wasn't** tired.
- We **weren't** ready.
- They **weren't** students.

### More Examples:

**With Adjectives:**
- I **wasn't** happy.
- He **wasn't** angry.
- We **weren't** sad.
- They **weren't** busy.

**With Locations:**
- I **wasn't** at school.
- She **wasn't** in the office.
- We **weren't** at the party.

**With Nouns:**
- I **wasn't** a teacher.
- He **wasn't** my boyfriend.
- They **weren't** friends.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 12-14: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Negative sentence examples
audio.play_audio("I wasn't at school yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They weren't happy about the news.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She wasn't my teacher.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 15: Section 5 - Questions
    cells.append(
        create_cell(
            "markdown",
            """## 5. Questions with Irregular Verbs ❓

### Structure:
```
WAS/WERE + subject + complement?
```

### Yes/No Questions:
- **Was** I late?
- **Were** you at home?
- **Was** he angry?
- **Was** she there?
- **Was** it expensive?
- **Were** we right?
- **Were** they students?

### Wh- Questions:
We can combine question words with WAS/WERE:

| Question Word | Example |
|---------------|---------|
| **Where** | Where **was** she? |
| **When** | When **was** the party? |
| **Why** | Why **were** you late? |
| **Who** | Who **was** your teacher? |
| **What** | What **was** your job? |
| **How** | How **was** the movie? |
| **How old** | How old **were** you? |
| **How much** | How much **was** it? |

### Examples:
- **Where were** you yesterday?
- **When was** your birthday?
- **Why was** she sad?
- **Who were** they?
- **What was** his name?
- **How was** your day?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 16-18: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Question examples
audio.play_audio("Were you at home yesterday?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Where was she last night?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("How was your weekend?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 19: Section 6 - Short Answers
    cells.append(
        create_cell(
            "markdown",
            """## 6. Short Answers 👍👎

### Structure:
```
Yes, + subject + irregular verbs.
No, + subject + wasn't/weren't.
```

### Complete Table of Short Answers:

| Question | Positive Answer | Negative Answer |
|----------|----------------|------------------|
| Was I right? | Yes, you were. | No, you weren't. |
| Were you late? | Yes, I was. | No, I wasn't. |
| Was he angry? | Yes, he was. | No, he wasn't. |
| Was she there? | Yes, she was. | No, she wasn't. |
| Was it good? | Yes, it was. | No, it wasn't. |
| Were we wrong? | Yes, you were. | No, you weren't. |
| Were they happy? | Yes, they were. | No, they weren't. |

### Important Rules:
1. **Don't repeat the complement** in short answers:
   - Was she happy? → Yes, she was. ✅ (NOT "Yes, she was happy.")

2. **Don't use contractions in positive short answers:**
   - Yes, I was. ✅ (NOT "Yes, I's.")
   - No, I wasn't. ✅

3. **Match the subject:**
   - Were you tired? → Yes, I was. (switch from "you" to "I")
   - Was I late? → No, you weren't. (switch from "I" to "you")

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 20-21: Conversation examples
    cells.append(
        create_cell(
            "code",
            """# Short answer conversation
audio.create_conversation_audio([
    ("Person A", "Were you at the party last night?"),
    ("Person B", "Yes, I was. Were you?"),
    ("Person A", "No, I wasn't. I was at home.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.create_conversation_audio([
    ("Student", "Was the test difficult?"),
    ("Teacher", "No, it wasn't. It was quite easy.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 22: Section 7 - Time Expressions
    cells.append(
        create_cell(
            "markdown",
            """## 7. Time Expressions with Past Simple 📅

When we talk about the past, we use specific time expressions to show WHEN something happened.

### Common Time Expressions:

**Yesterday:**
- yesterday
- yesterday morning
- yesterday afternoon
- yesterday evening

**Last:**
- last night
- last week
- last month
- last year
- last Monday
- last summer
- last weekend

**Ago:**
- a minute ago
- an hour ago
- two days ago
- three weeks ago
- a month ago
- five years ago

**Other Time Expressions:**
- in 2020
- in January
- on Monday
- on my birthday
- this morning (if it's now afternoon)
- when I was young
- when I was a child

### Examples:
- I **was** tired **yesterday**.
- She **was** here **last week**.
- They **were** students **two years ago**.
- It **was** cold **in January**.
- We **were** at the beach **last summer**.
- He **was** my teacher **when I was young**.

### Word Order:
Time expressions usually go at the END of the sentence:
```
Subject + irregular verbs + complement + TIME EXPRESSION
```

Example: I was at school yesterday. ✅

They can also go at the BEGINNING (for emphasis):
```
TIME EXPRESSION, subject + irregular verbs + complement
```

Example: Yesterday, I was at school. ✅

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 23-25: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Time expression examples
audio.play_audio("I was at the cinema last night.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She was here two hours ago.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They were in Paris last summer.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 26: Section 8 - Common Uses
    cells.append(
        create_cell(
            "markdown",
            """## 8. Common Uses of Irregular Verbs 🎯

### 1. Physical Descriptions in the Past
Describing how someone/something looked:
- She **was** very beautiful.
- He **was** tall and strong.
- They **were** very young.
- The house **was** big and white.

### 2. Emotional States
Describing feelings and emotions:
- I **was** happy.
- She **was** sad.
- We **were** excited.
- They **were** afraid.
- He **was** angry.

### 3. Locations
Saying where someone/something was:
- I **was** at home.
- She **was** in London.
- We **were** at the park.
- They **were** in the office.
- The keys **were** on the table.

### 4. Ages
Talking about age in the past:
- I **was** 10 years old.
- She **was** very young.
- They **were** teenagers.

### 5. Occupations and Roles
Past jobs or positions:
- I **was** a student.
- He **was** a teacher.
- She **was** a doctor.
- We **were** colleagues.

### 6. Weather
Describing past weather:
- It **was** sunny yesterday.
- It **was** very cold.
- It **was** rainy last week.

### 7. Time
Stating what time/day it was:
- It **was** Monday.
- It **was** 3 o'clock.
- It **was** morning.

### 8. Prices
Past prices:
- The ticket **was** $20.
- The shoes **were** expensive.
- It **was** very cheap.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 27-29: Audio examples
    cells.append(
        create_cell(
            "code",
            """# Common uses examples
audio.play_audio("The weather was beautiful yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("I was a teacher ten years ago.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("The movie was very interesting.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 30: Section 9 - There was/There were
    cells.append(
        create_cell(
            "markdown",
            """## 9. There Was / There Were 🔍

We use **THERE WAS** and **THERE WERE** to say that something existed in the past.

### Rules:
- **THERE WAS** + singular noun
- **THERE WERE** + plural noun

### Structure:
```
There irregular verbs + noun + (location/time)
```

### Affirmative:
**Singular:**
- **There was** a book on the table.
- **There was** a problem yesterday.
- **There was** a cat in the garden.

**Plural:**
- **There were** books on the table.
- **There were** many people at the party.
- **There were** three cats in the garden.

### Negative:
**Singular:**
- **There wasn't** a book on the table.
- **There wasn't** any problem.

**Plural:**
- **There weren't** any books on the table.
- **There weren't** many people.

### Questions:
**Singular:**
- **Was there** a book on the table?
- **Was there** a problem?

**Plural:**
- **Were there** any books?
- **Were there** many people?

### Short Answers:
| Question | Positive | Negative |
|----------|----------|----------|
| Was there a book? | Yes, there was. | No, there wasn't. |
| Were there books? | Yes, there were. | No, there weren't. |

### Examples:
- **There was** a great movie on TV last night.
- **There were** many students in the class.
- **There wasn't** any food in the fridge.
- **There weren't** many people at the meeting.
- **Was there** a test yesterday? - Yes, there was.
- **Were there** any questions? - No, there weren't.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 31-33: Audio examples
    cells.append(
        create_cell(
            "code",
            """# There irregular verbs examples
audio.play_audio("There was a problem with my computer.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("There were many people at the concert.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Were there any messages for me?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 34: Section 10 - Common Mistakes
    cells.append(
        create_cell(
            "markdown",
            """## 10. Common Mistakes to Avoid ⚠️

### Mistake 1: Using wrong form (was vs were)
❌ I **were** at home. → ✅ I **was** at home.
❌ They **was** happy. → ✅ They **were** happy.
❌ You **was** late. → ✅ You **were** late. (ALWAYS "were" with "you")

**Remember:**
- WAS = I, he, she, it
- WERE = you, we, they

### Mistake 2: Using present instead of past
❌ Yesterday I **am** tired. → ✅ Yesterday I **was** tired.
❌ Last week she **is** here. → ✅ Last week she **was** here.

**Remember:** Use past forms when talking about the past!

### Mistake 3: Wrong negative form
❌ I **wasn't not** there. → ✅ I **wasn't** there.
❌ He **not was** happy. → ✅ He **wasn't** happy.

**Remember:** Use "wasn't" or "weren't" (not "not irregular verbs")

### Mistake 4: Wrong question form
❌ **Was** they at home? → ✅ **Were** they at home?
❌ You **was** at the party? → ✅ **Were** you at the party?

**Remember:** Invert subject and verb for questions!

### Mistake 5: Using "to be" after irregular verbs
❌ I was **to be** tired. → ✅ I was tired.
❌ She was **to be** happy. → ✅ She was happy.

### Mistake 6: Confusing there irregular verbs with they were
❌ **They was** a problem. → ✅ **There was** a problem.
❌ **There were** very happy. → ✅ **They were** very happy.

**Remember:**
- **THERE WAS/WERE** = something existed
- **THEY WERE** = plural subject

### Mistake 7: Wrong short answer
❌ Were you late? - Yes, I were. → ✅ Yes, I was.
❌ Was she there? - No, she wasn't was. → ✅ No, she wasn't.

### Mistake 8: Forgetting time expressions
❌ I was tired. (When? Present or past unclear?)
✅ I was tired yesterday. (Clear it's the past)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 35: Section 11 - Practice Conversations
    cells.append(
        create_cell(
            "markdown",
            """## 11. Practice Conversations 🗣️

### Conversation 1: Talking About Yesterday</cell>""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation about yesterday
audio.create_conversation_audio([
    ("Anna", "Hi Tom! Where were you yesterday?"),
    ("Tom", "I was at home. I wasn't feeling well."),
    ("Anna", "Oh no! Were you sick?"),
    ("Tom", "Yes, I was. I had a terrible headache."),
    ("Anna", "That's too bad. Are you better now?"),
    ("Tom", "Yes, I'm fine now. Thanks!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conversation 2
    cells.append(
        create_cell(
            "markdown",
            """### Conversation 2: Asking About the Past</cell>""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation asking about the past
audio.create_conversation_audio([
    ("Sarah", "How was your weekend?"),
    ("Mike", "It was great! I was at the beach with my family."),
    ("Sarah", "Nice! Was the weather good?"),
    ("Mike", "Yes, it was sunny and warm. Where were you?"),
    ("Sarah", "I was at my grandmother's house."),
    ("Mike", "Was it fun?"),
    ("Sarah", "Yes, it was wonderful!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conversation 3
    cells.append(
        create_cell(
            "markdown",
            """### Conversation 3: There Irregular Verbs</cell>""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation using there irregular verbs
audio.create_conversation_audio([
    ("Student", "Was there homework yesterday?"),
    ("Teacher", "Yes, there was. There were three exercises."),
    ("Student", "Were there any difficult questions?"),
    ("Teacher", "No, there weren't. They were all easy."),
    ("Student", "Great! Thank you!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conversation 4
    cells.append(
        create_cell(
            "markdown", """### Conversation 4: Describing the Past</cell>""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation describing the past
audio.create_conversation_audio([
    ("Lisa", "How was the party last night?"),
    ("John", "It was amazing! There were about 50 people."),
    ("Lisa", "Wow! Was the music good?"),
    ("John", "Yes, it was excellent. Everyone was dancing."),
    ("Lisa", "I'm sorry I wasn't there. I was too tired."),
    ("John", "That's okay. There's another party next week!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Separator
    cells.append(create_cell("markdown", """---""", f"cell-{cell_counter}"))
    cell_counter += 1

    # Pronunciation guide
    cells.append(
        create_cell(
            "code",
            """# Display pronunciation guide
create_pronunciation_guide()""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Final section
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

Now that you understand Past Simple irregular verbs, it's time to practice!

### Continue to:
1. **02_controlled_practice.ipynb** - 70+ exercises on irregular verbs
2. **03_meaningful_practice.ipynb** - Write about your past experiences
3. **04_communicative_practice.ipynb** - Real conversations about the past

---

## 📌 Key Takeaways

✅ **WAS** = I, he, she, it (singular)

✅ **WERE** = you, we, they (plural + you)

✅ WAS/WERE describe states, feelings, locations in the past

✅ Negative: **wasn't / weren't**

✅ Questions: **Irregular Verbs + subject...?**

✅ Short answers: *Yes, I was* / *No, I wasn't*

✅ Time expressions: yesterday, last week, ago

✅ **There was** (singular) / **There were** (plural)

✅ Use past forms when talking about the past!

---

## 📊 Summary Table

| | Affirmative | Negative | Question | Short Answer |
|---|-------------|----------|----------|--------------|
| **I** | I was | I wasn't | Was I...? | Yes, I was / No, I wasn't |
| **You** | You were | You weren't | Were you...? | Yes, you were / No, you weren't |
| **He/She/It** | He was | He wasn't | Was he...? | Yes, he was / No, he wasn't |
| **We** | We were | We weren't | Were we...? | Yes, we were / No, we weren't |
| **They** | They were | They weren't | Were they...? | Yes, they were / No, they weren't |

---

**Great job completing the introduction!** 🌟

Ready for practice? Open **02_controlled_practice.ipynb**""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    return notebook


if __name__ == "__main__":
    # Build the notebook
    notebook = build_phase1_notebook()

    # Save to file
    output_path = "01_introduction.ipynb"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    # Get file size
    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"Module 17 Phase 1 notebook created successfully!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_kb:.2f} KB")
    print(f"Cells: {len(notebook['cells'])}")
