# BMCS3003: Distributed Systems and Parallel Computing

**Educational Jupyter Notebooks for Learning Parallel Processing and Distributed Systems**

[![Course](https://img.shields.io/badge/Course-BMCS3003-blue)]()
[![Level](https://img.shields.io/badge/Level-Year%203%20Semester%202-orange)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)]()

---

## 📚 Course Information

**Course Code**: BMCS3003
**Course Title**: Distributed Systems and Parallel Computing
**Instructor**: Assoc Prof Ts Dr Tew Yiqi
**Contact**: yiqi@tarc.edu.my
**Institution**: Tunku Abdul Rahman University College (TAR UC)

### Course Learning Outcomes (CLOs)

1. **CLO 1**: Discuss the variety of parallel and distributed computing techniques (C2)
2. **CLO 2**: Analyse a given scenario with parallel and distributed computing techniques (C4)
3. **CLO 3**: Demonstrate appropriate programming skills with regards to parallel and distributed computing (P4)

### Assessment Structure

- **Midterm Test**: 40% (Week 7/8)
- **Assignment**: 60% (Completed Week 12, Presented Week 13-14)
- **Final Examination**: Based on past years' papers

---

## 🎯 Learning Path

### Available Notebooks

| Module | Topic | Difficulty | Time | Status |
|--------|-------|------------|------|--------|
| **00** | Course Setup and Introduction | ⭐⭐⭐ | 45 min | ✅ Complete |
| **01** | Introduction to Distributed Systems | ⭐⭐⭐ | 90 min | ✅ Complete |
| **02** | System Architectures and Transparency | ⭐⭐⭐ | 90 min | 📝 Planned |
| **03** | Real-time Systems | ⭐⭐⭐ | 75 min | 📝 Planned |
| **04** | Clock Synchronization | ⭐⭐⭐ | 75 min | 📝 Planned |
| **05** | Distributed Operating Systems | ⭐⭐⭐ | 60 min | 📝 Planned |

---

## 🚀 Getting Started

### Prerequisites

- Basic understanding of operating systems
- Computer architecture fundamentals
- Python programming (intermediate level)
- Multi-core processor (4+ cores recommended)

### Installation

```bash
# Navigate to parallel-processing directory
cd y3s2/parallel-processing

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install numpy matplotlib psutil jupyter multiprocess

# Launch Jupyter
jupyter notebook
```

Navigate to `notebooks/` and start with `00_setup_introduction.ipynb`.

---

## 📁 Repository Structure

```
parallel-processing/
│
├── notebooks/                          # Educational Jupyter notebooks
│   ├── 00_setup_introduction.ipynb    # ✅ Environment setup
│   ├── 01_introduction_distributed_systems.ipynb  # ✅ Distributed systems basics
│   ├── 02_architectures_transparency.ipynb  # 📝 Coming soon
│   ├── 03_realtime_systems.ipynb      # 📝 Coming soon
│   ├── 04_clock_synchronization.ipynb # 📝 Coming soon
│   └── 05_distributed_operating_systems.ipynb  # 📝 Coming soon
│
├── data/                              # Datasets for exercises
│   ├── raw/                          # Original datasets
│   ├── processed/                    # Cleaned datasets
│   └── sample/                       # Small sample datasets
│
├── LectureNotes/                     # Original lecture PDFs (12 chapters)
├── assignments/                      # Course assignments
├── labs/                            # Lab exercises
├── Practicals/                      # Practical sessions
├── projects/                        # Project templates
├── resources/                       # Additional learning resources
│
└── README.md                        # This file
```

---

## 📖 Module Highlights

### Module 00: Course Setup and Introduction
- ✅ Environment setup and verification
- ✅ First parallel program (sequential vs parallel)
- ✅ Performance metrics (speedup, efficiency)
- ✅ Amdahl's Law introduction
- ✅ System resource monitoring

### Module 01: Introduction to Distributed Systems
- ✅ Distributed systems definition and characteristics
- ✅ Traditional vs distributed architectures
- ✅ Scalability (horizontal vs vertical)
- ✅ Fault tolerance and replication
- ✅ Performance through parallelism
- ✅ Geographical distribution benefits
- ✅ Tightly-coupled vs loosely-coupled systems

### Upcoming Modules

**Module 02**: Distribution architectures, transparency types (access, location, concurrency, replication, failure, migration, performance, scaling)

**Module 03**: Real-time systems, controlling vs controlled systems, typical features, distributed real-time systems

**Module 04**: Clock synchronization (Cristian's Algorithm, Berkeley Algorithm), network delays, time synchronization challenges

**Module 05**: Network OS vs Distributed OS, process/memory/storage management, protection and security

---

## 💡 Study Tips

1. **Sequential Learning**: Complete modules in order
2. **Hands-On Practice**: Run all code examples
3. **Complete Exercises**: Don't skip exercises
4. **Experiment**: Try different parameters
5. **Visualize**: Create plots to understand performance

### Time Allocation
- **Weekly**: 6-8 hours
  - 2-3 hours: Lecture review
  - 3-4 hours: Notebook exercises
  - 1-2 hours: Additional practice

---

## 🛠️ Technologies Covered

- **Python**: multiprocessing, concurrent.futures
- **Visualization**: Matplotlib, NumPy
- **Performance**: psutil, time, timeit
- **Future Modules**: OpenMP, MPI, CUDA (if applicable)

---

## 📚 Additional Resources

### Documentation
- [CUDA Toolkit](https://docs.nvidia.com/cuda/)
- [OpenMP Reference](https://www.openmp.org/wp-content/uploads/OpenMPRefCard-5-2-web.pdf)
- [OpenACC Guide](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

### Textbooks
1. Distributed Systems: Principles and Paradigms - Tanenbaum & Van Steen
2. Introduction to Parallel Computing - Grama et al.

---

## 🗓️ Semester Timeline

| Week | Topics | Deliverables |
|------|--------|--------------|
| 1-2 | Introduction, Distributed Systems | Module 00-01 |
| 3-4 | Architectures, Real-time Systems | Module 02-03 |
| 5-6 | Clock Sync, Operating Systems | Module 04-05 |
| **7-8** | **MIDTERM TEST** | **40%** |
| 9-12 | Advanced Topics, Assignment Work | Modules 06+ |
| **12** | **Assignment Due** | **60%** |
| 13-14 | Presentations, Review | - |
| 15 | **FINAL EXAMINATION** | Comprehensive |

---

## 📞 Contact

**Instructor**: Assoc Prof Ts Dr Tew Yiqi
**Email**: yiqi@tarc.edu.my

---

**Last Updated**: November 2025
**Version**: 1.0

Happy Learning! 🚀
