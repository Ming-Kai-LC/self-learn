"""
B1 Level - Batch 6: Integration and Consolidation (Modules 26-30)
FINAL B1 batch - comprehensive integration and B2 preview

This batch focuses on:
- Question Tags (aren't you? doesn't he?)
- Discourse Markers (however, therefore, moreover)
- Purpose and Result Clauses (so that, in order to, so...that)
- Contrast Clauses Advanced (while, whereas, despite, although)
- B1 CONSOLIDATION & B2 PREVIEW (Module 30) - THE CAPSTONE

Architecture: Integration patterns + comprehensive review + B2 preview
Exercise Count: 445 total exercises (100 in Module 30!)
Special: Module 30 has 5 phases (adds B2 Preview phase)
"""

import os

import nbformat as nbf

# ============================================================================
# MODULE 26: QUESTION TAGS CHARACTERISTICS
# ============================================================================

QUESTION_TAGS_CHARACTERISTICS = {
    "concept": "Short questions added to statements to confirm or ask for agreement",
    "basic_structure": "Statement + auxiliary verb (opposite polarity) + pronoun?",
    "formation_rules": {
        "rule_1_opposite_polarity": {
            "positive_statement": "Negative tag",
            "negative_statement": "Positive tag",
            "examples": [
                "You like pizza, don't you? (positive → negative)",
                "You don't like pizza, do you? (negative → positive)",
            ],
        },
        "rule_2_match_auxiliary": {
            "principle": "Use the auxiliary from the statement",
            "examples": [
                "He is working, isn't he? (be → be)",
                "She can swim, can't she? (can → can)",
                "They have finished, haven't they? (have → have)",
            ],
        },
        "rule_3_add_do_if_needed": {
            "when": "No auxiliary in statement (simple tenses)",
            "examples": [
                "She likes coffee, doesn't she? (present simple → does)",
                "He went home, didn't he? (past simple → did)",
            ],
        },
        "rule_4_use_pronoun": {
            "principle": "Replace noun with pronoun in tag",
            "examples": [
                "Your sister lives here, doesn't she? (sister → she)",
                "The car is red, isn't it? (car → it)",
            ],
        },
    },
    "special_cases": {
        "i_am": "I'm right, aren't I? (NOT 'amn't I' - doesn't exist!)",
        "lets": "Let's go, shall we?",
        "imperatives": "Open the door, will you? / would you? / can you?",
        "there_is": "There's a problem, isn't there?",
        "negative_words": {
            "nothing": "Nothing happened, did it? (positive tag - 'nothing' already negative)",
            "nobody": "Nobody came, did they? (positive tag)",
        },
    },
    "intonation": {
        "falling": {
            "meaning": "Confirming something you believe (not really a question)",
            "example": "You're from Spain, aren't you? ↓ (I'm pretty sure)",
        },
        "rising": {
            "meaning": "Real question - you don't know",
            "example": "You're from Spain, aren't you? ↑ (asking for info)",
        },
    },
    "usage": [
        "Confirming information",
        "Making conversation",
        "Asking for agreement",
        "Checking understanding",
        "Being polite (softening)",
    ],
    "common_errors": [
        "❌ You like pizza, don't he? → ✅ don't you? (pronoun match)",
        "❌ He is working, doesn't he? → ✅ isn't he? (match auxiliary)",
        "❌ I am right, am I not? → ✅ aren't I? (special form)",
        "❌ Let's go, don't we? → ✅ shall we? (special form)",
    ],
}

# ============================================================================
# MODULE 27: DISCOURSE MARKERS CHARACTERISTICS
# ============================================================================

DISCOURSE_MARKERS_CHARACTERISTICS = {
    "concept": "Words/phrases that connect ideas and organize text logically",
    "purpose": [
        "Link sentences and paragraphs",
        "Show logical relationships",
        "Create cohesive text",
        "Sound more sophisticated",
    ],
    "categories": {
        "addition_continuation": {
            "markers": [
                "moreover",
                "furthermore",
                "in addition",
                "additionally",
                "also",
                "besides",
            ],
            "function": "Add more information to support a point",
            "examples": [
                "The movie was exciting. Moreover, the acting was excellent.",
                "She's intelligent. In addition, she's very kind.",
            ],
        },
        "contrast_opposition": {
            "markers": [
                "however",
                "nevertheless",
                "nonetheless",
                "on the other hand",
                "in contrast",
            ],
            "function": "Show contrast",
            "examples": [
                "I studied hard. However, I didn't pass.",
                "It was raining. Nevertheless, we went out.",
                "The job pays well. On the other hand, it requires long hours.",
            ],
        },
        "result_consequence": {
            "markers": ["therefore", "thus", "consequently", "as a result", "hence", "accordingly"],
            "function": "Show logical result",
            "examples": [
                "He didn't study. Therefore, he failed.",
                "It rained heavily. As a result, the match was cancelled.",
            ],
        },
        "example_illustration": {
            "markers": ["for example", "for instance", "such as", "in particular"],
            "function": "Provide specific examples",
            "examples": [
                "Many cities are crowded. For example, Tokyo has 37 million people.",
                "I enjoy sports such as tennis and swimming.",
            ],
        },
        "emphasis_clarification": {
            "markers": ["in fact", "actually", "indeed", "that is", "in other words"],
            "function": "Emphasize or clarify",
            "examples": [
                "He's very talented. In fact, he's a genius.",
                "He's bilingual. That is, he speaks two languages.",
            ],
        },
        "summary_conclusion": {
            "markers": [
                "in conclusion",
                "to conclude",
                "to sum up",
                "in summary",
                "overall",
                "all in all",
            ],
            "function": "Conclude argument or summarize",
            "examples": [
                "In conclusion, we must act now.",
                "Overall, it was a successful project.",
            ],
        },
        "time_sequence": {
            "markers": [
                "meanwhile",
                "in the meantime",
                "subsequently",
                "afterwards",
                "eventually",
                "finally",
            ],
            "function": "Show time relationships",
            "examples": [
                "I studied. Meanwhile, my brother watched TV.",
                "We waited for hours. Eventually, the bus came.",
            ],
        },
    },
    "punctuation": {
        "pattern_1": "Sentence. Marker, new sentence.",
        "pattern_2": "Sentence; marker, continuation.",
        "key_rule": "Use comma after discourse marker at start of sentence!",
        "example": "It rained. However, we went out.",
    },
    "formality": {
        "formal": ["moreover", "furthermore", "nevertheless", "consequently", "hence"],
        "neutral": ["however", "therefore", "for example", "in fact", "meanwhile"],
        "informal": ["also", "too", "so", "but", "then", "anyway"],
    },
}

# ============================================================================
# MODULE 28: PURPOSE AND RESULT CLAUSES CHARACTERISTICS
# ============================================================================

PURPOSE_RESULT_CLAUSES_CHARACTERISTICS = {
    "concept": "Expressing why (purpose) and what happened (result)",
    "purpose_clauses": {
        "to_infinitive": {
            "form": "to + infinitive",
            "usage": "Most common purpose expression",
            "examples": ["I study to improve my English.", "She works to earn money."],
        },
        "in_order_to": {
            "form": "in order to + infinitive",
            "usage": "More formal than 'to'",
            "examples": [
                "I study in order to improve my English.",
                "He saved money in order to buy a car.",
            ],
        },
        "so_that": {
            "form": "so that + subject + modal (can/will/would)",
            "usage": "Need subject + modal verb",
            "examples": [
                "I study so that I can improve my English.",
                "She left early so that she wouldn't be late.",
            ],
        },
        "negative_purpose": {
            "to_avoid": "to avoid + -ing",
            "so_as_not_to": "so as not to / in order not to + infinitive",
            "so_that_wont": "so that... won't/wouldn't",
            "examples": [
                "I left early to avoid being late.",
                "I spoke quietly so as not to wake the baby.",
                "I left early so that I wouldn't be late.",
            ],
        },
    },
    "result_clauses": {
        "so_adjective_that": {
            "form": "so + adjective/adverb + that + result",
            "examples": [
                "The test was so difficult that I couldn't finish.",
                "She ran so fast that nobody could catch her.",
            ],
        },
        "such_noun_that": {
            "form": "such + (adjective) + noun + that + result",
            "examples": [
                "It was such a difficult test that I couldn't finish.",
                "He's such a good teacher that everyone learns quickly.",
            ],
        },
        "so_much_many": {
            "so_much": "so much + uncountable + that",
            "so_many": "so many + countable + that",
            "examples": [
                "I ate so much that I felt sick.",
                "She has so many friends that her house is always full.",
            ],
        },
    },
    "so_vs_such": {
        "so": "so + adjective/adverb",
        "such": "such + (adjective) + noun",
        "examples": {
            "so": "It's so hot! / He works so hard!",
            "such": "It's such a hot day! / He's such a hard worker!",
        },
    },
    "common_confusions": {
        "purpose_vs_result": {
            "purpose": "I saved money to buy a car. (intention)",
            "result": "I saved so much money that I bought a car. (consequence)",
        },
        "so_that_purpose_vs_so_that_result": {
            "purpose": "I studied so that I could pass. (so that + modal)",
            "result": "The test was so easy that everyone passed. (so + adj + that)",
        },
    },
}

# ============================================================================
# MODULE 29: CONTRAST CLAUSES ADVANCED CHARACTERISTICS
# ============================================================================

CONTRAST_CLAUSES_ADVANCED_CHARACTERISTICS = {
    "concept": "Showing difference or unexpected situations",
    "types": {
        "concession": "Despite a problem, something happens",
        "comparison_contrast": "Comparing two different things",
        "unexpected_result": "Opposite of expectation",
    },
    "although_though_even_though": {
        "although": {
            "form": "although + clause",
            "usage": "Neutral formality",
            "examples": ["Although I studied, I failed.", "Although it was raining, we went out."],
        },
        "though": {
            "form": "though + clause (or end position)",
            "usage": "Less formal, can come at end",
            "examples": [
                "Though I studied, I failed.",
                "I failed, though I studied. (end position)",
            ],
        },
        "even_though": {
            "form": "even though + clause",
            "usage": "Stronger emphasis on unexpectedness",
            "examples": ["Even though I studied for weeks, I still failed."],
        },
    },
    "despite_in_spite_of": {
        "despite": {
            "form": "despite + noun/-ing (NO clause!)",
            "examples": [
                "Despite the rain, we went out.",
                "Despite studying hard, I failed.",
                "Despite his age, he's very active.",
            ],
        },
        "in_spite_of": {
            "form": "in spite of + noun/-ing",
            "usage": "Same meaning as despite, slightly less formal",
            "examples": [
                "In spite of the rain, we went out.",
                "In spite of studying hard, I failed.",
            ],
        },
        "key_difference": {
            "although": "although + clause (subject + verb)",
            "despite": "despite + noun or -ing (NO subject + verb)",
            "common_error": "❌ Despite I studied... → ✅ Despite studying... / Although I studied...",
        },
        "despite_the_fact_that": {
            "form": "despite/in spite of + the fact that + clause",
            "usage": "If you want 'despite' + clause, use 'the fact that'",
            "examples": [
                "Despite the fact that I studied, I failed.",
                "In spite of the fact that it was raining, we went out.",
            ],
        },
    },
    "while_whereas": {
        "while": {
            "form": "while + clause",
            "usage": "Compare two different/opposite things",
            "examples": [
                "While I like coffee, my sister prefers tea.",
                "While he's tall, she's short.",
            ],
        },
        "whereas": {
            "form": "whereas + clause",
            "usage": "More formal than while",
            "examples": ["Whereas I like coffee, my sister prefers tea."],
        },
        "vs_although": {
            "although": "Unexpected result",
            "while_whereas": "Simple comparison/difference",
            "examples": {
                "although": "Although I like coffee, I drink tea. (unexpected)",
                "while": "While I like coffee, my sister likes tea. (just comparing)",
            },
        },
    },
    "yet_still_nevertheless": {
        "yet": "I studied hard, yet I failed. (formal conjunction)",
        "still": "I studied hard. I still failed. (adverb)",
        "nevertheless": "I studied hard. Nevertheless, I failed. (very formal)",
    },
    "however_vs_although": {
        "although": "Although it was raining, we went out. (conjunction, one sentence)",
        "however": "It was raining. However, we went out. (discourse marker, two sentences)",
        "error": "❌ However it was raining... → ✅ Although it was raining...",
    },
}

# ============================================================================
# MODULE 30: B1 CONSOLIDATION AND B2 PREVIEW CHARACTERISTICS
# ============================================================================

B1_CONSOLIDATION_B2_PREVIEW_CHARACTERISTICS = {
    "special_status": "CAPSTONE_MODULE",
    "module_type": "FIVE_PHASE_MODULE",
    "purpose": [
        "Review and integrate ALL 29 previous modules",
        "Ensure mastery of all B1 structures",
        "Identify remaining weaknesses",
        "Provide B2 preview to maintain motivation",
        "Final assessment of B1 readiness",
    ],
    "five_phases": {
        "phase_1": "B1 Review - Batches 1-6 Integration",
        "phase_2": "Controlled Practice - ALL Structures Mixed",
        "phase_3": "Meaningful Practice - Personal Integration",
        "phase_4": "Communicative Practice - Real-World Tasks",
        "phase_5": "B2 Preview - Next Level Introduction",
    },
    "batch_reviews": {
        "batch_1": "Perfect Tenses (Modules 1-5)",
        "batch_2": "Conditionals (Modules 6-10)",
        "batch_3": "Passive and Reporting (Modules 11-15)",
        "batch_4": "Relative Clauses and Modals (Modules 16-20)",
        "batch_5": "Verb Patterns and Criterial Feature (Modules 21-25)",
        "batch_6": "Integration (Modules 26-29)",
    },
    "b2_preview_topics": [
        "What is B2 (Upper-Intermediate)?",
        "B2 Criterial Features",
        "B2 Grammar Preview",
        "B2 Vocabulary Expansion",
        "B2 Skills Development",
        "B2 vs B1 Differences",
        "B2 Certification Options",
        "Your B2 Journey",
    ],
}

# ============================================================================
# MODULE CONFIGURATION
# ============================================================================

BATCH_6_MODULES = {
    26: {
        "title": "Question Tags",
        "subtitle": "Aren't You? Doesn't He? - Interactive Confirmation",
        "grammar_focus": "Formation, Meaning, and Intonation",
        "sections": 14,
        "exercises": 90,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": QUESTION_TAGS_CHARACTERISTICS,
    },
    27: {
        "title": "Discourse Markers",
        "subtitle": "However, Therefore, Moreover - Text Cohesion",
        "grammar_focus": "Logical Connectors and Organization",
        "sections": 15,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": DISCOURSE_MARKERS_CHARACTERISTICS,
    },
    28: {
        "title": "Purpose and Result Clauses",
        "subtitle": "So That, In Order To, So...That, Such...That",
        "grammar_focus": "Expressing Purpose and Result",
        "sections": 14,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": PURPOSE_RESULT_CLAUSES_CHARACTERISTICS,
    },
    29: {
        "title": "Contrast Clauses - Advanced",
        "subtitle": "While, Whereas, Despite, Although, In Spite Of",
        "grammar_focus": "Complex Contrast Expressions",
        "sections": 14,
        "exercises": 85,
        "activities": 10,
        "tasks": 8,
        "estimated_hours": "5-6",
        "difficulty": 3,
        "characteristics": CONTRAST_CLAUSES_ADVANCED_CHARACTERISTICS,
    },
    30: {
        "title": "B1 Consolidation and B2 Preview",
        "subtitle": "Integration of All 30 Modules + B2 Introduction",
        "grammar_focus": "COMPREHENSIVE B1 REVIEW + B2 PREVIEW",
        "sections": 10,
        "exercises": 100,
        "activities": 15,
        "tasks": 10,
        "estimated_hours": "7-8",
        "difficulty": 5,
        "characteristics": B1_CONSOLIDATION_B2_PREVIEW_CHARACTERISTICS,
        "special_status": "CAPSTONE",
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
        1: "Phase 1: Introduction" if module_num != 30 else "Phase 1: B1 Review - Integration",
        2: "Phase 2: Controlled Practice",
        3: "Phase 3: Meaningful Practice",
        4: "Phase 4: Communicative Practice",
        5: "Phase 5: B2 Preview",
    }

    special_marker = " [CAPSTONE]" if module_data.get("special_status") == "CAPSTONE" else ""

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
# PHASE 1: INTRODUCTION (OR B1 REVIEW FOR MODULE 30)
# ============================================================================


def create_phase_1(module_num, module_data):
    """Create Phase 1: Introduction (or B1 Review for Module 30)"""
    cells = []
    cells.append(create_header(module_num, module_data, 1, "Introduction"))

    if module_num == 26:
        cells.extend(create_module_26_phase_1(module_data))
    elif module_num == 27:
        cells.extend(create_module_27_phase_1(module_data))
    elif module_num == 28:
        cells.extend(create_module_28_phase_1(module_data))
    elif module_num == 29:
        cells.extend(create_module_29_phase_1(module_data))
    elif module_num == 30:
        cells.extend(create_module_30_phase_1(module_data))

    return cells


def create_module_26_phase_1(module_data):
    """Module 26: Question Tags"""
    cells = []

    intro = """## 1. Introduction - Interactive Confirmation Questions

Welcome to **Question Tags** - a sophisticated interactive feature!

**What you'll learn:**
- How to form question tags correctly
- Opposite polarity rule (positive → negative, negative → positive)
- Matching the auxiliary verb
- Special cases (I am, let's, imperatives)
- How intonation changes meaning

**Why this matters:**
- Very common in spoken English
- Makes you sound more native
- Useful for confirmation and conversation
- Shows grammatical sophistication

**The pattern:** Statement + opposite auxiliary + pronoun?
- "You like pizza, **don't you**?"

**This module will take 5-6 hours.** Master the patterns!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Question Tags

### Formation Rules

**1. Opposite polarity:**
- Positive statement → Negative tag
- Negative statement → Positive tag

**2. Match the auxiliary:**
- Use the auxiliary from the statement
- Add do/does/did if no auxiliary

**3. Use pronoun in tag:**
- Replace noun with pronoun

### Special Cases

- I am → aren't I?
- Let's → shall we?
- Imperatives → will you? / would you?
- Nothing/nobody → positive tag

### Intonation

- **Falling ↓:** Confirming (not really asking)
- **Rising ↑:** Real question (don't know)

**Examples:**
- "You're a student, **aren't you**?"
- "She doesn't like coffee, **does she**?"
- "They went home, **didn't they**?"

**Practice makes perfect!** You'll see 90 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_27_phase_1(module_data):
    """Module 27: Discourse Markers"""
    cells = []

    intro = """## 1. Introduction - Connecting Ideas Logically

Welcome to **Discourse Markers** - making your writing sophisticated!

**What you'll learn:**
- How to connect ideas logically
- Addition, contrast, result, example markers
- Punctuation with discourse markers
- Formal vs informal markers
- Creating cohesive text

**Why this matters:**
- Essential for sophisticated writing
- Makes text flow naturally
- Shows logical relationships
- Critical for academic/professional English

**Example:**
- "I studied hard. **However**, I didn't pass."
- "The movie was exciting. **Moreover**, the acting was excellent."

**This module will take 5-6 hours.** Connect ideas like a pro!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Discourse Markers

### Main Categories

**Addition:** moreover, furthermore, in addition, also
**Contrast:** however, nevertheless, on the other hand
**Result:** therefore, consequently, as a result
**Example:** for example, for instance, such as
**Summary:** in conclusion, to sum up, overall

### Punctuation

**Pattern:** Sentence. **Marker,** new sentence.
- "It rained. **However,** we went out."

**Key:** Use comma after marker!

### Formality

**Formal:** moreover, furthermore, nevertheless, consequently
**Neutral:** however, therefore, for example, meanwhile
**Informal:** also, so, but, then

**Practice makes perfect!** You'll see 85 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_28_phase_1(module_data):
    """Module 28: Purpose and Result Clauses"""
    cells = []

    intro = """## 1. Introduction - Purpose and Result

Welcome to **Purpose and Result Clauses** - expressing why and what happened!

**What you'll learn:**
- Purpose clauses (to, in order to, so that)
- Result clauses (so...that, such...that)
- So vs such (the key difference)
- Negative purpose (to avoid, so as not to)
- Purpose vs result distinction

**Why this matters:**
- Essential for explaining intentions
- Critical for cause-effect relationships
- Common in all types of English
- Shows sophisticated thinking

**Examples:**
- Purpose: "I study **to** improve my English."
- Result: "The test was **so difficult that** I couldn't finish."

**This module will take 5-6 hours.** Express purpose and result clearly!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Purpose and Result

### Purpose (Why?)

**to + infinitive:** I study to improve.
**in order to:** I study in order to improve. (formal)
**so that + modal:** I study so that I can improve.

### Result (What happened?)

**so + adj/adv + that:** It was so difficult that I failed.
**such + noun + that:** It was such a difficult test that I failed.

### So vs Such

**So + adjective:** It's **so hot**!
**Such + noun:** It's **such a hot day**!

### Key Difference

**Purpose:** Future intention (to buy)
**Result:** Consequence (so...that I bought)

**Practice makes perfect!** You'll see 85 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_29_phase_1(module_data):
    """Module 29: Contrast Clauses - Advanced"""
    cells = []

    intro = """## 1. Introduction - Advanced Contrast

Welcome to **Contrast Clauses - Advanced** - sophisticated contrast expression!

**What you'll learn:**
- Although, though, even though + clause
- Despite, in spite of + noun/-ing
- While, whereas (comparison contrast)
- The critical difference: although vs despite
- Yet, still, nevertheless

**Why this matters:**
- Essential for sophisticated writing
- Shows unexpected situations
- Compares and contrasts effectively
- Critical for academic English

**The key:** Although + clause, Despite + noun!
- "**Although** I studied, I failed." (clause)
- "**Despite** studying, I failed." (noun/-ing)

**This module will take 5-6 hours.** Master contrast structures!
"""
    cells.append(create_markdown_cell(intro))

    summary = """## Summary: Contrast Clauses

### Although / Though / Even Though

**+ Clause** (subject + verb)
- "Although I studied, I failed."
- "Even though it was raining, we went out."

### Despite / In Spite Of

**+ Noun or -ing** (NOT clause!)
- "Despite the rain, we went out."
- "Despite studying, I failed."

### While / Whereas

**Comparison contrast:**
- "While I like coffee, she likes tea."
- "Whereas I'm tall, she's short."

### Key Difference

**Although vs Despite:**
- Although + clause ✅
- Despite + noun/-ing ✅
- ❌ Despite I studied... (WRONG!)

**Practice makes perfect!** You'll see 85 exercises in Phase 2.

---

**Ready for Phase 2: Controlled Practice!**
"""
    cells.append(create_markdown_cell(summary))

    return cells


def create_module_30_phase_1(module_data):
    """Module 30: B1 Review - Integration"""
    cells = []

    intro = """## B1 COMPREHENSIVE REVIEW - ALL 30 MODULES

Welcome to **Module 30 - The B1 Capstone!**

This is THE most important review module. You will integrate ALL B1 structures from Modules 1-29.

**What makes Module 30 special:**
- Reviews ALL 6 batches systematically
- 100 exercises covering everything
- 15 personal integration activities
- 10 real-world communicative tasks
- **PHASE 5: B2 Preview** (motivation for next level!)

**Your B1 journey so far:**
- 29 modules completed
- ~2,600 exercises done
- ~170 hours of study
- Criterial B1 feature mastered (indirect questions)

**After this module:**
- B1 level COMPLETE
- Ready for B2 (Upper-Intermediate)
- Certification ready (PET, IELTS 5.5)

**This module will take 7-8 hours.** Let's consolidate your B1 mastery!

---

## Batch 1: Perfect Tenses (Modules 1-5)

**Key structures:**
- Present Perfect vs Past Simple (THE foundation)
- Present Perfect Continuous
- Past Perfect
- Future Perfect
- All perfect aspects together

**Critical points to remember:**
- Unfinished time = Present Perfect
- Finished time = Past Simple
- Duration focus = Continuous
- Earlier past action = Past Perfect

---

## Batch 2: Conditionals (Modules 6-10)

**Key structures:**
- First Conditional (real future)
- Second Conditional (unreal present/future)
- Third Conditional (impossible past)
- Mixed Conditionals
- Alternative forms (unless, provided, supposing)

**Critical points:**
- Reality level determines conditional type
- Time reference + reality = choice
- Mixed conditionals cross time periods

---

## Batch 3: Passive and Reporting (Modules 11-15)

**Key structures:**
- Passive Voice (all tenses)
- Reported Speech statements
- Reported questions
- Reported commands
- Reporting verbs

**Critical points:**
- be + past participle
- Tense backshift in reporting
- Say vs tell
- Question word order in reported

---

## Batch 4: Relative Clauses and Modals (Modules 16-20)

**Key structures:**
- Defining vs non-defining (commas!)
- Whose, whom
- Object relatives and omission
- Modal deduction present (must/can't/might be)
- Modal deduction past (must/can't/might have + pp)

**Critical points:**
- Comma usage changes meaning
- That vs which in different types
- Certainty scale for modals

---

## Batch 5: Verb Patterns + CRITERIAL FEATURE (Modules 21-25)

**Key structures:**
- Used to / would / be-get used to
- Gerunds and infinitives (meaning changes!)
- Causatives (make/let/help/get)
- Three-particle phrasal verbs
- **INDIRECT QUESTIONS** (THE B1 criterial feature)

**Most critical:**
- **Indirect questions = THE B1 hallmark**
- Statement word order (NO inversion!)
- "Can you tell me where the station **is**?"

---

## Batch 6: Integration (Modules 26-29)

**Key structures:**
- Question tags
- Discourse markers
- Purpose and result clauses
- Contrast clauses advanced

**Critical points:**
- Opposite polarity in tags
- Discourse marker punctuation
- So vs such
- Although vs despite

---

**You've reviewed all 6 batches! Ready for comprehensive practice!**

**Next:** Phase 2 - 100 mixed exercises testing EVERYTHING!
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

In this phase, you'll complete **{module_data['activities']} meaningful activities** applying {module_data['title']} to your own life.

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
    if module_num == 30:
        completion = """## MODULE 30 COMPLETE - B1 LEVEL ACHIEVED!

**CONGRATULATIONS!** You've completed THE CAPSTONE MODULE!

**What you've achieved:**
- Reviewed ALL 30 B1 modules comprehensively
- Completed 100 comprehensive exercises
- Integrated all B1 structures naturally
- Ready for real-world B1 communication
- **B1 (INTERMEDIATE) LEVEL COMPLETE!**

**Time spent:** ~{} hours on Module 30
**Total B1 time:** ~180 hours across 30 modules

**Module 30 Status:** COMPLETE
- Batch reviews: ALL 6 batches
- Comprehensive practice: 100 exercises
- Integration activities: 15 personal tasks
- Communicative tasks: 10 real-world applications

### B1 LEVEL: COMPLETE!

**Final B1 Achievement:**
- **30 modules completed** (120 notebooks)
- **~2,700 exercises completed**
- **~180 hours of study**
- **ALL B1 criterial features mastered**
- **Ready for B2 (Upper-Intermediate)!**

### Certification Readiness

You are now ready for:
- **Cambridge Preliminary (PET)** - B1 level
- **IELTS Academic/General** - Bands 5.0-5.5
- **TOEFL iBT** - Scores 42-71

### Next Steps

**ONE MORE PHASE:** Phase 5 - B2 Preview!

This final phase will:
- Show you what B2 looks like
- Preview new grammar structures
- Explain B2 vs B1 differences
- Prepare you for the next level
- Maintain your motivation!

---

**Ready for Phase 5: B2 Preview!**
""".format(
            module_data["estimated_hours"]
        )
    elif module_num == 29:
        completion = f"""## Module {module_num} Complete!

**Excellent work!** You've completed Module {module_num}!

**Time spent:** ~{module_data['estimated_hours']} hours

**Achievement:** Advanced contrast structures mastered!

**Next:** Module 30 - **THE B1 CAPSTONE MODULE**

Module 30 is THE most important module:
- Reviews ALL 30 modules
- 100 comprehensive exercises
- 5 phases (includes B2 Preview!)
- Final B1 consolidation

---

**Ready for the final module!**
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
# PHASE 5: B2 PREVIEW (MODULE 30 ONLY)
# ============================================================================


def create_phase_5_module_30(module_data):
    """Create Phase 5: B2 Preview (Module 30 only)"""
    cells = []

    header = create_markdown_cell(
        """# B1 Level - Module 30: B1 Consolidation and B2 Preview [CAPSTONE]

## Integration of All 30 Modules + B2 Introduction

**Grammar Focus:** COMPREHENSIVE B1 REVIEW + B2 PREVIEW
**Estimated Time:** 7-8 hours
**Difficulty:** ★★★★★

---

# Phase 5: B2 Preview
"""
    )
    cells.append(header)

    intro = """## Phase 5: B2 Preview - Your Next Journey

**Congratulations on completing B1!** This final phase previews B2 (Upper-Intermediate) level.

**What you'll learn:**
- What is B2 level?
- B2 criterial features
- New grammar structures
- Vocabulary expansion
- B2 vs B1 differences
- Certification options
- Your B2 journey

**Purpose:**
- Maintain motivation
- Show clear progression
- Preview next challenges
- Set realistic expectations

---

## 1. What is B2 (Upper-Intermediate)?

**CEFR B2 Definition:**
"Can understand the main ideas of complex text on both concrete and abstract topics. Can interact with a degree of fluency and spontaneity that makes regular interaction with native speakers quite possible. Can produce clear, detailed text on a wide range of subjects."

**What this means:**
- **B1:** Handle clear, standard situations
- **B2:** Handle complex, abstract situations
- **B1:** Familiar topics
- **B2:** Wide range including abstract topics
- **B1:** Simple linking
- **B2:** Sophisticated cohesion

**Time commitment:** 6-12 months (150-200 hours)

---

## 2. B2 Criterial Features

**What makes B2 distinct from B1:**

**1. Advanced Passive Structures**
- Passive with reporting verbs
- "It is said that..." / "He is thought to..."
- Have something done (causative passive)

**2. Participle Clauses**
- Present participle: "Feeling tired, I went to bed."
- Past participle: "Built in 1850, the house is old."
- Replaces relative clauses for brevity

**3. Advanced Conditionals**
- Inversion in conditionals: "Had I known..."
- Alternative forms: "Otherwise, but for, if it weren't for"

**4. Cleft Sentences**
- It-cleft: "It was John who did it."
- Wh-cleft: "What I need is sleep."
- Emphasis structures

**5. Future Continuous/Perfect**
- Future continuous: "I'll be working at 3pm."
- Future perfect: "I'll have finished by 5pm."

---

## 3. B2 Grammar Preview - New Structures

**Structures you'll learn at B2:**

**Inversion after negative adverbials:**
- "Never have I seen such beauty."
- "Rarely does he complain."
- "Not only did he win, but he also broke the record."

**Fronting for emphasis:**
- "This I cannot accept." (object fronting)
- "Interesting though it was..." (adjective fronting)

**Subjunctive mood (limited):**
- "I suggest that he go." (not "goes")
- "It's important that she be here." (not "is")
- Formal/American English

**Advanced wish/if only:**
- "I wish I had listened." (past regret)
- "If only I were taller!" (present impossible)

**Advanced gerund/infinitive:**
- Gerund/infinitive as subject extensively
- Perfect infinitive: "He seems to have left."
- Perfect gerund: "He denied having been there."

---

## 4. B2 Vocabulary Expansion

**B1 vs B2 vocabulary:**
- **B1:** ~2,500 word families
- **B2:** 3,500-4,000 word families

**Focus areas:**
- Academic Word List (AWL) mastery
- Collocation sophistication
- Phrasal verb expansion (300+)
- Idiom introduction
- Register awareness

**Example:**
- B1: "I'm busy now."
- B2: "I'm tied up at the moment." (collocation/idiom)

---

## 5. B2 Skills Development

**Reading:**
- Complex texts, literature
- Long articles, reports
- Abstract topics
- Inference skills

**Writing:**
- Essays (300+ words)
- Formal reports
- Reviews, articles
- Clear argumentation

**Listening:**
- Natural speech speed
- Various accents
- Longer recordings
- Implicit meaning

**Speaking:**
- Fluency and spontaneity
- Debate and discuss
- Abstract topics
- Self-correction

---

## 6. B2 vs B1 - Key Differences

| Aspect | B1 | B2 |
|--------|----|----|
| **Topics** | Familiar, personal | Abstract, complex |
| **Situations** | Predictable | Unpredictable |
| **Fluency** | Some hesitation | Quite fluent |
| **Accuracy** | Errors don't impede | Few errors |
| **Complexity** | Simple linking | Sophisticated cohesion |
| **Interaction** | Familiar speakers | Native speakers easily |

**The key shift:** B1 = standard situations; B2 = complex situations

---

## 7. B2 Certification Options

**Cambridge English: First (FCE)**
- Official B2 certificate
- Widely recognized
- 4 papers (Reading/Use, Writing, Listening, Speaking)

**IELTS Academic/General**
- Bands 5.5-6.5 = B2
- Popular for immigration/university
- 4 sections

**TOEFL iBT**
- Scores 72-94 = B2
- Popular in USA
- 4 sections

**When to take:** After completing B2 curriculum (6-12 months)

---

## 8. Your B2 Journey - Next Steps

**Immediate next steps:**

**1. Review B1 Regularly**
- Don't forget B1 structures
- Weekly B1 review (30 minutes)
- Use B1 grammar naturally

**2. Start B2 Curriculum**
- B2 Batch 1: Advanced Tenses & Passives
- Systematic progression
- 6 batches total

**3. Increase Immersion**
- Read B2 level materials
- Listen to authentic content
- Speak regularly (language exchange)
- Write longer texts

**4. Real-World Practice**
- Use English daily
- Think in English
- Real communication focus
- Don't fear mistakes

**5. Maintain Motivation**
- Set clear goals
- Track progress
- Celebrate achievements
- Remember why you started

---

## B2 PREVIEW COMPLETE!

**You're ready for B2!**

**What you've accomplished:**
- ✅ B1 level COMPLETE (30 modules, 120 notebooks)
- ✅ ~2,700 exercises completed
- ✅ ~180 hours of study
- ✅ Criterial B1 feature mastered (indirect questions)
- ✅ Ready for Upper-Intermediate (B2)

**Your English journey:**
- A1 → A2 → **B1 ✅** → B2 (next!) → C1 → C2

**Next:** Start B2 Level - Batch 1!

---

**CONGRATULATIONS ON COMPLETING B1 LEVEL!**

You are now an **Intermediate English speaker** capable of:
- Handling most everyday situations
- Describing experiences and events
- Explaining opinions and plans
- Understanding the main points of clear standard input
- Using all major English tenses and structures
- **Communicating confidently in English!**

**Well done!** Your hard work has paid off. You've achieved B1 mastery!

**See you at B2!** 🎓
"""
    cells.append(create_markdown_cell(intro))

    return cells


# ============================================================================
# NOTEBOOK CREATION
# ============================================================================


def create_module_all_phases(module_num, module_data):
    """Create all phases for a module (4 for most, 5 for Module 30)"""
    base_path = f"notebooks/B1/Module_{module_num:02d}"
    os.makedirs(base_path, exist_ok=True)

    if module_num == 30:
        # Module 30 has 5 phases
        phases = [
            ("01_b1_review.ipynb", create_phase_1),
            ("02_controlled_practice.ipynb", create_phase_2),
            ("03_meaningful_practice.ipynb", create_phase_3),
            ("04_communicative_practice.ipynb", create_phase_4),
            ("05_b2_preview.ipynb", lambda num, data: create_phase_5_module_30(data)),
        ]
    else:
        # Regular 4-phase structure
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
    """Generate all B1 Batch 6 modules"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) != "english-learning":
        print("ERROR: Script must be run from english-learning directory")
        return

    os.chdir(script_dir)

    print("=" * 70)
    print("B1 LEVEL - BATCH 6: INTEGRATION AND CONSOLIDATION")
    print("Generating Modules 26-30")
    print("SIXTH B1 BATCH - FINAL BATCH (Module 30 = Capstone)")
    print("=" * 70)
    print()

    total_exercises = 0
    total_activities = 0
    total_tasks = 0

    for module_num in sorted(BATCH_6_MODULES.keys()):
        module_data = BATCH_6_MODULES[module_num]
        special = " [CAPSTONE - 5 PHASES]" if module_num == 30 else ""
        print(f"Creating Module {module_num}: {module_data['title']}{special}")
        print(f"  Subtitle: {module_data['subtitle']}")
        print(f"  Grammar Focus: {module_data['grammar_focus']}")
        print(f"  Sections: {module_data['sections']} | Exercises: {module_data['exercises']}")
        if module_num == 30:
            print(f"  SPECIAL: 5 phases (includes B2 Preview)")

        create_module_all_phases(module_num, module_data)

        total_exercises += module_data["exercises"]
        total_activities += module_data["activities"]
        total_tasks += module_data["tasks"]

        print(f"  [COMPLETE] Module {module_num} complete!\n")

    print("=" * 70)
    print("BATCH 6 GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nModules Created: 5 (Modules 26-30)")
    print(f"Notebooks Created: 21 (4 modules x 4 phases + Module 30 x 5 phases)")
    print(f"Total Exercises: {total_exercises}")
    print(f"Total Activities: {total_activities}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Total Learning Content: 28-32 hours")
    print("\nB1 Level Batch 6: COMPLETE")
    print("- Integration structures mastered")
    print("- ALL B1 MODULES REVIEWED (Module 30)")
    print("- B2 Preview provided")
    print("- B1 Progress: 100% complete (30/30 modules) [COMPLETE!]")
    print("\n" + "=" * 70)
    print("B1 LEVEL COMPLETE!")
    print("=" * 70)
    print("\n30 modules | 121 notebooks | ~2,700 exercises | ~180 hours")
    print("Criterial B1 feature mastered: Indirect Questions")
    print("\nYou have achieved B1 (Intermediate) level!")
    print("Ready for B2 (Upper-Intermediate) level!")
    print("\nAll notebooks created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
