# House Price Prediction

**Difficulty**: ⭐ Beginner
**Type**: Regression
**Dataset**: California Housing Dataset
**Estimated Time**: 25-30 hours

## Problem Statement

**Goal**: Predict median house prices in California districts based on features like location, demographics, and housing characteristics.

This project demonstrates regression modeling techniques, feature engineering for continuous targets, and handling geographic data.

## Dataset

- **Source**: Scikit-learn built-in dataset (California Housing)
- **Rows**: 20,640 districts
- **Features**: 8 features including demographics, location, and housing characteristics
- **Target**: Median house value in hundreds of thousands of dollars

### Key Features
- `MedInc`: Median income in block group (tens of thousands)
- `HouseAge`: Median house age (years)
- `AveRooms`: Average number of rooms per household
- `AveBedrms`: Average number of bedrooms per household
- `Population`: Block group population
- `AveOccup`: Average household members
- `Latitude` / `Longitude`: Geographic coordinates
- **Target**: `MedHouseVal` - Median house value ($100k units)

## Approach

### 1. Exploratory Data Analysis
- Target variable distribution (right-skewed, capped at $500k)
- Geographic visualization (coastal areas premium)
- Feature distributions and outlier detection
- Correlation analysis (MedInc has 0.69 correlation with price)

### 2. Feature Engineering
- **RoomsPerBedroom**: Indicator of apartment type
- **PopulationDensity**: People per household
- **BedroomRatio**: Proportion of bedrooms to total rooms
- **Log transformations**: For skewed features (income, rooms, population)
- **Geographic features**: Distance from San Francisco and Los Angeles
- Total: 8 engineered features created

### 3. Data Preparation
- No missing values (clean dataset)
- Feature scaling with StandardScaler
- Compared original vs engineered features
- 80/20 train-test split

### 4. Machine Learning Models
Trained and compared 9 regression algorithms:
- Linear Regression (baseline)
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)
- ElasticNet (L1 + L2)
- Decision Tree
- Random Forest
- Gradient Boosting
- Support Vector Regression (SVR)
- K-Nearest Neighbors (KNN)

### 5. Model Evaluation
- R² Score (coefficient of determination)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)
- Residual analysis

### 6. Hyperparameter Tuning
- Grid Search CV on Gradient Boosting
- Optimized: n_estimators, max_depth, learning_rate, min_samples_split
- 5-fold cross-validation for stability

## Results

### Model Performance

| Model | R² Score | RMSE ($100k) | MAE ($100k) | MAPE (%) |
|-------|----------|--------------|-------------|----------|
| Random Forest | ~0.81 | ~0.50 | ~0.33 | ~17% |
| Gradient Boosting | ~0.80 | ~0.52 | ~0.35 | ~18% |
| Ridge Regression | ~0.60 | ~0.74 | ~0.53 | ~26% |
| Linear Regression | ~0.60 | ~0.74 | ~0.53 | ~26% |
| Lasso | ~0.60 | ~0.74 | ~0.53 | ~26% |

*RMSE of ~0.50 means average prediction error of ~$50k*

### Key Findings

**Price Patterns:**
- Average house price: ~$200k (1990s California)
- Strong geographic influence (Bay Area and LA coast premium)
- Median income is strongest predictor (r = 0.69)
- Prices capped at $500k in dataset

**Most Important Features:**
1. Median Income (MedInc) - 0.69 correlation
2. Location (Latitude, Longitude) - Geographic premium
3. House Age - Moderate importance
4. Average Rooms - Housing quality indicator

**Model Insights:**
- Tree-based models (Random Forest, Gradient Boosting) significantly outperformed linear models
- R² ~0.80-0.81 means models explain 80-81% of price variance
- Prediction error: ~$50-55k average deviation
- Linear models achieved R² ~0.60 (reasonable baseline)

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
jupyter notebook house_price_prediction.ipynb
```

### Run Cells
Execute cells sequentially. The dataset is built into scikit-learn (no download required).

## Project Structure

```
02_house_prices/
├── house_price_prediction.ipynb   # Main analysis notebook
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

## Key Insights

1. **Income Drives Prices**: Median income is the single strongest predictor (r=0.69). Socioeconomic status determines housing affordability.

2. **Location Premium**: Coastal areas (Bay Area, Los Angeles) command significantly higher prices. Geographic coordinates are highly predictive.

3. **Tree Models Win**: Random Forest and Gradient Boosting achieved R²~0.80-0.81, far superior to linear models (R²~0.60). Non-linear relationships matter.

4. **Age Paradox**: Older houses don't necessarily have lower prices. Vintage/character may add value in certain locations.

5. **Occupancy Irrelevant**: Average occupancy has minimal impact on price. House size and location matter more than crowding.

## Next Steps

### Potential Improvements
1. **Test Engineered Features**: Compare performance with RoomsPerBedroom, DistanceFromSF, log transformations
2. **Polynomial Features**: Create quadratic terms for non-linear relationships
3. **Advanced Ensembles**: XGBoost, LightGBM, stacking
4. **Error Analysis**: Investigate large residuals (>$100k errors)
5. **Learning Curves**: Diagnose bias vs variance
6. **Deployment**: Create Streamlit app for interactive predictions

### For Portfolio
- [ ] Test engineered features impact
- [ ] Create visualizations dashboard
- [ ] Write blog post about findings
- [ ] Deploy as web app
- [ ] Add to portfolio website

## Learning Objectives Achieved

✅ Regression analysis on real-world data
✅ Multivariate feature relationships
✅ Geographic data visualization
✅ Feature engineering for continuous targets
✅ Regularization techniques (Ridge, Lasso, ElasticNet)
✅ 9 regression algorithms comparison
✅ Model evaluation with RMSE, MAE, R², MAPE
✅ Hyperparameter tuning with GridSearchCV
✅ Cross-validation for model stability
✅ Feature importance analysis
✅ Residual analysis and diagnostics
✅ Professional project documentation

## References

- [California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
- Scikit-learn documentation
- "Hands-On Machine Learning" by Aurélien Géron (uses this dataset as example)
- "Introduction to Statistical Learning" - regression chapters

## Author

Created as part of the Data Science Portfolio Projects series.

## License

This project is for educational purposes.

---

**Note**: This dataset contains 1990 California census data. Prices are in 1990 dollars and capped at $500k. Modern California house prices are significantly higher. The modeling techniques demonstrated here are applicable to any regression problem.
