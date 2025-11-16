"""
B1 Level - Batch 2: Hypothetical Conditionals (Modules 6-10)
Second B1 batch focusing on unreal and hypothetical situations

This batch focuses on:
- Second Conditional (hypothetical present/future)
- Third Conditional (impossible past)
- Mixed Conditionals (combining time frames)
- Conditional Alternatives (unless, provided that, as long as, in case)
- Wish and If Only (regrets and wishes)

Architecture: Conditional-specific characteristics with reality level analysis
Exercise Count: 455 total exercises
"""

import os

import nbformat as nbf

# ============================================================================
# CONDITIONAL CHARACTERISTICS - Conditional-Specific Dictionaries
# ============================================================================

SECOND_CONDITIONAL_CHARACTERISTICS = {
    "form": "If + past simple, would + base verb",
    "reality_level": "UNREAL - hypothetical, unlikely, or imaginary",
    "time_reference": "Present or future (but unreal)",
    "key_concept": "Past tense signals UNREALITY, not past time!",
    "uses": {
        "hypothetical_present": {
            "description": "Imagining different present reality",
            "examples": [
                "If I lived in Paris, I would visit museums every day. (I don't live in Paris)",
                "If I were rich, I would travel the world. (I'm not rich)",
                "If I had a car, I would drive to work. (I don't have a car)",
            ],
        },
        "unlikely_future": {
            "description": "Very unlikely future possibilities",
            "examples": [
                "If I won the lottery, I would buy a house. (very unlikely)",
                "If aliens landed tomorrow, people would panic. (extremely unlikely)",
                "If oil ran out, we would need alternative energy. (hypothetical future)",
            ],
        },
        "advice": {
            "description": "Giving advice with 'If I were you'",
            "examples": [
                "If I were you, I would study harder.",
                "If I were in your position, I would accept the offer.",
                "If I were you, I wouldn't worry about it.",
            ],
            "note": "Use 'were' for all persons (subjunctive), though 'was' is acceptable informally",
        },
    },
    "vs_first_conditional": {
        "first": {
            "reality": "Real possibility",
            "example": "If it rains, I will stay home. (might really rain)",
        },
        "second": {
            "reality": "Unreal/unlikely",
            "example": "If it rained every day, I would stay home. (not real - hypothetical)",
        },
    },
    "modals": {
        "would": "Most common - expected result",
        "could": "Ability or possibility",
        "might": "Less certain possibility",
    },
    "subjunctive": {
        "rule": "'If I/he/she/it were' (formal/written)",
        "informal": "'If I/he/she/it was' (conversational)",
        "recommendation": "Use 'were' in writing and formal situations",
    },
    "common_errors": [
        "❌ If I will have time, I will help. → ✅ If I had time, I would help.",
        "❌ If I would be rich, I would travel. → ✅ If I were rich, I would travel.",
        "❌ If I had money, I will buy it. → ✅ If I had money, I would buy it.",
        "❌ If I am you, I would go. → ✅ If I were you, I would go.",
    ],
}

THIRD_CONDITIONAL_CHARACTERISTICS = {
    "form": "If + past perfect, would have + past participle",
    "reality_level": "IMPOSSIBLE - past that cannot be changed",
    "time_reference": "Past only",
    "key_concept": "Imagining how past could have been different (but can't change it)",
    "uses": {
        "regrets": {
            "description": "Expressing regret about past actions",
            "examples": [
                "If I had studied harder, I would have passed the exam. (I didn't study, I didn't pass)",
                "If I had known about the party, I would have gone. (I didn't know, I didn't go)",
                "If I had taken that job, I would be happier now. (I didn't take it - regret)",
            ],
        },
        "criticism": {
            "description": "Softened criticism or blame",
            "examples": [
                "If you had called me, I would have helped you. (you didn't call, I didn't help)",
                "If he had listened to advice, he wouldn't have made that mistake.",
                "If they had been more careful, the accident wouldn't have happened.",
            ],
        },
        "relief": {
            "description": "Expressing relief about what didn't happen",
            "examples": [
                "If I had taken that job, I would have been miserable. (glad I didn't)",
                "If we had bought that house, we would have lost money. (lucky we didn't)",
                "If I had married him, I would have been unhappy. (relief)",
            ],
        },
        "speculation": {
            "description": "Speculating about past events",
            "examples": [
                "If he had known the truth, he would have acted differently.",
                "If they had had more time, they could have finished the project.",
                "If the weather had been better, we might have gone to the beach.",
            ],
        },
    },
    "modals": {
        "would_have": "Expected result (most common)",
        "could_have": "Ability or possibility in past",
        "might_have": "Less certain past possibility",
    },
    "vs_second_conditional": {
        "second": {
            "time": "Present/future (unreal)",
            "example": "If I were rich, I would travel. (I'm not rich NOW)",
        },
        "third": {
            "time": "Past (impossible to change)",
            "example": "If I had been rich, I would have traveled. (I wasn't rich THEN)",
        },
    },
    "common_errors": [
        "❌ If I would have known, I would have come. → ✅ If I had known, I would have come.",
        "❌ If I studied harder, I would have passed. → ✅ If I had studied harder, I would have passed.",
        "❌ If I had money then, I will have bought it. → ✅ If I had had money then, I would have bought it.",
        "❌ I wish I would have seen it. → ✅ I wish I had seen it.",
    ],
}

MIXED_CONDITIONALS_CHARACTERISTICS = {
    "concept": "Combining different time frames in one conditional",
    "types": {
        "type_1": {
            "structure": "If + past perfect, would + base verb",
            "time_frame": "Past condition → Present result",
            "explanation": "Past action (or lack of action) has result in present",
            "examples": [
                "If I had studied medicine, I would be a doctor now. (didn't study THEN → not a doctor NOW)",
                "If we had bought that house, we would be living there now. (didn't buy THEN → not living there NOW)",
                "If I had practiced more, I would be better at piano now. (didn't practice THEN → not good NOW)",
            ],
        },
        "type_2": {
            "structure": "If + past simple, would have + past participle",
            "time_frame": "Present condition → Past result",
            "explanation": "Present/general characteristic affected past event",
            "examples": [
                "If I were more organized, I would have remembered your birthday. (not organized NOW → didn't remember THEN)",
                "If he weren't so stubborn, he would have apologized yesterday. (stubborn NOW → didn't apologize THEN)",
                "If I spoke French, I would have enjoyed Paris more. (don't speak NOW → didn't enjoy THEN)",
            ],
        },
    },
    "when_to_use": {
        "type_1_usage": "Past decisions/actions affecting your current situation",
        "type_2_usage": "Permanent characteristics affecting past events",
        "common_type": "Type 1 is much more common than Type 2",
    },
    "timeline_visual": """
    Type 1: Past → Present
    PAST ACTION ------→ PRESENT RESULT
    (didn't do)         (situation now)
    If + past perfect   would + base

    Type 2: Present → Past
    PRESENT STATE ------→ PAST EVENT
    (characteristic)    (what happened)
    If + past simple    would have + pp
    """,
    "common_errors": [
        "❌ If I studied medicine, I will be a doctor. → ✅ If I had studied medicine, I would be a doctor now.",
        "❌ If I am more organized, I would have remembered. → ✅ If I were more organized, I would have remembered.",
        "❌ If I had studied, I will be smart now. → ✅ If I had studied, I would be smarter now.",
    ],
}

CONDITIONAL_ALTERNATIVES_CHARACTERISTICS = {
    "unless": {
        "meaning": "if...not (exception)",
        "structure": "Unless + positive clause (NOT negative)",
        "examples": [
            "Unless you study, you'll fail. = If you don't study, you'll fail.",
            "I won't go unless you come with me. = I won't go if you don't come.",
            "Unless it rains, we'll have the party outside. = If it doesn't rain...",
        ],
        "common_error": "❌ Unless you don't study... → ✅ Unless you study... (no double negative)",
    },
    "provided_that": {
        "meaning": "if (prerequisite/requirement)",
        "formality": "More formal than 'if'",
        "examples": [
            "You can borrow my car provided that you drive carefully. (requirement)",
            "I'll help you provided that you promise to study. (condition)",
            "We'll go provided that the weather is good. (prerequisite)",
        ],
        "alternative": "Providing that (same meaning)",
    },
    "as_long_as": {
        "meaning": "if/only if (requirement/condition)",
        "emphasis": "Emphasizes the condition as important",
        "examples": [
            "You can stay as long as you help with chores. (requirement)",
            "I don't mind as long as you're happy. (condition)",
            "As long as you work hard, you'll succeed. (key condition)",
        ],
    },
    "only_if": {
        "meaning": "exclusive condition - nothing else will work",
        "emphasis": "Strong emphasis on this specific condition",
        "examples": [
            "I'll go only if you go too. (won't go otherwise)",
            "You can pass only if you score 80% or higher. (no other way)",
            "Only if you apologize will I forgive you. (inversion possible)",
        ],
    },
    "in_case": {
        "meaning": "as a precaution (different from 'if'!)",
        "key_difference": "Preparation, not condition",
        "vs_if": {
            "in_case": "Take an umbrella in case it rains. (might or might not rain - be prepared)",
            "if": "Take an umbrella if it rains. (take it WHEN it rains, not before)",
        },
        "examples": [
            "I'll take my phone in case you need to call me. (precaution)",
            "Save your work in case the computer crashes. (preparation)",
            "Here's my number in case you have questions. (might need it)",
        ],
        "common_error": "Confusing 'in case' with 'if' - they're NOT the same!",
    },
}

WISH_CHARACTERISTICS = {
    "wish_past_simple": {
        "use": "Regret about PRESENT (want different present)",
        "structure": "wish + past simple",
        "time": "Present dissatisfaction",
        "examples": [
            "I wish I had more time. (I don't have enough time NOW)",
            "I wish I spoke Spanish. (I don't speak it NOW)",
            "I wish I were taller. (I'm not tall NOW)",
            "She wishes she lived in Paris. (she doesn't live there NOW)",
        ],
        "like_second_conditional": "Uses same structure as second conditional (unreal present)",
    },
    "wish_past_perfect": {
        "use": "Regret about PAST (want different past)",
        "structure": "wish + past perfect",
        "time": "Past dissatisfaction (can't change now)",
        "examples": [
            "I wish I had studied harder. (I didn't study hard - regret)",
            "I wish I had taken that job. (I didn't take it - too late now)",
            "She wishes she had gone to the party. (she didn't go - regrets it)",
            "I wish I hadn't said that. (I said it - regret)",
        ],
        "like_third_conditional": "Uses same structure as third conditional (impossible past)",
    },
    "wish_would": {
        "use": "Annoyance about present behavior / wanting change",
        "structure": "wish + would + base verb",
        "time": "Present/future (wanting change)",
        "examples": [
            "I wish you would stop smoking. (you smoke - I want you to stop)",
            "I wish it would stop raining. (it's raining - want it to stop)",
            "I wish he would listen to me. (he doesn't listen - annoying)",
        ],
        "note": "Cannot use 'I wish I would' - use 'I wish I could' instead",
    },
    "if_only": {
        "meaning": "Emphatic wish (stronger emotion)",
        "structure": "Same as wish but more emphatic",
        "examples": [
            "If only I were taller! (strong wish)",
            "If only I had known! (strong regret about past)",
            "If only you would listen! (strong annoyance)",
        ],
        "note": "Often used as exclamation with !",
    },
    "vs_hope": {
        "wish": {
            "reality": "Unreal/unlikely/impossible",
            "examples": ["I wish I were rich. (I'm not)", "I wish I could fly. (impossible)"],
        },
        "hope": {
            "reality": "Possible/real",
            "examples": [
                "I hope I pass the exam. (might pass)",
                "I hope you come to my party. (you might come)",
            ],
        },
        "rule": "Wish = unreal/unlikely | Hope = possible",
    },
    "common_errors": [
        "❌ I wish I am taller. → ✅ I wish I were taller. (past simple for present)",
        "❌ I wish I have more time. → ✅ I wish I had more time.",
        "❌ I hope I were rich. → ✅ I wish I were rich. (unreal, so 'wish')",
        "❌ I wish I would have studied. → ✅ I wish I had studied. (not 'would have')",
    ],
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_2_MODULES = {
    6: {
        "title": "Second Conditional - Unreal Present and Future",
        "subtitle": "If + Past Simple, Would + Base Verb",
        "grammar_focus": "Hypothetical Present/Future Situations",
        "sections": 16,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 4,
        "characteristics": SECOND_CONDITIONAL_CHARACTERISTICS,
    },
    7: {
        "title": "Third Conditional - Imagining Different Past",
        "subtitle": "If + Past Perfect, Would Have + Past Participle",
        "grammar_focus": "Impossible Past Situations",
        "sections": 16,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 5,
        "characteristics": THIRD_CONDITIONAL_CHARACTERISTICS,
    },
    8: {
        "title": "Mixed Conditionals - Past and Present Combined",
        "subtitle": "Combining Different Time Frames",
        "grammar_focus": "Mixed Conditional Structures",
        "sections": 15,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 5,
        "characteristics": MIXED_CONDITIONALS_CHARACTERISTICS,
    },
    9: {
        "title": "Conditional Alternatives - Unless, Provided That, As Long As",
        "subtitle": "Different Ways to Express Conditions",
        "grammar_focus": "Alternative Conditional Expressions",
        "sections": 14,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": CONDITIONAL_ALTERNATIVES_CHARACTERISTICS,
    },
    10: {
        "title": "Wish and If Only - Expressing Regrets and Desires",
        "subtitle": "I Wish + Past Simple/Past Perfect",
        "grammar_focus": "Wish Structures for Regrets",
        "sections": 15,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 4,
        "characteristics": WISH_CHARACTERISTICS,
    },
}

# ============================================================================
# HELPER FUNCTIONS - Cell Creation
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

    # Module-specific introduction content
    if module_num == 6:
        cells.extend(create_module_6_phase_1(module_data))
    elif module_num == 7:
        cells.extend(create_module_7_phase_1(module_data))
    elif module_num == 8:
        cells.extend(create_module_8_phase_1(module_data))
    elif module_num == 9:
        cells.extend(create_module_9_phase_1(module_data))
    elif module_num == 10:
        cells.extend(create_module_10_phase_1(module_data))

    return cells


def create_module_6_phase_1(module_data):
    """Create Module 6 Phase 1 content - Second Conditional"""
    cells = []

    intro = """## 1. Introduction - Imagining Unreal Situations

Welcome to the **Second Conditional** - your gateway to expressing hypothetical, unreal, and unlikely situations!

**What you'll learn:**
- How to imagine different present realities
- How to talk about unlikely future possibilities
- How to give advice using "If I were you..."
- The important concept of "unreality" in grammar

**Why this matters:**
In A2, you learned the **first conditional** for real possibilities. Now in B1, you'll master the **second conditional** for **unreal** situations. This is essential for:
- Giving advice
- Expressing wishes indirectly
- Discussing hypothetical scenarios
- Softening requests

**This module will take 6-7 hours.** The concept of "unreality" is new and important!
"""
    cells.append(create_markdown_cell(intro))

    formation = """## 2. Formation - If + Past Simple, Would + Base Verb

### Structure

**If-clause:** If + subject + past simple
**Main clause:** subject + would + base verb

**Examples:**
- If I **had** more time, I **would** read more books.
- If she **lived** in London, she **would** visit museums every day.
- If we **won** the lottery, we **would** travel the world.

### Can Reverse the Order

- I **would** read more books if I **had** more time.
- She **would** visit museums every day if she **lived** in London.

**Comma rule:** Use comma when if-clause comes first. No comma when main clause comes first.

### Important Note

The **past simple** in the if-clause does NOT mean past time!
It signals **unreality** - imagining a different present or unlikely future.
"""
    cells.append(create_markdown_cell(formation))

    unreal_concept = """## 3. The "Unreal Past" Concept

### Why Past Tense for Present/Future?

This confuses many learners! Here's why:

**Past tense = Psychological distance from reality**

- Real (first conditional): "If it **rains**, I **will** stay home." (might really happen)
- Unreal (second conditional): "If it **rained** every day, I **would** stay home." (not real - hypothetical)

### The Key Understanding

| Conditional | Reality Level | Example |
|-------------|--------------|---------|
| **First** | Real possibility | If I **have** time, I **will** help. (I might have time) |
| **Second** | Unreal/unlikely | If I **had** time, I **would** help. (I don't have time) |

**The past tense creates distance from reality!**

This pattern exists in many languages - using past tense to signal politeness or unreality:
- "Could you help me?" (more polite than "Can you help me?")
- "I wanted to ask you something" (softer than "I want to ask")
"""
    cells.append(create_markdown_cell(unreal_concept))

    # Add summary
    summary = """## Summary: Second Conditional

### Quick Reference

- **Form:** If + past simple, would + base verb
- **Use:** Unreal present or unlikely future
- **Key:** Past tense = unreality, NOT past time
- **Common:** Giving advice, imagining scenarios

### Examples

✅ **If I were rich, I would travel the world.** (I'm not rich - unreal present)
✅ **If I won the lottery, I would buy a house.** (unlikely future)
✅ **If I were you, I would study harder.** (advice - I'm not you)

**Practice makes perfect!** You'll see 95 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_7_phase_1(module_data):
    """Create Module 7 Phase 1 content - Third Conditional"""
    cells = []

    intro = """## 1. Introduction - Impossible Past

Welcome to the **Third Conditional** - expressing regrets and imagining how the past could have been different!

**What you'll learn:**
- How to express regrets about the past
- How to give (softened) criticism
- How to speculate about past events
- How to express relief about what didn't happen

**Prerequisites:**
You MUST understand **past perfect** from Module 4 (Batch 1). If you're not confident with past perfect, review Module 4 first!

**This module will take 6-7 hours.** This is one of the most complex English structures!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_8_phase_1(module_data):
    """Create Module 8 Phase 1 content - Mixed Conditionals"""
    cells = []

    intro = """## 1. Introduction - When Time Frames Mix

Welcome to **Mixed Conditionals** - combining past and present in one conditional sentence!

**What you'll learn:**
- Past condition → Present result
- Present condition → Past result
- When to use mixed vs standard conditionals
- Complex time relationships

**Prerequisites:**
You MUST understand both:
- Second conditional (Module 6) - unreal present
- Third conditional (Module 7) - impossible past

**This module will take 5-6 hours.** Prepare for complex temporal thinking!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_9_phase_1(module_data):
    """Create Module 9 Phase 1 content - Conditional Alternatives"""
    cells = []

    intro = """## 1. Introduction - Beyond "If"

Welcome to **Conditional Alternatives** - different ways to express conditions!

**What you'll learn:**
- **Unless** = if...not (exception)
- **Provided that / As long as** = if (requirement)
- **Only if** = exclusive condition
- **In case** = precaution (different from "if"!)

**This module will take 5-6 hours.** Expand your conditional vocabulary!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_10_phase_1(module_data):
    """Create Module 10 Phase 1 content - Wish and If Only"""
    cells = []

    intro = """## 1. Introduction - Expressing Wishes and Regrets

Welcome to **Wish and If Only** - expressing desires for different reality!

**What you'll learn:**
- Wish + past simple (present regrets)
- Wish + past perfect (past regrets)
- Wish + would (annoyance/wanting change)
- If only (emphatic wishes)
- Wish vs Hope (important distinction!)

**This module will take 5-6 hours.** Express your wishes in English!
"""
    cells.append(create_markdown_cell(intro))

    return cells


# ============================================================================
# PHASE 2: CONTROLLED PRACTICE
# ============================================================================


def create_phase_2(module_num, module_data):
    """Create Phase 2: Controlled Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 2, "Controlled Practice"))

    intro = f"""## Welcome to Phase 2: Controlled Practice

In this phase, you'll complete **{module_data['exercises']} exercises** to master the grammar.

**How to use these exercises:**
1. Complete each exercise carefully
2. Check your answer immediately
3. If wrong, review the explanation
4. Understand WHY the answer is correct
5. Move forward with confidence!

**Remember:** Conditionals can be tricky. Take your time and understand the logic!

---

Let's begin!
"""
    cells.append(create_markdown_cell(intro))

    exercise_count = module_data["exercises"]
    cells.append(create_markdown_cell(f"## Exercises (Total: {exercise_count})"))
    cells.append(create_exercise_placeholder(module_num, exercise_count))

    return cells


def create_exercise_placeholder(module_num, count):
    """Create exercise placeholder"""
    content = f"""### Exercise Sets

**Total Exercises:** {count}

In the complete implementation, this section contains:
- Formation exercises
- Reality level identification
- Conditional type choice
- Transformation exercises
- Error correction
- Mixed conditional practice

Each exercise includes:
- Clear instructions
- Answer validation
- Explanations
- Common error warnings

**Note:** This is a template version. Full exercises will be generated in production.
"""
    return create_markdown_cell(content)


# ============================================================================
# PHASE 3: MEANINGFUL PRACTICE
# ============================================================================


def create_phase_3(module_num, module_data):
    """Create Phase 3: Meaningful Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 3, "Meaningful Practice"))

    intro = f"""## Welcome to Phase 3: Meaningful Practice

Now you'll use the grammar with **your own** personal content.

**Activities in this phase:** {module_data['activities']}

**Purpose:**
- Make the grammar personally relevant
- Express your own hypothetical situations, regrets, or wishes
- Semi-guided production
- Prepare for free communication

**Instructions:**
- Write about YOUR life, YOUR situations, YOUR wishes
- Use the conditional structures from this module
- Be creative and honest
- There are no "wrong" answers - it's YOUR content!

---
"""
    cells.append(create_markdown_cell(intro))

    for i in range(1, module_data["activities"] + 1):
        activity = create_activity_placeholder(module_num, i)
        cells.append(activity)

    return cells


def create_activity_placeholder(module_num, activity_num):
    """Create activity placeholder"""
    content = f"""### Activity {activity_num}

**Instructions:** [Activity description would go here]

**Your Response:**

[Write your answer here]

---
"""
    return create_markdown_cell(content)


# ============================================================================
# PHASE 4: COMMUNICATIVE PRACTICE
# ============================================================================


def create_phase_4(module_num, module_data):
    """Create Phase 4: Communicative Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 4, "Communicative Practice"))

    intro = f"""## Welcome to Phase 4: Communicative Practice

The final phase focuses on **real communication**!

**Tasks in this phase:** {module_data['tasks']}

**Purpose:**
- Use conditionals in authentic communication
- Develop fluency and confidence
- Integrate with other grammar and vocabulary
- Prepare for real-world English use

**Note:** Many tasks require a partner or group. Use:
- Language exchange platforms (iTalki, Tandem, HelloTalk)
- Study groups
- Online forums
- Self-recording if no partner available

---
"""
    cells.append(create_markdown_cell(intro))

    for i in range(1, module_data["tasks"] + 1):
        task = create_task_placeholder(module_num, i)
        cells.append(task)

    # Add batch completion celebration for Module 10
    if module_num == 10:
        completion = f"""## 🎉 Module {module_num} Complete - B1 Batch 2 FINISHED!

**Congratulations!** You've completed:

✅ Module 6: Second Conditional
✅ Module 7: Third Conditional
✅ Module 8: Mixed Conditionals
✅ Module 9: Conditional Alternatives
✅ Module 10: Wish and If Only

### B1 Batch 2 Achievement

**You can now:**
- Express hypothetical present/future situations
- Express regrets about the past
- Combine different time frames in conditionals
- Use alternative conditional expressions
- Express wishes and desires

**Total in Batch 2:** {module_data['exercises']} exercises + activities + tasks

### Next Steps

1. **Review:** Revisit any difficult modules
2. **Integration Practice:** Mix Batch 1 (Perfect Tenses) + Batch 2 (Conditionals)
3. **Move Forward:** Ready for Batch 3 (Passive Voice and Reporting)!

---

**You're halfway through B1! Excellent progress!**
"""
    else:
        completion = f"""## 🎉 Module {module_num} Complete!

**Congratulations!** You've completed all four phases.

### Next Steps

1. **Review:** Revisit any difficult sections
2. **Practice:** Keep using this grammar daily
3. **Move Forward:** Ready for Module {module_num + 1}!

**Time spent:** Approximately {module_data['estimated_hours']} hours

---
"""

    cells.append(create_markdown_cell(completion))

    return cells


def create_task_placeholder(module_num, task_num):
    """Create task placeholder"""
    content = f"""### Task {task_num}

**Type:** [Task type - interview/presentation/discussion/etc.]

**Instructions:** [Task description would go here]

**Preparation:**
[Preparation steps]

**Reflection:**
[Space for reflection after task]

---
"""
    return create_markdown_cell(content)


# ============================================================================
# NOTEBOOK CREATION
# ============================================================================


def create_module_all_phases(module_num, module_data):
    """Create all 4 phases for a module"""
    base_path = f"notebooks/B1/Module_{module_num:02d}"

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
    """Generate all B1 Batch 2 modules"""
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
    print("B1 LEVEL - BATCH 2: HYPOTHETICAL CONDITIONALS")
    print("Generating Modules 6-10")
    print("SECOND B1 BATCH - Mastering Unreal and Hypothetical Situations")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_2_MODULES.keys()):
        module_data = BATCH_2_MODULES[module_num]
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
    print("BATCH 2 GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nModules Created: 5 (Modules 6-10)")
    print(f"Notebooks Created: 20 (5 modules × 4 phases)")
    print(f"Total Exercises: {total_exercises}")
    print(f"Total Activities: {total_activities}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Total Learning Content: 28-32 hours")
    print("\nB1 Level Batch 2: COMPLETE")
    print("- Second, Third, and Mixed Conditionals mastered")
    print("- Conditional alternatives learned")
    print("- Wish and If Only structures acquired")
    print("- Ready for Batch 3 (Passive Voice and Reporting)")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
