"""
Builder script for Module 14 Phase 1: Like/Love/Hate + -ing - Introduction
Target: 18-22 KB, 40-50 cells, 12 comprehensive sections
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


def build_phase1_notebook():
    """Build the complete Phase 1 notebook"""
    cells = []
    cell_counter = 0

    # Cell 0: Title and Introduction
    cells.append(
        create_cell(
            "markdown",
            """# Module 14: Like, Love, Hate + -ing - Introduction

## 📚 Phase 1: Introduction (15% of learning time)

**Welcome to Module 14!** 🎉

In this module, you'll learn how to express your **preferences and feelings** about activities using LIKE, LOVE, and HATE with the **-ing form** (gerunds). This is essential for talking about hobbies, interests, and daily activities!

### Learning Objectives
By the end of this module, you will be able to:
- [OK] Use LIKE + -ing to express preferences
- [OK] Use LOVE + -ing to express strong positive feelings
- [OK] Use HATE + -ing to express strong negative feelings
- [OK] Use other preference verbs (enjoy, prefer, don't mind)
- [OK] Form the -ing verb correctly (gerund rules)
- [OK] Make negative sentences (don't like, don't love)
- [OK] Ask questions about preferences
- [OK] Use common collocations naturally
- [OK] Talk about hobbies and free time
- [OK] Understand like -ing vs like to
- [OK] Avoid common mistakes
- [OK] Have conversations about interests

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

print("[OK] Setup complete! Let's learn about expressing preferences with -ing!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 2: Section 1 - Introduction to Expressing Preferences
    cells.append(
        create_cell(
            "markdown",
            """## 1. Introduction to Expressing Preferences 💬

When we talk about activities we enjoy or dislike, we use **preference verbs** + **-ing form**:

### Main Preference Verbs:
| Verb | Meaning | Intensity |
|------|---------|-----------|
| **LOVE** | Very strong positive feeling | +++ |
| **LIKE** | Positive feeling | ++ |
| **DON'T MIND** | Neutral/Okay with it | +/- |
| **DON'T LIKE** | Negative feeling | -- |
| **HATE** | Very strong negative feeling | --- |

### Basic Structure:
```
Subject + preference verb + -ing + (object/complement)
```

### Examples:
- I **like reading** books.
- She **loves dancing**.
- They **hate waiting** in line.
- We **enjoy traveling**.
- He **doesn't mind cooking**.

### Why Use -ing?
When talking about activities in general (not specific instances), we use the **-ing form** (also called a **gerund**). The gerund makes a verb work like a noun.

**Compare:**
- I like **books**. (noun - thing)
- I like **reading**. (gerund - activity)

### 🎯 Key Point:
The -ing form lets you talk about activities as if they were things!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 3: Section 2 - LIKE + -ing
    cells.append(
        create_cell(
            "markdown",
            """## 2. LIKE + -ing (Expressing Positive Preferences) 👍

**LIKE** shows you have a positive feeling about an activity.

### Structure:
```
Subject + LIKE/LIKES + verb-ing + (complement)
```

### Forms:
- **I/You/We/They** + **like** + -ing
- **He/She/It** + **likes** + -ing

### Usage Examples:

**1. Talking about hobbies:**
- I **like reading** science fiction.
- She **likes watching** movies.
- They **like playing** football.
- We **like listening** to music.

**2. Expressing enjoyment:**
- I **like swimming** in the ocean.
- He **likes cooking** Italian food.
- They **like traveling** to new places.
- She **likes learning** languages.

**3. Daily activities:**
- I **like walking** to work.
- She **likes drinking** coffee in the morning.
- We **like eating** out on weekends.
- He **likes sleeping** late on Sundays.

**4. With objects/complements:**
- I **like playing** video games with friends.
- She **likes reading** before bed.
- They **like going** to the beach in summer.
- We **like watching** documentaries.

### Common Collocations with LIKE:
- like **reading** (books, magazines, novels)
- like **watching** (movies, TV, videos)
- like **playing** (sports, games, instruments)
- like **listening** to (music, podcasts, radio)
- like **going** to (concerts, parties, restaurants)
- like **spending** time (with friends, family)
- like **doing** (exercise, homework, yoga)
- like **eating** (out, healthy food, sweets)

### Time Reference:
"Like + -ing" talks about activities **in general**, not a specific moment:
- [OK] I like swimming. (general preference)
- ❌ I like swimming now. (use present continuous instead)

### 🎯 Key Point:
LIKE + -ing expresses a general, consistent preference for an activity.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 4-7: Audio examples for LIKE
    cells.append(
        create_cell(
            "code",
            """# LIKE + -ing - Examples with audio
audio.play_audio("I like reading books in my free time.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She likes watching movies on weekends.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They like playing football after school.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We like going to the beach in summer.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 8: Section 3 - LOVE + -ing
    cells.append(
        create_cell(
            "markdown",
            """## 3. LOVE + -ing (Expressing Strong Positive Feelings) ❤️

**LOVE** shows a very strong positive feeling about an activity - stronger than "like".

### Structure:
```
Subject + LOVE/LOVES + verb-ing + (complement)
```

### Forms:
- **I/You/We/They** + **love** + -ing
- **He/She/It** + **loves** + -ing

### Usage Examples:

**1. Strong enthusiasm:**
- I **love dancing** at parties!
- She **loves singing** in the shower.
- They **love traveling** around the world.
- We **love eating** at new restaurants.

**2. Passionate hobbies:**
- I **love painting** landscapes.
- He **loves playing** the guitar.
- They **love surfing** in big waves.
- She **loves writing** poetry.

**3. Deep enjoyment:**
- I **love spending** time with my family.
- She **loves reading** mystery novels.
- They **love hiking** in the mountains.
- We **love watching** the sunset.

**4. Favorite activities:**
- I **love cooking** for friends.
- He **loves working** on his car.
- They **love going** to concerts.
- She **loves learning** new things.

### LOVE vs LIKE:
| LIKE | LOVE |
|------|------|
| I like chocolate. (good) | I love chocolate! (excellent!) |
| I like running. (positive) | I love running! (very positive) |
| She likes dancing. (enjoys it) | She loves dancing! (adores it) |

### Common Collocations with LOVE:
- love **dancing** (at parties, salsa, ballet)
- love **traveling** (abroad, by train, solo)
- love **cooking** (for others, Italian food)
- love **reading** (novels, at night, fiction)
- love **spending** time (with family, outdoors)
- love **playing** (music, with kids, sports)
- love **learning** (languages, new skills)
- love **being** (creative, outdoors, active)

### Intensity Comparison:
```
HATE < DON'T LIKE < DON'T MIND < LIKE < LOVE
```

### 🎯 Key Point:
LOVE + -ing expresses passion and strong enthusiasm for an activity!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 9-12: Audio examples for LOVE
    cells.append(
        create_cell(
            "code",
            """# LOVE + -ing - Examples with audio
audio.play_audio("I love dancing at parties!", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She loves traveling to new countries.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They love cooking Italian food together.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We love spending time with our family.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 13: Section 4 - HATE + -ing
    cells.append(
        create_cell(
            "markdown",
            """## 4. HATE + -ing (Expressing Strong Negative Feelings) 😠

**HATE** shows a very strong negative feeling about an activity. It's the opposite of "love".

### Structure:
```
Subject + HATE/HATES + verb-ing + (complement)
```

### Forms:
- **I/You/We/They** + **hate** + -ing
- **He/She/It** + **hates** + -ing

### Usage Examples:

**1. Strong dislike:**
- I **hate waiting** in line.
- She **hates waking up** early.
- They **hate doing** homework.
- We **hate being** late.

**2. Unpleasant activities:**
- I **hate cleaning** the bathroom.
- He **hates ironing** clothes.
- They **hate washing** dishes.
- She **hates going** to the dentist.

**3. Annoying situations:**
- I **hate losing** my keys.
- She **hates missing** the bus.
- They **hate forgetting** important things.
- We **hate arguing** with people.

**4. Common dislikes:**
- I **hate getting up** early on Mondays.
- He **hates working** late.
- They **hate sitting** in traffic.
- She **hates repeating** herself.

### Important Notes:

**1. HATE is very strong:**
- Use "don't like" for less intense feelings
- HATE can sound dramatic or emotional

**2. Cultural note:**
- Some cultures avoid saying "hate" too often
- "Don't like" is often softer and more polite

**3. Common in spoken English:**
- "I hate doing..." (very common)
- "I hate it when..." (describing situations)

### Common Collocations with HATE:
- hate **waiting** (in line, for people)
- hate **cleaning** (the house, my room)
- hate **waking up** (early, on Mondays)
- hate **doing** (homework, chores, paperwork)
- hate **being** (late, wrong, interrupted)
- hate **losing** (things, games, time)
- hate **getting** (up early, stuck in traffic)
- hate **sitting** (still, in traffic)

### HATE vs DON'T LIKE:
| DON'T LIKE | HATE |
|------------|------|
| I don't like running. (mild) | I hate running! (strong) |
| She doesn't like coffee. (preference) | She hates coffee! (intense) |
| They don't like waiting. (dislike) | They hate waiting! (strong dislike) |

### Alternatives to HATE (softer):
- **can't stand** + -ing (strong but less than hate)
- **don't like** + -ing (mild)
- **dislike** + -ing (formal)
- **not keen on** + -ing (British, mild)

### 🎯 Key Point:
HATE + -ing expresses a strong, intense dislike. Use carefully and consider softer alternatives when appropriate!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 14-17: Audio examples for HATE
    cells.append(
        create_cell(
            "code",
            """# HATE + -ing - Examples with audio
audio.play_audio("I hate waiting in long lines.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She hates waking up early on Mondays.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They hate cleaning the house.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("We hate being late for meetings.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 18: Section 5 - Other Preference Verbs
    cells.append(
        create_cell(
            "markdown",
            """## 5. Other Preference Verbs (Enjoy, Prefer, Don't Mind) 🎯

Besides LIKE, LOVE, and HATE, there are other important verbs for expressing preferences.

### 1. ENJOY + -ing (Similar to LIKE but more active)

**Structure:** Subject + ENJOY/ENJOYS + -ing

**Meaning:** To get pleasure from doing something (active participation)

**Examples:**
- I **enjoy reading** novels.
- She **enjoys playing** tennis.
- They **enjoy spending** time outdoors.
- We **enjoy cooking** together.

**Usage notes:**
- ENJOY = actively getting pleasure from something
- More formal than LIKE
- Often used for activities you actively participate in

**Common collocations:**
- enjoy **reading** / **watching** / **playing**
- enjoy **spending** time
- enjoy **working** / **learning** / **teaching**

---

### 2. PREFER + -ing (Showing one choice over another)

**Structure:** Subject + PREFER/PREFERS + -ing (to + -ing)

**Meaning:** To like something better than another thing

**Examples:**
- I **prefer reading** books to watching TV.
- She **prefers walking** to driving.
- They **prefer staying** home to going out.
- We **prefer cooking** at home.

**Two patterns:**
```
Pattern 1: prefer + -ing (alone)
- I prefer swimming.

Pattern 2: prefer + -ing + TO + -ing (comparison)
- I prefer swimming TO running.
```

**Usage notes:**
- Use "prefer...to..." to compare two things
- "To" here is a preposition, not infinitive
- Can also use: prefer + noun + to + noun

**Common collocations:**
- prefer **staying** home to going out
- prefer **reading** to watching
- prefer **walking** to driving
- prefer **working** alone to working in teams

---

### 3. DON'T MIND + -ing (Neutral/Willing to do)

**Structure:** Subject + DON'T/DOESN'T MIND + -ing

**Meaning:** Not bothered by something; willing to do it (neutral feeling)

**Examples:**
- I **don't mind waiting**.
- She **doesn't mind helping** you.
- They **don't mind working** late.
- We **don't mind driving**.

**Usage notes:**
- Expresses willingness without enthusiasm
- "It's okay with me"
- Between LIKE and DON'T LIKE on the scale
- Very common in polite offers/requests

**In questions (offers):**
- "Would you mind helping me?" (polite request)
- "Do you mind waiting?" (asking permission)

**Negative form (careful!):**
- "I don't mind" = I'm okay with it ✓
- "I mind" = I'm NOT okay with it (less common)

**Common collocations:**
- don't mind **waiting** / **helping**
- don't mind **doing** (chores, favors)
- don't mind **working** (late, weekends)
- don't mind **if** + clause

---

### Comparison Table:

| Verb | Intensity | Usage | Example |
|------|-----------|-------|---------|
| **LOVE** | Very positive +++ | Strong passion | I love swimming! |
| **ENJOY** | Positive ++ | Active pleasure | I enjoy swimming. |
| **LIKE** | Positive ++ | General preference | I like swimming. |
| **PREFER** | Comparative | One over another | I prefer swimming to running. |
| **DON'T MIND** | Neutral +/- | Willingness/OK | I don't mind swimming. |
| **DON'T LIKE** | Negative -- | Mild dislike | I don't like swimming. |
| **HATE** | Very negative --- | Strong dislike | I hate swimming. |

---

### Other Common Preference Verbs:

**4. CAN'T STAND + -ing** (strong negative, less than hate)
- I **can't stand waiting** in traffic.
- She **can't stand listening** to loud music.

**5. DISLIKE + -ing** (formal for "don't like")
- I **dislike getting up** early.
- He **dislikes working** in noisy places.

**6. ADORE + -ing** (very positive, like "love")
- I **adore spending** time with my grandchildren.
- She **adores dancing**.

---

### 🎯 Key Point:
Different verbs express different levels of preference - from strong positive (love, adore) to neutral (don't mind) to strong negative (hate, can't stand). Choose the verb that matches your feeling!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 19-23: Audio examples for other verbs
    cells.append(
        create_cell(
            "code",
            """# ENJOY - Examples with audio
audio.play_audio("I enjoy reading mystery novels.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She enjoys playing tennis every weekend.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# PREFER - Examples with audio
audio.play_audio("I prefer walking to driving.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("They prefer staying home to going out.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# DON'T MIND - Examples with audio
audio.play_audio("I don't mind waiting a few minutes.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 24: Section 6 - Forming the -ing Verb
    cells.append(
        create_cell(
            "markdown",
            """## 6. Forming the -ing Verb (Gerund Spelling Rules) ✍️

To use verbs with preference words, you need to add **-ing**. Here are the spelling rules:

### Rule 1: Most Verbs - Just Add -ing ✓

**Simply add -ing to the base verb:**

| Base Verb | + -ing | Example Sentence |
|-----------|--------|------------------|
| read | reading | I like **reading**. |
| watch | watching | She loves **watching** movies. |
| play | playing | They enjoy **playing** games. |
| work | working | He hates **working** late. |
| eat | eating | We like **eating** out. |
| sleep | sleeping | I love **sleeping** late. |
| cook | cooking | She enjoys **cooking**. |
| listen | listening | They like **listening** to music. |
| learn | learning | I love **learning** languages. |
| help | helping | He doesn't mind **helping**. |

---

### Rule 2: Verbs Ending in -e - Drop the e, Add -ing 📝

**If the verb ends in -e, drop the -e and add -ing:**

| Base Verb | Drop -e | + -ing | Example Sentence |
|-----------|---------|--------|------------------|
| make | mak | making | I enjoy **making** cookies. |
| write | writ | writing | She loves **writing** stories. |
| dance | danc | dancing | They like **dancing**. |
| take | tak | taking | I don't mind **taking** photos. |
| drive | driv | driving | He hates **driving** in traffic. |
| come | com | coming | We like **coming** here. |
| bake | bak | baking | I love **baking** bread. |
| ride | rid | riding | She enjoys **riding** horses. |
| smoke | smok | smoking | I hate **smoking**. |
| save | sav | saving | They prefer **saving** money. |

**Exception:** Verbs ending in -ee, -ye, -oe keep the -e:
- see → see**ing** (I like seeing you.)
- agree → agree**ing** (We enjoy agreeing.)
- canoe → canoe**ing** (They love canoeing.)

---

### Rule 3: One Syllable Verbs - Double the Consonant + -ing 🔄

**For one-syllable verbs ending in: consonant + vowel + consonant (CVC)**
**Double the final consonant and add -ing:**

| Base Verb | Pattern | Double + -ing | Example Sentence |
|-----------|---------|---------------|------------------|
| run | CVC | running | I love **running** in the park. |
| swim | CVC | swimming | She enjoys **swimming**. |
| sit | CVC | sitting | I hate **sitting** all day. |
| shop | CVC | shopping | They love **shopping**. |
| stop | CVC | stopping | He doesn't mind **stopping**. |
| plan | CVC | planning | I enjoy **planning** trips. |
| get | CVC | getting | She hates **getting** up early. |
| cut | CVC | cutting | I don't mind **cutting** vegetables. |
| put | CVC | putting | He likes **putting** things in order. |
| jog | CVC | jogging | We enjoy **jogging** together. |

**Don't double these endings:**
- -w: show → showing (not showwing)
- -x: fix → fixing (not fixxing)
- -y: play → playing (not playying)

---

### Rule 4: Two Syllables - Double if Stressed on Last Syllable 🎵

**For two-syllable verbs ending in CVC:**
- **Stressed on last syllable → double the consonant**
- **Stressed on first syllable → don't double**

**Double the consonant (stressed on LAST syllable):**

| Base Verb | Stress | + -ing | Example Sentence |
|-----------|--------|--------|------------------|
| begin | be-GIN | beginning | I'm beginning to like it. |
| prefer | pre-FER | preferring | She's preferring coffee. |
| occur | oc-CUR | occurring | It's occurring more often. |
| admit | ad-MIT | admitting | I enjoy admitting mistakes. |
| permit | per-MIT | permitting | They're permitting it. |

**Don't double (stressed on FIRST syllable):**

| Base Verb | Stress | + -ing | Example Sentence |
|-----------|--------|--------|------------------|
| open | O-pen | opening | I like **opening** presents. |
| listen | LIS-ten | listening | She loves **listening** to music. |
| happen | HAP-pen | happening | What's **happening**? |
| visit | VIS-it | visiting | They enjoy **visiting** friends. |
| offer | OF-fer | offering | I don't mind **offering** help. |

---

### Rule 5: Verbs Ending in -ie - Change to -y + ing 🔄

**Change -ie to -y and add -ing:**

| Base Verb | Change | + -ing | Example Sentence |
|-----------|--------|--------|------------------|
| die | dy | dying | I hate **dying** in video games. |
| lie | ly | lying | She doesn't like **lying**. |
| tie | ty | tying | I don't mind **tying** shoes. |

---

### Rule 6: Verbs Ending in -c - Add -king 🔤

**For verbs ending in -c, add -k before -ing:**

| Base Verb | + k | + -ing | Example Sentence |
|-----------|-----|--------|------------------|
| picnic | picnick | picnicking | We love **picnicking** in the park. |
| panic | panick | panicking | I hate **panicking**. |
| traffic | traffick | trafficking | (Note: rarely used in -ing form) |

---

### Quick Reference Chart:

| Rule | Base Verb | -ing Form | Example |
|------|-----------|-----------|---------|
| Add -ing | work | working | like working |
| Drop -e | write | writing | love writing |
| Double consonant (1 syllable) | run | running | enjoy running |
| Double consonant (2 syllables, stressed last) | begin | beginning | prefer beginning |
| No double (2 syllables, stressed first) | listen | listening | like listening |
| -ie → -y | lie | lying | hate lying |
| -c → -ck | picnic | picnicking | love picnicking |

---

### Practice Tips:
1. **Most verbs just add -ing** (easiest!)
2. **Look for the -e at the end** (drop it!)
3. **Count syllables for CVC verbs** (may need to double)
4. **Check where the stress is** (for 2-syllable verbs)

### 🎯 Key Point:
Knowing these spelling rules helps you write gerunds correctly. When in doubt, check a dictionary!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 25: Visual aid for spelling rules
    cells.append(
        create_cell(
            "code",
            """# Display spelling rules visual aid
display(HTML('''
<div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50;">
<h3 style="color: #2196F3;">Quick -ing Spelling Guide</h3>
<table style="width:100%; border-collapse: collapse;">
<tr style="background-color: #4CAF50; color: white;">
<th style="padding: 10px; border: 1px solid #ddd;">Rule</th>
<th style="padding: 10px; border: 1px solid #ddd;">Example</th>
<th style="padding: 10px; border: 1px solid #ddd;">Result</th>
</tr>
<tr><td style="padding: 8px; border: 1px solid #ddd;">Most verbs</td><td style="padding: 8px; border: 1px solid #ddd;">work</td><td style="padding: 8px; border: 1px solid #ddd;"><b>working</b></td></tr>
<tr style="background-color: #f2f2f2;"><td style="padding: 8px; border: 1px solid #ddd;">End in -e</td><td style="padding: 8px; border: 1px solid #ddd;">make</td><td style="padding: 8px; border: 1px solid #ddd;"><b>making</b></td></tr>
<tr><td style="padding: 8px; border: 1px solid #ddd;">1 syllable CVC</td><td style="padding: 8px; border: 1px solid #ddd;">run</td><td style="padding: 8px; border: 1px solid #ddd;"><b>running</b></td></tr>
<tr style="background-color: #f2f2f2;"><td style="padding: 8px; border: 1px solid #ddd;">End in -ie</td><td style="padding: 8px; border: 1px solid #ddd;">lie</td><td style="padding: 8px; border: 1px solid #ddd;"><b>lying</b></td></tr>
</table>
</div>
'''))""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 26: Section 7 - Negative Forms
    cells.append(
        create_cell(
            "markdown",
            """## 7. Negative Forms (Don't Like, Don't Love) ❌

To express that you DON'T have a preference for something, use negative forms.

### Structure:
```
Subject + DON'T/DOESN'T + preference verb + -ing
```

### Forms:
- **I/You/We/They** + **don't** + verb + -ing
- **He/She/It** + **doesn't** + verb + -ing

---

### 1. DON'T LIKE + -ing (Mild Negative)

**Examples:**
- I **don't like waking up** early.
- She **doesn't like waiting** in line.
- They **don't like eating** spicy food.
- He **doesn't like working** on weekends.
- We **don't like driving** in heavy traffic.
- You **don't like cleaning**, do you?

**Usage notes:**
- Most common negative form
- Polite and neutral
- Not as strong as "hate"

---

### 2. DON'T LOVE + -ing (Less Intense Positive)

**Examples:**
- I **don't love cooking**, but I don't hate it.
- She **doesn't love exercising**, but she does it.
- They **don't love studying**, but it's necessary.
- We **don't love shopping** for groceries.

**Usage notes:**
- Less common than "don't like"
- Means: it's okay, but not a favorite
- Often used to be diplomatic

---

### 3. DON'T ENJOY + -ing

**Examples:**
- I **don't enjoy doing** homework.
- She **doesn't enjoy speaking** in public.
- They **don't enjoy commuting** to work.
- He **doesn't enjoy attending** meetings.

**Usage notes:**
- More formal than "don't like"
- Professional/polite contexts

---

### 4. DON'T PREFER + -ing (Usually with comparisons)

**Examples:**
- I **don't prefer working** alone.
- She **doesn't prefer traveling** by plane.
- They **don't prefer eating** meat.

**Usage notes:**
- Often better to say "I prefer X to Y" (positive)
- Less common in negative form

---

### Negative Strength Scale:

```
Strongest negative ←                                → Mildest negative
HATE                CAN'T STAND        DON'T LIKE        DON'T LOVE/ENJOY
```

---

### Comparison: Positive vs Negative

| Positive | Negative |
|----------|----------|
| I love dancing. | I don't love dancing. |
| She likes reading. | She doesn't like reading. |
| They enjoy cooking. | They don't enjoy cooking. |
| We prefer walking. | We don't prefer walking. |

---

### Important Grammar Notes:

**1. Use DON'T/DOESN'T + base verb (no -s):**
- [OK] She **doesn't like** cooking.
- ❌ She **doesn't likes** cooking.
- ❌ She **don't like** cooking.

**2. Still use -ing after the verb:**
- [OK] I **don't like waiting**.
- ❌ I **don't like wait**.

**3. No double negatives:**
- [OK] I **don't like** it.
- ❌ I **don't like nothing**.

---

### Common Negative Expressions:

**With LIKE:**
- I **don't like** running.
- I'm **not keen on** running. (British)
- I'm **not a fan of** running. (informal)
- I'm **not into** running. (very informal)

**With ENJOY:**
- I **don't enjoy** waiting.
- I **don't really enjoy** waiting. (softer)
- I **don't particularly enjoy** waiting. (formal)

**With MIND:**
- I **don't mind** = I'm okay with it (NOT negative!)
- I **do mind** = I'm NOT okay with it (true negative, less common)

---

### Softening Negative Opinions:

Sometimes you want to be less direct:

**1. Add "really":**
- I don't **really** like it. (softer)
- I don't **really** enjoy it.

**2. Add "very much":**
- I don't like it **very much**. (polite)
- She doesn't enjoy it **very much**.

**3. Add "that much":**
- I don't like cooking **that much**.
- They don't enjoy traveling **that much**.

**4. Use "not a big fan":**
- I'm **not a big fan of** running. (informal, polite)
- She's **not a big fan of** studying.

---

### 🎯 Key Point:
Use DON'T + verb + -ing to express negative preferences. Different verbs (like, enjoy, love) express different intensities of the negative feeling!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 27-30: Audio examples for negative forms
    cells.append(
        create_cell(
            "code",
            """# Negative forms - DON'T LIKE
audio.play_audio("I don't like waking up early on Mondays.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("She doesn't like waiting in long lines.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Negative forms - DON'T ENJOY
audio.play_audio("They don't enjoy doing homework.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("He doesn't enjoy commuting to work every day.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 31: Section 8 - Questions
    cells.append(
        create_cell(
            "markdown",
            """## 8. Questions (Do you like...? What do you like...?) ❓

Questions about preferences help you learn about people's interests and hobbies.

### Type 1: Yes/No Questions ✓❌

**Structure:**
```
Do/Does + subject + preference verb + -ing?
```

**Forms:**
- **Do** + I/you/we/they + like/love/enjoy + -ing?
- **Does** + he/she/it + like/love/enjoy + -ing?

**Examples:**

**With LIKE:**
- **Do you like** reading books?
- **Does she like** watching movies?
- **Do they like** playing football?
- **Does he like** cooking?

**Possible answers:**
- Yes, I do. / Yes, she does.
- No, I don't. / No, she doesn't.
- Yes, I love it! (enthusiastic)
- Not really. (soft negative)
- Kind of. / Sort of. (neutral)

**With LOVE:**
- **Do you love** dancing?
- **Does he love** traveling?
- **Do they love** swimming?

**With ENJOY:**
- **Do you enjoy** working here?
- **Does she enjoy** teaching?
- **Do they enjoy** living in the city?

**With HATE:**
- **Do you hate** waiting?
- **Does he hate** cleaning?

---

### Type 2: Wh- Questions (Information Questions) 🔍

**Structure:**
```
What/Which/Where/When/Why/How + do/does + subject + preference verb + -ing?
```

**WHAT questions:**
- **What do you like doing** in your free time?
- **What does she love doing** on weekends?
- **What do they enjoy doing** after work?
- **What don't you like doing?**

**Answers:**
- I like reading and watching movies.
- She loves going to concerts.
- They enjoy playing sports.
- I don't like cleaning.

**WHICH questions (choice):**
- **Which do you prefer**: reading **or** watching TV?
- **Which do you enjoy more**: cooking **or** eating out?
- **Which does he like better**: swimming **or** running?

**Answers:**
- I prefer reading.
- I enjoy cooking more.
- He likes swimming better.

**WHERE questions:**
- **Where do you like going** on vacation?
- **Where does she enjoy shopping?**
- **Where do they love eating?**

**Answers:**
- I like going to the beach.
- She enjoys shopping at the mall.
- They love eating at Italian restaurants.

**WHEN questions:**
- **When do you like exercising?**
- **When does he enjoy reading?**
- **When do they prefer traveling?**

**Answers:**
- I like exercising in the morning.
- He enjoys reading before bed.
- They prefer traveling in summer.

**WHY questions:**
- **Why do you like reading?**
- **Why does she love dancing?**
- **Why don't you like cooking?**

**Answers:**
- I like reading because it's relaxing.
- She loves dancing because it's fun.
- I don't like cooking because it takes too long.

**HOW questions (manner/frequency):**
- **How often do you enjoy** going to the gym?
- **How much do you like** traveling?

**Answers:**
- I enjoy going twice a week.
- I like it a lot!

---

### Type 3: Subject Questions 👤

**When asking about WHO likes/loves/enjoys something:**

**Structure:**
```
Who + likes/loves/enjoys + -ing?
```

**Examples:**
- **Who likes** playing football?
- **Who loves** cooking Italian food?
- **Who enjoys** going to concerts?
- **Who hates** waking up early?

**Note:** Use the -s form (likes, loves, enjoys) because "who" is treated as third person singular.

**Answers:**
- John does. / Mary does.
- I do. / We do.
- Everyone does!
- Nobody does.

---

### Type 4: Questions with MIND 🤔

**Structure with MIND (special - asking permission or making requests):**

**Would you mind + -ing?** (Polite request)
- **Would you mind helping** me?
- **Would you mind waiting** a moment?
- **Would you mind closing** the window?

**Answers:**
- Not at all! (= I don't mind = Yes, I'll do it)
- Of course not! (= I don't mind = Yes, I'll do it)
- No, I don't mind. (= Yes, I'll do it)

**Note:** Answering "no" means "yes, I'll help"! This can be confusing!

**Do you mind + -ing?** (More direct)
- **Do you mind waiting?**
- **Do you mind coming** back later?

---

### Common Question Patterns:

| Question Type | Example | Answer |
|--------------|---------|--------|
| Yes/No | Do you like swimming? | Yes, I do. / No, I don't. |
| What | What do you like doing? | I like reading. |
| Which (choice) | Which do you prefer? | I prefer coffee. |
| Where | Where do you like going? | I like going to the park. |
| When | When do you enjoy reading? | I enjoy reading at night. |
| Why | Why do you like it? | Because it's fun. |
| How often | How often do you go? | Twice a week. |
| Who | Who likes dancing? | Sarah does. |

---

### Follow-up Questions:

After someone answers, you can ask follow-up questions:

**Conversation example:**
- A: **Do you like reading?**
- B: Yes, I love it!
- A: **What kind of books do you like reading?**
- B: I like reading mystery novels.
- A: **Who's your favorite author?**
- B: Agatha Christie.

---

### Short Questions for Quick Responses:

**In conversation, you can use short forms:**
- Like it? (Do you like it?)
- Enjoy yourself? (Did you enjoy yourself?)
- Love to! (Would you love to?)

---

### 🎯 Key Point:
Use DO/DOES to form questions about preferences. Remember: Do + I/you/we/they, Does + he/she/it. The verb after the subject stays in base form + -ing!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 32-36: Audio examples for questions
    cells.append(
        create_cell(
            "code",
            """# Questions - Yes/No
audio.play_audio("Do you like reading books?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.create_conversation_audio([
    ("Person A", "Do you like reading books?"),
    ("Person B", "Yes, I love it! I read every day.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Questions - What
audio.play_audio("What do you like doing in your free time?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.create_conversation_audio([
    ("Person A", "What do you like doing in your free time?"),
    ("Person B", "I like playing sports and listening to music.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Questions - Which (preference)
audio.create_conversation_audio([
    ("Person A", "Which do you prefer, reading or watching TV?"),
    ("Person B", "I prefer reading. It's more relaxing.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 37: Section 9 - Common Collocations
    cells.append(
        create_cell(
            "markdown",
            """## 9. Common Collocations (Natural Combinations) 🔗

Certain verbs naturally go together with preference verbs. Learning these **collocations** makes your English sound more natural!

### Reading & Learning Activities 📚

**Common combinations:**
- like/love/enjoy **reading** (books, novels, magazines, newspapers)
- like/love/enjoy **learning** (languages, new things, skills)
- like/love/enjoy **studying** (history, science, English)
- like/love/enjoy **writing** (stories, emails, poetry)
- like/love/enjoy **doing** research

**Examples:**
- I **love reading** mystery novels before bed.
- She **enjoys learning** new languages.
- They **like studying** together at the library.
- He **loves writing** short stories.
- We **enjoy doing** research on history.

---

### Entertainment & Media 🎬

**Common combinations:**
- like/love/enjoy **watching** (movies, TV shows, sports, videos)
- like/love/enjoy **listening to** (music, podcasts, radio, audiobooks)
- like/love/enjoy **playing** (video games, board games)
- like/love/enjoy **going to** (movies, concerts, theater, shows)
- like/love/enjoy **browsing** (social media, the internet)

**Examples:**
- I **love watching** documentaries on weekends.
- She **enjoys listening to** jazz music.
- They **like playing** video games together.
- He **loves going to** rock concerts.
- We **enjoy browsing** social media during breaks.

---

### Physical Activities & Sports 🏃

**Common combinations:**
- like/love/enjoy **playing** (football, basketball, tennis, golf)
- like/love/enjoy **doing** (yoga, exercise, sports, martial arts)
- like/love/enjoy **running** (in the park, marathons)
- like/love/enjoy **swimming** (in the pool, ocean)
- like/love/enjoy **cycling** (to work, in the mountains)
- like/love/enjoy **working out** (at the gym, at home)
- like/love/enjoy **hiking** (in nature, mountains)
- like/love/enjoy **dancing** (salsa, ballet, at parties)

**Examples:**
- I **love playing** tennis on Saturdays.
- She **enjoys doing** yoga every morning.
- They **like running** in the park.
- He **loves swimming** in the ocean.
- We **enjoy cycling** through the countryside.

---

### Food & Cooking 🍳

**Common combinations:**
- like/love/enjoy **cooking** (dinner, Italian food, for friends)
- like/love/enjoy **eating** (out, healthy food, seafood)
- like/love/enjoy **baking** (cakes, bread, cookies)
- like/love/enjoy **trying** (new restaurants, new foods)
- like/love/enjoy **drinking** (coffee, tea, wine)
- hate/don't like **washing** (dishes, pots and pans)

**Examples:**
- I **love cooking** Italian food for my family.
- She **enjoys eating** at new restaurants.
- They **like baking** cookies on weekends.
- He **loves trying** exotic foods.
- We **enjoy drinking** coffee in the morning.
- I **hate washing** dishes!

---

### Social Activities 👥

**Common combinations:**
- like/love/enjoy **spending time** (with friends, with family, alone)
- like/love/enjoy **talking** (to people, on the phone, about politics)
- like/love/enjoy **meeting** (new people, friends, for coffee)
- like/love/enjoy **hanging out** (with friends, at the mall)
- like/love/enjoy **chatting** (online, with neighbors)
- like/love/enjoy **going out** (to eat, with friends, at night)
- like/love/enjoy **visiting** (friends, museums, relatives)
- like/love/enjoy **socializing** (at parties, at work)

**Examples:**
- I **love spending time** with my family.
- She **enjoys talking** to new people.
- They **like meeting** for coffee on Fridays.
- He **loves hanging out** with his friends.
- We **enjoy going out** to dinner.

---

### Creative Activities 🎨

**Common combinations:**
- like/love/enjoy **painting** (landscapes, portraits)
- like/love/enjoy **drawing** (cartoons, sketches)
- like/love/enjoy **taking** photos (of nature, portraits)
- like/love/enjoy **making** (crafts, jewelry, furniture)
- like/love/enjoy **designing** (websites, graphics, clothes)
- like/love/enjoy **playing** (musical instruments: guitar, piano)
- like/love/enjoy **singing** (in the shower, in a choir)

**Examples:**
- I **love painting** landscapes on weekends.
- She **enjoys taking** photos of nature.
- They **like making** handmade jewelry.
- He **loves playing** the guitar.
- We **enjoy singing** together.

---

### Work & Productivity 💼

**Common combinations:**
- like/love/enjoy **working** (from home, with people, alone, on projects)
- hate/don't like **commuting** (to work, in traffic)
- like/love/enjoy **solving** (problems, puzzles)
- like/love/enjoy **helping** (people, customers, colleagues)
- like/love/enjoy **organizing** (things, events, my desk)
- hate/don't like **attending** (meetings, conferences)
- hate/don't like **filling out** (forms, paperwork)

**Examples:**
- I **enjoy working** from home.
- She **hates commuting** in rush hour.
- They **love solving** complex problems.
- He **enjoys helping** customers.
- We **hate attending** long meetings.

---

### Relaxation & Downtime 😌

**Common combinations:**
- like/love/enjoy **relaxing** (at home, on the beach)
- like/love/enjoy **sleeping** (late, in on weekends)
- like/love/enjoy **taking** (naps, breaks, baths)
- like/love/enjoy **lying** (on the couch, in bed, in the sun)
- like/love/enjoy **doing** (nothing, meditation)
- hate/don't like **getting up** (early, on Mondays)

**Examples:**
- I **love relaxing** on the beach.
- She **enjoys sleeping** late on Sundays.
- They **like taking** afternoon naps.
- He **loves lying** in the sun.
- We **hate getting up** early on Mondays.

---

### Travel & Adventure ✈️

**Common combinations:**
- like/love/enjoy **traveling** (abroad, solo, with friends)
- like/love/enjoy **exploring** (new places, cities, nature)
- like/love/enjoy **visiting** (museums, historical sites, new countries)
- like/love/enjoy **going** (on vacation, on road trips, camping)
- like/love/enjoy **discovering** (new cultures, hidden gems)
- hate/don't like **packing** (suitcases, bags)

**Examples:**
- I **love traveling** to new countries.
- She **enjoys exploring** old cities.
- They **like visiting** historical sites.
- He **loves going** on road trips.
- We **hate packing** suitcases!

---

### Household Chores 🏠

**Common combinations:**
- hate/don't like **cleaning** (the house, the bathroom, my room)
- hate/don't like **doing** (laundry, dishes, housework)
- hate/don't like **washing** (clothes, windows, the car)
- hate/don't like **ironing** (clothes, shirts)
- hate/don't like **vacuuming** (the carpet, the floor)
- don't mind **tidying** (up, my desk)

**Examples:**
- I **hate cleaning** the bathroom.
- She **doesn't like doing** laundry.
- They **hate washing** dishes.
- He **hates ironing** his shirts.
- I **don't mind tidying** my room.

---

### Waiting & Delays ⏰

**Common combinations:**
- hate/don't like **waiting** (in line, for the bus, for people)
- hate/don't like **being** (late, stuck in traffic, interrupted)
- hate/don't like **standing** (in line, in the rain)

**Examples:**
- I **hate waiting** in long lines.
- She **hates being** late for appointments.
- They **don't like standing** in the rain.

---

### Quick Reference: Most Common Collocations

**Top 20 most common:**
1. like/love **watching** TV/movies
2. like/love **listening to** music
3. like/love **reading** books
4. like/love **playing** sports/games
5. like/love **spending time** with friends/family
6. like/love **eating** out
7. like/love **cooking** at home
8. like/love **traveling** abroad
9. enjoy **working** from home
10. enjoy **learning** new things
11. hate **waiting** in line
12. hate **getting up** early
13. hate **cleaning** the house
14. hate **doing** homework
15. don't mind **helping** people
16. enjoy **going** to concerts
17. love **dancing** at parties
18. like **taking** photos
19. enjoy **talking** to friends
20. hate **being** late

---

### 🎯 Key Point:
Learning collocations (natural word combinations) helps you sound more fluent and natural. Don't just learn single words - learn phrases!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 38: Collocation visual aid
    cells.append(
        create_cell(
            "code",
            """# Display common collocations chart
display(HTML('''
<div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border: 2px solid #FF9800;">
<h3 style="color: #F57C00;">Most Common Collocations</h3>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
<div>
<h4>💚 Positive (LIKE/LOVE)</h4>
<ul>
<li>love <b>watching</b> movies</li>
<li>like <b>listening to</b> music</li>
<li>enjoy <b>reading</b> books</li>
<li>love <b>spending time</b> with family</li>
<li>like <b>playing</b> sports</li>
</ul>
</div>
<div>
<h4>❤️ Negative (HATE/DON'T LIKE)</h4>
<ul>
<li>hate <b>waiting</b> in line</li>
<li>don't like <b>getting up</b> early</li>
<li>hate <b>cleaning</b> the house</li>
<li>don't like <b>doing</b> homework</li>
<li>hate <b>being</b> late</li>
</ul>
</div>
</div>
</div>
'''))""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 39: Section 10 - Talking About Hobbies and Free Time
    cells.append(
        create_cell(
            "markdown",
            """## 10. Talking About Hobbies and Free Time 🎨

One of the most common uses of preference verbs + -ing is talking about hobbies and free time activities.

### Common Questions About Hobbies:

**Direct questions:**
- What do you like doing in your free time?
- What are your hobbies?
- What do you do for fun?
- What do you enjoy doing on weekends?
- What do you like to do after work?

**Follow-up questions:**
- How often do you do that?
- When did you start?
- Why do you like it?
- Are you good at it?
- Where do you usually do it?

---

### How to Answer - Structure:

**Pattern 1: Simple answer**
```
I like/love/enjoy + -ing + (complement)
```
- I **like reading** mystery novels.
- I **love playing** tennis.
- I **enjoy cooking** Italian food.

**Pattern 2: Multiple hobbies**
```
I like + -ing + and + -ing
```
- I **like reading** and **watching** movies.
- I **love swimming** and **hiking**.
- I **enjoy cooking** and **baking**.

**Pattern 3: With time reference**
```
I like + -ing + time expression
```
- I **like reading** before bed.
- I **love running** in the morning.
- I **enjoy playing** guitar on weekends.

**Pattern 4: With reason**
```
I like + -ing + because + clause
```
- I **like reading** because it's relaxing.
- I **love dancing** because it's fun.
- I **enjoy cooking** because I can be creative.

**Pattern 5: With additional details**
```
I really/absolutely + like/love + -ing + detail
```
- I **really enjoy** swimming in the ocean.
- I **absolutely love** traveling to new countries.
- I **really like** playing basketball with friends.

---

### Common Hobby Categories:

**1. Sports & Fitness:**
- I **love playing** tennis/football/basketball.
- I **enjoy doing** yoga every morning.
- I **like running** in the park.
- I **love swimming** at the beach.
- I **enjoy cycling** on weekends.
- I **like working out** at the gym.

**2. Creative Hobbies:**
- I **love painting** landscapes.
- I **enjoy taking** photos.
- I **like drawing** cartoons.
- I **love playing** the guitar.
- I **enjoy writing** stories.
- I **like making** crafts.

**3. Reading & Learning:**
- I **love reading** novels.
- I **enjoy learning** languages.
- I **like studying** history.
- I **love reading** about science.
- I **enjoy doing** online courses.

**4. Entertainment:**
- I **love watching** movies.
- I **enjoy listening to** music.
- I **like playing** video games.
- I **love going to** concerts.
- I **enjoy binge-watching** TV series.

**5. Social Activities:**
- I **love spending time** with friends.
- I **enjoy meeting** new people.
- I **like going out** to eat.
- I **love talking** to people.
- I **enjoy hanging out** at cafes.

**6. Outdoor Activities:**
- I **love hiking** in the mountains.
- I **enjoy camping** in nature.
- I **like fishing** at the lake.
- I **love gardening** in my backyard.
- I **enjoy walking** in the park.

**7. Cooking & Food:**
- I **love cooking** new recipes.
- I **enjoy baking** cakes.
- I **like trying** new restaurants.
- I **love eating** different cuisines.

**8. Travel:**
- I **love traveling** to new places.
- I **enjoy exploring** different cities.
- I **like visiting** historical sites.
- I **love going on** road trips.

---

### Sample Conversations:

**Conversation 1: Getting to know someone**
```
A: So, what do you like doing in your free time?
B: I love reading and watching movies. How about you?
A: I enjoy playing sports, especially basketball.
B: Oh, that's cool! How often do you play?
A: I play twice a week with friends.
```

**Conversation 2: Talking about weekends**
```
A: What do you usually do on weekends?
B: I enjoy spending time outdoors. I love hiking and cycling.
A: That sounds great! I prefer staying home. I like reading and cooking.
B: Do you like cooking any particular type of food?
A: Yes, I love cooking Italian food!
```

**Conversation 3: Finding common interests**
```
A: Do you like watching movies?
B: Yes, I love it! What kind of movies do you like watching?
A: I enjoy watching action movies and thrillers. What about you?
B: I prefer comedies and romantic movies.
A: Maybe we can watch a movie together sometime!
```

---

### Expressing Intensity with Adverbs:

**Making it stronger:**
- I **really** like swimming.
- I **absolutely** love dancing!
- I **totally** enjoy cooking.
- I **definitely** prefer reading.

**Making it softer:**
- I **kind of** like running.
- I **sort of** enjoy painting.
- I **quite** like playing chess.
- I **fairly** enjoy gardening.

---

### Talking About New Hobbies:

**Starting a new hobby:**
- I've **started** learning the guitar.
- I've **begun** doing yoga.
- I've **recently started** painting.
- I'm **learning** to play tennis.

**Wanting to try:**
- I'd **like to try** rock climbing.
- I **want to start** learning Spanish.
- I'm **interested in** taking up photography.
- I'd **love to learn** how to surf.

**Past hobbies:**
- I **used to love** playing video games. (but not anymore)
- I **used to enjoy** running. (in the past)
- I **stopped** playing the piano. (no longer do it)

---

### Useful Phrases:

**Showing enthusiasm:**
- I'm **really into** photography.
- I'm **passionate about** cooking.
- I'm **crazy about** football.
- I'm **a big fan of** hiking.

**Showing lack of interest:**
- I'm **not really into** sports.
- I'm **not keen on** cooking.
- I'm **not a fan of** video games.

**Asking for details:**
- What kind of books do you like reading?
- Where do you like playing tennis?
- When do you usually go running?
- Who do you enjoy spending time with?

---

### Quick Tip for Conversation:

When someone tells you their hobby:
1. Show interest: "Oh, that's interesting!"
2. Ask a question: "How long have you been doing that?"
3. Share your experience: "I've tried that too!" or "I've never done that."
4. Find connections: "We should do it together sometime!"

---

### 🎯 Key Point:
Talking about hobbies and free time is one of the most common conversation topics. Using LIKE/LOVE/ENJOY + -ing naturally helps you express your interests clearly and start meaningful conversations!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 40-42: Audio examples for hobbies conversations
    cells.append(
        create_cell(
            "code",
            """# Hobbies conversation 1
audio.create_conversation_audio([
    ("Person A", "What do you like doing in your free time?"),
    ("Person B", "I love reading books and listening to music. How about you?"),
    ("Person A", "I enjoy playing sports, especially basketball.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Hobbies conversation 2
audio.create_conversation_audio([
    ("Person A", "Do you have any hobbies?"),
    ("Person B", "Yes! I love painting and taking photos. I really enjoy being creative."),
    ("Person A", "That's amazing! I'd love to see your work sometime.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Hobbies conversation 3
audio.create_conversation_audio([
    ("Person A", "What do you do for fun?"),
    ("Person B", "I enjoy hiking and camping. I love spending time in nature."),
    ("Person A", "That sounds great! I prefer staying home and watching movies.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 43: Section 11 - Common Mistakes
    cells.append(
        create_cell(
            "markdown",
            """## 11. Common Mistakes to Avoid ⚠️

Here are the most common errors learners make with preference verbs + -ing:

### Mistake 1: Forgetting -ing (Using Base Form)

**Wrong: Using the infinitive without 'to' or base verb**

❌ I like **read** books.
[OK] I like **reading** books.

❌ She loves **cook**.
[OK] She loves **cooking**.

❌ They enjoy **play** football.
[OK] They enjoy **playing** football.

❌ He hates **wait**.
[OK] He hates **waiting**.

**Rule:** After LIKE, LOVE, HATE, ENJOY, etc., always use **-ing form**!

---

### Mistake 2: Confusing "LIKE + -ing" vs "LIKE TO + infinitive"

Both are possible, but with different meanings:

**LIKE + -ing** = general preference/enjoyment
- I **like reading**. (I enjoy it in general)

**LIKE TO + infinitive** = habit/choice
- I **like to read** before bed. (I choose to do this)

**Common mistake:**
❌ I like **to reading**.
[OK] I like **reading**. OR I like **to read**.

**With LOVE and HATE:**
- Both forms are possible but -ing is more common
- I love **dancing**. (more common)
- I love **to dance**. (also correct, less common)

**With ENJOY:**
- ONLY use -ing (infinitive is WRONG)
- [OK] I enjoy **reading**.
- ❌ I enjoy **to read**.

**With PREFER:**
- Both forms possible
- I prefer **reading**. (more common)
- I prefer **to read**. (also correct)

---

### Mistake 3: Wrong Verb Form in Negatives

**Using -s or wrong auxiliary:**

❌ She don't like cooking.
[OK] She **doesn't** like cooking.

❌ She doesn't **likes** cooking.
[OK] She doesn't **like** cooking.

❌ He no like swimming.
[OK] He **doesn't like** swimming.

❌ They don't likes playing.
[OK] They don't like playing.

**Rule:** DON'T/DOESN'T + base verb + -ing

---

### Mistake 4: Wrong Verb Form in Questions

**Using -s or forgetting auxiliary:**

❌ **Likes** you reading?
[OK] **Do** you like reading?

❌ **Does** you like swimming?
[OK] **Do** you like swimming?

❌ She likes reading?
[OK] **Does** she like reading?

❌ What you like doing?
[OK] What **do** you like doing?

**Rule:** DO/DOES + subject + base verb + -ing

---

### Mistake 5: Incorrect -ing Spelling

**Not following spelling rules:**

❌ I like **runing**.
[OK] I like **running**. (double the n)

❌ She loves **danceing**.
[OK] She loves **dancing**. (drop the e)

❌ They enjoy **swiming**.
[OK] They enjoy **swimming**. (double the m)

❌ He hates **stoping**.
[OK] He hates **stopping**. (double the p)

**Review Section 6 for spelling rules!**

---

### Mistake 6: Using Wrong Preposition

**Adding wrong preposition after preference verb:**

❌ I like **of** reading.
[OK] I like reading.

❌ She loves **for** cooking.
[OK] She loves cooking.

❌ They enjoy **to** playing.
[OK] They enjoy playing.

**Exception: LISTEN requires "to"**
[OK] I like **listening to** music.
❌ I like **listening** music.

---

### Mistake 7: Missing Articles or Objects

**Sometimes you need more after -ing:**

❌ I like cooking. ✓ (This is fine!)
❌ I like playing. (incomplete - playing what?)
[OK] I like playing **the piano**.
[OK] I like playing **football**.

**Some verbs need objects:**
- playing → playing + WHAT (sport/instrument/game)
- listening → listening to + WHAT
- watching → watching + WHAT
- reading → can be alone OR reading + WHAT

**These can be alone:**
- swimming, running, dancing, cooking, singing, etc.

---

### Mistake 8: Wrong Word Order

**Putting -ing in wrong place:**

❌ I reading like.
[OK] I like reading.

❌ She loves really dancing.
[OK] She **really** loves dancing.

❌ Playing football I love.
[OK] I love playing football.

**Rule:** Subject + preference verb + -ing + (complement)

---

### Mistake 9: Using "Very Much" in Wrong Position

**Incorrect placement of "very much":**

❌ I very much like reading.
[OK] I like reading **very much**.

❌ She very much loves cooking.
[OK] She loves cooking **very much**.

**Correct positions:**
- I **really** like reading. (adverb before verb)
- I like reading **very much**. (at the end)
- I like reading **a lot**. (at the end)

---

### Mistake 10: Translating Directly from Native Language

**Different languages use different structures:**

Many languages use infinitive instead of -ing:
- Spanish: Me gusta **leer**. (infinitive)
- English: I like **reading**. (gerund)

**Don't translate word-for-word!**

---

### Mistake 11: Overusing "LOVE" and "HATE"

**Being too extreme:**

Some learners say:
- ❌ I **love** everything!
- ❌ I **hate** everything!

**Better to vary:**
- Use **like** for positive feelings
- Use **don't like** or **don't enjoy** for negative
- Save **love** and **hate** for strong feelings

---

### Mistake 12: Confusing Subject-Verb Agreement

**Wrong person with verb:**

❌ She **like** cooking.
[OK] She **likes** cooking.

❌ He **love** reading.
[OK] He **loves** reading.

❌ They **likes** swimming.
[OK] They **like** swimming.

**Rule:**
- I/You/We/They → like, love, hate, enjoy
- He/She/It → likes, loves, hates, enjoys

---

### Mistake 13: Using "FOR" Incorrectly

**Adding unnecessary "for":**

❌ I like reading **for** books.
[OK] I like reading books.

❌ She loves cooking **for** Italian food.
[OK] She loves cooking Italian food.

**When FOR is correct:**
- I like cooking **for** my family. (for = beneficiary)
- She loves singing **for** people. (for = audience)

---

### Mistake 14: Wrong Stress Pattern

**Pronunciation mistake (less serious but common):**

- ❌ I like **READ**-ing (wrong stress)
- [OK] I like **read**-ing (stress on first syllable of root)

- ❌ She loves **swim-MING** (wrong stress)
- [OK] She loves **SWIM**-ming (stress on first syllable)

**Rule:** Usually stress the root verb, not the -ing ending.

---

### Quick Error Check:

Before saying/writing your sentence, ask:
1. Did I use **-ing** form? ✓
2. Did I spell the **-ing** correctly? ✓
3. For negatives: Did I use **don't/doesn't**? ✓
4. For questions: Did I use **do/does**? ✓
5. Did I use the right **subject-verb agreement**? ✓

---

### 🎯 Key Point:
The most common mistake is forgetting -ing! Always remember: LIKE/LOVE/HATE/ENJOY + **verb-ing**!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 44: Section 12 - Practice Conversations
    cells.append(
        create_cell(
            "markdown",
            """## 12. Practice Conversations 🗣️

Let's see preference expressions in action through natural conversations!

### Conversation 1: First Meeting at a Party 🎉""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 1: First meeting
audio.create_conversation_audio([
    ("Anna", "Hi! I'm Anna. Nice to meet you!"),
    ("Ben", "Hi Anna! I'm Ben. So, what do you like doing for fun?"),
    ("Anna", "I love reading books and watching movies. How about you?"),
    ("Ben", "I enjoy playing sports, especially basketball. Do you like sports?"),
    ("Anna", "Not really. I don't mind watching, but I don't enjoy playing."),
    ("Ben", "That's okay! What kind of movies do you like watching?"),
    ("Anna", "I love watching thrillers and comedies. What about you?"),
    ("Ben", "I prefer action movies, but I don't mind comedies either!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell("markdown", """### Conversation 2: Weekend Plans 📅""", f"cell-{cell_counter}")
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 2: Weekend plans
audio.create_conversation_audio([
    ("Maria", "What are you doing this weekend?"),
    ("Tom", "I'm not sure yet. What do you like doing on weekends?"),
    ("Maria", "I love going to the beach and swimming. The weather is perfect!"),
    ("Tom", "That sounds nice, but I hate getting sunburned!"),
    ("Maria", "You can use sunscreen! Do you like swimming?"),
    ("Tom", "I don't mind swimming, but I prefer staying indoors. I enjoy playing video games."),
    ("Maria", "Maybe you can come to the beach in the evening? We usually barbecue."),
    ("Tom", "Oh, I love eating barbecue! That sounds great!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell("markdown", """### Conversation 3: Job Interview 💼""", f"cell-{cell_counter}")
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 3: Job interview
audio.create_conversation_audio([
    ("Interviewer", "Tell me, what do you enjoy most about your current job?"),
    ("Candidate", "I really enjoy working with people and solving problems."),
    ("Interviewer", "That's great! And what don't you like about it?"),
    ("Candidate", "Honestly, I don't enjoy doing repetitive paperwork. I prefer more creative tasks."),
    ("Interviewer", "I understand. Do you mind working on weekends occasionally?"),
    ("Candidate", "I don't mind working weekends if it's important, but I prefer having regular hours."),
    ("Interviewer", "Good to know. Do you like working in teams or independently?"),
    ("Candidate", "I enjoy working in teams. I love collaborating with colleagues.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown", """### Conversation 4: Dating Conversation 💑""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 4: Dating
audio.create_conversation_audio([
    ("Sarah", "So, what do you like doing in your free time?"),
    ("John", "I love traveling and trying new restaurants. How about you?"),
    ("Sarah", "I enjoy traveling too! Where do you like going?"),
    ("John", "I prefer going to beach destinations. I love swimming and surfing."),
    ("Sarah", "That's awesome! I like hiking in the mountains. Do you like hiking?"),
    ("John", "I don't mind it, but I'm not very good at it!"),
    ("Sarah", "Maybe we can try both - beach and mountains!"),
    ("John", "I'd love that! By the way, do you like cooking?"),
    ("Sarah", "Yes! I love cooking Italian food. Do you enjoy cooking?"),
    ("John", "I enjoy eating more than cooking!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown", """### Conversation 5: Roommate Discussion 🏠""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 5: Roommates
audio.create_conversation_audio([
    ("Alex", "We should talk about household chores. What do you hate doing?"),
    ("Jordan", "I absolutely hate cleaning the bathroom! What about you?"),
    ("Alex", "I don't mind cleaning bathrooms, but I hate doing laundry."),
    ("Jordan", "I don't mind doing laundry at all! I actually enjoy it."),
    ("Alex", "Perfect! And do you like cooking?"),
    ("Jordan", "I love cooking! I enjoy trying new recipes."),
    ("Alex", "Great! I don't enjoy cooking, but I love eating! And I enjoy washing dishes."),
    ("Jordan", "This is perfect - I hate washing dishes!"),
    ("Alex", "Looks like we make a good team!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Conversation 6: Fitness Center Conversation 🏃""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 6: Fitness center
audio.create_conversation_audio([
    ("Trainer", "What kind of exercise do you enjoy doing?"),
    ("Client", "I like running and cycling, but I hate lifting weights."),
    ("Trainer", "Why don't you like lifting weights?"),
    ("Client", "I don't enjoy doing the same movements over and over. I prefer cardio."),
    ("Trainer", "I understand. Do you mind trying some yoga classes?"),
    ("Client", "I've never tried yoga. I'd love to try it!"),
    ("Trainer", "Great! Do you like doing exercises in groups or alone?"),
    ("Client", "I enjoy working out alone. I love listening to music while exercising.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 53: Pronunciation guide
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

    # Cell 55: What's Next
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

Now that you understand how to express preferences with -ing, it's time to practice!

### Continue to:
1. **02_controlled_practice.ipynb** - 70+ exercises on LIKE/LOVE/HATE + -ing
2. **03_meaningful_practice.ipynb** - Personal activities about YOUR preferences
3. **04_communicative_practice.ipynb** - Real conversations about interests

---

## 📌 Key Takeaways

[OK] **Preference verbs + -ing:** like, love, hate, enjoy, prefer, don't mind

[OK] **Basic structure:** Subject + verb + verb-ing

[OK] **-ing forms:** read → reading, make → making, run → running

[OK] **LOVE** = strong positive (+++)

[OK] **LIKE** = positive (++)

[OK] **DON'T MIND** = neutral (+/-)

[OK] **DON'T LIKE** = negative (--)

[OK] **HATE** = strong negative (---)

[OK] **Negatives:** don't/doesn't + verb + -ing

[OK] **Questions:** Do/Does + subject + verb + -ing?

[OK] **Common collocations:** like reading, love dancing, hate waiting

[OK] **Hobbies:** Perfect for talking about free time activities!

[OK] **Spelling rules:** Most add -ing, drop -e, double consonants for CVC

[OK] **LIKE -ing vs LIKE TO:** Both possible but -ing for general preferences

[OK] **ENJOY:** Only use -ing (never infinitive)

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
            "language_info": {"name": "python", "version": "3.8.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    return notebook


def main():
    """Main function to build and save the notebook"""
    # Build the notebook
    notebook = build_phase1_notebook()

    # Define output path
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "01_introduction.ipynb")

    # Save the notebook
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    # Get file size
    file_size = os.path.getsize(output_file)
    file_size_kb = file_size / 1024

    print(f"[OK] Phase 1 notebook created successfully!")
    print(f"📁 Location: {output_file}")
    print(f"📊 File size: {file_size_kb:.2f} KB")
    print(f"📝 Total cells: {len(notebook['cells'])}")

    # Check if size is within target range
    if 18 <= file_size_kb <= 22:
        print("[OK] File size is within target range (18-22 KB)")
    else:
        print(
            f"⚠️ File size is outside target range. Target: 18-22 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
