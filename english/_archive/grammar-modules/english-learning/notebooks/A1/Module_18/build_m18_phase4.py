"""
Builder script for Module 18 Phase 4: Going To Future - Communicative Practice
Target: 8 communicative tasks
"""

import nbformat as nbf


def create_notebook():
    nb = nbf.v4.new_notebook()
    cells = []

    # Title
    cells.append(nbf.v4.new_markdown_cell("""# Module 18: Going To Future - Phase 4: Communicative Practice

## Overview
This phase contains **8 communicative tasks** where you'll use "going to" in real interaction scenarios.

**Task Types:**
- Interview tasks
- Role-plays
- Discussion activities
- Information gap activities
- Problem-solving tasks
- Collaborative planning
- Presentation tasks

**Target Level:** A1 (Elementary)
**Estimated Time:** 60-90 minutes

**Note:** These tasks are designed for pair/group work but can be adapted for self-study."""))

    # Task 1: Future Plans Interview
    cells.append(nbf.v4.new_markdown_cell("""## Task 1: Future Plans Interview

**Type:** Pair work / Interview

**Objective:** Interview your partner about their future plans

**Instructions:**
1. Work with a partner (or imagine interviewing someone)
2. Ask questions using "going to"
3. Take notes on their answers
4. Share interesting information with the class/group

**Interview Questions:**

1. What are you going to do after this class/course?
2. Where are you going to go on your next vacation?
3. What are you going to study next year?
4. Are you going to change your job? Why/Why not?
5. What are you going to do this weekend?
6. Are you going to learn any new skills? Which ones?
7. Where are you going to live in 5 years?
8. What are you going to achieve in the next year?
9. Are you going to buy anything expensive soon? What?
10. Who are you going to visit in the near future?

**Follow-up Questions:**
- When exactly are you going to...?
- How are you going to...?
- Why are you going to...?
- Who is going to... with you?"""))

    cells.append(nbf.v4.new_code_cell("""# Task 1: Interview notes template
print("FUTURE PLANS INTERVIEW - NOTES TEMPLATE")
print("=" * 70)

interview_template = {
    "Partner's name": "___________________",
    "Date": "___________________",
    "Questions and Answers": [
        "1. After class/course: ",
        "2. Next vacation: ",
        "3. Study plans: ",
        "4. Job change: ",
        "5. This weekend: ",
        "6. New skills: ",
        "7. Living situation (5 years): ",
        "8. Next year goals: ",
        "9. Expensive purchase: ",
        "10. Visit plans: "
    ],
    "Interesting facts": [
        "1. ",
        "2. ",
        "3. "
    ]
}

print("\\nPartner's Name: _______________________")
print("Date: _______________________\\n")
print("INTERVIEW NOTES:\\n")

for item in interview_template["Questions and Answers"]:
    print(item + "_" * 50)
    print()

print("\\nMost interesting things I learned:")
for fact in interview_template["Interesting facts"]:
    print(fact + "_" * 60)

print("\\n" + "=" * 70)
print("Example Interview Summary:")
print("=" * 70)
print("""
Partner: Maria

Interesting plans:
• She's going to travel to Japan next summer for 3 weeks
• She's going to learn Japanese before the trip
• She's going to work as a volunteer teacher after graduation
• She's going to move to a new apartment next month
""")"""))

    # Task 2: Fortune Teller
    cells.append(nbf.v4.new_markdown_cell("""## Task 2: Fortune Teller Role-Play

**Type:** Role-play (pairs)

**Objective:** Practice making predictions using "going to"

**Instructions:**
1. Work in pairs
2. Student A: Fortune teller
3. Student B: Customer
4. The fortune teller makes predictions about the customer's future
5. The customer asks questions
6. Switch roles after 10 predictions

**Role A - Fortune Teller:**
Look at your customer and make predictions:
- "I see... you're going to..."
- "In your future, you're going to..."
- "Soon, you're going to..."

**Role B - Customer:**
Ask about different areas of life:
- "Am I going to be successful?"
- "What am I going to do next year?"
- "Am I going to meet someone special?"
- "Am I going to be rich?"

**Topics for predictions:**
- Career
- Love/relationships
- Travel
- Money
- Health
- Family
- Success
- Surprises"""))

    cells.append(nbf.v4.new_code_cell("""# Task 2: Fortune teller prediction cards
print("FORTUNE TELLER - PREDICTION CARDS")
print("=" * 70)

prediction_cards = {
    "Career & Education": [
        "You're going to get an amazing job offer soon.",
        "You're going to learn a valuable new skill this year.",
        "You're going to work in a different country.",
        "You're going to start your own business in the future."
    ],
    "Love & Relationships": [
        "You're going to meet someone special very soon.",
        "You're going to reconnect with an old friend.",
        "You're going to have an important conversation with someone.",
        "You're going to make a new best friend."
    ],
    "Travel & Adventure": [
        "You're going to take an exciting trip abroad.",
        "You're going to visit three new countries.",
        "You're going to have an unexpected adventure.",
        "You're going to move to a new city."
    ],
    "Money & Success": [
        "You're going to find money in an unexpected place!",
        "You're going to receive good financial news.",
        "You're going to make a smart investment.",
        "You're going to achieve a big goal."
    ],
    "Surprises": [
        "Something surprising is going to happen next week.",
        "You're going to receive an unexpected gift.",
        "You're going to discover a hidden talent.",
        "You're going to have a lucky day very soon."
    ]
}

print("\\nUse these prediction ideas (or create your own!):\\n")
for category, predictions in prediction_cards.items():
    print(f"{category.upper()}:")
    for pred in predictions:
        print(f"  • {pred}")
    print()

print("=" * 70)
print("EXAMPLE DIALOGUE:")
print("=" * 70)
print("""
Customer: What do you see in my future?
Fortune Teller: I see... you're going to travel very soon!
Customer: Really? Where am I going to go?
Fortune Teller: You're going to visit a beautiful island.
Customer: Am I going to travel alone?
Fortune Teller: No, you're going to travel with someone special.
Customer: That sounds wonderful! Am I going to have a good job?
Fortune Teller: Yes! You're going to get an excellent job offer next month.
Customer: Am I going to accept it?
Fortune Teller: I see that you're going to think carefully, and... yes,
               you're going to accept it!
""")"""))

    # Task 3: Weekend Plans Discussion
    cells.append(nbf.v4.new_markdown_cell("""## Task 3: Weekend Plans Discussion

**Type:** Group discussion (3-4 people)

**Objective:** Discuss and compare weekend plans

**Instructions:**
1. Form groups of 3-4 people
2. Each person shares their weekend plans
3. Ask each other questions
4. Find similarities and differences
5. Report to the class

**Discussion Points:**
- What are you going to do on Saturday?
- What are you going to do on Sunday?
- Are you going to stay home or go out?
- Are you going to meet any friends?
- What time are you going to wake up?
- Are you going to do anything special?
- Are you going to relax or be busy?

**Follow-up Discussion:**
- Who has the most interesting plans?
- Who is going to be the busiest?
- Who is going to relax the most?
- Does anyone have similar plans?
- Would you like to join anyone's plans?"""))

    cells.append(nbf.v4.new_code_cell("""# Task 3: Weekend plans comparison
print("WEEKEND PLANS DISCUSSION - GROUP ACTIVITY")
print("=" * 70)

print("\\nSTEP 1: Individual Planning")
print("-" * 70)
print("Complete your weekend plans:\\n")

weekend_plan_template = {
    "Saturday Morning": "",
    "Saturday Afternoon": "",
    "Saturday Evening": "",
    "Sunday Morning": "",
    "Sunday Afternoon": "",
    "Sunday Evening": ""
}

for time_slot in weekend_plan_template:
    print(f"{time_slot}: I'm going to _______________________________")

print("\\n" + "=" * 70)
print("STEP 2: Group Discussion Questions")
print("=" * 70)

discussion_questions = [
    "What are you going to do on Saturday morning?",
    "Where are you going to go?",
    "Who are you going to meet?",
    "What time are you going to wake up?",
    "Are you going to cook or eat out?",
    "Are you going to exercise?",
    "Are you going to watch any movies or shows?",
    "Are you going to do any housework?",
    "What's the most interesting thing you're going to do?"
]

print("\\nAsk your group members:")
for i, question in enumerate(discussion_questions, 1):
    print(f"{i}. {question}")

print("\\n" + "=" * 70)
print("STEP 3: Comparison")
print("=" * 70)
print("""
Compare plans and find:
• Who is going to be the busiest? _______________________
• Who is going to relax the most? _______________________
• Who has similar plans to you? _______________________
• Most interesting plan? _______________________
• Most relaxing plan? _______________________
""")

print("=" * 70)
print("EXAMPLE GROUP REPORT:")
print("=" * 70)
print("""
In our group:
• Maria is going to visit her parents on Saturday.
• John is going to play football with his friends.
• Anna is going to study for her exam all weekend.
• I'm going to go shopping and watch movies.
• Anna is going to be the busiest person!
• I'm going to be the most relaxed.
• Maria and I are both going to watch movies on Sunday evening.
""")"""))

    # Task 4: Travel Agency Role-Play
    cells.append(nbf.v4.new_markdown_cell("""## Task 4: Travel Agency Role-Play

**Type:** Role-play (pairs)

**Objective:** Plan a vacation together

**Instructions:**
1. Student A: Travel agent
2. Student B: Customer
3. The customer wants to plan a vacation
4. The travel agent asks questions and makes suggestions
5. Together, plan the perfect vacation

**Student A - Travel Agent:**
Ask questions and offer suggestions:
- "Where are you going to go?"
- "When are you going to travel?"
- "How long are you going to stay?"
- "What are you going to do there?"
- "Are you going to travel alone?"
- "What's your budget?"

Make suggestions:
- "You're going to love..."
- "I think you're going to enjoy..."
- "You're going to need..."

**Student B - Customer:**
Answer questions and ask for advice:
- "I'm going to..."
- "Am I going to need...?"
- "What am I going to do there?"
- "How am I going to get there?"
- "Where am I going to stay?"

**Plan together:**
- Destination
- Dates
- Duration
- Accommodation
- Activities
- Transportation
- Budget"""))

    cells.append(nbf.v4.new_code_cell("""# Task 4: Travel planning worksheet
print("TRAVEL AGENCY ROLE-PLAY - PLANNING WORKSHEET")
print("=" * 70)

print("\\nTRAVEL PLAN:")
print("=" * 70)

travel_plan = {
    "Destination": "Where are you going to go? _______________________",
    "Travel Dates": "When are you going to travel? _______________________",
    "Duration": "How long are you going to stay? _______________________",
    "Transportation": "How are you going to get there? _______________________",
    "Accommodation": "Where are you going to stay? _______________________",
    "Activities": "What are you going to do? (list 5 activities)",
    "Budget": "How much are you going to spend? _______________________",
    "Travel companions": "Who is going to travel with you? _______________________"
}

for key, value in travel_plan.items():
    if key == "Activities":
        print(f"\\n{key}:")
        for i in range(1, 6):
            print(f"  {i}. I'm going to _______________________________")
    else:
        print(f"\\n{key}: {value}")

print("\\n" + "=" * 70)
print("EXAMPLE DIALOGUE:")
print("=" * 70)
print("""
Agent: Good morning! Where are you going to go on vacation?
Customer: I'm thinking about going to Thailand.

Agent: Wonderful! When are you going to travel?
Customer: I'm going to travel in December.

Agent: How long are you going to stay?
Customer: I'm going to stay for two weeks.

Agent: Are you going to travel alone?
Customer: No, I'm going to travel with my partner.

Agent: Great! You're going to love Thailand in December. The weather is
       going to be perfect! Now, where are you going to stay?
Customer: I'm not sure. What do you suggest?

Agent: I think you're going to enjoy staying in Bangkok for a few days,
       then you're going to visit some islands.
Customer: That sounds perfect! What are we going to do there?

Agent: In Bangkok, you're going to visit temples and try amazing food.
       On the islands, you're going to swim and relax on beautiful beaches.
Customer: Wonderful! How much is this going to cost?

Agent: For two people, two weeks, you're going to spend about $3000,
       including flights and hotels.
Customer: That's reasonable. I'm going to book this trip!
""")"""))

    # Task 5: Problem Solving
    cells.append(nbf.v4.new_markdown_cell("""## Task 5: Problem-Solving Discussion

**Type:** Group discussion

**Objective:** Solve problems by discussing future actions

**Instructions:**
1. Read each problem situation
2. Discuss what you're going to do
3. Use "going to" to express your solutions
4. Compare solutions with other groups

**Problem Situations:**

**Situation 1: Bad Weather on Vacation Day**
You planned an outdoor picnic, but it's going to rain all day tomorrow.
- What are you going to do?
- Are you going to cancel or change plans?
- What alternative activities are you going to do?

**Situation 2: Failed Exam**
Your friend failed an important exam.
- What is your friend going to do?
- How are you going to help?
- What's the plan for the next exam?

**Situation 3: Late for Important Meeting**
You're stuck in traffic and you're going to be late for an important job interview.
- What are you going to do?
- Are you going to call?
- What are you going to say?

**Situation 4: Lost Passport Before Trip**
You're going to travel abroad next week, but you lost your passport.
- What are you going to do first?
- Who are you going to call?
- Are you going to cancel your trip?

**Situation 5: Surprise Guests**
Your parents are going to visit you tomorrow (surprise!), but your apartment is messy.
- What are you going to do tonight?
- What are you going to clean first?
- What are you going to cook for them?"""))

    cells.append(nbf.v4.new_code_cell("""# Task 5: Problem-solving solutions
print("PROBLEM-SOLVING DISCUSSION")
print("=" * 70)

problems_and_solutions = [
    {
        "problem": "Situation 1: Bad Weather on Vacation Day",
        "sample_solutions": [
            "We're going to move the picnic indoors.",
            "We're going to go to a museum instead.",
            "We're going to watch movies and cook at home.",
            "We're going to reschedule for next weekend."
        ]
    },
    {
        "problem": "Situation 2: Failed Exam",
        "sample_solutions": [
            "My friend is going to talk to the teacher.",
            "We're going to study together for the retake.",
            "He's going to make a study schedule.",
            "I'm going to help him with difficult topics."
        ]
    },
    {
        "problem": "Situation 3: Late for Important Meeting",
        "sample_solutions": [
            "I'm going to call immediately and explain.",
            "I'm going to apologize and give a new arrival time.",
            "I'm going to take a taxi instead.",
            "I'm going to ask if they can reschedule."
        ]
    },
    {
        "problem": "Situation 4: Lost Passport Before Trip",
        "sample_solutions": [
            "I'm going to call the passport office immediately.",
            "I'm going to apply for an emergency passport.",
            "I'm going to contact my travel insurance.",
            "If needed, I'm going to postpone my trip."
        ]
    },
    {
        "problem": "Situation 5: Surprise Guests",
        "sample_solutions": [
            "I'm going to clean the whole apartment tonight.",
            "I'm going to go shopping for food.",
            "I'm going to cook their favorite meal.",
            "I'm going to buy fresh flowers to decorate."
        ]
    }
]

print("\\nPROBLEM SITUATIONS AND SAMPLE SOLUTIONS:\\n")

for item in problems_and_solutions:
    print(f"{item['problem'].upper()}")
    print("Sample solutions:")
    for solution in item['sample_solutions']:
        print(f"  • {solution}")
    print()

print("=" * 70)
print("YOUR TURN - Plan your solutions:")
print("=" * 70)
print("""
For each situation, write at least 3 solutions:

Situation 1 (Bad Weather):
1. I'm going to _______________________________
2. We're going to _______________________________
3. I'm going to _______________________________

Situation 2 (Failed Exam):
1. My friend is going to _______________________________
2. I'm going to _______________________________
3. We're going to _______________________________

Situation 3 (Late for Meeting):
1. I'm going to _______________________________
2. I'm going to _______________________________
3. Then I'm going to _______________________________

Situation 4 (Lost Passport):
1. First, I'm going to _______________________________
2. Then I'm going to _______________________________
3. If necessary, I'm going to _______________________________

Situation 5 (Surprise Guests):
1. Tonight I'm going to _______________________________
2. Tomorrow morning I'm going to _______________________________
3. I'm also going to _______________________________
""")"""))

    # Task 6: Group Project Planning
    cells.append(nbf.v4.new_markdown_cell("""## Task 6: Group Project Planning

**Type:** Group activity (3-4 people)

**Objective:** Plan a group project together

**Instructions:**
1. Choose a project (options below)
2. Divide responsibilities
3. Create a timeline
4. Present your plan to the class

**Project Options:**
1. **Class Party:** Plan an end-of-course party
2. **Study Group:** Organize a study group for the exam
3. **Charity Event:** Plan a charity fundraising event
4. **Trip:** Organize a class trip
5. **Presentation:** Prepare a group presentation

**Planning Steps:**
1. What is your group going to do?
2. When are you going to do it?
3. Where is it going to be?
4. Who is going to do what?
5. What materials are you going to need?
6. How much is it going to cost?
7. What are the steps?

**Use "going to" to:**
- Assign tasks: "Maria is going to..."
- Set deadlines: "We're going to finish by..."
- Describe plans: "We're going to..."
- Make promises: "I'm going to make sure that..."'"""))

    cells.append(nbf.v4.new_code_cell("""# Task 6: Group project planning template
print("GROUP PROJECT PLANNING")
print("=" * 70)

print("\\nPROJECT PLANNING TEMPLATE\\n")

planning_template = {
    "Project Name": "_______________________________",
    "Group Members": [
        "1. _______________________________",
        "2. _______________________________",
        "3. _______________________________",
        "4. _______________________________"
    ],
    "Project Goals": "What are we going to achieve?",
    "Timeline": "When are we going to do this?",
    "Location": "Where is it going to be?",
    "Budget": "How much are we going to spend?",
    "Task Distribution": "Who is going to do what?",
    "Materials Needed": "What are we going to need?"
}

print(f"Project Name: {planning_template['Project Name']}")
print("\\nGroup Members:")
for member in planning_template['Group Members']:
    print(f"  {member}")

print(f"\\nProject Goals:")
print("We're going to _______________________________")
print("We're going to _______________________________")

print(f"\\nTimeline:")
print("Week 1: We're going to _______________________________")
print("Week 2: We're going to _______________________________")
print("Week 3: We're going to _______________________________")
print("Week 4: We're going to _______________________________")

print(f"\\nLocation: {planning_template['Location']}")
print(f"Budget: {planning_template['Budget']}")

print("\\nTask Distribution:")
print("_________________________________ is going to _______________________________")
print("_________________________________ is going to _______________________________")
print("_________________________________ is going to _______________________________")
print("_________________________________ is going to _______________________________")

print("\\nMaterials Needed:")
print("We're going to need _______________________________")

print("\\n" + "=" * 70)
print("EXAMPLE: Class Party Planning")
print("=" * 70)
print("""
Project: End-of-Course Party
Group Members: Maria, John, Anna, Tom

Project Goals:
• We're going to organize a fun party for all classmates
• We're going to celebrate the end of the course

Timeline:
• Week 1: We're going to decide the date and send invitations
• Week 2: We're going to buy decorations and plan the menu
• Week 3: We're going to prepare everything
• Week 4: We're going to have the party!

Location: School cafeteria
Date: Last Friday of the course, 6 PM
Budget: We're going to spend about $200

Task Distribution:
• Maria is going to organize the music and decorations
• John is going to handle the food and drinks
• Anna is going to send invitations and track RSVPs
• Tom is going to take photos and make a video

Materials Needed:
• We're going to need balloons, music equipment, tables, chairs
• We're going to need plates, cups, napkins
• We're going to need a camera for photos
""")"""))

    # Task 7: Predictions Game
    cells.append(nbf.v4.new_markdown_cell("""## Task 7: Predictions Game

**Type:** Group game

**Objective:** Make predictions about various topics

**Instructions:**
1. Form teams of 3-4 people
2. Take turns making predictions
3. Other teams guess if it's realistic or not
4. Discuss the predictions

**Prediction Categories:**

**A) Technology in 10 years**
- What new inventions are going to exist?
- How is technology going to change our lives?
- What devices are we going to use?

**B) Your Classmates' Futures**
- What is [name] going to do after this course?
- Where is [name] going to work?
- What is [name] going to achieve?

**C) The World in 2030**
- What changes are going to happen?
- What problems are we going to solve?
- What new challenges are we going to face?

**D) This Year**
- What's going to be the most popular movie?
- Who is going to win [sports event]?
- What's going to happen in [current event]?

**Game Rules:**
1. Make a prediction using "going to"
2. Other teams say "realistic" or "unrealistic"
3. Explain your prediction
4. Discuss different opinions
5. Points for creative and realistic predictions!"""))

    cells.append(nbf.v4.new_code_cell("""# Task 7: Predictions game cards
print("PREDICTIONS GAME")
print("=" * 70)

prediction_topics = {
    "Technology in 10 years": [
        "Cars are going to drive themselves everywhere.",
        "Everyone is going to have a robot assistant at home.",
        "We're going to use virtual reality for education.",
        "Smartphones are going to disappear - we're going to use smart glasses.",
        "AI is going to help doctors diagnose diseases faster."
    ],
    "Your Classmates": [
        "_____ is going to become a successful businessperson.",
        "_____ is going to travel to 50 countries.",
        "_____ is going to write a book.",
        "_____ is going to learn 5 languages.",
        "_____ is going to start their own company."
    ],
    "The World in 2030": [
        "Most cars are going to be electric.",
        "We're going to solve major environmental problems.",
        "People are going to work from home more often.",
        "Space tourism is going to be common.",
        "We're going to use more renewable energy."
    ],
    "This Year": [
        "The economy is going to improve.",
        "A new technology is going to change how we communicate.",
        "More people are going to learn online.",
        "Virtual events are going to become more popular.",
        "We're going to see amazing scientific discoveries."
    ],
    "Yourself in 5 years": [
        "I'm going to speak English fluently.",
        "I'm going to have my dream job.",
        "I'm going to live in a different country.",
        "I'm going to have achieved my main goals.",
        "I'm going to be very different from now."
    ]
}

print("\\nPREDICTION TOPICS AND EXAMPLES:\\n")

for category, predictions in prediction_topics.items():
    print(f"{category.upper()}:")
    for i, pred in enumerate(predictions, 1):
        print(f"  {i}. {pred}")
    print()

print("=" * 70)
print("HOW TO PLAY:")
print("=" * 70)
print("""
1. Team 1 makes a prediction:
   "In 10 years, cars are going to drive themselves everywhere."

2. Other teams respond:
   Team 2: "Realistic! Self-driving technology is developing fast."
   Team 3: "Unrealistic! Not everywhere - maybe in cities only."

3. Discuss:
   • Why do you think this is going to happen?
   • What evidence do you have?
   • When exactly is this going to happen?
   • How is this going to affect people?

4. Score points for:
   • Creative predictions
   • Realistic predictions
   • Good explanations
   • Interesting discussions
""")

print("\\nCREATE YOUR OWN PREDICTIONS:")
print("=" * 70)

categories = ["Technology", "Environment", "Society", "Your Life", "World Events"]
for category in categories:
    print(f"\\n{category}:")
    for i in range(1, 4):
        print(f"  {i}. _______________________ is/are going to _______________________")"""))

    # Task 8: Future Plans Presentation
    cells.append(nbf.v4.new_markdown_cell("""## Task 8: Future Plans Presentation

**Type:** Individual presentation

**Objective:** Present your future plans to the class

**Instructions:**
1. Prepare a 3-5 minute presentation about your future plans
2. Use "going to" throughout your presentation
3. Include visual aids if possible (pictures, timeline, etc.)
4. Answer questions from classmates

**Presentation Structure:**

**1. Introduction (30 seconds)**
- Greet the audience
- Introduce your topic
- "Today I'm going to talk about my future plans."

**2. Short-term Plans (1 minute)**
- This year
- Next few months
- "I'm going to..."

**3. Medium-term Plans (1-2 minutes)**
- 1-3 years
- Education/Career
- Personal goals
- "In the next few years, I'm going to..."

**4. Long-term Plans (1 minute)**
- 5+ years
- Big dreams and ambitions
- "In the future, I'm going to..."

**5. Conclusion (30 seconds)**
- Summary
- Final thoughts
- "These are my plans, and I'm going to work hard to achieve them."

**6. Q&A**
- Answer questions from classmates
- Use "going to" in your answers

**Tips:**
- Speak clearly and confidently
- Make eye contact
- Use gestures
- Show enthusiasm about your plans
- Be ready to explain WHY you're going to do these things"""))

    cells.append(nbf.v4.new_code_cell("""# Task 8: Presentation planning template
print("FUTURE PLANS PRESENTATION - PLANNING TEMPLATE")
print("=" * 70)

print("\\n1. INTRODUCTION")
print("-" * 70)
print("Opening: Good morning/afternoon everyone!")
print("Topic introduction: Today, I'm going to tell you about _______________________")
print()

print("\\n2. SHORT-TERM PLANS (This year)")
print("-" * 70)
print("This year, I'm going to:")
for i in range(1, 6):
    print(f"  {i}. _______________________________")
print()

print("\\n3. MEDIUM-TERM PLANS (1-3 years)")
print("-" * 70)
print("\\nEducation:")
print("I'm going to _______________________________")
print("\\nCareer:")
print("I'm going to _______________________________")
print("\\nPersonal Development:")
print("I'm going to _______________________________")
print("\\nOther goals:")
print("I'm going to _______________________________")
print()

print("\\n4. LONG-TERM PLANS (5+ years)")
print("-" * 70)
print("In the future:")
print("  • I'm going to _______________________________")
print("  • I'm going to _______________________________")
print("  • I'm going to _______________________________")
print()

print("\\n5. CONCLUSION")
print("-" * 70)
print("Summary: These are my main plans for the future.")
print("Final thought: I'm going to work hard to _______________________________")
print("Thank you: Thank you for listening!")
print()

print("=" * 70)
print("EXAMPLE PRESENTATION OUTLINE:")
print("=" * 70)
print("""
INTRODUCTION:
"Good morning! Today I'm going to tell you about my exciting plans for the future."

SHORT-TERM PLANS:
"This year, I have several important goals:
• I'm going to finish this English course with excellent grades
• I'm going to apply for university
• I'm going to get a part-time job
• I'm going to save money for my future education
• I'm going to improve my computer skills"

MEDIUM-TERM PLANS:
"In the next 2-3 years:
• I'm going to study Computer Science at university
• I'm going to do an internship at a technology company
• I'm going to learn two programming languages
• I'm going to make new friends and build a professional network
• I'm going to travel to another country to practice English"

LONG-TERM PLANS:
"Looking further into the future:
• I'm going to graduate and become a software engineer
• I'm going to work for an international company
• I'm going to continue learning new technologies
• I'm going to help my family
• I'm going to live in different countries and experience different cultures"

CONCLUSION:
"These are my plans for the future. I know it's going to be challenging,
but I'm going to work very hard to achieve my dreams. Thank you for listening!"

Q&A:
Q: "When exactly are you going to graduate?"
A: "I'm going to graduate in 2027."

Q: "Where are you going to work?"
A: "I'm going to try to work in a big tech company, maybe in another country."

Q: "Are you going to study abroad?"
A: "I hope so! I'm going to apply for exchange programs."
""")

print("\\n" + "=" * 70)
print("PRESENTATION CHECKLIST:")
print("=" * 70)
print("""
Before your presentation, make sure:
[OK] I'm going to speak for 3-5 minutes
[OK] I'm going to use 'going to' throughout
[OK] I'm going to make eye contact
[OK] I'm going to speak clearly
[OK] I'm going to show enthusiasm
[OK] I'm going to prepare for questions
[OK] I'm going to practice my presentation
""")"""))

    # Summary
    cells.append(nbf.v4.new_markdown_cell("""## Module 18 Complete! [COMPLETE]

### All Phases Completed!

**Phase 1 - Introduction:** [OK]
- Learned formation and uses of "going to"
- Studied affirmative, negative, and questions
- Understood plans, predictions, and intentions

**Phase 2 - Controlled Practice:** [OK]
- Completed 85+ exercises
- Practiced all forms and structures
- Mastered error correction

**Phase 3 - Meaningful Practice:** [OK]
- Completed 10 meaningful activities
- Applied "going to" in real contexts
- Planned future actions and goals

**Phase 4 - Communicative Practice:** [OK]
- Completed 8 communicative tasks
- Practiced in interactive scenarios
- Developed fluency and confidence

### What You Can Do Now:
[OK] Express future plans and intentions confidently
[OK] Make predictions based on evidence
[OK] Ask and answer questions about the future
[OK] Distinguish between "going to" and "will" (basic level)
[OK] Use "going to" naturally in conversation

### Next Module:
**Module 19: Will Future** - Learn to use "will" for spontaneous decisions, promises, predictions, and more!

Congratulations on completing Module 18! [TARGET]"""))

    cells.append(nbf.v4.new_code_cell("""# Module 18 completion summary
print("MODULE 18: GOING TO FUTURE - COMPLETION SUMMARY")
print("=" * 80)

completion_stats = {
    "Phase 1": {
        "name": "Introduction",
        "sections": 12,
        "cells": "40+",
        "status": "[OK] Complete"
    },
    "Phase 2": {
        "name": "Controlled Practice",
        "exercises": 85,
        "types": 10,
        "status": "[OK] Complete"
    },
    "Phase 3": {
        "name": "Meaningful Practice",
        "activities": 10,
        "contexts": "Personal plans, travel, career, predictions",
        "status": "[OK] Complete"
    },
    "Phase 4": {
        "name": "Communicative Practice",
        "tasks": 8,
        "types": "Interviews, role-plays, discussions, presentations",
        "status": "[OK] Complete"
    }
}

print("\\n[BOOK] LEARNING OUTCOMES ACHIEVED:\\n")
outcomes = [
    "Form 'going to' sentences correctly (affirmative, negative, questions)",
    "Express plans, intentions, and predictions with confidence",
    "Use appropriate time expressions with 'going to'",
    "Make predictions based on present evidence",
    "Distinguish basic differences between 'going to' and 'will'",
    "Avoid common mistakes with 'going to'",
    "Use 'going to' naturally in conversations",
    "Communicate about future plans fluently"
]

for i, outcome in enumerate(outcomes, 1):
    print(f"  {i}. [OK] {outcome}")

print("\\n" + "=" * 80)
print("[STATS] MODULE STATISTICS:")
print("=" * 80)

for phase, stats in completion_stats.items():
    print(f"\\n{phase}: {stats['name']} - {stats['status']}")
    for key, value in stats.items():
        if key not in ['name', 'status']:
            print(f"  • {key.capitalize()}: {value}")

print("\\n" + "=" * 80)
print("[TARGET] TOTAL MODULE CONTENT:")
print("=" * 80)
print(f"  • Introduction sections: 12")
print(f"  • Practice exercises: 85+")
print(f"  • Meaningful activities: 10")
print(f"  • Communicative tasks: 8")
print(f"  • Total learning time: 6-8 hours")

print("\\n" + "=" * 80)
print("* CONGRATULATIONS! YOU'VE COMPLETED MODULE 18!")
print("=" * 80)
print("\\nYou're now ready for Module 19: Will Future")
print("Keep up the excellent work! !")
print("=" * 80)"""))

    # Add all cells to notebook
    nb['cells'] = cells
    return nb

if __name__ == "__main__":
    notebook = create_notebook()
    output_path = "04_communicative_practice.ipynb"

    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(notebook, f)

    print(f"Notebook created successfully: {output_path}")
    print(f"Total cells: {len(notebook['cells'])}")
    print(f"Total tasks: 8")
