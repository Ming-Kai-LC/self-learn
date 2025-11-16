"""
Builder script for Module 15 Phase 3: Past Simple - Was/Were - Meaningful Practice
Target: 10 personalized activities
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


def build_phase3_notebook():
    """Build the complete Phase 3 notebook with 10 activities"""
    cells = []
    cell_counter = 0

    # Title
    cells.append(
        create_cell(
            "markdown",
            """# Module 15: Past Simple - Was/Were - Meaningful Practice

## 📚 Phase 3: Meaningful Practice (30% of learning time)

**Welcome to Meaningful Practice!** 🎨

In this phase, you'll use WAS and WERE to talk about **YOUR OWN** past experiences. These activities are personal and creative!

### Activities:
1. My Childhood (describing when you were young)
2. Last Weekend (what you did)
3. My Best Friend in the Past
4. A Memorable Day
5. My First School
6. Last Year
7. A Place I Visited
8. How I Was Different
9. My Family in the Past
10. A Special Memory

⏱️ **Estimated time:** 2-3 hours

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

print("✅ Setup complete! Let's practice with YOUR own stories!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 1
    cells.append(
        create_cell(
            "markdown",
            """## Activity 1: My Childhood 👶

**Instructions:** Write 5-7 sentences about when you were a child. Use WAS/WERE.

**Topics to include:**
- How old you were
- Where you were (city, country)
- What you were like (personality, appearance)
- Who was important to you
- What your interests were

**Example:**
> When I was a child, I was very shy. I was 8 years old in 2010. My family and I were in Tokyo. My parents were very kind. I was interested in drawing and music. My best friend was Yuki. We were in the same class.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 2
    cells.append(
        create_cell(
            "markdown",
            """## Activity 2: Last Weekend 📅

**Instructions:** Write 6-8 sentences about last weekend using WAS/WERE.

**Questions to answer:**
- Where were you?
- Who were you with?
- How was the weather?
- Were you busy or relaxed?
- Was it a good weekend? Why/why not?

**Example:**
> Last weekend was great! I was at home on Saturday morning. The weather was sunny and warm. In the afternoon, I was at the park with my friends. We were very happy. On Sunday, I was at my grandmother's house. She was 80 years old last week. It was her birthday party. There were about 20 people at the party.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 3
    cells.append(
        create_cell(
            "markdown",
            """## Activity 3: My Best Friend in the Past 👫

**Instructions:** Write about a best friend from your past (childhood, school, etc.).

**Include:**
- Who they were
- How old you both were
- What they were like
- Where you were together
- Why they were special

**Example:**
> My best friend in elementary school was Maria. We were both 10 years old. She was very funny and kind. We were in the same class for three years. She was good at sports, and I was good at math. We were always together at lunch time. Her family was from Brazil. They were very friendly.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 4
    cells.append(
        create_cell(
            "markdown",
            """## Activity 4: A Memorable Day 🌟

**Instructions:** Describe a special or memorable day from your past.

**Structure:**
- When it was
- Where you were
- Who was there
- What happened (using was/were for states)
- How you felt

**Example:**
> My most memorable day was my graduation day in 2018. It was June 15th. The weather was perfect - sunny but not too hot. The ceremony was at our school. All my classmates were there. My parents and my sister were in the audience. I was very nervous at first, but I was also excited. After the ceremony, there was a party. It was amazing! Everyone was happy and proud.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 5
    cells.append(
        create_cell(
            "markdown",
            """## Activity 5: My First School 🏫

**Instructions:** Write about your first school or your elementary school.

**Include:**
- When you were there
- Where it was
- What it was like
- Who your teachers were
- What subjects you were good/bad at

**Example:**
> My first school was Sunshine Elementary School. I was there from 2005 to 2011. It was in a small town near Tokyo. The school was quite old, but it was nice. There were about 200 students. My first teacher was Mrs. Tanaka. She was very kind and patient. I was good at art and music, but I wasn't good at sports. The playground was big, and there were many trees. My best memories were from that school.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 6
    cells.append(
        create_cell(
            "markdown",
            """## Activity 6: Last Year 📆

**Instructions:** Compare yourself last year to now. Use WAS/WERE.

**Topics:**
- Where you were living
- What your job/studies were
- Who was in your life
- What your interests were
- How you were different

**Example:**
> Last year, I was a university student. I was in my third year. I was living in a dormitory with my roommate. Life was very busy. I was stressed about exams. My schedule was difficult - there were classes every day. I wasn't very healthy because I wasn't sleeping enough. But my friends were great, and we were always together. Now, everything is different!

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 7
    cells.append(
        create_cell(
            "markdown",
            """## Activity 7: A Place I Visited 🗺️

**Instructions:** Write about a place you visited in the past.

**Include:**
- Where it was
- When you were there
- Who you were with
- What it was like
- How the weather was
- What was special about it

**Example:**
> Three years ago, I was in Paris for a week. It was in summer. The weather was hot and sunny. I was there with my family. Paris was beautiful! The buildings were old and elegant. There were tourists everywhere. The Eiffel Tower was amazing - it was bigger than in photos. The food was delicious. People were friendly. It was an unforgettable trip. I was so happy to be there.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 8
    cells.append(
        create_cell(
            "markdown",
            """## Activity 8: How I Was Different ⏪

**Instructions:** Write about how you were different 5 or 10 years ago.

**Compare:**
- Your personality
- Your interests
- Your appearance
- Your habits
- Your goals

**Example:**
> Ten years ago, I was very different. I was 15 years old. I was much shyer than now. I wasn't interested in languages - I was interested in video games. My hair was long, and I was very thin. I wasn't confident. I was afraid to speak in front of people. My dream was to be a game designer. Now, everything is different!

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 9
    cells.append(
        create_cell(
            "markdown",
            """## Activity 9: My Family in the Past 👨‍👩‍👧‍👦

**Instructions:** Write about your family when you were younger.

**Include:**
- Who was in your family
- Where they were
- What they were like
- What their jobs were
- What was special about them

**Example:**
> When I was young, my family was very close. My father was a teacher, and my mother was a nurse. They were both very busy, but they were always there for us. My older brother was in high school. He was good at sports. We were living in a small house near the mountains. There were four of us. My grandparents were living nearby. Sunday lunches were at their house. There was always good food and lots of laughter.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 10
    cells.append(
        create_cell(
            "markdown",
            """## Activity 10: A Special Memory 💭

**Instructions:** Write about a special memory. Use as many WAS/WERE sentences as possible.

**Free writing - Include anything you want!**

**Example:**
> One of my favorite memories was my 10th birthday party. It was in August, so the weather was warm. The party was in our garden. There were about 15 children from my class. My parents were organizing everything. There was a big cake with candles. My grandmother was there too. She was taking photos. All my friends were happy and excited. There were games and music. I was wearing a new dress. It was blue - my favorite color. That day was perfect. Everyone was kind and fun. I was so happy! It was one of the best days of my childhood.

**Your Turn:** ✍️

[Write your sentences here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Reflection
    cells.append(
        create_cell(
            "markdown",
            """## 🎯 Reflection and Self-Assessment

**Instructions:** Think about your practice and answer these questions:

1. Which activity was the easiest for you? Why?

2. Which activity was the most challenging? Why?

3. Did you make any mistakes? What were they?

4. What did you learn about using WAS/WERE?

5. Can you now talk comfortably about the past?

6. What do you want to practice more?

---

**Your Reflection:** ✍️

[Write your thoughts here]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Audio Practice
    cells.append(
        create_cell(
            "markdown",
            """## 🔊 Read Your Sentences Aloud

**Instructions:** Choose 3-5 of your best sentences and practice saying them aloud.

**Tips:**
- Speak clearly
- Pay attention to WAS vs WERE pronunciation
- Use natural intonation
- Practice until you feel confident

**Record yourself if possible and listen back!**

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Final section
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 Excellent Work!

You've completed **10 meaningful practice activities**!

### What You've Accomplished:
✅ Written about your childhood
✅ Described last weekend
✅ Talked about a best friend
✅ Shared a memorable day
✅ Described your first school
✅ Compared last year to now
✅ Written about a place you visited
✅ Reflected on how you've changed
✅ Described your family in the past
✅ Shared a special memory

### Key Achievement:
You've used WAS and WERE to tell **YOUR OWN STORIES** in English! This is real communication!

### Next Steps:
Continue to **04_communicative_practice.ipynb** for interactive conversations and real-life communication tasks!

---

**Amazing job!** 🌟 Your English is growing stronger!""",
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
    notebook = build_phase3_notebook()
    output_path = "03_meaningful_practice.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"Module 15 Phase 3 notebook created successfully!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_kb:.2f} KB")
    print(f"Cells: {len(notebook['cells'])}")
