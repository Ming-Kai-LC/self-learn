# Data Engineering Fundamentals
> A comprehensive, hands-on learning path to master the fundamentals of data engineering with Python and Big Data tools

## About This Project

This project provides a structured, beginner-friendly introduction to data engineering concepts and practices. Through a series of progressive Jupyter notebooks, you'll learn the essential skills needed to design, build, and maintain data pipelines that power modern data-driven applications.

Data engineering is the backbone of any data science or analytics initiative. This course focuses on practical, theory-first learning that builds a solid foundation in:
- ETL (Extract, Transform, Load) processes
- Data pipeline architecture
- Python-based data processing
- Introduction to Big Data tools (Apache Spark, Airflow)
- Data quality and validation techniques

Whether you're transitioning from software development, coming from a data science background, or starting fresh in the data field, this project will give you the foundational knowledge to build robust data systems.

## Who This Is For

This learning path is designed for:

- **Software developers** looking to transition into data engineering roles
- **Data analysts** wanting to understand the engineering behind data pipelines
- **Data science professionals** seeking to learn how data infrastructure works
- **Students** interested in learning data engineering fundamentals
- **Anyone** curious about how large-scale data systems are built and maintained

### Prerequisites Knowledge Level
- **Basic Python**: You should be comfortable with Python syntax, functions, and basic data structures
- **SQL basics**: Understanding of SELECT, JOIN, WHERE clauses is helpful but not required
- **Command line familiarity**: Basic terminal/command prompt usage
- **No prior data engineering experience required**: This course starts from the fundamentals

## What You'll Learn

By completing this course, you will:

### Core Concepts
- Understand the role and responsibilities of data engineers
- Learn the difference between ETL and ELT patterns
- Master data pipeline design principles
- Understand data modeling and schema design basics

### Technical Skills
- Extract data from various sources (APIs, databases, files)
- Transform and clean data using Python (pandas, numpy)
- Load data into different storage systems
- Build end-to-end ETL pipelines with Python
- Implement data quality checks and validation
- Introduction to Apache Spark for distributed processing
- Basic workflow orchestration with Apache Airflow concepts

### Best Practices
- Design patterns for scalable data pipelines
- Error handling and logging in data workflows
- Data validation and quality assurance
- Performance optimization techniques
- Documentation and code organization

## Project Structure

```
data-engineering-fundamentals/
│
├── README.md                          # This file - comprehensive project guide
├── requirements.txt                   # Python dependencies with version pinning
│
├── notebooks/                         # Jupyter notebooks for learning
│   ├── 00_setup_introduction.ipynb                    # Setup and course intro (20-30 min)
│   ├── 01_introduction_to_data_engineering.ipynb      # DE concepts and roles (45-60 min)
│   ├── 02_data_sources_and_extraction.ipynb           # Data extraction techniques (45-60 min)
│   ├── 03_data_transformation_cleaning.ipynb          # Transform data with Python (60-75 min)
│   ├── 04_data_loading_storage.ipynb                  # Loading data to destinations (45-60 min)
│   ├── 05_building_etl_pipelines.ipynb                # End-to-end ETL patterns (60-75 min)
│   ├── 06_introduction_to_apache_spark.ipynb          # Spark fundamentals (60-75 min)
│   ├── 07_workflow_orchestration_airflow.ipynb        # Airflow concepts (45-60 min)
│   ├── 08_data_quality_validation.ipynb               # Quality checks (45-60 min)
│   ├── 09_end_to_end_pipeline_project.ipynb           # Capstone project (90-120 min)
│   └── outputs/                       # Generated files and artifacts
│
├── data/                              # Sample datasets for exercises
│   ├── raw/                          # Raw, unprocessed data
│   ├── processed/                    # Transformed data
│   └── .gitkeep                      # Keeps folder in git
│
└── scripts/                           # Utility scripts
    └── setup_helpers.py              # Helper functions for setup
```

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version`

2. **Jupyter Notebook or JupyterLab**
   - Will be installed via requirements.txt
   - Alternative: Use VS Code with Jupyter extension

3. **Git** (for cloning the repository)
   - Download from: https://git-scm.com/

### Optional but Recommended

- **Docker Desktop** (for future Airflow/Spark exercises)
  - Download from: https://www.docker.com/products/docker-desktop
- **PostgreSQL** (for database exercises)
  - Download from: https://www.postgresql.org/download/
- **VS Code** or **PyCharm** (for better Python development experience)

### System Requirements
- **RAM**: 4GB minimum, 8GB+ recommended
- **Disk Space**: 2GB for dependencies and datasets
- **OS**: Windows 10/11, macOS 10.14+, or Linux

## Installation

Follow these steps to set up your learning environment:

### Step 1: Clone or Navigate to the Repository

```bash
# If you haven't cloned the portfolio yet
git clone https://github.com/yourusername/python-projects-portfolio.git
cd python-projects-portfolio/projects/data-engineering-fundamentals

# If you already have the portfolio
cd python-projects-portfolio/projects/data-engineering-fundamentals
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
python -c "import pandas, numpy, sqlalchemy; print('Dependencies installed successfully!')"
```

### Step 4: Launch Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (recommended)
jupyter lab
```

Your browser should open automatically to the Jupyter interface. Navigate to the `notebooks/` folder and start with `00_setup_introduction.ipynb`.

### Step 5: Verify Setup

Open and run `00_setup_introduction.ipynb` to:
- Verify all dependencies are installed correctly
- Understand the learning path
- Run your first data engineering example

## Learning Path

This course is designed to be followed sequentially. Each module builds upon concepts from previous modules.

### Module 00: Setup and Introduction (20-30 minutes)
**File**: `00_setup_introduction.ipynb`

- Verify your environment setup
- Overview of data engineering landscape
- Understanding the data engineering workflow
- Your first ETL example
- Introduction to Jupyter notebooks

**Key Takeaway**: Environment is ready and you understand the course structure.

---

### Module 01: Introduction to Data Engineering (45-60 minutes)
**File**: `01_introduction_to_data_engineering.ipynb`

- What is data engineering?
- Data engineer vs. data scientist vs. data analyst
- The modern data stack
- ETL vs. ELT patterns
- Data pipeline architectures
- Common data engineering challenges

**Key Takeaway**: Clear understanding of data engineering roles and responsibilities.

---

### Module 02: Data Sources and Extraction (45-60 minutes)
**File**: `02_data_sources_and_extraction.ipynb`

- Types of data sources (APIs, databases, files, streams)
- Reading CSV, JSON, and Excel files with pandas
- Connecting to databases with SQLAlchemy
- Extracting data from REST APIs
- Handling different data formats
- Error handling and retry logic

**Key Takeaway**: Confidence in extracting data from multiple sources.

---

### Module 03: Data Transformation and Cleaning (60-75 minutes)
**File**: `03_data_transformation_cleaning.ipynb`

- Data cleaning fundamentals
- Handling missing values
- Data type conversions
- String manipulation and regex
- Date and time operations
- Aggregations and grouping
- Merging and joining datasets
- Data normalization techniques

**Key Takeaway**: Master essential data transformation skills with pandas.

---

### Module 04: Data Loading and Storage (45-60 minutes)
**File**: `04_data_loading_storage.ipynb`

- Loading data to CSV, JSON, and Parquet files
- Writing data to SQL databases
- Batch vs. incremental loading
- Upsert operations
- Data partitioning strategies
- Compression and file formats
- Performance considerations

**Key Takeaway**: Efficiently load transformed data into target systems.

---

### Module 05: Building ETL Pipelines (60-75 minutes)
**File**: `05_building_etl_pipelines.ipynb`

- ETL pipeline design patterns
- Building modular pipeline components
- Configuration management
- Logging and monitoring
- Error handling and recovery
- Pipeline testing strategies
- Building your first complete ETL pipeline

**Key Takeaway**: Design and implement production-quality ETL pipelines.

---

### Module 06: Introduction to Apache Spark (60-75 minutes)
**File**: `06_introduction_to_apache_spark.ipynb`

- What is Apache Spark and why use it?
- Spark architecture (driver, executors, cluster)
- PySpark basics
- DataFrames and transformations
- Actions vs. transformations
- Reading and writing data with Spark
- When to use Spark vs. pandas

**Key Takeaway**: Understand distributed data processing with Apache Spark.

---

### Module 07: Workflow Orchestration with Airflow (45-60 minutes)
**File**: `07_workflow_orchestration_airflow.ipynb`

- What is workflow orchestration?
- Introduction to Apache Airflow
- DAGs (Directed Acyclic Graphs)
- Operators and tasks
- Scheduling and dependencies
- Monitoring and alerting
- Alternative orchestration tools

**Key Takeaway**: Understand how to schedule and manage data pipelines.

---

### Module 08: Data Quality and Validation (45-60 minutes)
**File**: `08_data_quality_validation.ipynb`

- Data quality dimensions
- Validation strategies
- Schema validation
- Data profiling
- Anomaly detection
- Implementing data quality checks
- Testing data pipelines
- Data contracts

**Key Takeaway**: Ensure data reliability with quality checks.

---

### Module 09: End-to-End Pipeline Project (90-120 minutes)
**File**: `09_end_to_end_pipeline_project.ipynb`

- Capstone project: Build a complete data pipeline
- Extract data from multiple sources
- Transform and clean the data
- Load into a data warehouse
- Implement quality checks
- Add logging and error handling
- Document your pipeline
- Best practices and optimization

**Key Takeaway**: Apply all learned concepts in a real-world scenario.

---

### Total Estimated Time: 8-10 hours

## How to Use This Project

### Recommended Approach

1. **Follow sequentially**: Start with Module 00 and progress in order
2. **Hands-on practice**: Run every code cell, don't just read
3. **Experiment**: Modify code examples to deepen understanding
4. **Take notes**: Document your learnings and questions
5. **Build as you learn**: Try implementing similar pipelines with your own data

### For Each Module

1. **Read the introduction**: Understand the module objectives
2. **Follow along**: Execute code cells as you read
3. **Complete exercises**: Practice problems are included in each module
4. **Review summary**: Ensure you understood key concepts
5. **Take breaks**: Don't rush through the material

### Study Schedule Suggestions

**Intensive (1 week)**
- 1-2 modules per day
- 1.5-2 hours daily
- Complete in 5-7 days

**Moderate (2 weeks)**
- 3-4 modules per week
- 1 hour per session
- Complete in 10-14 days

**Relaxed (1 month)**
- 2-3 modules per week
- 30-45 minutes per session
- Complete in 3-4 weeks

## Technologies Used

### Core Python Libraries
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **SQLAlchemy** - SQL toolkit and ORM
- **requests** - HTTP library for API calls

### Data Processing
- **PySpark** - Apache Spark Python API
- **pyarrow** - Columnar data processing

### Database Connectors
- **psycopg2** - PostgreSQL adapter
- **pymysql** - MySQL connector

### Data Validation
- **great_expectations** - Data quality framework
- **pandera** - Statistical data validation

### Workflow Orchestration (Concepts)
- **Apache Airflow** - Workflow orchestration
- **Prefect** - Modern workflow orchestration

### Utilities
- **python-dotenv** - Environment variable management
- **jupyter** - Interactive computing

## Tips for Success

1. **Master the fundamentals first**
   - Don't skip modules, even if they seem basic
   - Solid foundations lead to better understanding later

2. **Practice with real data**
   - After each module, try the concepts with your own datasets
   - Real-world practice reinforces learning

3. **Understand, don't memorize**
   - Focus on understanding concepts, not memorizing syntax
   - You can always look up syntax; understanding is key

4. **Join the community**
   - Engage with data engineering communities
   - Ask questions on Stack Overflow, Reddit's r/dataengineering
   - Share your learning journey

5. **Document your learning**
   - Keep a learning journal
   - Write blog posts about what you learn
   - Create your own data engineering projects

6. **Start small, think big**
   - Begin with simple pipelines
   - Gradually add complexity
   - Focus on reliability over features

7. **Read error messages carefully**
   - Errors are learning opportunities
   - Understand why something failed
   - Learn to debug systematically

## Troubleshooting

### Common Issues and Solutions

#### Issue: Package installation fails
```bash
# Solution: Upgrade pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Issue: Jupyter kernel crashes
```bash
# Solution: Reinstall ipykernel
pip install --upgrade ipykernel
python -m ipykernel install --user
```

#### Issue: Import errors for pandas/numpy
```bash
# Solution: Verify installation
pip list | grep pandas
pip install --force-reinstall pandas
```

#### Issue: Database connection errors
- Verify database is running
- Check connection string credentials
- Ensure firewall allows connections
- Test connection separately first

#### Issue: Out of memory errors
- Process data in chunks (use `chunksize` parameter)
- Reduce dataset size for learning
- Close unnecessary applications
- Upgrade RAM if consistently facing issues

#### Issue: Spark installation problems
- Ensure Java 8+ is installed
- Set JAVA_HOME environment variable
- Use PySpark instead of standalone Spark for learning
- Consider using Databricks Community Edition (free)

### Getting Help

If you encounter issues not covered here:

1. **Check the notebook comments**: Many common issues are addressed inline
2. **Search Stack Overflow**: Most Python/pandas errors have been solved before
3. **Review the official documentation**: pandas, Spark, Airflow docs are excellent
4. **Ask in communities**: r/dataengineering, r/learnpython, r/apachespark
5. **Create an issue**: If you find bugs in the notebooks, please report them

## Next Steps

After completing this course, consider these paths to deepen your data engineering skills:

### Immediate Next Steps
1. **Build your own project**
   - Find a dataset that interests you
   - Build an end-to-end pipeline
   - Deploy it (even locally)
   - Document the process

2. **Contribute to open source**
   - Contribute to data engineering tools
   - Share your improvements to these notebooks
   - Help others learning data engineering

3. **Expand your toolkit**
   - Learn Docker and containerization
   - Deep dive into Apache Airflow
   - Master Apache Spark
   - Explore cloud platforms (AWS, GCP, Azure)

### Advanced Topics to Explore
- **Stream processing**: Apache Kafka, Apache Flink
- **Data warehousing**: Snowflake, BigQuery, Redshift
- **Data lakes**: Delta Lake, Apache Iceberg
- **Data modeling**: Kimball, Data Vault 2.0
- **Infrastructure as Code**: Terraform, Pulumi
- **CI/CD for data**: Testing, deployment automation
- **Data governance**: Lineage, cataloging, compliance

### Recommended Resources
- **Books**:
  - "Fundamentals of Data Engineering" by Joe Reis & Matt Housley
  - "Designing Data-Intensive Applications" by Martin Kleppmann
  - "The Data Warehouse Toolkit" by Ralph Kimball

- **Online Courses**:
  - DataCamp: Data Engineering track
  - Coursera: Data Engineering specializations
  - Udacity: Data Engineering Nanodegree

- **Communities**:
  - r/dataengineering (Reddit)
  - Data Engineering Discord servers
  - Local data engineering meetups

- **Blogs and Newsletters**:
  - Seattle Data Guy
  - Data Engineering Weekly
  - Locally Optimistic

- **Practice Platforms**:
  - Kaggle (datasets and competitions)
  - DataCamp Projects
  - Databricks Community Edition

## Contributing

This is a learning project, but improvements are welcome! If you find:
- Errors or typos in notebooks
- Better ways to explain concepts
- Additional exercises or examples
- Missing important topics

Please feel free to contribute or provide feedback.

## License

This project is part of a personal learning portfolio. Feel free to use it for your own learning purposes.

## Acknowledgments

This learning path was created to provide a structured, comprehensive introduction to data engineering fundamentals. It draws from industry best practices, official documentation, and real-world data engineering experiences.

Special thanks to the open-source community for creating the amazing tools (pandas, Spark, Airflow) that make modern data engineering possible.

---

**Ready to start your data engineering journey?**

Open `notebooks/00_setup_introduction.ipynb` and let's begin!

**Questions or feedback?** Create an issue or reach out through the portfolio repository.

Happy Learning!
