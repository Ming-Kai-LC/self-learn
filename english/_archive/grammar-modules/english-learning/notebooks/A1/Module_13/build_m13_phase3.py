"""
Builder script for Module 13 Phase 3: This, That, These, Those - Meaningful Practice
Target: 16-20 KB, 22-25 cells, 10 personal activities
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


def build_phase3_notebook():
    """Build the complete Phase 3 notebook"""
    cells = []
    cell_counter = 0

    # Cell 0: Title and Introduction
    cells.append(
        create_cell(
            "markdown",
            """# Module 13: This, That, These, Those - Meaningful Practice

## 🎨 Phase 3: Meaningful Practice (25% of learning time)

Welcome to meaningful practice! Now you'll use demonstratives to talk about **your own life** and experiences.

### What Makes This "Meaningful"?
- [OK] You write about **your real objects and experiences**
- [OK] You make **personal choices** about what to describe
- [OK] The language is **true for you**
- [OK] You practice in **authentic contexts**

### What You'll Do:
In this phase, you'll complete **10 personal activities** where you:
- Describe objects around you (near vs far)
- Talk about your workspace
- Practice shopping scenarios
- Describe photos and places
- Discuss time in your life
- Compare near and far items
- Practice phone conversations
- Talk about past vs present situations
- Express your opinions
- Create a personal narrative

⏱️ **Estimated time:** 60-90 minutes

---

## How to Use This Notebook

### 📝 Double-Click to Edit
Each activity has a template. **Double-click the cell** to edit and write your own answers.

### 💡 Tips for Success:
1. **Be honest** - Write about your real life
2. **Use complete sentences** - Practice proper grammar
3. **Check your work** - Make sure you used the right demonstrative
4. **Add details** - The more you write, the more you practice!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 1: Describe Objects Around You
    cells.append(
        create_cell(
            "markdown",
            """## Activity 1: Describe Objects Around You (Near vs Far) 🏠

Look around your current space. Describe objects that are near you (THIS/THESE) and far from you (THAT/THOSE).

### Instructions:
Write 6-8 sentences describing objects in your space. Use demonstratives correctly!

### Example:
- This laptop in front of me is new.
- These books on my desk are about English.
- That window over there is open.
- Those pictures on the wall are from my vacation.

---

### 📝 Your Turn (Double-click to edit):

**Near me (THIS/THESE):**
1. This ____________________________________________
2. This ____________________________________________
3. These ___________________________________________
4. These ___________________________________________

**Far from me (THAT/THOSE):**
5. That ____________________________________________
6. That ____________________________________________
7. Those ___________________________________________
8. Those ___________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 2: Your Workspace Description
    cells.append(
        create_cell(
            "markdown",
            """## Activity 2: Your Workspace Description 💼

Describe your workspace or study area using demonstratives. Talk about objects near you and objects in different parts of the room.

### Instructions:
Write 8-10 sentences about your workspace. Include both near and far objects.

### Questions to help you:
- What's on your desk right now? (THIS/THESE)
- What's in the room but not within reach? (THAT/THOSE)
- What tools or equipment do you use?
- What makes your workspace comfortable or special?

---

### 📝 Your Workspace (Double-click to edit):

This is my workspace. _________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 3: Shopping Scenario
    cells.append(
        create_cell(
            "markdown",
            """## Activity 3: Shopping Scenario (Pointing to Items) 🛍️

Imagine you're shopping for clothes, electronics, or groceries. Practice pointing to items using demonstratives.

### Instructions:
Write a shopping dialogue (8-10 exchanges) where you point to items and ask about them.

### Example:
- Customer: "Excuse me, how much is this shirt?"
- Clerk: "This one is $30."
- Customer: "And what about those shoes over there?"
- Clerk: "Those are on sale for $45."

---

### 📝 Your Shopping Dialogue (Double-click to edit):

**Setting:** I'm shopping for _______________________________

**Customer (You):** Excuse me, ___________________________________

**Clerk:** _______________________________________________________

**Customer (You):** And _________________________________________

**Clerk:** _______________________________________________________

**Customer (You):** Can I see ___________________________________

**Clerk:** _______________________________________________________

**Customer (You):** How much ____________________________________

**Clerk:** _______________________________________________________

**Customer (You):** I'll take ___________________________________

**Clerk:** _______________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 4: Photo Description
    cells.append(
        create_cell(
            "markdown",
            """## Activity 4: Photo Description (This Person, Those Buildings) 📷

Think of a real photo you have (vacation, family, event). Describe it using demonstratives as if you're showing it to someone.

### Instructions:
Write 8-10 sentences describing a photo. Use demonstratives to point to people, places, and objects in the photo.

### Example:
- This is my family at the beach.
- This woman here is my mother.
- That building in the background is our hotel.
- Those people over there are other tourists.

---

### 📝 Your Photo Description (Double-click to edit):

**Photo:** This photo is from ____________________________________

This _____________________________________________________________

That _____________________________________________________________

These ____________________________________________________________

Those ____________________________________________________________

This person _______________________________________________________

That place ________________________________________________________

These people ______________________________________________________

Those things ______________________________________________________

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 5: Time in Your Life
    cells.append(
        create_cell(
            "markdown",
            """## Activity 5: Time in Your Life (This Week's Plans) 🗓️

Write about your current time period (THIS week, THIS month, THESE days) and compare it to a past time (THAT week, THAT month, THOSE days).

### Instructions:
Write 10-12 sentences comparing your current life with a past period.

### Example:
- This week I'm very busy with work.
- These days I wake up at 6 AM.
- That week in July was more relaxing.
- Those days I had more free time.

---

### 📝 Your Time Comparison (Double-click to edit):

**Current Time (THIS/THESE):**

This week ________________________________________________________

This month _______________________________________________________

These days _______________________________________________________

This year ________________________________________________________

This morning _____________________________________________________

**Past Time (THAT/THOSE):**

That week ________________________________________________________

That month _______________________________________________________

Those days _______________________________________________________

That year ________________________________________________________

That time ________________________________________________________

**Reflection:**

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 6: Comparing Near/Far Items
    cells.append(
        create_cell(
            "markdown",
            """## Activity 6: Comparing Near and Far Items ⚖️

Compare items that are near you with items that are far away. Express your preferences and opinions.

### Instructions:
Write 8-10 sentences comparing near and far objects and stating your preferences.

### Example:
- This book in my hand is about grammar. That book on the shelf is about vocabulary.
- I prefer this one because it has more examples.
- These shoes I'm wearing are more comfortable than those shoes in my closet.

---

### 📝 Your Comparisons (Double-click to edit):

**Comparison 1:**
This _________________________ and that _________________________

I prefer _________________________________________________________

**Comparison 2:**
These ________________________ and those ________________________

I think __________________________________________________________

**Comparison 3:**
This _________________________ but that _________________________

___________________________________________________________________

**Comparison 4:**
These ________________________ while those _______________________

___________________________________________________________________

**Overall preference:**

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 7: Phone Conversation Practice
    cells.append(
        create_cell(
            "markdown",
            """## Activity 7: Phone Conversation Practice 📞

Write a realistic phone conversation using demonstratives to identify yourself and discuss topics.

### Instructions:
Create a phone dialogue (10-12 exchanges) about a real situation in your life.

### Example topics:
- Calling a friend about weekend plans
- Calling a family member
- Making a doctor's appointment
- Calling about a job interview

---

### 📝 Your Phone Conversation (Double-click to edit):

**Topic:** _______________________________________________________

**Person A:** Hello?

**Person B (You):** Hi, this is ___________________________________

**Person A:** _____________________________________________________

**Person B (You):** I'm calling about ______________________________

**Person A:** _____________________________________________________

**Person B (You):** This ________________________________________

**Person A:** _____________________________________________________

**Person B (You):** That _________________________________________

**Person A:** _____________________________________________________

**Person B (You):** These ________________________________________

**Person A:** _____________________________________________________

**Person B (You):** _______________________________________________

**Person A:** _____________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 8: Past vs Present Situations
    cells.append(
        create_cell(
            "markdown",
            """## Activity 8: Past vs Present Situations 🔄

Reflect on how your life has changed. Compare a situation from the past (THAT/THOSE) with your current situation (THIS/THESE).

### Instructions:
Write 10-12 sentences comparing your past and present in different areas of life.

### Areas to consider:
- Daily routine
- Job or studies
- Hobbies
- Relationships
- Living situation

---

### 📝 Your Past vs Present (Double-click to edit):

**Daily Routine:**

This morning ______________________________________________________

That morning (in the past) ________________________________________

These days ________________________________________________________

Those days ________________________________________________________

**Work/Studies:**

This year ________________________________________________________

That year ________________________________________________________

**Lifestyle:**

This time in my life ______________________________________________

That time in my life ______________________________________________

These habits ______________________________________________________

Those habits ______________________________________________________

**Reflection on changes:**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 9: Your Opinions
    cells.append(
        create_cell(
            "markdown",
            """## Activity 9: Your Opinions (This Idea, That Suggestion) 💭

Express your opinions about different ideas, suggestions, or situations using demonstratives.

### Instructions:
Write 8-10 sentences giving your opinions on various topics. Use demonstratives to refer to ideas and concepts.

### Example:
- This idea of learning English every day is excellent.
- That suggestion about waking up early makes sense.
- These new methods are very effective.
- Those traditional approaches were less efficient.

---

### 📝 Your Opinions (Double-click to edit):

**About learning:**

This method of ____________________________________________________

That approach of __________________________________________________

**About technology:**

This new technology _______________________________________________

That old system ___________________________________________________

**About lifestyle:**

These modern habits _______________________________________________

Those traditional ways ____________________________________________

**About current events:**

This situation ____________________________________________________

That problem _____________________________________________________

**Your overall view:**

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 10: Personal Narrative
    cells.append(
        create_cell(
            "markdown",
            """## Activity 10: Personal Narrative Using Demonstratives 📖

Write a personal story or narrative using demonstratives throughout. This could be about a memorable day, a special event, or an interesting experience.

### Instructions:
Write a narrative of 12-15 sentences. Use demonstratives naturally to point to people, places, objects, and times in your story.

### Example beginning:
"This morning started like any other morning. I woke up in this small room where I've lived for two years. This bed I'm sleeping in is comfortable, but that day I couldn't wait to get up..."

---

### 📝 Your Personal Narrative (Double-click to edit):

**Title:** ________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Self-Reflection Section
    cells.append(
        create_cell(
            "markdown",
            """---

## 🤔 Self-Reflection

Now that you've completed all activities, reflect on your learning.

### Questions to Consider:

**1. Which demonstrative was easiest for you to use?**
- THIS
- THAT
- THESE
- THOSE

**2. Which activity helped you learn the most? Why?**

**3. Do you find it easier to use demonstratives for:**
- Physical objects (things you can see)
- Time references (this week, that day)
- Abstract ideas (this problem, that solution)

**4. What situations in your daily life could you practice demonstratives?**

**5. What's one thing you learned that surprised you?**

---

### 📝 Your Reflection (Double-click to edit):

**Easiest demonstrative:** ________________________________________

**Most helpful activity:** ________________________________________

Because: __________________________________________________________

**Easier context:** _______________________________________________

**Daily practice opportunities:**

___________________________________________________________________

___________________________________________________________________

**Something that surprised me:**

___________________________________________________________________

___________________________________________________________________

**My confidence level now (1-10):** _______

**What I still need to practice:**

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # What's Next section
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

Congratulations on completing the meaningful practice phase! You've personalized your learning by writing about your own life and experiences.

### [OK] What You've Accomplished:
- Described objects around you using demonstratives
- Talked about your workspace and daily life
- Practiced shopping scenarios
- Described photos and memories
- Discussed time in your life (present vs past)
- Compared items and expressed preferences
- Practiced phone conversations
- Reflected on past vs present situations
- Expressed your opinions
- Created a personal narrative

### 📊 Check Your Work:
Before moving on, review your answers:
- Did you use the correct demonstrative (THIS/THAT/THESE/THOSE)?
- Did you match singular/plural correctly?
- Did you consider near/far distance?
- Did you use correct verb agreement (is/are)?

### Continue to:
**04_communicative_practice.ipynb** - Real-world communicative tasks!

---

**Excellent work!** 🌟 You're making great progress!

The next phase will focus on **real communication** where you'll use demonstratives in interactive dialogues and realistic situations.

---""",
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
    notebook = build_phase3_notebook()

    # Define output path
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "03_meaningful_practice.ipynb")

    # Save the notebook
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    # Get file size
    file_size = os.path.getsize(output_file)
    file_size_kb = file_size / 1024

    print(f"[OK] Phase 3 notebook created successfully!")
    print(f"📁 Location: {output_file}")
    print(f"📊 File size: {file_size_kb:.2f} KB")
    print(f"📝 Total cells: {len(notebook['cells'])}")

    # Check if size is within target range
    if 16 <= file_size_kb <= 20:
        print("[OK] File size is within target range (16-20 KB)")
    else:
        print(
            f"Warning: File size is outside target range. Target: 16-20 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
