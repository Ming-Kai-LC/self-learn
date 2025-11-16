# Data Science Intermediate Track: Advanced ML & Deep Learning

**Welcome to the Advanced Track!** 🚀

If you've completed Modules 00-11 (Fundamentals), you're ready to level up your data science skills.

---

## Prerequisites

**You should have completed**:
- ✅ Module 00-03: Python, NumPy, Pandas basics
- ✅ Module 04-05: Data cleaning and EDA
- ✅ Module 06-07: Data visualization
- ✅ Module 08-11: Statistics and basic ML

**You should be comfortable with**:
- Python programming
- Pandas DataFrames manipulation
- Basic machine learning concepts
- Model training and evaluation

---

## What You'll Learn

This intermediate track takes you from **basic ML** to **production-ready ML/DL systems**.

### Phase 1: Advanced Machine Learning (Modules 12-15)
Master advanced ML techniques used in real-world projects:
- Feature engineering at scale
- Hyperparameter optimization
- Ensemble methods (XGBoost, LightGBM)
- Unsupervised learning and clustering

### Phase 2: Deep Learning Fundamentals (Modules 16-19)
Build neural networks from scratch and use modern frameworks:
- Neural networks from first principles
- Computer vision with CNNs
- Natural language processing
- Advanced deep learning techniques

### Phase 3: Real-World Applications (Modules 20-22)
Apply ML to real business problems:
- Time series forecasting
- Recommendation systems
- Model deployment (Flask, Docker, Streamlit)

### Phase 4: Capstone Projects (Modules 23-24)
Build portfolio-worthy projects:
- Kaggle competition strategies
- End-to-end ML project with deployment
- GitHub portfolio setup

---

## Learning Path

| Module | Topic | Time | Deliverable |
|--------|-------|------|-------------|
| **12** | Feature Engineering Mastery | 75 min | Feature engineering toolkit |
| **13** | Model Selection & Tuning | 75 min | Hyperparameter optimization pipeline |
| **14** | Ensemble Methods | 90 min | Kaggle competition submission |
| **15** | Unsupervised Learning | 75 min | Customer segmentation project |
| **16** | Neural Networks from Scratch | 90 min | NN implementation in NumPy |
| **17** | Computer Vision with CNNs | 90 min | Image classifier |
| **18** | Natural Language Processing | 90 min | Sentiment analyzer |
| **19** | Advanced Deep Learning | 90 min | Optimized DL model |
| **20** | Time Series Forecasting | 90 min | Sales forecasting system |
| **21** | Recommendation Systems | 75 min | Movie recommender |
| **22** | Model Deployment | 90 min | Deployed ML API |
| **23** | Kaggle Competition Strategy | 90 min | Competition entry |
| **24** | Final Portfolio Project | 120 min | Complete ML system |

**Total Learning Time**: ~18-20 hours

---

## Project Structure

```
data-science-fundamentals/
│
├── notebooks/
│   ├── 00-11_*.ipynb              # Fundamentals (completed)
│   └── advanced/                   # NEW: Intermediate modules
│       ├── 12_feature_engineering.ipynb
│       ├── 13_model_selection.ipynb
│       ├── 14_ensemble_methods.ipynb
│       ├── 15_unsupervised_learning.ipynb
│       ├── 16_neural_networks.ipynb
│       ├── 17_computer_vision.ipynb
│       ├── 18_nlp.ipynb
│       ├── 19_advanced_dl.ipynb
│       ├── 20_time_series.ipynb
│       ├── 21_recommendation_systems.ipynb
│       ├── 22_deployment.ipynb
│       ├── 23_kaggle_strategy.ipynb
│       └── 24_final_project.ipynb
│
├── data/                           # Original datasets
├── data_advanced/                  # NEW: Advanced datasets
│   ├── sales_timeseries.csv
│   ├── customer_reviews.csv
│   ├── images/                     # Image dataset
│   ├── movie_ratings.csv
│   └── sensor_data.csv
│
├── models/                         # NEW: Saved trained models
│   ├── best_model.pkl
│   └── neural_net.h5
│
├── deployments/                    # NEW: Deployment templates
│   ├── flask/                      # Flask API
│   └── streamlit/                  # Streamlit app
│
├── competitions/                   # NEW: Kaggle notebooks
│   ├── titanic_solution.ipynb
│   └── house_prices_solution.ipynb
│
└── papers/                         # NEW: Paper implementations
    ├── resnet_implementation.ipynb
    └── attention_mechanism.ipynb
```

---

## New Technologies & Libraries

You'll work with:

### Machine Learning
- **XGBoost**: Gradient boosting for competitions
- **LightGBM**: Fast gradient boosting
- **CatBoost**: Categorical feature boosting
- **Optuna**: Hyperparameter optimization

### Deep Learning
- **TensorFlow/Keras**: Neural network framework
- **PyTorch**: Alternative DL framework (basics)
- **Transformers**: Pre-trained models (Hugging Face)

### Deployment
- **Flask**: REST API for ML models
- **Streamlit**: Interactive web apps
- **Docker**: Containerization basics
- **Heroku/Railway**: Cloud deployment

### Utilities
- **SHAP**: Model interpretability
- **MLflow**: Experiment tracking
- **Weights & Biases**: Advanced tracking

---

## Installation

### Update Your Environment

```bash
# Activate your virtual environment
cd projects/data-science-fundamentals
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install advanced requirements
pip install -r requirements_intermediate.txt
```

### New Dependencies Include
- tensorflow>=2.13.0
- torch>=2.0.0
- xgboost>=2.0.0
- lightgbm>=4.0.0
- catboost>=1.2.0
- optuna>=3.3.0
- shap>=0.42.0
- mlflow>=2.7.0
- flask>=3.0.0
- streamlit>=1.28.0
- transformers>=4.30.0

---

## How to Use This Track

### Sequential Learning (Recommended)
1. Complete Modules 12-15 (Advanced ML)
2. Move to Modules 16-19 (Deep Learning)
3. Apply learning in Modules 20-22 (Real-World)
4. Showcase in Modules 23-24 (Portfolio)

### Project-Based Learning
Pick modules based on your project needs:
- Need deployment? → Module 22
- Building recommender? → Module 21
- Kaggle competition? → Module 14, 23
- Time series problem? → Module 20

### Career-Focused Path
For job applications:
1. Module 14 (Ensemble) + Module 23 (Kaggle) = Competition experience
2. Module 17 (CV) or Module 18 (NLP) = Specialized skill
3. Module 22 (Deployment) = Production experience
4. Module 24 (Portfolio) = Showcase project

---

## Portfolio Projects You'll Build

### 1. Customer Segmentation System (Module 15)
- K-means clustering on real customer data
- Visualization dashboard
- Business recommendations

### 2. Image Classifier (Module 17)
- CNN trained on custom dataset
- Transfer learning from ResNet
- Web interface for predictions

### 3. Sentiment Analyzer (Module 18)
- LSTM for customer reviews
- Real-time prediction API
- Deployment to cloud

### 4. Sales Forecasting System (Module 20)
- ARIMA + LSTM hybrid model
- Interactive forecast dashboard
- Business insights report

### 5. Movie Recommender (Module 21)
- Collaborative filtering
- Streamlit web app
- Personalized recommendations

### 6. End-to-End ML System (Module 24)
- Problem definition to deployment
- Full documentation
- GitHub repository showcase

---

## Success Tips

### 1. Build Your Portfolio
- Create GitHub repository for each project
- Write clear README files
- Include visualizations and results
- Show your thinking process

### 2. Participate in Kaggle
- Start with competitions in Module 23
- Learn from others' notebooks
- Climb the leaderboard
- Build competition experience

### 3. Deploy Your Models
- Don't just train models - deploy them
- Create APIs others can use
- Share Streamlit apps
- Get feedback

### 4. Implement Papers
- Read research papers (papers/ directory)
- Implement algorithms from scratch
- Compare with library implementations
- Deepen your understanding

### 5. Document Everything
- Write blog posts about projects
- Create tutorial notebooks
- Share on LinkedIn/Medium
- Build your brand

---

## Next Steps After Completion

### Advanced Topics to Explore
- **MLOps**: Kubeflow, Airflow, production pipelines
- **Advanced NLP**: BERT, GPT, transformers
- **Advanced CV**: Object detection, segmentation
- **Reinforcement Learning**: Q-learning, policy gradients
- **AutoML**: Neural architecture search
- **Big Data**: Spark, Dask for large-scale ML

### Career Advancement
- **Build portfolio**: 3-5 impressive projects
- **Contribute to open source**: Scikit-learn, TensorFlow
- **Write technical blogs**: Medium, personal blog
- **Network**: LinkedIn, Kaggle, local meetups
- **Apply for jobs**: You're ready for ML roles!

---

## Estimated Completion Timeline

### Intensive Track (2-3 weeks)
- 8-10 hours/week
- Focus on projects
- Complete all modules

### Balanced Track (1-2 months)
- 4-5 hours/week
- Deep learning + practice
- Build strong portfolio

### Part-Time Track (2-3 months)
- 2-3 hours/week
- Weekend projects
- Steady progress

---

## Support & Resources

### Getting Help
- **Main README**: Installation and basics
- **docs/README.md**: FAQ and troubleshooting
- **Module notebooks**: Detailed explanations
- **Stack Overflow**: Tag questions with 'machine-learning'
- **Kaggle Forums**: Community help

### Additional Resources
- **Fast.ai**: Practical deep learning course
- **Coursera**: Andrew Ng's ML course
- **Papers with Code**: Latest research implementations
- **Towards Data Science**: Articles and tutorials
- **YouTube**: 3Blue1Brown (neural networks), StatQuest

---

## Assessment

### Self-Evaluation Checklist

After completing this track, you should be able to:

**Advanced ML**:
- [ ] Engineer features from raw data
- [ ] Tune hyperparameters effectively
- [ ] Build ensemble models
- [ ] Perform clustering and dimensionality reduction

**Deep Learning**:
- [ ] Build neural networks from scratch
- [ ] Train CNNs for image tasks
- [ ] Process text with LSTMs
- [ ] Optimize deep learning models

**Production**:
- [ ] Deploy models as APIs
- [ ] Create web apps for ML models
- [ ] Use Docker for containerization
- [ ] Monitor model performance

**Portfolio**:
- [ ] Have 3-5 complete ML projects
- [ ] GitHub repository with clean code
- [ ] Deployed applications
- [ ] Kaggle competition experience

---

## Congratulations!

You're embarking on an exciting journey from **beginner** to **professional data scientist**.

This intermediate track will:
- ✅ Sharpen your ML skills
- ✅ Teach production-ready techniques
- ✅ Build your portfolio
- ✅ Prepare you for ML careers

**Ready to start?** Open `notebooks/advanced/12_feature_engineering.ipynb` and let's begin!

---

**Questions?** Check the main README or docs/ folder.

**Excited?** You should be - you're about to become a serious data scientist! 🚀📊🤖
