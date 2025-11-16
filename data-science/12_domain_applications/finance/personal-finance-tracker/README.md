# Personal Finance Tracker 💰

An enhanced personal finance application with both an interactive Jupyter notebook for learning and a production-ready Streamlit web interface.

## Overview

This comprehensive project tracks and analyzes both income and expenses using Python's data science stack. It combines educational content with production-ready features, making it perfect for both learning data analysis and managing your actual finances.

## Features

### Core Functionality
- **Income & Expense Tracking**: Full double-entry bookkeeping with transaction IDs
- **Budget Management**: Set budgets per category with real-time alerts
- **Transaction Management**: Search, edit, and delete transactions
- **Recurring Transactions**: Automate tracking of subscriptions and regular bills
- **Net Savings Analysis**: Calculate savings rate and financial health metrics

### Data Analysis
- **Category Analysis**: Detailed spending breakdowns with statistics
- **Time-based Analysis**: Daily, weekly, and monthly trends
- **Budget vs Actual**: Compare spending against budgets
- **Day-of-week Patterns**: Identify spending patterns by weekday

### Visualizations
- **Static Charts** (matplotlib/seaborn):
  - Pie charts for category proportions
  - Line charts for spending trends
  - Bar charts for monthly comparisons
  - Stacked bar charts for detailed breakdowns
- **Interactive Charts** (Plotly):
  - Waterfall charts for cash flow analysis
  - Interactive pie charts with hover details
  - Spending heatmaps by day of week
  - Income vs expenses trend comparisons

### Advanced Features
- **Predictive Analytics**: ML-based spending forecasts using linear regression
- **Anomaly Detection**: Identify unusual expenses automatically
- **Budget Recommendations**: AI-powered budget suggestions based on historical data
- **Data Import/Export**:
  - Import from bank CSV statements
  - Export to Excel (XLSX) with multiple sheets
  - JSON backup/restore for data portability
- **Web Interface**: Full-featured Streamlit dashboard

## What You'll Learn

### Data Science Concepts
- Working with pandas DataFrames for data manipulation
- Grouping and aggregating data with `.groupby()`
- DateTime operations in pandas
- Creating visualizations with matplotlib, seaborn, and Plotly
- File I/O operations (CSV, Excel, JSON)
- Writing reusable Python functions
- Data validation and error handling

### Machine Learning
- Linear regression for time series forecasting
- Statistical anomaly detection
- Feature engineering for financial data
- Model evaluation and interpretation

### Web Development
- Building interactive dashboards with Streamlit
- State management in web applications
- Form handling and data persistence
- Responsive layout design

## Project Structure

```
personal-finance-tracker/
├── personal_finance_tracker.ipynb  # Enhanced Jupyter notebook with full tutorial
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── data/                           # Data storage directory
    ├── expenses.csv                # Expense records
    └── income.csv                  # Income records
```

## Installation

1. Navigate to the project directory:
   ```bash
   cd projects/personal-finance-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Option 1: Jupyter Notebook (Learning & Analysis)

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `personal_finance_tracker.ipynb`

3. Run cells sequentially to:
   - Learn data analysis concepts
   - Explore all features interactively
   - Customize analysis for your needs
   - Run predictive models

### Option 2: Streamlit Web App (Daily Use)

1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Your browser will open at `http://localhost:8501`

3. Use the web interface to:
   - Add transactions quickly
   - View dashboard with real-time metrics
   - Manage budgets visually
   - Generate reports and forecasts

## Key Functions

### Transaction Management
- `add_expense(df, date, category, amount, description)` - Add new expense
- `add_income(df, date, category, amount, description)` - Add income entry
- `add_transaction_ids(df)` - Add unique IDs to transactions
- `edit_transaction(df, id, **kwargs)` - Edit existing transaction
- `delete_transaction(df, id)` - Delete transaction by ID
- `search_transactions(df, **filters)` - Search with multiple criteria
- `view_transaction(df, id)` - View transaction details

### Financial Analysis
- `calculate_net_savings(income_df, expenses_df)` - Calculate net savings and rate
- `analyze_by_category(df)` - Spending breakdown by category
- `analyze_monthly_spending(df)` - Monthly trends and statistics
- `get_spending_insights(df)` - Comprehensive financial insights

### Budget Management
- `set_budget(category, amount)` - Set monthly budget for category
- `check_budget_status(df, period, year, month)` - Compare actual vs budget
- `budget_alert(df, category, threshold)` - Get budget alerts

### Recurring Transactions
- `add_recurring_transaction(type, category, amount, description, frequency)` - Add recurring template
- `generate_recurring_transactions(end_date)` - Auto-generate transactions
- `list_recurring_transactions()` - View all recurring transactions

### Import/Export
- `import_from_csv(filename, column_mapping)` - Import from bank statements
- `export_to_excel(expenses_df, income_df, filename)` - Export to Excel
- `export_to_json(expenses_df, income_df, budgets, filename)` - JSON backup
- `import_from_json(filename)` - Restore from JSON backup

### Predictive Analytics
- `forecast_spending(df, months_ahead)` - ML-based spending forecast
- `detect_anomalies(df, std_threshold)` - Identify unusual expenses
- `recommend_budget(df, savings_target_pct)` - AI budget recommendations

### Visualizations
- `create_waterfall_chart(income_df, expenses_df)` - Cash flow waterfall
- `create_spending_heatmap(df)` - Day-of-week spending patterns
- `create_interactive_category_pie(df)` - Interactive Plotly pie chart
- `create_trend_chart(expenses_df, income_df)` - Income vs expenses trends

## Sample Data

The notebook includes sample data:
- **Expenses**: 21 transactions across 5 categories over 3 months
- **Income**: 6 income entries (salary, freelance, investments)
- **Budgets**: Pre-set budgets for all expense categories
- **Recurring**: Example subscriptions (Netflix, Spotify) and salary

## Technology Stack

- **Python 3.8+**
- **pandas** - Data manipulation and analysis
- **matplotlib & seaborn** - Static visualizations
- **Plotly** - Interactive charts
- **scikit-learn** - Machine learning for predictions
- **Streamlit** - Web application framework
- **openpyxl** - Excel file operations
- **Jupyter** - Interactive notebook environment

## Educational Value

This project is structured to teach progressively:

1. **Part I (Basics)**: Core pandas and visualization concepts
2. **Part II (Advanced)**: Production features and ML integration
3. **Streamlit App**: Web development and deployment

Each section includes:
- Clear explanations of concepts
- Code with detailed comments
- Example outputs and interpretations
- Best practices and common pitfalls
- Practice exercises

## Requirements

All dependencies are listed in `requirements.txt`. Key packages:

```
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0
scikit-learn>=1.3.0
streamlit>=1.28.0
openpyxl>=3.1.0
jupyter>=1.0.0
```

## Contributing

This is a portfolio project, but suggestions for improvements are welcome!

## License

MIT License - Feel free to use this project for learning or personal finance management.

## Author

Created as part of a Python projects portfolio to demonstrate:
- Data science and analysis skills
- Machine learning implementation
- Web application development
- Technical documentation
- Code organization and best practices

---

**Happy tracking! 💰📊**
