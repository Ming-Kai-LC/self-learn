"""
Builder script for Module 13 Phase 1: This, That, These, Those - Introduction
Target: 18-22 KB, 40-50 cells, 10-12 comprehensive sections
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
            """# Module 13: This, That, These, Those - Introduction

## 📚 Phase 1: Introduction (15% of learning time)

**Welcome to Module 13!** 🎉

**Demonstratives** (THIS, THAT, THESE, THOSE) are words we use to point to things and show distance. They help us identify and talk about specific objects, people, or ideas - whether they are near us or far from us!

### Learning Objectives
By the end of this module, you will be able to:
- [OK] Use THIS for singular objects near you
- [OK] Use THAT for singular objects far from you
- [OK] Use THESE for plural objects near you
- [OK] Use THOSE for plural objects far from you
- [OK] Understand distance concepts (physical and abstract)
- [OK] Use demonstratives with and without nouns
- [OK] Ask questions with demonstratives
- [OK] Use time references (this week, that day)
- [OK] Use demonstratives in phone conversations
- [OK] Avoid common mistakes

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

print("[OK] Setup complete! Let's learn about demonstratives.")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 2: Section 1 - What are Demonstratives (Overview Table)
    cells.append(
        create_cell(
            "markdown",
            """## 1. What are Demonstratives? 👉

**Demonstratives** are special words that help us point to specific things. In English, we have four main demonstratives:

### Complete Overview Table:

| Demonstrative | Number | Distance | Example | When to Use |
|---------------|--------|----------|---------|-------------|
| **THIS** | Singular (one) | Near (close to speaker) | This book is mine. | One thing close to you |
| **THAT** | Singular (one) | Far (away from speaker) | That car is red. | One thing away from you |
| **THESE** | Plural (2+) | Near (close to speaker) | These books are mine. | Multiple things close to you |
| **THOSE** | Plural (2+) | Far (away from speaker) | Those cars are red. | Multiple things away from you |

### Two Key Questions to Ask:
1. **How many?** → Singular (one) or Plural (more than one)
2. **How far?** → Near (close to me) or Far (away from me)

### Visual Representation:
```
        YOU (Speaker)
         👤
    NEAR | FAR
    -----|-----
THIS     |     THAT     (Singular - one thing)
THESE    |     THOSE    (Plural - multiple things)
```

### 🎯 Key Point:
Demonstratives replace or go with nouns. They answer the question "Which one?" or "Which ones?"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 3: Section 2 - THIS (Singular, Near)
    cells.append(
        create_cell(
            "markdown",
            """## 2. THIS - Singular, Near (One Thing Close to You) 👆

**THIS** is used for:
- **ONE thing** (singular)
- **NEAR you** (close to the speaker)

### Structure:
```
THIS + singular noun
THIS + is/was + ...
```

### Usage Examples:

**1. With a noun (pointing to objects):**
- **This** book is interesting. (one book, in my hand)
- **This** pen doesn't work. (one pen, near me)
- **This** chair is comfortable. (one chair, I'm sitting on it)
- **This** coffee is delicious. (one cup, I'm drinking it)

**2. Without a noun (THIS alone):**
- **This** is my house. (pointing to the house)
- **This** is difficult. (referring to a situation)
- **This** is John. (introducing someone)
- What is **this**? (asking about something near)

**3. Introducing people:**
- **This** is my friend Maria. (Maria is near me)
- **This** is my brother. (brother is standing next to me)

**4. On the phone:**
- "Hello, **this** is Sarah speaking." (identifying yourself)
- "Is **this** John?" (asking who you're speaking to)

### Grammar Rules:
- [OK] Use **THIS IS** (not "This are")
- [OK] **This** book (singular noun only)
- [OK] Can use alone: "I like this." (no noun needed)

### Common Contexts:
- 📱 Phone calls: "This is John."
- 👋 Introductions: "This is my friend."
- 👆 Pointing: "This tastes good."
- 📍 Showing: "Look at this!"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 4-7: Audio examples for THIS
    cells.append(
        create_cell(
            "code",
            """# THIS - Examples with audio
audio.play_audio("This book is very interesting.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("This is my new phone.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("This coffee tastes great.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("This is my friend Sarah.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 8: Section 3 - THAT (Singular, Far)
    cells.append(
        create_cell(
            "markdown",
            """## 3. THAT - Singular, Far (One Thing Away from You) 👉

**THAT** is used for:
- **ONE thing** (singular)
- **FAR from you** (away from the speaker)

### Structure:
```
THAT + singular noun
THAT + is/was + ...
```

### Usage Examples:

**1. With a noun (pointing to distant objects):**
- **That** building is tall. (one building, far from me)
- **That** car is expensive. (one car, across the street)
- **That** tree is beautiful. (one tree, in the distance)
- **That** restaurant is good. (one restaurant, not near here)

**2. Without a noun (THAT alone):**
- **That** is my school. (pointing to a distant building)
- **That** is interesting. (referring to something mentioned)
- **That** is correct. (agreeing with a statement)
- What is **that**? (asking about something far)

**3. Referring to past or mentioned ideas:**
- I heard the news. **That** is sad. (referring to the news)
- She's moving. **That** is exciting! (referring to her moving)

**4. Time reference (past time):**
- **That** day was special. (a day in the past)
- I remember **that** moment. (a past moment)

### Grammar Rules:
- [OK] Use **THAT IS** (not "That are")
- [OK] **That** car (singular noun only)
- [OK] Can use alone: "I want that." (no noun needed)

### Distance Types:
- **Physical distance:** That mountain is high. (physically far)
- **Time distance:** That was yesterday. (time in the past)
- **Abstract distance:** That sounds difficult. (idea/concept)

### Common Contexts:
- 👀 Pointing to far objects: "Look at that!"
- 🕒 Past events: "That was fun."
- 💭 Ideas mentioned: "That makes sense."
- 🎯 Identifying: "What is that?"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 9-12: Audio examples for THAT
    cells.append(
        create_cell(
            "code",
            """# THAT - Examples with audio
audio.play_audio("That building is very tall.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("That is a great idea.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("That car over there is mine.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("That was an amazing movie.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 13: Section 4 - THESE (Plural, Near)
    cells.append(
        create_cell(
            "markdown",
            """## 4. THESE - Plural, Near (Multiple Things Close to You) 👆👆

**THESE** is used for:
- **TWO OR MORE things** (plural)
- **NEAR you** (close to the speaker)

### Structure:
```
THESE + plural noun
THESE + are/were + ...
```

### Usage Examples:

**1. With a noun (pointing to nearby objects):**
- **These** books are mine. (multiple books, in my hands)
- **These** shoes are comfortable. (multiple shoes, I'm wearing them)
- **These** cookies are delicious. (multiple cookies, near me)
- **These** flowers smell nice. (multiple flowers, close by)

**2. Without a noun (THESE alone):**
- **These** are my friends. (pointing to people near me)
- **These** are expensive. (referring to nearby items)
- I like **these**. (choosing nearby items)
- What are **these**? (asking about things near)

**3. Showing or presenting:**
- **These** are the new designs. (presenting nearby documents)
- **These** are my children. (introducing kids next to you)
- Look at **these**! (showing nearby items)

**4. Current items or topics:**
- **These** problems are difficult. (current problems)
- **These** days are busy. (current time period)

### Grammar Rules:
- [OK] Use **THESE ARE** (not "These is")
- [OK] **These** books (plural noun only)
- [OK] Can use alone: "I want these." (no noun needed)
- [OK] **THESE** is the plural form of **THIS**

### Comparison with THIS:
- THIS book → THESE books (one → many)
- THIS is mine → THESE are mine
- I like THIS → I like THESE

### Common Contexts:
- 🛍️ Shopping: "I'll take these."
- 📝 Presenting: "These are my ideas."
- 👋 Introducing: "These are my colleagues."
- 👆 Showing: "Look at these!"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 14-17: Audio examples for THESE
    cells.append(
        create_cell(
            "code",
            """# THESE - Examples with audio
audio.play_audio("These books are very interesting.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("These are my favorite shoes.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("These cookies taste amazing.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("These are my colleagues from work.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 18: Section 5 - THOSE (Plural, Far)
    cells.append(
        create_cell(
            "markdown",
            """## 5. THOSE - Plural, Far (Multiple Things Away from You) 👉👉

**THOSE** is used for:
- **TWO OR MORE things** (plural)
- **FAR from you** (away from the speaker)

### Structure:
```
THOSE + plural noun
THOSE + are/were + ...
```

### Usage Examples:

**1. With a noun (pointing to distant objects):**
- **Those** mountains are beautiful. (multiple mountains, far away)
- **Those** cars are expensive. (multiple cars, across the street)
- **Those** people are tourists. (multiple people, at a distance)
- **Those** houses are old. (multiple houses, not near here)

**2. Without a noun (THOSE alone):**
- **Those** are my neighbors. (pointing to distant people)
- **Those** are better. (comparing distant items)
- I prefer **those**. (choosing distant items)
- What are **those**? (asking about things far away)

**3. Referring to past or mentioned things:**
- I miss **those** days. (days in the past)
- **Those** were good times. (referring to past times)
- Remember **those** stories? (stories mentioned before)

**4. Distant groups or categories:**
- **Those** students are smart. (students over there)
- **Those** questions are difficult. (questions already mentioned)

### Grammar Rules:
- [OK] Use **THOSE ARE** (not "Those is")
- [OK] **Those** cars (plural noun only)
- [OK] Can use alone: "I want those." (no noun needed)
- [OK] **THOSE** is the plural form of **THAT**

### Comparison with THAT:
- THAT car → THOSE cars (one → many)
- THAT is mine → THOSE are mine
- I like THAT → I like THOSE

### Distance Types:
- **Physical distance:** Those birds are flying high. (far in space)
- **Time distance:** Those were happy days. (far in time)
- **Abstract distance:** Those ideas are interesting. (conceptual distance)

### Common Contexts:
- 👀 Pointing far: "Look at those!"
- 🕒 Past events: "Those were the days."
- 🏪 Shopping: "I prefer those."
- 🎯 Identifying: "What are those?"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 19-22: Audio examples for THOSE
    cells.append(
        create_cell(
            "code",
            """# THOSE - Examples with audio
audio.play_audio("Those mountains are very beautiful.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those are my favorite restaurants.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those people over there are my friends.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those were the best days of my life.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 23: Section 6 - Distance Concepts
    cells.append(
        create_cell(
            "markdown",
            """## 6. Distance Concepts (Physical vs Abstract) 📏

Distance with demonstratives isn't always about physical space. It can also be about time, emotional closeness, or abstract concepts.

### Types of Distance:

#### 1. Physical Distance (Space) 🌍
Distance you can see and measure:

**NEAR (THIS/THESE):**
- This room is small. (I'm in the room)
- These chairs are comfortable. (I'm sitting on them)
- This is in my hand.

**FAR (THAT/THOSE):**
- That mountain is high. (I see it in the distance)
- Those buildings are tall. (across the city)
- That is over there.

#### 2. Time Distance ⏰
How far away in time:

**NEAR = Present/Recent (THIS/THESE):**
- **This** week is busy. (current week)
- **This** morning I woke up early. (today's morning)
- **These** days I'm very happy. (current period)
- **This** year has been great. (current year)

**FAR = Past/Future (THAT/THOSE):**
- **That** day was special. (a specific past day)
- **That** year was difficult. (a past year)
- **Those** were happy times. (period in the past)
- Remember **that** summer? (past summer)

#### 3. Emotional/Psychological Distance 💭
How connected you feel:

**NEAR = Connected/Involved (THIS/THESE):**
- **This** is my problem. (I'm involved)
- **These** are my responsibilities. (I'm responsible)
- **This** matters to me. (I care about it)

**FAR = Distant/Detached (THAT/THOSE):**
- **That** is not my problem. (I'm not involved)
- **Those** are their issues. (not my concern)
- **That** doesn't concern me. (I'm detached)

#### 4. Abstract/Conceptual Distance 🎯
Ideas, topics, and situations:

**NEAR = Current topic (THIS/THESE):**
- **This** is important. (what we're discussing now)
- **This** makes sense. (the current explanation)
- **These** ideas are good. (ideas just presented)

**FAR = Previous topic (THAT/THOSE):**
- **That** was interesting. (something mentioned earlier)
- **That** reminds me of... (previous topic)
- **Those** points were good. (points made earlier)

### Summary Table:

| Distance Type | NEAR (THIS/THESE) | FAR (THAT/THOSE) |
|---------------|-------------------|------------------|
| **Physical** | This book (in my hand) | That book (on the shelf) |
| **Time** | This week (now) | That week (past) |
| **Emotional** | This is my issue (involved) | That is their issue (detached) |
| **Abstract** | This is the topic (current) | That was the topic (previous) |

### 🎯 Key Point:
"Near" and "far" are relative concepts. They depend on the speaker's perspective!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 24-27: Audio examples for distance concepts
    cells.append(
        create_cell(
            "code",
            """# Distance concepts - Time examples
audio.play_audio("This week has been very busy.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("That day was the happiest day of my life.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("These days I feel very energetic.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those were difficult times for everyone.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 28: Section 7 - Using With/Without Nouns
    cells.append(
        create_cell(
            "markdown",
            """## 7. Using Demonstratives With and Without Nouns 📝

Demonstratives can be used in two ways: **with a noun** (as adjectives) or **without a noun** (as pronouns).

### A. With a Noun (Determiner/Adjective) 📖

When you use the demonstrative + noun, you're being specific about which thing:

**Structure:** Demonstrative + Noun

**Examples:**
- **This book** is mine. (which book? this one)
- **That car** is expensive. (which car? that one)
- **These students** are smart. (which students? these ones)
- **Those houses** are old. (which houses? those ones)

**More examples:**
- I like **this color**. (specific color)
- **That movie** was boring. (specific movie)
- **These shoes** are comfortable. (specific shoes)
- **Those people** are friendly. (specific people)

### B. Without a Noun (Pronoun) 👉

When the noun is obvious or already mentioned, you can use just the demonstrative:

**Structure:** Demonstrative alone (replaces the noun)

**Examples:**
- **This** is mine. (this thing/this one)
- **That** is expensive. (that thing/that one)
- **These** are smart. (these people/these ones)
- **Those** are old. (those things/those ones)

**More examples:**
- I like **this**. (don't need to repeat the noun)
- **That** was boring. (referring to the movie)
- **These** are comfortable. (referring to the shoes)
- **Those** are friendly. (referring to the people)

### When to Use Each:

#### Use WITH noun when:
1. First mention: "Look at **this book**."
2. Need to be clear: "I want **that red car**, not the blue one."
3. Specifying type: "**These Italian shoes** are expensive."

#### Use WITHOUT noun when:
1. Context is clear: "Which one? **This** or **that**?"
2. Noun just mentioned: "I love these shoes. **These** are perfect!"
3. Pointing/showing: "What is **this**?" (pointing)
4. Making choices: "I'll take **these**." (in a shop)

### Comparison Examples:

| With Noun | Without Noun |
|-----------|--------------|
| This book is good. | This is good. |
| That idea is great. | That is great. |
| These apples are fresh. | These are fresh. |
| Those questions are hard. | Those are hard. |

### Special Uses Without Nouns:

**1. Questions:**
- What is **this**?
- Who are **those**?
- Which do you prefer, **this** or **that**?

**2. Introductions:**
- **This** is my friend Sarah. (person)
- **These** are my parents. (people)

**3. Identifying:**
- **That** is the answer. (solution)
- **Those** are the keys. (objects)

**4. Referring to ideas:**
- **This** is difficult. (situation)
- **That** makes sense. (statement)

### Grammar Note:
When using without a noun:
- THIS/THAT + IS (singular verb)
- THESE/THOSE + ARE (plural verb)

[OK] This is good. / These are good.
[OK] That was fun. / Those were fun.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 29-31: Audio examples with/without nouns
    cells.append(
        create_cell(
            "code",
            """# With and without nouns
audio.play_audio("This coffee is delicious. I love this.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those shoes are beautiful. I want those.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("What is this? This is a new phone.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 32: Section 8 - Questions with Demonstratives
    cells.append(
        create_cell(
            "markdown",
            """## 8. Questions with Demonstratives ❓

Demonstratives are very useful for asking questions, especially when pointing to things or identifying objects.

### Types of Questions:

#### 1. Identifying Questions (What is...?) 🔍

**Asking about singular things (THIS/THAT):**
- What is **this**?
- What is **that**?
- What is **this thing** here?
- What is **that building** over there?

**Asking about plural things (THESE/THOSE):**
- What are **these**?
- What are **those**?
- What are **these objects**?
- What are **those flowers**?

**Answers:**
- This is a pen.
- That is a museum.
- These are my keys.
- Those are roses.

#### 2. Ownership Questions (Whose...?) 👤

**Structure:** Whose + is/are + demonstrative?

**Examples:**
- Whose is **this**? (Whose book is this?)
- Whose are **these**? (Whose shoes are these?)
- Whose is **that** car?
- Whose are **those** bags?

**Answers:**
- This is mine.
- These are John's.
- That is my mother's car.
- Those are the teacher's bags.

#### 3. Choice Questions (Which...?) 🎯

**Structure:** Which + noun + question / Which one(s)?

**Examples:**
- Which one do you want, **this** or **that**?
- Which books, **these** or **those**?
- Which do you prefer, **this one** or **that one**?
- Which color, **this** or **that**?

**Answers:**
- I want this one.
- I prefer those.
- This color is better.
- I'll take that.

#### 4. Opinion Questions 💭

**Asking about opinions using demonstratives:**
- Is **this** good?
- Are **these** correct?
- Was **that** interesting?
- Were **those** useful?

**With question words:**
- How is **this**?
- Why is **that**?
- How are **these**?
- Why are **those** important?

#### 5. Yes/No Questions [OK]❌

**Structure:** Is/Are/Was/Were + demonstrative + ...?

**Examples:**
- Is **this** your book?
- Are **these** your keys?
- Was **that** your car?
- Were **those** your friends?

**Answers:**
- Yes, this is. / No, this isn't.
- Yes, these are. / No, these aren't.
- Yes, that was. / No, that wasn't.
- Yes, those were. / No, those weren't.

### Common Question Patterns:

| Question Pattern | Example | Answer |
|-----------------|---------|--------|
| What is this/that? | What is this? | This is a phone. |
| What are these/those? | What are these? | These are photos. |
| Whose is this/that? | Whose is this? | This is mine. |
| Whose are these/those? | Whose are these? | These are Tom's. |
| Which one? | Which one do you want? | I want this one. |
| Is this...? | Is this your bag? | Yes, it is. |
| Are these...? | Are these your books? | No, they aren't. |
| How is this/that? | How is this coffee? | This is delicious. |

### Question Word Order:

**Identifying:**
```
What + is/are + THIS/THAT/THESE/THOSE?
```

**Choice:**
```
Which (one/ones) ... THIS/THAT or THESE/THOSE?
```

**Yes/No:**
```
Is/Are + THIS/THAT/THESE/THOSE + ...?
```

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 33-36: Audio examples for questions
    cells.append(
        create_cell(
            "code",
            """# Questions with demonstratives
audio.play_audio("What is this? This is my new phone.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Whose are these keys? These are mine.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Which do you prefer, this one or that one?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Are those your books? Yes, those are mine.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 37: Section 9 - Time References
    cells.append(
        create_cell(
            "markdown",
            """## 9. Time References (This week, That day) 🗓️

Demonstratives are commonly used with time expressions to show when something happens or happened.

### THIS + Time (Present/Current Time) 🕐

**THIS** indicates the current time period or a time period close to now:

**Common time expressions with THIS:**

- **This morning** = today's morning
  - I woke up early **this morning**.

- **This afternoon** = today's afternoon
  - I have a meeting **this afternoon**.

- **This evening** = tonight/today's evening
  - We're going out **this evening**.

- **This week** = the current week
  - I'm very busy **this week**.

- **This month** = the current month
  - **This month** has been productive.

- **This year** = the current year
  - **This year** I want to learn Spanish.

- **This weekend** = the coming weekend
  - What are you doing **this weekend**?

- **This time** = right now
  - **This time** I will succeed.

**Special cases:**
- **These days** = currently, nowadays
  - **These days** people use smartphones a lot.
  - **These days** I'm feeling happy.

### THAT + Time (Past Time) 🕰️

**THAT** indicates a specific time in the past:

**Common time expressions with THAT:**

- **That morning** = a specific morning in the past
  - **That morning** was beautiful.

- **That afternoon** = a specific afternoon in the past
  - I remember **that afternoon** well.

- **That evening** = a specific evening in the past
  - **That evening** we had a party.

- **That day** = a specific day in the past
  - **That day** changed my life.

- **That week** = a specific week in the past
  - **That week** was very difficult.

- **That month** = a specific month in the past
  - **That month** we traveled to Paris.

- **That year** = a specific year in the past
  - **That year** was 2020.

- **That time** = a specific moment in the past
  - I remember **that time** when we met.

**Special cases:**
- **Those days** = a period in the past
  - **Those days** were wonderful.
  - I miss **those days**.

- **Those times** = a period in the past
  - **Those times** were difficult.

### Comparison Table:

| Current (THIS/THESE) | Past (THAT/THOSE) |
|---------------------|-------------------|
| This morning (today) | That morning (a past day) |
| This week (current week) | That week (a past week) |
| This year (current year) | That year (a past year) |
| This time (now) | That time (a past moment) |
| These days (currently) | Those days (past period) |

### Usage Examples in Context:

**THIS (Current):**
- **This morning** I had coffee with Sarah.
- I'm traveling to London **this weekend**.
- **This year** has been amazing so far.
- **These days** I wake up early.

**THAT (Past):**
- **That morning** I met my future wife.
- I remember **that weekend** in the mountains.
- **That year** I graduated from university.
- **Those days** we were so young.

### Special Notes:

1. **TODAY vs THIS (morning/afternoon/evening):**
   - TODAY = the whole day
   - THIS morning/afternoon/evening = specific part of today

2. **TONIGHT = THIS EVENING:**
   - Let's go to the cinema **tonight**.
   - Let's go to the cinema **this evening**.
   (Both are correct and mean the same thing)

3. **Future with THIS:**
   - THIS can also refer to near future:
   - I'm starting a new job **this Monday**. (the coming Monday)
   - We're having a party **this Saturday**.

### Common Mistakes:

❌ I saw him **this morning** (when talking about yesterday)
[OK] I saw him yesterday morning / **that morning**

❌ I'm busy **that week** (when talking about current week)
[OK] I'm busy **this week**

❌ **This days** I'm happy
[OK] **These days** I'm happy

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 38-41: Audio examples for time references
    cells.append(
        create_cell(
            "code",
            """# Time references - THIS
audio.play_audio("I'm very busy this week.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("This morning I went to the gym.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Time references - THAT
audio.play_audio("That day was the best day of my life.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Those were happy times.", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 42: Section 10 - Phone Conversation Uses
    cells.append(
        create_cell(
            "markdown",
            """## 10. Phone Conversation Uses ("This is John calling") 📞

Demonstratives are essential in phone conversations for identifying yourself and asking who you're speaking to.

### Identifying Yourself (THIS) 🗣️

When you answer the phone or introduce yourself on a call, use **THIS**:

**Structure:** This is + (your name)

**Common patterns:**

1. **Simple introduction:**
   - Hello, **this is** John.
   - Hi, **this is** Sarah speaking.
   - **This is** Tom calling.

2. **Formal business calls:**
   - Good morning, **this is** David Miller from ABC Company.
   - **This is** Dr. Smith's office.
   - **This is** the City Library.

3. **When calling:**
   - Hello, **this is** Maria. Can I speak to John?
   - Hi, **this is** Sarah calling. Is Tom available?

4. **Answering questions:**
   - A: "Is this John?"
   - B: "Yes, **this is** John." OR "Yes, **this is** he."

### Why THIS (not I)?

In phone conversations, we use THIS instead of I to refer to ourselves because:
- You can't see each other
- THIS identifies you through the phone
- It's a telephone convention in English

### Asking Who Is Calling (THAT) 📱

To ask who you're speaking to, you can use **THIS** or **THAT**:

**Common questions:**

1. **Formal questions:**
   - Who is **this**? (Who am I speaking to?)
   - May I ask who **this** is?
   - Could you tell me who is calling?

2. **Informal questions:**
   - Is **this** John?
   - Is **that** you, Sarah?
   - Who's **that**?

3. **Checking identity:**
   - A: "Is **this** Mary?"
   - B: "Yes, **this is** Mary."

### Complete Phone Conversation Examples:

**Example 1: Calling a Friend**
- A: "Hello?"
- B: "Hi, **this is** Tom. Is Sarah there?"
- A: "Yes, **this is** Sarah speaking!"
- B: "Oh, hi Sarah! I didn't recognize your voice."

**Example 2: Formal Business Call**
- A: "Good morning, ABC Company."
- B: "Good morning, **this is** John Smith calling. May I speak to Mr. Johnson?"
- A: "May I ask who **this** is?"
- B: "**This is** John Smith from XYZ Corporation."

**Example 3: Receiving a Call**
- A: "Hello?"
- B: "Hello, is **this** Maria?"
- A: "Yes, **this is** Maria. Who is **this**?"
- B: "**This is** David from the gym."

**Example 4: Wrong Number**
- A: "Hello?"
- B: "Hi, is **this** Tom?"
- A: "No, **this is** Sarah. I think you have the wrong number."
- B: "Oh, I'm sorry!"

### Common Phone Expressions with THIS/THAT:

| Expression | Example | When to Use |
|------------|---------|-------------|
| This is [name] | This is John. | Identifying yourself |
| This is [name] speaking | This is Sarah speaking. | Answering a call |
| This is [name] calling | This is Tom calling. | Making a call |
| Is this [name]? | Is this Maria? | Asking who answered |
| Who is this? | Who is this? | Asking caller's identity |
| Is that you? | Is that you, John? | Confirming identity |
| This is [place] | This is City Hospital. | Business/organization |

### Important Notes:

1. **Don't say "I am...":**
   - ❌ "Hello, I am John."
   - [OK] "Hello, **this is** John."

2. **For questions, both THIS and THAT are possible:**
   - "Is **this** John?" (more common)
   - "Is **that** John?" (also correct)

3. **Short answers:**
   - "Is this Sarah?" → "Yes, **this is** Sarah." OR "Yes, **this is** she."
   - "Is that Tom?" → "Yes, **this is** Tom." OR "Yes, **this is** he."

4. **Messages:**
   - "Can you tell her **this is** John calling?"
   - "Please let him know **this is** urgent."

### Cultural Note:
In phone conversations, using demonstratives (THIS/THAT) is standard in English. Different languages may use different conventions, so this is an important pattern to learn!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 43-46: Audio examples for phone conversations
    cells.append(
        create_cell(
            "code",
            """# Phone conversation examples
audio.create_conversation_audio([
    ("Person A", "Hello?"),
    ("Person B", "Hi, this is John. Is Sarah there?"),
    ("Person A", "Yes, this is Sarah speaking!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.create_conversation_audio([
    ("Receptionist", "Good morning, ABC Company."),
    ("Caller", "Good morning, this is David Miller. May I speak to Mr. Johnson?")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.create_conversation_audio([
    ("Person A", "Hello?"),
    ("Person B", "Is this Maria?"),
    ("Person A", "Yes, this is Maria. Who is this?"),
    ("Person B", "This is Tom from work.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """audio.play_audio("Hello, this is Dr. Smith's office. How may I help you?", accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 47: Section 11 - Common Mistakes
    cells.append(
        create_cell(
            "markdown",
            """## 11. Common Mistakes to Avoid Warning:

Here are the most common errors learners make with demonstratives:

### Mistake 1: Singular/Plural Confusion

**Wrong number (singular vs plural):**

❌ **This** books are good.
[OK] **These** books are good. (plural noun needs THESE)

❌ **These** book is good.
[OK] **This** book is good. (singular noun needs THIS)

❌ **That** cars are expensive.
[OK] **Those** cars are expensive. (plural noun needs THOSE)

❌ **Those** car is expensive.
[OK] **That** car is expensive. (singular noun needs THAT)

**Rule:** Match the demonstrative with the noun number!
- THIS/THAT → singular nouns
- THESE/THOSE → plural nouns

### Mistake 2: Wrong Verb Agreement

**Using wrong verb with demonstrative pronouns:**

❌ This **are** my book.
[OK] This **is** my book. (THIS = singular → use IS)

❌ These **is** my books.
[OK] These **are** my books. (THESE = plural → use ARE)

❌ That **are** interesting.
[OK] That **is** interesting. (THAT = singular → use IS)

❌ Those **is** expensive.
[OK] Those **are** expensive. (THOSE = plural → use ARE)

**Rule:**
- THIS/THAT → IS/WAS (singular verb)
- THESE/THOSE → ARE/WERE (plural verb)

### Mistake 3: Confusing Demonstratives with Articles

**Mixing up demonstratives with A/AN/THE:**

❌ I like **this** books. (trying to say "I like books in general")
[OK] I like **these** books. (specific books near me)
[OK] I like books. (books in general, no demonstrative)

❌ **This** is **a** my book.
[OK] **This** is my book. (no article needed)

❌ **The** this book
[OK] **This** book (don't use article with demonstrative)

**Rule:** Don't use articles (a/an/the) with demonstratives!
- ❌ the this book
- [OK] this book
- [OK] the book

### Mistake 4: Wrong Distance Choice

**Using NEAR when you mean FAR, or vice versa:**

❌ Look at **this** mountain! (pointing to a distant mountain)
[OK] Look at **that** mountain!

❌ I'll take **those**. (pointing to items in your hand)
[OK] I'll take **these**.

❌ **That** morning I woke up early. (talking about today's morning)
[OK] **This** morning I woke up early.

**Rule:** Think about the distance (near vs far) before choosing!

### Mistake 5: Mixing THIS/THAT in Phone Conversations

**Using wrong demonstrative on the phone:**

❌ Hello, **I am** John. (on the phone)
[OK] Hello, **this is** John.

❌ Hello, **that is** Sarah speaking.
[OK] Hello, **this is** Sarah speaking.

**Rule:** Always use THIS (not I, not THAT) to identify yourself on the phone.

### Mistake 6: Using Demonstratives with Possessives

**Trying to use both together:**

❌ **This** my book
[OK] **This** is my book. (add verb IS)
[OK] **This** book is mine. (demonstrative + noun, then possessive)

❌ **These** your keys?
[OK] Are **these** your keys? (add verb ARE)

**Rule:** If using "my/your/his/her", you need a verb or different structure.

### Mistake 7: Forgetting Plural Forms

**Not changing THIS/THAT to plural:**

❌ Look at **this** beautiful flowers!
[OK] Look at **these** beautiful flowers!

❌ I remember **that** happy days.
[OK] I remember **those** happy days.

**Rule:**
- THIS → THESE (for plural)
- THAT → THOSE (for plural)

### Mistake 8: Wrong Time Expression

**Mixing up time demonstratives:**

❌ **This days** I'm busy.
[OK] **These days** I'm busy. (days = plural)

❌ **Those** morning was cold. (talking about this morning)
[OK] **This** morning was cold.

**Rule:** Check if time reference is present (THIS/THESE) or past (THAT/THOSE)

### Mistake 9: Overusing Demonstratives

**Using demonstratives when not needed:**

❌ I wake up every morning at 7. **This** morning I wake up at 7.
[OK] I wake up every morning at 7. I wake up at 7 every morning. (habitual action)

❌ I love books. **These** books are great. (talking about books in general)
[OK] I love books. Books are great. (general statement)

**Rule:** Only use demonstratives when pointing to specific things!

### Quick Reference - Common Errors:

| ❌ Wrong | [OK] Correct | Error Type |
|---------|-----------|------------|
| This books | These books | Singular/Plural |
| These is good | These are good | Verb agreement |
| The this book | This book | Article + demonstrative |
| This mountain (far away) | That mountain | Wrong distance |
| I am John (on phone) | This is John | Phone convention |
| This my book | This is my book | Missing verb |
| This beautiful flowers | These beautiful flowers | Plural form |
| This days | These days | Time expression |

### Practice Tip:
Before using a demonstrative, ask yourself:
1. **How many?** (one → THIS/THAT, many → THESE/THOSE)
2. **How far?** (near → THIS/THESE, far → THAT/THOSE)
3. **What verb?** (singular → IS/WAS, plural → ARE/WERE)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 48: Section 12 - Practice Conversations
    cells.append(
        create_cell(
            "markdown",
            """## 12. Practice Conversations 🗣️

Let's see demonstratives in action through natural conversations!

### Conversation 1: Shopping at a Store 🛍️</cell>""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 1: Shopping
audio.create_conversation_audio([
    ("Customer", "Excuse me, how much is this shirt?"),
    ("Clerk", "This one is thirty dollars."),
    ("Customer", "And what about that one over there?"),
    ("Clerk", "That one is on sale. It's twenty-five dollars."),
    ("Customer", "Great! Can I try these shoes too?"),
    ("Clerk", "Of course! These are very comfortable."),
    ("Customer", "Perfect. I'll take this shirt and these shoes.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell("markdown", """### Conversation 2: At a Museum 🎨""", f"cell-{cell_counter}")
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 2: Museum
audio.create_conversation_audio([
    ("Tour Guide", "This painting here is from 1890."),
    ("Tourist", "It's beautiful! What about those sculptures over there?"),
    ("Tour Guide", "Those are from ancient Greece. They're over 2000 years old."),
    ("Tourist", "Incredible! And what is this?"),
    ("Tour Guide", "This is a special exhibit. These artifacts are very rare."),
    ("Tourist", "This museum is amazing!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown", """### Conversation 3: Looking at Photos 📷""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 3: Photos
audio.create_conversation_audio([
    ("Anna", "Look at these photos from my vacation!"),
    ("Ben", "Wow! Where is this?"),
    ("Anna", "This is Paris. And that building in the back is the Eiffel Tower."),
    ("Ben", "Beautiful! Who are these people?"),
    ("Anna", "These are my friends from university."),
    ("Ben", "And what about that photo? Was that in Paris too?"),
    ("Anna", "No, that was in London. Those were amazing days!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell("markdown", """### Conversation 4: In a Restaurant 🍽️""", f"cell-{cell_counter}")
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 4: Restaurant
audio.create_conversation_audio([
    ("Waiter", "Are you ready to order?"),
    ("Customer", "Yes. What is this dish here?"),
    ("Waiter", "This is our special pasta. It's very popular."),
    ("Customer", "Sounds good. And what are those?"),
    ("Waiter", "Those are our desserts. This chocolate cake is delicious."),
    ("Customer", "Perfect! I'll have this pasta and that chocolate cake."),
    ("Waiter", "Excellent choice!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown", """### Conversation 5: Meeting Someone New 👋""", f"cell-{cell_counter}"
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 5: Introductions
audio.create_conversation_audio([
    ("Maria", "Hi! This is my first day here."),
    ("John", "Welcome! This is a great company. Let me introduce you."),
    ("John", "This is Sarah, she works in marketing."),
    ("Sarah", "Nice to meet you!"),
    ("John", "And those people over there are the design team."),
    ("Maria", "Everyone is so friendly!"),
    ("John", "Yes, these are good times to be here. The company is growing.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell("markdown", """### Conversation 6: Phone Call 📱""", f"cell-{cell_counter}")
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Conversation 6: Phone call
audio.create_conversation_audio([
    ("Person A", "Hello?"),
    ("Person B", "Hi, this is Tom. Is this Maria?"),
    ("Person A", "Yes, this is Maria. Hi Tom!"),
    ("Person B", "I'm calling about this weekend. Are you still free?"),
    ("Person A", "Yes! This weekend works perfectly for me."),
    ("Person B", "Great! That restaurant we talked about - is it still open?"),
    ("Person A", "Yes, I checked this morning. It's open.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 59: Pronunciation guide
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

    # Cell 61: What's Next
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

Now that you understand demonstratives, it's time to practice!

### Continue to:
1. **02_controlled_practice.ipynb** - 70+ exercises on THIS/THAT/THESE/THOSE
2. **03_meaningful_practice.ipynb** - Personal activities using demonstratives
3. **04_communicative_practice.ipynb** - Real conversations with demonstratives

---

## 📌 Key Takeaways

[OK] **THIS** = singular, near (This book)

[OK] **THAT** = singular, far (That car)

[OK] **THESE** = plural, near (These books)

[OK] **THOSE** = plural, far (Those cars)

[OK] Ask: **How many?** (singular/plural) and **How far?** (near/far)

[OK] **Distance** can be physical, temporal, or abstract

[OK] Can use **with nouns** (This book) or **without** (This is good)

[OK] Use in **questions**: What is this? Whose are these?

[OK] **Time**: This week (now), That day (past), These days (current period)

[OK] **Phone**: This is John speaking (identify yourself)

[OK] **Verb agreement**: This/That IS, These/Those ARE

[OK] **No articles**: "This book" (not "the this book")

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
            f"Warning: File size is outside target range. Target: 18-22 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
