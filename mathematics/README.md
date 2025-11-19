# Mathematics for Malaysian Stock Trading

**Learn the math behind technical indicators using real Malaysian stocks**

## 🎯 Project Goals

This learning path teaches you the **mathematical foundations** behind technical analysis indicators. Instead of just using indicators blindly, you'll understand:
- **WHY** indicators work (or don't work)
- **HOW** they're calculated mathematically
- **WHEN** to trust them based on their mathematical properties
- **HOW TO** create your own custom indicators

Every concept is taught using **real Malaysian stock data** (KLSE), making the math immediately practical and relevant to your trading.

## 👥 Who This Is For

- **Traders** who want to understand the math behind their indicators
- **Beginners** with basic high school math (algebra, percentages)
- **Malaysian investors** trading on Bursa Malaysia (KLSE)
- **Anyone** who wants to move beyond "black box" technical analysis

## 📋 Prerequisites

### Knowledge Prerequisites
- ✅ Basic algebra (adding, subtracting, multiplication, division)
- ✅ Understanding percentages
- ✅ Basic graphing/chart reading
- ❌ **NO** advanced calculus required
- ❌ **NO** university-level math required

### Technical Prerequisites
- Python 3.8+
- Jupyter Notebook
- Libraries: pandas, numpy, matplotlib, yfinance
- (See `requirements.txt` for complete list)

## 🗺️ Learning Path

### Part 1: Mathematical Foundations (⭐ Beginner)

Build the basic math skills needed to understand technical indicators.

#### Module 00: Introduction and Stock Returns
**Time**: 30 minutes
**What you'll learn**:
- How to calculate stock returns (daily, weekly, monthly)
- Percentage changes vs absolute changes
- Compound returns and growth rates
**Malaysian stocks used**: 1155.KL (Maybank), 5225.KL (Top Glove)

#### Module 01: Averages and Central Tendency
**Time**: 45 minutes
**What you'll learn**:
- Mean, median, mode with stock prices
- Why average price matters in trading
- Weighted averages (foundation for indicators)
**Indicators explained**: Simple Moving Average (SMA) basics

#### Module 02: Spread and Variation
**Time**: 45 minutes
**What you'll learn**:
- Range, variance, standard deviation
- Measuring stock volatility mathematically
- Why standard deviation matters for risk
**Indicators explained**: Bollinger Bands foundation

#### Module 03: Percentages, Ratios, and Changes
**Time**: 45 minutes
**What you'll learn**:
- Percentage calculations in trading
- Rate of change (ROC) mathematics
- Normalizing values (0-100 scale)
**Indicators explained**: RSI calculation foundation

---

### Part 2: Technical Indicator Mathematics (⭐⭐ Intermediate)

Understand exactly HOW popular indicators are calculated and WHY they work.

#### Module 04: Moving Averages - The Complete Math
**Time**: 60 minutes
**What you'll learn**:
- Simple Moving Average (SMA) - step-by-step calculation
- Exponential Moving Average (EMA) - the weighting formula
- Why EMA reacts faster than SMA (mathematically)
- Smoothing constants and their effects
**Indicators explained**: SMA, EMA, smoothed MA

#### Module 05: Momentum Mathematics
**Time**: 60 minutes
**What you'll learn**:
- Rate of Change (ROC) - the velocity formula
- Relative Strength Index (RSI) - the full calculation
- Stochastic Oscillator - normalization math
- Why momentum indicators oscillate
**Indicators explained**: RSI, ROC, Stochastic, Williams %R

#### Module 06: Volatility Mathematics
**Time**: 60 minutes
**What you'll learn**:
- Bollinger Bands - standard deviation bands
- Average True Range (ATR) - measuring price movement
- Why volatility indicators expand/contract
- Using ATR for stop-loss positioning
**Indicators explained**: Bollinger Bands, ATR, Keltner Channels

#### Module 07: Trend and Convergence Mathematics
**Time**: 60 minutes
**What you'll learn**:
- MACD - the difference between EMAs
- Signal line - why it's a 9-period EMA
- Histogram - convergence/divergence math
- Why MACD shows momentum AND trend
**Indicators explained**: MACD, Signal Line, Histogram

---

### Part 3: Advanced Applications (⭐⭐ Intermediate)

Apply mathematical concepts to real trading scenarios.

#### Module 08: Correlation and Relationships
**Time**: 60 minutes
**What you'll learn**:
- Correlation coefficient (-1 to +1)
- Analyzing relationships between stocks
- Sector correlation in KLSE
- Portfolio diversification mathematics
**Malaysian focus**: Analyzing banking sector, glove sector, tech sector

#### Module 09: Probability and Risk Management
**Time**: 60 minutes
**What you'll learn**:
- Win rate vs risk/reward ratio mathematics
- Expected value in trading
- Position sizing formulas
- Kelly Criterion (simplified)
**Practical math**: How much to invest per trade

#### Module 10: Final Project - Complete Stock Analysis
**Time**: 90 minutes
**Capstone project**:
- Choose a Malaysian stock
- Calculate ALL indicators from scratch (no libraries)
- Analyze using mathematical insights
- Present findings with proper explanations

---

## 📊 Malaysian Stocks Used Throughout

We use **real, diverse Malaysian stocks** for all examples:

| Stock Code | Company | Sector | Why Used |
|------------|---------|--------|----------|
| 1155.KL | Maybank | Banking | Stable, large-cap, good for averages |
| 5225.KL | Top Glove | Healthcare | Volatile, good for volatility indicators |
| 1023.KL | CIMB | Banking | Correlation examples with Maybank |
| 6888.KL | Axiata | Telecommunications | Moderate volatility |
| 5347.KL | Petronas Chemicals | Energy/Chemicals | Sector comparison |

All data is downloaded using `yfinance` with proper date ranges and validation.

## 🛠️ Technical Setup

### Installation

```bash
# Clone or navigate to the mathematics folder
cd mathematics

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Data Access

All notebooks use **automated data downloading**:
```python
import yfinance as yf

# Download Malaysian stock data
maybank = yf.download('1155.KL', start='2020-01-01', end='2024-01-01')
```

No manual data files needed! Internet connection required for first run (data is cached).

## 📚 Learning Tips

### How to Use These Notebooks

1. **Read First**: Read the markdown explanations before running code
2. **Run Cell by Cell**: Don't skip ahead - concepts build on each other
3. **Modify and Experiment**: Change parameters, try different stocks
4. **Do ALL Exercises**: Practice is essential for understanding
5. **Take Notes**: Write down insights in markdown cells

### Recommended Pace

- **Intensive**: 1 module per day (finish in 2 weeks)
- **Steady**: 2-3 modules per week (finish in 1 month)
- **Relaxed**: 1 module per week (finish in 2.5 months)

**Important**: Master each module before moving forward. Understanding foundations is crucial.

### Success Metrics

You've mastered a module when you can:
- ✅ Explain the math to someone else
- ✅ Calculate the indicator manually (without code)
- ✅ Identify when the indicator might fail
- ✅ Complete all exercises without looking at solutions

## 🔗 Related Content

This mathematics topic integrates with:
- **malaysia-stock/**: Apply these mathematical insights to trading strategies
- **data-science/01_mathematics/**: More general mathematical concepts
- **data-science/02_data_manipulation/**: Data handling skills

## 📈 After Completing This Path

You will be able to:
- ✅ Calculate any technical indicator from scratch
- ✅ Understand indicator limitations mathematically
- ✅ Create custom indicators for specific needs
- ✅ Evaluate indicator effectiveness objectively
- ✅ Avoid common indicator misuse pitfalls
- ✅ Combine indicators intelligently (understanding overlap)

## 🤝 Contributing

This is a personal learning portfolio, but suggestions are welcome:
- Found an error in calculations? Please report it
- Have a clearer way to explain a concept? Share it
- Want to add more Malaysian stock examples? Suggest them

## 📄 License

Educational content for personal learning and reference.

## 🙏 Acknowledgments

- **yfinance**: For easy access to Malaysian stock data
- **Bursa Malaysia**: For providing transparent market data
- **Technical analysis community**: For decades of indicator development

---

**Ready to start?** Open `notebooks/00_introduction_stock_returns.ipynb` and begin your journey into the mathematics of trading!
