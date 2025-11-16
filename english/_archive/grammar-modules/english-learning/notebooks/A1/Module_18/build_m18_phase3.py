"""
Builder script for Module 18 Phase 3: Going To Future - Meaningful Practice
Target: 10 meaningful activities
"""

import nbformat as nbf


def create_notebook():
    nb = nbf.v4.new_notebook()
    cells = []

    # Title
    cells.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 3: Meaningful Practice

## Overview
This phase contains **10 meaningful activities** where you'll use "going to" in realistic contexts about future plans, intentions, and predictions.

**Activity Types:**
- Personal future plans
- Weekend activities
- Predictions based on evidence
- Travel plans
- Life goals and ambitions
- Weather predictions
- Career plans
- Family activities
- Event planning
- New Year resolutions

**Target Level:** A1 (Elementary)
**Estimated Time:** 60-90 minutes"""
        )
    )

    # Activity 1: My Future Plans
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 1: My Future Plans

Write about your plans for the next year using "going to".

**Instructions:**
1. Think about 8-10 things you're planning to do in the next year
2. Write complete sentences using "going to"
3. Include time expressions (next month, in summer, etc.)
4. Mix different types of plans (study, work, personal, hobbies)

**Example:**
- I'm going to learn Spanish next semester.
- I'm going to join a gym in January.
- I'm going to visit my grandparents in the summer.
- I'm going to save money for a new laptop."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 1: Write your future plans
print("MY FUTURE PLANS")
print("=" * 70)
print()

# Example plans
example_plans = [
    "I'm going to improve my English skills this year.",
    "I'm going to read at least 12 books.",
    "I'm going to exercise three times a week.",
    "I'm going to learn to cook new recipes.",
    "I'm going to travel to a new country next summer.",
    "I'm going to spend more time with my family.",
    "I'm going to start a new hobby in the spring.",
    "I'm going to save money for a vacation.",
    "I'm going to take a photography course.",
    "I'm going to volunteer at a local charity."
]

print("Example plans:\\n")
for i, plan in enumerate(example_plans, 1):
    print(f"{i}. {plan}")

print("\\n" + "=" * 70)
print("NOW IT'S YOUR TURN!")
print("=" * 70)
print("\\nWrite 8-10 of your own future plans using 'going to':")
print("(Use the space below or a separate document)\\n")

# Space for student's own plans
your_plans = [
    "1. I'm going to ______________________",
    "2. I'm going to ______________________",
    "3. I'm going to ______________________",
    "4. I'm going to ______________________",
    "5. I'm going to ______________________",
    "6. I'm going to ______________________",
    "7. I'm going to ______________________",
    "8. I'm going to ______________________",
    "9. I'm going to ______________________",
    "10. I'm going to ______________________"
]

for plan_template in your_plans:
    print(plan_template)"""
        )
    )

    # Activity 2: This Weekend
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 2: This Weekend

Plan your ideal weekend and write about what you're going to do.

**Instructions:**
1. Plan activities for Saturday and Sunday
2. Include times (morning, afternoon, evening)
3. Use "going to" for all activities
4. Be specific and realistic

**Structure:**
- Saturday morning: ...
- Saturday afternoon: ...
- Saturday evening: ...
- Sunday morning: ...
- Sunday afternoon: ...
- Sunday evening: ..."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 2: Weekend plans
print("MY WEEKEND PLANS")
print("=" * 70)

example_weekend = {
    "Saturday": {
        "Morning": "I'm going to sleep until 9 AM. Then I'm going to have a big breakfast.",
        "Afternoon": "I'm going to go shopping with my friends. We're going to buy some new clothes.",
        "Evening": "I'm going to cook dinner at home. Then I'm going to watch a movie."
    },
    "Sunday": {
        "Morning": "I'm going to go to the gym. I'm going to exercise for an hour.",
        "Afternoon": "I'm going to visit my parents. We're going to have lunch together.",
        "Evening": "I'm going to prepare for the new week. I'm going to organize my things for Monday."
    }
}

print("\\nExample Weekend Plan:\\n")
for day, activities in example_weekend.items():
    print(f"{day.upper()}:")
    for time_of_day, activity in activities.items():
        print(f"  {time_of_day}: {activity}")
    print()

print("=" * 70)
print("NOW PLAN YOUR IDEAL WEEKEND!")
print("=" * 70)
print("\\nSATURDAY:")
print("  Morning: I'm going to ___________________________________")
print("  Afternoon: I'm going to ___________________________________")
print("  Evening: I'm going to ___________________________________")
print("\\nSUNDAY:")
print("  Morning: I'm going to ___________________________________")
print("  Afternoon: I'm going to ___________________________________")
print("  Evening: I'm going to ___________________________________")"""
        )
    )

    # Activity 3: Making Predictions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 3: Making Predictions

Look at the situations and make predictions using "going to".

**Instructions:**
1. Read each situation carefully
2. Look for evidence or clues
3. Make a logical prediction using "going to"
4. Explain why (what evidence do you see?)

**Remember:** Use "going to" for predictions when you have evidence!"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 3: Making predictions
situations = [
    {
        "situation": "The sky is full of dark clouds and the wind is getting stronger.",
        "prediction": "It's going to rain/storm soon.",
        "evidence": "Dark clouds and strong wind"
    },
    {
        "situation": "Tom studied very hard for his exam and knows all the answers.",
        "prediction": "He's going to pass the exam.",
        "evidence": "He studied hard and knows the material"
    },
    {
        "situation": "Sarah is running for the bus, but it's starting to move.",
        "prediction": "She's going to miss the bus.",
        "evidence": "The bus is leaving and she's still far"
    },
    {
        "situation": "The restaurant is full and there are 20 people waiting outside.",
        "prediction": "We're going to wait a long time. / We're not going to get a table soon.",
        "evidence": "Restaurant is full with many people waiting"
    },
    {
        "situation": "My phone battery is at 2% and I don't have a charger.",
        "prediction": "My phone is going to die soon.",
        "evidence": "Very low battery, no charger"
    },
    {
        "situation": "The baby is crying and looks very tired.",
        "prediction": "The baby is going to sleep soon.",
        "evidence": "Tired and crying (signs of sleepiness)"
    },
    {
        "situation": "John has been practicing basketball every day for months.",
        "prediction": "He's going to improve his skills. / He's going to play well.",
        "evidence": "Regular daily practice"
    },
    {
        "situation": "The traffic is terrible and we're still 30 minutes away from the airport. Our flight is in 40 minutes.",
        "prediction": "We're going to miss our flight.",
        "evidence": "Heavy traffic, not enough time"
    }
]

print("ACTIVITY 3: MAKING PREDICTIONS")
print("=" * 70)
print("\\nInstructions: Read each situation and make a prediction.\\n")

for i, item in enumerate(situations, 1):
    print(f"{i}. SITUATION: {item['situation']}")
    print(f"   YOUR PREDICTION: _______________________________")
    print()

print("=" * 70)
print("SAMPLE ANSWERS:")
print("=" * 70 + "\\n")

for i, item in enumerate(situations, 1):
    print(f"{i}. PREDICTION: {item['prediction']}")
    print(f"   EVIDENCE: {item['evidence']}")
    print()"""
        )
    )

    # Activity 4: Travel Plans
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 4: Dream Vacation

Plan your dream vacation and describe what you're going to do.

**Instructions:**
1. Choose a destination
2. Decide when you're going to go
3. Plan what you're going to do there (at least 8 activities)
4. Include details (where, when, with whom)

**Topics to cover:**
- Transportation (how are you going to get there?)
- Accommodation (where are you going to stay?)
- Activities (what are you going to do?)
- Food (what are you going to eat/try?)
- Sightseeing (what are you going to visit?)"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 4: Dream vacation plans
print("MY DREAM VACATION")
print("=" * 70)

example_vacation = {
    "Destination": "Paris, France",
    "When": "Next summer (July)",
    "Duration": "10 days",
    "Plans": [
        "I'm going to fly to Paris from my city.",
        "I'm going to stay in a small hotel near the Eiffel Tower.",
        "I'm going to visit the Louvre Museum on the first day.",
        "I'm going to climb the Eiffel Tower and take photos.",
        "I'm going to try authentic French croissants and pastries.",
        "I'm going to walk along the Seine River.",
        "I'm going to visit Versailles Palace.",
        "I'm going to eat at traditional French restaurants.",
        "I'm going to practice my French with local people.",
        "I'm going to buy souvenirs for my family.",
        "I'm going to take lots of photos and create a photo album."
    ]
}

print("\\nExample Dream Vacation:\\n")
print(f"Destination: {example_vacation['Destination']}")
print(f"When: {example_vacation['When']}")
print(f"Duration: {example_vacation['Duration']}")
print("\\nMy Plans:")
for i, plan in enumerate(example_vacation['Plans'], 1):
    print(f"  {i}. {plan}")

print("\\n" + "=" * 70)
print("NOW PLAN YOUR DREAM VACATION!")
print("=" * 70)
print("\\nDestination: ______________________________")
print("When: ______________________________")
print("Duration: ______________________________")
print("\\nMy Plans:")
for i in range(1, 11):
    print(f"  {i}. I'm going to ______________________________")"""
        )
    )

    # Activity 5: Life Goals
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 5: Five-Year Plan

Think about your life 5 years from now. What are you going to achieve?

**Instructions:**
1. Think about different areas of your life
2. Set realistic goals for 5 years from now
3. Write what you're going to do to achieve these goals
4. Use "going to" for your plans and intentions

**Areas to consider:**
- Career/Education
- Personal development
- Relationships/Family
- Health/Fitness
- Hobbies/Skills
- Financial goals"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 5: Five-year plan
print("MY FIVE-YEAR PLAN")
print("=" * 70)

example_five_year_plan = {
    "Career/Education": [
        "I'm going to finish my university degree.",
        "I'm going to find a job in my field.",
        "I'm going to gain 5 years of professional experience."
    ],
    "Personal Development": [
        "I'm going to learn three new languages.",
        "I'm going to read 100 important books.",
        "I'm going to develop my public speaking skills."
    ],
    "Health/Fitness": [
        "I'm going to exercise regularly and stay healthy.",
        "I'm going to run a marathon.",
        "I'm going to eat healthier food."
    ],
    "Relationships/Family": [
        "I'm going to spend quality time with my family.",
        "I'm going to make new friends from different countries.",
        "I'm going to stay in touch with old friends."
    ],
    "Skills/Hobbies": [
        "I'm going to learn to play the piano.",
        "I'm going to learn photography.",
        "I'm going to start painting."
    ],
    "Financial": [
        "I'm going to save money every month.",
        "I'm going to invest in my future.",
        "I'm going to buy my own apartment."
    ]
}

print("\\nExample Five-Year Plan:\\n")
for category, goals in example_five_year_plan.items():
    print(f"{category.upper()}:")
    for goal in goals:
        print(f"  • {goal}")
    print()

print("=" * 70)
print("NOW CREATE YOUR FIVE-YEAR PLAN!")
print("=" * 70)

categories = ["Career/Education", "Personal Development", "Health/Fitness",
              "Relationships/Family", "Skills/Hobbies", "Financial"]

for category in categories:
    print(f"\\n{category.upper()}:")
    for i in range(1, 4):
        print(f"  {i}. I'm going to ______________________________")"""
        )
    )

    # Activity 6: Weather Forecast
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 6: Weather Predictions

Look at the weather signs and make predictions for the next week.

**Instructions:**
1. Read the weather signs/conditions
2. Make predictions using "going to"
3. Say what people are/aren't going to do because of the weather
4. Give advice based on your predictions

**Useful vocabulary:**
- rain, snow, storm, sunshine, clouds
- hot, cold, warm, cool
- windy, foggy, sunny, cloudy"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 6: Weather predictions
print("WEATHER PREDICTIONS FOR THE WEEK")
print("=" * 70)

weather_scenarios = [
    {
        "day": "Monday",
        "signs": "Heavy dark clouds gathering, wind getting stronger, temperature dropping",
        "prediction": "It's going to rain heavily. / It's going to storm.",
        "consequences": "People are going to stay indoors. / We're going to need umbrellas."
    },
    {
        "day": "Tuesday",
        "signs": "Clear blue sky, sun shining bright, temperature 30°C",
        "prediction": "It's going to be hot and sunny.",
        "consequences": "People are going to go to the beach. / We're going to need sunscreen."
    },
    {
        "day": "Wednesday",
        "signs": "Temperature -5°C, grey clouds, feels like snow weather",
        "prediction": "It's going to snow.",
        "consequences": "People are going to wear warm clothes. / Children are going to play in the snow."
    },
    {
        "day": "Thursday",
        "signs": "Foggy morning, visibility low, damp and cold",
        "prediction": "It's going to be foggy all day.",
        "consequences": "Drivers are going to drive slowly. / Flights are going to be delayed."
    },
    {
        "day": "Friday",
        "signs": "Mild temperature, partly cloudy, light breeze",
        "prediction": "It's going to be a nice day.",
        "consequences": "People are going to spend time outside. / It's going to be perfect for outdoor activities."
    }
]

print("\\nWeather Signs → Predictions → Consequences\\n")

for scenario in weather_scenarios:
    print(f"{scenario['day'].upper()}:")
    print(f"  Signs: {scenario['signs']}")
    print(f"  Prediction: {scenario['prediction']}")
    print(f"  Consequences: {scenario['consequences']}")
    print()

print("=" * 70)
print("NOW CREATE YOUR OWN WEATHER PREDICTIONS!")
print("=" * 70)

days = ["Saturday", "Sunday"]
for day in days:
    print(f"\\n{day.upper()}:")
    print("  Weather signs: ______________________________")
    print("  Prediction: It's going to ______________________________")
    print("  People are going to ______________________________")"""
        )
    )

    # Activity 7: Career Plans
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 7: My Career Path

Describe your career plans and professional goals.

**Instructions:**
1. Think about your career aspirations
2. Write about your educational plans
3. Describe your job goals
4. Mention skills you're going to develop
5. Include timeline (when things are going to happen)

**Questions to answer:**
- What are you going to study?
- Where are you going to work?
- What position are you going to have?
- What skills are you going to learn?
- How are you going to achieve your goals?"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 7: Career plans
print("MY CAREER PATH")
print("=" * 70)

example_career_plan = {
    "Short-term (This year)": [
        "I'm going to finish my current courses with high grades.",
        "I'm going to do an internship at a tech company.",
        "I'm going to improve my programming skills.",
        "I'm going to attend professional networking events."
    ],
    "Medium-term (1-3 years)": [
        "I'm going to graduate from university.",
        "I'm going to get my first job as a software developer.",
        "I'm going to learn new programming languages.",
        "I'm going to work on real projects and gain experience."
    ],
    "Long-term (3-5 years)": [
        "I'm going to become a senior developer.",
        "I'm going to lead a team of developers.",
        "I'm going to work on innovative projects.",
        "I'm going to continue learning and developing my skills."
    ],
    "Skills to develop": [
        "I'm going to learn Python, JavaScript, and Java.",
        "I'm going to improve my problem-solving skills.",
        "I'm going to develop my communication skills.",
        "I'm going to learn about project management."
    ]
}

print("\\nExample Career Plan:\\n")
for phase, plans in example_career_plan.items():
    print(f"{phase}:")
    for plan in plans:
        print(f"  • {plan}")
    print()

print("=" * 70)
print("NOW DESCRIBE YOUR CAREER PATH!")
print("=" * 70)

phases = ["Short-term (This year)", "Medium-term (1-3 years)",
          "Long-term (3-5 years)", "Skills to develop"]

for phase in phases:
    print(f"\\n{phase}:")
    for i in range(1, 5):
        print(f"  {i}. I'm going to ______________________________")"""
        )
    )

    # Activity 8: Family Plans
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 8: Family Activities

Plan activities you're going to do with your family in the near future.

**Instructions:**
1. Think about activities with different family members
2. Include various types of activities (meals, outings, celebrations, etc.)
3. Mention when these activities are going to happen
4. Use "going to" for all plans

**Ideas:**
- Meals together
- Weekend outings
- Special celebrations
- Helping family members
- Family projects"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 8: Family activities
print("FAMILY ACTIVITIES PLANS")
print("=" * 70)

example_family_plans = [
    {
        "activity": "Family dinner",
        "when": "This Sunday",
        "details": "We're going to have dinner together at home. My mom is going to cook her special pasta. We're all going to help with cooking and cleaning."
    },
    {
        "activity": "Visit grandparents",
        "when": "Next weekend",
        "details": "My brother and I are going to visit our grandparents. We're going to spend the whole day with them. We're going to help them with housework."
    },
    {
        "activity": "Birthday celebration",
        "when": "Next month",
        "details": "We're going to celebrate my sister's birthday. We're going to organize a surprise party. We're going to invite all her friends."
    },
    {
        "activity": "Family trip",
        "when": "Summer vacation",
        "details": "We're going to take a family trip to the mountains. We're going to stay there for a week. We're going to go hiking and enjoy nature."
    },
    {
        "activity": "Help with project",
        "when": "This month",
        "details": "I'm going to help my dad with his garden project. We're going to plant new flowers and vegetables. We're going to work on it every weekend."
    }
]

print("\\nExample Family Plans:\\n")
for i, plan in enumerate(example_family_plans, 1):
    print(f"{i}. {plan['activity'].upper()} - {plan['when']}")
    print(f"   {plan['details']}")
    print()

print("=" * 70)
print("NOW PLAN YOUR FAMILY ACTIVITIES!")
print("=" * 70)

print("\\n1. ACTIVITY: ______________________  WHEN: ______________________")
print("   Details: We're going to ______________________________")
print("\\n2. ACTIVITY: ______________________  WHEN: ______________________")
print("   Details: We're going to ______________________________")
print("\\n3. ACTIVITY: ______________________  WHEN: ______________________")
print("   Details: We're going to ______________________________")
print("\\n4. ACTIVITY: ______________________  WHEN: ______________________")
print("   Details: We're going to ______________________________")
print("\\n5. ACTIVITY: ______________________  WHEN: ______________________")
print("   Details: We're going to ______________________________")"""
        )
    )

    # Activity 9: Event Planning
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 9: Planning a Party

You're going to organize a party! Plan all the details.

**Instructions:**
1. Decide what kind of party (birthday, graduation, etc.)
2. Plan all the details using "going to"
3. Include: date, time, place, guests, food, activities, decorations

**Details to plan:**
- When and where is it going to be?
- Who are you going to invite?
- What food are you going to serve?
- What activities are you going to have?
- How are you going to decorate?
- What music are you going to play?"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 9: Party planning
print("PARTY PLANNING")
print("=" * 70)

example_party_plan = {
    "Type": "Birthday party",
    "Date & Time": "Next Saturday, 7 PM",
    "Location": "My apartment",
    "Plans": [
        "I'm going to invite 20 friends.",
        "I'm going to decorate the room with balloons and lights.",
        "I'm going to order pizza and make a salad.",
        "I'm going to bake a chocolate cake.",
        "I'm going to prepare a playlist with dance music.",
        "My friend is going to help me with the decorations.",
        "We're going to play some party games.",
        "We're going to take lots of photos.",
        "The party is going to end at midnight.",
        "I'm going to clean up the next morning."
    ],
    "Shopping List": [
        "I'm going to buy balloons and decorations.",
        "I'm going to buy drinks and snacks.",
        "I'm going to buy ingredients for the cake.",
        "I'm going to buy party hats and plates."
    ]
}

print("\\nExample Party Plan:\\n")
print(f"Party Type: {example_party_plan['Type']}")
print(f"Date & Time: {example_party_plan['Date & Time']}")
print(f"Location: {example_party_plan['Location']}")
print("\\nParty Plans:")
for i, plan in enumerate(example_party_plan['Plans'], 1):
    print(f"  {i}. {plan}")
print("\\nShopping List:")
for item in example_party_plan['Shopping List']:
    print(f"  • {item}")

print("\\n" + "=" * 70)
print("NOW PLAN YOUR PARTY!")
print("=" * 70)
print("\\nParty Type: ______________________________")
print("Date & Time: ______________________________")
print("Location: ______________________________")
print("\\nParty Plans:")
for i in range(1, 11):
    print(f"  {i}. I'm going to / We're going to ______________________________")
print("\\nShopping List:")
for i in range(1, 6):
    print(f"  {i}. I'm going to buy ______________________________")"""
        )
    )

    # Activity 10: New Year Resolutions
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Activity 10: New Year's Resolutions

Make a list of New Year's resolutions - things you're going to do to improve your life.

**Instructions:**
1. Think about different aspects of your life you want to improve
2. Write realistic resolutions
3. Explain how you're going to achieve each resolution
4. Use "going to" for all your intentions

**Categories:**
- Health and fitness
- Learning and education
- Relationships
- Career
- Hobbies and interests
- Personal habits"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Activity 10: New Year's resolutions
print("MY NEW YEAR'S RESOLUTIONS")
print("=" * 70)

example_resolutions = [
    {
        "resolution": "Get healthier and fitter",
        "how": [
            "I'm going to exercise 4 times a week.",
            "I'm going to eat more vegetables and fruits.",
            "I'm going to drink more water.",
            "I'm going to sleep 8 hours every night."
        ]
    },
    {
        "resolution": "Learn new skills",
        "how": [
            "I'm going to take an online course in web design.",
            "I'm going to practice English every day.",
            "I'm going to learn to play the guitar.",
            "I'm going to read one book per month."
        ]
    },
    {
        "resolution": "Improve relationships",
        "how": [
            "I'm going to call my parents every week.",
            "I'm going to spend more time with my friends.",
            "I'm going to be more patient and kind.",
            "I'm going to listen more and talk less."
        ]
    },
    {
        "resolution": "Save money and manage finances better",
        "how": [
            "I'm going to create a monthly budget.",
            "I'm going to save 20% of my income.",
            "I'm going to reduce unnecessary expenses.",
            "I'm going to invest in my education."
        ]
    },
    {
        "resolution": "Be more organized and productive",
        "how": [
            "I'm going to wake up earlier.",
            "I'm going to make daily to-do lists.",
            "I'm going to clean my room every weekend.",
            "I'm going to plan my week in advance."
        ]
    }
]

print("\\nExample Resolutions:\\n")
for i, res in enumerate(example_resolutions, 1):
    print(f"{i}. {res['resolution'].upper()}")
    print("   How I'm going to achieve it:")
    for step in res['how']:
        print(f"   • {step}")
    print()

print("=" * 70)
print("NOW WRITE YOUR NEW YEAR'S RESOLUTIONS!")
print("=" * 70)

resolution_categories = [
    "Health and Fitness",
    "Learning and Education",
    "Relationships",
    "Career/Work",
    "Personal Habits"
]

for i, category in enumerate(resolution_categories, 1):
    print(f"\\n{i}. {category.upper()}")
    print("   Resolution: I'm going to ______________________________")
    print("   How I'm going to achieve it:")
    for j in range(1, 4):
        print(f"   {j}. I'm going to ______________________________")"""
        )
    )

    # Summary
    cells.append(
        nbf.v4.new_markdown_cell(
            """## Phase 3 Complete!

### Activities Completed: 10

**You have practiced "going to" in meaningful contexts:**
- [OK] Personal future plans
- [OK] Weekend planning
- [OK] Making predictions based on evidence
- [OK] Dream vacation planning
- [OK] Five-year life goals
- [OK] Weather predictions
- [OK] Career path planning
- [OK] Family activities
- [OK] Event planning (party)
- [OK] New Year's resolutions

### What's Next?
In **Phase 4 (Communicative Practice)**, you'll use "going to" in interactive tasks and real communication scenarios.

Excellent progress! [TARGET]"""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# Phase 3 summary
summary = {
    "Total activities": 10,
    "Contexts practiced": [
        "Personal plans and intentions",
        "Weekend and leisure activities",
        "Evidence-based predictions",
        "Travel and vacation planning",
        "Long-term life goals",
        "Weather forecasting",
        "Career and professional development",
        "Family and social activities",
        "Event organization",
        "New Year's resolutions and self-improvement"
    ],
    "Skills developed": [
        "Expressing future plans naturally",
        "Making predictions with evidence",
        "Organizing thoughts about the future",
        "Using time expressions appropriately",
        "Writing about intentions and goals",
        "Describing planned activities"
    ],
    "Estimated time": "60-90 minutes"
}

print("PHASE 3 COMPLETION SUMMARY")
print("=" * 70)
print(f"\\nTotal Activities: {summary['Total activities']}")
print(f"\\nContexts Practiced:")
for i, context in enumerate(summary['Contexts practiced'], 1):
    print(f"  {i}. {context}")
print(f"\\nSkills Developed:")
for i, skill in enumerate(summary['Skills developed'], 1):
    print(f"  {i}. {skill}")
print(f"\\nEstimated Time: {summary['Estimated time']}")
print("\\n" + "=" * 70)
print("[OK] Ready for Phase 4: Communicative Practice!")
print("=" * 70)"""
        )
    )

    # Add all cells to notebook
    nb["cells"] = cells
    return nb


if __name__ == "__main__":
    notebook = create_notebook()
    output_path = "03_meaningful_practice.ipynb"

    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(notebook, f)

    print(f"Notebook created successfully: {output_path}")
    print(f"Total cells: {len(notebook['cells'])}")
    print(f"Total activities: 10")
