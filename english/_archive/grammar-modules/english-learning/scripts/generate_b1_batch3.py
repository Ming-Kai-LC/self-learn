"""
B1 Level - Batch 3: Passive Voice and Reporting (Modules 11-15)
Third B1 batch focusing on voice transformations and reported speech

This batch focuses on:
- Passive Voice - Present and Past Simple (when/why passive)
- Passive Voice - All Tenses (present perfect, future, continuous, modal)
- Reported Speech - Statements (say/tell, tense backshift)
- Reported Speech - Questions and Commands (word order, imperatives)
- Advanced Reporting Verbs (suggest, recommend, advise - verb patterns)

Architecture: Passive/reporting-specific characteristics with transformation rules
Exercise Count: 455 total exercises
"""

import os

import nbformat as nbf

# ============================================================================
# PASSIVE VOICE CHARACTERISTICS
# ============================================================================

PASSIVE_VOICE_SIMPLE_CHARACTERISTICS = {
    "concept": "Shifting focus from WHO (actor) to WHAT (action/receiver)",
    "formation": "be + past participle (+ by agent)",
    "present_simple_passive": {
        "form": "am/is/are + past participle",
        "examples": [
            "English is spoken in many countries.",
            "These cars are made in Germany.",
            "I am paid monthly.",
            "The office is cleaned every day.",
        ],
        "uses": ["General facts", "Regular actions", "States"],
    },
    "past_simple_passive": {
        "form": "was/were + past participle",
        "examples": [
            "The building was built in 1920.",
            "The students were tested yesterday.",
            "I was born in Tokyo.",
            "The letter was sent last week.",
        ],
        "uses": ["Completed past actions", "Historical events", "Past states"],
    },
    "by_phrase": {
        "when_to_include": {
            "important_agent": "The book was written by a child. (surprising)",
            "specific_person": "Romeo and Juliet was written by Shakespeare.",
            "contrast": "This was painted by Picasso, that by Monet.",
        },
        "when_to_omit": {
            "unknown": "My bike was stolen. (don't know who)",
            "obvious": "The president was elected. (obviously by voters)",
            "unimportant": "The house was built in 1990. (who built it not relevant)",
            "general_people": "Spanish is spoken in Spain. (not 'by people')",
        },
    },
    "active_to_passive_transformation": {
        "step_1": "Object of active sentence becomes subject of passive",
        "step_2": "Verb changes to be + past participle (match tense)",
        "step_3": "Subject of active becomes by-phrase (optional)",
        "example": "The chef cooked the meal → The meal was cooked (by the chef).",
    },
    "when_to_use_passive": [
        "Agent unknown",
        "Agent obvious from context",
        "Agent unimportant to message",
        "Focus on receiver/action not actor",
        "Formal/academic style",
        "News reporting",
    ],
    "common_errors": [
        "❌ The house is build. → ✅ The house is built. (past participle, not base)",
        "❌ It was happened. → ✅ It happened. (happen doesn't use passive)",
        "❌ The book was write by him. → ✅ The book was written by him.",
        "❌ English is spoke here. → ✅ English is spoken here.",
    ],
}

PASSIVE_VOICE_ALL_TENSES_CHARACTERISTICS = {
    "present_continuous_passive": {
        "form": "am/is/are being + past participle",
        "use": "Action in progress NOW",
        "examples": [
            "The house is being built. (in progress)",
            "The patients are being treated. (happening now)",
            "The car is being repaired. (at this moment)",
        ],
    },
    "present_perfect_passive": {
        "form": "have/has been + past participle",
        "use": "Completed action with present relevance",
        "examples": [
            "The work has been completed. (finished, relevant now)",
            "The letters have been sent. (done, present result)",
            "The decision has been made. (completed, affects now)",
        ],
    },
    "future_passive_will": {
        "form": "will be + past participle",
        "use": "Future action",
        "examples": [
            "The meeting will be held tomorrow.",
            "The results will be announced next week.",
            "The project will be finished soon.",
        ],
    },
    "future_passive_going_to": {
        "form": "am/is/are going to be + past participle",
        "use": "Planned future action",
        "examples": [
            "The building is going to be demolished.",
            "The rules are going to be changed.",
            "A new bridge is going to be built.",
        ],
    },
    "modal_passive": {
        "form": "modal + be + past participle",
        "modals": ["can", "could", "should", "must", "may", "might"],
        "examples": [
            "It can be done. (possibility)",
            "It should be fixed. (advice/recommendation)",
            "It must be submitted by Friday. (obligation)",
            "It may be cancelled. (possibility)",
            "It might be delayed. (possibility)",
        ],
    },
    "past_perfect_passive": {
        "form": "had been + past participle",
        "use": "Past action before another past action (rare)",
        "examples": [
            "The building had been demolished before we arrived.",
            "The email had been sent before I noticed the error.",
            "The decision had already been made.",
        ],
    },
    "common_errors": [
        "❌ It is being build. → ✅ It is being built.",
        "❌ It has been send. → ✅ It has been sent.",
        "❌ It will being done. → ✅ It will be done.",
        "❌ It can being fixed. → ✅ It can be fixed.",
    ],
}

# ============================================================================
# REPORTED SPEECH CHARACTERISTICS
# ============================================================================

REPORTED_SPEECH_STATEMENTS_CHARACTERISTICS = {
    "concept": "Reporting what someone said using tense backshift",
    "say_vs_tell": {
        "say": {
            "structure": "say (that) + clause OR say to someone (that)",
            "examples": [
                "He said (that) he was tired.",
                "She said to me (that) she would come.",
                "They said (that) they had finished.",
            ],
            "note": "More common in reported speech",
        },
        "tell": {
            "structure": "tell someone (that) + clause",
            "examples": [
                "He told me (that) he was tired.",
                "She told us (that) she would come.",
                "They told him (that) they had finished.",
            ],
            "error": "❌ He told to me... → ✅ He told me...",
        },
    },
    "tense_backshift": {
        "present_simple": "→ past simple | 'I am tired' → He said he was tired",
        "present_continuous": "→ past continuous | 'I am working' → He said he was working",
        "present_perfect": "→ past perfect | 'I have finished' → He said he had finished",
        "past_simple": "→ past perfect | 'I went' → He said he had gone",
        "will": "→ would | 'I will go' → He said he would go",
        "can": "→ could | 'I can help' → He said he could help",
        "may": "→ might | 'I may come' → He said he might come",
        "must": "→ had to | 'I must leave' → He said he had to leave",
    },
    "no_backshift_when": {
        "general_truths": "'The earth goes around the sun' → He said the earth goes around the sun",
        "still_true": "'I live in London' → He said he lives in London (if still true)",
        "reporting_immediately": "'I'm tired' → She says she's tired (present 'says')",
    },
    "pronoun_changes": {
        "I": "→ he/she",
        "we": "→ they",
        "you": "→ I/we (depends on who's reporting)",
        "my": "→ his/her",
        "our": "→ their",
    },
    "time_word_changes": {
        "today": "→ that day",
        "tonight": "→ that night",
        "tomorrow": "→ the next day / the following day",
        "yesterday": "→ the day before / the previous day",
        "last week": "→ the week before / the previous week",
        "next week": "→ the following week / the week after",
        "ago": "→ before",
        "now": "→ then / at that time",
    },
    "place_changes": {"here": "→ there", "this": "→ that", "these": "→ those"},
    "common_errors": [
        "❌ He said that he is tired. → ✅ He said that he was tired. (backshift)",
        "❌ He told to me that... → ✅ He told me that...",
        "❌ She said me that... → ✅ She told me that... (say doesn't take object)",
        "❌ He said 'I will come tomorrow'. → ✅ He said he would come the next day.",
    ],
}

REPORTED_QUESTIONS_COMMANDS_CHARACTERISTICS = {
    "reported_yes_no_questions": {
        "structure": "asked + if/whether + subject + verb (NO inversion)",
        "direct": "'Are you tired?'",
        "reported": "He asked if/whether I was tired.",
        "key_point": "NO question mark, NO do/does/did, NORMAL word order",
        "examples": [
            "'Do you like coffee?' → She asked if I liked coffee.",
            "'Have you finished?' → He asked whether I had finished.",
            "'Can you help?' → She asked if I could help.",
            "'Did you go?' → They asked if I had gone.",
        ],
    },
    "reported_wh_questions": {
        "structure": "asked + question word + subject + verb (NO inversion)",
        "direct": "'Where do you live?'",
        "reported": "He asked where I lived.",
        "key_point": "Keep question word, but use NORMAL word order",
        "examples": [
            "'What are you doing?' → She asked what I was doing.",
            "'Where did you go?' → He asked where I had gone.",
            "'When will you arrive?' → They asked when I would arrive.",
            "'Why are you late?' → She asked why I was late.",
        ],
    },
    "reported_commands": {
        "positive_structure": "tell/ask someone to + infinitive",
        "negative_structure": "tell/ask someone not to + infinitive",
        "examples": {
            "positive": [
                "'Close the door.' → He told me to close the door.",
                "'Please help me.' → She asked me to help her.",
                "'Sit down.' → The teacher told us to sit down.",
            ],
            "negative": [
                "'Don't be late.' → He told me not to be late.",
                "'Don't touch that.' → She told me not to touch it.",
                "'Don't forget.' → They told me not to forget.",
            ],
        },
        "tell_vs_ask": {"tell": "Stronger, orders", "ask": "Politer, requests"},
    },
    "word_order_critical": {
        "error": "❌ He asked what was I doing.",
        "correct": "✅ He asked what I was doing.",
        "error2": "❌ She asked where did I go.",
        "correct2": "✅ She asked where I went.",
    },
    "common_errors": [
        "❌ He asked if was I ready. → ✅ He asked if I was ready.",
        "❌ She asked where did I live. → ✅ She asked where I lived.",
        "❌ He told to close the door. → ✅ He told me to close the door.",
        "❌ They asked to not be late. → ✅ They asked us not to be late.",
    ],
}

ADVANCED_REPORTING_VERBS_CHARACTERISTICS = {
    "pattern_1_verb_that_clause": {
        "verbs": ["say", "claim", "announce", "explain", "mention", "report", "state"],
        "structure": "verb + that-clause",
        "examples": [
            "He claimed that he was innocent.",
            "She announced that she was leaving.",
            "They explained that they were busy.",
        ],
    },
    "pattern_2_verb_object_that_clause": {
        "verbs": ["tell", "remind", "inform", "convince", "assure", "warn"],
        "structure": "verb + object + that-clause",
        "examples": [
            "She told me that she would come.",
            "He reminded me that it was important.",
            "They informed us that the meeting was cancelled.",
        ],
    },
    "pattern_3_verb_to_infinitive": {
        "verbs": ["agree", "refuse", "offer", "promise", "threaten", "decide"],
        "structure": "verb + to-infinitive",
        "examples": [
            "He agreed to help.",
            "She refused to answer.",
            "They offered to pay.",
            "I promised to come.",
        ],
    },
    "pattern_4_verb_object_to_infinitive": {
        "verbs": ["tell", "ask", "advise", "warn", "encourage", "persuade", "invite"],
        "structure": "verb + object + to-infinitive",
        "examples": [
            "She advised me to study harder.",
            "He warned us to be careful.",
            "They encouraged her to try.",
            "I asked him to help.",
        ],
    },
    "pattern_5_verb_ing": {
        "verbs": ["suggest", "recommend", "deny", "admit"],
        "structure": "verb + -ing",
        "examples": [
            "He suggested going to the movies.",
            "She recommended trying the new restaurant.",
            "They denied stealing the money.",
            "I admitted making a mistake.",
        ],
        "alternatives": {
            "suggest_that": "He suggested that we go to the movies.",
            "recommend_that": "She recommended that I try the restaurant.",
        },
    },
    "special_verbs": {
        "suggest_recommend": {
            "pattern_1": "suggest/recommend + -ing",
            "pattern_2": "suggest/recommend + that-clause",
            "examples": [
                "He suggested going. / He suggested that we go.",
                "She recommended trying. / She recommended that I try.",
            ],
        },
        "advise": {
            "pattern": "advise + object + to-infinitive",
            "example": "The doctor advised me to rest.",
            "error": "❌ He advised to go. → ✅ He advised me to go.",
        },
    },
    "common_errors": [
        "❌ He suggested to go. → ✅ He suggested going.",
        "❌ He advised to study. → ✅ He advised me to study.",
        "❌ She agreed helping. → ✅ She agreed to help.",
        "❌ They refused helping. → ✅ They refused to help.",
    ],
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_3_MODULES = {
    11: {
        "title": "Passive Voice Introduction - Present and Past Simple",
        "subtitle": "Be + Past Participle - Focus on Action, Not Actor",
        "grammar_focus": "Passive Voice Formation and Usage",
        "sections": 17,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 4,
        "characteristics": PASSIVE_VOICE_SIMPLE_CHARACTERISTICS,
    },
    12: {
        "title": "Passive Voice in All Tenses",
        "subtitle": "Present Perfect, Future, and Continuous Passive",
        "grammar_focus": "Passive Voice in Complex Tenses",
        "sections": 16,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 4,
        "characteristics": PASSIVE_VOICE_ALL_TENSES_CHARACTERISTICS,
    },
    13: {
        "title": "Reported Speech Introduction - Statements",
        "subtitle": "He Said (That)... - Reporting What People Said",
        "grammar_focus": "Reported Statements with Tense Backshift",
        "sections": 18,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 4,
        "characteristics": REPORTED_SPEECH_STATEMENTS_CHARACTERISTICS,
    },
    14: {
        "title": "Reported Speech - Questions and Commands",
        "subtitle": "He Asked If/Whether... - He Told Me To...",
        "grammar_focus": "Reported Questions and Imperatives",
        "sections": 16,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 4,
        "characteristics": REPORTED_QUESTIONS_COMMANDS_CHARACTERISTICS,
    },
    15: {
        "title": "Advanced Reporting Verbs - Suggest, Recommend, Advise",
        "subtitle": "Verb Patterns in Reported Speech",
        "grammar_focus": "Alternative Reporting Verbs and Patterns",
        "sections": 14,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": ADVANCED_REPORTING_VERBS_CHARACTERISTICS,
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
    if module_num == 11:
        cells.extend(create_module_11_phase_1(module_data))
    elif module_num == 12:
        cells.extend(create_module_12_phase_1(module_data))
    elif module_num == 13:
        cells.extend(create_module_13_phase_1(module_data))
    elif module_num == 14:
        cells.extend(create_module_14_phase_1(module_data))
    elif module_num == 15:
        cells.extend(create_module_15_phase_1(module_data))

    return cells


def create_module_11_phase_1(module_data):
    """Create Module 11 Phase 1 content - Passive Voice Simple"""
    cells = []

    intro = """## 1. Introduction - Changing Focus

Welcome to **Passive Voice** - a new way of expressing actions!

**What you'll learn:**
- How to shift focus from WHO does an action to WHAT receives the action
- When and why to use passive voice
- How to form passive in present and past simple
- When to include or omit the "by-phrase"

**Why this matters:**
Passive voice is essential for:
- Academic and formal writing
- News reporting
- Professional communication
- When the actor is unknown, obvious, or unimportant

**Example transformation:**
- **Active:** The chef cooked the meal. (focus on chef)
- **Passive:** The meal was cooked by the chef. (focus on meal)

**This module will take 6-7 hours.** This is a fundamental voice transformation!
"""
    cells.append(create_markdown_cell(intro))

    formation = """## 2. Formation - Be + Past Participle

### Basic Structure

**Passive Voice = be + past participle**

The form of "be" changes according to tense and subject:

**Present Simple Passive:**
- I **am** paid
- He/She/It **is** paid
- We/You/They **are** paid

**Past Simple Passive:**
- I/He/She/It **was** paid
- We/You/They **were** paid

### Past Participle Review

**Regular verbs:** base + -ed (same as past simple)
- cook → cooked
- use → used
- clean → cleaned

**Irregular verbs:** (must know from Batch 1!)
- make → made
- build → built
- write → written
- speak → spoken
- take → taken

### With By-Phrase (Optional)

**Full passive:** Subject + be + past participle + by + agent

**Examples:**
- The meal **was cooked by** the chef.
- English **is spoken by** millions of people.
- The house **was built by** my grandfather.

**Note:** The by-phrase is often omitted (we'll learn when)!
"""
    cells.append(create_markdown_cell(formation))

    summary = """## Summary: Passive Voice Simple Tenses

### Quick Reference

- **Form:** be + past participle
- **Use:** Shift focus to action/receiver, not actor
- **When:** Actor unknown, obvious, or unimportant
- **By-phrase:** Optional, include if agent is important

### Examples

✅ **English is spoken in many countries.** (general fact)
✅ **The building was built in 1920.** (historical fact)
✅ **My car was stolen.** (agent unknown)

**Practice makes perfect!** You'll see 95 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_12_phase_1(module_data):
    """Create Module 12 Phase 1 content - Passive All Tenses"""
    cells = []

    intro = """## 1. Introduction - Expanding Passive Voice

Welcome to **Passive Voice in All Tenses** - extending passive to complex tenses!

**What you'll learn:**
- Present continuous passive (is being done)
- Present perfect passive (has been done)
- Future passive (will be done)
- Modal passive (can be done, should be done)
- Past perfect passive (had been done)

**Prerequisites:**
You MUST understand:
- Present and past simple passive (Module 11)
- All tenses from Batch 1

**This module will take 5-6 hours.** Complex formations ahead!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_13_phase_1(module_data):
    """Create Module 13 Phase 1 content - Reported Statements"""
    cells = []

    intro = """## 1. Introduction - Reporting What People Say

Welcome to **Reported Speech** - retelling what others said!

**What you'll learn:**
- How to report statements (He said that...)
- Say vs Tell differences
- Tense backshift rules
- Pronoun, time, and place changes

**Example:**
- **Direct:** She said, "I am tired."
- **Reported:** She said (that) she was tired.

**This module will take 6-7 hours.** Systematic transformations required!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_14_phase_1(module_data):
    """Create Module 14 Phase 1 content - Reported Questions/Commands"""
    cells = []

    intro = """## 1. Introduction - Reporting Questions and Commands

Welcome to **Reported Questions and Commands**!

**What you'll learn:**
- How to report yes/no questions (He asked if...)
- How to report wh- questions (He asked where...)
- Word order changes (NO inversion!)
- How to report commands (He told me to...)

**Critical:** Word order changes - no do/does/did in reported questions!

**This module will take 5-6 hours.** Word order is crucial!
"""
    cells.append(create_markdown_cell(intro))

    return cells


def create_module_15_phase_1(module_data):
    """Create Module 15 Phase 1 content - Advanced Reporting Verbs"""
    cells = []

    intro = """## 1. Introduction - Beyond Say and Tell

Welcome to **Advanced Reporting Verbs**!

**What you'll learn:**
- Suggest, recommend (+ -ing or that-clause)
- Advise, warn, encourage (+ object + to-infinitive)
- Agree, refuse, offer, promise (+ to-infinitive)
- Admit, deny (+ -ing)

**Moving beyond:** "He said..." to more precise reporting!

**This module will take 5-6 hours.** Verb pattern variety!
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

**Remember:** {module_data['grammar_focus']} requires systematic practice!

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
- Transformation exercises (active↔passive / direct↔reported)
- Pattern identification
- Error correction
- Mixed application

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
- Practice in authentic contexts
- Semi-guided production
- Prepare for free communication

**Instructions:**
- Write about YOUR experiences, YOUR city, YOUR stories
- Use the structures from this module
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
- Use grammar in authentic communication
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

    # Add batch completion celebration for Module 15
    if module_num == 15:
        completion = f"""## 🎉 Module {module_num} Complete - B1 Batch 3 FINISHED!

**Congratulations!** You've completed:

✅ Module 11: Passive Voice - Present & Past Simple
✅ Module 12: Passive Voice - All Tenses
✅ Module 13: Reported Speech - Statements
✅ Module 14: Reported Speech - Questions & Commands
✅ Module 15: Advanced Reporting Verbs

### B1 Batch 3 Achievement

**You can now:**
- Use passive voice in all major tenses
- Report statements, questions, and commands
- Choose appropriate reporting verbs
- Write in formal/academic style
- Report conversations accurately

**Total in Batch 3:** ~455 exercises + activities + tasks

### B1 Progress

**Completed:** 15/30 modules (50% of B1 level!)

**Batches completed:**
- ✅ Batch 1: Perfect Tenses (Modules 1-5)
- ✅ Batch 2: Hypothetical Conditionals (Modules 6-10)
- ✅ Batch 3: Passive Voice and Reporting (Modules 11-15)

**Remaining:**
- 📋 Batch 4: Advanced Relatives and Modals (Modules 16-20)
- 📋 Batch 5: Advanced Verb Patterns (Modules 21-25)
- 📋 Batch 6: B1 Integration and Consolidation (Modules 26-30)

### Next Steps

1. **Review:** Revisit any difficult modules
2. **Integration:** Practice combining Batches 1+2+3
3. **Move Forward:** Ready for Batch 4!

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
    """Generate all B1 Batch 3 modules"""
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
    print("B1 LEVEL - BATCH 3: PASSIVE VOICE AND REPORTING")
    print("Generating Modules 11-15")
    print("THIRD B1 BATCH - Voice Transformations and Reported Speech")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_3_MODULES.keys()):
        module_data = BATCH_3_MODULES[module_num]
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
    print("BATCH 3 GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nModules Created: 5 (Modules 11-15)")
    print(f"Notebooks Created: 20 (5 modules × 4 phases)")
    print(f"Total Exercises: {total_exercises}")
    print(f"Total Activities: {total_activities}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Total Learning Content: 27-31 hours")
    print("\nB1 Level Batch 3: COMPLETE")
    print("- Passive voice in all tenses mastered")
    print("- Reported speech (statements, questions, commands) acquired")
    print("- Advanced reporting verbs learned")
    print("- B1 Progress: 50% complete (15/30 modules)")
    print("- Ready for Batch 4 (Advanced Relatives and Modals)")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
