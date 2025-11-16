# 📈 KLSE Advanced: Backtesting Trading Strategies

## Overview

This is an **intermediate-level educational notebook** that teaches backtesting concepts and strategy development for Malaysian stocks (KLSE). It builds naturally from the beginner KLSE Stock Screener notebook.

**Status:** 🚧 Currently being built

## What You'll Learn

1. **Backtesting Fundamentals** - Test strategies on historical data
2. **Build Trading Strategies** - MA Crossover, RSI Mean Reversion, MACD Momentum
3. **Performance Metrics** - Returns, Sharpe ratio, max drawdown, win rate
4. **Risk Management** - Stop-loss, position sizing, portfolio allocation
5. **Avoid Pitfalls** - Overfitting, biases, unrealistic assumptions
6. **Strategy Comparison** - Find what works best for Malaysian stocks

## Prerequisites

- Completed KLSE Stock Screener notebook (or equivalent knowledge)
- Comfortable with Python basics, pandas, DataFrames
- Understanding of basic technical indicators (SMA, RSI, MACD)

## Notebook Structure (12 Sections)

### Part 1: Foundations
1. **Introduction to Backtesting** - What, why, how, limitations
2. **Backtesting Framework Setup** - Data prep, costs, position sizing
3. **Performance Metrics Deep Dive** - CAGR, Sharpe, drawdown, win rate

### Part 2: Core Strategies
4. **Strategy #1: Moving Average Crossover** - Golden Cross, backtesting, analysis
5. **Strategy #2: RSI Mean Reversion** - Oversold/overbought, implementation
6. **Strategy #3: MACD Momentum** - Signal crossovers, testing

### Part 3: Risk & Portfolio
7. **Risk Management Essentials** - Stop-loss, take-profit, position sizing
8. **Multi-Stock Portfolio Backtesting** - Test across 10 KLSE stocks

### Part 4: Advanced Concepts
9. **Avoiding Common Pitfalls** - Overfitting, biases, curve-fitting
10. **Walk-Forward Testing** - In-sample vs out-of-sample validation
11. **Strategy Comparison & Optimization** - Compare all strategies

### Part 5: Wrap-up
12. **Next Steps & Advanced Topics** - ML integration, live trading, resources

## Key Features

✅ **Educational Focus** - Detailed explanations, not just code
✅ **Beginner-Friendly** - Builds on KLSE screener concepts
✅ **Hands-On Practice** - Multiple exercises and challenges
✅ **Real Malaysian Data** - KLSE stocks with realistic scenarios
✅ **Complete Framework** - Reusable backtesting functions
✅ **Risk-Aware** - Includes transaction costs and proper risk management

## Installation

```bash
# Install required packages
pip install yfinance pandas numpy pandas-ta matplotlib seaborn plotly

# Or use existing venv from KLSE screener project
source ../../venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

```bash
# Open in Jupyter
jupyter notebook klse_backtesting_strategies.ipynb

# Or use VS Code with Jupyter extension
```

## Learning Outcomes

After completing this notebook, you will:
- ✅ Understand backtesting fundamentals and limitations
- ✅ Build and test trading strategies systematically
- ✅ Calculate and interpret risk-adjusted performance metrics
- ✅ Implement proper risk management techniques
- ✅ Avoid common backtesting mistakes and biases
- ✅ Compare strategies objectively with data
- ✅ Make informed, data-driven trading decisions

## Estimated Time

**3-4 hours** to complete thoroughly (with exercises)

## Example Strategies Tested

### 1. Moving Average Crossover
```python
# Buy when SMA-50 crosses above SMA-200 (Golden Cross)
# Sell when SMA-50 crosses below SMA-200 (Death Cross)
```

**Pros:** Simple, trend-following, works in strong trends
**Cons:** Lagging, whipsaws in sideways markets

### 2. RSI Mean Reversion
```python
# Buy when RSI < 30 (oversold)
# Sell when RSI > 70 (overbought)
```

**Pros:** Good in range-bound markets, clear signals
**Cons:** Can stay overbought/oversold for long periods

### 3. MACD Momentum
```python
# Buy when MACD crosses above signal line
# Sell when MACD crosses below signal line
```

**Pros:** Combines trend and momentum, widely used
**Cons:** Can generate false signals in choppy markets

## Performance Metrics Explained

### 1. Total Return
Simple percentage gain/loss over the period.

### 2. CAGR (Compound Annual Growth Rate)
```
CAGR = (Ending Value / Beginning Value)^(1/Years) - 1
```
Annualized return, accounts for compounding.

### 3. Sharpe Ratio
```
Sharpe = (Returns - Risk-Free Rate) / Standard Deviation
```
Risk-adjusted returns. Higher is better.
- < 1.0: Not great
- 1.0-2.0: Good
- > 2.0: Excellent

### 4. Maximum Drawdown
Largest peak-to-trough decline. Measures worst-case scenario.
- 10-20%: Acceptable
- 20-30%: High risk
- > 30%: Very risky

### 5. Win Rate
Percentage of profitable trades.
- 50%+: Good
- 60%+: Very good
- Note: High win rate doesn't always mean profitable!

## Malaysian Stocks Used

The notebook tests strategies on these KLSE stocks:
- **Banking**: Maybank (1155.KL), Public Bank (1295.KL), CIMB (1023.KL)
- **Utilities**: Tenaga Nasional (5296.KL)
- **Telecom**: Maxis (4197.KL), Axiata (6012.KL)
- **Plantation**: IOI Corp (2445.KL)
- **Healthcare**: IHH Healthcare (3816.KL)
- **Consumer**: Nestle Malaysia (3816.KL)
- **Industrial**: Gamuda (1961.KL)

## Important Disclaimers

⚠️ **This notebook is for EDUCATIONAL purposes only!**

- Past performance does NOT guarantee future results
- Backtesting has limitations (discussed in detail)
- Always paper trade before using real money
- Markets can behave differently than historical data
- Consult licensed financial advisors for investment decisions
- Never invest more than you can afford to lose

## Common Pitfalls Covered

1. **Overfitting** - Making strategy work TOO well on past data
2. **Look-ahead Bias** - Using information you wouldn't have had
3. **Survivorship Bias** - Only testing stocks that still exist
4. **Data-snooping** - Testing many strategies until one works
5. **Ignoring Costs** - Forgetting commissions and slippage
6. **Unrealistic Execution** - Assuming perfect fills at exact prices

## Next Steps After This Notebook

1. **Paper Trading** - Test strategies in real-time without money
2. **Machine Learning** - Use ML to improve strategy selection
3. **Live Trading** - Implement with proper risk management
4. **Portfolio Optimization** - Modern Portfolio Theory
5. **Options Strategies** - Hedging and income generation

## Resources

### Recommended Reading:
- "Evidence-Based Technical Analysis" by David Aronson
- "Algorithmic Trading" by Ernest P. Chan
- "Quantitative Trading" by Ernest P. Chan

### Useful Websites:
- [QuantStart](https://www.quantstart.com/) - Quant trading education
- [Investopedia](https://www.investopedia.com/) - Financial education
- [Quantopian Lectures](https://github.com/quantopian/research_public) - Free quant finance lectures

### Malaysian Market:
- [Bursa Malaysia](https://www.bursamalaysia.com/) - Official exchange
- [i3investor](https://klse.i3investor.com/) - Malaysian stock community

## Project Structure

```
klse-backtesting/
├── klse_backtesting_strategies.ipynb  # Main notebook
├── README.md                           # This file
├── backtest_results/                   # Saved backtest results
│   ├── ma_crossover_results.csv
│   ├── rsi_results.csv
│   └── macd_results.csv
└── data/                               # Cached stock data (gitignored)
```

## Contributing

This is an educational project. Suggestions and improvements welcome!

## License

Educational use only. See main project LICENSE.

## Support

Having issues? Check the troubleshooting section in the notebook or refer back to the KLSE Stock Screener notebook for basics.

---

**Happy Backtesting! 📊📈🚀**

*Remember: Knowledge + Discipline + Patience = Trading Success*
