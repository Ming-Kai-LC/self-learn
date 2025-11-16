# English Learning Notebooks - Interactive Grammar Course

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, research-backed English grammar learning system built with Jupyter Notebooks. **A1 (Beginner) level is complete** with all **20 interactive modules**, and **A2 (Elementary) level is progressing** with Batches 1-4 (Modules 1-20) covering past tense mastery, future & time structures, modal verbs, and comparisons & descriptions, all following proven pedagogical methodologies.

## Overview

This project implements a complete English learning curriculum based on the **Cambridge English Grammar Profile**, **CEFR standards**, and applied linguistics research. It features:

- **Interactive exercises** with immediate feedback
- **Text-to-speech audio** for pronunciation practice
- **Spaced repetition system** for optimal retention
- **Progress tracking** with visual dashboards
- **5-phase learning structure** (Introduction → Controlled Practice → Meaningful Practice → Communicative Practice → Spaced Review)

## Features

### Pedagogical Foundation

Based on research showing:
- **Explicit grammar instruction** yields the highest effect size (d=1.26) among language skills
- **Spaced repetition** improves long-term retention by up to 200%
- **Practice distribution** should favor communicative practice (60-70% at intermediate levels)
- **Focus on Form** approach balances accuracy and fluency

### Technical Features

- **Interactive exercises** using ipywidgets with instant validation
- **Audio generation** using gTTS for pronunciation examples
- **Progress tracking** with JSON-based storage
- **Spaced repetition scheduler** implementing SuperMemo-inspired algorithm
- **Data visualization** using matplotlib and plotly
- **Modular architecture** for easy expansion to 160 modules (A1-C2)

## Project Structure

```
english-learning/
├── notebooks/
│   ├── A1/                     # 20 modules (COMPLETE)
│   │   ├── Module_01/          # Verb "To Be"
│   │   │   ├── 01_introduction.ipynb
│   │   │   ├── 02_controlled_practice.ipynb
│   │   │   ├── 03_meaningful_practice.ipynb
│   │   │   ├── 04_communicative_practice.ipynb
│   │   │   └── audio/
│   │   ├── Module_02/          # Personal Pronouns
│   │   ├── Module_03/          # Present Simple - Affirmative
│   │   ├── Module_04/          # Present Simple - Negatives/Questions
│   │   ├── Module_05/          # Articles and Demonstratives
│   │   ├── Module_06/          # Nouns and Plurals
│   │   ├── Module_07/          # Possessives
│   │   ├── Module_08/          # Adjectives
│   │   ├── Module_09/          # There Is/Are
│   │   └── Module_10-20/       # ... (see module descriptions below)
│   ├── A2/                     # Batches 1-4: 20 modules (Modules 1-20)
│   │   ├── Module_01/          # Past Continuous Formation
│   │   ├── Module_02/          # Past Continuous vs Past Simple
│   │   ├── Module_03/          # Past Continuous for Interrupted Actions
│   │   ├── Module_04/          # Present Perfect - Life Experiences
│   │   ├── Module_05/          # Present Perfect with Ever/Never
│   │   ├── Module_06/          # Future: Going To vs Will Review
│   │   ├── Module_07/          # Present Continuous for Future Arrangements
│   │   ├── Module_08/          # Future Time Clauses
│   │   ├── Module_09/          # Time Sequencing
│   │   ├── Module_10/          # Talking About Duration (for, since)
│   │   ├── Module_11/          # Should/Shouldn't - Advice and Recommendations
│   │   ├── Module_12/          # Must/Have To - Obligation and Necessity
│   │   ├── Module_13/          # Don't Have To vs Mustn't
│   │   ├── Module_14/          # May/Might/Could - Possibility and Permission
│   │   ├── Module_15/          # Would Like - Polite Requests
│   │   ├── Module_16/          # Comparative Adjectives - Formation and Use
│   │   ├── Module_17/          # Superlative Adjectives - The Best, The Biggest
│   │   ├── Module_18/          # As...As Comparisons - Equality
│   │   ├── Module_19/          # Adverbs of Manner and Comparison
│   │   └── Module_20/          # Intensifiers - Very, Quite, Too, Enough
│   ├── reviews/
│   │   ├── A1_Review_Modules_1-5.ipynb
│   │   └── ... (additional review notebooks)
│   └── progress_tracker.ipynb
├── utils/
│   ├── feedback_system.py      # Exercise validation and feedback
│   ├── audio_generator.py      # Text-to-speech functionality
│   └── spaced_repetition.py    # Review scheduling system
├── data/
│   └── progress.json           # Student progress tracking
├── generate_modules.py         # Module generation script
├── requirements.txt
├── English-Path.md            # Complete curriculum documentation
└── README.md
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. **Clone or navigate to the repository:**
   ```bash
   cd projects/english-learning
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Enable Jupyter widgets:**
   ```bash
   jupyter nbextension enable --py widgetsnbextension
   ```

5. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

## Usage

### Getting Started

1. **Open the Progress Tracker:**
   - Navigate to `notebooks/progress_tracker.ipynb`
   - Run all cells to see your learning dashboard
   - This will be empty initially

2. **Start with Module 1:**
   - Go to `notebooks/A1/Module_01/`
   - Open `01_introduction.ipynb`
   - Follow the 4-phase structure

3. **Complete Each Module:**
   - **Phase 1** (01_introduction.ipynb): Learn concepts with examples and audio
   - **Phase 2** (02_controlled_practice.ipynb): Complete exercises with feedback
   - **Phase 3** (03_meaningful_practice.ipynb): Write about your own life
   - **Phase 4** (04_communicative_practice.ipynb): Real communication tasks

4. **Mark Module Complete:**
   - At the end of Phase 4, uncomment and run the completion cell
   - This schedules your first review and updates the progress tracker

5. **Review Regularly:**
   - Check the progress tracker for due reviews
   - Complete review sessions on schedule
   - After Module 5, complete the consolidation review

### Learning Path

**Recommended pace:** 1-2 modules per week

- **Modules 1-5** (Weeks 1-3): Basic grammar foundations
  - Complete the consolidation review after Module 5
- **Modules 6-10** (Weeks 4-6): Expanding vocabulary and structures
  - Regular spaced repetition reviews

**Total time estimate:** 80-100 hours for complete A1 level

### Study Tips

1. **Study regularly:** 30-60 minutes daily > 4 hours once a week
2. **Complete all 4 phases:** Each phase builds on the previous
3. **Do the reviews:** Spaced repetition is crucial for retention
4. **Practice speaking:** Read exercises aloud, use the audio examples
5. **Personalize learning:** The meaningful practice phase is critical
6. **Track progress:** Use the progress tracker to stay motivated

## Module Descriptions

### Module 1: Verb "To Be"
Master am/is/are in positive, negative, and question forms. The foundation for all English grammar.

### Module 2: Personal Pronouns
Subject pronouns (I, you, he, she, it, we, they) and object pronouns (me, you, him, her, it, us, them).

### Module 3: Present Simple - Affirmative
Form positive statements with emphasis on third-person -s/es/ies rules.

### Module 4: Present Simple - Negatives and Questions
Use do/does for negatives and questions, including Wh-questions.

### Module 5: Articles and Demonstratives
Master a/an/the usage and this/that/these/those distinctions.

### Module 6: Nouns and Plurals
Regular and irregular plural forms, countable vs uncountable nouns.

### Module 7: Possessives
Possessive adjectives (my, your, his, her) and possessive 's.

### Module 8: Adjectives
Describing people, places, and things with proper adjective placement.

### Module 9: There Is/Are
Express existence and location with there is/there are constructions.

### Module 10: Prepositions
Place prepositions (in, on, at, under, behind) and time prepositions (in, on, at).

### Module 11: Question Words
Master What, Where, Who, When, Why, and How for asking and answering questions.

### Module 12: Can/Can't
Use the modal verb CAN to express ability and permission.

### Module 13: This, That, These, Those - Deep Dive
Extended practice with demonstratives for pointing and identifying things.

### Module 14: Like, Love, Hate + -ing
Express preferences and talk about hobbies using verbs with -ing forms.

### Module 15: Past Simple - Was/Were
Learn past tense of "to be" for describing past situations.

### Module 16: Past Simple - Regular Verbs
Form past tense with regular verbs using -ed endings and pronunciation rules.

### Module 17: Past Simple - Irregular Verbs
Master 50+ common irregular past tense verbs for storytelling.

### Module 18: Going To Future
Talk about future plans and predictions using "going to".

### Module 19: Will Future
Use "will" for spontaneous decisions, promises, and predictions.

### Module 20: Adverbs of Frequency - Extended
Master frequency expressions to describe how often you do things.

---

## A2 Level Modules (Elementary)

**Status:** ALL BATCHES COMPLETE ✅ (Batches 1-5, Modules 1-25) - A2 LEVEL COMPLETE

### Module 01: Past Continuous Formation
Master was/were + verb-ing for actions in progress in the past. Learn spelling rules, time expressions, and uses for interrupted actions and story backgrounds.

**Target:** 80 exercises | **Focus:** Enhanced grammar foundation
**Key Topics:** Formation, spelling -ing rules, time expressions, parallel actions, background descriptions

### Module 02: Past Continuous vs Past Simple
Distinguish between completed actions (past simple) and ongoing actions (past continuous). Combine both tenses in complex sentences.

**Target:** 85 exercises | **Focus:** Tense contrast and combination
**Key Topics:** When to use each tense, interrupted actions, sequences vs background, time markers

### Module 03: Past Continuous for Interrupted Actions
Deep dive into using past continuous with past simple for interrupted actions. Master "when" and "while" clauses in storytelling.

**Target:** 80 exercises | **Focus:** Complex sentence structures
**Key Topics:** When/while clauses, interruption patterns, narrative techniques, temporal connections

### Module 04: Present Perfect - Introduction (Life Experiences)
Introduction to have/has + past participle for life experiences. Use with ever/never for asking about experiences.

**Target:** 80 exercises | **Focus:** New tense introduction
**Key Topics:** Formation, past participle forms, life experiences, ever/never, yet/already/just

### Module 05: Present Perfect with Ever/Never
Extended practice with present perfect for experiences. Master question formation with "Have you ever...?" and responses.

**Target:** 80 exercises | **Focus:** Experience questions and discussions
**Key Topics:** Ever/never usage, superlatives with present perfect, experience discussions, interview techniques

### Module 06: Future - Going To vs Will Review
Deep dive into distinguishing between the two main future forms. Learn when to use each based on context and meaning.

**Target:** 85 exercises | **Focus:** Future form mastery
**Key Topics:** Going to for intentions/evidence-based predictions, will for spontaneous decisions/promises, context-based selection

### Module 07: Present Continuous for Future Arrangements
Use present continuous to express fixed future plans and appointments. Distinguish from other future forms.

**Target:** 85 exercises | **Focus:** Definite arrangements
**Key Topics:** Present continuous for future, time markers (essential), meet/see/visit verbs, arrangement vs intention

### Module 08: Future Time Clauses (when, as soon as, until)
Master time clauses with future reference. Learn the crucial rule: present tense in time clause, future in main clause.

**Target:** 82 exercises | **Focus:** Complex future sentences
**Key Topics:** When/as soon as/until/before/after, present simple in time clauses, sequence and timing

### Module 09: Time Sequencing (before, after, then, finally)
Organize events and actions in logical chronological order across all tenses. Build coherent narratives.

**Target:** 83 exercises | **Focus:** Narrative sequencing
**Key Topics:** Before/after conjunctions, then/finally adverbs, chronological flow, tense consistency in sequences

### Module 10: Talking About Duration (for, since)
Distinguish between 'for' (length of time) and 'since' (starting point). Essential for present perfect mastery.

**Target:** 84 exercises | **Focus:** Duration expressions
**Key Topics:** For + time period, since + time point, How long questions, present perfect with for/since

### Module 11: Should/Shouldn't - Advice and Recommendations
Give advice and make recommendations using should/shouldn't. Express opinions about what is right or wrong.

**Target:** 80 exercises | **Focus:** Advice and suggestions
**Key Topics:** Formation with should/shouldn't, giving advice, making recommendations, expressing opinions, should vs must

### Module 12: Must/Have To - Obligation and Necessity
Express rules, requirements, and obligations using must and have to. Understand the difference between internal and external obligations.

**Target:** 85 exercises | **Focus:** Obligations and rules
**Key Topics:** Must vs have to, internal vs external obligation, questions with have to, expressing necessity

### Module 13: Don't Have To vs Mustn't - No Obligation vs Prohibition
Master the critical distinction between 'don't have to' (not necessary) and 'mustn't' (prohibited/not allowed).

**Target:** 82 exercises | **Focus:** Meaning distinction
**Key Topics:** No obligation vs prohibition, don't/doesn't have to, mustn't, context-based usage

### Module 14: May/Might/Could - Possibility and Permission
Express possibility, uncertainty, and ask for permission politely using may, might, and could.

**Target:** 84 exercises | **Focus:** Possibility and permission
**Key Topics:** Expressing possibility, making predictions, asking permission, subtle differences between may/might/could

### Module 15: Would Like - Polite Requests and Preferences
Make polite requests, offers, and express preferences using 'would like' instead of the more direct 'want'.

**Target:** 85 exercises | **Focus:** Polite communication
**Key Topics:** Would like + noun, would like to + verb, contractions, making offers, polite requests

### Module 16: Comparative Adjectives - Formation and Use
Compare two things using comparative adjectives. Master formation rules, spelling changes, and use 'than' correctly.

**Target:** 85 exercises | **Focus:** Comparing two things
**Key Topics:** -er vs more, spelling rules (double consonants, -y to -i), 'than' usage, irregular comparatives (better/worse)

### Module 17: Superlative Adjectives - The Best, The Biggest, The Most
Describe extremes among three or more items using superlative adjectives. Always use 'the' with superlatives.

**Target:** 85 exercises | **Focus:** Describing extremes
**Key Topics:** -est vs most, spelling rules, in/of phrases, irregular superlatives, 'one of the' + superlative

### Module 18: As...As Comparisons - Equality and Inequality
Express that things are the same or different using as...as structures. Learn when to use this vs comparative forms.

**Target:** 82 exercises | **Focus:** Equality comparisons
**Key Topics:** as + adjective + as, not as + adjective + as, as much/many as, common expressions

### Module 19: Adverbs of Manner and Comparison
Describe how actions are performed using adverbs. Learn formation rules and distinguish adverbs from adjectives.

**Target:** 84 exercises | **Focus:** Describing how things happen
**Key Topics:** adjective + -ly, irregular adverbs (well/fast/hard), placement, comparative/superlative adverbs

### Module 20: Intensifiers and Descriptive Language
Add depth and precision to descriptions using intensifiers. Master very, quite, too, and enough.

**Target:** 84 exercises | **Focus:** Degree and intensity
**Key Topics:** very/really/quite, too (excessive), enough (sufficiency), combining with comparatives

---

### Module 21: Zero and First Conditional - If Clauses and Real Possibilities
Express conditions and future possibilities with if-clauses. Master zero conditional for general truths and first conditional for real future possibilities.

**Target:** 85 exercises | **Focus:** Conditionals
**Key Topics:** zero conditional structure, first conditional structure, if + present, avoiding 'will' in if-clause

---

### Module 22: Connectors and Linking Words - Because, So, But, Although
Connect ideas logically with essential connectors. Master cause-result relationships with because/so and contrast with but/although.

**Target:** 84 exercises | **Focus:** Logical connectors
**Key Topics:** because (reason), so (result), but (contrast), although (concession), punctuation rules

---

### Module 23: Relative Clauses - Who, Which, That, Where
Describe and define people, things, and places with relative clauses. Build detailed descriptions using who, which, that, and where.

**Target:** 85 exercises | **Focus:** Relative pronouns
**Key Topics:** who for people, which/that for things, where for places, defining relative clauses

---

### Module 24: Question Formation - Comprehensive Review Across All Tenses
Master question formation across all A2 grammar structures. Review yes/no questions, wh-questions, and subject vs object questions.

**Target:** 82 exercises | **Focus:** All question types
**Key Topics:** yes/no questions, wh-question word order, subject questions, object questions, questions across all tenses

---

### Module 25: A2 Consolidation and Review - Integration and Real-World Communication
Integrate all A2 grammar in authentic communication tasks. Demonstrate mastery across all skills and prepare for B1 transition.

**Target:** 99 exercises | **Focus:** Integration and assessment
**Key Topics:** tense integration, complex sentences, real-world scenarios, A2 self-assessment, B1 preview

---

## Technical Details

### Feedback System

The `feedback_system.py` module provides:
- `ExerciseValidator`: Checks answers with various matching strategies
- `InteractiveExercise`: Creates fill-in-blank, multiple choice, and matching exercises
- `create_progress_bar()`: Visual progress indicators
- `display_hint()`: Collapsible hints for difficult exercises

### Audio Generator

The `audio_generator.py` module provides:
- `AudioGenerator`: Text-to-speech with multiple accents (US, UK, AU, IN)
- `create_pronunciation_card()`: Rich vocab cards with audio
- `create_sentence_audio()`: Audio for example sentences
- `create_conversation_audio()`: Dialogue audio with turn-taking

### Spaced Repetition

The `spaced_repetition.py` module implements:
- **Review intervals:** Day 1, 2, 4, 7, 14, 30, 60, 120
- **Adaptive scheduling:** Adjusts based on performance
- **Progress tracking:** JSON-based storage
- **Visual dashboard:** Shows due and upcoming reviews

## Expanding the Project

### Adding New Modules

Use the `generate_modules.py` script as a template:

1. Define module data in the `MODULES` dictionary
2. Run the script to generate all 4 phase notebooks
3. Manually enhance with detailed exercises and content
4. Test thoroughly before releasing

### Scaling to Full Curriculum

The system is designed to scale to **160 modules** (A1-C2):
- **A1**: 20 modules ✓ COMPLETE (80 notebooks)
- **A2**: 25 modules COMPLETE ✅ (Batch 1: Modules 1-5 ✓ - 20 notebooks | Batch 2: Modules 6-10 ✓ - 20 notebooks | Batch 3: Modules 11-15 ✓ - 20 notebooks | Batch 4: Modules 16-20 ✓ - 20 notebooks | Batch 5: Modules 21-25 ✓ - 20 notebooks)
- **B1**: 30 modules (Planned)
- **B2**: 35 modules (Planned)
- **C1**: 30 modules (Planned)
- **C2**: 20 modules (Planned)

**Current Status:** 180 interactive notebooks created across A1 and A2 levels (45/160 modules = 28%) - A2 COMPLETE ✅

See `English-Path.md` for the complete curriculum specification.

## Research Foundation

This project is based on:

- **Cambridge English Grammar Profile** (55 million word corpus analysis)
- **CEFR** (Common European Framework of Reference)
- **Global Scale of English** (Pearson)
- **Applied Linguistics Research** (Rod Ellis, Michael Long, etc.)
- **Cognitive Science** (spaced repetition, retrieval practice)

Key findings implemented:
- Explicit instruction has highest effect size (d=1.26)
- Spaced repetition increases retention by 200%
- Developmental sequences must be respected
- Practice should progress from controlled → communicative
- Feedback should be immediate for accuracy, delayed for fluency

## Contributing

Contributions welcome! Areas for improvement:

- **More exercises:** Each module could have 50+ exercises
- **Better audio:** Professional voice recordings
- **Gamification:** Points, badges, leaderboards
- **Adaptive difficulty:** Adjust based on performance
- **Mobile support:** Responsive design for smartphones
- **Additional modules:** Expand to A2, B1, B2, C1, C2
- **Video content:** Grammar explanations with animations
- **Community features:** Study groups, forums, peer review

## Future Enhancements

- [ ] Web-based interface (Streamlit/Dash)
- [ ] Database backend (SQLite/PostgreSQL)
- [ ] User authentication
- [ ] Cloud deployment
- [ ] Mobile app version
- [ ] Integration with language exchange platforms
- [ ] AI-powered feedback (LLM integration)
- [ ] Speech recognition for pronunciation practice
- [ ] Automated exercise generation
- [ ] Personalized learning paths

## License

MIT License - feel free to use, modify, and distribute.

## Acknowledgments

- **Cambridge University Press** for Grammar Profile research
- **Foreign Service Institute** for language learning timelines
- **Rod Ellis** for Focus on Form methodology
- **Michael Long** for Task-Based Language Teaching
- **Pienemann** for Processability Theory

## Author

Created as a portfolio project demonstrating:
- Educational technology development
- Jupyter notebook expertise
- Python programming
- Data visualization
- UX/UI design for learning
- Research-backed curriculum design

## Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub.

---

**Happy Learning!** 🚀📚

*This pilot project demonstrates a scalable, research-backed approach to language learning. With proper expansion, it could become a complete English learning platform covering all proficiency levels.*
