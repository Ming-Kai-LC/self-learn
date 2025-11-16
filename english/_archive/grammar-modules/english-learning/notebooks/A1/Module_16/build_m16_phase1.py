"""
Builder script for Module 16 Phase 1: Past Simple - Regular Verbs - Introduction
Target: 18-22 KB, 45-50 cells, 12 comprehensive sections
"""

import json
import os


def create_cell(cell_type, content, cell_id):
    """Create a notebook cell"""
    if cell_type == "markdown":
        return {"cell_type": "markdown", "id": cell_id, "metadata": {}, "source": content}
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

    # Cell 0: Title
    cells.append(
        create_cell(
            "markdown",
            """# Module 16: Past Simple - Regular Verbs - Introduction

## 📚 Phase 1: Introduction (15% of learning time)

**Welcome to Module 16!** 🎉

Now you'll learn how to talk about **past actions** using **regular verbs** in the Past Simple tense. This is essential for telling stories and describing what happened!

### Learning Objectives
By the end of this module, you will be able to:
- ✅ Form Past Simple with regular verbs (add -ed)
- ✅ Apply spelling rules for -ed endings
- ✅ Pronounce -ed correctly (/t/, /d/, /ɪd/)
- ✅ Make affirmative sentences in the past
- ✅ Make negative sentences (didn't + base verb)
- ✅ Ask questions in the past (Did you...?)
- ✅ Give short answers (Yes, I did / No, I didn't)
- ✅ Use time expressions with past actions
- ✅ Know common regular verbs
- ✅ Avoid common mistakes
- ✅ Have conversations about past activities

### Time Requirement
⏱️ Estimated time: 6-8 hours (spread across multiple sessions)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Setup
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

print("✅ Setup complete! Let's learn about Past Simple regular verbs!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 1
    cells.append(
        create_cell(
            "markdown",
            """## 1. Introduction to Past Simple Regular Verbs ⏰

In Module 15, you learned **WAS/WERE** for past states. Now you'll learn how to talk about **past ACTIONS**.

### Regular Verbs:
Regular verbs are verbs that follow a pattern. To make the past simple, we **add -ed** to the base verb.

### Formula:
```
Base verb + -ed = Past Simple
```

### Examples:
| Base Verb | Past Simple | Meaning |
|-----------|-------------|---------|
| play | play**ed** | played |
| walk | walk**ed** | walked |
| watch | watch**ed** | watched |
| listen | listen**ed** | listened |
| work | work**ed** | worked |
| help | help**ed** | helped |
| cook | cook**ed** | cooked |
| clean | clean**ed** | cleaned |

### Key Point:
🎯 The past form is the **SAME for all subjects** (I, you, he, she, it, we, they)!

- I play**ed** ✅
- He play**ed** ✅
- They play**ed** ✅

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Audio examples
    cells.append(
        create_cell(
            "code",
            """# Past Simple examples
audio.play_audio("I played football yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She watched a movie last night.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We walked in the park.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 2: Spelling Rules
    cells.append(
        create_cell(
            "markdown",
            """## 2. Spelling Rules for -ed Endings 📝

Most verbs just add -ed, but there are special spelling rules:

### Rule 1: Most Regular Verbs → Add -ed
Just add -ed to the base verb:

| Base | Past | Example |
|------|------|---------|
| walk | walked | I walked to school. |
| talk | talked | She talked to me. |
| play | played | We played games. |
| watch | watched | He watched TV. |
| work | worked | They worked hard. |

### Rule 2: Verb ends in -e → Add -d only
If the verb already ends in -e, just add -d:

| Base | Past | Example |
|------|------|---------|
| like | liked | I liked the movie. |
| love | loved | She loved the book. |
| live | lived | We lived in Tokyo. |
| dance | danced | They danced all night. |
| use | used | He used my pen. |
| smile | smiled | She smiled at me. |

### Rule 3: Verb ends in consonant + y → Change y to i, add -ed
| Base | Past | Example |
|------|------|---------|
| study | stud**ied** | I studied English. |
| try | tr**ied** | She tried hard. |
| cry | cr**ied** | The baby cried. |
| carry | carr**ied** | He carried the bags. |
| worry | worr**ied** | We worried about you. |

**But:** If vowel + y → just add -ed
- play → played (NOT "plaied")
- enjoy → enjoyed (NOT "enjoied")

### Rule 4: One-syllable verb ending in consonant-vowel-consonant → Double the last consonant + -ed

| Base | Past | Example |
|------|------|---------|
| stop | sto**pp**ed | I stopped the car. |
| plan | pla**nn**ed | We planned a trip. |
| shop | sho**pp**ed | She shopped all day. |
| drop | dro**pp**ed | He dropped the ball. |

**Exceptions:** Don't double w, x, y
- show → showed (NOT "showwed")
- fix → fixed (NOT "fixxed")

### Rule 5: Two-syllable verbs ending in consonant-vowel-consonant:
- If stress is on FIRST syllable → don't double
  - visit → visited (NOT "visitted")
  - open → opened (NOT "openned")

- If stress is on SECOND syllable → double it
  - prefer → preferred
  - admit → admitted

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Spelling practice audio
    cells.append(
        create_cell(
            "code",
            """# Spelling examples
audio.play_audio("I liked the movie.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code", """audio.play_audio("She studied hard.", accent="us")""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We stopped at the store.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 3: Pronunciation
    cells.append(
        create_cell(
            "markdown",
            """## 3. Pronunciation of -ed Endings 🔊

The -ed ending has **THREE different pronunciations**!

### /t/ Sound (voiceless)
After voiceless sounds: /p/, /k/, /f/, /s/, /ʃ/, /tʃ/

| Verb | Pronunciation | Example |
|------|---------------|---------|
| walked | walk/t/ | I walked home. |
| talked | talk/t/ | She talked loudly. |
| helped | help/t/ | We helped them. |
| watched | watch/t/ | He watched TV. |
| stopped | stop/t/ | They stopped here. |
| liked | like/t/ | I liked it. |
| finished | finish/t/ | She finished work. |

### /d/ Sound (voiced)
After voiced sounds: /b/, /g/, /v/, /z/, /m/, /n/, /l/, /r/ and vowels

| Verb | Pronunciation | Example |
|------|---------------|---------|
| played | play/d/ | I played football. |
| lived | live/d/ | She lived here. |
| cleaned | clean/d/ | We cleaned the house. |
| listened | listen/d/ | He listened carefully. |
| arrived | arrive/d/ | They arrived late. |
| enjoyed | enjoy/d/ | I enjoyed the party. |

### /ɪd/ Sound (extra syllable)
After /t/ or /d/ sounds - creates an extra syllable!

| Verb | Pronunciation | Example |
|------|---------------|---------|
| wanted | want/ɪd/ (2 syllables) | I wanted ice cream. |
| needed | need/ɪd/ (2 syllables) | She needed help. |
| started | start/ɪd/ (2 syllables) | We started early. |
| ended | end/ɪd/ (2 syllables) | It ended at 5. |
| decided | decid/ɪd/ (3 syllables) | They decided to go. |
| visited | visit/ɪd/ (3 syllables) | I visited my friend. |

### Quick Rule:
- T or D sound at the end? → /ɪd/
- Voiceless sound? → /t/
- Voiced sound or vowel? → /d/

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Pronunciation practice
    cells.append(
        create_cell(
            "code",
            """# Pronunciation practice - /t/ sound
audio.play_audio("I walked to school.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Pronunciation practice - /d/ sound
audio.play_audio("She played the piano.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Pronunciation practice - /ɪd/ sound
audio.play_audio("We wanted to go home.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 4: Affirmative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## 4. Affirmative Sentences (Positive Statements) ✅

### Structure:
```
Subject + Past Simple verb + (object/complement)
```

### Remember: The past form is the SAME for all subjects!

### Examples:

**I:**
- I **played** tennis yesterday.
- I **watched** a movie last night.
- I **studied** English.

**You:**
- You **worked** hard.
- You **helped** me a lot.
- You **lived** in London.

**He/She/It:**
- He **walked** to school.
- She **cooked** dinner.
- It **started** at 9 o'clock.

**We:**
- We **enjoyed** the party.
- We **visited** our grandparents.
- We **cleaned** the house.

**They:**
- They **arrived** late.
- They **talked** for hours.
- They **danced** all night.

### More Examples:

- I **liked** the book.
- She **finished** her homework.
- We **planned** a trip.
- They **moved** to Tokyo.
- He **opened** the door.
- I **called** my friend.
- She **answered** the phone.
- We **waited** for the bus.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Affirmative examples
    cells.append(
        create_cell(
            "code",
            """# Affirmative sentences
audio.play_audio("I played football yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She cooked dinner last night.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We visited the museum.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 5: Negative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## 5. Negative Sentences 🚫

### Structure:
```
Subject + DIDN'T + base verb + (object/complement)
```

### Important Rules:
1. Use **DIDN'T** (did not) for all subjects
2. Use the **BASE VERB** (not the past form) after didn't!
3. DIDN'T already shows it's past, so no -ed!

### Examples:

**Correct Form:**
- I **didn't play** tennis. ✅ (NOT "didn't played")
- She **didn't watch** TV. ✅
- We **didn't study** yesterday. ✅
- They **didn't work** last week. ✅

**Common Mistakes:**
- I didn't played ❌ → I didn't play ✅
- She didn't worked ❌ → She didn't work ✅

### More Examples:

**All Subjects:**
- I **didn't like** the movie.
- You **didn't help** me.
- He **didn't call** me.
- She **didn't finish** the work.
- It **didn't start** on time.
- We **didn't enjoy** the party.
- They **didn't arrive** early.

### Full Form vs Contraction:
| Full Form | Contraction | Usage |
|-----------|-------------|-------|
| did not | didn't | Most common in speaking |

**Examples:**
- I **did not** study. (formal)
- I **didn't** study. (common)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Negative examples
    cells.append(
        create_cell(
            "code",
            """# Negative sentences
audio.play_audio("I didn't play football yesterday.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She didn't watch the movie.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They didn't finish their homework.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 6: Questions
    cells.append(
        create_cell(
            "markdown",
            """## 6. Questions in Past Simple ❓

### Structure:
```
DID + subject + base verb + ...?
```

### Important Rules:
1. Use **DID** for all subjects (same as didn't)
2. Use the **BASE VERB** after did
3. DID shows it's past, so no -ed!

### Yes/No Questions:

- **Did** you **play** football? ✅ (NOT "Did you played?")
- **Did** she **watch** TV? ✅
- **Did** they **study** English? ✅
- **Did** he **work** yesterday? ✅

### Wh- Questions:
Combine question words with DID:

| Question Word | Example |
|---------------|---------|
| **What** | What **did** you **do** yesterday? |
| **Where** | Where **did** she **go**? |
| **When** | When **did** they **arrive**? |
| **Why** | Why **did** he **call** you? |
| **Who** | Who **did** you **meet**? |
| **How** | How **did** you **learn** that? |
| **What time** | What time **did** it **start**? |

### More Examples:

- Did you like the movie?
- Did she finish her homework?
- Did they enjoy the party?
- Where did you live?
- When did you start learning English?
- Why did she call you?
- What did they watch?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Question examples
    cells.append(
        create_cell(
            "code",
            """# Questions
audio.play_audio("Did you play football yesterday?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Where did you go last weekend?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("What did you do yesterday?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 7: Short Answers
    cells.append(
        create_cell(
            "markdown",
            """## 7. Short Answers 👍👎

### Structure:
```
Yes, + subject + did.
No, + subject + didn't.
```

### Examples:

| Question | Positive Answer | Negative Answer |
|----------|----------------|------------------|
| Did you play tennis? | Yes, I did. | No, I didn't. |
| Did she call you? | Yes, she did. | No, she didn't. |
| Did they finish? | Yes, they did. | No, they didn't. |
| Did he work yesterday? | Yes, he did. | No, he didn't. |
| Did it rain? | Yes, it did. | No, it didn't. |

### Important Rules:
1. **Don't repeat the main verb:**
   - Did you play? → Yes, I did. ✅ (NOT "Yes, I did play.")

2. **Don't use contractions in positive short answers:**
   - Yes, I did. ✅ (NOT "Yes, I'd.")
   - No, I didn't. ✅ (correct to use didn't)

3. **Match the subject:**
   - Did you study? → Yes, I did. (you → I)
   - Did she work? → Yes, she did. (she → she)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Short answer conversation
    cells.append(
        create_cell(
            "code",
            """# Short answers conversation
audio.create_conversation_audio([
    ("Person A", "Did you watch the game last night?"),
    ("Person B", "Yes, I did. Did you?"),
    ("Person A", "No, I didn't. I was too tired.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 8: Time Expressions
    cells.append(
        create_cell(
            "markdown",
            """## 8. Time Expressions with Past Simple 📅

These are the same time expressions you learned with WAS/WERE:

### Common Time Expressions:

**Yesterday:**
- yesterday
- yesterday morning/afternoon/evening

**Last:**
- last night
- last week/month/year
- last Monday/Tuesday, etc.
- last summer/winter

**Ago:**
- a minute ago
- an hour ago
- two days ago
- three weeks ago
- a year ago

**Other:**
- in 2020
- in January
- on Monday
- this morning (if it's afternoon now)
- when I was young

### Examples:

- I **played** football **yesterday**.
- She **studied** English **last week**.
- We **visited** Paris **two years ago**.
- They **worked** hard **last month**.
- He **called** me **an hour ago**.
- I **watched** that movie **in 2020**.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Time expressions
    cells.append(
        create_cell(
            "code",
            """# Time expressions
audio.play_audio("I visited my grandparents last weekend.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She called me two hours ago.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 9: Common Regular Verbs List
    cells.append(
        create_cell(
            "markdown",
            """## 9. Common Regular Verbs (50+ verbs) 📚

### Daily Activities:
| Base | Past | Meaning |
|------|------|---------|
| work | worked | to do a job |
| study | studied | to learn |
| cook | cooked | to prepare food |
| clean | cleaned | to make clean |
| wash | washed | to clean with water |
| watch | watched | to look at |
| listen | listened | to hear carefully |
| play | played | to do sport/game |
| walk | walked | to go on foot |
| talk | talked | to speak |
| call | called | to phone |
| help | helped | to assist |
| start | started | to begin |
| finish | finished | to complete |
| wait | waited | to stay until |
| arrive | arrived | to reach |
| stay | stayed | to remain |
| visit | visited | to go see |
| travel | travelled/traveled | to journey |
| move | moved | to change place |

### Communication & Interaction:
| Base | Past | Meaning |
|------|------|---------|
| ask | asked | to question |
| answer | answered | to reply |
| explain | explained | to make clear |
| discuss | discussed | to talk about |
| share | shared | to give to others |
| agree | agreed | to say yes |
| decide | decided | to choose |
| plan | planned | to arrange |
| invite | invited | to ask to come |

### Feelings & Opinions:
| Base | Past | Meaning |
|------|------|---------|
| like | liked | to enjoy |
| love | loved | to love |
| hate | hated | to dislike strongly |
| enjoy | enjoyed | to take pleasure |
| want | wanted | to desire |
| need | needed | to require |
| prefer | preferred | to like better |

### Actions & Changes:
| Base | Past | Meaning |
|------|------|---------|
| open | opened | to make open |
| close | closed | to shut |
| stop | stopped | to cease |
| drop | dropped | to let fall |
| pick | picked | to choose/take |
| carry | carried | to transport |
| push | pushed | to press |
| pull | pulled | to draw toward |
| change | changed | to make different |
| use | used | to employ |
| try | tried | to attempt |
| show | showed | to display |
| paint | painted | to color |
| fix | fixed | to repair |

### Other Common Verbs:
| Base | Past | Meaning |
|------|------|---------|
| rain | rained | precipitation |
| snow | snowed | white precipitation |
| happen | happened | to occur |
| seem | seemed | to appear |
| look | looked | to appear/see |
| belong | belonged | to be owned by |

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 10: Common Mistakes
    cells.append(
        create_cell(
            "markdown",
            """## 10. Common Mistakes to Avoid ⚠️

### Mistake 1: Using past form after DID/DIDN'T
❌ I didn't **played**. → ✅ I didn't **play**.
❌ Did you **watched**? → ✅ Did you **watch**?

**Remember:** DIDN'T and DID are already past, so use base verb!

### Mistake 2: Forgetting -ed in affirmative sentences
❌ I **play** football yesterday. → ✅ I **played** football yesterday.
❌ She **work** last week. → ✅ She **worked** last week.

**Remember:** Add -ed in affirmative past sentences!

### Mistake 3: Wrong spelling of -ed
❌ I **studyed** English. → ✅ I **studied** English.
❌ She **stoped** the car. → ✅ She **stopped** the car.
❌ We **planed** a trip. → ✅ We **planned** a trip.

**Remember:** Follow the spelling rules!

### Mistake 4: Using TO after DID
❌ Did you **to play**? → ✅ Did you **play**?
❌ I didn't **to watch** TV. → ✅ I didn't **watch** TV.

**Remember:** No "to" after did/didn't!

### Mistake 5: Wrong question word order
❌ What you did yesterday? → ✅ What **did you do** yesterday?
❌ Where she went? → ✅ Where **did she go**?

**Remember:** DID + subject + base verb

### Mistake 6: Confusing regular and irregular verbs
Some verbs are irregular (you'll learn these in Module 17):
- go → went (NOT "goed")
- eat → ate (NOT "eated")
- see → saw (NOT "seed")

### Mistake 7: Adding -s for he/she/it
❌ He play**s** yesterday. → ✅ He play**ed** yesterday.
❌ She work**s** last week. → ✅ She work**ed** last week.

**Remember:** In past simple, NO -s for he/she/it!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Section 11: Practice Dialogues
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
            """# Conversation 1
audio.create_conversation_audio([
    ("Anna", "What did you do yesterday?"),
    ("Tom", "I played football with my friends. What about you?"),
    ("Anna", "I studied for my test and then I watched a movie."),
    ("Tom", "Did you enjoy the movie?"),
    ("Anna", "Yes, I did! It was great."),
    ("Tom", "Did you pass your test?"),
    ("Anna", "I don't know yet. We didn't get the results.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conversation 2
    cells.append(
        create_cell(
            "markdown", """### Conversation 2: Weekend Activities</cell>""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 2
audio.create_conversation_audio([
    ("Lisa", "Did you do anything special last weekend?"),
    ("Mike", "Yes! I visited my grandparents. We cooked dinner together."),
    ("Lisa", "That sounds nice! What did you cook?"),
    ("Mike", "We prepared Italian food. We cooked pasta and pizza."),
    ("Lisa", "Yum! Did your grandparents enjoy it?"),
    ("Mike", "Yes, they loved it! What did you do?"),
    ("Lisa", "I stayed home. I cleaned my apartment and listened to music.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conversation 3
    cells.append(
        create_cell(
            "markdown", """### Conversation 3: Last Vacation</cell>""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 3
audio.create_conversation_audio([
    ("Sarah", "Where did you travel on your last vacation?"),
    ("John", "We visited Thailand. We stayed in Bangkok for a week."),
    ("Sarah", "Wow! Did you enjoy it?"),
    ("John", "Yes, we loved it! We tried lots of Thai food and visited temples."),
    ("Sarah", "That sounds amazing! Did you shop there?"),
    ("John", "Yes, we shopped at the markets. Everything was very cheap!"),
    ("Sarah", "Lucky you! I didn't travel last year. I worked all summer.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Pronunciation guide
    cells.append(create_cell("markdown", """---""", f"cell-{cell_counter}"))
    cell_counter += 1

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

Now that you understand Past Simple with regular verbs, it's time to practice!

### Continue to:
1. **02_controlled_practice.ipynb** - 70+ exercises on regular past verbs
2. **03_meaningful_practice.ipynb** - Write about your own past activities
3. **04_communicative_practice.ipynb** - Real conversations about the past

---

## 📌 Key Takeaways

✅ Regular verbs: **base verb + -ed**

✅ Same form for all subjects: I/you/he/she/it/we/they + verb-ed

✅ **Spelling rules:** most add -ed, some change (study→studied, stop→stopped)

✅ **Pronunciation:** /t/, /d/, or /ɪd/ depending on the last sound

✅ **Affirmative:** Subject + verb-ed

✅ **Negative:** Subject + didn't + base verb

✅ **Questions:** Did + subject + base verb?

✅ **Short answers:** Yes, I did / No, I didn't

✅ Use base verb (NOT past form) after did/didn't!

---

## 📊 Summary Table

| | Affirmative | Negative | Question | Short Answer |
|---|-------------|----------|----------|--------------|
| **Form** | verb-ed | didn't + base | Did + base? | Yes/No + did/didn't |
| **Example** | I played | I didn't play | Did I play? | Yes, I did |
| **All subjects** | Same form | Same form | Same form | Changes by subject |

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
    notebook = build_phase1_notebook()
    output_path = "01_introduction.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"Module 16 Phase 1 notebook created successfully!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_kb:.2f} KB")
    print(f"Cells: {len(notebook['cells'])}")
