---
skill_name: technical-analysis-educator
description: Domain expertise for teaching stock market technical analysis, indicators, and trading strategies
version: 1.0.0
author: Educational Notebook System
tags: [finance, trading, technical-analysis, stocks, indicators, education]
activation_keywords: [technical analysis, stock market, trading, indicators, RSI, MACD, moving average, candlestick, chart patterns]
dependencies: [yfinance, pandas-ta, plotly, mplfinance]
---

# Technical Analysis Educator Skill

## Purpose

Provides domain-specific knowledge and teaching patterns for creating educational content about stock market technical analysis, trading indicators, and market analysis techniques.

## When to Use This Skill

Activate when creating content about:
- Technical indicators (MA, RSI, MACD, Bollinger Bands, etc.)
- Chart patterns and price action
- Volume analysis and market sentiment
- Trading strategies and backtesting
- Risk management and position sizing
- Market data analysis with Python

## Core Concepts to Teach

### 1. Price Charts and Candlesticks

**Key Learning Points**:
- OHLC (Open, High, Low, Close) data structure
- Candlestick patterns (doji, hammer, engulfing)
- Support and resistance levels
- Trendlines and channels

**Teaching Pattern**:
```python
# Start with simple line chart of closing prices
# Progress to candlestick charts
# Introduce volume bars
# Add trendlines and support/resistance
```

### 2. Moving Averages

**Types to Cover**:
- Simple Moving Average (SMA): `prices.rolling(window=20).mean()`
- Exponential Moving Average (EMA): `prices.ewm(span=20).mean()`
- Weighted Moving Average (WMA)

**Common Periods**:
- 20-day: Short-term trend
- 50-day: Medium-term trend
- 200-day: Long-term trend

**Trading Signals**:
- Golden Cross: 50-day crosses above 200-day (bullish)
- Death Cross: 50-day crosses below 200-day (bearish)

**Teaching Pattern**:
```python
# 1. Calculate single MA and plot
# 2. Add multiple MAs (20, 50, 200)
# 3. Identify crossovers
# 4. Backtest simple MA crossover strategy
```

### 3. Momentum Indicators

**RSI (Relative Strength Index)**:
- Range: 0-100
- Overbought: >70
- Oversold: <30
- Divergence signals

**MACD (Moving Average Convergence Divergence)**:
- MACD line: 12-day EMA - 26-day EMA
- Signal line: 9-day EMA of MACD
- Histogram: MACD - Signal
- Crossovers indicate momentum shifts

**Teaching Pattern**:
```python
# 1. Explain what momentum measures
# 2. Calculate indicator step-by-step
# 3. Plot with price chart for context
# 4. Identify buy/sell signals
# 5. Discuss false signals and limitations
```

### 4. Volatility Indicators

**Bollinger Bands**:
- Middle band: 20-day SMA
- Upper band: Middle + (2 × standard deviation)
- Lower band: Middle - (2 × standard deviation)
- Price touching bands signals potential reversal

**Average True Range (ATR)**:
- Measures volatility
- Used for position sizing and stop-loss placement

### 5. Volume Analysis

**Key Concepts**:
- Volume confirms price movements
- Volume spikes indicate significant events
- On-Balance Volume (OBV)
- Volume-Weighted Average Price (VWAP)

## Malaysian Stock Market Specifics

### Bursa Malaysia Context

**Market Structure**:
- Trading hours: 9:00 AM - 5:00 PM MYT
- Currency: Malaysian Ringgit (MYR)
- Major indices: FTSE Bursa Malaysia KLCI

**Stock Code Format**:
- Format: `XXXX.KL` (e.g., `1155.KL` for Maybank)
- Use with yfinance: `yf.download('1155.KL')`

**Common Malaysian Stocks for Examples**:
```python
# Blue chips for demonstrations
example_stocks = {
    '1155.KL': 'Maybank',      # Banking
    '5225.KL': 'Top Glove',    # Healthcare
    '5347.KL': 'Press Metal',  # Industrials
    '6012.KL': 'Maxis',        # Telco
    '1023.KL': 'CIMB'          # Banking
}
```

### Data Considerations

**Using yfinance**:
```python
import yfinance as yf

# Download Malaysian stock data
ticker = '1155.KL'  # Maybank
data = yf.download(ticker, start='2020-01-01', end='2024-01-01')

# Always validate data
print(f"Downloaded {len(data)} trading days")
assert len(data) > 0, "No data retrieved - check ticker symbol"
```

**Handling Missing Data**:
- Malaysian public holidays differ from US
- Use forward-fill for missing days
- Validate date ranges

## Teaching Patterns

### Pattern 1: Indicator Introduction

```markdown
## [Indicator Name]

### What is it?
[Simple definition relating to trading decision-making]

### Why traders use it?
[Practical benefit - what problem it solves]

### How to calculate it?
[Step-by-step breakdown with formulas]

### Implementation
```python
# Manual calculation (educational)
# [step-by-step code]

# Using pandas-ta (practical)
import pandas_ta as ta
data.ta.rsi(length=14, append=True)
```

### Interpretation
- [Signal 1]: [What it means]
- [Signal 2]: [What it means]
- [Warning]: [Limitations and false signals]

### Practice Exercise
[Apply indicator to real Malaysian stock]
```

### Pattern 2: Strategy Backtesting

```markdown
## Strategy: [Strategy Name]

### Rules
**Buy Signal**: [Specific conditions]
**Sell Signal**: [Specific conditions]
**Position Sizing**: [How much to invest]
**Stop Loss**: [Risk management]

### Implementation
```python
# 1. Calculate indicators
# 2. Generate signals
# 3. Backtest on historical data
# 4. Calculate performance metrics
```

### Performance Metrics
- Total Return: [%]
- Max Drawdown: [%]
- Win Rate: [%]
- Sharpe Ratio: [value]

### Analysis
- What worked well: [observations]
- Limitations: [issues encountered]
- Improvements: [potential enhancements]
```

## Code Examples

### Complete Indicator Calculation

```python
def calculate_rsi(prices, period=14):
    """
    Calculate Relative Strength Index.

    RSI measures momentum by comparing upward vs downward price movements.
    Values range from 0-100, with >70 indicating overbought and <30 oversold.

    Parameters
    ----------
    prices : pd.Series
        Price data (typically closing prices)
    period : int, default=14
        Lookback period (14 is standard)

    Returns
    -------
    pd.Series
        RSI values

    Example
    -------
    >>> rsi = calculate_rsi(data['Close'], period=14)
    >>> overbought = rsi > 70
    >>> oversold = rsi < 30
    """
    # Calculate price changes
    delta = prices.diff()

    # Separate gains and losses
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    # Calculate average gains and losses
    avg_gains = gains.rolling(window=period).mean()
    avg_losses = losses.rolling(window=period).mean()

    # Calculate RS and RSI
    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1 + rs))

    return rsi
```

### Visualization Best Practices

```python
def plot_price_with_indicators(data, ticker_name):
    """Create educational chart with price and indicators"""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Create subplots: price + volume + RSI
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.5, 0.25, 0.25],
        subplot_titles=(f'{ticker_name} Price', 'Volume', 'RSI')
    )

    # Price candlestick
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name='Price'
        ),
        row=1, col=1
    )

    # Volume bars
    fig.add_trace(
        go.Bar(x=data.index, y=data['Volume'], name='Volume'),
        row=2, col=1
    )

    # RSI line
    fig.add_trace(
        go.Scatter(x=data.index, y=data['RSI'], name='RSI', line=dict(color='purple')),
        row=3, col=1
    )

    # Add RSI reference lines
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)

    fig.update_layout(
        title=f'{ticker_name} Technical Analysis',
        xaxis_title='Date',
        yaxis_title='Price (MYR)',
        height=800,
        showlegend=False
    )

    fig.show()
```

## Common Pitfalls to Address

### 1. Overfitting
**Issue**: Strategy works perfectly on historical data but fails in real trading
**Teaching**: Always use train/test split, out-of-sample validation

### 2. Look-Ahead Bias
**Issue**: Using future data to make past decisions
**Teaching**: Ensure indicators only use data available at that point in time

### 3. Transaction Costs
**Issue**: Ignoring fees and slippage
**Teaching**: Include realistic costs in backtests (0.3-0.5% per trade for Malaysia)

### 4. Survivorship Bias
**Issue**: Only testing on stocks that still exist
**Teaching**: Acknowledge limitation when using current stock lists

## Glossary of Terms

Include clear definitions for:
- **Bullish**: Expecting prices to rise
- **Bearish**: Expecting prices to fall
- **Resistance**: Price level where selling pressure prevents further increase
- **Support**: Price level where buying pressure prevents further decrease
- **Breakout**: Price moving beyond support/resistance
- **Divergence**: Indicator moving opposite to price (warning signal)
- **Crossover**: One line crossing above/below another
- **Backtesting**: Testing strategy on historical data
- **Drawdown**: Peak-to-trough decline
- **Sharpe Ratio**: Risk-adjusted return measure

## Exercise Ideas

### Beginner Exercises
1. Download Malaysian stock data and create price chart
2. Calculate 20-day and 50-day moving averages
3. Identify where MAs cross over
4. Plot RSI and mark overbought/oversold periods

### Intermediate Exercises
1. Implement complete MACD indicator from scratch
2. Create Bollinger Bands and identify squeeze periods
3. Compare multiple Malaysian stocks using same indicator
4. Calculate correlation between stocks in same sector

### Advanced Challenges
1. Implement multi-indicator trading strategy
2. Backtest with proper risk management (stop-loss, position sizing)
3. Optimize indicator parameters using walk-forward analysis
4. Create dashboard comparing multiple strategies

## Success Criteria

Technical analysis educational content should:
- ✅ Explain WHY indicators work (market psychology)
- ✅ Show calculations step-by-step before using libraries
- ✅ Use real Malaysian stocks for examples
- ✅ Discuss limitations and false signals honestly
- ✅ Include proper backtesting methodology
- ✅ Address risk management, not just entries/exits
- ✅ Provide realistic expectations (no "get rich quick")
- ✅ Encourage paper trading before real money
- ✅ Cite reputable sources (Wilder, Appel, Bollinger)
- ✅ Include glossary of technical terms
