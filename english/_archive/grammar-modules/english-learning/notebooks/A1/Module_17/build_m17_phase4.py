"""
Builder script for Module 17 Phase 4: Past Simple - Irregular Verbs - Communicative Practice
Target: 8 real-world communication tasks
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


def build_phase4_notebook():
    """Build the complete Phase 4 notebook with 8 tasks"""
    cells = []
    cell_counter = 0

    # Title
    cells.append(
        create_cell(
            "markdown",
            """# Module 17: Past Simple - Irregular Verbs - Communicative Practice

## 📚 Phase 4: Communicative Practice (25% of learning time)

**Welcome to Communicative Practice!** 🗣️

In this final phase, you'll use Past Simple irregular verbs in **real-world communication tasks**. These activities simulate authentic conversations and situations.

### Communication Tasks:
1. Interview About the Past
2. Comparing Then and Now
3. Telling a Story
4. Weekend Report
5. Describing a Past Event
6. Childhood Memories Exchange
7. Travel Stories
8. Problem-Solving: What Happened?

⏱️ **Estimated time:** 2-3 hours

**Note:** These activities work best with a partner, but you can also practice by writing and speaking aloud!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Setup
    cells.append(
        create_cell(
            "code",
            """# Setup
import sys
sys.path.append('../../../utils')

from audio_generator import AudioGenerator
from IPython.display import display, HTML

audio = AudioGenerator(audio_dir="audio")

print("✅ Setup complete! Let's communicate in English!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 1
    cells.append(
        create_cell(
            "markdown",
            """## Task 1: Interview About the Past 🎤

**Scenario:** You're interviewing someone about their childhood and past.

**Your Role:** Interviewer
**Partner's Role:** Interviewee (or answer yourself)

### Questions to Ask:
1. Where were you born?
2. When were you born?
3. What was your hometown like?
4. Who was your best friend when you were young?
5. What were you like as a child?
6. Were you a good student?
7. What was your favorite subject?
8. Were you interested in sports?
9. Who was your favorite teacher?
10. What was your dream when you were young?

### Example Conversation:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example interview
audio.create_conversation_audio([
    ("Interviewer", "Where were you born?"),
    ("Person", "I was born in Tokyo, in 1995."),
    ("Interviewer", "What was your hometown like?"),
    ("Person", "It was very busy and crowded, but I loved it."),
    ("Interviewer", "Were you a good student?"),
    ("Person", "Yes, I was. I was especially good at math."),
    ("Interviewer", "What was your dream?"),
    ("Person", "My dream was to be a teacher.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

**If you have a partner:** Take turns asking and answering these questions.

**If you're alone:** Write your answers to all 10 questions, then practice saying them aloud.

**Your Answers:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 2
    cells.append(
        create_cell(
            "markdown",
            """## Task 2: Comparing Then and Now 🔄

**Scenario:** Talk with someone about how things were different in the past compared to now.

**Topics to compare:**
- Your appearance
- Your personality
- Your interests
- Your daily routine
- Your friends
- Your home
- Your goals

### Useful Phrases:
- "Ten years ago, I was..."
- "Now I'm..."
- "In the past, I wasn't..."
- "But now I am..."
- "Things were different..."
- "Everything was..."

### Example:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example comparison
audio.create_conversation_audio([
    ("Maria", "I was so different five years ago!"),
    ("John", "Really? How?"),
    ("Maria", "I was much shyer. I wasn't confident at all."),
    ("John", "And now?"),
    ("Maria", "Now I'm more outgoing! What about you?"),
    ("John", "Five years ago, I was a student. Life was easier!"),
    ("Maria", "Were you happy?"),
    ("John", "Yes, I was. But I'm happy now too, just in a different way.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Create a dialogue comparing your past and present. Write at least 8-10 exchanges.

**Your Dialogue:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 3
    cells.append(
        create_cell(
            "markdown",
            """## Task 3: Telling a Story 📖

**Scenario:** Tell a story about something that happened in the past. Use WAS/WERE for descriptions and states.

**Story ideas:**
- A funny experience
- An embarrassing moment
- A scary situation
- A surprising event
- A happy memory
- A difficult day

### Story Structure:
1. **Beginning:** Set the scene (when, where, who, weather, feelings)
2. **Middle:** What happened (use irregular verbs for descriptions)
3. **End:** How it ended, how you felt

### Example Story:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example story
story = '''
Last year, I was on vacation in Thailand. It was July, so it was very hot.
One day, I was at the beach. The water was beautiful and clear. There weren't
many people. I was swimming when suddenly, I saw something in the water. It
was huge! I was terrified! I thought it was a shark. I swam back to the
beach as fast as possible. My heart was beating so fast! But when I looked
again, it wasn't a shark. It was just a big piece of wood! I was so
embarrassed, but also relieved. My friends were laughing. It was funny, but
scary at the time!
'''

audio.play_audio(story, accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Write and tell your own story (150-200 words). Use WAS/WERE throughout.

**Your Story:** ✍️

[Write here]

**Practice speaking it aloud!**

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 4
    cells.append(
        create_cell(
            "markdown",
            """## Task 4: Weekend Report 📅

**Scenario:** It's Monday morning. Tell your partner (or write) about your weekend.

**Include:**
- Where you were
- Who you were with
- What you did (use irregular verbs for states)
- How the weather was
- How you felt
- If it was good or bad

### Useful Language:
- "On Saturday morning, I was..."
- "The weather was..."
- "I was with..."
- "There were..."
- "It was..."
- "I was feeling..."

### Example:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example weekend report
audio.create_conversation_audio([
    ("Anna", "How was your weekend, Tom?"),
    ("Tom", "It was great! On Saturday, I was at a concert."),
    ("Anna", "Nice! Who was performing?"),
    ("Tom", "It was a rock band. They were amazing!"),
    ("Anna", "Were there many people?"),
    ("Tom", "Yes, there were hundreds! The atmosphere was incredible."),
    ("Anna", "Lucky you! I was at home all weekend. I was sick."),
    ("Tom", "Oh no! Are you better now?"),
    ("Anna", "Yes, I'm fine now. Thanks!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Write about YOUR last weekend (or imagine one). Write 10-12 sentences using WAS/WERE.

**Your Weekend Report:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 5
    cells.append(
        create_cell(
            "markdown",
            """## Task 5: Describing a Past Event 🎉

**Scenario:** Describe a past event you attended (party, concert, wedding, festival, etc.)

**Describe:**
- When and where it was
- Who was there
- What it was like
- What the atmosphere was like
- How you felt
- If there were any problems
- If it was enjoyable

### Questions to answer:
1. What was the event?
2. When was it?
3. Where was it?
4. Who was there?
5. How many people were there?
6. What was the weather like?
7. Was there food/music/entertainment?
8. How was the atmosphere?
9. Were you happy/excited/nervous?
10. Was it a success?

### Example:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example event description
description = '''
Last month, I was at my cousin's wedding. It was on a Saturday in June.
The ceremony was at a beautiful hotel near the beach. There were about 150
guests. The weather was perfect - sunny and warm. My cousin was beautiful
in her white dress. She was so happy! Her husband was nervous, but excited.
The ceremony was short but emotional. There were flowers everywhere. After
the ceremony, there was a big reception. The food was delicious. There was
live music and dancing. Everyone was having a great time. I was with my
family. We were all very happy for the couple. It was a wonderful day!
'''

audio.play_audio(description, accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Describe a past event you attended. Write 12-15 sentences.

**Your Event Description:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 6
    cells.append(
        create_cell(
            "markdown",
            """## Task 6: Childhood Memories Exchange 👶

**Scenario:** Exchange childhood memories with a partner.

**Take turns asking and answering:**

**Partner A asks:**
1. What was your favorite toy when you were a child?
2. Who was your best friend?
3. What were your favorite activities?
4. Were you afraid of anything?
5. What was your favorite place?

**Partner B asks:**
1. Where were you living when you were 10?
2. What was your school like?
3. Who was your favorite family member?
4. Were you a quiet or noisy child?
5. What was your happiest memory?

### Example Exchange:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example childhood exchange
audio.create_conversation_audio([
    ("Lisa", "What was your favorite toy when you were a child?"),
    ("Mike", "My favorite toy was a red toy car. It was my most precious thing! What about you?"),
    ("Lisa", "Mine was a doll. Her name was Rosie. She was my best friend!"),
    ("Mike", "That's sweet! Who was your best friend in real life?"),
    ("Lisa", "My best friend was my neighbor, Sarah. We were together every day."),
    ("Mike", "Were you two in the same class?"),
    ("Lisa", "No, we weren't. But we were in the same school.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

**If with a partner:** Take turns asking and answering all questions.

**If alone:** Write detailed answers to all 10 questions.

**Your Answers:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 7
    cells.append(
        create_cell(
            "markdown",
            """## Task 7: Travel Stories 🌍

**Scenario:** Share travel experiences from the past.

**Talk about:**
- A place you visited
- When you were there
- Who you were with
- What it was like
- What the weather was like
- If there were any interesting moments
- If you were happy with the trip

### Conversation Starters:
- "Have you ever been to...?"
- "When were you there?"
- "What was it like?"
- "Were you there for long?"
- "Was it expensive?"
- "Were the people friendly?"

### Example Conversation:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example travel conversation
audio.create_conversation_audio([
    ("Sarah", "I was in Italy last summer. Have you ever been there?"),
    ("David", "Yes! I was in Rome five years ago. Where were you?"),
    ("Sarah", "I was in Venice. It was absolutely beautiful!"),
    ("David", "I bet! What was the weather like?"),
    ("Sarah", "It was hot and sunny. Perfect! Were you in Rome the whole time?"),
    ("David", "No, I was also in Florence. It was amazing. The art was incredible."),
    ("Sarah", "Were there many tourists?"),
    ("David", "Yes, there were tourists everywhere! But it was worth it."),
    ("Sarah", "I agree. Italy was wonderful. I want to go back!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Create a conversation about travel (8-12 exchanges). Use WAS/WERE throughout.

**Your Travel Conversation:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 8
    cells.append(
        create_cell(
            "markdown",
            """## Task 8: Problem-Solving: What Happened? 🔍

**Scenario:** Something went wrong! Use WAS/WERE to explain and discuss what happened.

**Situations to discuss:**
1. **Missed Meeting:** "I wasn't at the meeting yesterday because..."
2. **Lost Item:** "My keys weren't in my bag. They were..."
3. **Late Arrival:** "I was late because the traffic was..."
4. **Misunderstanding:** "I thought the party was on Saturday, but it was..."
5. **Cancelled Plans:** "We weren't able to go because..."

### Example Conversations:

**Situation 1: Missed Meeting**""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example problem-solving 1
audio.create_conversation_audio([
    ("Boss", "You weren't at the meeting yesterday. What happened?"),
    ("Employee", "I'm so sorry! I was stuck in traffic. There was an accident."),
    ("Boss", "Was it serious?"),
    ("Employee", "Yes, the highway was closed. I was there for two hours!"),
    ("Boss", "That's unfortunate. Were you able to read the meeting notes?"),
    ("Employee", "Yes, I was. Tom sent them to me.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(create_cell("markdown", """**Situation 2: Lost Item**""", f"cell-{cell_counter}"))
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example problem-solving 2
audio.create_conversation_audio([
    ("Lisa", "I can't find my phone! It wasn't in my bag."),
    ("Tom", "Where were you last?"),
    ("Lisa", "I was at the cafe. Maybe it's there."),
    ("Tom", "Was it on the table?"),
    ("Lisa", "I think so. I was sitting near the window."),
    ("Tom", "Call them. Maybe someone found it."),
    ("Lisa", "Good idea! I hope it's there.")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Your Practice:

Choose 2-3 situations and write conversations (6-8 exchanges each).

**Your Conversations:** ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Final Practice Activity
    cells.append(
        create_cell(
            "markdown",
            """## 🎯 Final Challenge: Extended Conversation

**Scenario:** Have a natural conversation using WAS/WERE. Imagine you're meeting someone after a long time.

**Topics to include:**
- Where you both were all this time
- What you were doing
- How life was
- Changes that happened
- Mutual friends - where they were

**Goal:** Create a natural, flowing conversation of 15-20 exchanges.

### Your Extended Conversation: ✍️

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Self-Assessment
    cells.append(
        create_cell(
            "markdown",
            """## 📊 Self-Assessment

**Rate yourself (1-5):**

1. I can use WAS/WERE correctly in conversations: ___/5

2. I can ask questions about the past: ___/5

3. I can tell stories about past events: ___/5

4. I can describe people and places in the past: ___/5

5. I feel confident using WAS/WERE: ___/5

**What did you learn in this module?**

[Write here]

**What do you still need to practice?**

[Write here]

**How will you use WAS/WERE in real life?**

[Write here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Conclusion
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎉 Congratulations! Module 17 Complete!

You've successfully completed all four phases of **Past Simple - Irregular Verbs**!

### What You've Achieved:

**Phase 1 - Introduction:**
✅ Learned all forms of WAS/WERE
✅ Understood when to use each form
✅ Learned time expressions
✅ Studied there was/there were

**Phase 2 - Controlled Practice:**
✅ Completed 70+ accuracy exercises
✅ Practiced all sentence types
✅ Corrected common errors

**Phase 3 - Meaningful Practice:**
✅ Wrote personal stories
✅ Described your own past
✅ Created meaningful content

**Phase 4 - Communicative Practice:**
✅ Practiced real conversations
✅ Told stories
✅ Exchanged information
✅ Solved problems using English

---

## 🎯 You Can Now:
- Talk about past states and situations
- Describe how things were
- Tell stories about the past
- Ask and answer questions about past events
- Have natural conversations about past experiences

---

## 📚 Next Module: Past Simple - Regular Verbs

In Module 16, you'll learn how to talk about past ACTIONS using regular verbs!

**Example:** I **played** football. She **watched** TV. They **studied** English.

---

## 🌟 Keep Practicing!

Use WAS/WERE every day:
- Talk about your day yesterday
- Describe places you visited
- Share memories with friends
- Write in a journal about the past

**Excellent work!** You're making amazing progress! 🚀""",
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
    notebook = build_phase4_notebook()
    output_path = "04_communicative_practice.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"Module 17 Phase 4 notebook created successfully!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_kb:.2f} KB")
    print(f"Cells: {len(notebook['cells'])}")
