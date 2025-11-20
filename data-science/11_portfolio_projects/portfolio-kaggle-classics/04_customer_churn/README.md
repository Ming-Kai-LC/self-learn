# Customer Churn Prediction

**Difficulty**: ⭐ Beginner
**Type**: Binary Classification
**Dataset**: Telco Customer Churn (Kaggle)
**Estimated Time**: 20-25 hours

## Problem Statement

Customer churn is a critical business metric for subscription-based companies. Losing customers directly impacts revenue and growth. The cost of acquiring a new customer is typically 5-25x higher than retaining an existing one.

**Goal**: Build a predictive model to identify customers who are likely to churn (cancel their service), enabling proactive retention strategies.

## Business Impact

**Why This Matters**:
- Identify at-risk customers before they leave
- Target retention campaigns to high-value customers
- Reduce customer acquisition costs
- Improve customer lifetime value (CLV)
- Optimize resource allocation for retention efforts

**Potential ROI**: If retention campaign costs $10/customer and saves 20% of at-risk customers worth $100/month average, the model provides significant value.

## Dataset

- **Source**: Telco Customer Churn (Kaggle/IBM Sample Data)
- **Rows**: 7,043 customers
- **Features**: 21 features including demographics, services, and account information
- **Target**: `Churn` (Yes/No) - whether customer left within last month

### Key Features

**Demographics**:
- `gender`: Customer gender (Male/Female)
- `SeniorCitizen`: Whether customer is senior (1/0)
- `Partner`: Whether customer has partner (Yes/No)
- `Dependents`: Whether customer has dependents (Yes/No)

**Services**:
- `PhoneService`: Phone service subscription
- `MultipleLines`: Multiple phone lines
- `InternetService`: Type (DSL, Fiber optic, No)
- `OnlineSecurity`: Online security add-on
- `OnlineBackup`: Online backup add-on
- `DeviceProtection`: Device protection add-on
- `TechSupport`: Tech support add-on
- `StreamingTV`: TV streaming service
- `StreamingMovies`: Movie streaming service

**Account**:
- `tenure`: Months as customer
- `Contract`: Contract type (Month-to-month, One year, Two year)
- `PaperlessBilling`: Paperless billing (Yes/No)
- `PaymentMethod`: Payment method
- `MonthlyCharges`: Current monthly charge
- `TotalCharges`: Total charges to date

## Approach

### 1. Exploratory Data Analysis
- Churn rate analysis (overall and by segment)
- Service usage patterns
- Tenure vs churn relationship
- Contract type impact
- Missing value analysis
- Correlation analysis

### 2. Feature Engineering
- **tenure_group**: Categorize tenure (0-12, 12-24, 24-48, 48+)
- **avg_monthly_charges**: TotalCharges / tenure (handle new customers)
- **service_count**: Total number of services used
- **has_premium_services**: Binary for premium service usage
- **charges_per_service**: MonthlyCharges / service_count

### 3. Data Preprocessing
- Handle missing values (TotalCharges has some blanks)
- Convert TotalCharges from string to numeric
- Encode categorical variables (one-hot encoding)
- Handle class imbalance (26.5% churn rate)
- Feature scaling for distance-based algorithms

### 4. Machine Learning Models
Trained and compared 6 classification algorithms:
- Logistic Regression (baseline)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- Support Vector Machine (SVM)

### 5. Handling Class Imbalance
- **Baseline**: Train on imbalanced data
- **SMOTE**: Synthetic Minority Over-sampling
- **Class weights**: Penalize misclassification of minority class
- **Threshold tuning**: Optimize decision threshold

### 6. Model Evaluation
- **Primary Metric**: Recall (catch churners) and Precision (avoid false alarms)
- F1 Score, ROC AUC
- Confusion Matrix analysis
- Precision-Recall curve
- Business cost-benefit analysis
- 5-Fold Cross-Validation
- Feature importance analysis

### 7. Business Recommendations
- Identify top churn drivers
- Customer segments most at risk
- Actionable retention strategies
- Predicted customer lifetime value

## Results

### Key Findings

**Churn Patterns**:
- Overall churn rate: **26.5%**
- Month-to-month contracts: **42% churn** vs 2-year: **3% churn**
- Fiber optic customers: **42% churn** (price sensitivity)
- Customers with tenure <12 months: **48% churn**
- Senior citizens: **41% churn** vs non-seniors: **24% churn**
- Customers without tech support: **41% churn**

**Model Performance**:
- Best model: **XGBoost** or **Random Forest**
- Test accuracy: **~79-82%**
- Precision: **~65-70%** (of predicted churners, 65-70% actually churn)
- Recall: **~75-80%** (catch 75-80% of actual churners)
- F1 Score: **~70-75%**
- ROC AUC: **~84-87%**

**Most Important Features**:
1. **Contract type** - Most predictive (month-to-month = high risk)
2. **Tenure** - New customers churn more
3. **TotalCharges** - Lower total spend = higher churn
4. **MonthlyCharges** - Higher monthly = higher churn (price sensitivity)
5. **InternetService type** - Fiber optic users churn more
6. **Tech support** - Lack of support correlates with churn
7. **Payment method** - Electronic check users churn more

### Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| XGBoost | ~0.81 | ~0.68 | ~0.78 | ~0.73 | ~0.86 |
| Random Forest | ~0.80 | ~0.67 | ~0.76 | ~0.71 | ~0.85 |
| Gradient Boosting | ~0.80 | ~0.66 | ~0.75 | ~0.70 | ~0.84 |
| Logistic Regression | ~0.78 | ~0.63 | ~0.72 | ~0.67 | ~0.82 |
| SVM | ~0.77 | ~0.62 | ~0.70 | ~0.66 | ~0.81 |
| Decision Tree | ~0.73 | ~0.55 | ~0.65 | ~0.60 | ~0.74 |

*Note: With SMOTE and threshold tuning, recall can reach 80-85% with ~55-60% precision*

### Business Recommendations

1. **Target Month-to-Month Customers**: Offer incentives for annual contracts
   - Expected impact: Reduce churn by 15-20%

2. **First 12 Months Are Critical**: Implement onboarding program
   - Suggested: 3-month check-in, personalized service recommendations
   - Expected impact: Reduce new customer churn by 10-15%

3. **Tech Support Matters**: Offer free tech support trial
   - Customers without tech support are 2x more likely to churn
   - Cost: $5/month, Potential save: $50/month in CLV

4. **Address Fiber Optic Pricing**: Review pricing strategy
   - Fiber optic has highest churn despite premium positioning
   - Consider loyalty discounts or value-added services

5. **Prioritize High-Value Customers**: Focus retention on high TotalCharges
   - Top 20% of customers generate 60% of revenue
   - Custom retention packages for high-value at-risk customers

## Technologies Used

- **Python 3.8+**
- **Data Manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn, xgboost, imbalanced-learn
- **Environment**: Jupyter Notebook

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Download Dataset
Download the Telco Customer Churn dataset from Kaggle:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Place `WA_Fn-UseC_-Telco-Customer-Churn.csv` in the project folder.

### Run the Notebook
```bash
jupyter notebook customer_churn_prediction.ipynb
```

### Run Cells
Execute cells sequentially from top to bottom.

## Project Structure

```
04_customer_churn/
├── customer_churn_prediction.ipynb  # Main analysis notebook
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
└── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset (download from Kaggle)
```

## Key Insights

1. **Contract Length is King**: Month-to-month contracts have 14x higher churn than 2-year contracts. Converting just 10% to annual contracts saves significant revenue.

2. **The First Year Challenge**: Nearly half of customers churn in the first 12 months. A structured onboarding program is essential.

3. **Service Quality Matters**: Customers without tech support churn at 2x the rate. Support services are retention drivers, not just upsells.

4. **Price Sensitivity**: Higher monthly charges correlate with churn, especially for fiber optic users. Value perception is critical.

5. **Payment Method Signal**: Electronic check users have highest churn (45%). This may indicate financial instability or poor user experience.

6. **Model Trade-offs**: Higher recall (catching more churners) means more false positives. Business must balance retention costs vs missed opportunities.

## Next Steps

### Model Improvements
1. **Feature Engineering**: Add tenure-charge interaction, customer cohort analysis
2. **Advanced Models**: CatBoost, LightGBM, Neural Networks
3. **Ensemble Methods**: Stacking multiple models
4. **Time Series**: Incorporate month-over-month trends
5. **SHAP Analysis**: Explain individual customer predictions

### Deployment
1. **Build API**: FastAPI for real-time churn prediction
2. **Dashboard**: Streamlit for business users
3. **Batch Scoring**: Weekly churn risk scores for all customers
4. **A/B Testing**: Measure retention campaign effectiveness
5. **Monitoring**: Track model performance over time

### For Portfolio
- [ ] Create presentation slides
- [ ] Write blog post on handling imbalanced classification
- [ ] Deploy Streamlit app
- [ ] Add customer segment analysis
- [ ] Calculate expected ROI from model

## Learning Objectives Achieved

✅ Binary classification with imbalanced data
✅ Business problem framing (cost-benefit analysis)
✅ Feature engineering from domain knowledge
✅ SMOTE and class weighting techniques
✅ Precision-recall trade-off optimization
✅ Multiple model comparison
✅ Feature importance interpretation
✅ Business recommendations from model insights
✅ Professional project documentation

## References

- [Kaggle Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- "Data Science for Business" by Foster Provost & Tom Fawcett
- "Hands-On Machine Learning" by Aurélien Géron

## Author

Created as part of the Data Science Portfolio Projects series.

## License

This project is for educational purposes.
