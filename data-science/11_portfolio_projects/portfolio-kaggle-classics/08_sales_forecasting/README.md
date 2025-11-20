# Project 08: Time Series Sales Forecasting (⭐⭐ Intermediate)

## Problem Statement

Forecast retail sales for the next 3-6 months using historical sales data. Build and compare multiple time series forecasting models to predict future sales accurately, incorporating trends, seasonality, and external factors like holidays. The goal is to help retailers optimize inventory, staffing, and marketing strategies.

## Dataset

**Rossmann Store Sales** or **Walmart Sales Forecasting** (Kaggle)

### Rossmann Store Sales
- **Source**: [Kaggle - Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales)
- **Size**: 1,017,209 sales records from 1,115 stores
- **Time Period**: 2.5 years of daily sales data
- **Features**:
  - Store ID, date, sales, customers
  - Store type, assortment, competition distance
  - Promo indicators, school holidays, state holidays

### Walmart Sales Forecasting (Alternative)
- **Source**: [Kaggle - Walmart Recruiting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)
- **Size**: 421,570 sales records from 45 stores
- **Features**:
  - Store, department, date, weekly sales
  - Temperature, fuel price, CPI, unemployment
  - Holiday flags (Super Bowl, Labor Day, Thanksgiving, Christmas)

## Forecasting Methods

This project implements and compares multiple time series forecasting approaches:

1. **SARIMA (Seasonal ARIMA)**
   - Statistical model for univariate time series
   - Captures trend and seasonality
   - Requires manual parameter tuning (p, d, q, P, D, Q, s)
   - Good baseline model

2. **Prophet (Facebook Prophet)**
   - Automatic seasonality detection (daily, weekly, yearly)
   - Handles holidays and special events
   - Robust to missing data and outliers
   - User-friendly with minimal tuning

3. **XGBoost for Time Series**
   - Gradient boosting with time series features
   - Uses lag features, rolling statistics, date features
   - Handles multiple external variables (weather, holidays, promotions)
   - High accuracy with proper feature engineering

4. **LSTM (Long Short-Term Memory)**
   - Deep learning approach for sequential data
   - Learns complex temporal patterns automatically
   - Effective for long-term dependencies
   - Requires more data and computational resources

## Feature Engineering

Key features for improved forecasting accuracy:

- **Lag Features**: Sales from previous 1, 7, 14, 28, 30 days
- **Rolling Statistics**: 7-day, 30-day moving averages and standard deviations
- **Date Features**: Day of week, month, quarter, year, is_weekend
- **Holiday Indicators**: Binary flags for major holidays
- **Promotional Events**: Promo periods, special campaigns
- **External Variables**: Temperature, fuel prices, economic indicators
- **Store Characteristics**: Store type, size, competition distance

## Evaluation Metrics

- **RMSE** (Root Mean Squared Error): Standard metric for forecast accuracy
- **MAE** (Mean Absolute Error): Average absolute difference
- **MAPE** (Mean Absolute Percentage Error): Percentage-based error metric
- **Directional Accuracy**: Percentage of correct trend predictions (up/down)
- **Coverage**: Percentage of actual values within prediction intervals

## Tech Stack

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Statistical Models**: statsmodels (SARIMA)
- **Prophet**: fbprophet (or prophet for newer versions)
- **Machine Learning**: xgboost, scikit-learn
- **Deep Learning**: tensorflow or pytorch (for LSTM)
- **Development**: Jupyter notebook

## Expected Performance

- **Target MAPE**: < 15%
- **Typical Results**:
  - SARIMA: MAPE ~12-18% (baseline)
  - Prophet: MAPE ~10-15% (automatic seasonality)
  - XGBoost: MAPE ~8-12% (with good features)
  - LSTM: MAPE ~7-11% (with sufficient data)
  - Ensemble: MAPE ~6-10% (combining models)

## Key Insights

1. **Seasonality Patterns**: Sales often show weekly (weekends vs weekdays) and yearly (holiday seasons) patterns
2. **Holiday Effects**: Major holidays significantly impact sales, requiring special handling
3. **Promotions Impact**: Promotional events can cause sudden spikes in sales
4. **Store Heterogeneity**: Different stores have different patterns; consider store-specific models
5. **Feature Importance**: Lag features and rolling statistics are typically most important
6. **Model Ensemble**: Combining statistical and ML approaches often yields best results

## Learning Objectives

By completing this project, you will:
- Understand time series data characteristics (trend, seasonality, autocorrelation)
- Perform stationarity tests and data transformations
- Implement SARIMA models with parameter tuning
- Use Prophet for automatic seasonality detection
- Engineer time series features for machine learning
- Build XGBoost and LSTM models for forecasting
- Compare multiple forecasting approaches systematically
- Generate business recommendations from forecasts
- Visualize forecasts with confidence intervals

## Project Structure

```
08_sales_forecasting/
├── README.md                    # This file
├── sales_forecasting.ipynb      # Main analysis notebook
├── requirements.txt             # Python dependencies
└── data/                        # Dataset directory (download separately)
    ├── rossmann/                # Rossmann dataset
    │   ├── train.csv
    │   ├── test.csv
    │   ├── store.csv
    │   └── sample_submission.csv
    └── walmart/                 # Walmart dataset (alternative)
        ├── train.csv
        ├── test.csv
        ├── features.csv
        └── stores.csv
```

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download dataset**:
   - Visit [Kaggle - Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales/data)
   - Or [Kaggle - Walmart Sales](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data)
   - Download and extract to `data/rossmann/` or `data/walmart/`

3. **Run notebook**:
   ```bash
   jupyter notebook sales_forecasting.ipynb
   ```

## Business Applications

Sales forecasting enables:
- **Inventory Optimization**: Order right amount of stock, reduce waste
- **Staffing Planning**: Schedule employees based on expected traffic
- **Marketing Strategy**: Plan promotions and campaigns effectively
- **Financial Planning**: Improve revenue and budget forecasting
- **Supply Chain**: Optimize distribution and logistics

## Next Steps

After completing this project, consider:
- **Multi-Store Forecasting**: Build hierarchical models for store groups
- **Anomaly Detection**: Identify unusual sales patterns
- **Demand Sensing**: Real-time forecast updates with recent data
- **Causal Impact**: Measure specific promotion or event effects
- **Production Deployment**: Automate forecasting pipeline with Airflow

## References

- [Statsmodels SARIMAX Documentation](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)
- [Prophet Documentation](https://facebook.github.io/prophet/)
- [XGBoost for Time Series](https://towardsdatascience.com/using-gradient-boosting-for-time-series-prediction-tasks-600fac66a5fc)
- [Time Series with LSTM](https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/)
- Research Paper: [Forecasting: Principles and Practice](https://otexts.com/fpp3/)
