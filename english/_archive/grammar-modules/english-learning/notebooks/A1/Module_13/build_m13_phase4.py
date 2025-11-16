"""
Builder script for Module 13 Phase 4: This, That, These, Those - Communicative Practice
Target: 16-20 KB, 20-22 cells, 8 real-world tasks with module completion
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
            """# Module 13: This, That, These, Those - Communicative Practice

## 💬 Phase 4: Communicative Practice (40% of learning time)

Welcome to the final phase! Now you'll use demonstratives in **real communication situations**.

### What is Communicative Practice?
This phase focuses on **realistic dialogues** and **interactive tasks** where you:
- [OK] Have a **real purpose** for communicating
- [OK] Exchange **meaningful information**
- [OK] Make **authentic choices** about what to say
- [OK] Use demonstratives **naturally** in conversation

### What You'll Do:
Complete **8 real-world communicative tasks**:
1. Shopping dialogue (customer and salesperson)
2. Museum tour guide scenario
3. Real estate showing
4. Restaurant ordering
5. Tech store assistance
6. Photo album sharing
7. City tour conversation
8. Office orientation

Each task includes **12-16 exchanges** for rich practice!

⏱️ **Estimated time:** 90-120 minutes

---

## How to Complete These Tasks

### 📝 Instructions:
1. **Read the scenario** - Understand the situation
2. **Choose your role** - Customer, guide, visitor, etc.
3. **Complete the dialogue** - Fill in realistic responses
4. **Use demonstratives naturally** - THIS, THAT, THESE, THOSE
5. **Make it real** - Write what you would actually say

### 💡 Tips:
- Imagine you're really in this situation
- Use demonstratives to point to specific things
- Add personal details to make it authentic
- Read your dialogue aloud to check if it sounds natural

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 1: Shopping Dialogue
    cells.append(
        create_cell(
            "markdown",
            """## Task 1: Shopping Dialogue (Customer Pointing to Items) 🛍️

**Scenario:** You're shopping for clothes at a boutique. You see items you like and need to ask about them. The salesperson helps you by describing items and answering questions.

**Your Goal:** Point to different items using demonstratives and make a purchase decision.

### Instructions:
Complete the dialogue (12-16 exchanges). Use demonstratives to point to items near and far.

---

### 📝 Your Dialogue (Double-click to edit):

**Salesperson:** Good afternoon! Welcome to our store. How can I help you today?

**You:** Hi! I'm looking for ___________________________________________

**Salesperson:** Great! We have many options. Are you interested in anything specific?

**You:** Yes, I like this _________________________________________

**Salesperson:** Excellent choice! That's one of our best sellers. Would you like to try it on?

**You:** How much is _____________________________________________

**Salesperson:** This one is $___________. And that one over there is $_________.

**You:** What about those _________________________________________

**Salesperson:** Those are on sale today. They're 30% off.

**You:** Can I see ______________________________________________

**Salesperson:** Of course! Here you go. This comes in several colors.

**You:** Do these ________________________________________________

**Salesperson:** Yes, these come in small, medium, and large. What size do you need?

**You:** I need __________________________________________________

**Salesperson:** Perfect! That size is available. Would you like to try these on?

**You:** Yes, please. And can I also see _________________________

**Salesperson:** Sure! That's in the next section. Follow me, please.

**You:** Thank you. I think I'll take ____________________________

**Salesperson:** Wonderful! Is there anything else you'd like?

**You:** No, that's all. These _____________________________________

**Salesperson:** Great! Let me ring these up for you. That will be $_______ total.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 2: Museum Tour Guide
    cells.append(
        create_cell(
            "markdown",
            """## Task 2: Museum Tour Guide Scenario 🎨

**Scenario:** You're a tour guide at an art museum. You're showing a group of tourists around and explaining the exhibits. You need to point to different artworks and artifacts.

**Your Goal:** Guide the tourists through the museum using demonstratives to indicate different pieces.

### Instructions:
Complete the tour guide dialogue (14-16 exchanges). Point to near and far exhibits.

---

### 📝 Your Tour Guide Script (Double-click to edit):

**You (Guide):** Welcome everyone to the National Art Museum! This _______

**Tourist 1:** Excuse me, what is that painting over there?

**You:** That's ____________________________________________________

**Tourist 2:** It's beautiful! How old is it?

**You:** This painting dates back to ________________________________

**Tourist 1:** And what about these sculptures here?

**You:** These are ________________________________________________

**Tourist 3:** Who created those statues in the corner?

**You:** Those statues were created by _____________________________

**Tourist 2:** Can we take photos of this?

**You:** Yes, you can photograph this section, but that area _______

**Tourist 1:** What's in that room over there?

**You:** That room contains _______________________________________

**Tourist 3:** Are these artifacts original?

**You:** Yes, these are __________________________________________

**Tourist 2:** This is fascinating! What period is this from?

**You:** This piece is from ______________________________________

**Tourist 1:** And those paintings on that wall?

**You:** Those are _______________________________________________

**Tourist 3:** Can you tell us more about this technique?

**You:** Of course! This technique ________________________________

**Tourist 2:** Where can we see more like those?

**You:** You can see more in _____________________________________

**Tourist 1:** Thank you! This has been a wonderful tour.

**You:** You're welcome! Before we finish, let me show you _________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 3: Real Estate Showing
    cells.append(
        create_cell(
            "markdown",
            """## Task 3: Real Estate Showing 🏠

**Scenario:** You're a real estate agent showing a house to potential buyers. You need to point out features of the house, both nearby and in other parts of the property.

**Your Goal:** Show the house using demonstratives to highlight different features and spaces.

### Instructions:
Complete the house showing dialogue (14-16 exchanges). Use demonstratives to point to features.

---

### 📝 Your Real Estate Dialogue (Double-click to edit):

**You (Agent):** Welcome! Thank you for coming to see this beautiful property.

**Buyer 1:** Thank you for showing us around. This house looks great from outside!

**You:** Yes, this _________________________________________________

**Buyer 2:** How many bedrooms does it have?

**You:** This house has __________ bedrooms. This room right here is _

**Buyer 1:** What about that room down the hall?

**You:** That's ____________________________________________________

**Buyer 2:** These windows are very large. Do they face south?

**You:** Yes, these windows _______________________________________

**Buyer 1:** And what about those windows upstairs?

**You:** Those windows ____________________________________________

**Buyer 2:** This kitchen is beautiful! Is this appliance new?

**You:** Yes, this _________________________________________________

**Buyer 1:** What about those cabinets? Are they included?

**You:** Yes, those _______________________________________________

**Buyer 2:** Can we see that backyard you mentioned?

**You:** Of course! This door leads to the backyard. _______________

**Buyer 1:** That garden looks well-maintained. Who takes care of it?

**You:** That garden ______________________________________________

**Buyer 2:** These floors are beautiful. What material is this?

**You:** These floors are _________________________________________

**Buyer 1:** And what about that garage? How many cars fit?

**You:** That garage ______________________________________________

**Buyer 2:** This is exactly what we're looking for! What's the price?

**You:** This property is listed at ______________________________

**Buyer 1:** And are those solar panels on the roof included?

**You:** Yes, those _______________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 4: Restaurant Ordering
    cells.append(
        create_cell(
            "markdown",
            """## Task 4: Restaurant Ordering 🍽️

**Scenario:** You're at a restaurant looking at the menu and asking the waiter about different dishes. Some dishes are shown in pictures, others are being served to nearby tables.

**Your Goal:** Ask about dishes using demonstratives and order your meal.

### Instructions:
Complete the restaurant dialogue (12-14 exchanges). Point to menu items and dishes you see.

---

### 📝 Your Restaurant Dialogue (Double-click to edit):

**Waiter:** Good evening! Have you decided what you'd like to order?

**You:** Not yet. Can you tell me what this ______________________

**Waiter:** That's our signature pasta dish. It's very popular.

**You:** It looks delicious! And what about that ___________________

**Waiter:** That's our grilled fish special. It comes with vegetables.

**You:** What are these items here on the menu? ___________________

**Waiter:** These are our appetizers. These small plates are perfect for sharing.

**You:** And what are those people at that table eating? ___________

**Waiter:** Those are our specialty pizzas. They're made in a wood-fired oven.

**You:** That looks amazing! What's in this dish? __________________

**Waiter:** This one has chicken, mushrooms, and cream sauce.

**You:** How big are these portions? ______________________________

**Waiter:** These portions are quite generous. Most people find them very filling.

**You:** Perfect! I'll have _______________________________________

**Waiter:** Excellent choice! And would you like this with soup or salad?

**You:** I'll take ________________________________________________

**Waiter:** Great! And what about drinks? What would you like?

**You:** What's this drink that ___________________________________

**Waiter:** That's our house specialty lemonade. It's freshly made.

**You:** That sounds good! I'll have _____________________________

**Waiter:** Perfect! So that's ______________ with _______________ and _______________. Is that correct?

**You:** Yes, that's right. How long will this take? _____________

**Waiter:** About 15-20 minutes. I'll bring that right out.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 5: Tech Store Assistance
    cells.append(
        create_cell(
            "markdown",
            """## Task 5: Tech Store Assistance 💻

**Scenario:** You're working at a technology store helping a customer choose between different products. The customer is looking at phones, laptops, and accessories.

**Your Goal:** Help the customer by explaining products using demonstratives to point to different items.

### Instructions:
Complete the tech store dialogue (14-16 exchanges). Use demonstratives to discuss different products.

---

### 📝 Your Tech Store Dialogue (Double-click to edit):

**Customer:** Hi, I'm looking for a new laptop. Can you help me?

**You (Sales Associate):** Of course! This ________________________

**Customer:** What about that laptop on display over there?

**You:** That one ________________________________________________

**Customer:** And what's the difference between this model and that one?

**You:** Well, this model _________________________________________

**Customer:** What about these specifications here?

**You:** These specs ______________________________________________

**Customer:** And those laptops on that shelf? Are they good?

**You:** Yes, those _______________________________________________

**Customer:** This price seems reasonable. What's included with this?

**You:** This comes with __________________________________________

**Customer:** What about that warranty you mentioned?

**You:** That warranty ____________________________________________

**Customer:** Can I see these accessories you have?

**You:** Certainly! These are ______________________________________

**Customer:** Do those work with this laptop?

**You:** Yes, those _______________________________________________

**Customer:** This is a tough decision. What would you recommend?

**You:** Based on your needs, I'd recommend _______________________

**Customer:** And what about that extended warranty option?

**You:** That extended warranty ___________________________________

**Customer:** These features are exactly what I need. How's the battery life on this?

**You:** This model's battery ______________________________________

**Customer:** Perfect! I'll take this one. Do these all come in the box?

**You:** Yes, these _______________________________________________

**Customer:** Great! And can I add that carrying case?

**You:** Absolutely! That case ____________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 6: Photo Album Sharing
    cells.append(
        create_cell(
            "markdown",
            """## Task 6: Photo Album Sharing 📷

**Scenario:** You're showing your photo album to a friend, explaining who people are, where photos were taken, and telling stories about different moments.

**Your Goal:** Share your photos using demonstratives to point to people, places, and moments.

### Instructions:
Complete the photo sharing dialogue (12-14 exchanges). Use demonstratives naturally.

---

### 📝 Your Photo Sharing Dialogue (Double-click to edit):

**Friend:** I'd love to see your vacation photos!

**You:** Great! Let me show you. This _____________________________

**Friend:** Wow, beautiful! Where is this?

**You:** This is ________________________________________________

**Friend:** And who are these people with you?

**You:** These are ______________________________________________

**Friend:** What about that building in the background?

**You:** That's __________________________________________________

**Friend:** This looks like an amazing place! When was this taken?

**You:** This was taken __________________________________________

**Friend:** And what about those mountains we can see?

**You:** Those mountains __________________________________________

**Friend:** This photo is stunning! What were you doing here?

**You:** In this photo, I was ____________________________________

**Friend:** Who's that person over there?

**You:** That's __________________________________________________

**Friend:** These photos are wonderful! What about this one?

**You:** Oh, this is ______________________________________________

**Friend:** And what are those things in this picture?

**You:** Those are _______________________________________________

**Friend:** This must have been an incredible trip! Which was your favorite part?

**You:** My favorite was __________________________________________

**Friend:** I can see why! And what about that day when you...?

**You:** Oh yes! That day was ____________________________________

**Friend:** Thanks for sharing these with me! This has been great.

**You:** You're welcome! These memories ___________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 7: City Tour Conversation
    cells.append(
        create_cell(
            "markdown",
            """## Task 7: City Tour Conversation 🏙️

**Scenario:** You're giving a walking tour of your city to visitors. You're pointing out landmarks, explaining history, and answering questions about different places.

**Your Goal:** Guide visitors through the city using demonstratives to indicate landmarks and locations.

### Instructions:
Complete the city tour dialogue (14-16 exchanges). Point to various city features.

---

### 📝 Your City Tour Dialogue (Double-click to edit):

**Visitor 1:** Thank you for showing us around your city!

**You (Tour Guide):** My pleasure! This _________________________

**Visitor 2:** What's that tall building we can see from here?

**You:** That building ___________________________________________

**Visitor 1:** And what about these old buildings around us?

**You:** These buildings _________________________________________

**Visitor 2:** That's fascinating! When were they built?

**You:** These were built ________________________________________

**Visitor 1:** What's that monument over there?

**You:** That monument __________________________________________

**Visitor 2:** Can we visit this church we're standing in front of?

**You:** Yes, this church _______________________________________

**Visitor 1:** What about those bridges we crossed earlier?

**You:** Those bridges __________________________________________

**Visitor 2:** This square is beautiful! What happens here?

**You:** This square ____________________________________________

**Visitor 1:** And what's that market in the distance?

**You:** That's ________________________________________________

**Visitor 2:** These streets are so charming! How old is this neighborhood?

**You:** This neighborhood _______________________________________

**Visitor 1:** What about those modern buildings on that side?

**You:** Those are ______________________________________________

**Visitor 2:** Can you tell us about this statue?

**You:** This statue ____________________________________________

**Visitor 1:** And what's happening at that plaza over there?

**You:** That plaza _____________________________________________

**Visitor 2:** This has been wonderful! What's your favorite place in the city?

**You:** My favorite place is ____________________________________

**Visitor 1:** We'd love to visit that! How do we get there?

**You:** From here, ______________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Task 8: Office Orientation
    cells.append(
        create_cell(
            "markdown",
            """## Task 8: Office Orientation 🏢

**Scenario:** It's your first day at a new job. A colleague is showing you around the office, introducing you to people, and explaining where everything is.

**Your Goal:** Learn about the office using demonstratives to ask about and identify different areas and people.

### Instructions:
Complete the office orientation dialogue (14-16 exchanges). Use demonstratives to ask and learn.

---

### 📝 Your Office Orientation Dialogue (Double-click to edit):

**Colleague:** Welcome to the team! Let me show you around.

**You:** Thank you! I appreciate this. What's this _______________

**Colleague:** This is the main workspace. This is where our team sits.

**You:** Great! And who are these people over here? _______________

**Colleague:** These are your teammates. Let me introduce you.

**You:** Nice to meet everyone! What about that ___________________

**Colleague:** That's the conference room. We have meetings there every Monday.

**You:** And what's this room we're standing near? _________________

**Colleague:** This is the break room. Feel free to use this anytime.

**You:** Perfect! What about those _______________________________

**Colleague:** Those are the manager's offices. That corner office is the CEO's.

**You:** I see. And what's this equipment here? ____________________

**Colleague:** This is the printer and copier. You'll use this often.

**You:** Good to know! Who are those people in that _______________

**Colleague:** Those are the IT team. They're very helpful if you have technical issues.

**You:** That's good to know. What about these ____________________

**Colleague:** These are supply cabinets. You can find pens, paper, everything here.

**You:** Excellent! And that area over there? ______________________

**Colleague:** That's the reception area. That's where visitors check in.

**You:** I see. This desk here, is this _____________________________

**Colleague:** Yes! This is your desk. You'll be sitting here.

**You:** Perfect! And those monitors, are those ____________________

**Colleague:** Yes, those are yours. Everything on this desk is set up for you.

**You:** This is great! One more question - what's that ___________

**Colleague:** That's the emergency exit. Important to know where that is.

**You:** Thank you for showing me around! These ___________________

**Colleague:** You're welcome! If you have any questions, just ask. This team is very supportive.

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Module Completion Assessment
    cells.append(
        create_cell(
            "markdown",
            """---

## 📊 Module Completion Assessment

Congratulations on completing all communicative tasks! Let's assess your mastery of demonstratives.

### Self-Assessment Questions:

**1. Demonstrative Usage:**
- Can you use THIS for singular, near objects? ☐ Yes ☐ Needs practice
- Can you use THAT for singular, far objects? ☐ Yes ☐ Needs practice
- Can you use THESE for plural, near objects? ☐ Yes ☐ Needs practice
- Can you use THOSE for plural, far objects? ☐ Yes ☐ Needs practice

**2. Context Usage:**
- Can you use demonstratives in shopping situations? ☐ Yes ☐ Needs practice
- Can you use demonstratives to describe locations? ☐ Yes ☐ Needs practice
- Can you use demonstratives on the phone? ☐ Yes ☐ Needs practice
- Can you use time references (this week, that day)? ☐ Yes ☐ Needs practice

**3. Grammar Accuracy:**
- Do you use correct verb agreement (this is/these are)? ☐ Yes ☐ Needs practice
- Do you match singular/plural correctly? ☐ Yes ☐ Needs practice
- Do you avoid common mistakes? ☐ Yes ☐ Needs practice

**4. Natural Communication:**
- Can you use demonstratives naturally in conversation? ☐ Yes ☐ Needs practice
- Do you feel confident using them in real situations? ☐ Yes ☐ Needs practice

---

### 📝 Your Reflection (Double-click to edit):

**What I learned in this module:**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Most useful activity:**

___________________________________________________________________

**Most challenging part:**

___________________________________________________________________

**How I'll use demonstratives in real life:**

___________________________________________________________________

___________________________________________________________________

**My confidence level (1-10):** _______

**Additional notes:**

___________________________________________________________________

___________________________________________________________________

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Spaced Repetition Setup
    cells.append(
        create_cell(
            "markdown",
            """## 🔄 Spaced Repetition Setup

To ensure long-term retention, let's set up your spaced repetition schedule for demonstratives.

### Review Schedule:

**Day 1 (Tomorrow):**
- Quick review: Write 5 sentences using THIS, THAT, THESE, THOSE
- Time: 5 minutes

**Day 3:**
- Practice: Describe your room using all demonstratives
- Time: 10 minutes

**Day 7:**
- Exercise: Complete 10 random exercises from Phase 2
- Time: 15 minutes

**Day 14:**
- Application: Use demonstratives in a real conversation
- Time: Natural use

**Day 30:**
- Assessment: Write a dialogue using all demonstratives naturally
- Time: 20 minutes

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    cells.append(
        create_cell(
            "code",
            """# Setup spaced repetition
import sys
sys.path.append('../../../utils')

from spaced_repetition import SpacedRepetitionScheduler, create_review_calendar

# Initialize scheduler
scheduler = SpacedRepetitionScheduler()

# Add review items for demonstratives
review_items = [
    {
        'concept': 'THIS - singular, near',
        'examples': ['This book is mine.', 'This is my house.'],
        'difficulty': 'easy'
    },
    {
        'concept': 'THAT - singular, far',
        'examples': ['That car is red.', 'That was fun.'],
        'difficulty': 'easy'
    },
    {
        'concept': 'THESE - plural, near',
        'examples': ['These books are mine.', 'These are good.'],
        'difficulty': 'medium'
    },
    {
        'concept': 'THOSE - plural, far',
        'examples': ['Those cars are expensive.', 'Those were happy days.'],
        'difficulty': 'medium'
    },
    {
        'concept': 'Time references',
        'examples': ['This week', 'That day', 'These days', 'Those times'],
        'difficulty': 'medium'
    },
    {
        'concept': 'Phone conversations',
        'examples': ['This is John speaking.', 'Is this Maria?'],
        'difficulty': 'hard'
    }
]

# Schedule reviews
for item in review_items:
    scheduler.add_item(
        content=item['concept'],
        examples=item['examples'],
        difficulty=item['difficulty']
    )

# Display review calendar
create_review_calendar(scheduler, weeks=4)

print("[OK] Spaced repetition schedule created!")
print("📅 Check your calendar above for review dates.")""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Completion Certificate
    cells.append(
        create_cell(
            "markdown",
            """---

## 🎓 Module Completion Certificate

### Certificate of Completion

**This certifies that you have successfully completed:**

# Module 13: This, That, These, Those

**Demonstratives Mastery**

---

### [OK] Skills Acquired:

✓ Using THIS for singular, near objects

✓ Using THAT for singular, far objects

✓ Using THESE for plural, near objects

✓ Using THOSE for plural, far objects

✓ Understanding physical, temporal, and abstract distance

✓ Using demonstratives with and without nouns

✓ Asking questions with demonstratives

✓ Using time references correctly

✓ Using demonstratives in phone conversations

✓ Avoiding common mistakes

✓ Natural communication with demonstratives

---

### 📊 Module Statistics:

- **Total Phases Completed:** 4/4
- **Exercises Completed:** 70+
- **Communicative Tasks:** 8/8
- **Personal Activities:** 10/10
- **Time Invested:** ~15-20 hours

---

### 🎯 Next Steps:

Continue to **Module 14** to learn more English grammar!

Practice demonstratives daily in real conversations.

Review this module in 1 week, 2 weeks, and 1 month.

---

**Date Completed:** _______________

**Signature:** _______________

---

**Congratulations!** 🎉🌟

You are now confident in using English demonstratives!

---""",
            f"cell-{cell_counter}",
        )
    )
    cell_counter += 1

    # Final Notes
    cells.append(
        create_cell(
            "markdown",
            """---

## 📚 Final Notes and Resources

### Key Reminders:

**The Four Demonstratives:**
- **THIS** = one thing, near me
- **THAT** = one thing, far from me
- **THESE** = multiple things, near me
- **THOSE** = multiple things, far from me

**Two Questions to Ask:**
1. How many? (singular → THIS/THAT, plural → THESE/THOSE)
2. How far? (near → THIS/THESE, far → THAT/THOSE)

**Verb Agreement:**
- THIS/THAT + IS/WAS (singular)
- THESE/THOSE + ARE/WERE (plural)

**Special Uses:**
- Time: THIS week (now), THAT day (past)
- Phone: THIS is [name] speaking
- Introductions: THIS is my friend

---

### Practice Opportunities:

**Daily Life:**
- Describe objects around you
- Point to things while talking
- Use in phone calls
- Describe photos

**Specific Situations:**
- Shopping
- Giving directions
- Showing people around
- Talking about time

---

### Common Mistakes to Avoid:

❌ This books (wrong number)
[OK] These books

❌ These is good (wrong verb)
[OK] These are good

❌ I am John (on phone)
[OK] This is John

❌ This days (wrong plural)
[OK] These days

---

### Keep Learning!

You've completed Module 13! Continue your English learning journey with confidence.

Remember: The best way to master demonstratives is to **use them every day** in real situations!

---

**Thank you for your dedication to learning English!** 🌟

**See you in the next module!** 🚀

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

    # Check if size is within target range
    if 16 <= file_size_kb <= 20:
        print("[OK] File size is within target range (16-20 KB)")
    else:
        print(
            f"Warning: File size is outside target range. Target: 16-20 KB, Actual: {file_size_kb:.2f} KB"
        )


if __name__ == "__main__":
    main()
