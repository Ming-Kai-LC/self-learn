"""
A2 Level - Batch 3: Modal Verbs
Generates Modules 11-15 with enhanced modal-specific architecture
Data-driven approach with modal verb validation and specialized templates
"""

import os

import nbformat as nbf

# ============================================================================
# MODAL VERB CHARACTERISTICS
# ============================================================================

MODAL_CHARACTERISTICS = {
    "common_features": [
        "No -s in third person (he should, NOT he shoulds)",
        "Followed by base verb (should go, NOT should to go)",
        "No 'to' before the modal (NOT to should)",
        "Questions: Modal + subject + base verb",
        "Negatives: Modal + not + base verb",
    ],
    "contractions": {
        "should not": "shouldn't",
        "must not": "mustn't",
        "cannot": "can't",
        "could not": "couldn't",
        "would not": "wouldn't",
        "may not": "may not (no contraction)",
        "might not": "mightn't (rare)",
    },
}

# ============================================================================
# MODULE CONTENT CONFIGURATION
# ============================================================================

BATCH_3_MODULES = {
    "11": {
        "title": "Should/Shouldn't - Advice and Recommendations",
        "subtitle": "Giving Advice and Making Suggestions",
        "time": "4-5 hours",
        "exercises": 80,
        "description": "Master 'should' and 'shouldn't' for giving advice, making recommendations, and expressing opinions",
        "topics": [
            "Form affirmative and negative sentences with should/shouldn't",
            "Use should/shouldn't to give advice and recommendations",
            "Form questions with should and give appropriate responses",
            "Express opinions about what is right or wrong",
            "Distinguish between strong obligation (must) and advice (should)",
        ],
        "sections": 13,
        "activities": 10,
        "tasks": 8,
        "modal_focus": "should/shouldn't",
        "key_uses": ["advice", "recommendations", "opinions", "suggestions"],
    },
    "12": {
        "title": "Must/Have To - Obligation and Necessity",
        "subtitle": "Expressing Rules and Requirements",
        "time": "5-6 hours",
        "exercises": 85,
        "description": "Understand must and have to for expressing obligation, rules, and necessity",
        "topics": [
            "Form sentences with must and have to for obligations",
            "Distinguish between must (internal obligation) and have to (external rules)",
            "Use has to/have to correctly with different subjects",
            "Form questions and negatives with have to (do/does + have to)",
            "Understand when to use must vs have to in context",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "modal_focus": "must/have to",
        "key_uses": ["obligation", "necessity", "rules", "requirements"],
    },
    "13": {
        "title": "Don't Have To vs Mustn't - No Obligation vs Prohibition",
        "subtitle": "Understanding the Critical Difference",
        "time": "4-5 hours",
        "exercises": 82,
        "description": "Master the crucial distinction between 'don't have to' (no obligation) and 'mustn't' (prohibition)",
        "topics": [
            "Understand don't have to = not necessary (no obligation)",
            "Understand mustn't = prohibited (not allowed)",
            "Recognize the critical meaning difference between the two",
            "Use the correct form based on context (rules vs freedom)",
            "Form sentences expressing lack of obligation vs prohibition",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
        "modal_focus": "don't have to/mustn't",
        "key_uses": ["no obligation", "prohibition", "not necessary", "not allowed"],
    },
    "14": {
        "title": "May/Might/Could - Possibility and Permission",
        "subtitle": "Expressing Uncertainty and Asking Permission",
        "time": "5-6 hours",
        "exercises": 84,
        "description": "Use may, might, and could for expressing possibility, making predictions, and asking permission",
        "topics": [
            "Express possibility and uncertainty with may/might/could",
            "Use may and could for polite permission requests",
            "Understand the subtle differences between may/might/could",
            "Make predictions about present and future situations",
            "Form questions and negatives appropriately",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "modal_focus": "may/might/could",
        "key_uses": ["possibility", "permission", "predictions", "uncertainty"],
    },
    "15": {
        "title": "Would Like - Polite Requests and Preferences",
        "subtitle": "Expressing Wants and Desires Politely",
        "time": "4-5 hours",
        "exercises": 85,
        "description": "Master 'would like' for polite requests, preferences, and invitations",
        "topics": [
            "Form sentences with would like + noun and would like to + verb",
            "Distinguish between would like (polite) and want (direct)",
            "Make polite offers and invitations using would like",
            "Form questions: Would you like...? / What would you like?",
            "Use contractions: I'd like, you'd like, he'd like",
        ],
        "sections": 13,
        "activities": 10,
        "tasks": 8,
        "modal_focus": "would like",
        "key_uses": ["polite requests", "preferences", "offers", "invitations"],
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


def validate_modal_sentence(sentence, modal):
    """Validation helper for modal verb sentences"""
    checks = {
        "has_modal": modal.lower() in sentence.lower(),
        "no_to_after_modal": f"{modal} to" not in sentence.lower(),
        "no_s_on_modal": f"{modal}s " not in sentence.lower(),
    }
    return all(checks.values()), checks


def create_intro_header(module_num, module_data):
    """Create introduction notebook header with modal-specific info"""
    content = f"""# Module {module_num}: {module_data['title']} - Phase 1: Introduction

## Learning Objectives
{chr(10).join('- ' + topic for topic in module_data['topics'])}

**Target Level:** A2
**Estimated Time:** {module_data['time']}
**Modal Focus:** {module_data['modal_focus']}

## Important Modal Verb Rules

All modal verbs share these characteristics:
{chr(10).join('- ' + rule for rule in MODAL_CHARACTERISTICS['common_features'])}"""
    return create_markdown_cell(content)


def create_practice_header(module_num, module_data, phase_name, phase_num):
    """Create practice phase header"""
    if phase_num == 2:
        overview = f"""{module_data['exercises']} exercises to master {module_data['modal_focus']}

**Total: {module_data['exercises']} exercises** *(Enhanced for modal verb accuracy)*
**Focus:** {', '.join(module_data['key_uses'])}"""
    elif phase_num == 3:
        overview = (
            f"""10 personalized activities using {module_data['modal_focus']} in real contexts"""
        )
    else:  # phase 4
        overview = (
            f"""8 real-world communicative tasks focusing on {', '.join(module_data['key_uses'])}"""
        )

    content = f"""# Module {module_num}: {module_data['title']} - Phase {phase_num}: {phase_name}

## Overview
{overview}"""
    return create_markdown_cell(content)


def create_modal_section_placeholder(section_num, section_title, modal_focus):
    """Create placeholder section with modal-specific examples"""
    cells = []

    md = f"""## {section_num}. {section_title}

[Content to be added: Detailed grammar explanation]

### Examples with {modal_focus}:
- Example 1: [Affirmative sentence]
- Example 2: [Negative sentence]
- Example 3: [Question]
- Example 4: [Short answer]

### Key Grammar Points:
- **Formation:** {modal_focus} + base verb (NO 'to', NO -s)
- **Meaning:** [Specific use to be added]
- **Context:** [When to use this modal]

### Common Mistakes to Avoid:
- ❌ WRONG: [Common error example]
- ✅ CORRECT: [Corrected version]"""
    cells.append(create_markdown_cell(md))

    code = f"""# {section_title} - Practice
print("{section_title}")
print("=" * 60)

examples = [
    "Example sentence 1 with {modal_focus}",
    "Example sentence 2 with {modal_focus}",
    "Example sentence 3 with {modal_focus}",
    "Example sentence 4 with {modal_focus}"
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nYour turn: Create sentences using {modal_focus}")
print("Remember: {modal_focus} + base verb (no 'to', no -s)")"""
    cells.append(create_code_cell(code))

    return cells


def create_exercise_set(set_num, set_name, count, description, modal_focus):
    """Create exercise set with modal-specific validation"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Exercise Set {set_num}: {set_name} ({count} exercises)

**Focus:** {description}
**Modal:** {modal_focus}

### Instructions:
Complete all {count} exercises below. Pay attention to modal verb rules!

**Remember:**
- Use base verb after {modal_focus}
- No -s in third person
- Check word order in questions"""
        )
    )

    code = f"""# Exercise Set {set_num}: {set_name}
from projects.english_learning.utils.feedback_system import ExerciseValidator

validator = ExerciseValidator()
print("{set_name}")
print("=" * 60)

# {count} exercises with {modal_focus}
for i in range(1, {count} + 1):
    print(f"{{i}}. Exercise {{i}}: [Modal verb exercise to be added]")

print("\\n[Detailed answers and explanations at end of notebook]")
print("\\nValidation tip: Check that {modal_focus} is followed by base verb!")"""
    cells.append(create_code_cell(code))

    return cells


def create_modal_activity(activity_num, activity_name, modal_focus, use_case):
    """Create meaningful practice activity with modal-specific context"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Activity {activity_num}: {activity_name}

**Modal Focus:** {modal_focus}
**Context:** {use_case}

### Instructions:
1. Write 8-10 sentences using {modal_focus}
2. Use affirmative, negative, and question forms
3. Make it personal and realistic
4. Check: base verb after modal (no -s, no 'to')

**Example:**
[Model answer using {modal_focus} to be added]"""
        )
    )

    code = f"""# Activity {activity_num}: {activity_name}
print("{activity_name}")
print("=" * 60)
print(f"\\nUse {modal_focus} to talk about: {use_case}")
print("\\nWrite your sentences below:")
print()

for j in range(1, 11):
    print(f"{{j}}. _________________________________")

print("\\nRemember: {modal_focus} + base verb!")"""
    cells.append(create_code_cell(code))

    return cells


def create_modal_task(task_num, task_name, modal_focus, communicative_goal):
    """Create communicative practice task with modal-specific goal"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Task {task_num}: {task_name}

**Modal Focus:** {modal_focus}
**Communicative Goal:** {communicative_goal}

### Instructions:
- Work in pairs or small groups
- Use {modal_focus} throughout the activity
- Focus on natural communication
- Present findings to the class

**Time:** 15-20 minutes

### Language Focus:
- Use {modal_focus} for {communicative_goal}
- Ask and answer questions naturally
- Give reasons for your answers"""
        )
    )

    code = f"""# Task {task_num}: {task_name}
print("{task_name}")
print("=" * 60)
print(f"\\nCommunicative Goal: {communicative_goal}")
print(f"\\nUseful {modal_focus} questions:")
print("- Question 1: [To be added]")
print("- Question 2: [To be added]")
print("- Question 3: [To be added]")
print("\\nPrepare and practice with your partner!")"""
    cells.append(create_code_cell(code))

    return cells


# ============================================================================
# MODULE-SPECIFIC SECTION TITLES
# ============================================================================

SECTION_TITLES_BY_MODULE = {
    "11": [  # Should/Shouldn't
        "Introduction to Should/Shouldn't",
        "Formation - Affirmative (should + base verb)",
        "Formation - Negative (shouldn't + base verb)",
        "Formation - Questions (Should + subject + base verb?)",
        "Short Answers (Yes, I should / No, I shouldn't)",
        "Giving Advice and Recommendations",
        "Expressing Opinions (I think you should...)",
        "Making Suggestions (We should...)",
        "Should vs Must - Advice vs Obligation",
        "Common Collocations with Should",
        "Pronunciation and Contractions",
        "Common Mistakes with Should",
        "Practice Conversations - Giving Advice",
    ],
    "12": [  # Must/Have To
        "Introduction to Must and Have To",
        "Formation - Must + base verb",
        "Formation - Have to / Has to + base verb",
        "Must vs Have to - Internal vs External Obligation",
        "Negatives - Must not vs Don't have to (Preview)",
        "Questions with Have to (Do/Does... have to?)",
        "Short Answers",
        "Expressing Rules and Requirements",
        "Talking About Necessity",
        "Personal Obligations vs External Rules",
        "Common Collocations",
        "Pronunciation - Have to /hæftə/",
        "Common Mistakes with Must/Have to",
        "Register and Formality",
        "Practice Conversations - Rules and Obligations",
    ],
    "13": [  # Don't Have To vs Mustn't
        "Introduction - The Critical Difference",
        "Don't Have To = Not Necessary (No Obligation)",
        "Mustn't = Prohibited (Not Allowed)",
        "Formation - Don't/Doesn't have to",
        "Formation - Must not / Mustn't",
        "Meaning Contrast - Freedom vs Prohibition",
        "Context Clues - Which One to Use?",
        "Common Situations - No Obligation",
        "Common Situations - Prohibition",
        "Pronunciation and Contractions",
        "Common Mistakes and Confusions",
        "Practice with Rules and Signs",
        "Comparison Chart - Summary",
        "Practice Conversations - Rules at School/Work",
    ],
    "14": [  # May/Might/Could
        "Introduction to May/Might/Could",
        "Formation - Affirmative (may/might/could + base verb)",
        "Formation - Negative (may not/might not/couldn't)",
        "Expressing Possibility (50-50 chance)",
        "Making Predictions about Present",
        "Making Predictions about Future",
        "Asking Permission - May I / Could I?",
        "Giving Permission - You may / You can",
        "Subtle Differences - May vs Might vs Could",
        "Certainty Scale (must → may/might/could → can't)",
        "Common Collocations",
        "Pronunciation",
        "Common Mistakes",
        "Register - Formality Levels",
        "Practice Conversations - Possibilities and Permission",
    ],
    "15": [  # Would Like
        "Introduction to Would Like",
        "Formation - Would like + noun",
        "Formation - Would like to + verb",
        "Contractions - I'd like, you'd like, he'd like",
        "Questions - Would you like...?",
        "Questions - What would you like?",
        "Short Answers",
        "Would Like vs Want - Politeness",
        "Making Polite Requests",
        "Making Offers and Invitations",
        "Responding to Offers",
        "Common Collocations",
        "Common Mistakes",
    ],
}

ACTIVITY_NAMES_BY_MODULE = {
    "11": [
        "Give Advice to a Friend",
        "Health and Lifestyle Recommendations",
        "Study Tips and Suggestions",
        "Travel Advice",
        "Career Recommendations",
        "Should I or Shouldn't I? - Personal Decisions",
        "Advice Column",
        "Environmental Suggestions",
        "Friendship Advice",
        "Self-Improvement Goals",
    ],
    "12": [
        "School/Work Rules and Obligations",
        "Personal Responsibilities",
        "Family Obligations",
        "Travel Requirements",
        "Health and Safety Must-dos",
        "Legal Obligations in Your Country",
        "Must vs Have to - Your Life",
        "Daily Necessities",
        "Professional Requirements",
        "Cultural Obligations",
    ],
    "13": [
        "Understanding Signs and Rules",
        "Freedoms and Prohibitions at School",
        "Workplace Do's and Don'ts",
        "Travel Restrictions and Freedoms",
        "Library/Museum Rules",
        "Traffic Laws - Must vs Don't Have To",
        "Cultural Prohibitions",
        "Hotel Rules and Policies",
        "Park Regulations",
        "Restaurant Policies",
    ],
    "14": [
        "Making Predictions about Your Future",
        "Uncertain Situations",
        "Possibility of Events Happening",
        "Asking Permission Politely",
        "Weather Predictions",
        "Guessing Games with May/Might",
        "Mystery Situations",
        "Future Possibilities",
        "Polite Requests in Different Contexts",
        "Probability Discussions",
    ],
    "15": [
        "Ordering at a Restaurant Politely",
        "Making Travel Arrangements",
        "Expressing Preferences",
        "Party Planning and Invitations",
        "Shopping Politely",
        "Would Like vs Want - Politeness Practice",
        "Making Offers to Help",
        "Future Wishes and Desires",
        "Formal Email Requests",
        "Interview Situations",
    ],
}

TASK_NAMES_BY_MODULE = {
    "11": [
        "Advice Clinic - Role Play",
        "Problem Solving Discussion",
        "Lifestyle Improvement Plan",
        "Advice for Newcomers",
        "Should We or Shouldn't We? - Group Decision",
        "Travel Planning Advice",
        "Agony Aunt Letters",
        "Recommendation Presentation",
    ],
    "12": [
        "Comparing Rules - School vs Work",
        "Creating a Guidebook for Visitors",
        "Obligations Interview",
        "Must-Do List for Success",
        "Rule-Making Activity",
        "Obligation Debate",
        "Cultural Comparison - Rules in Different Countries",
        "Personal vs External Obligations Discussion",
    ],
    "13": [
        "Creating Signs and Rules",
        "Prohibition vs Freedom Debate",
        "Rules Review - What's Fair?",
        "Designing Classroom Rules",
        "Understanding Legal Requirements",
        "Cultural Prohibitions Presentation",
        "Rule Sorting Game",
        "Policy Making Activity",
    ],
    "14": [
        "Prediction Competition",
        "Permission Role-Plays",
        "Mystery Situation Guessing Game",
        "Future Possibility Discussions",
        "Polite Request Scenarios",
        "Weather Forecast Presentation",
        "Possibility Interview",
        "Formal Permission Letters",
    ],
    "15": [
        "Restaurant Role-Play",
        "Planning a Party - Offers and Preferences",
        "Polite Customer Service Scenarios",
        "Making Invitations",
        "Shopping Role-Plays",
        "Formal Meeting - Would Like Requests",
        "Preference Survey and Presentation",
        "Polite Decline Practice",
    ],
}

# ============================================================================
# MODULE GENERATION FUNCTIONS
# ============================================================================


def create_phase_1(module_num, module_data):
    """Generate Phase 1: Introduction notebook with modal-specific content"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"
    os.makedirs(base_path, exist_ok=True)

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_intro_header(module_num, module_data))

    # Generate section placeholders with modal focus
    section_titles = SECTION_TITLES_BY_MODULE.get(module_num, [])

    for i, title in enumerate(section_titles[: module_data["sections"]], 1):
        cells.extend(create_modal_section_placeholder(i, title, module_data["modal_focus"]))

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
        ("Formation - Affirmative", "Create affirmative sentences with correct modal form"),
        ("Formation - Negative", "Create negative sentences correctly"),
        ("Formation - Questions", "Form questions with proper word order"),
        ("Short Answers", "Give appropriate short answers"),
        ("Error Correction", "Find and correct modal verb mistakes"),
        ("Gap Filling", "Complete with correct modal forms"),
        ("Sentence Transformation", "Convert between forms"),
        ("Context Matching", "Choose appropriate modal for context"),
        ("Meaning Focus", "Use modal based on intended meaning"),
        ("Mixed Practice", "Apply all skills together"),
    ]

    for i, (name, desc) in enumerate(exercise_sets, 1):
        count = exercises_per_set + (1 if i <= remainder else 0)
        cells.extend(create_exercise_set(i, name, count, desc, module_data["modal_focus"]))

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

    # Generate activities with module-specific names
    activity_names = ACTIVITY_NAMES_BY_MODULE.get(module_num, [])
    key_uses = module_data["key_uses"]

    for i, name in enumerate(activity_names[: module_data["activities"]], 1):
        use_case = key_uses[i % len(key_uses)]
        cells.extend(create_modal_activity(i, name, module_data["modal_focus"], use_case))

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

    # Generate tasks with module-specific names
    task_names = TASK_NAMES_BY_MODULE.get(module_num, [])
    key_uses = module_data["key_uses"]

    for i, name in enumerate(task_names[: module_data["tasks"]], 1):
        goal = key_uses[i % len(key_uses)]
        cells.extend(create_modal_task(i, name, module_data["modal_focus"], goal))

    nb["cells"] = cells
    with open(f"{base_path}/04_communicative_practice.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def create_module_all_phases(module_num, module_data):
    """Create all 4 phases for a module"""
    print(f"\nCreating Module {module_num}: {module_data['title']}...")

    create_phase_1(module_num, module_data)
    print(f"  [OK] Phase 1 created ({module_data['sections']} sections)")

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
    """Generate all A2 Batch 3 modules"""
    print("=" * 70)
    print("A2 LEVEL - BATCH 3: MODAL VERBS")
    print("Generating Modules 11-15")
    print("=" * 70)

    # Ensure A2 directory exists
    os.makedirs("projects/english-learning/notebooks/A2", exist_ok=True)

    # Generate each module
    total_exercises = 0
    for module_num, module_data in BATCH_3_MODULES.items():
        try:
            result = create_module_all_phases(module_num, module_data)
            total_exercises += module_data["exercises"]
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
    print(f"Total Exercises: {total_exercises} (modal verb focused)")
    print("Target Level: A2")
    print("Focus: Modal Verbs (Advice, Obligation, Possibility, Requests)")
    print("\nModal Verb Features:")
    print("- Modal-specific validation framework")
    print("- Context-aware section titles")
    print("- Module-specific activity names")
    print("- Communicative tasks aligned with modal uses")
    print("- Enhanced error prevention (no -s, no 'to')")
    print("\nNext Steps:")
    print("1. Test Module 11 Phase 1")
    print("2. Add detailed content to Phase 1 sections")
    print("3. Add specific exercises to Phase 2 sets")
    print("4. Enhance Phase 3 activity instructions")
    print("5. Complete Phase 4 task scenarios")
    print("=" * 70)


if __name__ == "__main__":
    main()
