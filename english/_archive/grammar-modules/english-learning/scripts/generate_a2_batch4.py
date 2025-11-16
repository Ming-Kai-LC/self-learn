"""
A2 Level - Batch 4: Comparisons and Descriptions
Generates Modules 16-20 with comparison-specific architecture
Data-driven approach with comparison validation and specialized templates
"""

import os

import nbformat as nbf

# ============================================================================
# COMPARISON CHARACTERISTICS
# ============================================================================

COMPARISON_CHARACTERISTICS = {
    "formation_rules": {
        "one_syllable": {
            "comparative": "adjective + -er + than",
            "superlative": "the + adjective + -est",
            "examples": ["tall → taller → tallest", "big → bigger → biggest"],
            "spelling_rules": [
                "Regular: tall → taller → tallest",
                "Double final consonant (CVC): big → bigger → biggest",
                "Final -e: nice → nicer → nicest",
            ],
        },
        "two_syllables_y": {
            "comparative": "change -y to -ier + than",
            "superlative": "the + change -y to -iest",
            "examples": ["happy → happier → happiest", "easy → easier → easiest"],
        },
        "long_adjectives": {
            "comparative": "more + adjective + than",
            "superlative": "the most + adjective",
            "examples": [
                "expensive → more expensive → most expensive",
                "beautiful → more beautiful → most beautiful",
            ],
        },
    },
    "irregular_forms": {
        "good": {"comparative": "better than", "superlative": "the best"},
        "bad": {"comparative": "worse than", "superlative": "the worst"},
        "far": {"comparative": "farther/further than", "superlative": "the farthest/furthest"},
    },
    "common_patterns": {
        "as_as": "as + adjective + as (equality)",
        "not_as_as": "not as + adjective + as (inequality)",
        "the_the": "the + comparative, the + comparative (correlation)",
    },
    "common_errors": [
        {"wrong": "more better", "correct": "better", "rule": "Irregular forms don't use 'more'"},
        {
            "wrong": "more taller",
            "correct": "taller",
            "rule": "Short adjectives use -er, not 'more'",
        },
        {
            "wrong": "She is taller her brother",
            "correct": "She is taller than her brother",
            "rule": "Use 'than' with comparatives",
        },
        {
            "wrong": "He is tallest",
            "correct": "He is the tallest",
            "rule": "Superlatives need 'the'",
        },
    ],
}

# ============================================================================
# MODULE CONTENT CONFIGURATION
# ============================================================================

BATCH_4_MODULES = {
    "16": {
        "title": "Comparative Adjectives - Formation and Use",
        "subtitle": "Comparing Two Things",
        "time": "5-6 hours",
        "exercises": 85,
        "description": "Master comparative adjective formation and use for comparing people, places, and things",
        "topics": [
            "Form comparatives correctly: -er, more + adjective, irregular forms",
            "Apply spelling rules when adding -er (double consonants, -y to -i)",
            "Use 'than' correctly in comparative sentences",
            "Distinguish between short adjective + -er and long adjective + more",
            "Use irregular comparatives: better, worse, farther",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "comparison_focus": "comparative adjectives",
        "key_patterns": ["adjective + -er + than", "more + adjective + than", "irregular forms"],
    },
    "17": {
        "title": "Superlative Adjectives - The Best, The Biggest, The Most",
        "subtitle": "Describing Extremes",
        "time": "5-6 hours",
        "exercises": 85,
        "description": "Use superlative adjectives to describe the highest degree among three or more items",
        "topics": [
            "Form superlatives: the + adjective + -est, the most + adjective",
            "Apply the same spelling rules as comparatives",
            "Use superlatives with 'in' (the tallest in the class) and 'of' (the best of all)",
            "Master irregular superlatives: the best, the worst, the farthest",
            "Combine with 'one of the' for emphasis",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "comparison_focus": "superlative adjectives",
        "key_patterns": [
            "the + adjective + -est",
            "the most + adjective",
            "one of the + superlative",
        ],
    },
    "18": {
        "title": "As...As Comparisons - Equality and Inequality",
        "subtitle": "Showing Things Are the Same or Different",
        "time": "4-5 hours",
        "exercises": 82,
        "description": "Express equality and inequality using as...as structures",
        "topics": [
            "Form equality comparisons: as + adjective + as",
            "Form inequality comparisons: not as + adjective + as",
            "Understand when to use as...as vs comparative forms",
            "Use as...as with quantities: as much as, as many as",
            "Practice common expressions: as soon as possible, as well as",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
        "comparison_focus": "as...as patterns",
        "key_patterns": ["as + adjective + as", "not as + adjective + as", "as much/many as"],
    },
    "19": {
        "title": "Adverbs of Manner and Comparison",
        "subtitle": "How Things Happen - Quickly, Carefully, Well",
        "time": "5-6 hours",
        "exercises": 84,
        "description": "Describe how actions are performed using adverbs of manner",
        "topics": [
            "Form adverbs from adjectives: adjective + -ly",
            "Learn irregular adverbs: well (not goodly), fast, hard",
            "Place adverbs correctly in sentences",
            "Distinguish between adjectives and adverbs",
            "Form comparative and superlative adverbs",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "comparison_focus": "adverbs of manner",
        "key_patterns": ["adjective + -ly", "irregular adverbs", "adverb placement"],
    },
    "20": {
        "title": "Intensifiers and Descriptive Language",
        "subtitle": "Very, Quite, Too, Enough - Adding Degree and Intensity",
        "time": "4-5 hours",
        "exercises": 84,
        "description": "Add depth and precision to descriptions using intensifiers",
        "topics": [
            "Use very/really/quite to intensify adjectives and adverbs",
            "Understand 'too' for excessive degree (too expensive, too difficult)",
            "Use 'enough' correctly (adjective + enough, enough + noun)",
            "Distinguish between very (neutral) and too (negative implication)",
            "Combine intensifiers with comparatives for emphasis",
        ],
        "sections": 13,
        "activities": 10,
        "tasks": 8,
        "comparison_focus": "intensifiers",
        "key_patterns": [
            "very/really/quite + adj/adv",
            "too + adj",
            "adj + enough",
            "enough + noun",
        ],
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
    """Create introduction notebook header with comparison-specific info"""
    content = f"""# Module {module_num}: {module_data['title']} - Phase 1: Introduction

## Learning Objectives
{chr(10).join('- ' + topic for topic in module_data['topics'])}

**Target Level:** A2
**Estimated Time:** {module_data['time']}
**Comparison Focus:** {module_data['comparison_focus']}

## Important Formation Rules

{chr(10).join('- ' + pattern for pattern in module_data['key_patterns'])}

### Common Errors to Avoid:
{chr(10).join('- ❌ ' + err['wrong'] + ' → ✅ ' + err['correct'] for err in COMPARISON_CHARACTERISTICS['common_errors'][:3])}"""
    return create_markdown_cell(content)


def create_practice_header(module_num, module_data, phase_name, phase_num):
    """Create practice phase header"""
    if phase_num == 2:
        overview = f"""{module_data['exercises']} exercises to master {module_data['comparison_focus']}

**Total: {module_data['exercises']} exercises** *(Enhanced for comparison accuracy)*
**Focus:** {', '.join(module_data['key_patterns'])}"""
    elif phase_num == 3:
        overview = f"""10 personalized activities using {module_data['comparison_focus']} in real contexts"""
    else:  # phase 4
        overview = (
            f"""8 real-world communicative tasks focusing on {module_data['comparison_focus']}"""
        )

    content = f"""# Module {module_num}: {module_data['title']} - Phase {phase_num}: {phase_name}

## Overview
{overview}"""
    return create_markdown_cell(content)


def create_comparison_section_placeholder(section_num, section_title, comparison_focus):
    """Create placeholder section with comparison-specific examples"""
    cells = []

    md = f"""## {section_num}. {section_title}

[Content to be added: Detailed grammar explanation]

### Formation Rules:
- **Short adjectives (1 syllable):** Add -er/-est (tall → taller → tallest)
- **Long adjectives (3+ syllables):** Use more/most (beautiful → more beautiful → most beautiful)
- **Two-syllable -y adjectives:** Change -y to -ier/-iest (happy → happier → happiest)
- **Irregular forms:** Learn by heart (good → better → best, bad → worse → worst)

### Spelling Rules:
1. Double final consonant for CVC: big → bigger, hot → hotter
2. Drop final -e: nice → nicer, large → largest
3. Change -y to -i: easy → easier, pretty → prettier

### Examples with {comparison_focus}:
- Example 1: [Affirmative sentence]
- Example 2: [Negative sentence]
- Example 3: [Question]
- Example 4: [Complex sentence]

### Common Mistakes:
- ❌ WRONG: [Error example]
- ✅ CORRECT: [Corrected version]

### Key Grammar Points:
- Point 1: [Specific use to be added]
- Point 2: [Context when to use]
- Point 3: [Integration with other grammar]"""
    cells.append(create_markdown_cell(md))

    code = f"""# {section_title} - Practice
print("{section_title}")
print("=" * 60)

# Formation reminder for {comparison_focus}
print("\\nREMEMBER:")
print("- Short adjectives: add -er/-est")
print("- Long adjectives: use more/most")
print("- Irregular: good→better→best, bad→worse→worst")
print("\\n" + "=" * 60)

examples = [
    "Example sentence 1 with {comparison_focus}",
    "Example sentence 2 with {comparison_focus}",
    "Example sentence 3 with {comparison_focus}",
    "Example sentence 4 with {comparison_focus}"
]

for i, ex in enumerate(examples, 1):
    print(f"{{i}}. {{ex}}")

print("\\nYour turn: Create sentences using {comparison_focus}")
print("Check: Correct spelling? Right form (-er/more)? 'Than' if comparative? 'The' if superlative?")"""
    cells.append(create_code_cell(code))

    return cells


def create_exercise_set(set_num, set_name, count, description, comparison_focus):
    """Create exercise set with comparison-specific validation"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Exercise Set {set_num}: {set_name} ({count} exercises)

**Focus:** {description}
**Comparison Type:** {comparison_focus}

### Instructions:
Complete all {count} exercises below. Pay attention to:
- ✓ Correct spelling (double consonants, -y to -i)
- ✓ Choosing -er/-est vs more/most correctly
- ✓ Including 'than' in comparatives
- ✓ Including 'the' in superlatives
- ✓ Using correct irregular forms

**Remember:**
- 1 syllable → -er/-est (tall, big, old)
- 2 syllables ending in -y → -ier/-iest (happy, easy, busy)
- 3+ syllables → more/most (expensive, comfortable, interesting)
- Irregular → memorize (good/better/best, bad/worse/worst)"""
        )
    )

    code = f"""# Exercise Set {set_num}: {set_name}
from projects.english_learning.utils.feedback_system import ExerciseValidator

validator = ExerciseValidator()
print("{set_name}")
print("=" * 60)

# Quick reference for {comparison_focus}
formation_guide = {{
    "1_syllable": "add -er/-est",
    "2_syllable_y": "-y to -ier/-iest",
    "3+_syllables": "more/most",
    "irregular": "good→better→best, bad→worse→worst"
}}

print("\\nQuick Reference:")
for pattern, rule in formation_guide.items():
    print(f"  {{pattern}}: {{rule}}")

print("\\n" + "=" * 60)
print(f"\\nComplete {count} exercises below:")
print()

# {count} exercises with {comparison_focus}
for i in range(1, {count} + 1):
    print(f"{{i}}. Exercise {{i}}: [Comparison exercise to be added]")

print("\\n[Detailed answers and explanations at end of notebook]")
print("\\nValidation checklist:")
print("□ Correct spelling?")
print("□ Right form (-er/-est or more/most)?")
print("□ 'Than' in comparatives?")
print("□ 'The' in superlatives?")
print("□ Checked irregular forms?")"""
    cells.append(create_code_cell(code))

    return cells


def create_comparison_activity(activity_num, activity_name, comparison_focus):
    """Create meaningful practice activity with comparison-specific context"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Activity {activity_num}: {activity_name}

**Comparison Focus:** {comparison_focus}

### Instructions:
1. Write 8-10 sentences using {comparison_focus}
2. Use affirmative, negative, and question forms
3. Make it personal and realistic
4. Check: correct formation and spelling

**Example:**
[Model answer using {comparison_focus} to be added]

**Tips:**
- Use real people, places, and things from your life
- Compare across different categories (people, places, experiences)
- Include reasons for your comparisons"""
        )
    )

    code = f"""# Activity {activity_num}: {activity_name}
print("{activity_name}")
print("=" * 60)
print(f"\\nUse {comparison_focus} to make personal comparisons")
print("\\nWrite your sentences below:")
print()

for j in range(1, 11):
    print(f"{{j}}. _________________________________")

print("\\nRemember:")
print("- Check your spelling carefully")
print("- Use 'than' with comparatives")
print("- Use 'the' with superlatives")
print("\\nShare with a partner and compare!")"""
    cells.append(create_code_cell(code))

    return cells


def create_comparison_task(task_num, task_name, comparison_focus):
    """Create communicative practice task with comparison-specific goal"""
    cells = []

    cells.append(
        create_markdown_cell(
            f"""## Task {task_num}: {task_name}

**Comparison Focus:** {comparison_focus}

### Instructions:
- Work in pairs or small groups
- Use {comparison_focus} throughout the activity
- Focus on natural communication
- Present findings to the class

**Time:** 15-20 minutes

### Language Focus:
- Use {comparison_focus} naturally
- Ask and answer questions
- Give reasons for comparisons
- Listen to others' opinions"""
        )
    )

    code = f"""# Task {task_num}: {task_name}
print("{task_name}")
print("=" * 60)
print(f"\\nUse {comparison_focus} in this communicative task")
print("\\nUseful patterns:")
print("- Pattern 1: [To be added]")
print("- Pattern 2: [To be added]")
print("- Pattern 3: [To be added]")
print("\\nPrepare and practice with your partner!")"""
    cells.append(create_code_cell(code))

    return cells


# ============================================================================
# MODULE-SPECIFIC SECTION TITLES
# ============================================================================

SECTION_TITLES_BY_MODULE = {
    "16": [
        "Introduction to Comparative Adjectives",
        "Formation - Short Adjectives (adjective + -er)",
        "Formation - Long Adjectives (more + adjective)",
        "Formation - Two-Syllable Adjectives Ending in -y",
        "Spelling Rules - Doubling Consonants (big → bigger)",
        "Spelling Rules - Dropping -e (nice → nicer)",
        "Spelling Rules - Changing -y to -i (happy → happier)",
        "Using 'Than' in Comparative Sentences",
        "Irregular Comparatives (good → better, bad → worse)",
        "Comparing People - Height, Age, Personality",
        "Comparing Things - Size, Price, Quality",
        "Comparing Places - Beauty, Size, Population",
        "Common Mistakes with Comparatives",
        "Pronunciation of -er Endings",
        "Practice Conversations - Making Comparisons",
    ],
    "17": [
        "Introduction to Superlative Adjectives",
        "Formation - The + Adjective + -est",
        "Formation - The Most + Adjective",
        "Same Spelling Rules as Comparatives",
        "Using 'The' with Superlatives (Always!)",
        "Superlatives with 'In' (the tallest in the class)",
        "Superlatives with 'Of' (the best of all)",
        "Irregular Superlatives (the best, the worst)",
        "One of the + Superlative + Plural Noun",
        "Describing Extremes - People",
        "Describing Extremes - Places and Things",
        "World Records and Superlatives",
        "Common Mistakes with Superlatives",
        "Pronunciation of -est Endings",
        "Practice Conversations - Talking About Bests and Worsts",
    ],
    "18": [
        "Introduction to As...As Comparisons",
        "Formation - As + Adjective + As (Equality)",
        "Formation - Not As + Adjective + As (Inequality)",
        "When to Use As...As vs Comparatives",
        "As...As with Adjectives",
        "As Much As / As Many As (Quantities)",
        "Common Expressions (as soon as possible, as well as)",
        "Comparing Equal Characteristics",
        "Showing Things Are NOT Equal",
        "As...As in Questions",
        "Twice As...As, Three Times As...As",
        "Common Mistakes with As...As",
        "Pronunciation Patterns",
        "Practice Conversations - Equality Comparisons",
    ],
    "19": [
        "Introduction to Adverbs of Manner",
        "Formation - Adjective + -ly (quick → quickly)",
        "Irregular Adverbs (good → well, fast → fast, hard → hard)",
        "Spelling Changes (happy → happily, simple → simply)",
        "Adverb Placement - After Verb",
        "Adverb Placement - After Verb + Object",
        "Adjectives vs Adverbs (good/well, careful/carefully)",
        "Common Adverbs of Manner",
        "Comparative Adverbs (more quickly, faster)",
        "Superlative Adverbs (most carefully, fastest)",
        "Adverbs with Past Tense Narratives",
        "Adverbs with Future Actions",
        "Common Mistakes with Adverbs",
        "Pronunciation of -ly Endings",
        "Practice Conversations - Describing Actions",
    ],
    "20": [
        "Introduction to Intensifiers",
        "Very + Adjective/Adverb",
        "Really + Adjective/Adverb",
        "Quite + Adjective (British vs American usage)",
        "Too + Adjective (excessive/negative)",
        "Adjective/Adverb + Enough",
        "Enough + Noun",
        "Position Rules (very/too before, enough after)",
        "Very vs Too - Understanding the Difference",
        "Combining Intensifiers with Comparatives",
        "Gradable vs Non-Gradable Adjectives",
        "Common Mistakes with Intensifiers",
        "Practice Conversations - Adding Emphasis",
    ],
}

ACTIVITY_NAMES_BY_MODULE = {
    "16": [
        "Compare Yourself to Family Members",
        "My City vs Another City",
        "This Year vs Last Year",
        "Comparing Two Favorite Things",
        "Before and After - Personal Changes",
        "Comparing Two Friends or Classmates",
        "Old Phone vs New Phone",
        "Comparing Weather in Different Seasons",
        "Comparing Two Jobs or Careers",
        "Comparing Learning Methods",
    ],
    "17": [
        "The Best and Worst in My Life",
        "My Country's Records and Extremes",
        "The Most Interesting Places I've Visited",
        "The Best Movie/Book/Song Ever",
        "My Class Superlatives",
        "World Records Discussion",
        "The Most Important Person in My Life",
        "Ranking My Top 3 Favorites",
        "The Biggest Achievements and Challenges",
        "One of the Best Days of My Life",
    ],
    "18": [
        "Things That Are the Same in My Life",
        "Not As...As - Finding Differences",
        "Equal Comparisons - People I Know",
        "As...As Challenges and Achievements",
        "Comparing Similarities Between Cities/Countries",
        "As Good As or Better Than?",
        "Things That Aren't As Good As They Used To Be",
        "As Much/Many As Comparisons",
        "Equal Abilities and Skills",
        "As Soon As Possible - My Plans",
    ],
    "19": [
        "How Do You Do Things? - Adverb Self-Description",
        "Describing How Others Act",
        "Then vs Now - How Things Have Changed",
        "Good Performance vs Poor Performance",
        "Cultural Differences in Behavior",
        "How I Want to Improve",
        "Fast vs Slow - Speed Comparisons",
        "Careful vs Careless - Quality Descriptions",
        "Well vs Badly - Skill Levels",
        "Describing a Perfect Day - Using Manner Adverbs",
    ],
    "20": [
        "Very vs Too - Making Distinctions",
        "What's Enough and What Isn't?",
        "Too Much of a Good Thing",
        "Quite Interesting - British Understatement",
        "Really Amazing Experiences",
        "Not Enough Time/Money/Space",
        "Too Expensive or Just Right?",
        "Very Good vs Really Excellent",
        "Enough is Enough - Setting Limits",
        "Intensifying Your Descriptions",
    ],
}

TASK_NAMES_BY_MODULE = {
    "16": [
        "Comparison Shopping - Which One to Buy?",
        "Debate: City Life vs Country Life",
        "Comparing Two Tourist Destinations",
        "Then vs Now - Interview Activity",
        "Product Comparison Presentation",
        "Comparing Different Solutions to a Problem",
        "Two Options Decision-Making Role Play",
        "Comparing Learning Strategies",
    ],
    "17": [
        "Creating a Top 10 List and Presenting",
        "Superlatives Quiz Game",
        "The Best Place in Our City - Presentation",
        "Class Survey - Finding Our Superlatives",
        "World Records Research and Presentation",
        "Ranking and Explaining Choices",
        "Creating Award Categories",
        "Debate: What's the Most Important...?",
    ],
    "18": [
        "Finding Things in Common - Interview",
        "As...As Challenge - Finding Equalities",
        "Equality vs Inequality Sorting Game",
        "Myth Busting - Is X Really As...As Y?",
        "Comparing Twins or Similar Things",
        "As Soon As Possible - Urgent Tasks Role Play",
        "Finding Equal Qualities in Different Things",
        "Similarity Search Activity",
    ],
    "19": [
        "How Do You...? - Manner Interview",
        "Demonstrating and Describing Actions",
        "Adverb Charades",
        "Describing Perfect Performance",
        "Cultural Behavior Comparison",
        "Improving Skills - Adverb Goals",
        "Story Retelling with Manner Adverbs",
        "Performance Review Role Play",
    ],
    "20": [
        "Too or Enough? - Decision Making",
        "Intensifier Degrees Game",
        "Complaint Role Play (Too...)",
        "Satisfaction Survey (Enough...)",
        "Very vs Really - Emphasis Practice",
        "Setting Standards - What's Enough?",
        "Consumer Feedback - Using Intensifiers",
        "Describing Ideal Conditions",
    ],
}

# ============================================================================
# MODULE GENERATION FUNCTIONS
# ============================================================================


def create_phase_1(module_num, module_data):
    """Generate Phase 1: Introduction notebook with comparison-specific content"""
    base_path = f"projects/english-learning/notebooks/A2/Module_{module_num}"
    os.makedirs(base_path, exist_ok=True)

    nb = nbf.v4.new_notebook()
    cells = []

    # Header
    cells.append(create_intro_header(module_num, module_data))

    # Generate section placeholders
    section_titles = SECTION_TITLES_BY_MODULE.get(module_num, [])

    for i, title in enumerate(section_titles[: module_data["sections"]], 1):
        cells.extend(
            create_comparison_section_placeholder(i, title, module_data["comparison_focus"])
        )

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
        ("Formation - Comparatives/Superlatives", "Master correct formation"),
        ("Spelling Practice", "Apply spelling rules correctly"),
        ("Gap Filling", "Complete sentences with correct forms"),
        ("Sentence Construction", "Build complete comparative/superlative sentences"),
        ("Error Correction", "Find and fix mistakes"),
        ("Transformation", "Change between forms"),
        ("Context Matching", "Choose appropriate form for context"),
        ("Question Formation", "Create comparative/superlative questions"),
        ("Short Answers", "Respond appropriately"),
        ("Mixed Practice", "Apply all skills together"),
    ]

    for i, (name, desc) in enumerate(exercise_sets, 1):
        count = exercises_per_set + (1 if i <= remainder else 0)
        cells.extend(create_exercise_set(i, name, count, desc, module_data["comparison_focus"]))

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

    for i, name in enumerate(activity_names[: module_data["activities"]], 1):
        cells.extend(create_comparison_activity(i, name, module_data["comparison_focus"]))

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

    for i, name in enumerate(task_names[: module_data["tasks"]], 1):
        cells.extend(create_comparison_task(i, name, module_data["comparison_focus"]))

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
    """Generate all A2 Batch 4 modules"""
    print("=" * 70)
    print("A2 LEVEL - BATCH 4: COMPARISONS AND DESCRIPTIONS")
    print("Generating Modules 16-20")
    print("=" * 70)

    # Ensure A2 directory exists
    os.makedirs("projects/english-learning/notebooks/A2", exist_ok=True)

    # Generate each module
    total_exercises = 0
    for module_num, module_data in BATCH_4_MODULES.items():
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
    print(f"Total Exercises: {total_exercises} (comparison-focused)")
    print("Target Level: A2")
    print("Focus: Comparisons and Descriptions")
    print("\nComparison Features:")
    print("- Formation rules for all adjective types")
    print("- Spelling rule emphasis throughout")
    print("- Comparison-specific validation framework")
    print("- Integration with Batches 1-3 grammar")
    print(
        "- Progressive complexity (comparatives → superlatives → as...as → adverbs → intensifiers)"
    )
    print("\nNext Steps:")
    print("1. Test Module 16 Phase 1")
    print("2. Add detailed content to Phase 1 sections")
    print("3. Add specific exercises to Phase 2 sets")
    print("4. Enhance Phase 3 activity instructions")
    print("5. Complete Phase 4 task scenarios")
    print("=" * 70)


if __name__ == "__main__":
    main()
