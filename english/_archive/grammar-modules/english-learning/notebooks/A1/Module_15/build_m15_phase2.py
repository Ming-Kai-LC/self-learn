"""
Builder script for Module 15 Phase 2: Past Simple - Was/Were - Controlled Practice
Target: 70+ exercises covering all aspects of was/were
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


def build_phase2_notebook():
    """Build the complete Phase 2 notebook with 70+ exercises"""
    cells = []
    cell_counter = 0

    # Title
    cells.append(
        create_cell(
            "markdown",
            """# Module 15: Past Simple - Was/Were - Controlled Practice

## 📚 Phase 2: Controlled Practice (30% of learning time)

**Welcome to Controlled Practice!** 💪

In this phase, you'll complete **70+ exercises** to master WAS and WERE. These exercises focus on accuracy and proper form.

### Exercise Categories:
1. Was vs Were (choosing the correct form)
2. Affirmative sentences
3. Negative sentences
4. Questions
5. Short answers
6. Time expressions
7. There was/were
8. Error correction
9. Sentence completion
10. Mixed practice

⏱️ **Estimated time:** 3-4 hours

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

print("✅ Setup complete! Let's practice WAS and WERE!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 1: Was vs Were
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 1: Was vs Were (10 exercises)

**Instructions:** Choose the correct form (was or were).

1. I _____ at home yesterday.
2. They _____ very happy.
3. She _____ my best friend.
4. We _____ at the park.
5. He _____ a good student.
6. You _____ late for class.
7. It _____ a beautiful day.
8. The children _____ in the garden.
9. My sister _____ 10 years old.
10. The books _____ on the table.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Answers 1
    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 1:

1. I **was** at home yesterday.
2. They **were** very happy.
3. She **was** my best friend.
4. We **were** at the park.
5. He **was** a good student.
6. You **were** late for class.
7. It **was** a beautiful day.
8. The children **were** in the garden.
9. My sister **was** 10 years old.
10. The books **were** on the table.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 2: Affirmative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 2: Affirmative Sentences (10 exercises)

**Instructions:** Complete the sentences with was or were.

1. The weather _____ nice yesterday.
2. My parents _____ at work.
3. I _____ tired after the game.
4. The movie _____ very interesting.
5. We _____ students at that school.
6. She _____ a nurse in 2015.
7. The test _____ easy.
8. They _____ my neighbors.
9. He _____ the manager of the store.
10. You _____ right about the answer.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 2:

1. The weather **was** nice yesterday.
2. My parents **were** at work.
3. I **was** tired after the game.
4. The movie **was** very interesting.
5. We **were** students at that school.
6. She **was** a nurse in 2015.
7. The test **was** easy.
8. They **were** my neighbors.
9. He **was** the manager of the store.
10. You **were** right about the answer.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 3: Negative Sentences
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 3: Negative Sentences (10 exercises)

**Instructions:** Make these sentences negative using wasn't or weren't.

1. I was at school. → I _____ at school.
2. They were happy. → They _____ happy.
3. She was my teacher. → She _____ my teacher.
4. We were late. → We _____ late.
5. He was angry. → He _____ angry.
6. You were there. → You _____ there.
7. It was expensive. → It _____ expensive.
8. The doors were open. → The doors _____ open.
9. I was ready. → I _____ ready.
10. The food was good. → The food _____ good.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 3:

1. I **wasn't** at school.
2. They **weren't** happy.
3. She **wasn't** my teacher.
4. We **weren't** late.
5. He **wasn't** angry.
6. You **weren't** there.
7. It **wasn't** expensive.
8. The doors **weren't** open.
9. I **wasn't** ready.
10. The food **wasn't** good.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 4: Questions
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 4: Questions (10 exercises)

**Instructions:** Make questions from these statements.

1. You were at home. → _____ you at home?
2. She was happy. → _____ she happy?
3. They were students. → _____ they students?
4. It was cold. → _____ it cold?
5. We were late. → _____ we late?
6. He was a doctor. → _____ he a doctor?
7. I was right. → _____ I right?
8. The movie was good. → _____ the movie good?
9. You were tired. → _____ you tired?
10. The doors were closed. → _____ the doors closed?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 4:

1. **Were** you at home?
2. **Was** she happy?
3. **Were** they students?
4. **Was** it cold?
5. **Were** we late?
6. **Was** he a doctor?
7. **Was** I right?
8. **Was** the movie good?
9. **Were** you tired?
10. **Were** the doors closed?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 5: Short Answers
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 5: Short Answers (10 exercises)

**Instructions:** Answer with short answers (Yes/No).

1. Were you at home yesterday? (Yes) → _____
2. Was she your teacher? (No) → _____
3. Were they happy? (Yes) → _____
4. Was it expensive? (No) → _____
5. Were we late? (Yes) → _____
6. Was he a student? (No) → _____
7. Was I right? (Yes) → _____
8. Were you tired? (No) → _____
9. Was the food good? (Yes) → _____
10. Were the doors open? (No) → _____

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 5:

1. Yes, I was.
2. No, she wasn't.
3. Yes, they were.
4. No, it wasn't.
5. Yes, you were.
6. No, he wasn't.
7. Yes, you were.
8. No, I wasn't.
9. Yes, it was.
10. No, they weren't.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 6: Time Expressions
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 6: Time Expressions (10 exercises)

**Instructions:** Complete with was/were and the time expression in parentheses.

1. I _____ at the cinema _____. (last night)
2. They _____ in Paris _____. (last summer)
3. She _____ very busy _____. (yesterday)
4. We _____ students _____. (five years ago)
5. He _____ at the office _____. (this morning)
6. The weather _____ terrible _____. (last week)
7. You _____ at the party _____. (on Saturday)
8. It _____ my birthday _____. (yesterday)
9. The shops _____ closed _____. (last Monday)
10. I _____ 10 years old _____. (in 2015)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 6:

1. I **was** at the cinema **last night**.
2. They **were** in Paris **last summer**.
3. She **was** very busy **yesterday**.
4. We **were** students **five years ago**.
5. He **was** at the office **this morning**.
6. The weather **was** terrible **last week**.
7. You **were** at the party **on Saturday**.
8. It **was** my birthday **yesterday**.
9. The shops **were** closed **last Monday**.
10. I **was** 10 years old **in 2015**.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 7: There was/were
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 7: There Was/Were (10 exercises)

**Instructions:** Complete with there was or there were.

1. _____ a book on the table.
2. _____ many people at the party.
3. _____ a problem with my computer.
4. _____ three cats in the garden.
5. _____ a good movie on TV last night.
6. _____ some cookies in the jar.
7. _____ an accident on the highway.
8. _____ two letters for you.
9. _____ a lot of noise last night.
10. _____ several questions on the test.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 7:

1. **There was** a book on the table.
2. **There were** many people at the party.
3. **There was** a problem with my computer.
4. **There were** three cats in the garden.
5. **There was** a good movie on TV last night.
6. **There were** some cookies in the jar.
7. **There was** an accident on the highway.
8. **There were** two letters for you.
9. **There was** a lot of noise last night.
10. **There were** several questions on the test.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 8: Error Correction
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 8: Error Correction (10 exercises)

**Instructions:** Find and correct the error in each sentence.

1. I were at home yesterday.
2. They was very happy.
3. She wasn't to be there.
4. Was they at school?
5. We wasn't ready.
6. There was many people.
7. He were my teacher.
8. You was late.
9. It weren't expensive.
10. Were she your friend?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 8:

1. I **was** at home yesterday. (were → was)
2. They **were** very happy. (was → were)
3. She **wasn't** there. (wasn't to be → wasn't)
4. **Were** they at school? (Was → Were)
5. We **weren't** ready. (wasn't → weren't)
6. There **were** many people. (was → were)
7. He **was** my teacher. (were → was)
8. You **were** late. (was → were)
9. It **wasn't** expensive. (weren't → wasn't)
10. **Was** she your friend? (Were → Was)

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 9: Sentence Completion
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 9: Sentence Completion (10 exercises)

**Instructions:** Complete the sentences with was, were, wasn't, or weren't.

1. The movie _____ boring. I enjoyed it a lot. (negative)
2. We _____ at the beach last weekend. The weather _____ perfect.
3. _____ you at the party? No, I _____.
4. My parents _____ teachers when they _____ young.
5. The test _____ difficult, so everyone _____ happy.
6. _____ she your classmate? Yes, she _____.
7. There _____ any milk in the fridge this morning.
8. I _____ tired yesterday because I _____ at work all day.
9. The doors _____ locked, so we _____ able to enter.
10. _____ the children at school? No, they _____. It _____ Saturday.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 9:

1. The movie **wasn't** boring. I enjoyed it a lot.
2. We **were** at the beach last weekend. The weather **was** perfect.
3. **Were** you at the party? No, I **wasn't**.
4. My parents **were** teachers when they **were** young.
5. The test **wasn't** difficult, so everyone **was** happy.
6. **Was** she your classmate? Yes, she **was**.
7. There **wasn't** any milk in the fridge this morning.
8. I **was** tired yesterday because I **was** at work all day.
9. The doors **were** locked, so we **weren't** able to enter.
10. **Were** the children at school? No, they **weren't**. It **was** Saturday.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Exercise Set 10: Mixed Practice
    cells.append(
        create_cell(
            "markdown",
            """## Exercise Set 10: Mixed Practice - Challenge (10 exercises)

**Instructions:** Translate or create sentences using was/were.

1. I / not / at home / yesterday morning
2. Where / you / last night / ?
3. The weather / beautiful / last weekend
4. there / many people / at the concert / ?
5. My friends / not / happy / with the results
6. she / your teacher / when you / young / ?
7. we / tired / after the long journey
8. there / not / any problems / with the computer
9. How / the movie / ?
10. They / at the beach / but / it / cold

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "markdown",
            """### Answers - Exercise Set 10:

1. I **wasn't at home yesterday morning**.
2. **Where were you last night?**
3. The weather **was beautiful last weekend**.
4. **Were there many people at the concert?**
5. My friends **weren't happy with the results**.
6. **Was she your teacher when you were young?**
7. We **were tired after the long journey**.
8. **There weren't any problems with the computer**.
9. **How was the movie?**
10. They **were at the beach, but it was cold**.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Pronunciation Practice
    cells.append(
        create_cell(
            "markdown",
            """## Pronunciation Practice 🔊

Listen and repeat these sentences:""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Pronunciation practice
sentences = [
    "I was at home yesterday.",
    "They were very happy.",
    "She wasn't at school.",
    "Were you at the party?",
    "There was a problem.",
    "There were many people."
]

for sentence in sentences:
    audio.play_audio(sentence, accent="us")""",
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

You've completed **70+ controlled practice exercises** on WAS and WERE!

### What You've Practiced:
✅ Choosing was vs were
✅ Making affirmative sentences
✅ Making negative sentences (wasn't/weren't)
✅ Forming questions
✅ Giving short answers
✅ Using time expressions
✅ Using there was/were
✅ Correcting errors
✅ Completing sentences
✅ Mixed practice challenges

### Next Steps:
Continue to **03_meaningful_practice.ipynb** to use was/were in more personalized and creative ways!

---

**Great job!** 🌟 You're making excellent progress!""",
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
    notebook = build_phase2_notebook()
    output_path = "02_controlled_practice.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"Module 15 Phase 2 notebook created successfully!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_kb:.2f} KB")
    print(f"Cells: {len(notebook['cells'])}")
