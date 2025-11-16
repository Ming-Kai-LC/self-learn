# Advanced Data Science Research Methods (Intermediate Level)

**Take your research skills to the next level!**

This comprehensive intermediate course builds on foundational research skills to teach advanced methodologies, statistical rigor, and professional research execution. Perfect for those who have completed beginner research training and want to conduct publication-quality research.

## Prerequisites

**Required:**
- Completion of [Data Science Research Skills (Beginner)](../data-science-research-skills/) or equivalent knowledge
- Python programming basics
- Understanding of basic statistics
- Familiarity with Jupyter notebooks

**Knowledge You Should Have:**
- Basic literature review techniques
- Simple experimental design (A/B testing)
- Basic data collection and ethics
- Introduction to reproducibility
- Basic Git and documentation

## What You'll Learn

This course takes you from **basic research skills** to **advanced research execution**, covering:

- Advanced statistical inference and hypothesis testing
- Causal inference and confounding control
- Complex experimental designs
- Survey design and psychometrics
- Systematic literature reviews and meta-analysis
- Research communication and publishing
- Open science and preregistration
- Advanced reproducibility with Docker
- Research collaboration and project management
- Grant writing and professional development

## Course Structure

**Total Time:** 8-10 hours
**Format:** 15 interactive Jupyter notebooks
**Level:** Intermediate (builds on beginner foundation)

### Learning Path

| Module | Title | Time | Topics |
|--------|-------|------|--------|
| **00** | Intermediate Research Foundations | 30 min | Advanced tooling, Docker, DVC setup |
| **01** | Advanced Statistical Inference | 45 min | Hypothesis testing, effect sizes, power analysis |
| **02** | Causal Inference Fundamentals | 45 min | Causation vs correlation, DAGs, confounding |
| **03** | Advanced Experimental Designs | 45 min | Quasi-experiments, within-subjects, RDD |
| **04** | Survey Design & Measurement | 40 min | Psychometrics, validity, reliability, Cronbach's alpha |
| **05** | Sampling Strategies | 40 min | Probability sampling, sample size calculations |
| **06** | Systematic Literature Reviews | 45 min | PRISMA guidelines, quality assessment, data extraction |
| **07** | Meta-Analysis Basics | 45 min | Pooled effects, forest plots, heterogeneity |
| **08** | Research Communication & Writing | 45 min | IMRaD structure, peer review, publishing |
| **09** | Preregistration & Open Science | 40 min | OSF, registered reports, FAIR principles |
| **10** | Advanced Reproducibility & Containerization | 45 min | Docker, workflow automation, Snakemake |
| **11** | Research Collaboration & Project Management | 40 min | Git workflows, authorship, team dynamics |
| **12** | Publication Ethics & Integrity | 35 min | Research misconduct, p-hacking, integrity |
| **13** | Grant Proposal Basics | 40 min | Funding opportunities, proposal writing |
| **14** | Advanced Data Visualization | 45 min | Publication-quality figures, Plotly, accessibility |
| **15** | Capstone Research Project | 90 min | Complete end-to-end research project |

**Total:** ~9.5 hours of comprehensive, hands-on learning

## Installation

### 1. Clone the Repository

```bash
cd python-projects-portfolio/projects
# Navigate to this directory
cd data-science-research-methods-intermediate
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n research-intermediate python=3.10
conda activate research-intermediate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Docker Setup

For complete reproducibility:

```bash
# Build Docker image
docker build -t research-intermediate .

# Run container
docker run -p 8888:8888 -v $(pwd):/workspace research-intermediate
```

## Quick Start

```bash
# Activate your environment
source venv/bin/activate  # or conda activate research-intermediate

# Start Jupyter
jupyter notebook

# Open notebooks/00_intermediate_foundations.ipynb
```

## Project Structure

```
data-science-research-methods-intermediate/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Docker container setup
├── .gitignore                        # Git ignore rules
│
├── notebooks/                         # Learning modules
│   ├── 00_intermediate_foundations.ipynb
│   ├── 01_advanced_statistical_inference.ipynb
│   ├── 02_causal_inference_fundamentals.ipynb
│   ├── 03_advanced_experimental_designs.ipynb
│   ├── 04_survey_design_measurement.ipynb
│   ├── 05_sampling_strategies.ipynb
│   ├── 06_systematic_literature_reviews.ipynb
│   ├── 07_meta_analysis_basics.ipynb
│   ├── 08_research_communication_writing.ipynb
│   ├── 09_preregistration_open_science.ipynb
│   ├── 10_advanced_reproducibility_containerization.ipynb
│   ├── 11_research_collaboration_project_management.ipynb
│   ├── 12_publication_ethics_integrity.ipynb
│   ├── 13_grant_proposal_basics.ipynb
│   ├── 14_advanced_data_visualization.ipynb
│   ├── 15_capstone_research_project.ipynb
│   ├── outputs/                       # Generated outputs
│   └── exercises/                     # Practice materials
│
├── data/
│   ├── sample_datasets/               # Example datasets
│   ├── meta_analysis_data/            # Meta-analysis examples
│   └── survey_templates/              # Survey design templates
│
├── templates/                         # Research templates
│   ├── preregistration_template.md
│   ├── manuscript_template.md
│   ├── grant_proposal_template.md
│   ├── systematic_review_protocol.md
│   └── data_management_plan.md
│
├── scripts/
│   ├── statistical_helpers.py         # Statistical utilities
│   ├── meta_analysis_tools.py         # Meta-analysis functions
│   ├── visualization_helpers.py       # Advanced plotting
│   └── workflow_automation.py         # Research workflows
│
├── docs/
│   ├── resources.md                   # Additional resources
│   ├── statistical_tables.md          # Reference tables
│   ├── software_guide.md              # Advanced tools
│   └── glossary.md                    # Term definitions
│
└── examples/                          # Example projects
    ├── example_systematic_review/
    ├── example_meta_analysis/
    └── example_rct_analysis/
```

## Learning Approach

### Recommended Study Plan

**Week 1: Statistical Foundations & Design (Modules 00-03)**
- Understand advanced statistical concepts
- Learn causal inference thinking
- Master complex experimental designs

**Week 2: Data & Synthesis (Modules 04-07)**
- Design valid surveys and measurements
- Understand sampling strategies
- Conduct systematic reviews
- Perform meta-analyses

**Week 3: Communication & Collaboration (Modules 08-11)**
- Write research papers
- Practice open science
- Use advanced reproducibility tools
- Collaborate effectively

**Week 4: Integration & Application (Modules 12-15)**
- Navigate research ethics
- Write grant proposals
- Create publication-quality visualizations
- Complete capstone project

### Tips for Success

1. **Build on Beginner Knowledge**: Review beginner concepts if needed
2. **Practice Actively**: Complete all exercises and coding examples
3. **Use Templates**: Leverage provided templates for your own research
4. **Document Everything**: Apply what you learn immediately
5. **Collaborate**: Discuss concepts with peers or study groups
6. **Read Papers**: Apply techniques to real research papers
7. **Build Portfolio**: Use capstone project for your portfolio

## Key Features

- Interactive code examples with real data
- Publication-ready templates
- Advanced visualization techniques
- Docker containerization for reproducibility
- Open science best practices
- Real-world research scenarios
- Comprehensive checklists and workflows
- Example research projects

## Technologies Used

### Core Libraries
- **Statistical Analysis**: pingouin, statsmodels, scipy
- **Causal Inference**: dowhy, causalml
- **Meta-Analysis**: meta, pymare
- **Survey Analysis**: factor-analyzer
- **Visualization**: plotly, bokeh, altair, seaborn
- **Workflow**: snakemake, papermill
- **Containers**: docker
- **Open Science**: osfclient

### Research Tools
- Git/GitHub for version control
- Docker for containerization
- Jupyter for interactive analysis
- Open Science Framework (OSF)
- LaTeX for publication-ready documents

## From Beginner to Intermediate

### What You Learned in Beginner Course
- Basic literature reviews
- Simple research questions
- A/B testing
- Basic data collection
- Introduction to reproducibility
- Basic documentation

### What You'll Gain in This Course
- Statistical rigor and hypothesis testing
- Causal thinking and confounding control
- Complex experimental designs
- Psychometrics and measurement theory
- Systematic reviews and meta-analysis
- Professional research communication
- Advanced reproducibility with containers
- Open science practices
- Grant writing and publishing
- Real-world research execution

## Additional Resources

### Books
- "Designing Clinical Research" by Hulley et al.
- "The Craft of Research" by Booth et al.
- "Meta-Analysis" by Borenstein et al.
- "Causal Inference: The Mixtape" by Cunningham

### Online Courses
- Coursera: "Improving Your Statistical Inferences"
- edX: "Principles, Statistical and Computational Tools for Reproducible Science"
- OSF: Open Science tutorials

### Software Documentation
- [Pingouin Documentation](https://pingouin-stats.org/)
- [DoWhy Documentation](https://www.pywhy.org/dowhy/)
- [Docker Documentation](https://docs.docker.com/)
- [Open Science Framework](https://osf.io/)

### Research Communities
- Open Science Community
- ReproducibiliTea journal clubs
- rOpenSci community
- Center for Open Science

## Troubleshooting

### Common Issues

**Docker not working:**
```bash
# Ensure Docker is installed and running
docker --version
docker ps

# Build image with verbose output
docker build -t research-intermediate . --progress=plain
```

**Package installation errors:**
```bash
# Update pip first
pip install --upgrade pip

# Install packages one by one
pip install -r requirements.txt --verbose
```

**Jupyter notebook not starting:**
```bash
# Reinstall Jupyter
pip install --force-reinstall jupyter notebook

# Start with explicit IP
jupyter notebook --ip=0.0.0.0
```

**Module import errors:**
```bash
# Add project root to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Contributing

Found an issue or have suggestions? This is a learning project, but feedback is welcome:
1. Review the content carefully
2. Test code examples
3. Share improvements or corrections

## License

This project is for educational purposes. Feel free to use these materials for learning and adapt them for your own research training.

## Citation

If you use these materials in your research training, please cite:

```bibtex
@misc{research_methods_intermediate_2024,
  title={Advanced Data Science Research Methods: Intermediate Course},
  author={Research Skills Portfolio},
  year={2024},
  publisher={GitHub},
  url={https://github.com/your-username/python-projects-portfolio}
}
```

## Acknowledgments

This course builds on:
- Open science principles from the Center for Open Science
- Statistical methods from the ASA and RSS
- Best practices from the research community
- Reproducibility guidelines from The Turing Way

---

**Ready to take your research skills to the next level?**

Start with [Module 00: Intermediate Research Foundations](notebooks/00_intermediate_foundations.ipynb)

**Questions or feedback?** Open an issue or reach out to the community.

*Last updated: 2024*
