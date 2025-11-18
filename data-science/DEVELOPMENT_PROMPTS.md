# Data Science Development Prompts

**Purpose**: Use these prompts to parallelize development across multiple Claude Code sessions.

**Instructions**:
1. Copy the relevant prompt below
2. Start a new Claude Code session
3. Paste the prompt to begin development
4. Each session will work independently on different folders

---

## 🔥 HIGHEST PRIORITY - Machine Learning

### Prompt 1: ML Fundamentals (Part 1 - Regression & Classification)

```
I need you to develop Machine Learning fundamentals notebooks for the data-science project.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards and guidelines
- Location: /home/user/self-learn/data-science/05_machine_learning/

**Your Task**:
Create notebooks for ML Fundamentals covering:

1. **Linear Regression** (3 notebooks):
   - Module 00: Introduction to ML and Linear Regression (⭐)
   - Module 01: Multiple Linear Regression (⭐⭐)
   - Module 02: Polynomial Regression and Regularization (⭐⭐)

2. **Logistic Regression** (3 notebooks):
   - Module 03: Binary Classification with Logistic Regression (⭐)
   - Module 04: Multiclass Classification (⭐⭐)
   - Module 05: Advanced Logistic Regression (⭐⭐⭐)

**Requirements**:
- Follow notebook quality standards (≥30% markdown, ≥3 exercises per concept)
- Use sample datasets (add to data/sample/ if needed, <10MB)
- Include visualizations for all concepts
- Progressive difficulty (⭐ to ⭐⭐⭐)
- Test all notebooks ("Restart and Run All")
- Create README.md for the ml-fundamentals subfolder

**Deliverables**:
- 6 complete, tested notebooks
- README.md with learning path
- requirements.txt with dependencies
- Sample data files (if needed)

**Commit Message Format**: [Data-Science-ML] Add: Linear and Logistic Regression modules

Work on branch: claude/ml-fundamentals-regression-[SESSION_ID]
When done, commit and push your changes.
```

---

### Prompt 2: ML Fundamentals (Part 2 - Tree-Based Models)

```
I need you to develop Machine Learning tree-based model notebooks for the data-science project.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/05_machine_learning/

**Your Task**:
Create notebooks for tree-based ML algorithms:

1. **Decision Trees** (3 notebooks):
   - Module 06: Introduction to Decision Trees (⭐)
   - Module 07: Tree Pruning and Hyperparameters (⭐⭐)
   - Module 08: Regression Trees (⭐⭐)

2. **Random Forests** (3 notebooks):
   - Module 09: Introduction to Random Forests (⭐)
   - Module 10: Feature Importance and Selection (⭐⭐)
   - Module 11: Advanced Random Forest Techniques (⭐⭐⭐)

**Requirements**:
- Follow notebook quality standards (≥30% markdown, ≥3 exercises)
- Include decision tree visualizations
- Feature importance plots
- Comparison with linear models
- Real-world datasets (classification and regression)
- Test all notebooks

**Deliverables**:
- 6 complete notebooks
- Sample datasets with tree visualization examples
- README section for tree-based methods

**Commit Message Format**: [Data-Science-ML] Add: Decision Trees and Random Forests modules

Work on branch: claude/ml-fundamentals-trees-[SESSION_ID]
```

---

### Prompt 3: ML Fundamentals (Part 3 - Other Algorithms)

```
I need you to develop notebooks for SVM, KNN, and Naive Bayes algorithms.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/05_machine_learning/

**Your Task**:
Create notebooks covering:

1. **Support Vector Machines** (3 notebooks):
   - Module 12: Introduction to SVM (⭐)
   - Module 13: Kernel Tricks and Non-linear SVM (⭐⭐)
   - Module 14: SVM for Multi-class Classification (⭐⭐⭐)

2. **K-Nearest Neighbors** (2 notebooks):
   - Module 15: KNN for Classification and Regression (⭐)
   - Module 16: Distance Metrics and Optimization (⭐⭐)

3. **Naive Bayes** (2 notebooks):
   - Module 17: Probability Theory and Naive Bayes (⭐)
   - Module 18: Text Classification with Naive Bayes (⭐⭐)

**Requirements**:
- Visual explanations of decision boundaries
- Comparison of different algorithms
- When to use each algorithm (decision guide)
- Real-world applications
- Test all notebooks

**Deliverables**:
- 7 complete notebooks
- Algorithm comparison guide
- Sample datasets for each algorithm type

**Commit Message Format**: [Data-Science-ML] Add: SVM, KNN, and Naive Bayes modules

Work on branch: claude/ml-fundamentals-algorithms-[SESSION_ID]
```

---

### Prompt 4: ML Model Evaluation & Validation

```
I need you to develop notebooks covering model evaluation, validation, and hyperparameter tuning.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/05_machine_learning/

**Your Task**:
Create comprehensive evaluation and validation notebooks:

1. **Model Evaluation** (3 notebooks):
   - Module 19: Classification Metrics (Accuracy, Precision, Recall, F1) (⭐)
   - Module 20: Regression Metrics (MSE, RMSE, R², MAE) (⭐)
   - Module 21: ROC Curves and AUC (⭐⭐)

2. **Cross-Validation** (3 notebooks):
   - Module 22: Train-Test Split and Validation Sets (⭐)
   - Module 23: K-Fold Cross-Validation (⭐⭐)
   - Module 24: Stratified and Time-Series CV (⭐⭐⭐)

3. **Hyperparameter Tuning** (3 notebooks):
   - Module 25: Grid Search (⭐⭐)
   - Module 26: Random Search and Bayesian Optimization (⭐⭐⭐)
   - Module 27: Best Practices and Avoiding Overfitting (⭐⭐⭐)

**Requirements**:
- Visual confusion matrices
- Learning curves
- Validation curves
- Practical examples with multiple algorithms
- Common pitfalls and solutions

**Deliverables**:
- 9 complete notebooks
- Evaluation metrics cheat sheet
- Complete ML fundamentals README

**Commit Message Format**: [Data-Science-ML] Add: Model evaluation and validation modules

Work on branch: claude/ml-evaluation-validation-[SESSION_ID]
```

---

### Prompt 5: ML Ensemble Methods

```
I need you to develop notebooks for ensemble learning methods.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/05_machine_learning/ensemble-methods/

**Your Task**:
Create ensemble methods notebooks:

1. **Bagging and Boosting Fundamentals** (3 notebooks):
   - Module 00: Introduction to Ensemble Learning (⭐)
   - Module 01: Bagging and Bootstrap Aggregating (⭐⭐)
   - Module 02: AdaBoost (⭐⭐)

2. **Gradient Boosting** (4 notebooks):
   - Module 03: Gradient Boosting Fundamentals (⭐⭐)
   - Module 04: XGBoost (⭐⭐⭐)
   - Module 05: LightGBM (⭐⭐⭐)
   - Module 06: CatBoost (⭐⭐⭐)

3. **Stacking and Blending** (3 notebooks):
   - Module 07: Model Stacking (⭐⭐⭐)
   - Module 08: Blending Techniques (⭐⭐⭐)
   - Module 09: Ensemble Best Practices (⭐⭐⭐)

**Requirements**:
- Compare ensemble vs single models
- Hyperparameter tuning for each method
- Feature importance analysis
- Kaggle competition examples
- Performance benchmarks

**Deliverables**:
- 10 complete notebooks
- Ensemble methods comparison guide
- README for ensemble-methods subfolder

**Commit Message Format**: [Data-Science-ML] Add: Ensemble methods (Bagging, Boosting, Stacking)

Work on branch: claude/ml-ensemble-methods-[SESSION_ID]
```

---

### Prompt 6: ML Feature Engineering

```
I need you to develop notebooks for feature engineering techniques.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/05_machine_learning/feature-engineering/

**Your Task**:
Create feature engineering notebooks:

1. **Feature Selection** (4 notebooks):
   - Module 00: Introduction to Feature Engineering (⭐)
   - Module 01: Filter Methods (Correlation, Chi-Square) (⭐)
   - Module 02: Wrapper Methods (RFE, Forward/Backward Selection) (⭐⭐)
   - Module 03: Embedded Methods (Lasso, Tree-based) (⭐⭐)

2. **Feature Extraction** (4 notebooks):
   - Module 04: Principal Component Analysis (PCA) (⭐⭐)
   - Module 05: Linear Discriminant Analysis (LDA) (⭐⭐)
   - Module 06: t-SNE and UMAP (⭐⭐⭐)
   - Module 07: Autoencoders for Feature Learning (⭐⭐⭐)

3. **Encoding and Transformation** (4 notebooks):
   - Module 08: Categorical Encoding (One-Hot, Label, Target) (⭐)
   - Module 09: Numerical Transformations (Scaling, Normalization) (⭐)
   - Module 10: Feature Crosses and Interactions (⭐⭐)
   - Module 11: Advanced Feature Engineering Pipeline (⭐⭐⭐)

**Requirements**:
- Before/after comparisons
- Impact on model performance
- Visualization of dimensionality reduction
- Practical pipeline examples
- Common pitfalls and solutions

**Deliverables**:
- 12 complete notebooks
- Feature engineering workflow guide
- README for feature-engineering subfolder

**Commit Message Format**: [Data-Science-ML] Add: Feature engineering techniques

Work on branch: claude/ml-feature-engineering-[SESSION_ID]
```

---

## 🔥 HIGH PRIORITY - Deep Learning Gaps

### Prompt 7: Deep Learning Fundamentals

```
I need you to fill critical gaps in deep learning by creating fundamentals notebooks.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/06_deep_learning/
- Note: CNN module already exists, focus on fundamentals

**Your Task**:
Create deep learning fundamentals notebooks:

1. **Neural Network Basics** (4 notebooks):
   - Module 00: Introduction to Neural Networks (⭐)
   - Module 01: Perceptrons and Activation Functions (⭐)
   - Module 02: Forward Propagation (⭐⭐)
   - Module 03: Backpropagation and Gradient Descent (⭐⭐)

2. **Training Neural Networks** (4 notebooks):
   - Module 04: Loss Functions and Optimizers (⭐⭐)
   - Module 05: Regularization (Dropout, L1/L2) (⭐⭐)
   - Module 06: Batch Normalization and Layer Normalization (⭐⭐⭐)
   - Module 07: Learning Rate Schedules and Advanced Optimizers (⭐⭐⭐)

3. **Deep Learning Architectures** (3 notebooks):
   - Module 08: Fully Connected Networks (⭐)
   - Module 09: Model Design Patterns (⭐⭐)
   - Module 10: Transfer Learning Fundamentals (⭐⭐)

**Requirements**:
- Visual explanations of concepts (network diagrams, gradient flow)
- Code from scratch (understand internals)
- PyTorch and/or TensorFlow implementations
- Training visualizations (loss curves, accuracy)
- Practical examples with real datasets

**Deliverables**:
- 11 complete notebooks
- Deep learning fundamentals README
- Model training best practices guide

**Commit Message Format**: [Data-Science-DL] Add: Deep learning fundamentals modules

Work on branch: claude/dl-fundamentals-[SESSION_ID]
```

---

### Prompt 8: NLP and Transformers

```
I need you to develop NLP and transformer notebooks for deep learning.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/06_deep_learning/
- CNN already exists, add NLP alongside it

**Your Task**:
Create NLP and transformer notebooks:

1. **RNN and LSTM** (4 notebooks):
   - Module 11: Introduction to RNN (⭐)
   - Module 12: LSTM and GRU (⭐⭐)
   - Module 13: Bidirectional RNN (⭐⭐)
   - Module 14: Sequence-to-Sequence Models (⭐⭐⭐)

2. **Attention Mechanisms** (3 notebooks):
   - Module 15: Attention Mechanism Fundamentals (⭐⭐)
   - Module 16: Self-Attention (⭐⭐)
   - Module 17: Multi-Head Attention (⭐⭐⭐)

3. **Transformers** (5 notebooks):
   - Module 18: Transformer Architecture (⭐⭐)
   - Module 19: BERT for Text Classification (⭐⭐⭐)
   - Module 20: GPT and Text Generation (⭐⭐⭐)
   - Module 21: Fine-tuning Pre-trained Models (⭐⭐⭐)
   - Module 22: Hugging Face Transformers Library (⭐⭐)

**Requirements**:
- Attention visualization
- Text preprocessing pipelines
- Pre-trained model usage
- Fine-tuning examples
- NLP tasks: classification, generation, QA
- Use small datasets for quick training

**Deliverables**:
- 12 complete notebooks
- NLP/Transformers README section
- Pre-trained model usage guide

**Commit Message Format**: [Data-Science-DL] Add: NLP, RNN, LSTM, and Transformers modules

Work on branch: claude/dl-nlp-transformers-[SESSION_ID]
```

---

## 🔥 HIGH PRIORITY - MLOps and Deployment

### Prompt 9: MLOps - Docker and Containerization

```
I need you to develop MLOps notebooks focusing on Docker and containerization.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/09_mlops_deployment/

**Your Task**:
Create Docker and containerization notebooks:

1. **Docker Fundamentals** (4 notebooks):
   - Module 00: Introduction to Docker and Containers (⭐)
   - Module 01: Dockerfile and Building Images (⭐)
   - Module 02: Docker Compose for Multi-Container Apps (⭐⭐)
   - Module 03: Docker Best Practices for ML (⭐⭐)

2. **Containerizing ML Models** (4 notebooks):
   - Module 04: Packaging ML Models with Docker (⭐⭐)
   - Module 05: Creating ML APIs with FastAPI (⭐⭐)
   - Module 06: Flask for Model Deployment (⭐⭐)
   - Module 07: Optimizing Container Size and Performance (⭐⭐⭐)

**Requirements**:
- Working Dockerfiles for ML projects
- API endpoints for model inference
- Example requests and responses
- Testing containerized applications
- Security best practices

**Deliverables**:
- 8 complete notebooks
- Sample Dockerfiles and docker-compose.yml
- API deployment examples
- README for containerization section

**Commit Message Format**: [Data-Science-MLOps] Add: Docker and containerization modules

Work on branch: claude/mlops-docker-[SESSION_ID]
```

---

### Prompt 10: MLOps - Experiment Tracking and Model Registry

```
I need you to develop MLOps notebooks for experiment tracking and model management.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/09_mlops_deployment/

**Your Task**:
Create experiment tracking and model registry notebooks:

1. **MLflow** (5 notebooks):
   - Module 08: Introduction to MLflow (⭐)
   - Module 09: MLflow Tracking (Logging Metrics, Parameters) (⭐⭐)
   - Module 10: MLflow Projects (⭐⭐)
   - Module 11: MLflow Models and Registry (⭐⭐⭐)
   - Module 12: MLflow Deployment (⭐⭐⭐)

2. **Weights & Biases** (3 notebooks):
   - Module 13: W&B for Experiment Tracking (⭐⭐)
   - Module 14: Hyperparameter Sweeps with W&B (⭐⭐⭐)
   - Module 15: Model Registry and Versioning (⭐⭐)

3. **DVC (Data Version Control)** (2 notebooks):
   - Module 16: Version Control for Data and Models (⭐⭐)
   - Module 17: DVC Pipelines (⭐⭐⭐)

**Requirements**:
- Compare different tracking tools
- Real experiment tracking examples
- Model versioning workflows
- Reproducibility best practices

**Deliverables**:
- 10 complete notebooks
- MLflow setup guide
- Experiment tracking best practices

**Commit Message Format**: [Data-Science-MLOps] Add: MLflow, W&B, and DVC modules

Work on branch: claude/mlops-tracking-[SESSION_ID]
```

---

### Prompt 11: MLOps - CI/CD and Production Deployment

```
I need you to develop MLOps notebooks for CI/CD and production deployment.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/09_mlops_deployment/

**Your Task**:
Create CI/CD and deployment notebooks:

1. **CI/CD for ML** (4 notebooks):
   - Module 18: Introduction to CI/CD for ML (⭐)
   - Module 19: GitHub Actions for ML Workflows (⭐⭐)
   - Module 20: Automated Testing for ML Models (⭐⭐)
   - Module 21: Continuous Training Pipelines (⭐⭐⭐)

2. **Kubernetes for ML** (4 notebooks):
   - Module 22: Kubernetes Fundamentals (⭐⭐)
   - Module 23: Deploying ML Models to Kubernetes (⭐⭐⭐)
   - Module 24: KServe/Seldon for Model Serving (⭐⭐⭐)
   - Module 25: Scaling and Load Balancing (⭐⭐⭐)

3. **Monitoring and Observability** (3 notebooks):
   - Module 26: Model Monitoring and Drift Detection (⭐⭐)
   - Module 27: Logging and Alerting (⭐⭐)
   - Module 28: A/B Testing and Canary Deployments (⭐⭐⭐)

**Requirements**:
- Working CI/CD pipelines
- Kubernetes deployment manifests
- Monitoring dashboards
- Production best practices
- Cost optimization strategies

**Deliverables**:
- 11 complete notebooks
- CI/CD pipeline templates
- Kubernetes deployment examples
- Complete MLOps README

**Commit Message Format**: [Data-Science-MLOps] Add: CI/CD, Kubernetes, and monitoring modules

Work on branch: claude/mlops-cicd-deployment-[SESSION_ID]
```

---

## 🔥 HIGH PRIORITY - Portfolio Projects

### Prompt 12: Portfolio Projects - Beginner Level (⭐)

```
I need you to create beginner-level portfolio projects showcasing fundamental ML skills.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/11_portfolio_projects/

**Your Task**:
Create 3-4 beginner portfolio projects (⭐ difficulty):

1. **Project 01: Iris Classification** (⭐)
   - Multi-class classification
   - EDA, visualization, basic ML models
   - Model comparison and evaluation

2. **Project 02: House Price Prediction** (⭐)
   - Regression problem
   - Feature engineering basics
   - Linear regression and tree-based models

3. **Project 03: Customer Segmentation** (⭐)
   - Clustering with K-Means
   - Visualization of segments
   - Business insights

4. **Project 04: Sentiment Analysis** (⭐)
   - Text classification
   - Basic NLP preprocessing
   - Logistic regression or Naive Bayes

**Requirements**:
- End-to-end ML pipeline (data → model → evaluation)
- Clear business problem statement
- Visualizations and insights
- Model deployment code (simple API)
- Complete documentation
- Professional presentation

**Deliverables**:
- 3-4 complete project notebooks
- README for each project
- Sample datasets
- Deployment examples

**Commit Message Format**: [Data-Science-Portfolio] Add: Beginner-level projects (⭐)

Work on branch: claude/portfolio-beginner-[SESSION_ID]
```

---

### Prompt 13: Portfolio Projects - Intermediate Level (⭐⭐)

```
I need you to create intermediate-level portfolio projects showcasing advanced ML techniques.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/11_portfolio_projects/

**Your Task**:
Create 3-4 intermediate portfolio projects (⭐⭐ difficulty):

1. **Project 05: Credit Card Fraud Detection** (⭐⭐)
   - Imbalanced classification
   - Anomaly detection techniques
   - Ensemble methods (XGBoost, Random Forest)
   - Performance on imbalanced data

2. **Project 06: Movie Recommendation System** (⭐⭐)
   - Collaborative filtering
   - Content-based filtering
   - Hybrid approaches
   - Evaluation metrics for recommenders

3. **Project 07: Time Series Forecasting** (⭐⭐)
   - Stock price or sales forecasting
   - ARIMA, SARIMA, Prophet
   - Feature engineering for time series
   - Walk-forward validation

4. **Project 08: Image Classification with CNN** (⭐⭐)
   - CNN architecture design
   - Transfer learning (ResNet, VGG)
   - Data augmentation
   - Model interpretation (Grad-CAM)

**Requirements**:
- Complex data preprocessing
- Advanced feature engineering
- Multiple modeling approaches
- Hyperparameter tuning
- Model interpretation
- Deployment-ready code

**Deliverables**:
- 3-4 complete project notebooks
- Detailed README for each
- Model comparison analysis
- Deployment examples with API

**Commit Message Format**: [Data-Science-Portfolio] Add: Intermediate-level projects (⭐⭐)

Work on branch: claude/portfolio-intermediate-[SESSION_ID]
```

---

### Prompt 14: Portfolio Projects - Advanced Level (⭐⭐⭐)

```
I need you to create advanced-level portfolio projects showcasing expert ML/DL skills.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Read /home/user/self-learn/.claude/CLAUDE.md for quality standards
- Location: /home/user/self-learn/data-science/11_portfolio_projects/

**Your Task**:
Create 3-4 advanced portfolio projects (⭐⭐⭐ difficulty):

1. **Project 09: NLP Question Answering System** (⭐⭐⭐)
   - Fine-tuned BERT/RoBERTa
   - Custom dataset creation
   - Attention visualization
   - Production-ready API with caching

2. **Project 10: Object Detection and Segmentation** (⭐⭐⭐)
   - YOLO or Faster R-CNN
   - Instance segmentation (Mask R-CNN)
   - Real-time inference optimization
   - Deployment to edge devices

3. **Project 11: Kaggle Competition Solution** (⭐⭐⭐)
   - Full competition pipeline
   - Advanced ensemble techniques
   - Feature engineering creativity
   - Model stacking and blending
   - Detailed solution writeup

4. **Project 12: End-to-End MLOps Pipeline** (⭐⭐⭐)
   - CI/CD with GitHub Actions
   - MLflow experiment tracking
   - Docker containerization
   - Kubernetes deployment
   - Monitoring and alerting
   - A/B testing framework

**Requirements**:
- Production-quality code
- Comprehensive documentation
- Reproducible results
- Performance benchmarks
- Scalability considerations
- Security best practices

**Deliverables**:
- 3-4 complete advanced projects
- Detailed architecture documentation
- Deployment guides
- Performance reports
- Complete portfolio README

**Commit Message Format**: [Data-Science-Portfolio] Add: Advanced-level projects (⭐⭐⭐)

Work on branch: claude/portfolio-advanced-[SESSION_ID]
```

---

## MEDIUM PRIORITY - Expansion Projects

### Prompt 15: Mathematics - Advanced Topics

```
I need you to expand the mathematics folder with advanced topics.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Current: 8 notebooks covering basics
- Location: /home/user/self-learn/data-science/01_mathematics/

**Your Task**:
Add advanced mathematics notebooks:

1. **Advanced Probability** (3 notebooks):
   - Module 09: Probability Distributions (⭐⭐)
   - Module 10: Bayesian Statistics (⭐⭐⭐)
   - Module 11: Markov Chains and Monte Carlo (⭐⭐⭐)

2. **Advanced Linear Algebra** (3 notebooks):
   - Module 12: Matrix Decompositions (SVD, QR) (⭐⭐)
   - Module 13: Eigenvalues and Eigenvectors (⭐⭐)
   - Module 14: Linear Algebra for ML (⭐⭐⭐)

3. **Optimization** (3 notebooks):
   - Module 15: Convex Optimization (⭐⭐)
   - Module 16: Gradient-Based Optimization (⭐⭐)
   - Module 17: Constrained Optimization (⭐⭐⭐)

**Deliverables**:
- 9 additional notebooks
- Updated mathematics README
- Visualization-heavy explanations

**Commit Message Format**: [Data-Science-Math] Add: Advanced probability, linear algebra, and optimization

Work on branch: claude/math-advanced-[SESSION_ID]
```

---

### Prompt 16: Visualization - Advanced Techniques

```
I need you to expand visualization folder with advanced techniques.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Current: 8 notebooks covering basics
- Location: /home/user/self-learn/data-science/03_visualization/

**Your Task**:
Add advanced visualization notebooks:

1. **Advanced Plotly** (4 notebooks):
   - Module 09: 3D Visualizations (⭐⭐)
   - Module 10: Animated Visualizations (⭐⭐)
   - Module 11: Interactive Dashboards with Dash (⭐⭐⭐)
   - Module 12: Custom Plotly Components (⭐⭐⭐)

2. **Geographic Visualizations** (3 notebooks):
   - Module 13: Maps with Folium (⭐⭐)
   - Module 14: Choropleth Maps (⭐⭐)
   - Module 15: Geospatial Data with GeoPandas (⭐⭐⭐)

3. **Advanced Techniques** (3 notebooks):
   - Module 16: Custom Styling and Themes (⭐⭐)
   - Module 17: Network Visualizations (⭐⭐)
   - Module 18: Real-time Data Visualization (⭐⭐⭐)

**Deliverables**:
- 10 additional notebooks
- Interactive examples
- Updated visualization README

**Commit Message Format**: [Data-Science-Viz] Add: Advanced Plotly, maps, and custom visualizations

Work on branch: claude/viz-advanced-[SESSION_ID]
```

---

### Prompt 17: Computer Vision - Advanced Techniques

```
I need you to expand computer vision folder with advanced CV and deep learning.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Current: 10 notebooks with OpenCV basics
- Location: /home/user/self-learn/data-science/07_computer_vision/

**Your Task**:
Add advanced computer vision notebooks:

1. **Object Detection** (4 notebooks):
   - Module 11: Introduction to Object Detection (⭐⭐)
   - Module 12: YOLO Implementation (⭐⭐⭐)
   - Module 13: Faster R-CNN (⭐⭐⭐)
   - Module 14: Real-time Object Detection (⭐⭐⭐)

2. **Segmentation** (3 notebooks):
   - Module 15: Semantic Segmentation (U-Net) (⭐⭐⭐)
   - Module 16: Instance Segmentation (Mask R-CNN) (⭐⭐⭐)
   - Module 17: Panoptic Segmentation (⭐⭐⭐)

3. **Advanced Applications** (3 notebooks):
   - Module 18: Face Recognition Systems (⭐⭐)
   - Module 19: Video Processing and Tracking (⭐⭐⭐)
   - Module 20: Generative Models (GANs for Images) (⭐⭐⭐)

**Deliverables**:
- 10 additional notebooks
- Pre-trained model examples
- Real-time demo applications
- Updated CV README

**Commit Message Format**: [Data-Science-CV] Add: Object detection, segmentation, and advanced CV

Work on branch: claude/cv-advanced-[SESSION_ID]
```

---

### Prompt 18: Big Data - PySpark Development

```
I need you to develop the complete big data folder focusing on PySpark.

**Context**:
- Read /home/user/self-learn/data-science/COMPLETION_STATUS.md for project status
- Currently empty (0 notebooks)
- Location: /home/user/self-learn/data-science/08_big_data/

**Your Task**:
Create comprehensive PySpark notebooks:

1. **PySpark Fundamentals** (5 notebooks):
   - Module 00: Introduction to Big Data and Spark (⭐)
   - Module 01: PySpark Setup and RDDs (⭐)
   - Module 02: DataFrames and Datasets (⭐⭐)
   - Module 03: Spark SQL (⭐⭐)
   - Module 04: Data Transformations and Actions (⭐⭐)

2. **PySpark ML** (5 notebooks):
   - Module 05: MLlib Introduction (⭐⭐)
   - Module 06: Classification with PySpark (⭐⭐)
   - Module 07: Regression with PySpark (⭐⭐)
   - Module 08: Clustering with PySpark (⭐⭐⭐)
   - Module 09: Pipeline and Model Persistence (⭐⭐⭐)

3. **Advanced Spark** (5 notebooks):
   - Module 10: Spark Streaming (⭐⭐⭐)
   - Module 11: Performance Tuning (⭐⭐⭐)
   - Module 12: GraphX for Graph Processing (⭐⭐⭐)
   - Module 13: Delta Lake (⭐⭐⭐)
   - Module 14: Spark on Cloud (AWS/GCP/Azure) (⭐⭐⭐)

**Requirements**:
- Use sample datasets appropriate for big data scenarios
- Performance comparisons with pandas
- Best practices for distributed computing
- Real-world use cases

**Deliverables**:
- 15 complete notebooks
- Big data README
- Setup guides for local and cloud Spark
- Sample datasets

**Commit Message Format**: [Data-Science-BigData] Add: Complete PySpark fundamentals and advanced topics

Work on branch: claude/bigdata-pyspark-[SESSION_ID]
```

---

## Usage Instructions

### For Single Session Development:
1. Choose one prompt from above
2. Copy the entire prompt block
3. Start new Claude Code session
4. Paste and start working

### For Parallel Development:
1. Start multiple Claude Code sessions
2. Assign different prompts to each session
3. Each session works independently
4. Merge results when all complete

### Branch Naming:
- Replace `[SESSION_ID]` with your Claude Code session ID
- Example: `claude/ml-fundamentals-regression-01ABC123def`

### After Completion:
1. Each session should commit and push to its branch
2. Review all branches
3. Merge to main branch when satisfied
4. Update COMPLETION_STATUS.md

---

## Priority Order for Development

**If doing sequentially, follow this order**:

1. ⚡ **Prompts 1-4**: ML Fundamentals (foundation for everything)
2. ⚡ **Prompt 5**: ML Ensemble Methods (essential ML skill)
3. ⚡ **Prompt 6**: Feature Engineering (practical ML skill)
4. ⚡ **Prompt 7**: Deep Learning Fundamentals (DL foundation)
5. ⚡ **Prompt 8**: NLP and Transformers (modern DL)
6. ⚡ **Prompts 9-11**: MLOps (production skills)
7. ⚡ **Prompts 12-14**: Portfolio Projects (showcase skills)
8. 📊 **Prompts 15-18**: Expansion topics (as needed)

**If doing in parallel, group by**:
- **ML Track**: Prompts 1-6
- **DL Track**: Prompts 7-8
- **MLOps Track**: Prompts 9-11
- **Portfolio Track**: Prompts 12-14
- **Expansion Track**: Prompts 15-18

---

**Total Prompts**: 18 specialized development prompts
**Estimated Total Time**: 400-500 hours of development
**Target Output**: ~200-250 additional notebooks

Good luck with the development! 🚀
