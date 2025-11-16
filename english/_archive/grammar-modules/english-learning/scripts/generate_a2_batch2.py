"""
A2 Level - Batch 2: Future & Time Structures
Generates Modules 6-10 with improved architecture
Data-driven approach with reusable components
"""

import os

import nbformat as nbf

# ============================================================================
# MODULE CONTENT CONFIGURATION
# ============================================================================

BATCH_2_MODULES = {
    "06": {
        "title": "Future: Going To vs Will Review",
        "subtitle": "Deep Dive into Future Forms",
        "time": "4-5 hours",
        "exercises": 85,
        "description": "Master the distinction between 'going to' and 'will' for different future contexts",
        "topics": [
            "Distinguish between 'going to' and 'will'",
            "Use 'going to' for pre-planned intentions and evidence-based predictions",
            "Use 'will' for spontaneous decisions, promises, and predictions",
            "Form questions and negatives accurately",
            "Choose appropriate future form based on context",
        ],
        "sections": 13,
        "activities": 10,
        "tasks": 8,
    },
    "07": {
        "title": "Present Continuous for Future Arrangements",
        "subtitle": "Definite Plans and Appointments",
        "time": "4-5 hours",
        "exercises": 85,
        "description": "Use present continuous to express fixed future arrangements and appointments",
        "topics": [
            "Understand present continuous for definite future arrangements",
            "Distinguish between present continuous for 'now' vs 'future'",
            "Form sentences about fixed plans with time markers",
            "Differentiate: present continuous vs going to vs will",
            "Use appropriate verbs for arrangements (meet, see, visit, fly)",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
    },
    "08": {
        "title": "Future Time Clauses (when, as soon as, until)",
        "subtitle": "Connecting Future Actions",
        "time": "5-6 hours",
        "exercises": 82,
        "description": "Master time clauses with future reference using present simple",
        "topics": [
            "Form complex sentences with future time clauses",
            "Apply rule: present tense in time clause, future in main clause",
            "Use when, as soon as, until, before, after correctly",
            "Understand sequence and timing relationships",
            "Avoid using 'will' in time clauses",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
    },
    "09": {
        "title": "Time Sequencing (before, after, then, finally)",
        "subtitle": "Organizing Events in Order",
        "time": "4-5 hours",
        "exercises": 83,
        "description": "Organize events and actions in logical chronological order",
        "topics": [
            "Organize events and actions in logical time order",
            "Use before, after, then, next, finally to show sequence",
            "Construct narratives with clear chronological flow",
            "Distinguish between conjunctions and adverbs",
            "Apply correct verb tenses when sequencing actions",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
    },
    "10": {
        "title": "Talking About Duration (for, since)",
        "subtitle": "Length of Time vs Starting Point",
        "time": "4-5 hours",
        "exercises": 84,
        "description": "Distinguish between 'for' (duration) and 'since' (starting point) with present perfect",
        "topics": [
            "Distinguish between 'for' (length) and 'since' (starting point)",
            "Use 'for' with time periods correctly",
            "Use 'since' with specific points in time",
            "Combine for/since with appropriate tenses",
            "Ask and answer 'How long...?' questions",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
    },
}

# ============================================================================
# REUSABLE CELL CREATION FUNCTIONS
# ============================================================================


def create_markdown_cell(content):
    """Create markdown cell with consistent formatting"""
    return nbf.v4.new_markdown_cell(content)


def create_code_cell(code):
    """Create code cell with consistent formatting"""
    return nbf.v4.new_code_cell(code)


def create_intro_header(module_num, module_data):
    """Create introduction notebook header"""
    content = f"""# Module {module_num}: {module_data['title']} - Phase 1: Introduction

## Learning Objectives
{chr(10).join('- ' + topic for topic in module_data['topics'])}

**Target Level:** A2
**Estimated Time:** {module_data['time']}"""
    return create_markdown_cell(content)


def create_practice_header(module_num, module_data, phase_name, phase_num):
    """Create practice phase header"""
    if phase_num == 2:
        overview = f"""{module_data['exercises']} exercises to master {module_data['title'].lower()}

**Total: {module_data['exercises']} exercises** *(Enhanced for stronger grammar foundation)*"""
    elif phase_num == 3:
        overview = f"""10 personalized activities using {module_data['title'].lower()}"""
    else:  # phase 4
        overview = f"""8 real-world communicative tasks"""

    content = f"""# Module {module_num}: {module_data['title']} - Phase {phase_num}: {phase_name}

## Overview
{overview}"""
    return create_markdown_cell(content)


def create_section_placeholder(section_num, section_title):
    """Create placeholder section for manual content addition"""
    cells = []

    md = f"""## {section_num}. {section_title}

[Content to be added: Detailed grammar explanation]

### Examples:
- Example 1
- Example 2
- Example 3
- Example 4

### Key Grammar Points:
- Point 1
- Point 2
- Point 3"""
    cells.append(create_markdown_cell(md))

    code = f"""# {section_title} - Practice
print("{section_title}")
print("=" * 60)

examples = [
    "Example sentence 1",
    "Example sentence 2",
    "Example sentence 3",
    "Example sentence 4"
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nYour turn: Create sentences using this grammar point")"""
    cells.append(create_code_cell(code))

    return cells


def create_exercise_set(set_num, set_name, count, description):
    """Create exercise set with validation framework"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Exercise Set {set_num}: {set_name} ({count} exercises)

**Focus:** {description}

### Instructions:
Complete all {count} exercises below. Check your answers at the end."""
        )
    )

    code = f"""# Exercise Set {set_num}: {set_name}
from projects.english_learning.utils.feedback_system import ExerciseValidator

validator = ExerciseValidator()
print("{set_name}")
print("=" * 60)

# {count} exercises
for i in range(1, {count} + 1):
    print(f"{{i}}. Exercise {{i}}: [Grammar exercise to be added]")

print("\\n[Detailed answers and explanations at end of notebook]")"""
    cells.append(create_code_cell(code))

    return cells


def create_activity(activity_num, activity_name):
    """Create meaningful practice activity"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Activity {activity_num}: {activity_name}

**Task:** [Description to be added]

### Instructions:
1. Write 8-10 sentences using the target grammar
2. Use affirmative, negative, and question forms
3. Include appropriate time expressions
4. Make it personal and specific

**Example:**
[Model answer to be added]"""
        )
    )

    code = f"""# Activity {activity_num}: {activity_name}
print("{activity_name}")
print("=" * 60)
print("\\nWrite your sentences below:")
print()

for j in range(1, 11):
    print(f"{{j}}. _________________________________")

print("\\nShare with a partner and compare!")"""
    cells.append(create_code_cell(code))

    return cells


def create_task(task_num, task_name):
    """Create communicative practice task"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Task {task_num}: {task_name}

**Objective:** [Description to be added]

### Instructions:
- Work in pairs or small groups
- Use target grammar throughout
- Ask and answer questions naturally
- Present findings to the class

**Time:** 15-20 minutes

### Language Focus:
- [Focus point 1]
- [Focus point 2]
- [Focus point 3]"""
        )
    )

    code = f"""# Task {task_num}: {task_name}
print("{task_name}")
print("=" * 60)
print("\\nUseful questions and prompts:")
print("- Question 1: [To be added]")
print("- Question 2: [To be added]")
print("- Question 3: [To be added]")
print("\\nPrepare and practice with your partner!")"""
    cells.append(create_code_cell(code))

    return cells


# ============================================================================
# MODULE GENERATION FUNCTIONS
# ============================================================================


def create_phase_1(module_num, module_data):
    """Generate Phase 1: Introduction notebook"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"
    os.makedirs(base_path, exist_ok=True)

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_intro_header(module_num, module_data))

    # Generate section placeholders
    section_titles = [
        "Introduction and Overview",
        "Formation - Affirmative",
        "Formation - Negative",
        "Formation - Questions",
        "Short Answers",
        "Key Uses and Contexts",
        "Time Expressions",
        "Comparison with Other Forms",
        "Position and Word Order",
        "Common Collocations",
        "Pronunciation and Contractions",
        "Common Mistakes",
        "Practice Conversations",
    ]

    for i, title in enumerate(section_titles[: module_data["sections"]], 1):
        cells.extend(create_section_placeholder(i, title))

    nb["cells"] = cells
    with open(f"{base_path}/01_introduction.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def create_phase_2(module_num, module_data):
    """Generate Phase 2: Controlled Practice notebook"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_practice_header(module_num, module_data, "Controlled Practice", 2))

    # Generate exercise sets (distribute exercises across 10 sets)
    total_ex = module_data["exercises"]
    exercises_per_set = total_ex // 10
    remainder = total_ex % 10

    exercise_sets = [
        ("Formation - Affirmative", "Create affirmative sentences"),
        ("Formation - Negative", "Create negative sentences"),
        ("Formation - Questions", "Form questions correctly"),
        ("Short Answers", "Give appropriate short answers"),
        ("Error Correction", "Find and correct mistakes"),
        ("Gap Filling", "Complete with correct forms"),
        ("Sentence Transformation", "Convert between forms"),
        ("Context Matching", "Choose appropriate form for context"),
        ("Time Expression Usage", "Use time markers correctly"),
        ("Mixed Practice", "Apply all skills together"),
    ]

    for i, (name, desc) in enumerate(exercise_sets, 1):
        count = exercises_per_set + (1 if i <= remainder else 0)
        cells.extend(create_exercise_set(i, name, count, desc))

    nb["cells"] = cells
    with open(f"{base_path}/02_controlled_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def create_phase_3(module_num, module_data):
    """Generate Phase 3: Meaningful Practice notebook"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_practice_header(module_num, module_data, "Meaningful Practice", 3))

    # Generate activities
    activity_names = [
        "Personal Experience 1",
        "Personal Experience 2",
        "Daily Life Application",
        "Future Plans",
        "Past Events",
        "Expressing Opinions",
        "Describing Situations",
        "Making Comparisons",
        "Telling Stories",
        "Creative Writing",
    ]

    for i, name in enumerate(activity_names[: module_data["activities"]], 1):
        cells.extend(create_activity(i, name))

    nb["cells"] = cells
    with open(f"{base_path}/03_meaningful_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def create_phase_4(module_num, module_data):
    """Generate Phase 4: Communicative Practice notebook"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_practice_header(module_num, module_data, "Communicative Practice", 4))

    # Generate tasks
    task_names = [
        "Pair Interview",
        "Role-Play Scenario",
        "Group Discussion",
        "Information Gap Activity",
        "Problem Solving Task",
        "Presentation Activity",
        "Collaborative Project",
        "Real-World Simulation",
    ]

    for i, name in enumerate(task_names[: module_data["tasks"]], 1):
        cells.extend(create_task(i, name))

    nb["cells"] = cells
    with open(f"{base_path}/04_communicative_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def create_module_all_phases(module_num, module_data):
    """Create all 4 phases for a module"""
    print(f"\nCreating Module {module_num}: {module_data['title']}...")

    create_phase_1(module_num, module_data)
    print(f"  [OK] Phase 1 created")

    create_phase_2(module_num, module_data)
    print(f"  [OK] Phase 2 created ({module_data['exercises']} exercises)")

    create_phase_3(module_num, module_data)
    print(f"  [OK] Phase 3 created ({module_data['activities']} activities)")

    create_phase_4(module_num, module_data)
    print(f"  [OK] Phase 4 created ({module_data['tasks']} tasks)")

    return f"Module {module_num} created successfully"


# ============================================================================
# MAIN EXECUTION
# ============================================================================


def main():
    """Generate all A2 Batch 2 modules"""
    print("=" * 70)
    print("A2 LEVEL - BATCH 2: FUTURE & TIME STRUCTURES")
    print("Generating Modules 06-10")
    print("=" * 70)

    # Ensure A2 directory exists
    os.makedirs("projects/english-learning/notebooks/A2", exist_ok=True)

    # Generate each module
    for module_num, module_data in BATCH_2_MODULES.items():
        try:
            result = create_module_all_phases(module_num, module_data)
            print(f"  [SUCCESS] {result}")
        except Exception as e:
            print(f"  [ERROR] Failed to create Module {module_num}: {e}")
            raise

    print("\n" + "=" * 70)
    print("ALL 5 MODULES CREATED SUCCESSFULLY!")
    print("=" * 70)

    # Summary
    print("\nSummary:")
    print("-" * 70)
    print("Total Modules: 5")
    print("Total Notebooks: 20 (5 modules x 4 phases)")
    print("Total Exercises: 419 (enhanced grammar foundation)")
    print("Target Level: A2")
    print("Focus: Future & Time Structures")
    print("\nImprovement Features:")
    print("- Data-driven configuration")
    print("- Reusable component functions")
    print("- Consistent structure across all modules")
    print("- Ready for content enhancement")
    print("\nNext Steps:")
    print("1. Add detailed content to Phase 1 sections")
    print("2. Add specific exercises to Phase 2 sets")
    print("3. Enhance Phase 3 activity descriptions")
    print("4. Complete Phase 4 task scenarios")
    print("5. Test Module 06 Phase 1")
    print("=" * 70)


if __name__ == "__main__":
    main()
