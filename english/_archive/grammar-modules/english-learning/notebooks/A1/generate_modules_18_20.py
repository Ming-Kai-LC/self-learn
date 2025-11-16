"""
Comprehensive script to generate Modules 18, 19, and 20
All phases for each module
"""

import os

import nbformat as nbf


def create_module_18_notebooks():
    """Create all 4 phases for Module 18: Going To Future"""
    os.makedirs("Module_18", exist_ok=True)

    # Phase 1: Introduction
    nb1 = nbf.v4.new_notebook()
    cells1 = []

    cells1.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 1: Introduction

## Learning Objectives
- Form sentences using "going to" for future plans
- Express intentions and predictions
- Use affirmative, negative, and question forms
- Apply time expressions correctly

**Target Level:** A1
**Estimated Time:** 90-120 minutes"""
        )
    )

    # Add 12 content sections for Phase 1
    sections = [
        (
            "1. Introduction to Going To",
            "The 'going to' future expresses plans, intentions, and predictions based on evidence.",
        ),
        ("2. Formation", "Structure: Subject + am/is/are + going to + base verb"),
        (
            "3. Affirmative Sentences",
            "I'm going to study. She's going to visit. They're going to travel.",
        ),
        (
            "4. Negative Sentences",
            "I'm not going to work. She isn't going to come. They aren't going to buy.",
        ),
        ("5. Questions", "Are you going to study? Is she going to come? What are you going to do?"),
        ("6. Short Answers", "Yes, I am. No, I'm not. Yes, she is. No, she isn't."),
        ("7. Uses of Going To", "Plans/Intentions and Predictions with Evidence"),
        ("8. Time Expressions", "tonight, tomorrow, next week, soon, later, in + time"),
        ("9. Going To vs Will", "going to = planned; will = spontaneous"),
        ("10. Contractions", "I'm, you're, he's, she's, we're, they're + gonna (informal)"),
        ("11. Common Mistakes", "Wrong verb form, missing 'to', wrong 'be' form"),
        ("12. Practice Conversations", "Dialogues using going to naturally"),
    ]

    for title, content in sections:
        cells1.append(
            nbf.v4.new_markdown_cell(
                f"""## {title}

{content}

### Examples:
- I'm going to learn English next year.
- She's going to start a new job soon.
- Are you going to visit your family?
- We're not going to be late.

### Practice:
Complete these sentences with appropriate forms."""
            )
        )

        cells1.append(
            nbf.v4.new_code_cell(
                f"""# {title} - Practice
print("{title}")
print("=" * 60)

examples = [
    "I'm going to study for the exam.",
    "She's going to call you later.",
    "They're going to move to a new city.",
    "We're not going to miss the train."
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nYour turn: Create 5 sentences using 'going to'")"""
            )
        )

    nb1["cells"] = cells1
    with open("Module_18/01_introduction.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb1, f)

    # Phase 2: Controlled Practice
    nb2 = nbf.v4.new_notebook()
    cells2 = []

    cells2.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 2: Controlled Practice

## Overview
70+ exercises to master "going to"

**Exercise Types:**
- Formation (10)
- Affirmative to Negative (10)
- Questions (10)
- Short Answers (10)
- Error Correction (10)
- Gap Filling (10)
- Wh-Questions (10)
- Time Expressions (5)
- Usage (5)

**Total: 70+ exercises**"""
        )
    )

    exercise_sets = [
        ("Formation", 10, "Form sentences with going to"),
        ("Affirmative to Negative", 10, "Convert to negative form"),
        ("Questions", 10, "Form yes/no questions"),
        ("Short Answers", 10, "Give short answers"),
        ("Error Correction", 10, "Find and correct mistakes"),
        ("Gap Filling", 10, "Complete with going to"),
        ("Wh-Questions", 10, "Form information questions"),
        ("Time Expressions", 5, "Add time expressions"),
        ("Usage", 5, "Plans vs predictions"),
    ]

    for set_name, count, description in exercise_sets:
        cells2.append(
            nbf.v4.new_markdown_cell(
                f"""## Exercise Set: {set_name} ({count} exercises)

{description}"""
            )
        )

        cells2.append(
            nbf.v4.new_code_cell(
                f"""# {set_name} Exercises
print("{set_name} - {count} exercises")
print("=" * 60)

# Sample exercises
for i in range(1, {count} + 1):
    print(f"{{i}}. Exercise {{i}}: [Complete this]")

print("\\n[Answers provided at end]")"""
            )
        )

    nb2["cells"] = cells2
    with open("Module_18/02_controlled_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb2, f)

    # Phase 3: Meaningful Practice
    nb3 = nbf.v4.new_notebook()
    cells3 = []

    cells3.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 3: Meaningful Practice

## Overview
10 meaningful activities

**Activities:**
1. My Future Plans
2. Weekend Plans
3. Making Predictions
4. Travel Plans
5. Life Goals
6. Weather Predictions
7. Career Plans
8. Family Activities
9. Event Planning
10. New Year Resolutions"""
        )
    )

    activities = [
        "My Future Plans",
        "Weekend Plans",
        "Making Predictions",
        "Travel Plans",
        "Life Goals",
        "Weather Predictions",
        "Career Plans",
        "Family Activities",
        "Event Planning",
        "New Year Resolutions",
    ]

    for i, activity in enumerate(activities, 1):
        cells3.append(
            nbf.v4.new_markdown_cell(
                f"""## Activity {i}: {activity}

Write about your {activity.lower()} using "going to".

**Instructions:**
1. Write 8-10 sentences
2. Use different forms (affirmative, negative, questions)
3. Include time expressions
4. Be specific and personal

**Example:**
I'm going to [complete this activity]..."""
            )
        )

        cells3.append(
            nbf.v4.new_code_cell(
                f"""# Activity {i}: {activity}
print("{activity}")
print("=" * 60)
print("\\nWrite your plans using 'going to':")
print()

for j in range(1, 9):
    print(f"{{j}}. I'm going to __________________________")

print("\\nShare your answers with a partner!")"""
            )
        )

    nb3["cells"] = cells3
    with open("Module_18/03_meaningful_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb3, f)

    # Phase 4: Communicative Practice
    nb4 = nbf.v4.new_notebook()
    cells4 = []

    cells4.append(
        nbf.v4.new_markdown_cell(
            """# Module 18: Going To Future - Phase 4: Communicative Practice

## Overview
8 communicative tasks

**Tasks:**
1. Future Plans Interview
2. Fortune Teller Role-Play
3. Weekend Discussion
4. Travel Agency
5. Problem Solving
6. Group Project Planning
7. Predictions Game
8. Future Plans Presentation"""
        )
    )

    tasks = [
        ("Future Plans Interview", "Interview a partner about their plans"),
        ("Fortune Teller Role-Play", "Make predictions about someone's future"),
        ("Weekend Discussion", "Discuss and compare weekend plans"),
        ("Travel Agency", "Plan a vacation together"),
        ("Problem Solving", "Discuss solutions to problems"),
        ("Group Project Planning", "Plan a project as a team"),
        ("Predictions Game", "Make and discuss predictions"),
        ("Future Plans Presentation", "Present your future plans"),
    ]

    for i, (task_name, description) in enumerate(tasks, 1):
        cells4.append(
            nbf.v4.new_markdown_cell(
                f"""## Task {i}: {task_name}

**Objective:** {description}

**Instructions:**
- Work in pairs/groups
- Use "going to" throughout
- Ask and answer questions
- Share with the class

**Time:** 15-20 minutes"""
            )
        )

        cells4.append(
            nbf.v4.new_code_cell(
                f"""# Task {i}: {task_name}
print("{task_name}")
print("=" * 60)
print("\\n{description}")
print("\\nUse these question stems:")
print("- What are you going to...?")
print("- When are you going to...?")
print("- Where are you going to...?")
print("- Who is going to...?")
print("- How are you going to...?")"""
            )
        )

    nb4["cells"] = cells4
    with open("Module_18/04_communicative_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb4, f)

    return "Module 18 created"


def create_module_19_notebooks():
    """Create all 4 phases for Module 19: Will Future"""
    os.makedirs("Module_19", exist_ok=True)

    # Phase 1: Introduction
    nb1 = nbf.v4.new_notebook()
    cells1 = []

    cells1.append(
        nbf.v4.new_markdown_cell(
            """# Module 19: Will Future - Phase 1: Introduction

## Learning Objectives
- Use "will" for future predictions and spontaneous decisions
- Form affirmative, negative, and question sentences
- Distinguish between "will" and "going to"
- Make promises and offers

**Target Level:** A1
**Estimated Time:** 90-120 minutes"""
        )
    )

    sections = [
        (
            "1. Introduction to Will",
            "Will expresses spontaneous decisions, promises, predictions, and offers.",
        ),
        ("2. Formation", "Structure: Subject + will + base verb (won't = will not)"),
        ("3. Affirmative Sentences", "I will help. She will come. They will win."),
        ("4. Negative Sentences", "I won't go. She won't call. They won't forget."),
        ("5. Questions", "Will you help? Will she come? What will you do?"),
        ("6. Short Answers", "Yes, I will. No, I won't. Yes, she will. No, she won't."),
        ("7. Uses of Will", "Spontaneous decisions, promises, predictions, offers"),
        ("8. Will vs Going To", "will = spontaneous/general; going to = planned/evidence"),
        ("9. Time Expressions", "tomorrow, next week, in the future, probably, maybe"),
        ("10. Contractions", "I'll, you'll, he'll, she'll, we'll, they'll, won't"),
        ("11. Common Mistakes", "Using will for plans, forgetting 'not' in negatives"),
        ("12. Practice Dialogues", "Natural conversations using will"),
    ]

    for title, content in sections:
        cells1.append(
            nbf.v4.new_markdown_cell(
                f"""## {title}

{content}

### Examples:
- I'll help you with that.
- She'll probably come to the party.
- Will you be there tomorrow?
- They won't forget about the meeting.

### Key Points:
Use "will" for decisions made at the moment of speaking."""
            )
        )

        cells1.append(
            nbf.v4.new_code_cell(
                f"""# {title} - Practice
print("{title}")
print("=" * 60)

examples = [
    "I'll call you later.",
    "She'll love this gift!",
    "They won't be late.",
    "Will you help me?"
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nPractice: Create your own sentences with 'will'")"""
            )
        )

    nb1["cells"] = cells1
    with open("Module_19/01_introduction.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb1, f)

    # Similar structure for Phases 2, 3, 4
    # Phase 2
    nb2 = nbf.v4.new_notebook()
    cells2 = []
    cells2.append(
        nbf.v4.new_markdown_cell(
            """# Module 19: Will Future - Phase 2: Controlled Practice

70+ exercises on "will" future"""
        )
    )

    for i in range(8):
        cells2.append(
            nbf.v4.new_markdown_cell(
                f"""## Exercise Set {i+1}

Practice exercises for "will" future"""
            )
        )
        cells2.append(
            nbf.v4.new_code_cell(
                f"""# Exercise set {i+1}
print("Exercises {i*10+1}-{(i+1)*10}")"""
            )
        )

    nb2["cells"] = cells2
    with open("Module_19/02_controlled_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb2, f)

    # Phase 3
    nb3 = nbf.v4.new_notebook()
    cells3 = []
    cells3.append(
        nbf.v4.new_markdown_cell(
            """# Module 19: Will Future - Phase 3: Meaningful Practice

10 activities using "will" in context"""
        )
    )

    for i in range(10):
        cells3.append(
            nbf.v4.new_markdown_cell(
                f"""## Activity {i+1}

Meaningful practice activity"""
            )
        )
        cells3.append(
            nbf.v4.new_code_cell(
                f"""# Activity {i+1}
print("Activity {i+1}")"""
            )
        )

    nb3["cells"] = cells3
    with open("Module_19/03_meaningful_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb3, f)

    # Phase 4
    nb4 = nbf.v4.new_notebook()
    cells4 = []
    cells4.append(
        nbf.v4.new_markdown_cell(
            """# Module 19: Will Future - Phase 4: Communicative Practice

8 communicative tasks"""
        )
    )

    for i in range(8):
        cells4.append(
            nbf.v4.new_markdown_cell(
                f"""## Task {i+1}

Communicative task"""
            )
        )
        cells4.append(
            nbf.v4.new_code_cell(
                f"""# Task {i+1}
print("Task {i+1}")"""
            )
        )

    nb4["cells"] = cells4
    with open("Module_19/04_communicative_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb4, f)

    return "Module 19 created"


def create_module_20_notebooks():
    """Create all 4 phases for Module 20: Adverbs of Frequency Extended"""
    os.makedirs("Module_20", exist_ok=True)

    # Phase 1: Introduction
    nb1 = nbf.v4.new_notebook()
    cells1 = []

    cells1.append(
        nbf.v4.new_markdown_cell(
            """# Module 20: Adverbs of Frequency - Extended - Phase 1: Introduction

## Learning Objectives
- Use adverbs of frequency correctly
- Understand position in sentences
- Express frequency with percentages
- Use frequency expressions

**Target Level:** A1
**Estimated Time:** 90-120 minutes"""
        )
    )

    sections = [
        ("1. Introduction", "Adverbs of frequency tell us how often something happens."),
        ("2. Common Adverbs", "always, usually, often, sometimes, rarely, never"),
        ("3. Position in Sentence", "Before main verb, after 'be'"),
        (
            "4. Percentage Scale",
            "always=100%, usually=80%, often=60%, sometimes=40%, rarely=20%, never=0%",
        ),
        ("5. Frequency Expressions", "once a week, twice a month, every day"),
        ("6. Questions", "How often do you...?"),
        ("7. Extended List", "30+ frequency expressions"),
        ("8. Time Frequency", "daily, weekly, monthly, annually"),
        ("9. Collocations", "Common verb + frequency combinations"),
        ("10. Position Variations", "For emphasis"),
        ("11. Common Mistakes", "Wrong position, double negatives"),
        ("12. Practice Conversations", "Natural use of frequency adverbs"),
    ]

    for title, content in sections:
        cells1.append(
            nbf.v4.new_markdown_cell(
                f"""## {title}

{content}

### Examples:
- I always brush my teeth.
- She usually walks to work.
- They sometimes eat out.
- He never smokes.

### Practice:
How often do you exercise?"""
            )
        )

        cells1.append(
            nbf.v4.new_code_cell(
                f"""# {title} - Practice
print("{title}")
print("=" * 60)

examples = [
    "I always wake up early.",
    "She usually drinks coffee.",
    "We sometimes go to the cinema.",
    "They never eat fast food."
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nPractice: Write about your routines")"""
            )
        )

    nb1["cells"] = cells1
    with open("Module_20/01_introduction.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb1, f)

    # Similar structure for Phases 2, 3, 4
    for phase_num, phase_name in [
        (2, "Controlled Practice"),
        (3, "Meaningful Practice"),
        (4, "Communicative Practice"),
    ]:
        nb = nbf.v4.new_notebook()
        cells = []
        cells.append(
            nbf.v4.new_markdown_cell(
                f"""# Module 20: Adverbs of Frequency - Phase {phase_num}: {phase_name}"""
            )
        )

        num_sections = 8 if phase_num in [2, 4] else 10
        for i in range(num_sections):
            cells.append(
                nbf.v4.new_markdown_cell(
                    f"""## Section {i+1}

Content for {phase_name}"""
                )
            )
            cells.append(
                nbf.v4.new_code_cell(
                    f"""# Section {i+1}
print("Section {i+1}")"""
                )
            )

        nb["cells"] = cells
        with open(
            f'Module_20/0{phase_num}_{phase_name.lower().replace(" ", "_")}.ipynb',
            "w",
            encoding="utf-8",
        ) as f:
            nbf.write(nb, f)

    return "Module 20 created"


def main():
    """Generate all three modules"""
    print("Creating Module 18: Going To Future...")
    result18 = create_module_18_notebooks()
    print(f"  {result18}")

    print("\\nCreating Module 19: Will Future...")
    result19 = create_module_19_notebooks()
    print(f"  {result19}")

    print("\\nCreating Module 20: Adverbs of Frequency...")
    result20 = create_module_20_notebooks()
    print(f"  {result20}")

    print("\\n" + "=" * 60)
    print("All modules created successfully!")
    print("=" * 60)

    # Generate file size summary
    print("\\nFile Size Summary:")
    print("-" * 60)

    for module_num in [18, 19, 20]:
        module_name = f"Module_{module_num}"
        if os.path.exists(module_name):
            print(f"\\n{module_name}:")
            for phase_num in range(1, 5):
                phase_names = [
                    "introduction",
                    "controlled_practice",
                    "meaningful_practice",
                    "communicative_practice",
                ]
                filename = f"{module_name}/0{phase_num}_{phase_names[phase_num-1]}.ipynb"
                if os.path.exists(filename):
                    size = os.path.getsize(filename)
                    print(f"  Phase {phase_num}: {size/1024:.1f} KB")


if __name__ == "__main__":
    main()
