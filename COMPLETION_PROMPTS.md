# Project Completion Prompts for Claude Code

**Last Updated**: 2025-11-18
**Purpose**: Actionable prompts to complete missing components in the self-learn repository

---

## How to Use These Prompts

1. Copy the entire prompt section for the component you want to complete
2. Open a new Claude Code session
3. Paste the prompt
4. Review and approve the plan
5. Let Claude Code complete the work

**Note**: Each prompt is self-contained and includes all necessary context.

---

## 🔴 CRITICAL PRIORITY (Complete These First)

### 1. Module 05.1: Machine Learning Fundamentals

**Impact**: Critical learning path gap - blocks progression to Deep Learning
**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐ Intermediate

```
I need you to create a complete Machine Learning Fundamentals learning path for my data science portfolio. This is Module 05 in my data-science project structure.

Context:
- Location: /home/user/self-learn/data-science/05_machine_learning/machine-learning-fundamentals/
- README and requirements.txt already exist but there are NO notebooks yet
- This follows my educational notebook standards (see .claude/CLAUDE.md)
- Previous modules cover: Python, Jupyter, Math, Pandas, Visualization, Data Engineering
- Students should have strong foundation in statistics and pandas

Requirements:
1. Create 12-15 sequential notebooks (00-14) covering:
   - 00: Introduction to ML and scikit-learn setup
   - 01: Supervised vs Unsupervised Learning
   - 02: Data Preparation and Train/Test Split
   - 03: Linear Regression (theory and practice)
   - 04: Logistic Regression
   - 05: Decision Trees
   - 06: Model Evaluation Metrics (accuracy, precision, recall, F1, ROC-AUC)
   - 07: Cross-Validation and Hyperparameter Tuning
   - 08: Regularization (L1, L2, Elastic Net)
   - 09: Support Vector Machines
   - 10: K-Nearest Neighbors
   - 11: Naive Bayes
   - 12: Clustering (K-Means, DBSCAN)
   - 13: Dimensionality Reduction (PCA, t-SNE)
   - 14: Final Project - End-to-End ML Pipeline

2. Quality Standards:
   - Each notebook must have: metadata cell, learning objectives, prerequisites
   - Minimum 30% markdown content (explanations, not just code)
   - At least 3 exercises per major concept
   - Use real datasets (iris, titanic, boston housing, etc. from sklearn)
   - All code must execute successfully ("Restart and Run All")
   - Use relative paths for data loading
   - Set random seeds for reproducibility

3. Teaching Approach:
   - Start with theory, then demonstrate with code
   - Show common pitfalls (data leakage, overfitting)
   - Include visualization of model performance
   - Explain when to use each algorithm
   - Progressive difficulty: basic → intermediate → advanced

4. After creating notebooks:
   - Run notebook-tester to validate quality metrics
   - Ensure requirements.txt has all dependencies
   - Create data/sample/ directory with small datasets (<10MB)
   - Update README.md with notebook descriptions

Please follow the project structure and quality standards defined in .claude/CLAUDE.md. Focus on practical, hands-on learning with clear explanations.
```

---

### 2. Module 05.2: Feature Engineering

**Impact**: Essential for ML model performance
**Estimated Time**: 2-3 hours
**Difficulty**: ⭐⭐ Intermediate

```
Create a comprehensive Feature Engineering learning path for my data science portfolio (Module 05.2).

Context:
- Location: /home/user/self-learn/data-science/05_machine_learning/feature-engineering/
- README and requirements.txt exist, NO notebooks yet
- Students have completed ML Fundamentals (Module 05.1)
- This is practical, hands-on skill development

Requirements:
1. Create 10-12 sequential notebooks covering:
   - 00: Introduction to Feature Engineering and Why It Matters
   - 01: Handling Missing Data (imputation strategies)
   - 02: Encoding Categorical Variables (one-hot, label, target encoding)
   - 03: Feature Scaling and Normalization
   - 04: Creating Polynomial Features and Interactions
   - 05: Binning and Discretization
   - 06: Date/Time Feature Engineering
   - 07: Text Feature Engineering (TF-IDF, word embeddings basics)
   - 08: Feature Selection Methods (filter, wrapper, embedded)
   - 09: Feature Importance and Interpretability
   - 10: Automated Feature Engineering (featuretools introduction)
   - 11: Final Project - Feature Engineering Pipeline

2. Datasets:
   - Use real-world messy datasets (Kaggle datasets with missing values)
   - Include examples with dates, text, and categorical features
   - Show before/after model performance improvements

3. Key Concepts:
   - Demonstrate impact on model performance (baseline vs. engineered)
   - Show proper train/test separation (avoid data leakage)
   - Use sklearn Pipeline and ColumnTransformer
   - Include exercises to engineer features creatively

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown content
   - 3+ exercises per notebook
   - All code executable with "Restart and Run All"
   - Create sample data in data/sample/ (<10MB)

Focus on practical techniques that improve model performance in real projects.
```

---

### 3. Module 05.3: Ensemble Methods

**Impact**: Advanced ML techniques, critical for competitions and production
**Estimated Time**: 2-3 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create an Ensemble Methods learning path for my data science portfolio (Module 05.3).

Context:
- Location: /home/user/self-learn/data-science/05_machine_learning/ensemble-methods/
- README and requirements.txt exist, NO notebooks yet
- Students have completed ML Fundamentals and Feature Engineering
- This is advanced content for competitive ML and production systems

Requirements:
1. Create 10-12 sequential notebooks covering:
   - 00: Introduction to Ensemble Learning (wisdom of crowds)
   - 01: Bagging and Bootstrap Aggregation
   - 02: Random Forests (theory, hyperparameters, tuning)
   - 03: Boosting Fundamentals (AdaBoost)
   - 04: Gradient Boosting Machines (GBM)
   - 05: XGBoost (installation, usage, tuning)
   - 06: LightGBM (speed and performance)
   - 07: CatBoost (handling categorical features)
   - 08: Stacking and Blending
   - 09: Voting Classifiers/Regressors
   - 10: Model Comparison and Selection
   - 11: Final Project - Kaggle-Style Competition

2. Key Focus Areas:
   - Hyperparameter tuning for each algorithm
   - Comparison of ensemble methods (speed, accuracy, interpretability)
   - Handling imbalanced datasets
   - Feature importance visualization
   - Cross-validation strategies

3. Practical Implementation:
   - Use real Kaggle datasets (Titanic, House Prices, etc.)
   - Show complete workflow: EDA → Feature Engineering → Model Selection → Tuning
   - Include model interpretation (SHAP values, feature importance)
   - Demonstrate ensemble diversity benefits

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown content explaining WHY, not just WHAT
   - 3+ exercises per major concept
   - Include performance benchmarks
   - All code must execute successfully

Target: Make students Kaggle-competition ready with ensemble methods mastery.
```

---

### 4. Module 08: Big Data with PySpark

**Impact**: Essential for big data processing and industry relevance
**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create a comprehensive PySpark learning path for my data science portfolio (Module 08).

Context:
- Location: /home/user/self-learn/data-science/08_big_data/big-data-with-pyspark/
- README and requirements.txt exist (template only), NO notebooks yet
- Students have completed Python, Pandas, SQL, and Data Engineering modules
- Focus on distributed computing concepts and PySpark API

Requirements:
1. Create 12-15 sequential notebooks covering:
   - 00: Introduction to Big Data and Spark Ecosystem
   - 01: PySpark Setup and SparkSession
   - 02: RDD Basics (Resilient Distributed Datasets)
   - 03: DataFrames and Datasets in PySpark
   - 04: Data Loading and Saving (CSV, Parquet, JSON)
   - 05: DataFrame Operations (select, filter, groupBy, joins)
   - 06: Spark SQL and Temporary Views
   - 07: Window Functions and Advanced Transformations
   - 08: PySpark Machine Learning (MLlib basics)
   - 09: Feature Engineering at Scale
   - 10: Model Training and Evaluation with MLlib
   - 11: Spark Streaming Basics
   - 12: Performance Optimization (partitioning, caching, broadcast)
   - 13: Spark on Clusters (local → cluster concepts)
   - 14: Final Project - ETL Pipeline with ML

2. Technical Requirements:
   - Use PySpark in local mode (no cluster needed for learning)
   - Include sample datasets of varying sizes
   - Show pandas → PySpark conversion patterns
   - Demonstrate lazy evaluation and DAG concepts
   - Include performance comparisons (pandas vs PySpark)

3. Key Concepts:
   - Distributed computing fundamentals
   - Transformations vs. Actions
   - Partitioning strategies
   - Broadcast variables and accumulators
   - Catalyst optimizer awareness

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown explaining distributed concepts
   - 3+ exercises per notebook
   - Include visualization of execution plans
   - All code must run locally

Focus on practical PySpark skills for big data engineering and ML at scale.
```

---

### 5. Module 09.1: MLOps and Deployment

**Impact**: Critical for production ML systems, high job market value
**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create a comprehensive MLOps and Deployment learning path for my data science portfolio (Module 09.1).

Context:
- Location: /home/user/self-learn/data-science/09_mlops_and_deployment/mlops-deployment/
- README and requirements.txt exist, NO notebooks yet
- Students have ML fundamentals and can build models
- Focus on productionizing ML models, not just training them

Requirements:
1. Create 12-15 sequential notebooks covering:
   - 00: Introduction to MLOps and the ML Lifecycle
   - 01: Experiment Tracking with MLflow
   - 02: Model Versioning and Registry
   - 03: Model Serialization (pickle, joblib, ONNX)
   - 04: Creating ML APIs with FastAPI
   - 05: Containerization with Docker
   - 06: Model Serving Patterns (batch, real-time, streaming)
   - 07: Model Monitoring and Logging
   - 08: Data Drift Detection
   - 09: Model Retraining Pipelines
   - 10: CI/CD for ML (GitHub Actions)
   - 11: A/B Testing and Model Evaluation in Production
   - 12: Infrastructure as Code (basics)
   - 13: MLOps Best Practices and Anti-Patterns
   - 14: Final Project - End-to-End MLOps Pipeline

2. Technical Stack:
   - MLflow for experiment tracking
   - FastAPI for model serving
   - Docker for containerization
   - GitHub Actions for CI/CD
   - Pytest for testing ML code
   - Great Expectations for data validation

3. Key Concepts:
   - Model lifecycle management
   - Reproducibility and versioning
   - Monitoring and observability
   - Continuous training vs. continuous deployment
   - ML technical debt

4. Practical Projects:
   - Deploy a simple model as REST API
   - Create Docker container for ML model
   - Set up automated testing pipeline
   - Implement model monitoring dashboard

5. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown content
   - Include architecture diagrams
   - All code executable locally
   - Focus on practical, production-ready patterns

Target: Make students production-ML ready with modern MLOps practices.
```

---

### 6. Module 09.2: Cloud Platforms for ML

**Impact**: Industry-standard deployment knowledge
**Estimated Time**: 2-3 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create a Cloud Platforms for ML learning path (Module 09.2).

Context:
- Location: /home/user/self-learn/data-science/09_mlops_and_deployment/cloud-platforms/
- README and requirements.txt exist, NO notebooks yet
- Students have completed MLOps Deployment basics
- Focus on major cloud platforms: AWS, Azure, GCP

Requirements:
1. Create 10-12 sequential notebooks covering:
   - 00: Introduction to Cloud ML Services (comparison)
   - 01: AWS SageMaker Basics (notebook instances, training)
   - 02: AWS SageMaker Deployment (endpoints, batch transform)
   - 03: Azure ML Studio Introduction
   - 04: Azure ML Pipelines and Deployment
   - 05: Google Cloud AI Platform Basics
   - 06: GCP Vertex AI (training and serving)
   - 07: Serverless ML (AWS Lambda, Azure Functions)
   - 08: Cost Optimization Strategies
   - 09: Multi-Cloud ML Considerations
   - 10: Cloud Storage for ML (S3, Blob, GCS)
   - 11: Final Project - Deploy Model on Cloud

2. Teaching Approach:
   - Show free tier / minimal cost examples
   - Include step-by-step screenshots/diagrams
   - Compare features across platforms
   - Focus on practical deployment patterns
   - Highlight cost considerations

3. Important Note:
   - Use mock/simulation where actual cloud costs apply
   - Provide clear instructions for cleanup
   - Show CLI/SDK usage, not just console
   - Include Infrastructure as Code examples (Terraform basics)

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown with architectural explanations
   - Include cost calculators
   - Clear warnings about charges
   - All code should be testable in free tiers

Focus on practical cloud deployment skills without breaking the bank.
```

---

## 🟡 HIGH PRIORITY (Complete After Critical)

### 7. Module 06.1: Deep Learning Fundamentals

**Impact**: Foundation for modern AI applications
**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create Deep Learning Fundamentals notebooks for my data science portfolio (Module 06.1).

Context:
- Location: /home/user/self-learn/data-science/06_deep_learning/deep-learning-fundamentals/
- README and requirements.txt exist, NO notebooks yet
- Students have ML fundamentals and math background
- This comes before CNN and NLP Transformers modules

Requirements:
1. Create 12-15 sequential notebooks covering:
   - 00: Introduction to Neural Networks and Deep Learning
   - 01: Perceptrons and Activation Functions
   - 02: Backpropagation and Gradient Descent
   - 03: Building Neural Networks with NumPy (from scratch)
   - 04: Introduction to TensorFlow/Keras
   - 05: Feed-Forward Neural Networks with Keras
   - 06: Optimizers (SGD, Adam, RMSprop)
   - 07: Regularization Techniques (Dropout, Batch Normalization)
   - 08: Loss Functions and Metrics
   - 09: Hyperparameter Tuning for Deep Learning
   - 10: Transfer Learning Concepts
   - 11: Debugging Neural Networks
   - 12: Model Interpretation and Visualization
   - 13: PyTorch Introduction (comparison with TensorFlow)
   - 14: Final Project - Deep Learning Pipeline

2. Key Concepts:
   - Mathematical intuition (gradients, chain rule)
   - Practical implementation patterns
   - Common pitfalls (vanishing gradients, overfitting)
   - Framework comparison (TensorFlow vs PyTorch)
   - GPU acceleration basics

3. Datasets:
   - Start with simple datasets (MNIST, Fashion-MNIST)
   - Progress to more complex (CIFAR-10 for basics)
   - Include tabular data examples

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown with mathematical explanations
   - Include visualizations of learning curves
   - 3+ exercises per major concept
   - All code executable (CPU mode, GPU optional)

Focus on building strong DL foundations before specialized architectures.
```

---

### 8. Module 06.3: NLP and Transformers

**Impact**: Modern NLP is transformer-based, high demand skill
**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create NLP and Transformers learning path for my data science portfolio (Module 06.3).

Context:
- Location: /home/user/self-learn/data-science/06_deep_learning/nlp-transformers/
- README and requirements.txt exist, NO notebooks yet
- Students have completed Deep Learning Fundamentals
- Focus on modern NLP with transformers (BERT, GPT family)

Requirements:
1. Create 12-15 sequential notebooks covering:
   - 00: Introduction to NLP and Text Processing
   - 01: Text Preprocessing (tokenization, cleaning, normalization)
   - 02: Word Embeddings (Word2Vec, GloVe, FastText)
   - 03: Recurrent Neural Networks (RNN, LSTM, GRU)
   - 04: Sequence-to-Sequence Models
   - 05: Attention Mechanism (theory and implementation)
   - 06: Transformer Architecture (detailed breakdown)
   - 07: BERT and Masked Language Modeling
   - 08: GPT and Autoregressive Models
   - 09: Fine-Tuning Transformers with Hugging Face
   - 10: Text Classification with Transformers
   - 11: Named Entity Recognition (NER)
   - 12: Question Answering Systems
   - 13: Text Generation and Summarization
   - 14: Final Project - End-to-End NLP Application

2. Technical Stack:
   - Hugging Face Transformers library
   - Datasets library for easy data loading
   - TensorFlow/Keras or PyTorch
   - spaCy for preprocessing
   - NLTK for text utilities

3. Key Concepts:
   - Self-attention mechanism visualization
   - Transfer learning in NLP
   - Tokenization strategies (BPE, WordPiece)
   - Model comparison (BERT vs GPT vs T5)
   - Ethical considerations (bias in language models)

4. Datasets:
   - Use Hugging Face datasets (GLUE, SQuAD, etc.)
   - Include multilingual examples
   - Show domain adaptation examples

5. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown content
   - Include architecture visualizations
   - 3+ exercises per notebook
   - All code executable (use small models for CPU)

Focus on practical transformer usage for real-world NLP tasks.
```

---

### 9. Module 11: Portfolio Projects (Kaggle Classics)

**Impact**: Showcase skills for job applications
**Estimated Time**: 4-5 hours
**Difficulty**: ⭐⭐⭐ Advanced

```
Create Portfolio Projects learning path featuring Kaggle competition solutions (Module 11).

Context:
- Location: /home/user/self-learn/data-science/11_portfolio_projects/portfolio-kaggle-classics/
- README and requirements.txt exist (template), NO notebooks yet
- Students have completed ML, Feature Engineering, Ensemble Methods
- Focus on end-to-end project walkthroughs

Requirements:
1. Create 8-10 project notebooks covering classic Kaggle competitions:
   - 00: Introduction to Kaggle and Competition Strategy
   - 01: Titanic - Classification Masterclass
   - 02: House Prices - Regression Techniques
   - 03: Credit Card Fraud - Imbalanced Classification
   - 04: Customer Segmentation - Clustering Project
   - 05: Time Series Forecasting - Sales Prediction
   - 06: NLP - Sentiment Analysis (IMDB/Amazon Reviews)
   - 07: Computer Vision - Image Classification
   - 08: Recommender Systems - Movie Recommendations
   - 09: Final Portfolio Project Guidelines

2. Project Structure (for each):
   - Problem understanding and EDA (comprehensive)
   - Data cleaning and feature engineering
   - Baseline model establishment
   - Advanced modeling techniques
   - Model interpretation and insights
   - Production considerations
   - Portfolio presentation tips

3. Key Skills Demonstrated:
   - Complete ML pipeline from raw data to predictions
   - Handling messy real-world data
   - Feature engineering creativity
   - Model selection and tuning
   - Result interpretation and communication
   - Code quality and documentation

4. Portfolio Focus:
   - GitHub-ready notebooks (clean, documented)
   - Include README for each project
   - Show thought process and decision-making
   - Visualizations for storytelling
   - Business insights, not just accuracy

5. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 40%+ markdown (explaining decisions)
   - Professional code quality
   - Include requirements.txt per project
   - All code executable with sample data

Target: Create portfolio-ready projects that impress recruiters and hiring managers.
```

---

### 10. Module 00.4: GitHub and Version Control

**Impact**: Essential developer skill, currently missing
**Estimated Time**: 2-3 hours
**Difficulty**: ⭐ Beginner

```
Create GitHub and Version Control learning path (Module 00.4).

Context:
- Location: /home/user/self-learn/data-science/00_tools_and_foundations/github-learning/
- README and requirements.txt exist, NO notebooks yet
- This is foundational skill for all developers
- Students may have no prior git experience

Requirements:
1. Create 10-12 sequential notebooks covering:
   - 00: Introduction to Version Control and Why It Matters
   - 01: Git Basics (init, add, commit, status, log)
   - 02: Branching and Merging
   - 03: Remote Repositories and GitHub
   - 04: Collaborating with Pull Requests
   - 05: Resolving Merge Conflicts
   - 06: Git Best Practices (commit messages, .gitignore)
   - 07: GitHub Features (Issues, Projects, Actions)
   - 08: Git for Data Science (handling notebooks, large files)
   - 09: GitHub Pages and Portfolio Hosting
   - 10: Advanced Git (rebase, cherry-pick, stash)
   - 11: Final Project - Create Your GitHub Portfolio

2. Teaching Approach:
   - Use Jupyter notebooks with embedded bash commands
   - Include visualizations of git concepts
   - Hands-on exercises with real repositories
   - Show common mistakes and how to fix them
   - Include GitHub CLI (gh) usage

3. Practical Exercises:
   - Create and manage repositories
   - Collaborate on a mock project
   - Set up GitHub Pages for portfolio
   - Use GitHub Actions for automation
   - Practice code review workflow

4. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - 30%+ markdown with explanations
   - Include diagrams of git workflows
   - 3+ exercises per notebook
   - All commands executable in notebook

Focus on practical git/GitHub skills for data science collaboration and portfolio building.
```

---

## 🟢 MEDIUM PRIORITY (Quality Improvements)

### 11. English Project Reorganization

**Impact**: Activate 500+ archived notebooks
**Estimated Time**: 2-3 hours
**Difficulty**: ⭐⭐ Intermediate

```
Reorganize and activate the English learning project structure.

Context:
- Location: /home/user/self-learn/english/
- Currently has 2 active notebooks + 500+ archived notebooks in _archive/
- Archived content: 30 B1/A2 modules × 4 parts each + A1 reviews
- B2 level started but incomplete
- Needs modern structure following CEFR progression

Requirements:
1. Analyze current structure:
   - Review _archive/ content for quality
   - Identify which modules to activate
   - Determine B2 completion needs

2. Create new structure:
   ```
   english/
   ├── A1_Beginner/
   │   ├── 00_placement_test.ipynb
   │   ├── modules/ (10-15 core modules)
   │   └── reviews/ (existing 4 review notebooks)
   ├── A2_Elementary/
   │   └── modules/ (select best from archive)
   ├── B1_Intermediate/
   │   └── modules/ (select best from archive)
   ├── B2_Upper_Intermediate/
   │   ├── writing/ (existing passive voice)
   │   └── [complete other skills]
   ├── 00_START_HERE/
   │   ├── daily_schedule.ipynb (keep)
   │   └── skill_assessment.ipynb (keep)
   └── data/ (audio files)
   ```

3. B2 Level Completion:
   - Create 10-12 B2 notebooks covering:
     - Writing: Advanced essays, business writing
     - Reading: Academic texts, critical analysis
     - Listening: Lectures, discussions (with audio)
     - Speaking: Presentations, debates (with prompts)
     - Grammar: Complex structures, nuanced usage
     - Vocabulary: Academic, professional contexts

4. Migration Strategy:
   - Select top 10 modules from each level (A2, B1)
   - Modernize format to match current standards
   - Ensure audio files are linked correctly
   - Update README with new structure

5. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - CEFR-aligned difficulty progression
   - Include audio for pronunciation practice
   - Interactive exercises with immediate feedback
   - Progress tracking between levels

Focus on creating a clear, progressive learning path from A1 to B2.
```

---

### 12. Add Requirements.txt to Finance Projects

**Impact**: Small but important infrastructure fix
**Estimated Time**: 30 minutes
**Difficulty**: ⭐ Easy

```
Add missing requirements.txt files to finance subprojects.

Context:
- Two projects missing requirements.txt:
  1. /home/user/self-learn/data-science/12_domain_applications/finance/klse-backtesting/
  2. /home/user/self-learn/data-science/12_domain_applications/finance/klse-stock-screener/
- README files exist for both
- Need to analyze code and create proper requirements

Tasks:
1. For klse-backtesting/:
   - Read all notebooks in the project
   - Identify all imported libraries
   - Create requirements.txt with pinned versions
   - Test installation in fresh virtualenv

2. For klse-stock-screener/:
   - Read all notebooks in the project
   - Identify all imported libraries
   - Create requirements.txt with pinned versions
   - Test installation in fresh virtualenv

3. Standard Requirements Format:
   ```
   # Core dependencies
   pandas==2.0.3
   numpy==1.24.3

   # Visualization
   matplotlib==3.7.2
   seaborn==0.12.2

   # Finance-specific
   yfinance==0.2.28
   ta-lib==0.4.28

   # Backtesting (if applicable)
   backtrader==1.9.78.123

   # Jupyter
   jupyter==1.0.0
   ipykernel==6.25.0
   ```

4. Commit message format:
   [Data-Science] Add: Requirements.txt for KLSE finance projects

This is a quick fix to ensure project completeness.
```

---

### 13. Add Tests to Major Projects

**Impact**: Improve code quality and reliability
**Estimated Time**: 3-4 hours total
**Difficulty**: ⭐⭐ Intermediate

```
Add comprehensive test coverage to major projects following the malaysia-stock pattern.

Context:
- malaysia-stock project has tests/ directory - use as template
- Target projects without tests:
  1. earn-money
  2. first-principle
  3. research-methodology
  4. projects/music-library-manager
- All are complete projects that need quality assurance

Requirements:
1. For each project, create tests/ directory with:
   - test_notebook_execution.py (run all notebooks)
   - test_quality_metrics.py (markdown ratio, exercise count)
   - test_data_paths.py (verify all paths are relative)
   - test_requirements.py (check dependencies installable)

2. Test Framework:
   ```python
   # Example structure
   import pytest
   import nbformat
   from nbconvert.preprocessors import ExecutePreprocessor

   def test_notebook_executes(notebook_path):
       """Test that notebook runs without errors"""
       with open(notebook_path) as f:
           nb = nbformat.read(f, as_version=4)

       ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
       ep.preprocess(nb, {'metadata': {'path': './'}})

       assert True  # If we get here, notebook executed

   def test_markdown_ratio(notebook_path):
       """Test that notebook has minimum 30% markdown"""
       # Implementation
       pass

   def test_has_learning_objectives(notebook_path):
       """Test that notebook has learning objectives"""
       # Implementation
       pass
   ```

3. Create GitHub Actions workflow:
   ```yaml
   name: Test Notebooks
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.10'
         - name: Install dependencies
           run: pip install -r requirements.txt
         - name: Run tests
           run: pytest tests/
   ```

4. Quality Standards:
   - All tests should pass
   - Include README in tests/ explaining test structure
   - Add pytest.ini configuration
   - Update main README with test badge

Focus on automated quality assurance for educational content.
```

---

## 🔵 LOW PRIORITY (Optional Enhancements)

### 14. Music Project - Create or Archive

**Impact**: Clean up empty placeholder
**Estimated Time**: 3-4 hours OR 5 minutes
**Difficulty**: ⭐⭐ Intermediate OR ⭐ Easy

**Option A: Create Music Theory/Production Project**
```
Create a comprehensive Music Theory and Production learning path.

Context:
- Location: /home/user/self-learn/music/
- Currently empty (only .gitkeep)
- Related to music-library-manager in projects/ folder
- Could complement that project

Requirements:
1. Create 10-12 sequential notebooks covering:
   - 00: Introduction to Music Theory Basics
   - 01: Notes, Scales, and Keys
   - 02: Chords and Harmony
   - 03: Rhythm and Time Signatures
   - 04: Music Analysis with Python (music21 library)
   - 05: Audio Signal Processing Basics
   - 06: MIDI Programming with Python
   - 07: Audio Synthesis and Effects
   - 08: Music Generation with AI
   - 09: Mixing and Mastering Concepts
   - 10: Final Project - Create a Song with Python

2. Technical Stack:
   - music21 for music theory
   - librosa for audio analysis
   - pydub for audio manipulation
   - mido for MIDI handling
   - numpy/scipy for DSP

3. Quality Standards:
   - Follow .claude/CLAUDE.md guidelines
   - Include audio examples
   - Interactive visualizations
   - Hands-on exercises

Focus on computational music analysis and creation.
```

**Option B: Archive the Directory**
```
Remove the empty music/ directory and update PROJECT_TRACKING.md.

Tasks:
1. Delete /home/user/self-learn/music/ directory
2. Update PROJECT_TRACKING.md to remove music from incomplete list
3. Update summary statistics
4. Commit with message: [Root] Remove: Empty music placeholder directory
```

**Recommendation**: Choose Option B (archive) unless you have specific interest in music theory/production.

---

### 15. N8N Project - Create or Archive

**Impact**: Clean up empty placeholder
**Estimated Time**: 3-4 hours OR 5 minutes
**Difficulty**: ⭐⭐ Intermediate OR ⭐ Easy

**Option A: Create Workflow Automation Project**
```
Create n8n workflow automation learning path.

Context:
- Location: /home/user/self-learn/n8n/
- Currently has empty docs/ directory
- n8n is a workflow automation tool (like Zapier)

Requirements:
1. Create 8-10 notebooks covering:
   - 00: Introduction to Workflow Automation
   - 01: n8n Setup and Configuration
   - 02: Building Your First Workflow
   - 03: API Integration Basics
   - 04: Data Transformation in n8n
   - 05: Conditional Logic and Branching
   - 06: Error Handling and Debugging
   - 07: Python Integration in n8n
   - 08: Practical Automation Projects
   - 09: Final Project - Multi-Step Automation

2. Focus Areas:
   - Practical workflow examples
   - Integration with common services
   - Python scripting within n8n
   - Best practices for automation

Note: This requires n8n installation (Docker or self-hosted).
```

**Option B: Archive the Directory**
```
Remove the empty n8n/ directory and update PROJECT_TRACKING.md.

Tasks:
1. Delete /home/user/self-learn/n8n/ directory
2. Update PROJECT_TRACKING.md
3. Commit: [Root] Remove: Empty n8n placeholder directory
```

**Recommendation**: Choose Option B (archive) unless you specifically need workflow automation training.

---

## Summary and Recommended Completion Order

### Phase 1: Critical ML Foundation (Week 1-2)
1. Module 05.1: Machine Learning Fundamentals ⏱️ 3-4h
2. Module 05.2: Feature Engineering ⏱️ 2-3h
3. Module 05.3: Ensemble Methods ⏱️ 2-3h

**Total: 7-10 hours | Impact: Completes critical ML learning path**

---

### Phase 2: Big Data & Production Skills (Week 3-4)
4. Module 08: Big Data with PySpark ⏱️ 3-4h
5. Module 09.1: MLOps and Deployment ⏱️ 3-4h
6. Module 09.2: Cloud Platforms ⏱️ 2-3h

**Total: 8-11 hours | Impact: Adds production ML and big data skills**

---

### Phase 3: Deep Learning Specialization (Week 5-6)
7. Module 06.1: Deep Learning Fundamentals ⏱️ 3-4h
8. Module 06.3: NLP and Transformers ⏱️ 3-4h

**Total: 6-8 hours | Impact: Completes deep learning track**

---

### Phase 4: Portfolio & Polish (Week 7-8)
9. Module 11: Portfolio Projects (Kaggle) ⏱️ 4-5h
10. Module 00.4: GitHub Learning ⏱️ 2-3h
11. English Project Reorganization ⏱️ 2-3h

**Total: 8-11 hours | Impact: Portfolio-ready projects**

---

### Phase 5: Quality & Cleanup (Week 9)
12. Add requirements.txt to finance projects ⏱️ 0.5h
13. Add tests to major projects ⏱️ 3-4h
14. Archive music/ and n8n/ directories ⏱️ 0.1h

**Total: 3.5-4.5 hours | Impact: Professional polish**

---

## Grand Total
**Estimated Time: 33-44 hours of focused work**
**Expected Completion: 8-10 weeks (at 4-5 hours/week)**

Upon completion, your portfolio will have:
- ✅ 100% complete ML/DL learning path
- ✅ Big data and MLOps skills
- ✅ Portfolio-ready Kaggle projects
- ✅ Production deployment knowledge
- ✅ Professional test coverage
- ✅ No incomplete placeholder directories

**Result**: A world-class, production-ready data science portfolio! 🚀

---

## Tips for Using These Prompts

1. **Start Fresh**: Each prompt is self-contained, open new Claude Code session
2. **One at a Time**: Complete one module before starting the next
3. **Review Quality**: Run notebook-tester after creation
4. **Commit Often**: Commit after each completed module
5. **Update Tracking**: Update PROJECT_TRACKING.md after each completion
6. **Test Execution**: Always run "Restart and Run All" before committing
7. **Ask Questions**: If Claude Code needs clarification, provide it
8. **Stay Consistent**: Reference .claude/CLAUDE.md in each prompt

Good luck with your learning journey! 🎓
