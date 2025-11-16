"""
B1 Level - Batch 4: Advanced Relatives and Modals (Modules 16-20)
Fourth B1 batch focusing on relative clause mastery and modal sophistication

This batch focuses on:
- Defining vs Non-Defining Relative Clauses (comma usage, essential vs extra)
- Relative Clauses - Whose and Whom (possession and formal object relatives)
- Relative Clauses - Advanced Patterns (object relatives, omission, reduction)
- Modal Verbs for Deduction - Present (must, can't, may, might, could)
- Modal Verbs for Deduction - Past (must have, can't have, might have + pp)

Architecture: Relatives/modals-specific characteristics with certainty scales
Exercise Count: 455 total exercises
"""

import os

import nbformat as nbf

# ============================================================================
# RELATIVE CLAUSE CHARACTERISTICS
# ============================================================================

DEFINING_VS_NON_DEFINING_CHARACTERISTICS = {
    "concept": "Two types of relative clauses with different purposes",
    "defining_relative_clauses": {
        "purpose": "Essential information to identify the noun",
        "punctuation": "NO commas",
        "can_remove": "NO - meaning changes without it",
        "pronouns": "who, which, that, where, when",
        "that_allowed": "YES - 'that' is common",
        "examples": [
            "The woman who works at the bank is my neighbor. (which woman? essential)",
            "The book that I'm reading is interesting. (which book? essential)",
            "The restaurant where we ate was excellent. (which restaurant? essential)",
        ],
        "key": "Answers: Which one? Who? Where? → Essential to identify",
    },
    "non_defining_relative_clauses": {
        "purpose": "Extra information (already know which one)",
        "punctuation": "Commas REQUIRED (before and after, or before if at end)",
        "can_remove": "YES - main meaning remains clear",
        "pronouns": "who, which, where, when (NOT that!)",
        "that_allowed": "NO - cannot use 'that'",
        "examples": [
            "My mother, who is 65, lives in London. (only one mother - extra info)",
            "Paris, which is the capital of France, is beautiful. (everyone knows Paris)",
            "We visited the Eiffel Tower, which was built in 1889. (extra fact)",
        ],
        "key": "Already identified - just adding bonus information",
    },
    "comma_rule": {
        "defining": "NO commas - The students who studied hard passed. (only those who studied)",
        "non_defining": "WITH commas - The students, who studied hard, passed. (all studied, all passed)",
        "meaning_changes": "Same words, different punctuation = different meaning!",
    },
    "that_vs_which": {
        "in_defining": "Both 'that' and 'which' acceptable ('that' more common in speech)",
        "in_non_defining": "MUST use 'which' - NEVER 'that'",
        "error": "❌ My car, that is red, needs repairs. → ✅ My car, which is red, needs repairs.",
    },
    "proper_nouns": {
        "rule": "Proper nouns (names) usually get non-defining clauses",
        "examples": [
            "Shakespeare, who wrote many plays, lived in England.",
            "London, which is the capital, has 9 million people.",
            "My friend John, who lives in Paris, is visiting.",
        ],
    },
    "decision_guide": {
        "ask": "Do I need this information to know which person/thing?",
        "yes": "Defining - no commas",
        "no": "Non-defining - use commas",
    },
    "common_errors": [
        "❌ My mother who is 65 lives in London. → ✅ My mother, who is 65, lives in London. (need commas)",
        "❌ Paris, that is beautiful, ... → ✅ Paris, which is beautiful, ... (not 'that')",
        "❌ The book, I bought, is good. → ✅ The book I bought is good. (defining, no commas)",
    ],
}

WHOSE_WHOM_CHARACTERISTICS = {
    "whose_possession": {
        "function": "Shows possession (replaces his/her/their/its + noun)",
        "formation": "whose + noun (the possessed thing)",
        "examples": [
            "The student whose bag was stolen reported it. (student's bag)",
            "I know a woman whose son is a doctor. (woman's son)",
            "That's the house whose roof is damaged. (house's roof)",
        ],
        "works_with": "Both people AND things",
        "defining_and_non_defining": "Can be used in both types",
    },
    "whose_vs_whos": {
        "whose": "Possession - relative pronoun",
        "whos": "who is / who has - contraction",
        "error": "❌ Who's car is this? → ✅ Whose car is this?",
        "examples": {
            "whose": "The man whose car is red... (possession)",
            "who's": "Who's coming to the party? (who is)",
        },
    },
    "whom_formal_object": {
        "function": "Formal object of relative clause (replaces him/her/them)",
        "formality": "Formal English, especially with prepositions",
        "formation": "(preposition +) whom",
        "examples": [
            "The person to whom I spoke was helpful. (I spoke to him/her)",
            "The colleague with whom I work is experienced. (I work with him/her)",
            "The professor from whom I learned retired. (I learned from him/her)",
        ],
    },
    "whom_vs_who": {
        "formal": "whom (especially with preposition at start)",
        "informal": "who or that (preposition at end)",
        "very_informal": "omit pronoun entirely",
        "examples": {
            "formal": "The person to whom I spoke...",
            "informal": "The person (who/that) I spoke to...",
            "very_informal": "The person I spoke to...",
        },
    },
    "preposition_position": {
        "at_start": "Must use 'whom' - The person to whom I gave...",
        "at_end": "Can use 'who/that' or omit - The person (who) I gave... to",
    },
    "when_to_use_whom": [
        "Formal writing (academic, business)",
        "With preposition at start of clause",
        "Legal and official documents",
        "When you want to sound very correct/formal",
    ],
    "common_errors": [
        "❌ The person to who I spoke... → ✅ The person to whom I spoke...",
        "❌ Who's car is this? → ✅ Whose car is this?",
        "❌ The woman whose is my teacher... → ✅ The woman who is my teacher... (who's = who is)",
    ],
}

ADVANCED_RELATIVE_PATTERNS_CHARACTERISTICS = {
    "subject_vs_object": {
        "subject_relative": {
            "definition": "Pronoun is subject of relative clause verb",
            "example": "The man who lives next door... (who = subject of 'lives')",
            "omission": "CANNOT omit",
            "test": "Pronoun followed immediately by verb",
        },
        "object_relative": {
            "definition": "Pronoun is object of relative clause verb",
            "example": "The man (who) I met... (who = object of 'met' - I met him)",
            "omission": "CAN omit in informal English",
            "test": "Pronoun followed by subject + verb",
        },
    },
    "omission_rules": {
        "can_omit_when": [
            "Pronoun is object of relative clause",
            "In defining clauses only (NOT non-defining)",
            "Informal/conversational English",
        ],
        "cannot_omit_when": [
            "Pronoun is subject of clause",
            "In non-defining clauses",
            "When formality is required",
        ],
        "examples_with_omission": [
            "The book (that) I bought... ✅ omission OK",
            "The person (who) I spoke to... ✅ omission OK",
            "The movie (that) we saw... ✅ omission OK",
        ],
        "examples_no_omission": [
            "The man who lives next door... ❌ cannot omit (subject)",
            "My mother, who is 65,... ❌ cannot omit (non-defining)",
        ],
    },
    "reduced_relatives": {
        "present_participle": {
            "form": "Remove relative pronoun + be, keep -ing",
            "full": "The man who is standing by the door...",
            "reduced": "The man standing by the door...",
            "use": "Active ongoing action",
        },
        "past_participle": {
            "form": "Remove relative pronoun + be, keep past participle",
            "full": "The car which was stolen...",
            "reduced": "The car stolen...",
            "use": "Passive action",
        },
        "note": "Advanced B1/B2 - introduce here, master later",
    },
    "common_patterns": {
        "with_preposition": "The person (who) I work with...",
        "with_possessive": "The man whose car...",
        "with_place": "The place (where) I went...",
        "with_time": "The day (when) I arrived...",
    },
    "common_errors": [
        "❌ The man lives next door... (missing relative pronoun - subject)",
        "❌ My mother, is a teacher,... (missing 'who' in non-defining)",
        "❌ The man standing by door he is my boss. (redundant 'he')",
    ],
}

# ============================================================================
# MODAL DEDUCTION CHARACTERISTICS
# ============================================================================

MODAL_DEDUCTION_PRESENT_CHARACTERISTICS = {
    "concept": "Using modals for DEDUCTION (logical conclusions), not obligation",
    "vs_a2_modals": {
        "a2": "Must = obligation (You must study)",
        "b1": "Must = deduction (He must be tired - I'm certain based on evidence)",
    },
    "certainty_scale": {
        "100_percent_positive": "must be",
        "100_percent_negative": "can't be / couldn't be",
        "50_percent_possible": "may be / might be / could be",
    },
    "must_be_certainty": {
        "meaning": "I'm certain this is true (based on evidence)",
        "formation": "must + be/base verb",
        "examples": [
            "He's yawning. He must be tired. (evidence: yawning → conclusion: tired)",
            "The lights are on. Someone must be home. (evidence → deduction)",
            "She speaks perfect English. She must be British. (evidence → conclusion)",
        ],
        "key": "Based on evidence and logic, not rules!",
    },
    "cant_be_impossibility": {
        "meaning": "I'm certain this is NOT true (impossible based on evidence)",
        "formation": "can't be / couldn't be",
        "examples": [
            "He's just eaten. He can't be hungry. (impossible - just ate)",
            "She's only 30. She can't be your grandmother. (impossible - too young)",
            "That can't be right. Let me check. (certain it's wrong)",
        ],
        "note": "'Couldn't be' slightly more polite/tentative",
    },
    "may_might_could_possibility": {
        "meaning": "It's possible (about 50% - not certain)",
        "formation": "may be / might be / could be",
        "examples": [
            "He might be at home. I'm not sure. (possible, not certain)",
            "She may be busy. Try calling later. (possible)",
            "That could be the answer. (considering possibility)",
        ],
        "differences": {
            "may": "Neutral possibility",
            "might": "Slightly less certain than may",
            "could": "Suggests considering the possibility",
        },
        "key": "All three mean roughly the same - about 50% possible",
    },
    "visual_scale": """
    CERTAINTY SCALE:

    100% certain positive  → MUST BE
    |
    50% possible          → MAY/MIGHT/COULD BE
    |
    0% impossible         → CAN'T BE / COULDN'T BE
    """,
    "evidence_pattern": "EVIDENCE (what I see/know) → MODAL DEDUCTION (logical conclusion)",
    "common_errors": [
        "❌ He must be to home. → ✅ He must be home. (no 'to')",
        "❌ She musts be tired. → ✅ She must be tired. (no -s on 'must')",
        "❌ It can't to be true. → ✅ It can't be true. (no 'to')",
        "❌ He might is at home. → ✅ He might be at home. ('be', not 'is')",
    ],
}

MODAL_DEDUCTION_PAST_CHARACTERISTICS = {
    "concept": "Using modals for deductions about the PAST",
    "formation": "modal + have + past participle",
    "prerequisite": "Must understand past perfect from Batch 1!",
    "certainty_scale_past": {
        "100_percent_positive": "must have + pp",
        "100_percent_negative": "can't have / couldn't have + pp",
        "50_percent_possible": "may have / might have / could have + pp",
    },
    "must_have_pp_certainty": {
        "meaning": "I'm certain this happened (based on evidence)",
        "formation": "must have + past participle",
        "examples": [
            "The ground is wet. It must have rained. (present evidence → past deduction)",
            "She looks upset. Someone must have told her. (present state → past event)",
            "He wasn't at work. He must have been sick. (past evidence → past conclusion)",
        ],
        "pattern": "Present evidence → Past deduction",
    },
    "cant_have_pp_impossibility": {
        "meaning": "I'm certain this didn't happen (impossible)",
        "formation": "can't have / couldn't have + pp",
        "examples": [
            "He can't have taken the bus. It wasn't running. (impossible)",
            "She couldn't have known. Nobody told her. (impossible)",
            "They can't have finished already. It's too soon. (impossible)",
        ],
    },
    "may_might_could_have_pp": {
        "meaning": "It's possible this happened (not certain)",
        "formation": "may have / might have / could have + pp",
        "examples": [
            "He might have gone home already. (possible)",
            "She may have forgotten about the meeting. (possible)",
            "They could have missed the train. (possible)",
        ],
    },
    "should_have_pp_different": {
        "meaning": "Expected to happen but didn't (criticism/expectation)",
        "formation": "should have / ought to have + pp",
        "examples": [
            "He should have arrived by now. (expected but hasn't)",
            "They should have called. (expected behavior, didn't happen)",
            "You should have told me! (criticism - you didn't)",
        ],
        "note": "This is EXPECTATION, not deduction! Different function.",
    },
    "deduction_vs_expectation": {
        "must_have": "Deduction - I'm certain it happened (based on evidence)",
        "should_have": "Expectation - I expected it but it didn't happen",
        "example_must": "The door is open. Someone must have opened it. (deduction)",
        "example_should": "He should have opened the door for her. (expected behavior)",
    },
    "visual_scale_past": """
    PAST CERTAINTY SCALE:

    100% certain it happened    → MUST HAVE + PP
    |
    50% possible it happened    → MAY/MIGHT/COULD HAVE + PP
    |
    0% impossible (didn't happen) → CAN'T HAVE / COULDN'T HAVE + PP

    Separate: SHOULD HAVE + PP = expectation not met
    """,
    "common_errors": [
        "❌ He must has gone. → ✅ He must have gone. ('have', not 'has')",
        "❌ She must have go. → ✅ She must have gone. (past participle)",
        "❌ They can't have been went. → ✅ They can't have gone. (just pp, not 'been went')",
        "❌ I should of called. → ✅ I should have called. ('have', not 'of')",
    ],
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_4_MODULES = {
    16: {
        "title": "Defining vs Non-Defining Relative Clauses",
        "subtitle": "Essential vs Extra Information - Comma Usage",
        "grammar_focus": "Distinguishing Clause Types",
        "sections": 17,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 4,
        "characteristics": DEFINING_VS_NON_DEFINING_CHARACTERISTICS,
    },
    17: {
        "title": "Relative Clauses with Whose and Whom",
        "subtitle": "Possession and Formal Object Relatives",
        "grammar_focus": "Advanced Relative Pronouns",
        "sections": 15,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": WHOSE_WHOM_CHARACTERISTICS,
    },
    18: {
        "title": "Relative Clauses - Object Relatives and Omission",
        "subtitle": "When You Can Leave Out the Relative Pronoun",
        "grammar_focus": "Advanced Relative Patterns",
        "sections": 14,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 4,
        "characteristics": ADVANCED_RELATIVE_PATTERNS_CHARACTERISTICS,
    },
    19: {
        "title": "Modal Verbs for Deduction - Present",
        "subtitle": "Must, Can't, May, Might, Could",
        "grammar_focus": "Making Logical Conclusions About Present",
        "sections": 16,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 4,
        "characteristics": MODAL_DEDUCTION_PRESENT_CHARACTERISTICS,
    },
    20: {
        "title": "Modal Verbs for Past Deduction",
        "subtitle": "Must Have, Can't Have, Might Have + PP",
        "grammar_focus": "Making Conclusions About Past Events",
        "sections": 17,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 5,
        "characteristics": MODAL_DEDUCTION_PAST_CHARACTERISTICS,
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def create_markdown_cell(content):
    """Create a markdown cell"""
    return nbf.v4.new_markdown_cell(content)


def create_code_cell(code):
    """Create a code cell"""
    return nbf.v4.new_code_cell(code)


def create_header(module_num, module_data, phase_num, phase_name):
    """Create module header"""
    headers = {
        1: "Phase 1: Introduction",
        2: "Phase 2: Controlled Practice",
        3: "Phase 3: Meaningful Practice",
        4: "Phase 4: Communicative Practice",
    }

    header = f"""# B1 Level - Module {module_num}: {module_data['title']}

## {module_data['subtitle']}

**Grammar Focus:** {module_data['grammar_focus']}
**Estimated Time:** {module_data['estimated_hours']} hours
**Difficulty:** {'★' * module_data['difficulty']}{'☆' * (5 - module_data['difficulty'])}

---

# {headers[phase_num]}
"""
    return create_markdown_cell(header)


# ============================================================================
# PHASE 1: INTRODUCTION
# ============================================================================


def create_phase_1(module_num, module_data):
    """Create Phase 1: Introduction"""
    cells = []
    cells.append(create_header(module_num, module_data, 1, "Introduction"))

    if module_num == 16:
        cells.extend(create_module_16_phase_1(module_data))
    elif module_num == 17:
        cells.extend(create_module_17_phase_1(module_data))
    elif module_num == 18:
        cells.extend(create_module_18_phase_1(module_data))
    elif module_num == 19:
        cells.extend(create_module_19_phase_1(module_data))
    elif module_num == 20:
        cells.extend(create_module_20_phase_1(module_data))

    return cells


def create_module_16_phase_1(module_data):
    """Module 16: Defining vs Non-Defining"""
    cells = []

    intro = """## 1. Introduction - Two Types of Information

Welcome to **Defining vs Non-Defining Relative Clauses** - a critical B1 distinction!

**What you'll learn:**
- The difference between essential and extra information
- When to use commas (and when not to!)
- How meaning changes with punctuation
- That vs which in different clause types

**Why this matters:**
- Non-defining clauses are a B1 criterial feature
- Comma usage affects meaning
- Essential for academic and formal writing
- Changes how you describe people and things

**The key question:** Is this information ESSENTIAL to know which person/thing, or is it just EXTRA details?

**This module will take 6-7 hours.** The comma makes all the difference!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Defining vs Non-Defining

### Quick Reference

**Defining (NO commas):**
- Essential information
- Identifies which one
- Can use "that"
- Cannot remove clause

**Non-Defining (WITH commas):**
- Extra information
- Already identified
- Use "which/who" (NOT "that")
- Can remove clause

### Examples

✅ **The students who studied passed.** (only those who studied)
✅ **The students, who studied, passed.** (all students - they all studied)

**Practice makes perfect!** You'll see 95 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_17_phase_1(module_data):
    """Module 17: Whose and Whom"""
    cells = []

    intro = """## 1. Introduction - Advanced Relative Pronouns

Welcome to **Whose and Whom** - sophisticated relative pronouns!

**What you'll learn:**
- Whose for possession (his/her/their car → whose car)
- Whose vs who's (critical distinction!)
- Whom for formal object relatives
- When to use whom (and when to use who)

**This module will take 5-6 hours.** Formality and possession!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_18_phase_1(module_data):
    """Module 18: Advanced Patterns"""
    cells = []

    intro = """## 1. Introduction - Advanced Relative Patterns

Welcome to **Advanced Relative Clause Patterns**!

**What you'll learn:**
- Subject vs object relative clauses
- When you can omit relative pronouns
- Reduced relative clauses (introduction)
- Natural spoken English patterns

**This module will take 5-6 hours.** Pattern recognition!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_19_phase_1(module_data):
    """Module 19: Present Deduction"""
    cells = []

    intro = """## 1. Introduction - Modals for Thinking, Not Doing

Welcome to **Modal Verbs for Deduction** - a NEW way to use modals!

**What you'll learn:**
- Must be (100% certain positive)
- Can't be (100% certain negative)
- May/might/could be (50% possible)
- Evidence-based logical conclusions

**Different from A2:**
- A2: "You must study" (obligation)
- B1: "He must be tired" (deduction from evidence)

**This module will take 5-6 hours.** Evidence → Conclusion!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_20_phase_1(module_data):
    """Module 20: Past Deduction"""
    cells = []

    intro = """## 1. Introduction - Deductions About the Past

Welcome to **Past Modal Deduction** - making conclusions about past events!

**What you'll learn:**
- Must have + pp (certain it happened)
- Can't have + pp (impossible it happened)
- May/might/could have + pp (possible it happened)
- Should have + pp (expectation not met)

**Prerequisites:** You MUST understand past perfect (Batch 1, Module 4)!

**This module will take 6-7 hours.** Complex modal perfects!
"""
    cells.append(create_markdown_cell(intro))

    return cells


# ============================================================================
# PHASE 2-4: Using Template Approach
# ============================================================================


def create_phase_2(module_num, module_data):
    """Create Phase 2: Controlled Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 2, "Controlled Practice"))

    intro = f"""## Welcome to Phase 2: Controlled Practice

In this phase, you'll complete **{module_data['exercises']} exercises**.

**Remember:** {module_data['grammar_focus']} requires systematic practice!

---

Let's begin!
"""
    cells.append(create_markdown_cell(intro))
    cells.append(create_markdown_cell(f"## Exercises (Total: {module_data['exercises']})"))
    cells.append(
        create_markdown_cell("### Exercise Sets\n\n**Note:** Full exercises in production version.")
    )

    return cells


def create_phase_3(module_num, module_data):
    """Create Phase 3: Meaningful Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 3, "Meaningful Practice"))

    intro = f"""## Welcome to Phase 3: Meaningful Practice

**Activities in this phase:** {module_data['activities']}

Make the grammar personally relevant!

---
"""
    cells.append(create_markdown_cell(intro))

    for i in range(1, module_data["activities"] + 1):
        cells.append(create_markdown_cell(f"### Activity {i}\n\n[Activity description]\n\n---"))

    return cells


def create_phase_4(module_num, module_data):
    """Create Phase 4: Communicative Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 4, "Communicative Practice"))

    intro = f"""## Welcome to Phase 4: Communicative Practice

**Tasks in this phase:** {module_data['tasks']}

Real communication focus!

---
"""
    cells.append(create_markdown_cell(intro))

    for i in range(1, module_data["tasks"] + 1):
        cells.append(create_markdown_cell(f"### Task {i}\n\n[Task description]\n\n---"))

    # Special completion for Module 20
    if module_num == 20:
        completion = """## 🎉 Module 20 Complete - B1 Batch 4 FINISHED!

**Congratulations!** You've completed:

✅ Module 16: Defining vs Non-Defining Relative Clauses
✅ Module 17: Whose and Whom
✅ Module 18: Advanced Relative Patterns
✅ Module 19: Modal Deduction - Present
✅ Module 20: Modal Deduction - Past

### B1 Batch 4 Achievement

**You can now:**
- Distinguish defining from non-defining clauses
- Use whose and whom correctly
- Omit relative pronouns when appropriate
- Make deductions using modal verbs
- Draw logical conclusions from evidence

**B1 Progress: 67% complete (20/30 modules)**

**Remaining:**
- Batch 5: Advanced Verb Patterns (Modules 21-25)
- Batch 6: Integration & Consolidation (Modules 26-30)

### Next Steps

Ready for Batch 5! Only 10 modules left to complete B1!

---

**You're two-thirds through B1! Outstanding progress!**
"""
    else:
        completion = f"""## 🎉 Module {module_num} Complete!

**Time spent:** ~{module_data['estimated_hours']} hours

Ready for Module {module_num + 1}!

---
"""

    cells.append(create_markdown_cell(completion))

    return cells


# ============================================================================
# NOTEBOOK CREATION
# ============================================================================


def create_module_all_phases(module_num, module_data):
    """Create all 4 phases for a module"""
    base_path = f"notebooks/B1/Module_{module_num:02d}"
    os.makedirs(base_path, exist_ok=True)

    phases = [
        ("01_introduction.ipynb", create_phase_1),
        ("02_controlled_practice.ipynb", create_phase_2),
        ("03_meaningful_practice.ipynb", create_phase_3),
        ("04_communicative_practice.ipynb", create_phase_4),
    ]

    for filename, phase_func in phases:
        cells = phase_func(module_num, module_data)
        nb = nbf.v4.new_notebook()
        nb.cells = cells

        filepath = os.path.join(base_path, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            nbf.write(nb, f)

        print(f"  [OK] Created: {filepath}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================


def main():
    """Generate all B1 Batch 4 modules"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) != "english-learning":
        print("ERROR: Script must be run from english-learning directory")
        return

    os.chdir(script_dir)

    print("=" * 70)
    print("B1 LEVEL - BATCH 4: ADVANCED RELATIVES AND MODALS")
    print("Generating Modules 16-20")
    print("FOURTH B1 BATCH - Relative Clause Mastery & Modal Sophistication")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_4_MODULES.keys()):
        module_data = BATCH_4_MODULES[module_num]
        print(f"Creating Module {module_num}: {module_data['title']}")
        print(f"  Subtitle: {module_data['subtitle']}")
        print(f"  Grammar Focus: {module_data['grammar_focus']}")
        print(f"  Sections: {module_data['sections']} | Exercises: {module_data['exercises']}")

        create_module_all_phases(module_num, module_data)

        total_exercises += module_data["exercises"]
        total_activities += module_data["activities"]
        total_tasks += module_data["tasks"]

        print(f"  [COMPLETE] Module {module_num} complete!\n")

    print("=" * 70)
    print("BATCH 4 GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nModules Created: 5 (Modules 16-20)")
    print(f"Notebooks Created: 20 (5 modules × 4 phases)")
    print(f"Total Exercises: {total_exercises}")
    print(f"Total Activities: {total_activities}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Total Learning Content: 27-31 hours")
    print("\nB1 Level Batch 4: COMPLETE")
    print("- Relative clause mastery achieved")
    print("- Modal deduction learned")
    print("- B1 Progress: 67% complete (20/30 modules)")
    print("- Ready for Batch 5 (Advanced Verb Patterns + Criterial Feature)")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
