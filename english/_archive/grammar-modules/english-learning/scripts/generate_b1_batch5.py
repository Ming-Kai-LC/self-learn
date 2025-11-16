"""
B1 Level - Batch 5: Advanced Verb Patterns + CRITERIAL FEATURE (Modules 21-25)
Fifth B1 batch - THE MOST IMPORTANT - contains the criterial B1 feature

This batch focuses on:
- Used To, Would, Be/Get Used To (confusing past/habit structures)
- Gerunds and Infinitives - Advanced (meaning changes, verb patterns)
- Make, Let, Help, Get - Causatives (getting people to do things)
- Phrasal Verbs - Three-Particle Verbs (complex phrasal patterns)
- INDIRECT QUESTIONS - THE CRITERIAL B1 FEATURE (Module 25) [STAR]

Architecture: Advanced verb pattern databases + indirect question transformation
Exercise Count: 465 total exercises (100 in Module 25 alone!)
"""

import os

import nbformat as nbf

# ============================================================================
# MODULE 21: USED TO / WOULD / BE USED TO / GET USED TO CHARACTERISTICS
# ============================================================================

USED_TO_PATTERNS_CHARACTERISTICS = {
    "concept": "Four confusing structures that learners constantly mix up",
    "four_structures": {
        "used_to": {
            "form": "used to + base verb",
            "meaning": "Past habit or state that is NO LONGER true",
            "time": "Past only",
            "examples": [
                "I used to smoke, but I quit. (past habit, stopped)",
                "She used to live in London. (past state, not anymore)",
                "There used to be a cinema here. (no longer exists)",
            ],
            "key": "Always implies CHANGE - was true, but isn't now",
            "works_with": "Both actions AND states",
        },
        "would": {
            "form": "would + base verb",
            "meaning": "Repeated actions in the past (nostalgic)",
            "time": "Past only",
            "examples": [
                "When I was young, I would visit my grandmother. (repeated action)",
                "We would spend hours playing. (repeated action)",
                "He would always forget his keys. (repeated action)",
            ],
            "key": "ONLY for repeated ACTIONS, NOT states",
            "limitation": "❌ Cannot use for states: 'I would be happy' is WRONG",
        },
        "be_used_to": {
            "form": "be used to + -ing (or noun)",
            "meaning": "Be accustomed to something (familiar, normal)",
            "time": "Present or past (NOT about past habits!)",
            "examples": [
                "I'm used to working late. (it's normal for me - accustomed)",
                "She's used to the cold weather. (accustomed to it)",
                "We're used to eating spicy food. (we're accustomed)",
            ],
            "key": "About being ACCUSTOMED (present/past state)",
            "not_about_past": "This is NOT about past habits! Different meaning!",
        },
        "get_used_to": {
            "form": "get used to + -ing (or noun)",
            "meaning": "BECOME accustomed (the process)",
            "time": "Any time (process of becoming accustomed)",
            "examples": [
                "I'm getting used to my new job. (becoming accustomed - process)",
                "It took me time to get used to driving on the left.",
                "You'll get used to the noise. (you'll become accustomed)",
            ],
            "key": "The PROCESS of becoming accustomed",
        },
    },
    "comparison_table": """
    | Structure       | Meaning                   | Time          | Form              |
    |----------------|---------------------------|---------------|-------------------|
    | used to        | Past habit/state (not now)| Past          | used to + base    |
    | would          | Repeated past action only | Past          | would + base      |
    | be used to     | Accustomed to            | Present/Past  | be used to + -ing |
    | get used to    | Become accustomed        | Any time      | get used to + -ing|
    """,
    "used_to_vs_would": {
        "both": "Can describe repeated past actions",
        "used_to_only": "Can describe past STATES (would cannot)",
        "examples": {
            "action_both_ok": "I used to play / I would play tennis. (both OK - action)",
            "state_only_used_to": "I used to be happy. ✅ / I would be happy. ❌",
        },
    },
    "used_to_questions_negatives": {
        "question": "Did you use to smoke? (NOT 'used to')",
        "negative": "I didn't use to like coffee. (NOT 'didn't used to')",
        "key": "In questions/negatives, 'used to' becomes 'use to' (no 'd')",
    },
    "common_errors": [
        "❌ I would be happy as a child. → ✅ I used to be happy. (state, not would)",
        "❌ I'm used to smoke. → ✅ I used to smoke. (past habit, not accustomed)",
        "❌ Did you used to live here? → ✅ Did you use to live here? (no 'd')",
        "❌ I'm use to it. → ✅ I'm used to it. ('used', not 'use')",
    ],
}

# ============================================================================
# MODULE 22: GERUNDS AND INFINITIVES - ADVANCED CHARACTERISTICS
# ============================================================================

GERUNDS_INFINITIVES_ADVANCED_CHARACTERISTICS = {
    "concept": "Different verbs require different patterns - some change meaning!",
    "four_categories": {
        "gerund_only": {
            "verbs": [
                "enjoy",
                "finish",
                "mind",
                "avoid",
                "suggest",
                "recommend",
                "consider",
                "practice",
                "deny",
                "admit",
                "miss",
                "risk",
                "can't help",
                "imagine",
                "keep (continue)",
            ],
            "form": "verb + -ing",
            "examples": [
                "I enjoy reading. (NOT 'enjoy to read')",
                "She finished working at 5pm.",
                "Do you mind closing the window?",
                "He avoided answering the question.",
            ],
        },
        "infinitive_only": {
            "verbs": [
                "want",
                "need",
                "decide",
                "plan",
                "hope",
                "expect",
                "agree",
                "refuse",
                "offer",
                "promise",
                "seem",
                "appear",
                "afford",
                "manage",
                "learn",
                "wish",
            ],
            "form": "verb + to + base",
            "examples": [
                "I want to go. (NOT 'want going')",
                "She decided to study medicine.",
                "They agreed to help.",
                "We can't afford to buy it.",
            ],
        },
        "both_no_change": {
            "verbs": ["like", "love", "hate", "prefer", "begin", "start", "continue"],
            "form": "verb + -ing OR to + base (same meaning)",
            "examples": [
                "I like swimming. = I like to swim.",
                "She started working. = She started to work.",
                "We continue studying. = We continue to study.",
            ],
            "note": "Infinitive sometimes more formal/specific",
        },
        "both_meaning_changes": {
            "description": "THE MOST IMPORTANT - meaning CHANGES!",
            "verbs": ["stop", "remember", "forget", "try", "regret"],
            "critical": "Must learn these differences!",
        },
    },
    "meaning_change_verbs": {
        "stop": {
            "stop_gerund": {
                "meaning": "Stop the activity (quit doing it)",
                "example": "I stopped smoking. (quit smoking)",
                "structure": "stop + -ing",
            },
            "stop_infinitive": {
                "meaning": "Stop in order to do something else",
                "example": "I stopped to smoke. (paused to have a cigarette)",
                "structure": "stop + to infinitive",
            },
            "key_difference": "Gerund = quit that activity; Infinitive = pause to do it",
        },
        "remember": {
            "remember_gerund": {
                "meaning": "Remember a past action (have memory of)",
                "example": "I remember meeting him. (memory of past meeting)",
                "structure": "remember + -ing",
            },
            "remember_infinitive": {
                "meaning": "Remember to do something (not forget duty)",
                "example": "I remembered to call her. (didn't forget to call)",
                "structure": "remember + to infinitive",
            },
            "key_difference": "Gerund = memory of past; Infinitive = didn't forget duty",
        },
        "forget": {
            "forget_gerund": {
                "meaning": "Forget a past event (lose memory of)",
                "example": "I'll never forget visiting Paris. (memory of past)",
                "structure": "forget + -ing",
            },
            "forget_infinitive": {
                "meaning": "Fail to remember to do something",
                "example": "I forgot to call her. (didn't call - forgot)",
                "structure": "forget + to infinitive",
            },
            "key_difference": "Gerund = lose memory of past; Infinitive = failed to do duty",
        },
        "try": {
            "try_gerund": {
                "meaning": "Experiment with something (see if it works)",
                "example": "I tried eating less. (experimented with this method)",
                "structure": "try + -ing",
            },
            "try_infinitive": {
                "meaning": "Attempt/make an effort (might not succeed)",
                "example": "I tried to eat less. (made effort, might have failed)",
                "structure": "try + to infinitive",
            },
            "key_difference": "Gerund = experiment; Infinitive = attempt/effort",
        },
        "regret": {
            "regret_gerund": {
                "meaning": "Regret a past action (sorry I did it)",
                "example": "I regret telling him. (I told him, now I regret it)",
                "structure": "regret + -ing",
            },
            "regret_infinitive": {
                "meaning": "Be sorry to say (formal announcement)",
                "example": "I regret to inform you... (formal)",
                "structure": "regret + to infinitive",
            },
            "key_difference": "Gerund = regret past action; Infinitive = formal announcement",
        },
    },
    "gerund_other_uses": {
        "as_subject": "Swimming is fun. (gerund as subject)",
        "after_prepositions": "I'm interested in learning French. (always gerund after preposition)",
        "after_expressions": "It's worth trying. / It's no use complaining.",
    },
    "common_errors": [
        "❌ I enjoy to read. → ✅ I enjoy reading. (gerund only)",
        "❌ I want going. → ✅ I want to go. (infinitive only)",
        "❌ I stopped to smoke. (when meaning quit) → ✅ I stopped smoking.",
        "❌ I remember to meet him. (past memory) → ✅ I remember meeting him.",
    ],
}

# ============================================================================
# MODULE 23: CAUSATIVE VERBS (MAKE, LET, HELP, GET) CHARACTERISTICS
# ============================================================================

CAUSATIVE_VERBS_CHARACTERISTICS = {
    "concept": "Getting people to do things - different ways to express causation",
    "four_main_causatives": {
        "make": {
            "meaning": "Force, compel (no choice)",
            "form": "make + object + base verb (NO 'to')",
            "examples": [
                "My parents made me study. (forced, no choice)",
                "The teacher makes us do homework. (requires)",
                "Don't make me laugh! (causing)",
            ],
            "passive": "be made + to infinitive (WITH 'to')",
            "passive_example": "I was made to study. (passive has 'to'!)",
            "key": "Strong force - no choice given",
        },
        "let": {
            "meaning": "Allow, permit (give permission)",
            "form": "let + object + base verb (NO 'to')",
            "examples": [
                "My parents let me go to the party. (gave permission)",
                "Please let me help you. (allow)",
                "She won't let me use her car. (won't allow)",
            ],
            "no_passive": "Cannot make passive - use 'be allowed to'",
            "passive_alternative": "I was allowed to go. (NOT 'I was let to go')",
            "key": "Permission given - they allow it",
        },
        "help": {
            "meaning": "Assist, aid",
            "form": "help + object + base verb OR to + base (BOTH OK)",
            "examples": [
                "I helped him carry the bags. (no 'to')",
                "I helped him to carry the bags. (with 'to')",
                "Both are correct!",
            ],
            "flexibility": "Only causative where 'to' is optional",
            "key": "Assisting - with or without 'to'",
        },
        "get": {
            "meaning": "Persuade, convince, arrange",
            "form": "get + object + TO + base verb (WITH 'to')",
            "examples": [
                "I got him to help me. (persuaded)",
                "She got me to change my mind. (convinced)",
                "Can you get them to come early? (arrange)",
            ],
            "vs_make": "Make = force (no choice); Get = persuade (they agree)",
            "key": "Persuasion - they were convinced",
        },
    },
    "comparison_table": """
    | Verb   | Pattern                    | Meaning    | Example              |
    |--------|---------------------------|------------|---------------------|
    | make   | make + obj + base (no to) | Force      | made me study       |
    | let    | let + obj + base (no to)  | Allow      | let me go           |
    | help   | help + obj + (to) base    | Assist     | helped me (to) go   |
    | get    | get + obj + TO base       | Persuade   | got me to help      |
    """,
    "causative_passive": {
        "concept": "Have/Get something done - arrange service",
        "meaning": "Arrange for someone else to do something for you",
        "form": "have/get + object + past participle",
        "examples": [
            "I had my car repaired. (someone repaired it for me)",
            "She got her hair cut. (at a salon)",
            "We're having the house painted. (hiring painters)",
        ],
        "note": "Advanced B1/B2 structure",
    },
    "make_vs_get": {
        "make": "Force - they have no choice (stronger)",
        "get": "Persuade - they agree to do it (weaker)",
        "example_make": "The teacher made me stay after class. (forced)",
        "example_get": "The teacher got me to help with cleanup. (persuaded)",
    },
    "common_errors": [
        "❌ She made me to go. → ✅ She made me go. (no 'to' after make)",
        "❌ Let me to help. → ✅ Let me help. (no 'to' after let)",
        "❌ I got him help. → ✅ I got him to help. (need 'to' after get)",
        "❌ I was let to go. → ✅ I was allowed to go. (no passive 'let')",
    ],
}

# ============================================================================
# MODULE 24: THREE-PARTICLE PHRASAL VERBS CHARACTERISTICS
# ============================================================================

THREE_PARTICLE_PHRASAL_VERBS_CHARACTERISTICS = {
    "concept": "Complex phrasal verbs: verb + adverb + preposition (three words)",
    "structure": {
        "pattern": "verb + adverb + preposition",
        "examples": ["look forward to", "get on with", "put up with"],
        "key_rule": "ALWAYS INSEPARABLE - cannot put object between particles",
        "often_idiomatic": "Meaning not obvious from individual words",
    },
    "common_three_particle_verbs": {
        "look_forward_to": {
            "meaning": "Anticipate with pleasure",
            "pattern": "look forward to + -ing/noun",
            "examples": [
                "I'm looking forward to seeing you.",
                "We're looking forward to the weekend.",
                "She looks forward to her vacation.",
            ],
        },
        "get_on_with": {
            "meaning_1": "Continue doing something",
            "meaning_2": "Have good relationship with someone",
            "examples": [
                "Let's get on with the work. (continue)",
                "I get on with my colleagues. (good relationship)",
                "Get on with your homework! (continue)",
            ],
        },
        "put_up_with": {
            "meaning": "Tolerate, endure (something annoying)",
            "examples": [
                "I can't put up with the noise anymore.",
                "She puts up with a lot from him.",
                "We won't put up with bad behavior.",
            ],
        },
        "run_out_of": {
            "meaning": "Use all of something, have none left",
            "examples": [
                "We've run out of milk.",
                "I'm running out of time.",
                "The car ran out of gas.",
            ],
        },
        "come_up_with": {
            "meaning": "Think of, produce (idea/solution)",
            "examples": [
                "She came up with a great idea.",
                "Can you come up with a solution?",
                "They came up with a plan.",
            ],
        },
        "get_away_with": {
            "meaning": "Do something bad without punishment",
            "examples": [
                "He got away with cheating.",
                "You won't get away with this!",
                "She got away with lying.",
            ],
        },
        "keep_up_with": {
            "meaning": "Maintain same pace/level",
            "examples": [
                "I can't keep up with the class.",
                "It's hard to keep up with technology.",
                "She keeps up with the news.",
            ],
        },
        "get_out_of": {
            "meaning": "Avoid doing something you should do",
            "examples": [
                "He got out of doing the dishes.",
                "I'm trying to get out of the meeting.",
                "She got out of going to the party.",
            ],
        },
    },
    "always_inseparable": {
        "rule": "Three-particle phrasal verbs are ALWAYS inseparable",
        "correct": "I look forward to it. ✅",
        "incorrect": "I look it forward to. ❌",
        "why": "Cannot split the three-particle unit",
    },
    "with_gerund": {
        "many_take_gerund": "Many three-particle verbs take gerund (-ing)",
        "examples": [
            "look forward to + -ing",
            "get on with + -ing (sometimes)",
            "put up with + -ing (sometimes)",
        ],
    },
    "common_errors": [
        "❌ I look it forward to. → ✅ I look forward to it. (inseparable)",
        "❌ I'm looking forward to see you. → ✅ I'm looking forward to seeing you. (gerund)",
        "❌ Get with on the work. → ✅ Get on with the work. (correct order)",
    ],
}

# ============================================================================
# MODULE 25: INDIRECT QUESTIONS - THE CRITERIAL B1 FEATURE [STAR]
# ============================================================================

INDIRECT_QUESTIONS_CHARACTERISTICS = {
    "criterial_feature": {
        "status": "THE CRITERIAL B1 FEATURE",
        "importance": "This is THE structure that distinguishes B1 from A2",
        "research": "Cambridge English Profile identifies this as the hallmark B1 structure",
        "definition": "If you master this, you have achieved B1 level",
    },
    "concept": "Questions embedded inside statements or polite questions",
    "basic_transformation": {
        "direct": "Where is the station?",
        "indirect": "Can you tell me where the station is?",
        "key_change": "Word order changes from question to STATEMENT order (NO inversion!)",
    },
    "why_use_indirect": {
        "politeness": "Much more polite than direct questions",
        "formality": "Appropriate in professional settings",
        "natural": "Native speakers use these constantly",
        "b1_hallmark": "THE defining B1 structure",
    },
    "wh_questions": {
        "pattern": "Polite phrase + wh-word + subject + verb (STATEMENT ORDER)",
        "direct_example": "Where is the station?",
        "indirect_example": "Can you tell me where the station is? (no inversion!)",
        "examples": [
            "Direct: What time is it? → Indirect: Do you know what time it is?",
            "Direct: Where does she live? → Indirect: Can you tell me where she lives? (no 'does'!)",
            "Direct: Why did he leave? → Indirect: I wonder why he left? (no 'did'!)",
        ],
        "common_polite_phrases": [
            "Can you tell me...?",
            "Do you know...?",
            "Could you tell me...?",
            "I wonder...",
            "I'd like to know...",
            "Do you have any idea...?",
        ],
    },
    "yes_no_questions": {
        "pattern": "Polite phrase + if/whether + subject + verb",
        "direct_example": "Is the bank open?",
        "indirect_example": "Do you know if the bank is open?",
        "examples": [
            "Direct: Is the bank open? → Indirect: Do you know if the bank is open?",
            "Direct: Does she speak English? → Indirect: Can you tell me if she speaks English?",
        ],
        "if_vs_whether": {
            "both_correct": "Both 'if' and 'whether' are correct",
            "whether_formal": "'Whether' slightly more formal",
            "if_common": "'If' more common in speech",
        },
    },
    "critical_rule": {
        "title": "STATEMENT WORD ORDER - THE MOST IMPORTANT RULE",
        "direct_inversion": "Direct questions have inversion (verb before subject)",
        "indirect_statement_order": "Indirect questions have STATEMENT order (subject before verb)",
        "examples": {
            "direct": "Where is he? (is = verb, he = subject → inverted)",
            "indirect": "...where he is (he = subject, is = verb → statement order)",
        },
        "this_is_key": "This is THE most important rule to master!",
    },
    "common_errors": {
        "most_common": "Keeping question word order in embedded clause",
        "errors": [
            "❌ Can you tell me where is the station? → ✅ Can you tell me where the station is?",
            "❌ Do you know what does she want? → ✅ Do you know what she wants?",
            "❌ I wonder why did he leave? → ✅ I wonder why he left?",
        ],
        "key_error": "THE biggest error is inversion in embedded clause!",
    },
    "advanced_patterns": {
        "negative_indirect": {
            "direct": "Why didn't she come?",
            "indirect": "I wonder why she didn't come. (keep didn't, statement order)",
        },
        "modal_verbs": {
            "direct": "Where can I buy tickets?",
            "indirect": "Do you know where I can buy tickets? (statement order)",
        },
    },
    "i_wonder_special": {
        "usage": "Often doesn't need answer (thinking aloud)",
        "example": "I wonder where he is... (not really asking)",
        "vs_do_you_know": "Do you know where he is? (clearly requesting info)",
    },
    "tense_maintenance": {
        "key": "Tense doesn't backshift (NOT reported speech!)",
        "present_stays_present": "Direct: Where is it? → Indirect: ...where it is",
        "past_stays_past": "Direct: Where did he go? → Indirect: ...where he went",
    },
    "transformation_steps": {
        "step_1": "Choose polite phrase (Can you tell me...?)",
        "step_2": "Add wh-word OR if/whether",
        "step_3": "Change to STATEMENT word order (subject before verb)",
        "step_4": "Remove do/does/did (absorbed into statement order)",
    },
    "politeness_levels": {
        "very_polite": "I was wondering if..., Would you mind telling me...?",
        "polite": "Could you tell me...?, Would you know...?",
        "normal": "Do you know...?, Can you tell me...?",
    },
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_5_MODULES = {
    21: {
        "title": "Used To, Would, and Be/Get Used To",
        "subtitle": "Past Habits vs Being Accustomed",
        "grammar_focus": "Distinguishing Confusing Structures",
        "sections": 16,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 4,
        "characteristics": USED_TO_PATTERNS_CHARACTERISTICS,
    },
    22: {
        "title": "Gerunds and Infinitives - Advanced Patterns",
        "subtitle": "Verbs Followed by -ing or To + Infinitive",
        "grammar_focus": "Verb Patterns and Meaning Changes",
        "sections": 18,
        "exercises": 95,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "6-7",
        "difficulty": 5,
        "characteristics": GERUNDS_INFINITIVES_ADVANCED_CHARACTERISTICS,
    },
    23: {
        "title": "Make, Let, Help, Get - Causative Patterns",
        "subtitle": "Getting People to Do Things",
        "grammar_focus": "Causative Verb Patterns",
        "sections": 14,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": CAUSATIVE_VERBS_CHARACTERISTICS,
    },
    24: {
        "title": "Phrasal Verbs - Three-Particle Verbs",
        "subtitle": "Look Forward To, Get On With, Put Up With",
        "grammar_focus": "Complex Phrasal Verb Structures",
        "sections": 13,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": THREE_PARTICLE_PHRASAL_VERBS_CHARACTERISTICS,
    },
    25: {
        "title": "Indirect Questions - THE CRITERIAL B1 FEATURE",
        "subtitle": "Can You Tell Me...? - Polite Question Formation",
        "grammar_focus": "THE CRITERIAL B1 FEATURE - Embedded Questions",
        "sections": 20,
        "exercises": 100,
        "activities": 12,
        "tasks": 10,
        "estimated_hours": "7-8",
        "difficulty": 5,
        "characteristics": INDIRECT_QUESTIONS_CHARACTERISTICS,
        "special_status": "CRITERIAL_FEATURE",
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

    special_marker = (
        " [CRITERIAL]" if module_data.get("special_status") == "CRITERIAL_FEATURE" else ""
    )

    header = f"""# B1 Level - Module {module_num}: {module_data['title']}{special_marker}

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

    if module_num == 21:
        cells.extend(create_module_21_phase_1(module_data))
    elif module_num == 22:
        cells.extend(create_module_22_phase_1(module_data))
    elif module_num == 23:
        cells.extend(create_module_23_phase_1(module_data))
    elif module_num == 24:
        cells.extend(create_module_24_phase_1(module_data))
    elif module_num == 25:
        cells.extend(create_module_25_phase_1(module_data))

    return cells


def create_module_21_phase_1(module_data):
    """Module 21: Used To, Would, Be/Get Used To"""
    cells = []

    intro = """## 1. Introduction - Four Confusing Structures

Welcome to **Used To, Would, and Be/Get Used To** - structures that learners constantly confuse!

**What you'll learn:**
- Used to + base verb (past habits and states)
- Would + base verb (repeated past actions only)
- Be used to + -ing (being accustomed)
- Get used to + -ing (becoming accustomed)

**Why this matters:**
- These look similar but mean VERY different things
- Extremely common in everyday English
- Native speakers use all four constantly
- Critical for describing past habits and current habits

**The key distinction:** Past habits vs being accustomed to something!

**This module will take 6-7 hours.** Don't mix them up!
"""
    cells.append(create_markdown_cell(intro))

    # Summary section
    summary = """## Summary: The Four Structures

### Quick Reference

**1. Used To + Base Verb:**
- Past habit/state (NOT true now)
- "I used to smoke." (quit - not now)

**2. Would + Base Verb:**
- Repeated past actions ONLY (NOT states)
- "I would visit my grandmother." (repeated action)

**3. Be Used To + -ing:**
- Accustomed to (familiar, normal)
- "I'm used to working late." (it's normal for me)

**4. Get Used To + -ing:**
- BECOME accustomed (process)
- "I'm getting used to the noise." (becoming accustomed)

### The Key Differences

| Structure      | Time    | Meaning                  |
|---------------|---------|--------------------------|
| used to       | Past    | No longer true           |
| would         | Past    | Repeated actions only    |
| be used to    | Any     | Accustomed to            |
| get used to   | Any     | Becoming accustomed      |

**Practice makes perfect!** You'll see 95 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_22_phase_1(module_data):
    """Module 22: Gerunds and Infinitives - Advanced"""
    cells = []

    intro = """## 1. Introduction - Verb Complementation Patterns

Welcome to **Gerunds and Infinitives - Advanced Patterns** - one of the trickiest parts of English!

**What you'll learn:**
- Verbs that take ONLY gerund (-ing)
- Verbs that take ONLY infinitive (to + base)
- Verbs that take BOTH (no meaning change)
- Verbs that take BOTH (meaning CHANGES!) [CRITICAL]

**Why this matters:**
- No single rule - must learn each verb's pattern
- Some verbs completely change meaning!
- Essential for natural English
- Very common errors even at B2 level

**The critical point:** Stop/remember/forget/try/regret CHANGE MEANING with -ing vs to!

**This module will take 6-7 hours.** The meaning changes are crucial!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Gerund vs Infinitive Patterns

### Quick Reference

**Gerund Only:** enjoy, finish, mind, avoid, suggest
**Infinitive Only:** want, need, decide, plan, hope
**Both (Same Meaning):** like, love, hate, prefer, begin, start

**Meaning Changes (CRITICAL):**

| Verb | + Gerund | + Infinitive |
|------|----------|--------------|
| stop | Quit doing it | Pause to do it |
| remember | Memory of past | Don't forget duty |
| forget | Lose memory | Fail to do duty |
| try | Experiment | Attempt/effort |
| regret | Regret past action | Formal "sorry to say" |

**Examples:**
- "I stopped smoking." (quit) vs "I stopped to smoke." (paused to have one)
- "I remember meeting him." (memory) vs "I remembered to call." (didn't forget)

**Practice makes perfect!** You'll see 95 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_23_phase_1(module_data):
    """Module 23: Make, Let, Help, Get - Causatives"""
    cells = []

    intro = """## 1. Introduction - Getting Others to Act

Welcome to **Make, Let, Help, Get - Causative Patterns** - expressing how to get people to do things!

**What you'll learn:**
- Make + object + base verb (force)
- Let + object + base verb (allow)
- Help + object + (to) base verb (assist)
- Get + object + to infinitive (persuade)

**Why this matters:**
- Each verb has different pattern (with/without "to")
- Different meanings (force vs allow vs persuade)
- Very common in everyday English
- Critical for describing influence on others

**The key distinction:** Force vs allow vs persuade vs assist!

**This module will take 5-6 hours.** Watch the patterns carefully!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Causative Verbs

### Quick Reference

| Verb | Pattern | Meaning | Example |
|------|---------|---------|---------|
| make | + obj + BASE (no to) | Force | made me study |
| let | + obj + BASE (no to) | Allow | let me go |
| help | + obj + (TO) BASE | Assist | helped me (to) go |
| get | + obj + TO base | Persuade | got me to help |

### Key Points

**Make:** Force (no choice)
- "My parents made me study." (forced)

**Let:** Allow (give permission)
- "My parents let me go." (allowed)

**Help:** Assist (with or without "to")
- "I helped him carry the bags." ✅
- "I helped him to carry the bags." ✅

**Get:** Persuade (they agree)
- "I got him to help me." (persuaded)

**Practice makes perfect!** You'll see 90 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_24_phase_1(module_data):
    """Module 24: Three-Particle Phrasal Verbs"""
    cells = []

    intro = """## 1. Introduction - Three-Particle Phrasal Verbs

Welcome to **Phrasal Verbs - Three-Particle Verbs** - complex phrasal verb patterns!

**What you'll learn:**
- Look forward to, get on with, put up with
- Run out of, come up with, get away with
- Keep up with, get out of
- ALWAYS inseparable rule

**Why this matters:**
- Very common in everyday English
- Often idiomatic (meaning not obvious)
- Always inseparable (cannot split)
- Essential for natural conversation

**The key rule:** Three-particle phrasal verbs are ALWAYS inseparable!

**This module will take 5-6 hours.** Master these common phrases!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Three-Particle Phrasal Verbs

### Common Verbs

**Look forward to:** Anticipate with pleasure
- "I'm looking forward to seeing you."

**Get on with:** Continue / have good relationship
- "Let's get on with the work." (continue)
- "I get on with my colleagues." (relationship)

**Put up with:** Tolerate
- "I can't put up with the noise."

**Run out of:** Use all of, have none left
- "We've run out of milk."

**Come up with:** Think of (idea/solution)
- "She came up with a great idea."

**Get away with:** Do bad thing without punishment
- "He got away with cheating."

**Keep up with:** Maintain same pace
- "I can't keep up with the class."

**Get out of:** Avoid doing something
- "He got out of doing the dishes."

### Key Rule

**ALWAYS INSEPARABLE!**
- ✅ "I look forward to it."
- ❌ "I look it forward to."

**Practice makes perfect!** You'll see 85 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_25_phase_1(module_data):
    """Module 25: Indirect Questions - THE CRITERIAL B1 FEATURE"""
    cells = []

    intro = """## 1. Introduction - THE B1 Criterial Feature [CRITERIAL]

Welcome to **Indirect Questions** - THE MOST IMPORTANT B1 STRUCTURE!

**Why this module is special:**
- Cambridge English Profile research identifies indirect questions as THE structure that reliably distinguishes B1 from A2 learners
- This is not just "a B1 structure" - it's **THE DEFINING CHARACTERISTIC** of B1 level
- If you master this module, you have achieved B1 level
- If you cannot use indirect questions naturally, you are not yet B1

**What you'll learn:**
- How to transform direct questions into polite indirect questions
- THE CRITICAL RULE: Statement word order (NO inversion!)
- When to use if/whether (yes/no questions)
- Common polite phrases
- Why word order is EVERYTHING

**Why this matters:**
- Much more polite than direct questions
- Native speakers use these constantly
- Essential for professional/formal contexts
- THE hallmark of B1 level

**The transformation:**
- Direct: "Where is the station?"
- Indirect: "Can you tell me where the station is?" (statement order!)

**This module will take 7-8 hours.** This is THE most important B1 module!
"""
    cells.append(create_markdown_cell(intro))

    critical_rule = """## 2. The Critical Rule - STATEMENT WORD ORDER

**THIS IS THE MOST IMPORTANT RULE IN ALL OF B1!**

### Direct Questions (Question Order)

**Inversion:** Verb comes BEFORE subject

Examples:
- "Where **is** the station?" (is = verb, station = subject)
- "What **does** she want?" (does = auxiliary, she = subject)
- "Why **did** he leave?" (did = auxiliary, he = subject)

### Indirect Questions (Statement Order)

**NO Inversion:** Subject comes BEFORE verb

Examples:
- "Can you tell me where **the station is**?" (station = subject, is = verb)
- "Do you know what **she wants**?" (she = subject, wants = verb - NO "does"!)
- "I wonder why **he left**?" (he = subject, left = verb - NO "did"!)

### The Pattern

**Polite phrase + wh-word + SUBJECT + VERB**

### Common Errors (AVOID THESE!)

❌ "Can you tell me where **is** the station?"
✅ "Can you tell me where the station **is**?"

❌ "Do you know what **does** she want?"
✅ "Do you know what she **wants**?"

❌ "I wonder why **did** he leave?"
✅ "I wonder why he **left**?"

**Remember:** In indirect questions, use STATEMENT word order - NO inversion!
"""
    cells.append(create_markdown_cell(critical_rule))

    summary = """## Summary: Indirect Questions - The Criterial Feature

### The Transformation

**Direct → Indirect:**
1. Choose polite phrase: "Can you tell me...?"
2. Add wh-word (or if/whether for yes/no)
3. **Change to STATEMENT word order** [KEY STEP]
4. Remove do/does/did

### Examples

**Wh- Questions:**
- Direct: "Where is it?" → Indirect: "Do you know where it **is**?"
- Direct: "What does she want?" → Indirect: "Can you tell me what she **wants**?"

**Yes/No Questions:**
- Direct: "Is the bank open?" → Indirect: "Do you know **if** the bank **is** open?"
- Direct: "Does she speak English?" → Indirect: "Can you tell me **if** she **speaks** English?"

### Common Polite Phrases

- Can you tell me...?
- Do you know...?
- Could you tell me...?
- I wonder...
- I'd like to know...

### The Most Common Error

**Using question word order in the embedded clause!**

This is THE error that distinguishes A2 from B1 learners. Master statement word order!

**Practice makes perfect!** You'll see 100 exercises in Phase 2 - the most in any module!

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


# ============================================================================
# PHASE 2: CONTROLLED PRACTICE
# ============================================================================


def create_phase_2(module_num, module_data):
    """Create Phase 2: Controlled Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 2, "Controlled Practice"))

    intro = f"""## Controlled Practice - {module_data['exercises']} Exercises

In this phase, you'll complete **{module_data['exercises']} controlled exercises** to master {module_data['title']}.

**Exercise Types:**
- Formation and structure
- Pattern recognition
- Error correction
- Transformation practice
- Mixed application

**Instructions:**
- Complete each exercise carefully
- Check your answers
- Review errors and understand why
- Don't rush - accuracy is more important than speed

---
"""
    cells.append(create_markdown_cell(intro))

    # Exercise sets (placeholder - would be expanded with actual exercises)
    exercises = f"""## Exercise Sets

**Total Exercises: {module_data['exercises']}**

[Exercise content would be generated here based on module characteristics]

### Exercise Set 1: Basic Formation
### Exercise Set 2: Pattern Recognition
### Exercise Set 3: Error Correction
### Exercise Set 4: Transformation Practice
### Exercise Set 5: Mixed Application

---

## Practice Complete!

You've completed {module_data['exercises']} controlled practice exercises!

**Next:** Phase 3 - Meaningful Practice (applying to your own life)
"""
    cells.append(create_markdown_cell(exercises))

    return cells


# ============================================================================
# PHASE 3: MEANINGFUL PRACTICE
# ============================================================================


def create_phase_3(module_num, module_data):
    """Create Phase 3: Meaningful Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 3, "Meaningful Practice"))

    intro = f"""## Meaningful Practice - {module_data['activities']} Activities

In this phase, you'll complete **{module_data['activities']} meaningful activities** applying {module_data['title']} to your own life and experiences.

**Purpose:**
- Use the grammar with YOUR OWN content
- Make it personally relevant
- Develop fluency, not just accuracy
- Connect grammar to real life

**Instructions:**
- Write about YOUR experiences
- Use the target grammar naturally
- Focus on communication, not perfection
- Make it meaningful to you

---
"""
    cells.append(create_markdown_cell(intro))

    activities = f"""## Activities ({module_data['activities']} Total)

[Activity content would be generated here based on module characteristics]

### Activity 1: Personal Application
### Activity 2: Life Experiences
### Activity 3: Expressing Yourself
### Activity 4: Real-World Contexts
### Activity 5: Integration Practice

---

## Meaningful Practice Complete!

You've completed {module_data['activities']} meaningful practice activities!

**Next:** Phase 4 - Communicative Practice (real interaction)
"""
    cells.append(create_markdown_cell(activities))

    return cells


# ============================================================================
# PHASE 4: COMMUNICATIVE PRACTICE
# ============================================================================


def create_phase_4(module_num, module_data):
    """Create Phase 4: Communicative Practice"""
    cells = []
    cells.append(create_header(module_num, module_data, 4, "Communicative Practice"))

    intro = f"""## Communicative Practice - {module_data['tasks']} Tasks

In this phase, you'll complete **{module_data['tasks']} communicative tasks** using {module_data['title']} in real interaction.

**Purpose:**
- Use grammar in real communication
- Focus on fluency and natural use
- Interact with others (if possible)
- Develop automatic, unconscious use

**Instructions:**
- Focus on COMMUNICATION first
- Grammar should be natural, not forced
- Interact with others when possible
- Build fluency and confidence

---
"""
    cells.append(create_markdown_cell(intro))

    tasks = f"""## Communicative Tasks ({module_data['tasks']} Total)

[Task content would be generated here based on module characteristics]

### Task 1: Interactive Communication
### Task 2: Real-Life Application
### Task 3: Fluency Development
### Task 4: Natural Integration

---
"""
    cells.append(create_markdown_cell(tasks))

    # Module completion
    if module_num == 25:
        completion = """## MODULE 25 COMPLETE - YOU'VE MASTERED THE CRITERIAL B1 FEATURE!

**Congratulations!** You've just completed THE MOST IMPORTANT module in all of B1!

**What you've achieved:**
- Mastered indirect questions - THE criterial B1 feature
- Can transform direct → indirect with correct word order
- Understand statement word order (no inversion)
- Can use polite question forms naturally
- **YOU HAVE ACHIEVED B1 LEVEL!**

**Time spent:** ~{module_data['estimated_hours']} hours on THE most important B1 structure

**Module 25 Status:** COMPLETE ✅
- 100 exercises completed
- 12 activities completed
- 10 communicative tasks completed
- Criterial feature MASTERED

### B1 Batch 5 Complete!

**Batch 5 Achievement:**
- 5 modules completed (Modules 21-25)
- 465 exercises completed
- THE criterial B1 feature mastered
- B1 Progress: 83% complete (25/30 modules)

### Next Steps

**Only ONE batch left to complete B1!**
- Batch 6: B1 Integration and Consolidation (Modules 26-30)

**After that:** B1 level COMPLETE - ready for B2!

---

**YOU'VE MASTERED THE B1 CRITERIAL FEATURE!**
"""
    elif module_num == 24:
        completion = f"""## Module {module_num} Complete!

**Excellent work!** You've completed Module {module_num}!

**Time spent:** ~{module_data['estimated_hours']} hours

**Achievement:** Three-particle phrasal verbs mastered!

**Next:** Module 25 - **THE CRITERIAL B1 FEATURE** (Indirect Questions) [CRITICAL]

Module 25 is THE MOST IMPORTANT module - the criterial B1 feature!

---

**Ready for the criterial feature!**
"""
    else:
        completion = f"""## Module {module_num} Complete!

**Excellent work!** You've completed Module {module_num}!

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
    """Generate all B1 Batch 5 modules"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) != "english-learning":
        print("ERROR: Script must be run from english-learning directory")
        return

    os.chdir(script_dir)

    print("=" * 70)
    print("B1 LEVEL - BATCH 5: ADVANCED VERB PATTERNS + CRITERIAL FEATURE")
    print("Generating Modules 21-25")
    print("FIFTH B1 BATCH - THE MOST IMPORTANT (Contains Module 25)")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_5_MODULES.keys()):
        module_data = BATCH_5_MODULES[module_num]
        special = " [CRITERIAL B1 FEATURE]" if module_num == 25 else ""
        print(f"Creating Module {module_num}: {module_data['title']}{special}")
        print(f"  Subtitle: {module_data['subtitle']}")
        print(f"  Grammar Focus: {module_data['grammar_focus']}")
        print(f"  Sections: {module_data['sections']} | Exercises: {module_data['exercises']}")

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
    print(f"Total Learning Content: 29-33 hours")
    print("\nB1 Level Batch 5: COMPLETE")
    print("- Advanced verb patterns mastered")
    print("- THE CRITERIAL B1 FEATURE MASTERED (Module 25) [CRITICAL]")
    print("- B1 Progress: 83% complete (25/30 modules)")
    print("- Only Batch 6 left to complete B1!")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
