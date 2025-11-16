---
skill_name: language-learning-educator
description: Domain expertise for teaching English language learning with audio, exercises, and progressive difficulty
version: 1.0.0
author: Educational Notebook System
tags: [language-learning, english, ESL, audio, exercises, CEFR, education]
activation_keywords: [english learning, language, ESL, CEFR, grammar, vocabulary, pronunciation, audio]
dependencies: [gtts, pyttsx3, soundfile, pandas]
---

# Language Learning Educator Skill

## Purpose

Provides domain expertise for creating educational content for English language learning, following CEFR standards with audio generation, interactive exercises, and progressive difficulty.

## CEFR Levels Overview

### A1 (Beginner)
- **Can Do**: Introduce self, ask/answer basic questions, simple phrases
- **Grammar**: Present simple, basic pronouns, singular/plural
- **Vocabulary**: ~500 words (everyday topics)
- **Sentence Length**: 3-7 words

### A2 (Elementary)
- **Can Do**: Describe background, immediate needs, simple exchanges
- **Grammar**: Past simple, future with "going to", comparatives
- **Vocabulary**: ~1000 words (routine activities)
- **Sentence Length**: 5-10 words

### B1 (Intermediate)
- **Can Do**: Handle travel situations, describe experiences, explain opinions
- **Grammar**: Present perfect, conditionals, modal verbs
- **Vocabulary**: ~2000 words (familiar topics)
- **Sentence Length**: 8-15 words

### B2 (Upper Intermediate)
- **Can Do**: Interact fluently, understand complex texts, argue viewpoints
- **Grammar**: Passive voice, reported speech, advanced tenses
- **Vocabulary**: ~4000 words (abstract topics)
- **Sentence Length**: 12-20 words

## Teaching Patterns

### Pattern 1: Vocabulary Introduction

```markdown
## Vocabulary: [Topic]

### New Words

| Word | Part of Speech | Pronunciation | Definition | Example |
|------|----------------|---------------|------------|---------|
| example | noun | /ɪɡˈzæmpəl/ | A thing characteristic of its kind | This is an *example* of good writing. |

### Audio Practice
```python
from gtts import gTTS
import IPython.display as ipd

def create_audio(text, lang='en'):
    \"\"\"Generate and play audio for vocabulary\"\"\"
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save('temp_audio.mp3')
    return ipd.Audio('temp_audio.mp3', autoplay=False)

# Listen to each word
for word in vocabulary_list:
    print(f"🔊 {word}")
    display(create_audio(word))
```

### Comprehension Check
1. Match words to definitions
2. Fill in the blanks
3. Create your own sentence
```

### Pattern 2: Grammar Module

```markdown
## Grammar: [Structure Name]

### Form
**Positive**: [Subject] + [Verb form] + [Object]
**Negative**: [Subject] + don't/doesn't + [Verb] + [Object]
**Question**: Do/Does + [Subject] + [Verb] + [Object]?

### Examples
✅ **Correct**:
- She *studies* English every day.
- They *don't* speak French.
- *Do* you *like* pizza?

❌ **Common Mistakes**:
- ~~She study English~~ → She *studies* English (add -s for third person)
- ~~She doesn't studies~~ → She doesn't *study* (don't add -s after doesn't)

### Practice Exercises

#### Exercise 1: Fill in the Gaps
Complete the sentences with the correct form:

1. He _____ (work) in a bank.
2. They _____ (not/have) a car.
3. _____ she _____ (speak) Spanish?

#### Exercise 2: Correction
Find and fix the errors:

1. She don't like coffee. → ___________
2. Does they live here? → ___________

#### Exercise 3: Create Sentences
Write 3 sentences using this grammar structure about your daily routine.
```

### Pattern 3: Listening Comprehension

```markdown
## Listening: [Topic Title]

### Pre-Listening
**Warm-up Question**: [Activate prior knowledge]

**Vocabulary to Know**:
- [Word 1]: [Definition]
- [Word 2]: [Definition]

### Listen

```python
# Generate listening passage
passage = \"\"\"
[Appropriate-level text with target grammar/vocabulary]
\"\"\"

display(create_audio(passage))
```

**Listen once**: Get the general idea
**Listen again**: Answer the questions below

### Questions

**General Understanding**:
1. What is the main topic?
2. Who are the speakers?

**Specific Details**:
3. [Specific fact question]
4. [Inference question]

**Vocabulary in Context**:
5. What does "[word]" mean in this context?

### Answers
[Provide answers for self-checking or in instructor version]
```

### Pattern 4: Speaking Practice

```markdown
## Speaking: [Activity Name]

### Preparation
**Topic**: [Topic]
**Key phrases to use**:
- [Phrase 1]
- [Phrase 2]
- [Phrase 3]

### Task
[Clear speaking task description]

### Model Example

```python
# Listen to example first
model_response = "[Example response at appropriate level]"
display(create_audio(model_response))
```

### Your Turn
1. Prepare your response (write notes below)
2. Practice saying it aloud
3. Record yourself (optional)
4. Compare to model example

### Self-Assessment
- [ ] Did I use the key phrases?
- [ ] Was my pronunciation clear?
- [ ] Did I speak for the target time?
- [ ] Did I answer completely?
```

## Audio Generation Best Practices

### Using gTTS (Google Text-to-Speech)

```python
from gtts import gTTS
import IPython.display as ipd
from pathlib import Path

def generate_audio_example(text, filename='audio', slow=False, lang='en'):
    \"\"\"
    Generate audio file for language learning.

    Parameters
    ----------
    text : str
        Text to convert to speech
    filename : str
        Output filename (without extension)
    slow : bool
        If True, speaks slower for beginners
    lang : str
        Language code ('en' for English)

    Returns
    -------
    IPython.display.Audio
        Audio player widget
    \"\"\"
    # Create audio object
    tts = gTTS(text=text, lang=lang, slow=slow)

    # Save to file
    output_path = f'audio/{filename}.mp3'
    Path('audio').mkdir(exist_ok=True)
    tts.save(output_path)

    # Return audio player
    return ipd.Audio(output_path, autoplay=False)

# Usage examples

# Normal speed for B1+ levels
audio_normal = generate_audio_example(
    "This is an example sentence.",
    filename="example_normal",
    slow=False
)
display(audio_normal)

# Slow speed for A1-A2 levels
audio_slow = generate_audio_example(
    "This is an example sentence.",
    filename="example_slow",
    slow=True
)
display(audio_slow)
```

### Creating Vocabulary Audio Lists

```python
def create_vocabulary_audio(vocabulary_dict):
    \"\"\"
    Create audio for vocabulary list.

    Parameters
    ----------
    vocabulary_dict : dict
        {word: definition} pairs

    Returns
    -------
    list
        Audio player objects
    \"\"\"
    audio_files = []

    for word, definition in vocabulary_dict.items():
        # Create audio for word
        word_audio = generate_audio_example(word, f'vocab_{word}')

        # Create audio for example sentence with word
        sentence = f"Example: {definition}"
        sentence_audio = generate_audio_example(sentence, f'example_{word}')

        audio_files.append({
            'word': word,
            'word_audio': word_audio,
            'sentence_audio': sentence_audio
        })

    return audio_files
```

## Exercise Types by Level

### A1 Exercises
1. **Picture Matching**: Match words to images
2. **Multiple Choice**: Choose correct word/form
3. **Fill in the Blank**: Complete with provided words
4. **True/False**: Simple comprehension
5. **Matching**: Connect related items
6. **Simple Substitution**: Replace words in sentences

### A2 Exercises
1. **Short Gap Fills**: Complete with correct form
2. **Sentence Reordering**: Put words in correct order
3. **Error Correction**: Find and fix mistakes
4. **Simple Transformations**: Change tense/form
5. **Dialogue Completion**: Fill missing responses
6. **Short Answer Questions**: 1-2 sentence responses

### B1 Exercises
1. **Extended Gap Fills**: Multiple words missing
2. **Paraphrasing**: Rewrite with same meaning
3. **Sentence Combining**: Join using conjunctions
4. **Controlled Writing**: Write using prompts
5. **Comprehension Questions**: Detailed answers
6. **Role Play Scenarios**: Interactive tasks

### B2 Exercises
1. **Essay Writing**: Structured compositions
2. **Debate Preparation**: Argue both sides
3. **Summary Writing**: Condense longer texts
4. **Critical Analysis**: Evaluate arguments
5. **Formal vs Informal**: Register transformation
6. **Idiomatic Expressions**: Natural language use

## Progress Tracking

### Module Completion Checklist

```markdown
## Progress Tracker

### Module [X]: [Topic]

**Completion Status**:
- [ ] Vocabulary learned (___/20 words)
- [ ] Grammar exercises (___/10 completed)
- [ ] Listening comprehension (___% correct)
- [ ] Speaking practice (completed: Y/N)
- [ ] Writing assignment (completed: Y/N)

**Self-Assessment**:
- I can [learning objective 1]: ⭐⭐⭐⭐⭐
- I can [learning objective 2]: ⭐⭐⭐⭐⭐
- I can [learning objective 3]: ⭐⭐⭐⭐⭐

**Notes**: [Personal observations, difficult points, questions]

**Next Steps**: Review [specific areas] before moving to Module [X+1]
```

### Batch Organization

For multi-module courses (like your A1, A2, B1 batches):

```python
# Batch metadata
batch_info = {
    'batch_name': 'A2 Batch 1',
    'modules': [1, 2, 3, 4, 5],
    'focus_areas': ['Present Simple', 'Daily Routines', 'Question Formation'],
    'estimated_hours': 10,
    'prerequisites': ['A1 Complete'],
    'learning_outcomes': [
        'Can describe daily routines',
        'Can ask and answer about habits',
        'Can use present simple confidently'
    ]
}
```

## Common Learner Errors to Address

### Grammar Errors
1. **Third Person -s**: *He work* → He works
2. **Article Usage**: *I am teacher* → I am a teacher
3. **Word Order**: *I like very much pizza* → I like pizza very much
4. **Tense Consistency**: Mixed tenses in narration
5. **Preposition Choice**: *Interested about* → Interested in

### Pronunciation Challenges
1. **TH sounds**: /θ/ (think) vs /ð/ (this)
2. **Vowel length**: ship /ɪ/ vs sheep /iː/
3. **Silent letters**: knight, climb, psychology
4. **Word stress**: PHOtograph vs phoTOGraphy
5. **Sentence stress**: Content vs function words

### Vocabulary Issues
1. **False friends**: *Embarrassed* vs *pregnant* (for Spanish speakers)
2. **Overuse of cognates**: Assuming similarity means same usage
3. **Literal translation**: Idioms from native language
4. **Register confusion**: Formal vs informal context

## Cultural Notes Integration

Include cultural context for authentic communication:

```markdown
## Cultural Note: [Topic]

### In English-speaking countries...
[Cultural practice/norm related to language use]

### Language Tips:
- In formal situations, use: [formal version]
- With friends, you can say: [informal version]
- Avoid: [what not to say and why]

### Example Situations:
[Real-world scenarios showing appropriate language use]
```

## Assessment Design

### Formative Assessment (During Learning)
- Quick comprehension checks after each section
- Self-assessment rubrics
- Error identification exercises
- Peer review activities

### Summative Assessment (End of Module)
- Comprehensive vocabulary test
- Grammar application tasks
- Listening comprehension passage
- Speaking prompt (record and submit)
- Writing composition

### Auto-Grading Where Possible

```python
def check_answer(user_answer, correct_answer, partial_credit=True):
    \"\"\"
    Check student answer with feedback.

    Parameters
    ----------
    user_answer : str
        Student's response
    correct_answer : str or list
        Correct answer(s)
    partial_credit : bool
        Allow partial credit for close answers

    Returns
    -------
    dict
        Score, feedback, and correctness
    \"\"\"
    user_clean = user_answer.lower().strip()

    # Handle multiple correct answers
    if isinstance(correct_answer, list):
        correct_answers = [ans.lower().strip() for ans in correct_answer]
    else:
        correct_answers = [correct_answer.lower().strip()]

    # Check for exact match
    if user_clean in correct_answers:
        return {
            'correct': True,
            'score': 1.0,
            'feedback': '✅ Correct!'
        }

    # Check for partial credit (minor spelling errors)
    if partial_credit:
        from difflib import SequenceMatcher
        for correct in correct_answers:
            similarity = SequenceMatcher(None, user_clean, correct).ratio()
            if similarity > 0.85:
                return {
                    'correct': 'partial',
                    'score': 0.5,
                    'feedback': f'⚠️  Close! Check your spelling. The answer is: {correct}'
                }

    return {
        'correct': False,
        'score': 0.0,
        'feedback': f'❌ Not quite. The correct answer is: {correct_answers[0]}'
    }
```

## Success Criteria

Language learning educational content should:
- ✅ Follow CEFR guidelines for level
- ✅ Include audio for all examples (pronunciation critical)
- ✅ Provide immediate feedback on exercises
- ✅ Progress logically from simple to complex
- ✅ Use authentic, natural language examples
- ✅ Address common learner errors explicitly
- ✅ Include cultural context where relevant
- ✅ Offer varied exercise types (reading, listening, writing, speaking)
- ✅ Enable self-paced learning with clear objectives
- ✅ Track progress and celebrate milestones
