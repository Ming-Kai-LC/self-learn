"""
Builder script for Module 14 Phase 4: Like/Love/Hate + -ing - Communicative Practice
Target: 16-20 KB, 20-22 cells, 8 real-world communication tasks
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


def build_phase4_notebook():
    """Build the complete Phase 4 notebook"""
    cells = []
    cell_counter = 0

    # Cell 0: Title and Introduction
    cells.append(
        create_cell(
            "markdown",
            """# Module 14: Like, Love, Hate + -ing - Communicative Practice

## 💬 Phase 4: Communicative Practice (35% of learning time)

Welcome to **Communicative Practice** - the final and most important phase! Here you'll use preference verbs + -ing in **realistic conversations and role-plays**.

### What Makes This Phase Special?
- **Real-world situations**: Practice scenarios you'll actually encounter
- **Interactive dialogues**: Create natural conversations
- **Role-play activities**: Act out realistic situations
- **Authentic communication**: Focus on meaning, not just grammar
- **Practical skills**: Develop fluency and confidence

### What You'll Do:
- [OK] Have a first date conversation about interests
- [OK] Plan activities with friends
- [OK] Get to know a new roommate
- [OK] Discuss work preferences in a job interview
- [OK] Talk about fitness activities at a gym
- [OK] Plan travel activities with a partner
- [OK] Write a social media post about hobbies
- [OK] Have a parent-child conversation about activities

⏱️ **Estimated time:** 90-120 minutes

---

## 💡 Tips for Communicative Practice:
1. **Focus on communication** - Don't worry about small mistakes
2. **Be natural** - Use contractions and casual language
3. **Ask follow-up questions** - Keep the conversation going
4. **Show interest** - React to what others say
5. **Use variety** - Mix different preference verbs
6. **Be creative** - Add your own personality
7. **Practice out loud** - Actually speak the conversations!

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

from feedback_system import CommunicativeTask, DialogueBuilder
from audio_generator import AudioGenerator
from IPython.display import display, HTML

# Initialize systems
task = CommunicativeTask()
dialogue = DialogueBuilder()
audio = AudioGenerator(audio_dir="audio")

print("[OK] Ready for communicative practice!")
print("💡 Remember: Communication is about expressing meaning, not perfection!")
print("🎭 Try to practice these conversations out loud with a partner if possible!")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 1: First Date Conversation
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 1: First Date Conversation 💑

You're on a first date and getting to know each other. Discuss your interests, hobbies, and preferences.

### Situation:
You and your date are at a coffee shop. You want to learn about each other's interests to see if you're compatible.

### Your Role:
Create a conversation where you:
- Ask about hobbies and interests
- Share your own preferences
- Find common interests
- Ask follow-up questions
- React positively to their interests

### Key Language:
- "What do you like doing in your free time?"
- "Do you enjoy...?"
- "I love/like/enjoy + -ing..."
- "That sounds interesting!"
- "Me too! / I don't really..."

### Guidelines:
- Write at least 10 exchanges (10 lines each person)
- Use various preference verbs
- Make it natural and friendly
- Include questions AND answers
- Show interest and enthusiasm

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 1: First date conversation
task.create_dialogue_task(
    "Create a first date conversation at a coffee shop. Discuss hobbies and interests. Minimum 10 exchanges each.",
    roles=["Person A (You)", "Person B (Your Date)"],
    min_exchanges=10
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Example first date conversation (listen first for inspiration)
audio.create_conversation_audio([
    ("Alex", "So, what do you like doing in your free time?"),
    ("Jordan", "I really enjoy reading and going to the gym. How about you?"),
    ("Alex", "That's cool! I love reading too. What kind of books do you like reading?"),
    ("Jordan", "I enjoy reading mystery novels. Do you like mysteries?"),
    ("Alex", "Yes! I love trying to solve them before the end! Do you do any sports?"),
    ("Jordan", "I enjoy playing tennis. Do you like any sports?"),
    ("Alex", "I don't mind watching sports, but I prefer hiking and being in nature."),
    ("Jordan", "Oh, I love hiking too! We should go together sometime!")
], accent="us")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 2: Planning Activities with Friends
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 2: Planning Activities with Friends 👥

You and your friends are planning what to do this weekend. Everyone has different preferences.

### Situation:
It's Friday evening. You're texting/talking with 2-3 friends to decide what to do on Saturday. Everyone likes different things, so you need to find activities everyone enjoys.

### Your Role:
Create a group conversation where you:
- Suggest different activities
- Express what you like/don't like
- Ask others about their preferences
- Find a compromise
- Make final plans

### Key Language:
- "What about + -ing...?"
- "I'd love to..."
- "I don't really feel like + -ing..."
- "Would you prefer + -ing or + -ing?"
- "Does everyone enjoy + -ing?"

### Guidelines:
- Write a conversation with 3 people
- Include at least 12-15 total exchanges
- Suggest multiple activities
- Show different preferences
- Reach a decision everyone likes

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 2: Planning with friends
task.create_dialogue_task(
    "Create a group conversation (3 friends) planning weekend activities. Show different preferences and reach agreement.",
    roles=["Friend 1 (You)", "Friend 2", "Friend 3"],
    min_exchanges=12
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 3: New Roommate Getting to Know Each Other
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 3: New Roommate - Getting to Know Each Other 🏠

You just moved in with a new roommate. You're discussing your lifestyles and preferences to avoid conflicts.

### Situation:
First evening with your new roommate. You want to understand each other's habits, preferences, and pet peeves to live together harmoniously.

### Your Role:
Create a conversation where you:
- Ask about daily routines and preferences
- Discuss household chores (who likes/hates what)
- Talk about noise levels and quiet time
- Share cooking and cleaning habits
- Discuss having guests over
- Find compromises

### Key Language:
- "Do you mind + -ing...?"
- "I don't mind + -ing, but I hate + -ing..."
- "I usually enjoy + -ing..."
- "Are you okay with...?"
- "Would you prefer if...?"

### Guidelines:
- Write at least 12 exchanges (12 lines each)
- Cover household topics
- Be honest but polite
- Find common ground
- Show willingness to compromise

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 3: Roommate conversation
task.create_dialogue_task(
    "Create a conversation with a new roommate. Discuss preferences, habits, and household chores. Find compromises.",
    roles=["You", "New Roommate"],
    min_exchanges=12
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 4: Job Interview About Work Preferences
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 4: Job Interview - Work Preferences 💼

You're in a job interview. The interviewer wants to know about your work preferences and style.

### Situation:
Second round interview for a job you really want. The hiring manager is asking about your work preferences to see if you're a good fit for the team and company culture.

### Your Role:
Create an interview conversation where you:
- Answer questions about work preferences honestly
- Show enthusiasm for things you enjoy
- Diplomatically discuss things you don't prefer
- Ask about the company's work environment
- Demonstrate self-awareness
- Show flexibility

### Key Language:
- "I really enjoy + -ing..."
- "I prefer + -ing to + -ing..."
- "I don't mind + -ing..."
- "I find + -ing + adjective..."
- "I'm passionate about + -ing..."

### Topics to Cover:
- Working independently vs. in teams
- Work environment preferences
- Task preferences
- Communication style
- Work-life balance
- Professional development

### Guidelines:
- Write at least 10 exchanges
- Sound professional but authentic
- Show both preferences and flexibility
- Ask intelligent questions back
- End positively

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 4: Job interview
task.create_dialogue_task(
    "Create a job interview conversation about work preferences. Be professional but honest. Show enthusiasm and flexibility.",
    roles=["Interviewer", "You (Candidate)"],
    min_exchanges=10
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 5: Gym/Fitness Class Discussion
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 5: Gym/Fitness Class Discussion 🏋️

You're talking with a personal trainer or fitness instructor about your exercise preferences and goals.

### Situation:
First meeting with a personal trainer at a gym. They want to understand what you enjoy, what you hate, and what you're willing to try to create the perfect fitness plan for you.

### Your Role:
Create a conversation where you:
- Discuss past exercise experience
- Express what you love/hate about exercise
- Talk about fitness goals
- Discuss preferences for different activities
- Show openness to trying new things
- Ask for recommendations

### Key Language:
- "I've never tried + -ing..."
- "I used to enjoy + -ing, but..."
- "I can't stand + -ing..."
- "I'd like to start + -ing..."
- "What do you recommend for someone who enjoys + -ing?"

### Topics to Cover:
- Cardio vs. strength training
- Group classes vs. solo workouts
- Indoor vs. outdoor activities
- Morning vs. evening exercise
- Specific sports or activities

### Guidelines:
- Write at least 10 exchanges
- Be honest about your fitness level
- Show motivation and goals
- Ask questions about options
- Be open to suggestions

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 5: Gym/fitness discussion
task.create_dialogue_task(
    "Create a conversation with a personal trainer. Discuss your fitness preferences, goals, and what you enjoy/hate about exercise.",
    roles=["Personal Trainer", "You (Client)"],
    min_exchanges=10
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 6: Travel Planning Discussion
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 6: Travel Planning - Discussing Activities 🌍

You and a travel companion are planning a trip. You need to discuss what activities to do at your destination.

### Situation:
You're planning a week-long vacation with a friend/partner. You have different interests, so you need to plan activities that you'll both enjoy.

### Your Role:
Create a conversation where you:
- Suggest activities at the destination
- Express travel preferences
- Discuss what you love doing on vacation
- Negotiate activities for each day
- Find balance between relaxation and adventure
- Make compromises

### Key Language:
- "When we're there, I'd love to..."
- "I prefer + -ing on vacation..."
- "We could try + -ing..."
- "I don't mind + -ing one day if we can..."
- "What about spending one day + -ing and another day + -ing?"

### Topics to Cover:
- Sightseeing vs. relaxing
- Adventure activities
- Cultural experiences
- Food and dining
- Shopping
- Beach/nature activities

### Guidelines:
- Write at least 12 exchanges
- Show different preferences
- Be specific about activities
- Reach compromises
- Create a balanced itinerary

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 6: Travel planning
task.create_dialogue_task(
    "Plan a vacation with a travel companion. Discuss activities, show different preferences, and create a balanced itinerary.",
    roles=["You", "Travel Companion"],
    min_exchanges=12
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 7: Social Media Post About Hobbies
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 7: Social Media Post About Your Hobbies 📱

Write an engaging social media post about your hobbies and interests.

### Situation:
You want to share with your friends and followers what you love doing. Write a post that's interesting, personal, and shows your personality.

### Your Task:
Write a social media post where you:
- Introduce your main hobbies
- Explain what you love about them
- Mention what you've been doing lately
- Maybe mention something new you want to try
- Use a friendly, casual tone
- Make it engaging

### Key Language:
- "I absolutely love + -ing..."
- "These days I've been enjoying + -ing..."
- "One thing I can't get enough of is + -ing..."
- "I'm thinking about trying + -ing..."
- "Anyone else love + -ing?"

### Post Structure:
1. Hook/Opening
2. Main hobbies (2-3)
3. What you love about them
4. Current activities
5. Future interests
6. Call to action (question for followers)

### Guidelines:
- Write 8-12 sentences
- Use emojis if you like (optional)
- Sound natural and enthusiastic
- Include variety of preference verbs
- End with a question for engagement

### Example Structure:
"Hey everyone! 👋 I wanted to share what I've been up to lately. I absolutely love [hobby] - there's nothing better than [detail]. I've also been enjoying [hobby] because [reason]. These days, I've been spending most of my free time [activity]. One thing I can't stand is [something you hate], so I try to avoid it! I'm thinking about trying [new hobby] soon. What about you? What do you love doing in your free time? Let me know in the comments! 💬"

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 7: Social media post
task.create_writing_task(
    "Write a social media post (8-12 sentences) about your hobbies and interests. Be engaging and end with a question.",
    min_length=8
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 8: Parent-Child Conversation About Activities
    cells.append(
        create_cell(
            "markdown",
            """---

## Task 8: Parent-Child Conversation About Activities 👨‍👩‍👧‍👦

A parent and teenager/young adult are discussing the child's activities and finding balance.

### Situation:
A parent is concerned that their teenager is spending too much time on certain activities. They want to encourage more balance and maybe try new things.

### Your Role:
Choose to be either the parent OR the teenager/young adult. Create a conversation where you:
- Discuss current activities and time spent
- Express preferences honestly
- Show understanding of the other's perspective
- Suggest compromises
- Talk about trying new activities
- Reach an agreement

### Key Language:
**For Parent:**
- "I notice you really enjoy + -ing..."
- "Would you consider + -ing?"
- "I'd like you to try + -ing..."

**For Teenager:**
- "I love + -ing because..."
- "I don't really enjoy + -ing..."
- "I'd be willing to try + -ing if..."

### Topics to Cover:
- Screen time vs. outdoor activities
- Social activities with friends
- Educational activities
- Physical activities
- Creative hobbies
- Family time

### Guidelines:
- Write at least 12 exchanges
- Show both perspectives
- Be respectful
- Find compromises
- End positively

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Task 8: Parent-child conversation
task.create_dialogue_task(
    "Create a conversation between a parent and teenager about activities and balance. Show both perspectives and reach compromise.",
    roles=["Parent", "Teenager/Young Adult"],
    min_exchanges=12
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Reflection and Self-Assessment
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎯 Reflection and Self-Assessment

Congratulations on completing all communicative tasks! Take a moment to reflect on your progress.

### Self-Assessment Questions:

1. **Fluency**: Can you now talk about preferences without stopping to think about grammar?
2. **Variety**: Did you use different preference verbs (like, love, hate, enjoy, prefer, don't mind)?
3. **Natural Communication**: Do your conversations sound natural and authentic?
4. **Confidence**: How confident do you feel discussing hobbies and preferences in English?
5. **Real-World Application**: Can you imagine using these conversations in real life?

### Think About:
- Which task was most useful for you?
- Which was most challenging?
- Which situation will you most likely encounter?
- How has your confidence improved?
- What will you practice more?

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Final reflection
task.create_writing_task(
    "Write a reflection: How do you feel about using preference verbs now? Which tasks were most useful? What will you practice more?",
    min_length=5
)""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Completion
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎉 Module 14 Complete!

**Congratulations!** You've successfully completed Module 14: Like, Love, Hate + -ing!

### What You've Achieved:
[OK] **Phase 1**: Learned all about preference verbs and -ing forms
[OK] **Phase 2**: Completed 70+ controlled practice exercises
[OK] **Phase 3**: Applied the language to YOUR personal life
[OK] **Phase 4**: Used the language in realistic conversations

### You Can Now:
- ✅ Express preferences using like/love/hate + -ing
- ✅ Use other preference verbs (enjoy, prefer, don't mind)
- ✅ Form -ing verbs correctly with proper spelling
- ✅ Create negative sentences and questions
- ✅ Talk about hobbies and interests naturally
- ✅ Have real conversations about preferences
- ✅ Understand and respond to questions about activities
- ✅ Compare preferences with others
- ✅ Express yourself in various social situations

---

## 📊 Your Module Statistics

### Time Investment:
- Phase 1 (Introduction): ~6-8 hours
- Phase 2 (Controlled Practice): ~90-120 minutes
- Phase 3 (Meaningful Practice): ~60-90 minutes
- Phase 4 (Communicative Practice): ~90-120 minutes
- **Total**: ~10-13 hours of learning

### Practice Completed:
- 70+ controlled exercises
- 10 meaningful activities
- 8 communicative tasks
- Multiple conversations created
- Dozens of sentences written

---

## 🚀 Next Steps

### Keep Practicing:
1. **Daily Use**: Try to use preference verbs when talking about your day
2. **Social Media**: Post about your hobbies using -ing forms
3. **Conversations**: Ask friends "What do you like doing?"
4. **Journaling**: Write about your preferences regularly
5. **Listening**: Notice how native speakers use these verbs

### Move Forward:
Continue to the next module in your English learning journey!

### Review If Needed:
You can always come back to review any phase of this module.

---

## 💡 Final Tips

**Remember:**
1. Preference verbs + -ing is one of the most useful structures in English
2. Use it constantly in daily conversation
3. Don't be afraid to express your true preferences
4. Variety makes you sound more fluent (use different verbs!)
5. Practice makes perfect - keep using it!

---

## 📌 Quick Reference Card

### Structure:
Subject + preference verb + verb-ing + (complement)

### Main Verbs:
- **LOVE** (very positive +++)
- **LIKE** (positive ++)
- **ENJOY** (active pleasure ++)
- **PREFER** (comparison)
- **DON'T MIND** (neutral +/-)
- **DON'T LIKE** (negative --)
- **HATE** (very negative ---)

### Questions:
Do/Does + subject + verb + verb-ing?

### Negatives:
Don't/Doesn't + verb + verb-ing

### Spelling:
- Most: add -ing (reading)
- End in -e: drop e (making)
- CVC 1 syllable: double (running)

---

**Thank you for your dedication to learning!** 🌟

You've done an amazing job! Keep up the great work! 💪

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
    notebook = build_phase4_notebook()

    # Define output path
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "04_communicative_practice.ipynb")

    # Save the notebook
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    # Get file size
    file_size = os.path.getsize(output_file)
    file_size_kb = file_size / 1024

    print(f"[OK] Phase 4 notebook created successfully!")
    print(f"📁 Location: {output_file}")
    print(f"📊 File size: {file_size_kb:.2f} KB")
    print(f"📝 Total cells: {len(notebook['cells'])}")

    # Count tasks
    task_count = sum(
        1
        for cell in notebook["cells"]
        if cell["cell_type"] == "code" and "task.create" in str(cell.get("source", ""))
    )
    print(f"🎯 Total tasks: {task_count}")

    # Check if size is within target range
    if 16 <= file_size_kb <= 20:
        print("[OK] File size is within target range (16-20 KB)")
    else:
        print(
            f"⚠️ File size is outside target range. Target: 16-20 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
