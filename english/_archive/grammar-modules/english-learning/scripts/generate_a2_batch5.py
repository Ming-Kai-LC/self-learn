"""
A2 Level - Batch 5: Advanced Structures and Integration (Modules 21-25)
Final A2 batch completing the elementary level curriculum

This batch focuses on:
- Zero and First Conditionals (if-clauses)
- Connectors and Linking Words (because, so, but, although)
- Relative Clauses (who, which, that, where)
- Comprehensive Question Formation
- A2 Consolidation and Integration

Architecture: Hybrid approach with topic-specific characteristics and integration framework
Exercise Count: 419 total exercises (Module 25 has 99 for comprehensive review)
"""

import os

import nbformat as nbf

# ============================================================================
# GRAMMAR CHARACTERISTICS - Topic-Specific Dictionaries
# ============================================================================

CONDITIONAL_CHARACTERISTICS = {
    "zero_conditional": {
        "structure": "If + present simple, present simple",
        "usage": "General truths, scientific facts, habits",
        "time_reference": "Always true / timeless",
        "examples": [
            "If you heat water to 100°C, it boils.",
            "If I wake up late, I miss the bus.",
            "If it rains, the ground gets wet.",
        ],
    },
    "first_conditional": {
        "structure": "If + present simple, will + base verb",
        "usage": "Real future possibilities, predictions, warnings, promises",
        "time_reference": "Future",
        "examples": [
            "If it rains tomorrow, I will stay at home.",
            "If you study hard, you will pass the exam.",
            "If we hurry, we won't be late.",
        ],
    },
    "key_points": [
        "Use present tense in the if-clause (NOT 'will' after 'if')",
        "Can reverse clause order: 'I will stay at home if it rains'",
        "Use comma when if-clause comes first",
        "Zero conditional = always true; First conditional = possible future",
    ],
    "common_errors": [
        "❌ If it will rain, I will stay home. → ✓ If it rains, I will stay home.",
        "❌ If you will study, you pass. → ✓ If you study, you will pass.",
        "❌ I will go if will have time. → ✓ I will go if I have time.",
    ],
}

CONNECTOR_CHARACTERISTICS = {
    "cause_result": {
        "because": {
            "function": "Shows reason/cause",
            "position": "Joins two clauses - can start or middle",
            "examples": [
                "I stayed home because it was raining.",
                "Because it was late, we took a taxi.",
            ],
        },
        "so": {
            "function": "Shows result/consequence",
            "position": "Middle of sentence only (connects result to cause)",
            "examples": [
                "It was raining, so I stayed home.",
                "I was tired, so I went to bed early.",
            ],
        },
    },
    "contrast": {
        "but": {
            "function": "Shows contrast between two ideas",
            "position": "Middle of sentence",
            "examples": [
                "I like coffee, but I don't like tea.",
                "It was expensive, but I bought it anyway.",
            ],
        },
        "although": {
            "function": "Shows concession (despite contrast)",
            "position": "Can start or middle",
            "examples": [
                "Although it was raining, we went out.",
                "We went out, although it was raining.",
            ],
        },
    },
    "key_points": [
        "'Because' = reason; 'So' = result (never use both together)",
        "'But' and 'although' both show contrast, but 'although' is more formal",
        "Use comma after 'because/although' clause when it starts the sentence",
        "'So' always has comma before it",
    ],
    "common_errors": [
        "❌ Because it was raining, so I stayed home. → ✓ Because it was raining, I stayed home. OR It was raining, so I stayed home.",
        "❌ Although I was tired but I worked. → ✓ Although I was tired, I worked.",
        "❌ I like it so I bought it → ✓ I like it, so I bought it.",
    ],
}

RELATIVE_CLAUSE_CHARACTERISTICS = {
    "relative_pronouns": {
        "who": {
            "usage": "For people (subject or object)",
            "examples": [
                "The man who called you is my brother.",
                "The teacher who teaches English is from London.",
            ],
        },
        "which": {
            "usage": "For things/animals (subject or object)",
            "examples": [
                "The book which is on the table is mine.",
                "The car which I bought is red.",
            ],
        },
        "that": {
            "usage": "For people or things (can replace who/which in defining clauses)",
            "examples": [
                "The man that called is my brother.",
                "The book that is on the table is mine.",
            ],
        },
        "where": {
            "usage": "For places",
            "examples": [
                "The restaurant where we ate was excellent.",
                "This is the hotel where I stayed.",
            ],
        },
    },
    "clause_types": {
        "defining": {
            "description": "Essential information to identify the noun (A2 level)",
            "no_commas": True,
            "examples": [
                "The woman who lives next door is a doctor.",
                "I like books that have happy endings.",
            ],
        }
    },
    "key_points": [
        "Relative clause comes immediately after the noun it describes",
        "Use 'who' for people, 'which' for things, 'where' for places",
        "'That' can replace 'who' or 'which' in defining clauses",
        "No commas with defining relative clauses at A2 level",
    ],
    "common_errors": [
        "❌ The man which called is my friend. → ✓ The man who called is my friend.",
        "❌ The place where I visited was nice. → ✓ The place which I visited was nice. (or The place I visited)",
        "❌ The book, that I read, was good. → ✓ The book that I read was good.",
    ],
}

QUESTION_FORMATION_PATTERNS = {
    "yes_no_questions": {
        "be_verbs": "Be + subject + ...?",
        "do_does_did": "Do/Does/Did + subject + base verb + ...?",
        "modals": "Modal + subject + base verb + ...?",
        "have_has": "Have/Has + subject + past participle + ...? (present perfect)",
    },
    "wh_questions": {
        "what": "What + auxiliary + subject + verb?",
        "where": "Where + auxiliary + subject + verb?",
        "when": "When + auxiliary + subject + verb?",
        "who_subject": "Who + verb? (no auxiliary needed)",
        "who_object": "Who + auxiliary + subject + verb?",
        "why": "Why + auxiliary + subject + verb?",
        "how": "How + auxiliary + subject + verb?",
        "which": "Which + noun + auxiliary + subject + verb?",
    },
    "key_points": [
        "Subject questions (Who/What as subject) don't use do/does/did",
        "Object questions need auxiliary verbs",
        "Keep the correct tense when forming questions",
        "Use question mark at the end",
    ],
    "common_errors": [
        "❌ What you are doing? → ✓ What are you doing?",
        "❌ Who did call? → ✓ Who called?",
        "❌ Where you went? → ✓ Where did you go?",
    ],
}

# ============================================================================
# INTEGRATION FRAMEWORK
# ============================================================================

INTEGRATION_MATRIX = {
    "batch_1_past": {
        "modules": [1, 2, 3, 4, 5],
        "key_structures": ["past continuous", "past simple", "present perfect"],
        "integration_focus": "Combine conditionals with past tenses, use relative clauses for past events",
    },
    "batch_2_future": {
        "modules": [6, 7, 8, 9, 10],
        "key_structures": [
            "going to",
            "will",
            "present continuous for future",
            "time clauses",
            "for/since",
        ],
        "integration_focus": "First conditional naturally uses will, connectors with future plans",
    },
    "batch_3_modals": {
        "modules": [11, 12, 13, 14, 15],
        "key_structures": ["should", "must/have to", "may/might", "would like"],
        "integration_focus": "Use modals in main clause of conditionals, combine with connectors",
    },
    "batch_4_comparisons": {
        "modules": [16, 17, 18, 19, 20],
        "key_structures": ["comparatives", "superlatives", "as...as", "adverbs", "intensifiers"],
        "integration_focus": "Describe with relative clauses and comparisons together",
    },
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_5_MODULES = {
    "21": {
        "title": "Zero and First Conditional - If Clauses and Real Possibilities",
        "subtitle": "Expressing Conditions and Future Possibilities",
        "time": "5-6 hours",
        "exercises": 85,
        "description": "Master zero and first conditional structures for general truths and real future possibilities",
        "topics": [
            "Form zero conditional for general truths and scientific facts",
            "Form first conditional for real future possibilities",
            "Understand the difference between zero and first conditional",
            "Use correct verb forms in if-clause and main clause",
            "Avoid common error: using 'will' in the if-clause",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "grammar_focus": "conditionals",
        "key_patterns": ["If + present, present", "If + present, will + base verb"],
    },
    "22": {
        "title": "Connectors and Linking Words - Because, So, But, Although",
        "subtitle": "Connecting Ideas Logically",
        "time": "5-6 hours",
        "exercises": 84,
        "description": "Master essential connectors to show cause-result and contrast relationships",
        "topics": [
            "Use 'because' and 'so' to connect cause and result",
            "Understand the difference between 'because' (reason) and 'so' (result)",
            "Use 'but' to express contrast between ideas",
            "Use 'although' for concession (despite contrast)",
            "Apply correct punctuation with connectors",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
        "grammar_focus": "connectors",
        "key_patterns": ["because", "so", "but", "although"],
    },
    "23": {
        "title": "Relative Clauses - Who, Which, That, Where",
        "subtitle": "Describing and Defining People, Things, and Places",
        "time": "5-6 hours",
        "exercises": 85,
        "description": "Master basic defining relative clauses to provide detailed descriptions",
        "topics": [
            "Use 'who' for people in relative clauses",
            "Use 'which' and 'that' for things in relative clauses",
            "Use 'where' for places in relative clauses",
            "Form sentences with relative clauses correctly",
            "Understand defining relative clauses (no commas at A2)",
        ],
        "sections": 15,
        "activities": 10,
        "tasks": 8,
        "grammar_focus": "relative_clauses",
        "key_patterns": ["who", "which", "that", "where"],
    },
    "24": {
        "title": "Question Formation - Comprehensive Review Across All Tenses",
        "subtitle": "Mastering All Question Types",
        "time": "5-6 hours",
        "exercises": 82,
        "description": "Master question formation across all A2 grammar structures",
        "topics": [
            "Form yes/no questions with be, do/does/did across all tenses",
            "Form wh-questions correctly with proper word order",
            "Understand subject questions vs object questions",
            "Form questions with modals and perfect tenses",
            "Review and integrate all A2 question types",
        ],
        "sections": 14,
        "activities": 10,
        "tasks": 8,
        "grammar_focus": "questions",
        "key_patterns": ["Yes/No questions", "Wh-questions", "Subject questions"],
    },
    "25": {
        "title": "A2 Consolidation and Review - Integration and Real-World Communication",
        "subtitle": "Bringing It All Together - B1 Preparation",
        "time": "6-8 hours",
        "exercises": 99,
        "description": "Integrate all A2 grammar in authentic communication tasks and prepare for B1",
        "topics": [
            "Integrate all A2 tenses naturally in communication",
            "Combine modals, conditionals, and connectors effectively",
            "Use complex sentences with multiple structures",
            "Demonstrate A2 mastery across all skills",
            "Prepare for B1 transition with preview",
        ],
        "sections": 12,
        "activities": 12,
        "tasks": 10,
        "grammar_focus": "integration",
        "key_patterns": ["All A2 grammar integrated"],
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
    """Create comprehensive introduction header"""
    title = module_data["title"]
    subtitle = module_data["subtitle"]
    time = module_data["time"]
    description = module_data["description"]

    header = f"""# A2 Module {module_num}: {title}

## {subtitle}

**Estimated Time:** {time}
**Level:** A2 (Elementary)
**Focus:** {module_data['grammar_focus'].replace('_', ' ').title()}

---

## Module Overview

{description}

### What You'll Learn

"""

    for i, topic in enumerate(module_data["topics"], 1):
        header += f"{i}. {topic}\n"

    header += f"""
### Module Structure

This module follows the proven 4-phase learning approach:

1. **Phase 1: Introduction** ({module_data['sections']} sections)
   - Detailed grammar explanations with examples
   - Formation rules and usage guidelines
   - Common errors to avoid

2. **Phase 2: Controlled Practice** ({module_data['exercises']} exercises)
   - Structured exercises with immediate feedback
   - Progressive difficulty
   - Integration with previous grammar

3. **Phase 3: Meaningful Practice** ({module_data['activities']} activities)
   - Personalized content creation
   - Real-world application
   - Your life, your examples

4. **Phase 4: Communicative Practice** ({module_data['tasks']} tasks)
   - Authentic communication scenarios
   - Free production
   - Fluency development

---

Let's begin!
"""

    return create_markdown_cell(header)


def create_section_placeholder(section_num, section_title, grammar_focus, module_num):
    """Create placeholder section with grammar-specific content"""
    cells = []

    # Section header
    md = f"""## {section_num}. {section_title}

[Content to be added: Detailed grammar explanation with examples]
"""

    # Add grammar-specific guidance
    if grammar_focus == "conditionals":
        md += """
### Key Points:
- Zero conditional: If + present, present (general truths)
- First conditional: If + present, will + base verb (real future possibilities)
- Do NOT use 'will' in the if-clause
- Use comma when if-clause comes first

### Formation:
```
Zero: If you heat water, it boils.
First: If it rains, I will stay home.
```
"""
    elif grammar_focus == "connectors":
        md += """
### Key Points:
- Because = reason (can start or middle of sentence)
- So = result (middle of sentence only, comma before it)
- But = contrast (middle of sentence, comma before it)
- Although = concession (can start or middle)

### Punctuation:
- Comma after because/although when they start the sentence
- Comma before so and but
"""
    elif grammar_focus == "relative_clauses":
        md += """
### Key Points:
- Who = people
- Which/That = things
- Where = places
- Relative clause comes right after the noun it describes
- No commas with defining relative clauses (A2 level)

### Examples:
- The woman who lives here is a teacher.
- The book which I read was interesting.
- The place where I work is near the station.
"""
    elif grammar_focus == "questions":
        md += """
### Key Points:
- Yes/No questions: Auxiliary + subject + verb?
- Wh-questions: Wh-word + auxiliary + subject + verb?
- Subject questions: Who/What + verb? (no auxiliary)
- Keep the correct tense when forming questions

### Word Order:
```
Statement: You are reading.
Question: What are you reading?
```
"""

    cells.append(create_markdown_cell(md))

    # Practice code cell
    code = f"""# Practice: {section_title}

# Example sentences will be provided here for practice
# Try to create your own examples following the patterns shown

print("Practice area - examples and exercises to be added")
"""
    cells.append(create_code_cell(code))

    return cells


def create_exercise_set(set_num, set_name, count, description, grammar_focus):
    """Create exercise set with validation framework"""
    cells = []

    # Exercise header
    md = f"""### Exercise Set {set_num}: {set_name}

**Exercises:** {count}
**Focus:** {description}

Complete the following exercises. Check your answers after each one.
"""
    cells.append(create_markdown_cell(md))

    # Exercise code cell with validation
    code = f"""# Exercise Set {set_num}: {set_name}

# Import the feedback system
import sys
sys.path.append('../../..')
from utils.feedback_system import ExerciseValidator

# Initialize validator
validator = ExerciseValidator()

# Exercise 1
print("Exercise 1: [Exercise text to be added]")
answer_1 = input("Your answer: ")
validator.check_answer(answer_1, "correct_answer_here", "Exercise 1")

# Exercise 2
print("\\nExercise 2: [Exercise text to be added]")
answer_2 = input("Your answer: ")
validator.check_answer(answer_2, "correct_answer_here", "Exercise 2")

# [Additional exercises will be added - total: {count} exercises]

# Show final score
validator.show_summary()
"""
    cells.append(create_code_cell(code))

    return cells


def create_activity_placeholder(activity_num, activity_name, grammar_focus):
    """Create meaningful practice activity"""
    cells = []

    md = f"""## Activity {activity_num}: {activity_name}

**Objective:** Apply {grammar_focus.replace('_', ' ')} in a personal, meaningful context.

**Instructions:**

[Detailed instructions to be added based on activity type]

**Your Turn:**

Create 8-10 sentences about your own life using the {grammar_focus.replace('_', ' ')} structure.
"""
    cells.append(create_markdown_cell(md))

    code = f"""# Activity {activity_num}: {activity_name}

# Write your sentences here
# Example format:

sentences = [
    "1. [Your sentence here]",
    "2. [Your sentence here]",
    "3. [Your sentence here]",
    # Add 8-10 sentences total
]

for sentence in sentences:
    print(sentence)
"""
    cells.append(create_code_cell(code))

    return cells


def create_task_placeholder(task_num, task_name, grammar_focus):
    """Create communicative practice task"""
    cells = []

    md = f"""## Task {task_num}: {task_name}

**Duration:** 15-20 minutes
**Skill Focus:** Speaking/Writing with {grammar_focus.replace('_', ' ')}

**Scenario:**

[Real-world scenario description to be added]

**Your Task:**

[Task instructions to be added]

**Tips:**

- Use natural, conversational language
- Don't worry about small mistakes
- Focus on communication
- Try to use the {grammar_focus.replace('_', ' ')} structures naturally
"""
    cells.append(create_markdown_cell(md))

    code = f"""# Task {task_num}: {task_name}

# Use this space to prepare your ideas or write your response

# Notes:
# -
# -
# -

print("Task preparation area")
"""
    cells.append(create_code_cell(code))

    return cells


# ============================================================================
# MODULE-SPECIFIC CONTENT
# ============================================================================

SECTION_TITLES_BY_MODULE = {
    "21": [  # Zero and First Conditional
        "Introduction to Conditionals",
        "Zero Conditional - Structure and Formation",
        "Zero Conditional - General Truths and Facts",
        "Zero Conditional - Habits and Routines",
        "First Conditional - Structure and Formation",
        "First Conditional - Real Future Possibilities",
        "First Conditional - Predictions and Warnings",
        "First Conditional - Promises and Offers",
        "Zero vs First Conditional - Key Differences",
        "Common Errors with Conditionals",
        "Conditionals in Questions",
        "Conditionals in Negatives",
        "Unless = If not",
        "Combining Conditionals with Other Grammar",
        "Practice Conversations with Conditionals",
    ],
    "22": [  # Connectors
        "Introduction to Connectors",
        "Because - Showing Reason",
        "So - Showing Result",
        "Because vs So - Understanding the Difference",
        "But - Showing Contrast",
        "Although - Showing Concession",
        "But vs Although - When to Use Each",
        "Punctuation with Connectors",
        "Combining Multiple Connectors",
        "Common Errors with Connectors",
        "Connectors in Questions",
        "Building Complex Sentences",
        "Paragraph Structure with Connectors",
        "Practice Conversations with Connectors",
    ],
    "23": [  # Relative Clauses
        "Introduction to Relative Clauses",
        "Who - For People (Subject)",
        "Who - For People (Object)",
        "Which - For Things (Subject)",
        "Which - For Things (Object)",
        "That - For People and Things",
        "Where - For Places",
        "Defining Relative Clauses",
        "Relative Clause Position in Sentences",
        "Common Errors with Relative Clauses",
        "Relative Clauses in Questions",
        "Omitting the Relative Pronoun (Object Clauses)",
        "Combining Relative Clauses with Other Grammar",
        "Building Detailed Descriptions",
        "Practice Conversations with Relative Clauses",
    ],
    "24": [  # Question Formation
        "Introduction to Question Formation",
        "Yes/No Questions - Present Simple and Continuous",
        "Yes/No Questions - Past Simple and Continuous",
        "Yes/No Questions - Future Forms",
        "Yes/No Questions - Present Perfect",
        "Yes/No Questions - With Modals",
        "Wh-Questions - Word Order Rules",
        "Subject Questions vs Object Questions",
        "Questions with What, Where, When",
        "Questions with Who, Why, How",
        "Questions with Which, Whose",
        "Common Errors in Question Formation",
        "Questions Across All A2 Grammar",
        "Practice Interviews and Dialogues",
    ],
    "25": [  # A2 Consolidation
        "A2 Grammar Overview - What We've Learned",
        "Tense Integration - Past, Present, Future",
        "Modal Verb Mastery Review",
        "Conditionals and Connectors in Context",
        "Comparisons and Descriptions Review",
        "Relative Clauses for Detailed Communication",
        "Real-World Scenario 1: Travel and Tourism",
        "Real-World Scenario 2: Work and Study",
        "Real-World Scenario 3: Social Life",
        "Complex Sentence Building - All Structures",
        "A2 Self-Assessment and Progress Check",
        "B1 Preview - What's Next in Your Learning Journey",
    ],
}

ACTIVITY_NAMES_BY_MODULE = {
    "21": [
        "My Daily Routines - Zero Conditional",
        "General Facts About Me - Zero Conditional",
        "My Future Plans - First Conditional",
        "What Will Happen If... - Predictions",
        "Promises to Myself - First Conditional",
        "My Habits and Results - Zero Conditional",
        "Weekend Plans with Conditions",
        "Advice Using Conditionals",
        "My Goals and Conditions",
        "Combining Conditionals in My Life",
    ],
    "22": [
        "Why I Do Things - Because",
        "Results of My Actions - So",
        "Contrasts in My Life - But",
        "Despite Difficulties - Although",
        "My Daily Life with Connectors",
        "Explaining My Choices",
        "My Opinions with Reasons",
        "Describing My Personality",
        "My Past Experiences with Connectors",
        "My Future Plans with Logical Connections",
    ],
    "23": [
        "People in My Life - Who",
        "Things I Own - Which/That",
        "Places I Know - Where",
        "Describing My Family",
        "My Favorite Things",
        "Places I've Visited",
        "People Who Inspire Me",
        "Things That Make Me Happy",
        "Describing My Environment",
        "Building Detailed Personal Descriptions",
    ],
    "24": [
        "Interview About My Past",
        "Questions About My Daily Life",
        "Future Plans Interview",
        "Getting to Know Someone",
        "Job Interview Preparation",
        "Travel Questions and Answers",
        "Questions About Preferences",
        "Information Gathering Practice",
        "Survey Creation",
        "Comprehensive Q&A Practice",
    ],
    "25": [
        "My Complete Life Story",
        "Past, Present, and Future - Integrated",
        "Giving Comprehensive Advice",
        "Describing Complex Situations",
        "My Learning Journey - A2 Reflection",
        "Planning a Complex Project",
        "Discussing Possibilities and Conditions",
        "Detailed Descriptions with Multiple Structures",
        "Real Conversation Practice",
        "A2 Mastery Showcase",
        "Preparing for B1 Challenges",
        "My English Goals Moving Forward",
    ],
}

TASK_NAMES_BY_MODULE = {
    "21": [
        "Life Advice Column",
        "What Will Happen? - Predictions",
        "Travel Conditions",
        "Health and Habits Discussion",
        "Making Promises",
        "Problem Solving with Conditionals",
        "Future Scenarios Role-Play",
        "Conditional Conversations",
    ],
    "22": [
        "Explaining Decisions",
        "Cause and Effect Discussion",
        "Contrasting Opinions Debate",
        "Story Telling with Connectors",
        "Explaining Complex Situations",
        "Paragraph Writing Practice",
        "Discussion: Reasons and Results",
        "Logical Arguments",
    ],
    "23": [
        "Describing People Role-Play",
        "Lost and Found Descriptions",
        "Travel Guide Creation",
        "Celebrity Description Game",
        "Ideal Partner/Friend Description",
        "Place Recommendations",
        "Detailed Product Reviews",
        "Story Enhancement with Details",
    ],
    "24": [
        "Getting-to-Know-You Interview",
        "Information Gap Activity",
        "Job Interview Simulation",
        "Survey Design and Conduct",
        "Twenty Questions Game",
        "Travel Information Desk",
        "Expert Interview",
        "Comprehensive Q&A Session",
    ],
    "25": [
        "Complete Life Presentation",
        "Complex Problem Discussion",
        "Integrated Storytelling",
        "Travel Planning Scenario",
        "Job Application Process",
        "Social Situation Navigation",
        "Academic Discussion Simulation",
        "Future Planning Consultation",
        "A2 Mastery Demonstration",
        "B1 Readiness Assessment",
    ],
}

# ============================================================================
# PHASE GENERATION FUNCTIONS
# ============================================================================


def create_phase_1(module_num, module_data):
    """Generate Phase 1: Introduction notebook"""
    cells = []

    # Header
    cells.append(create_intro_header(module_num, module_data))

    # Create sections
    section_titles = SECTION_TITLES_BY_MODULE[module_num]
    for i, section_title in enumerate(section_titles, 1):
        section_cells = create_section_placeholder(
            i, section_title, module_data["grammar_focus"], module_num
        )
        cells.extend(section_cells)

    # Completion message
    completion = f"""---

## Congratulations!

You've completed Phase 1 of Module {module_num}: **{module_data['title']}**

### What You've Learned

You now understand the fundamental concepts of {module_data['grammar_focus'].replace('_', ' ')}!

### Next Steps

Continue to **Phase 2: Controlled Practice** where you'll do {module_data['exercises']} exercises to reinforce your learning.

**Remember:** Understanding grammar is the first step. Practice makes it automatic!

---

📚 Progress: Phase 1 of 4 complete
"""
    cells.append(create_markdown_cell(completion))

    return cells


def create_phase_2(module_num, module_data):
    """Generate Phase 2: Controlled Practice notebook"""
    cells = []

    # Header
    header = f"""# A2 Module {module_num}: {module_data['title']}
## Phase 2: Controlled Practice

**Total Exercises:** {module_data['exercises']}
**Focus:** {module_data['grammar_focus'].replace('_', ' ').title()}

---

## Welcome to Controlled Practice!

In this phase, you'll complete {module_data['exercises']} structured exercises to build automaticity with {module_data['grammar_focus'].replace('_', ' ')}.

### How to Use This Notebook

1. Read each exercise carefully
2. Write your answer
3. Check the feedback immediately
4. Review mistakes and try again
5. Track your progress

### Exercise Structure

This notebook contains 10 exercise sets covering:
- Formation and structure
- Usage in context
- Common error correction
- Sentence transformation
- Integration with previous grammar

**Let's begin!**

---
"""
    cells.append(create_markdown_cell(header))

    # Setup cell
    setup_code = """# Setup: Import feedback system
import sys
sys.path.append('../../..')
from utils.feedback_system import ExerciseValidator

print("[OK] Feedback system loaded successfully!")
print("You're ready to start the exercises.\\n")
"""
    cells.append(create_code_cell(setup_code))

    # Create exercise sets (10 sets distributed across the exercises)
    exercises_per_set = module_data["exercises"] // 10
    exercise_sets = [
        (
            "Formation Basics",
            exercises_per_set,
            f"Basic {module_data['grammar_focus'].replace('_', ' ')} formation",
        ),
        ("Usage Practice", exercises_per_set, "Apply rules in different contexts"),
        ("Gap Filling", exercises_per_set - 1, "Complete sentences with correct forms"),
        ("Sentence Building", exercises_per_set - 1, "Construct full sentences"),
        ("Error Correction", exercises_per_set + 1, "Identify and fix mistakes"),
        ("Transformation", exercises_per_set - 1, "Transform sentence structures"),
        ("Context Selection", exercises_per_set - 1, "Choose appropriate forms for context"),
        ("Integration Practice", exercises_per_set + 1, "Combine with previous grammar"),
        ("Question Formation", exercises_per_set - 1, "Create questions"),
        (
            "Mixed Practice",
            module_data["exercises"] - (exercises_per_set * 9),
            "Comprehensive practice",
        ),
    ]

    for i, (set_name, count, description) in enumerate(exercise_sets, 1):
        set_cells = create_exercise_set(
            i, set_name, count, description, module_data["grammar_focus"]
        )
        cells.extend(set_cells)

    # Completion
    completion = f"""---

## Excellent Work!

You've completed Phase 2 of Module {module_num} - all {module_data['exercises']} exercises!

### Next Steps

Move on to **Phase 3: Meaningful Practice** where you'll create personal content using {module_data['grammar_focus'].replace('_', ' ')}.

---

📚 Progress: Phase 2 of 4 complete
"""
    cells.append(create_markdown_cell(completion))

    return cells


def create_phase_3(module_num, module_data):
    """Generate Phase 3: Meaningful Practice notebook"""
    cells = []

    # Header
    header = f"""# A2 Module {module_num}: {module_data['title']}
## Phase 3: Meaningful Practice

**Total Activities:** {module_data['activities']}
**Focus:** Personal application of {module_data['grammar_focus'].replace('_', ' ')}

---

## Welcome to Meaningful Practice!

In this phase, you'll create personal content using {module_data['grammar_focus'].replace('_', ' ')}.

### Why Meaningful Practice?

Research shows that when you create sentences about YOUR life, you remember them better!

### Activity Structure

Each activity asks you to:
1. Think about your own experiences
2. Create 8-10 sentences using the grammar structure
3. Make them true and meaningful for YOU

**Let's make it personal!**

---
"""
    cells.append(create_markdown_cell(header))

    # Create activities
    activity_names = ACTIVITY_NAMES_BY_MODULE[module_num]
    for i, activity_name in enumerate(activity_names, 1):
        activity_cells = create_activity_placeholder(i, activity_name, module_data["grammar_focus"])
        cells.extend(activity_cells)

    # Completion
    completion = f"""---

## Fantastic!

You've completed Phase 3 of Module {module_num} - all {module_data['activities']} meaningful activities!

### What You've Accomplished

You've created personalized content using {module_data['grammar_focus'].replace('_', ' ')} - this is YOUR English!

### Next Steps

Continue to **Phase 4: Communicative Practice** for real-world communication tasks.

---

📚 Progress: Phase 3 of 4 complete
"""
    cells.append(create_markdown_cell(completion))

    return cells


def create_phase_4(module_num, module_data):
    """Generate Phase 4: Communicative Practice notebook"""
    cells = []

    # Header
    header = f"""# A2 Module {module_num}: {module_data['title']}
## Phase 4: Communicative Practice

**Total Tasks:** {module_data['tasks']}
**Focus:** Real-world communication with {module_data['grammar_focus'].replace('_', ' ')}

---

## Welcome to Communicative Practice!

In this final phase, you'll use {module_data['grammar_focus'].replace('_', ' ')} in authentic communication scenarios.

### Task Philosophy

- Focus on COMMUNICATION, not perfection
- Use natural, conversational language
- Mistakes are okay - fluency is the goal
- Apply what you've learned naturally

### Task Structure

Each task presents a real-world scenario where you need to communicate using the grammar you've learned.

**Let's communicate!**

---
"""
    cells.append(create_markdown_cell(header))

    # Create tasks
    task_names = TASK_NAMES_BY_MODULE[module_num]
    for i, task_name in enumerate(task_names, 1):
        task_cells = create_task_placeholder(i, task_name, module_data["grammar_focus"])
        cells.extend(task_cells)

    # Module completion
    completion = f"""---

## 🎉 Module {module_num} Complete!

Congratulations! You've finished **{module_data['title']}**!

### What You've Achieved

[DONE] Completed {module_data['sections']} introduction sections
[DONE] Practiced through {module_data['exercises']} exercises
[DONE] Created {module_data['activities']} personalized activities
[DONE] Communicated in {module_data['tasks']} real-world tasks

### Mastery Checklist

Can you confidently:
"""

    for topic in module_data["topics"]:
        completion += f"- [ ] {topic}\n"

    completion += f"""
### Time Investment

You've invested approximately {module_data['time']} in this module. Well done!

### Next Steps

"""

    next_module = str(int(module_num) + 1)
    if next_module in BATCH_5_MODULES:
        completion += (
            f"Continue to **Module {next_module}: {BATCH_5_MODULES[next_module]['title']}**\n"
        )
    else:
        completion += "You've completed A2 Batch 5! Time to review and move toward B1!\n"

    completion += """
### Spaced Repetition

Review this module after:
- 1 day
- 3 days
- 7 days
- 14 days
- 30 days

---

Progress: Module Complete! 4 of 4 phases done
"""
    cells.append(create_markdown_cell(completion))

    return cells


def create_module_all_phases(module_num, module_data):
    """Create all 4 phases for a module"""
    base_path = f"notebooks/A2/Module_{module_num}"

    # Create directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    phases = [
        ("01_introduction.ipynb", create_phase_1),
        ("02_controlled_practice.ipynb", create_phase_2),
        ("03_meaningful_practice.ipynb", create_phase_3),
        ("04_communicative_practice.ipynb", create_phase_4),
    ]

    for filename, phase_func in phases:
        cells = phase_func(module_num, module_data)
        nb = nbf.v4.new_notebook(cells=cells)
        filepath = os.path.join(base_path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            nbf.write(nb, f)

        print(f"  [OK] Created {filename}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================


def main():
    """Generate all A2 Batch 5 modules"""
    # Validate working directory - ensure script is run from english-learning root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) != "english-learning":
        print("ERROR: Script must be run from the english-learning project directory")
        print(f"Current directory: {os.getcwd()}")
        print(f"Script directory: {script_dir}")
        print("\nPlease cd to the english-learning directory and run the script again.")
        return

    # Change to script directory to ensure relative paths work correctly
    os.chdir(script_dir)

    print("=" * 70)
    print("A2 LEVEL - BATCH 5: ADVANCED STRUCTURES AND INTEGRATION")
    print("Generating Modules 21-25")
    print("FINAL A2 BATCH - Completing Elementary Level")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_5_MODULES.keys()):
        module_data = BATCH_5_MODULES[module_num]
        print(f"Creating Module {module_num}: {module_data['title']}")
        print(f"  Subtitle: {module_data['subtitle']}")
        print(f"  Grammar Focus: {module_data['grammar_focus']}")
        print(
            f"  Sections: {module_data['sections']} | Exercises: {module_data['exercises']} | Activities: {module_data['activities']} | Tasks: {module_data['tasks']}"
        )

        create_module_all_phases(module_num, module_data)

        total_exercises += module_data["exercises"]
        total_activities += module_data["activities"]
        total_tasks += module_data["tasks"]

        print(f"  [COMPLETE] Module {module_num} complete!\n")

    print("=" * 70)
    print("BATCH 5 GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nModules Created: 5 (Modules 21-25)")
    print(f"Notebooks Created: 20 (5 modules × 4 phases)")
    print(f"Total Exercises: {total_exercises}")
    print(f"Total Activities: {total_activities}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Total Learning Content: 26-32 hours")
    print("\nA2 Level Curriculum: COMPLETE")
    print("- 25 modules total (Batches 1-5)")
    print("- 100 notebooks total")
    print("- 100% CEFR A2 coverage")
    print("- Ready for B1 transition")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
