# Parallel Processing Assignment - Complete Guide

**Course**: BMCS2103 Distributed Systems and Parallel Computing
**Total Weight**: 60% of coursework
**Group Size**: 2-3 members

---

## 📚 Assignment Structure

**Part A: Proposal** (40% of assignment)
- Deliverable: 5-10 page proposal
- Deadline: Week 3-4 (Long Semester)
- Grading: Introduction (30) + Literature (30) + Methodology (30) + References (10) = 100 marks

**Part B: Implementation & Report** (60% of assignment)
- Deliverables: 8-20 page report, source code, demo presentation
- Deadline: Week 11-13 (Long Semester)
- Grading: Program (60%) + Report (40%) = 100 marks

---

## 📖 Complete Notebook Series (12 Notebooks)

### 🔧 Setup & Planning (Week 1-2)

| # | Notebook | Purpose | Time |
|---|----------|---------|------|
| 00 | `00_assignment_overview.ipynb` | Requirements, timeline, setup | 30 min |
| 01 | `01_problem_selection.ipynb` | Choose problem, analyze parallelization | 2-3 hrs |

---

### 📝 Part A: Proposal Writing (Week 2-4)

| # | Notebook | Purpose | Time |
|---|----------|---------|------|
| 02 | `02_literature_review.ipynb` | Research papers, cite sources | 4-6 hrs |
| 03 | `03_methodology_design.ipynb` | Design parallel approach | 3-4 hrs |
| 04 | `04_proposal_writing.ipynb` | Compile proposal document | 3-4 hrs |

**Deliverable**: Submit Part A (Week 3-4)

---

### 💻 Part B: Implementation (Week 5-10)

| # | Notebook | Purpose | Time |
|---|----------|---------|------|
| 05 | `05_serial_implementation.ipynb` | Baseline code + profiling | 4-6 hrs |
| 06 | `06_openmp_parallel.ipynb` | Multi-core with OpenMP/Python | 6-8 hrs |
| 07 | `07_cuda_gpu_acceleration.ipynb` | GPU with CUDA/Numba (optional) | 6-8 hrs |
| 08 | `08_performance_benchmarking.ipynb` | Comprehensive testing | 3-4 hrs |
| 09 | `09_optimization_techniques.ipynb` | Improve performance | 4-6 hrs |

---

### 📊 Part B: Final Report & Presentation (Week 10-13)

| # | Notebook | Purpose | Time |
|---|----------|---------|------|
| 10 | `10_final_report_writing.ipynb` | 8-20 page final report | 5-7 hrs |
| 11 | `11_presentation_preparation.ipynb` | Demo + Q&A preparation | 3-4 hrs |

**Deliverables**: Submit Part B (Week 11), Present (Week 12-13)

---

## 🚀 Quick Start Guide

### First Time? Start Here!

1. **Read**: `00_assignment_overview.ipynb`
   - Understand requirements and grading
   - Check your Python environment
   - Review timeline

2. **Form Team**: 2-3 members
   - Discuss problem interests
   - Assign initial roles

3. **Choose Problem**: `01_problem_selection.ipynb`
   - Review suggested domains (Image Processing, Matrix Ops, Monte Carlo, etc.)
   - Analyze parallelization potential
   - Verify uniqueness with tutor

4. **Follow Sequence**: Notebooks 02 → 11
   - Each builds on previous work
   - Complete all exercises
   - Use provided templates

---

## 🎯 Recommended Problems

### ⭐⭐⭐ Best for Excellence

1. **Image Processing Pipeline**
   - Multiple filters (blur, edge detection, sharpening)
   - Perfect for GPU (massive parallelism)
   - Visual results (impressive)
   - Easy speedup measurement

2. **Matrix Operations Suite**
   - Multiplication + solving linear systems
   - Multiple parallel strategies
   - Clear performance metrics
   - Educational value

3. **K-Means Clustering**
   - Practical ML application
   - Iterative parallelism
   - Visualizable results
   - Real datasets

### ⭐⭐ Good Options

4. **Monte Carlo Simulations** - Embarrassingly parallel (beginner-friendly)
5. **N-Body Simulation** - Advanced, scientifically interesting

---

## 🛠️ Technical Setup

### Required Libraries

```bash
# Core libraries
pip install numpy matplotlib pandas

# Parallelization
pip install numba  # GPU + JIT compilation

# Optional (recommended)
pip install python-docx seaborn scipy
```

### Hardware

**Minimum**: Multi-core CPU (4+ cores), 8GB RAM, Python 3.7+

**Recommended**: NVIDIA GPU with CUDA (for excellent grades)

**No GPU?** Focus on CPU parallelization - still get excellent grades! Use Google Colab for GPU testing.

---

## 📋 Submission Checklists

### Part A Checklist (Week 3-4)
- [ ] 5-10 pages, Times New Roman 11pt
- [ ] Cover page (Appendix 1)
- [ ] Introduction + problem statement
- [ ] Literature review (5+ academic papers)
- [ ] Methodology with diagrams
- [ ] Task allocation table
- [ ] Harvard-style references
- [ ] Rubric (Appendix 2)
- [ ] Submit to Google Classroom

### Part B Checklist (Week 11)
- [ ] 8-20 pages report
- [ ] Title and abstract
- [ ] Results with tables/graphs
- [ ] Discussion + conclusion
- [ ] Complete source code (commented)
- [ ] README for running code
- [ ] Rubric (Appendix 3)
- [ ] Submit to Google Classroom

### Presentation Checklist (Week 12-13)
- [ ] 10-15 minute presentation
- [ ] Working demo
- [ ] Backup plan (screenshots/video)
- [ ] All members participate
- [ ] Q&A preparation

---

## 💡 Keys to Excellence (80-100%)

To achieve **Excellent** grade:

1. ✅ **Creative ideas** - Unique approach or combination
2. ✅ **Learn new skills** - Beyond course materials
3. ✅ **Multiple parallel models** - SPMD + loop + task parallelism
4. ✅ **Measurable optimization** - Show performance improvements
5. ✅ **Test multiple platforms** - OpenMP (CPU) AND CUDA (GPU)
6. ✅ **Excellent documentation** - Clear, well-written, working prototype
7. ✅ **Comprehensive testing** - Statistical rigor, multiple test cases
8. ✅ **Critical analysis** - Compare with literature, discuss limitations

---

## ⚠️ Common Pitfalls

1. ❌ Starting too late (start Week 1!)
2. ❌ Not verifying uniqueness with tutor
3. ❌ Using only websites (need academic papers)
4. ❌ No serial baseline (always profile first)
5. ❌ Not verifying correctness
6. ❌ Single test case (test multiple sizes)
7. ❌ No statistical analysis (run multiple times)
8. ❌ Poor documentation
9. ❌ No demo practice
10. ❌ **PLAGIARISM** - All work must be original!

---

## 📚 Supporting Documents

Located in this folder:
- `Assignment Question.docx` - Official instructions
- `Assignment Appendix 1 - Cover Page.docx` - Cover page template
- `Assignment Appendix 2 - Assessment Rubric (Part A).docx` - Proposal rubric
- `Assignment Appendix 3 - Assessment Rubric (Part B).docx` - Implementation rubric

---

## 📊 Detailed Grading Breakdown

### Part A: Proposal (40 marks → 40% of assignment)

| Criterion | Marks | What's Assessed |
|-----------|-------|-----------------|
| Introduction | 30 | Problem discussion, project uniqueness, system evaluation |
| Literature Review | 30 | Quality of sources, critical evaluation, paraphrasing |
| Methodology | 30 | System design, algorithm choice, explanation clarity |
| References | 10 | Harvard style, quality of sources, proper citations |

### Part B: Implementation (60 marks → 60% of assignment)

**Program Assessment (60%)**:

| Criterion | Marks | What's Assessed |
|-----------|-------|-----------------|
| Output | 10 | Information generated, accuracy, visualization quality |
| Programming | 10 | Logic, exception handling, algorithm complexity |
| Completion | 10 | Required features, bug-free demonstration |
| Optimization | 10 | Multiple parallel models, platform testing (OpenMP+CUDA) |
| Implementation | 10 | Conforms to proposed design |
| Presentation | 10 | Understanding of code, demo clarity |

**Final Report (40%)**:

| Criterion | Marks | What's Assessed |
|-----------|-------|-----------------|
| Title & Abstract | 10 | Informative, succinct, complete details |
| Results | 10 | Performance metrics, analytical methods, measurements |
| Discussion | 10 | Significance, limitations, future improvements |
| Organization | 5 | Structure, transitions, flow |
| Writing | 5 | Grammar, spelling, clarity |

---

## 📅 Suggested Timeline (Long Semester - 13 weeks)

| Week | Milestone | Activities | Deliverable |
|------|-----------|------------|-------------|
| 1 | Setup | Form team, review requirements | - |
| 2 | Problem selection | Choose problem, verify uniqueness | - |
| 3 | Research | Literature review, citations | - |
| 3-4 | Methodology | Design approach, diagrams | - |
| 4 | **Part A DUE** | Submit proposal | **Proposal** |
| 5-6 | Serial code | Implement baseline, profile | - |
| 7-8 | Parallel CPU | OpenMP/multiprocessing | - |
| 8-9 | Parallel GPU | CUDA/Numba (optional) | - |
| 9-10 | Testing | Benchmarking, optimization | - |
| 11 | **Part B DUE** | Submit report + code | **Report + Code** |
| 12 | Presentation | Prepare demo, rehearse | - |
| 12-13 | **Demo** | Present and Q&A | **Presentation** |

---

## 🆘 Getting Help

### If You're Stuck:

1. Re-read the notebook (answers often there)
2. Check lecture notes (review concepts)
3. Google error messages
4. Discuss with team
5. Ask tutor (office hours/email)
6. **Never plagiarize** - Adapt examples, don't copy

### Frequently Asked Questions

**Q: Can we use Python instead of C/C++?**
A: Yes! These notebooks use Python (numba, multiprocessing).

**Q: Do we need a GPU?**
A: No, but helps for excellent grades. Use cloud services if needed.

**Q: How unique must our project be?**
A: Unique title and approach. Can't duplicate another group.

**Q: What if demo fails?**
A: Have backup (screenshots, video). See notebook 11.

**Q: Page count?**
A: Part A: 5-10 pages. Part B: 8-20 pages. Quality > quantity.

---

## 📞 Resources

### Course Materials
- **Lecture Notes**: `../LectureNotes/Chapter 01-11.pdf`
- **Practicals**: `../Practicals/Practical 1-5.pdf`

### External Links
- [OpenMP Tutorial](https://www.openmp.org/resources/)
- [CUDA Programming](https://docs.nvidia.com/cuda/)
- [Numba Documentation](https://numba.readthedocs.io/)
- [Google Scholar](https://scholar.google.com/)
- [IEEE Xplore](https://ieeexplore.ieee.org/)

---

## 🎓 Learning Outcomes

After completing this assignment:

1. ✅ Understand parallel computing (shared/distributed memory)
2. ✅ Analyze problems for parallelization potential
3. ✅ Implement parallel algorithms (OpenMP/CUDA)
4. ✅ Measure performance (speedup, efficiency, scalability)
5. ✅ Optimize parallel code
6. ✅ Write technical proposals and reports
7. ✅ Present technical work professionally
8. ✅ Work effectively in technical teams

---

**Total Time Investment**: 40-60 hours (Part A: ~15h, Part B: ~35h, Presentation: ~5h)

**Good luck! You have all the tools to excel.** 🚀

---

*Created: November 2025*
*Complete series: 12 notebooks covering proposal → implementation → presentation*
