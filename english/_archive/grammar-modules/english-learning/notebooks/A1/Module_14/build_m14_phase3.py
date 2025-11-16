"""
Builder script for Module 14 Phase 3: Like/Love/Hate + -ing - Meaningful Practice
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
            """# Module 14: Like, Love, Hate + -ing - Meaningful Practice

## 🎨 Phase 3: Meaningful Practice (30% of learning time)

Welcome to **Meaningful Practice**! Now you'll use preference verbs + -ing to talk about **YOUR OWN** life, preferences, and experiences.

### What Makes This Different?
- **Personal**: Write about YOUR real preferences
- **Creative**: Express YOUR true feelings
- **Reflective**: Think about what YOU like and don't like
- **Authentic**: Use real examples from YOUR life

### What You'll Do:
- [OK] Describe your hobbies and interests
- [OK] Talk about free time activities you enjoy
- [OK] Explain things you don't like doing
- [OK] Interview someone about their preferences
- [OK] Compare preferences with others
- [OK] Discuss activities in different situations
- [OK] Talk about new activities to try
- [OK] Reflect on changed preferences
- [OK] Express weather and seasonal preferences
- [OK] Describe your ideal weekend

⏱️ **Estimated time:** 60-90 minutes

---

## 💡 Tips for Meaningful Practice:
1. **Be honest** - Write your real preferences!
2. **Be specific** - Add details to make it interesting
3. **Use variety** - Mix different preference verbs
4. **Explain why** - Tell why you like or don't like something
5. **Have fun** - Enjoy expressing yourself!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Cell 1: Setup
    cells.append(
        create_cell(
            "code",
            """# Setup
import sys
sys.path.append('../../../utils')

from feedback_system import PersonalResponseActivity
from IPython.display import display, HTML

# Initialize activity system
activity = PersonalResponseActivity()

print("[OK] Ready for meaningful practice! Share your real preferences and experiences.")
print("💡 Remember: There are no wrong answers - just express yourself honestly!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 1: Your hobbies and interests
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 1: Your Hobbies and Interests 🎨

Write about your hobbies and interests using preference verbs + -ing.

### Instructions:
- Write at least 5 sentences about activities you like/love/enjoy
- Use different preference verbs (like, love, enjoy, prefer)
- Be specific about what you do
- Add details to make it interesting

### Example:
"I love playing the guitar in my free time. I enjoy listening to rock music when I'm driving. I like reading mystery novels before bed. I absolutely love traveling to new countries. I prefer staying home on rainy days."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 1: Write about your hobbies
activity.create_writing_prompt(
    "Write 5-7 sentences about your hobbies and interests. Use: like, love, enjoy, prefer + -ing",
    min_sentences=5
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 2: Free time activities you enjoy
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 2: Free Time Activities You Enjoy 🎮

Describe what you enjoy doing in your free time on different days.

### Instructions:
- Write about activities for: weekdays, weekends, evenings
- Use various preference verbs
- Explain when you do these activities
- Include reasons if you want

### Example:
"On weekday evenings, I enjoy watching TV series after work. On weekends, I love going to the gym and working out. I also like meeting friends for coffee on Saturday mornings. On Sunday afternoons, I prefer reading books or taking naps."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 2: Free time activities
activity.create_writing_prompt(
    "Describe your free time activities for different times (weekdays/weekends/evenings). Use preference verbs + -ing.",
    min_sentences=5
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 3: Things you don't like doing
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 3: Things You Don't Like Doing 😤

Write about activities you don't enjoy, don't like, or hate.

### Instructions:
- Write at least 5 sentences about things you dislike
- Use: don't like, don't enjoy, hate, can't stand
- Explain why if possible
- Be honest about your dislikes

### Example:
"I hate waking up early on Mondays. I don't like cleaning the bathroom - it's my least favorite chore. I can't stand waiting in long lines at the supermarket. I don't enjoy doing paperwork at work. I really don't like sitting in traffic on my way home."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 3: Things you don't like
activity.create_writing_prompt(
    "Write 5-7 sentences about activities you don't like, don't enjoy, or hate. Explain why if you can.",
    min_sentences=5
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 4: Interview someone
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 4: Interview Someone About Preferences 🎤

Interview a friend, family member, or classmate about their preferences.

### Instructions:
- Ask at least 5 questions using "Do you like/love/enjoy + -ing?"
- Write both the questions AND their answers
- Use follow-up questions
- Ask about specific details

### Example Questions:
- Do you like reading books?
- What kind of movies do you enjoy watching?
- Do you love traveling?
- What activities do you hate doing?
- Do you prefer cooking or eating out?

### Format:
Q: [Your question]
A: [Their answer]

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 4: Interview exercise
activity.create_writing_prompt(
    "Interview someone. Write 5 questions and their answers about preferences. Format: Q: [question] A: [answer]",
    min_sentences=10
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 5: Compare preferences
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 5: Compare Your Preferences with a Friend 🤝

Compare what you and a friend/family member like and don't like.

### Instructions:
- Write about things you BOTH like
- Write about things you like but they don't (or vice versa)
- Write about things you BOTH dislike
- Use: both, but, while, whereas

### Example:
"My friend and I both love watching movies, but I prefer action movies while she prefers romantic comedies. We both hate waiting in line. I enjoy cooking, but she doesn't like it at all. She loves dancing, but I'm not really into it. We both enjoy traveling and trying new restaurants."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 5: Compare preferences
activity.create_writing_prompt(
    "Compare your preferences with someone else. Include similarities and differences. Use preference verbs + -ing.",
    min_sentences=6
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 6: Activities in different situations
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 6: Activities in Different Situations 🏠🏢🏖️

Describe what you like doing in different places or situations.

### Instructions:
- Write about preferences for: at home, at work/school, on vacation
- Use various preference verbs
- Be specific about each situation

### Example:
"At home, I love relaxing on the couch and watching Netflix. I enjoy cooking dinner for my family. At work, I like collaborating with my colleagues on projects. I don't enjoy attending long meetings. On vacation, I love exploring new cities and trying local food. I prefer staying at small hotels rather than big resorts."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 6: Different situations
activity.create_writing_prompt(
    "Describe what you like/don't like doing in different situations: at home, at work/school, on vacation.",
    min_sentences=6
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 7: New activities to try
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 7: New Activities You Want to Try 🆕

Write about activities you'd like to try or learn in the future.

### Instructions:
- Use: "I'd like to try...", "I want to start...", "I'm interested in..."
- Write at least 5 activities
- Explain why you want to try them
- Use -ing forms

### Example:
"I'd like to try learning to play the piano. I'm interested in taking up yoga because it looks relaxing. I want to start painting - I think I'd enjoy being creative. I'd love to try rock climbing someday. I'm thinking about learning to speak French."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 7: New activities
activity.create_writing_prompt(
    "Write about 5 new activities you'd like to try. Use: I'd like to try/learn/start + -ing. Explain why.",
    min_sentences=5
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 8: Changed preferences
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 8: Activities You've Changed Your Mind About 🔄

Write about activities you used to like/hate but now feel differently about.

### Instructions:
- Use: "I used to like/love/hate...but now..."
- Write at least 4 examples
- Explain why your feelings changed
- Use past and present preferences

### Example:
"I used to hate exercising, but now I love going to the gym. I used to love playing video games all day, but now I prefer doing more active things. I didn't use to enjoy cooking, but now I really like trying new recipes. I used to love staying up late, but now I prefer going to bed early."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 8: Changed preferences
activity.create_writing_prompt(
    "Write about activities you've changed your mind about. Use: 'I used to...but now...' with preference verbs + -ing.",
    min_sentences=4
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 9: Weather and seasonal preferences
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 9: Weather and Seasonal Preferences 🌦️❄️☀️

Describe what you like doing in different weather or seasons.

### Instructions:
- Write about activities for different weather/seasons
- Include: sunny days, rainy days, summer, winter, etc.
- Use preference verbs + -ing
- Be specific

### Example:
"On sunny days, I love going to the beach and swimming in the ocean. When it's raining, I prefer staying home and reading books. In summer, I enjoy eating ice cream and having barbecues. In winter, I like drinking hot chocolate and watching movies. I hate getting wet in the rain. On cold days, I love staying warm inside."

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 9: Weather and seasons
activity.create_writing_prompt(
    "Describe what you like doing in different weather or seasons. Use preference verbs + -ing for each situation.",
    min_sentences=6
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Activity 10: Your ideal weekend
    cells.append(
        create_cell(
            "markdown",
            """---

## Activity 10: Your Ideal Weekend 🌟

Describe your perfect weekend using preference verbs.

### Instructions:
- Write about your ideal Saturday and Sunday
- Include morning, afternoon, and evening activities
- Use various preference verbs (like, love, enjoy, prefer)
- Be creative and detailed
- Write at least 7 sentences

### Example:
"My ideal weekend starts with sleeping late on Saturday morning - I love not setting an alarm! I enjoy having a relaxed breakfast while reading the newspaper. In the afternoon, I like meeting friends for lunch at a nice restaurant. I love spending time outdoors, so I prefer going for a walk in the park. On Saturday evening, I enjoy watching a good movie at home. On Sunday, I like doing some light exercise, like yoga. I end my perfect weekend by preparing for the week - I don't mind doing this because it makes Monday easier!"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Activity 10: Ideal weekend
activity.create_writing_prompt(
    "Describe your ideal weekend. Include Saturday and Sunday activities. Use multiple preference verbs + -ing.",
    min_sentences=7
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Reflection
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 Reflection on Your Practice

Take a moment to reflect on what you've learned and practiced.

### Think about:
1. **Which activities were easiest for you?**
2. **Which were most challenging?**
3. **Did you discover anything new about your preferences?**
4. **How comfortable are you now using preference verbs + -ing?**
5. **Can you now talk naturally about your hobbies and interests?**

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Reflection activity
activity.create_writing_prompt(
    "Write a short reflection: What did you learn about expressing preferences? What was challenging? How do you feel now?",
    min_sentences=3
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # What's Next
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 What's Next?

Excellent work on meaningful practice! You've personalized your learning by talking about YOUR real preferences.

### Continue to:
**04_communicative_practice.ipynb** - Real-life conversations and role-plays using preference verbs!

---

## 📌 Key Takeaways from Meaningful Practice

[OK] You've practiced talking about **your real hobbies and interests**

[OK] You've expressed **what you like and don't like** honestly

[OK] You've compared **your preferences with others**

[OK] You've reflected on **activities in different situations**

[OK] You've thought about **new things to try**

[OK] You've considered **how your preferences have changed**

[OK] You've described **your ideal activities**

### Remember:
- **Preference verbs + -ing** help you talk about activities naturally
- **Different verbs** express different intensities of feeling
- **Personal examples** make your English more authentic and interesting
- **Being specific** makes your communication clearer

---

**Great job!** 🌟 You're now ready for communicative practice!

Open **04_communicative_practice.ipynb** to continue.""",
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

    # Count activities
    activity_count = sum(
        1
        for cell in notebook["cells"]
        if cell["cell_type"] == "code" and "activity.create" in str(cell.get("source", ""))
    )
    print(f"🎯 Total activities: {activity_count}")

    # Check if size is within target range
    if 16 <= file_size_kb <= 20:
        print("[OK] File size is within target range (16-20 KB)")
    else:
        print(
            f"⚠️ File size is outside target range. Target: 16-20 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
