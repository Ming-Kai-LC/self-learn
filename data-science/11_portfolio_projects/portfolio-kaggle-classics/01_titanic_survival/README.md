# Titanic Survival Prediction

**Difficulty**: ⭐ Beginner
**Type**: Binary Classification
**Dataset**: Titanic (Seaborn/Kaggle)
**Estimated Time**: 20-25 hours

## Problem Statement

The sinking of the Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew.

**Goal**: Build a predictive model that answers: "What sorts of people were more likely to survive?" using passenger data (name, age, gender, socio-economic class, etc.).

## Dataset

- **Source**: Seaborn built-in dataset / Kaggle Titanic competition
- **Rows**: 891 passengers
- **Features**: 12+ features including demographics, cabin class, fare, family info

### Key Features
- `survived`: Target variable (0 = No, 1 = Yes)
- `pclass`: Passenger class (1st, 2nd, 3rd)
- `sex`: Gender
- `age`: Age in years
- `sibsp`: Number of siblings/spouses aboard
- `parch`: Number of parents/children aboard
- `fare`: Ticket fare
- `embarked`: Port of embarkation (C, Q, S)

## Approach

### 1. Exploratory Data Analysis
- Survival rate analysis by gender, class, age
- Missing value analysis (Age: 19.9%, Embarked: 0.2%, Deck: 77.2%)
- Correlation analysis
- Multi-dimensional analysis (gender + class combination)

### 2. Feature Engineering
- **family_size**: Total family members (sibsp + parch + 1)
- **is_alone**: Binary indicator for solo travelers
- **fare_per_person**: Fare divided by family size
- **age_category**: Age binned into categories (Child, Teen, Adult, etc.)

### 3. Data Preprocessing
- Missing value imputation (age by gender/class median, embarked by mode)
- Categorical encoding (sex: binary, embarked: one-hot)
- Feature scaling (StandardScaler for SVM, KNN, Logistic Regression)

### 4. Machine Learning Models
Trained and compared 6 classification algorithms:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

### 5. Model Evaluation
- Accuracy, Precision, Recall, F1 Score, ROC AUC
- Confusion Matrix
- ROC Curve comparison
- 5-Fold Cross-Validation
- Feature importance analysis

### 6. Hyperparameter Tuning
- Grid Search CV on Random Forest
- Optimized parameters: n_estimators, max_depth, min_samples_split, min_samples_leaf

## Results

### Key Findings

**Survival Patterns:**
- Overall survival rate: **38.4%**
- Female survival rate: **74.2%** vs Male: **18.9%**
- 1st class survival: **63.0%** vs 3rd class: **24.2%**
- Children (<12 years) had higher survival rates

**Model Performance:**
- Best model: Random Forest / Gradient Boosting
- Test accuracy: **~80-85%**
- Cross-validation accuracy: **~82%** (stable across folds)

**Most Important Features:**
1. Gender (sex_encoded) - Most predictive
2. Passenger class (pclass) - Strong indicator
3. Fare - Correlates with class
4. Age - Children prioritized
5. Family size - Extremes (alone or large families) had lower survival

### Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| Random Forest | ~0.83 | ~0.81 | ~0.77 | ~0.79 | ~0.87 |
| Gradient Boosting | ~0.82 | ~0.80 | ~0.76 | ~0.78 | ~0.86 |
| Logistic Regression | ~0.80 | ~0.78 | ~0.73 | ~0.75 | ~0.84 |
| SVM | ~0.79 | ~0.77 | ~0.72 | ~0.74 | ~0.83 |
| KNN | ~0.77 | ~0.74 | ~0.70 | ~0.72 | ~0.80 |
| Decision Tree | ~0.76 | ~0.72 | ~0.68 | ~0.70 | ~0.78 |

*Note: Exact values depend on random seed and data split*

## Technologies Used

- **Python 3.8+**
- **Data Manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn
- **Environment**: Jupyter Notebook

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run the Notebook
```bash
jupyter notebook titanic_survival_prediction.ipynb
```

### Run Cells
Execute cells sequentially from top to bottom. The notebook is self-contained and uses seaborn's built-in Titanic dataset (no download required).

## Project Structure

```
01_titanic_survival/
├── titanic_survival_prediction.ipynb  # Main analysis notebook
├── README.md                           # This file
└── requirements.txt                    # Python dependencies
```

## Key Insights

1. **Gender Bias**: The "women and children first" protocol was clearly followed - women had 4x higher survival rate than men.

2. **Class Matters**: Socioeconomic status strongly influenced survival. 1st class passengers had priority access to lifeboats.

3. **Age Effect**: Children were prioritized for rescue, reflected in higher survival rates for younger passengers.

4. **Family Dynamics**: Traveling alone reduced survival chances, but very large families also struggled (couldn't evacuate together).

5. **Model Simplicity**: Simple models (Logistic Regression) performed surprisingly well, suggesting the relationships are relatively linear.

## Next Steps

### Potential Improvements
1. **Title Extraction**: Extract titles (Mr., Mrs., Master) from names - these encode age/gender/status
2. **Cabin Deck**: Parse cabin numbers to extract deck information (proximity to lifeboats)
3. **Interaction Features**: sex * class, age * class interactions
4. **Advanced Ensembles**: Stacking, blending, XGBoost, LightGBM
5. **SHAP Analysis**: Explain individual predictions
6. **Deployment**: Create Streamlit web app for interactive predictions

### For Portfolio
- [ ] Add professional visualizations
- [ ] Create presentation slides
- [ ] Write blog post
- [ ] Deploy as web app
- [ ] Add to portfolio website

## Learning Objectives Achieved

✅ Comprehensive exploratory data analysis (EDA)
✅ Missing value handling strategies
✅ Feature engineering from domain knowledge
✅ Multiple classification algorithms comparison
✅ Model evaluation with appropriate metrics
✅ Hyperparameter tuning with GridSearchCV
✅ Cross-validation for model stability
✅ Feature importance interpretation
✅ Professional project documentation

## References

- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- [Seaborn Titanic Dataset](https://github.com/mwaskom/seaborn-data)
- Scikit-learn documentation
- "Hands-On Machine Learning" by Aurélien Géron

## Author

Created as part of the Data Science Portfolio Projects series.

## License

This project is for educational purposes.
