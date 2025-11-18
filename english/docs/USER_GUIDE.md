# English Learning Curriculum - User Guide

**Complete guide to navigating and using the 335-notebook English learning curriculum**

*Last Updated: November 18, 2025*

---

## 📚 Table of Contents

1. [Getting Started](#getting-started)
2. [Understanding the Structure](#understanding-the-structure)
3. [How to Use the Notebooks](#how-to-use-the-notebooks)
4. [Learning Pathways](#learning-pathways)
5. [AI Tools Integration](#ai-tools-integration)
6. [Progress Tracking](#progress-tracking)
7. [Study Tips & Best Practices](#study-tips--best-practices)
8. [Troubleshooting](#troubleshooting)
9. [FAQ](#faq)

---

## Getting Started

### Prerequisites

**Technical Requirements:**
- Python 3.8+ installed
- Jupyter Notebook or JupyterLab
- Internet connection (for AI tools)
- Microphone (for speaking practice)
- Headphones (recommended for listening practice)

**Installation:**
```bash
# Install required packages
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### First Steps

1. **Assess Your Level** (`00_START_HERE/skill_assessment.ipynb`)
   - Take the CEFR self-assessment
   - Complete EF SET test (free, 50 minutes)
   - Record your baseline scores
   - Set realistic goals

2. **Plan Your Schedule** (`00_START_HERE/daily_schedule.ipynb`)
   - Review the 12-hour/week template
   - Customize for your lifestyle
   - Start tracking practice time

3. **Set Up AI Tools** (`resources/tools_guide.md`)
   - Create ChatGPT account (free)
   - Install Gliglish app (speaking)
   - Set up Grammarly (writing)
   - Download ELSA Speak (pronunciation)

4. **Start Learning!**
   - Go to your level folder (A1, A2, B1, B2, C1, or C2)
   - Choose a skill (writing, speaking, listening, or reading)
   - Open notebook 01

---

## Understanding the Structure

### Curriculum Organization

The curriculum is organized by **CEFR level** first, then by **skill**:

```
english/
├── A1/ (Beginner)          40 notebooks
├── A2/ (Elementary)        48 notebooks
├── B1/ (Intermediate)      60 notebooks
├── B2/ (Upper-Intermediate) 80 notebooks
├── C1/ (Advanced)          60 notebooks
└── C2/ (Proficient)        40 notebooks
```

Each level contains 4 skill folders:
- **writing/** - Written communication
- **speaking/** - Oral communication
- **listening/** - Audio comprehension
- **reading/** - Text comprehension

### CEFR Levels Explained

| Level | Name | Description | Time to Complete |
|-------|------|-------------|------------------|
| **A1** | Beginner | Absolute basics (alphabet, greetings, numbers) | 2-4 months |
| **A2** | Elementary | Simple everyday situations (shopping, family) | 3-5 months |
| **B1** | Intermediate | Work, travel, personal topics | 4-6 months |
| **B2** | Upper-Intermediate | Professional, complex topics | 5-8 months |
| **C1** | Advanced | Sophisticated, professional/academic | 6-10 months |
| **C2** | Proficient/Mastery | Native-equivalent proficiency | 6-12 months |

**Total pathway time**: 12-24 months (varies by study intensity)

### Notebook Numbering

Notebooks are numbered sequentially within each skill:
- `01_topic_name.ipynb` - First module
- `02_topic_name.ipynb` - Second module
- ...
- `10_assessment.ipynb` (or 12, 15, 20) - Final assessment

**Complete notebooks in order** for best results.

---

## How to Use the Notebooks

### Notebook Structure

Every notebook follows this consistent format:

#### 1. **Header Section**
```
# [Level] [Skill] [Number]: [Topic]
Difficulty: ⭐⭐
Time: 45 minutes
Prerequisites: Previous modules
```

#### 2. **Learning Objectives**
Clear, measurable goals for the session:
- "By the end of this notebook, you will be able to..."
- 3-6 specific objectives per notebook

#### 3. **Content Sections**
- **Introduction**: Why this topic matters
- **Core Content**: Main teaching material
- **Examples**: Real-world demonstrations
- **Explanation**: How and why it works

#### 4. **AI Practice**
- ChatGPT/Claude prompts ready to copy-paste
- Gliglish conversation starters (speaking)
- Tool-specific exercises

#### 5. **Exercises**
- Practice tasks (3-5 per notebook)
- Self-assessment questions
- Real-world applications

#### 6. **Summary**
- Key takeaways
- What you learned
- Next steps

### How to Work Through a Notebook

**Step 1: Read the Objectives** (2 min)
- Know what you're aiming to achieve
- Keep objectives in mind throughout

**Step 2: Study the Content** (15-25 min)
- Read carefully, don't rush
- Run code cells to see examples
- Take notes on new concepts

**Step 3: Practice with AI** (15-25 min)
- Copy the provided prompts
- Use ChatGPT/Claude for feedback
- Try Gliglish for speaking practice
- Get real-time corrections

**Step 4: Complete Exercises** (10-15 min)
- Do all practice tasks
- Check your understanding
- Review difficult parts

**Step 5: Review Summary** (3-5 min)
- Confirm you met objectives
- Note what to practice more
- Prepare for next module

### Difficulty Indicators

- ⭐ = Beginner (A1-A2)
- ⭐⭐ = Intermediate (B1)
- ⭐⭐⭐ = Upper-Intermediate/Advanced (B2-C1)
- ⭐⭐⭐⭐ = Mastery (C2)

---

## Learning Pathways

### Pathway 1: Complete Beginner to Mastery
**A1 → A2 → B1 → B2 → C1 → C2** (335 notebooks)

**For**: Absolute beginners or those starting from scratch
**Timeline**: 12-24 months
**Study Intensity**: 12-20 hours/week

**Suggested Schedule**:
- A1: Months 1-3 (40 notebooks)
- A2: Months 4-7 (48 notebooks)
- B1: Months 8-12 (60 notebooks)
- B2: Months 13-18 (80 notebooks)
- C1: Months 19-23 (60 notebooks)
- C2: Months 24+ (40 notebooks)

### Pathway 2: Elementary to Advanced
**A2 → B1 → B2 → C1** (248 notebooks)

**For**: Learners with basic English (can introduce themselves, order food)
**Timeline**: 9-18 months
**Study Intensity**: 12-18 hours/week

### Pathway 3: Intermediate to Proficient
**B1 → B2 → C1 → C2** (240 notebooks)

**For**: Intermediate learners (can discuss work, travel, opinions)
**Timeline**: 9-18 months
**Study Intensity**: 10-15 hours/week

### Pathway 4: Upper-Intermediate to Mastery
**B2 → C1 → C2** (180 notebooks)

**For**: Advanced learners seeking native-level proficiency
**Timeline**: 6-12 months
**Study Intensity**: 10-15 hours/week

### Custom Pathway: Skill-Focused

**Focus on One Skill Across Levels**:
- Complete all Writing notebooks (A1→C2): 82 notebooks
- Complete all Speaking notebooks (A1→C2): 82 notebooks
- Complete all Listening notebooks (A1→C2): 82 notebooks
- Complete all Reading notebooks (A1→C2): 82 notebooks

**For**: Learners who need to rapidly improve one specific skill
**Timeline**: 3-6 months per skill

---

## AI Tools Integration

### ChatGPT / Claude (Writing & General Practice)

**How to Use**:
1. Copy the provided prompt from notebook
2. Paste into ChatGPT or Claude
3. Attach your writing or questions
4. Get detailed feedback

**Example Prompt** (from B2 Writing):
```
I'm practicing business email writing at B2 level. Please review my email for:
1. Formal register appropriateness
2. Structure and organization
3. Grammar and vocabulary
4. Professional tone

[Paste your email here]
```

### Gliglish AI (Speaking Practice)

**Setup**:
1. Download app (iOS/Android)
2. Select your level (A1-C2)
3. Choose conversation topic
4. Start speaking!

**Tips**:
- Use daily for 10-15 minutes
- Focus on fluency, not perfection
- Record yourself to track progress
- Try different scenarios weekly

### ELSA Speak (Pronunciation)

**How to Use**:
1. Complete daily lessons (10 min)
2. Focus on problem sounds
3. Track accuracy scores
4. Practice minimal pairs

**Integration with Notebooks**:
- Speaking notebooks reference specific sounds
- Practice exercises aligned with ELSA content

### Grammarly (Writing Feedback)

**Setup**:
1. Install browser extension
2. Enable for all writing
3. Review suggestions carefully
4. Learn from corrections

**Use for**:
- Email practice
- Essay writing
- Business documents
- Academic writing

---

## Progress Tracking

### Tracking Your Progress

**Create a Learning Log**:
```python
# In a new notebook
import pandas as pd
from datetime import datetime

progress_log = {
    'date': [],
    'level': [],
    'skill': [],
    'notebook': [],
    'time_spent': [],
    'completed': [],
    'notes': []
}

# After each session
progress_log['date'].append(datetime.now().strftime('%Y-%m-%d'))
progress_log['level'].append('B2')
progress_log['skill'].append('writing')
progress_log['notebook'].append('01_passive_voice')
progress_log['time_spent'].append(45)  # minutes
progress_log['completed'].append(True)
progress_log['notes'].append('Need more practice with complex sentences')

# Save
df = pd.DataFrame(progress_log)
df.to_csv('my_progress.csv', index=False)
```

### Milestones to Celebrate

**Level Completion**:
- ✅ Complete all 4 skills at one level
- 🎉 Take end-of-level assessment
- 📊 Compare with baseline scores
- 🎯 Set goals for next level

**Skill Mastery**:
- Complete one skill across all levels (82 notebooks)
- Professional achievement (e.g., give presentation in English)
- Pass official exam (IELTS, TOEFL, Cambridge)

### Weekly Review

**Every Sunday** (30 minutes):
1. Review notebooks completed
2. Note difficult areas
3. Plan next week's focus
4. Update progress tracker
5. Celebrate wins!

---

## Study Tips & Best Practices

### Effective Study Habits

**1. Consistency Over Intensity**
- Study 1-2 hours daily > 10 hours once/week
- Build habit: same time, same place
- Small daily progress compounds

**2. Active Learning**
- Don't just read—practice!
- Use AI tools immediately
- Create real examples
- Teach concepts to others

**3. Spaced Repetition**
- Review previous notebooks weekly
- Revisit difficult concepts
- Use flashcards for vocabulary
- Test yourself regularly

**4. Real-World Application**
- Use English in daily life
- Join online communities
- Watch movies/shows
- Read news in English

### Time Management

**12-Hour/Week Schedule** (Recommended Minimum):

| Day | Time | Activity |
|-----|------|----------|
| Mon | 90 min | Writing notebook + practice |
| Tue | 90 min | Speaking practice (Gliglish) |
| Wed | 90 min | Listening notebook + podcasts |
| Thu | 90 min | Reading notebook + articles |
| Fri | 90 min | Writing + speaking review |
| Sat | 120 min | Mixed practice + AI conversations |
| Sun | 90 min | Weekly review + planning |

**Total**: 12 hours/week = 600 hours/year = Significant progress!

### Overcoming Plateaus

**When Progress Feels Slow**:
1. Review your baseline assessment
2. Test yourself—you've improved!
3. Try harder materials briefly
4. Change learning environment
5. Find a study partner
6. Take a short break (2-3 days)

---

## Troubleshooting

### Common Issues

**Problem**: "Notebooks won't run"
**Solution**:
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Restart Jupyter kernel
# Kernel → Restart & Clear Output
```

**Problem**: "Content too easy/hard"
**Solution**:
- Retake level assessment
- Jump up/down one level
- Focus on weaker skills first

**Problem**: "No time for 12 hours/week"
**Solution**:
- Start with 6 hours/week minimum
- Focus on one skill at a time
- Use micro-learning (15-min sessions)
- Listen to podcasts during commute

**Problem**: "Lost motivation"
**Solution**:
- Set concrete, short-term goals
- Join online English learning community
- Track progress visually
- Reward yourself for milestones
- Remember why you started

### Getting Help

**Resources**:
- Review `resources/` guides
- Check `docs/FAQ.md`
- Use AI tutors (ChatGPT/Claude)
- Online English learning forums

---

## FAQ

**Q: How long will it take to complete everything?**
A: 12-24 months if studying 12-20 hours/week. Varies by starting level and intensity.

**Q: Can I skip levels?**
A: Not recommended. Each level builds on the previous. Take the assessment first.

**Q: Do I need to finish one skill before starting another?**
A: No! Mix skills for variety. But complete notebooks in order within each skill.

**Q: Are the AI tools really free?**
A: ChatGPT (free tier), Gliglish (free with limits), Grammarly (free basic). Paid options available.

**Q: Can I use this for exam prep (IELTS/TOEFL)?**
A: Yes! B2-C1 levels align well with exam requirements. Add past papers for practice.

**Q: What if I don't have 12 hours/week?**
A: Start with 6 hours minimum. Progress will be slower but steady.

**Q: Should I complete one level before moving to the next?**
A: Yes, for best results. Complete all 4 skills at one level before advancing.

**Q: How do I know when I'm ready for the next level?**
A: Complete the assessment notebook (last in each skill). Aim for 80%+ accuracy.

---

## Next Steps

1. ✅ **Complete** `00_START_HERE/skill_assessment.ipynb`
2. ✅ **Set up** AI tools from `resources/tools_guide.md`
3. ✅ **Start** your first notebook at your level
4. ✅ **Track** progress in a learning log
5. ✅ **Review** this guide as needed

**Happy Learning!** 🎓📚

---

*For more help, see:*
- `QUICK_START_GUIDE.md` - Get started in 30 minutes
- `resources/tools_guide.md` - AI tool setup
- `IMPLEMENTATION_STATUS.md` - Complete curriculum details
