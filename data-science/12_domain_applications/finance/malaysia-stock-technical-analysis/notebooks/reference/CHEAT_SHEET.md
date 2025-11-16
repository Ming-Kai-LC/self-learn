# Technical Analysis Cheat Sheet

**Quick Reference Guide for Malaysian Stock Analysis**

---

## Table of Contents

### Beginner Section (Modules 00-06)
1. [Basic Concepts](#basic-concepts)
2. [Price Data (OHLCV)](#price-data-ohlcv)
3. [Moving Averages](#moving-averages)
4. [Momentum Indicators](#momentum-indicators)
5. [Volume Analysis](#volume-analysis)
6. [Trading Signals](#trading-signals)

### Intermediate Section (Modules 07-13)
7. [Bollinger Bands & Volatility](#bollinger-bands--volatility)
8. [Advanced Oscillators](#advanced-oscillators)
9. [Fibonacci Retracements](#fibonacci-retracements)
10. [Multi-Timeframe Analysis](#multi-timeframe-analysis)
11. [ADX & Chart Patterns](#adx--chart-patterns)
12. [Risk Management & Position Sizing](#risk-management--position-sizing)
13. [Stock Screening](#stock-screening)
14. [Quick Python Commands](#quick-python-commands)

---

## Basic Concepts

###  Technical vs Fundamental Analysis

| Aspect | Technical | Fundamental |
|--------|-----------|-------------|
| **Focus** | Price & Volume | Company Value |
| **Question** | WHEN to buy/sell? | WHAT to buy? |
| **Time Frame** | Short-Medium term | Long term |
| **Tools** | Charts, Indicators | Financial Statements |

### The Three Principles

1. **Price Discounts Everything** - All information is already in the price
2. **Price Moves in Trends** - Stocks follow patterns (up, down, sideways)
3. **History Repeats** - Similar patterns lead to similar outcomes

---

## Price Data (OHLCV)

### What Each Letter Means

- **O** = **Open** - Starting price when market opens
- **H** = **High** - Highest price during the day
- **L** = **Low** - Lowest price during the day
- **C** = **Close** - Final price (MOST IMPORTANT!)
- **V** = **Volume** - Number of shares traded

### Quick Interpretation

| Pattern | Meaning |
|---------|---------|
| Close > Open | Bullish day (buyers won) |
| Close < Open | Bearish day (sellers won) |
| Large High-Low range | High volatility (risky) |
| Small High-Low range | Low volatility (stable) |

---

## Moving Averages

### Types of Moving Averages

| Type | Full Name | Best For | Responsiveness |
|------|-----------|----------|----------------|
| **SMA** | Simple Moving Average | Long-term trends | Slow |
| **EMA** | Exponential Moving Average | Short-term trends | Fast |

### Common Time Periods

| Period | Type | Purpose |
|--------|------|---------|
| **20-day** | Short-term | Recent price action |
| **50-day** | Medium-term | Intermediate trends |
| **200-day** | Long-term | Major trends |

### Trading Signals

#### Golden Cross (BULLISH 📈)
- **What**: Short-term MA crosses ABOVE long-term MA
- **Example**: 50-day SMA crosses above 200-day SMA
- **Action**: Buy signal (uptrend starting)

#### Death Cross (BEARISH 📉)
- **What**: Short-term MA crosses BELOW long-term MA
- **Example**: 50-day SMA crosses below 200-day SMA
- **Action**: Sell signal (downtrend starting)

### Trend Identification

```
Price > 200-day MA = Uptrend (Bullish)
Price < 200-day MA = Downtrend (Bearish)
Price ≈ 200-day MA = Sideways (Neutral)
```

---

## Momentum Indicators

### RSI (Relative Strength Index)

**Range**: 0 to 100

| Level | Zone | Meaning | Action |
|-------|------|---------|--------|
| **> 70** | Overbought | Too many buyers | Consider SELLING |
| **30-70** | Neutral | Normal trading | Hold / Monitor |
| **< 30** | Oversold | Too many sellers | Consider BUYING |

**Formula**: RSI = 100 - [100 / (1 + RS)]
Where RS = Average Gain / Average Loss (14 days)

#### RSI Trading Signals
- ✅ **Buy**: RSI crosses ABOVE 30 (exiting oversold)
- ❌ **Sell**: RSI crosses BELOW 70 (exiting overbought)
- ⚠️ **Divergence**: Price makes new high, RSI doesn't (bearish)

---

### MACD (Moving Average Convergence Divergence)

**Components:**
1. **MACD Line** = 12-day EMA - 26-day EMA
2. **Signal Line** = 9-day EMA of MACD Line
3. **Histogram** = MACD Line - Signal Line

| Signal | Condition | Meaning |
|--------|-----------|---------|
| **Bullish Crossover** 📈 | MACD crosses ABOVE Signal | Buy signal |
| **Bearish Crossover** 📉 | MACD crosses BELOW Signal | Sell signal |
| **Positive Histogram** | MACD > Signal | Bullish momentum |
| **Negative Histogram** | MACD < Signal | Bearish momentum |

#### Quick Interpretation
```
MACD > 0 = Upward momentum
MACD < 0 = Downward momentum
Histogram growing = Momentum strengthening
Histogram shrinking = Momentum weakening
```

---

## Volume Analysis

### Volume Patterns

| Price | Volume | Interpretation | Strength |
|-------|--------|----------------|----------|
| ↑ | ↑ | Strong uptrend | VERY STRONG 💪 |
| ↑ | ↓ | Weak uptrend | WEAK ⚠️ |
| ↓ | ↑ | Strong downtrend | VERY STRONG ⚠️ |
| ↓ | ↓ | Weak downtrend | WEAK |

### Volume Rules

1. **High Volume = Strong Conviction** - Many people agree
2. **Low Volume = Weak Conviction** - Few people participating
3. **Always confirm price moves with volume!**

### OBV (On-Balance Volume)

**What it does**: Cumulative volume indicator

```
If Close > Yesterday's Close: OBV = Yesterday's OBV + Today's Volume
If Close < Yesterday's Close: OBV = Yesterday's OBV - Today's Volume
If Close = Yesterday's Close: OBV = Yesterday's OBV (unchanged)
```

**Interpretation:**
- OBV trending up = Accumulation (buyers winning)
- OBV trending down = Distribution (sellers winning)
- OBV diverges from price = Warning sign!

---

## Trading Signals

### Bullish Signals (Buy) 📈

| Indicator | Signal |
|-----------|--------|
| **MA** | Price crosses ABOVE moving average |
| **Golden Cross** | 50-day MA crosses above 200-day MA |
| **RSI** | Crosses above 30 (exiting oversold) |
| **MACD** | MACD line crosses above Signal line |
| **Volume** | Price up + Volume up |
| **OBV** | Rising OBV + Rising price |

### Bearish Signals (Sell) 📉

| Indicator | Signal |
|-----------|--------|
| **MA** | Price crosses BELOW moving average |
| **Death Cross** | 50-day MA crosses below 200-day MA |
| **RSI** | Crosses below 70 (exiting overbought) |
| **MACD** | MACD line crosses below Signal line |
| **Volume** | Price down + Volume up |
| **OBV** | Falling OBV + Falling price |

### Confirmation Strategy

**Never rely on ONE indicator! Use multiple confirmations:**

✅ **Strong Buy Example:**
- Price crosses above 50-day MA
- RSI is 35 (recovering from oversold)
- MACD bullish crossover
- Volume is above average

✅ **Strong Sell Example:**
- Price crosses below 50-day MA
- RSI is 75 (overbought)
- MACD bearish crossover
- Volume is increasing

---

# INTERMEDIATE TECHNICAL ANALYSIS

---

## Bollinger Bands & Volatility

### Bollinger Bands (Module 07)

**Components:**
1. **Upper Band** = Middle + (2 × StdDev)
2. **Middle Band** = 20-day SMA
3. **Lower Band** = Middle - (2 × StdDev)

**Default Settings**: 20, 2 (20-period, 2 standard deviations)

| Position | Interpretation | Action |
|----------|----------------|--------|
| Price at Upper Band | Overbought | Consider selling |
| Price at Lower Band | Oversold | Consider buying |
| Price at Middle Band | Neutral | Wait for direction |
| Narrow Bands | **Squeeze** - Low volatility | Big move coming soon! |
| Wide Bands | High volatility | Trend is strong |

**Formula:**
```
Middle Band = SMA(20)
Upper Band = Middle + (2 × Standard Deviation)
Lower Band = Middle - (2 × Standard Deviation)
Band Width = (Upper - Lower) / Middle
%B = (Price - Lower) / (Upper - Lower)
```

### ATR (Average True Range)

**What it measures**: Absolute volatility (in RM, not %)

**Formula:**
```
True Range = Max of:
  - High - Low
  - |High - Previous Close|
  - |Low - Previous Close|

ATR = 14-day average of True Range
```

**Usage:**
- **Stop-Loss**: Entry - (2 × ATR)
- **Position Sizing**: Adjust based on ATR
- **Volatility Check**: High ATR = volatile stock

| ATR as % of Price | Volatility | Risk Level |
|-------------------|------------|------------|
| < 2% | Low | Conservative |
| 2-5% | Moderate | Normal |
| > 5% | High | Aggressive |

### Bollinger Band Squeeze

**What it is**: When bands are at multi-month narrowest width

**How to detect:**
```python
BB_Width_Min = BB_Width.rolling(125).min()
Is_Squeeze = BB_Width <= (BB_Width_Min × 1.1)
```

**Trading Strategy:**
1. Identify squeeze (narrow bands)
2. Wait for breakout (price closes outside bands)
3. Enter in direction of breakout
4. Stop-loss at opposite band

---

## Advanced Oscillators

### Stochastic Oscillator (Module 08)

**Components:**
- **%K** (fast line) = Current momentum
- **%D** (slow line) = 3-day SMA of %K

**Default Settings**: 14, 3, 3

**Formula:**
```
%K = ((Close - Lowest Low) / (Highest High - Lowest Low)) × 100
%D = 3-day SMA of %K
```

**Range**: 0 to 100

| Level | Zone | Meaning |
|-------|------|---------|
| > 80 | Overbought | Potential sell |
| 20-80 | Neutral | Normal range |
| < 20 | Oversold | Potential buy |

**Trading Signals:**
- %K crosses ABOVE %D in oversold zone (< 20) = **BUY**
- %K crosses BELOW %D in overbought zone (> 80) = **SELL**

### Williams %R

**What it is**: Inverted Stochastic (more sensitive)

**Formula:**
```
Williams %R = ((Highest High - Close) / (Highest High - Lowest Low)) × -100
```

**Range**: 0 to -100 (inverted!)

| Level | Zone | Meaning |
|-------|------|---------|
| > -20 | Overbought | Potential sell |
| -20 to -80 | Neutral | Normal range |
| < -80 | Oversold | Potential buy |

**Comparison:**

| Feature | Stochastic | Williams %R |
|---------|------------|-------------|
| Lines | 2 (%K + %D) | 1 line |
| Scale | 0 to 100 | 0 to -100 |
| Speed | Slower | Faster |
| Best for | Confirmed signals | Early signals |

---

## Fibonacci Retracements

### Fibonacci Levels (Module 09)

**Key Levels:**
- **23.6%** - Shallow retracement
- **38.2%** - Moderate retracement (first support)
- **50.0%** - Psychological level (not Fibonacci, but widely used)
- **61.8%** - **Golden Ratio** (strongest support)
- **78.6%** - Extreme retracement

**Calculation:**
```
1. Find Swing High and Swing Low
2. Range = High - Low
3. For Uptrend:
   - 23.6% = Low + (Range × 0.236)
   - 38.2% = Low + (Range × 0.382)
   - 50.0% = Low + (Range × 0.50)
   - 61.8% = Low + (Range × 0.618)
   - 78.6% = Low + (Range × 0.786)
```

**Trading Strategy:**
1. Identify trend (uptrend or downtrend)
2. Wait for retracement to Fibonacci level
3. Enter when price bounces off 38.2%, 50%, or 61.8%
4. Stop-loss below next Fibonacci level
5. Target: Previous swing high/low

**Best Practices:**
- **61.8%** is strongest level (Golden Ratio)
- Combine with oscillators for confirmation
- Use in trending markets only

---

## Multi-Timeframe Analysis

### The Top-Down Approach (Module 10)

**Three Essential Timeframes:**

| Timeframe | Purpose | What to Look For |
|-----------|---------|------------------|
| **Monthly** | Long-term direction | Overall trend (forest view) |
| **Weekly** | Medium-term trend | Confirmation (trees view) |
| **Daily** | Entry/exit timing | Precise signals (leaves view) |

### The Golden Rule

**"Trade in the direction of the higher timeframe trend"**

**Examples:**
- Monthly uptrend + Weekly uptrend → Look for BUY on daily pullbacks
- Monthly downtrend + Weekly downtrend → Look for SELL on daily rallies
- Mixed signals → **STAY OUT** (too risky)

### Timeframe Alignment

| Monthly | Weekly | Daily | Action |
|---------|--------|-------|--------|
| ↑ | ↑ | ↑ | **STRONG BUY** |
| ↓ | ↓ | ↓ | **STRONG SELL** |
| ↑ | ↑ | ↓ | Buy on pullback |
| ↓ | ↓ | ↑ | Sell on rally |
| ↑ | ↓ | ↑ | **MIXED - Avoid** |

---

## ADX & Chart Patterns

### ADX (Average Directional Index) - Module 11

**What it measures**: Trend STRENGTH (not direction)

**Components:**
- **ADX** = Strength of trend (0-100)
- **+DI** = Upward pressure
- **-DI** = Downward pressure

**Default Period**: 14 days

| ADX Value | Trend Strength | Strategy |
|-----------|----------------|----------|
| 0-25 | Weak/No trend | Use oscillators, avoid trend trading |
| 25-50 | Strong trend | Trend trading works well |
| 50-75 | Very strong trend | Excellent for trend following |
| 75-100 | Extremely strong | Rare, powerful trend |

**Trading Rules:**
```
ADX > 25 + +DI > -DI = Trade UPTREND
ADX > 25 + -DI > +DI = Trade DOWNTREND
ADX < 25 = Use oscillator strategies (don't trend trade)
```

### Chart Patterns Quick Reference

**Continuation Patterns:**
- **Bull Flag**: Brief consolidation in uptrend → continues up
- **Ascending Triangle**: Flat resistance + rising support → breakout up
- **Pennant**: Small symmetrical triangle → continues trend

**Reversal Patterns:**
- **Head & Shoulders**: 3 peaks, middle highest → reversal down
- **Double Top**: Two peaks at same level → reversal down
- **Double Bottom**: Two valleys at same level → reversal up

---

## Risk Management & Position Sizing

### The 1-2% Rule (Module 12) - **MOST IMPORTANT!**

**Never risk more than 1-2% of capital per trade**

### Position Size Calculator

**Formula:**
```
Position Size = (Account Size × Risk %) / (Entry Price - Stop Loss)
```

**Example:**
- Account: RM 10,000
- Risk: 2% = RM 200
- Entry: RM 1.50
- Stop: RM 1.40
- Risk per share: RM 0.10

**Position Size** = RM 200 / RM 0.10 = **2,000 shares**

### Risk-Reward Ratio

**Minimum**: Never take trades with less than **1:2** risk-reward

**Formula:**
```
Risk-Reward = (Target - Entry) / (Entry - Stop Loss)
```

**Example:**
- Entry: RM 1.50
- Stop: RM 1.40 (Risk = RM 0.10)
- Target: RM 1.70 (Reward = RM 0.20)
- **Ratio: 1:2** ✅ Good!

**Win Rate Needed:**
- 1:1 Risk-Reward → Need 50% win rate
- 1:2 Risk-Reward → Need only 33% win rate
- 1:3 Risk-Reward → Need only 25% win rate

### Portfolio Heat

**Maximum total risk across all positions: 6%**

**Example:**
- Account: RM 10,000
- Risk per trade: 2%
- **Maximum 3 positions simultaneously**

**Formula:**
```
Portfolio Heat = Sum of all position risks / Account Size
```

### Position Sizing Table

| Account Size | 1% Risk | 2% Risk | Max Positions (6% heat) |
|--------------|---------|---------|------------------------|
| RM 5,000 | RM 50 | RM 100 | 3 positions |
| RM 10,000 | RM 100 | RM 200 | 3 positions |
| RM 20,000 | RM 200 | RM 400 | 3 positions |
| RM 50,000 | RM 500 | RM 1,000 | 3 positions |

---

## Stock Screening

### Screening Criteria (Module 13)

**Essential Filters:**

| Criterion | Filter | Purpose |
|-----------|--------|---------|
| **Trend** | Price > SMA 50 | Uptrend confirmation |
| **Momentum** | 40 < RSI < 70 | Not extreme |
| **Volume** | Volume > 20-day avg | Liquidity |
| **Strength** | ADX > 25 | Strong trend |

### Stock Scoring System

**Score Components (0-100):**
- Trend (40 points): Price above SMA 50
- Momentum (30 points): RSI in healthy range
- Volume (20 points): Above average
- Position (10 points): RSI near 50

**Interpretation:**
- **70-100**: Strong opportunity (Top watchlist)
- **50-70**: Moderate opportunity (Monitor)
- **0-50**: Weak opportunity (Skip)

### Screening Example (Python)

```python
def screen_stock(ticker):
    # Calculate indicators
    data['SMA_50'] = data['Close'].rolling(50).mean()
    data['RSI'] = calculate_rsi(data['Close'])
    data['Vol_Avg'] = data['Volume'].rolling(20).mean()

    # Score
    score = 0
    if data['Close'].iloc[-1] > data['SMA_50'].iloc[-1]:
        score += 40  # Uptrend

    rsi = data['RSI'].iloc[-1]
    if 40 <= rsi <= 70:
        score += 30  # Healthy momentum

    if data['Volume'].iloc[-1] > data['Vol_Avg'].iloc[-1]:
        score += 20  # High volume

    if 45 <= rsi <= 55:
        score += 10  # Sweet spot

    return score
```

### Daily Screening Routine

**Professional traders do this EVERY day:**

1. **Before Market Opens**:
   - Run screener on watchlist
   - Identify top 3-5 opportunities

2. **During Market**:
   - Monitor top opportunities
   - Wait for entry signals

3. **After Market**:
   - Review trades
   - Update watchlist

---

## Quick Python Commands

### Fetching Stock Data

```python
import yfinance as yf

# Get Malaysian stock data
ticker = "0310.KL"  # UUE Holdings
stock = yf.Ticker(ticker)
data = stock.history(period="6mo")  # 6 months of data
```

### Calculating Moving Averages

```python
# Simple Moving Average
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Exponential Moving Average
data['EMA_12'] = data['Close'].ewm(span=12).mean()
```

### Using pandas-ta for Indicators

```python
import pandas_ta as ta

# RSI
data['RSI'] = ta.rsi(data['Close'], length=14)

# MACD
macd = ta.macd(data['Close'])
data['MACD'] = macd['MACD_12_26_9']
data['Signal'] = macd['MACDs_12_26_9']
data['Histogram'] = macd['MACDh_12_26_9']

# OBV
data['OBV'] = ta.obv(data['Close'], data['Volume'])
```

### Quick Price Statistics

```python
# Latest price
latest = data['Close'].iloc[-1]

# Price change
change = ((data['Close'].iloc[-1] / data['Close'].iloc[0]) - 1) * 100

# Volatility (standard deviation)
volatility = data['Close'].pct_change().std() * 100
```

---

## Risk Management Rules

### Position Sizing

- **Conservative**: Risk only 1-2% of capital per trade
- **Moderate**: Risk 2-5% of capital per trade
- **Aggressive**: Risk 5-10% of capital per trade (NOT recommended for beginners!)

### Stop Loss Guidelines

- **Tight**: 2-3% below entry (for day traders)
- **Medium**: 5-8% below entry (for swing traders)
- **Wide**: 10-15% below entry (for long-term investors)

### The 2% Rule

**Never risk more than 2% of your total capital on a single trade.**

Example:
- Capital: RM 10,000
- Maximum risk per trade: RM 200 (2%)
- If stop loss is 5%: Buy RM 4,000 worth (5% of RM 4,000 = RM 200)

---

## Common Mistakes to Avoid

| Mistake | Why It's Bad | Better Approach |
|---------|--------------|-----------------|
| Using only ONE indicator | False signals | Use 2-3 indicators together |
| Ignoring volume | Miss weak signals | Always check volume |
| No stop loss | Unlimited losses | Set stop loss BEFORE buying |
| Chasing performance | Buy high, sell low | Wait for pullbacks |
| Over-trading | High fees eat profits | Be patient, quality > quantity |
| Revenge trading | Emotional decisions | Take a break after losses |

---

## Volatility Reference

| Standard Deviation | Volatility Level | Risk Level | Suitable For |
|-------------------|------------------|------------|--------------|
| < 1% | Low | Conservative | Retirees, beginners |
| 1-2% | Medium | Moderate | Balanced investors |
| 2-3% | High | Aggressive | Experienced traders |
| > 3% | Very High | Very Risky | Professionals only |

---

## Malaysian Stock Ticker Format

### How to Format Tickers for Yahoo Finance

```
Format: [Stock Code].KL

Examples:
0310.KL = UUE Holdings Berhad
1155.KL = Malayan Banking Berhad (Maybank)
1295.KL = Public Bank Berhad
5296.KL = Tenaga Nasional Berhad (TNB)
6012.KL = Petronas Chemicals Group Berhad
```

**Find stock codes at:** [Bursa Malaysia](https://www.bursamalaysia.com/)

---

## Time Frames for Different Trading Styles

| Style | Holding Period | Best Indicators | Recommended For |
|-------|----------------|-----------------|-----------------|
| **Day Trading** | Minutes-Hours | RSI, MACD, Volume | Full-time traders |
| **Swing Trading** | Days-Weeks | MA, RSI, MACD | Part-time traders |
| **Position Trading** | Weeks-Months | MA (50, 200), Trends | Working professionals |
| **Investing** | Months-Years | MA (200), Fundamentals | Long-term investors |

---

## Key Formulas

### Percentage Change
```
% Change = ((New Price - Old Price) / Old Price) × 100
```

### Daily Return
```
Daily Return % = ((Today's Close - Yesterday's Close) / Yesterday's Close) × 100
```

### Volatility (Standard Deviation)
```
1. Calculate daily returns for all days
2. Find the average daily return
3. Calculate how much each day deviates from average
4. Result = volatility measure
```

### Support and Resistance
```
Support = Price level where buying pressure exceeds selling (floor)
Resistance = Price level where selling pressure exceeds buying (ceiling)
```

---

## Quick Decision Tree

### Should I Buy?

```
START
  ↓
Is price above 50-day MA?
  ├─ YES → Check RSI
  │         ├─ RSI < 70 → Check MACD
  │         │             ├─ Bullish crossover → Check Volume
  │         │             │                      ├─ High volume → ✅ STRONG BUY
  │         │             │                      └─ Low volume → ⚠️ WEAK BUY
  │         │             └─ No crossover → ⏸️ WAIT
  │         └─ RSI ≥ 70 → ❌ DON'T BUY (Overbought)
  └─ NO → ⏸️ WAIT (Downtrend)
```

---

## Resources

### Websites
- **Bursa Malaysia**: [bursamalaysia.com](https://www.bursamalaysia.com/)
- **i3investor**: [klse.i3investor.com](https://klse.i3investor.com/)
- **TradingView**: [tradingview.com](https://www.tradingview.com/)
- **Investopedia**: [investopedia.com](https://www.investopedia.com/)

### Python Libraries
- **yfinance**: Free stock data
- **pandas**: Data manipulation
- **pandas-ta**: Technical indicators
- **matplotlib**: Charts
- **plotly**: Interactive charts

---

## Final Reminders

### ⚠️ Important Warnings

1. **Technical analysis is NOT a crystal ball** - It increases probabilities, doesn't guarantee results
2. **Past performance ≠ Future results** - Patterns can fail
3. **Always use stop losses** - Protect your capital
4. **Never invest money you can't afford to lose** - Only use risk capital
5. **This is education, not financial advice** - Do your own research
6. **Practice with paper trading first** - Test your strategy before using real money

### 🎯 Keys to Success

1. **Be Patient** - Wait for high-probability setups
2. **Be Disciplined** - Stick to your strategy
3. **Be Consistent** - Use the same indicators and rules
4. **Keep Learning** - Markets evolve, so should you
5. **Manage Risk** - Preservation of capital is #1 priority
6. **Review Trades** - Learn from both wins and losses

---

**Remember**: The goal isn't to predict every move correctly. The goal is to win more than you lose, and to lose small when you're wrong!

**Good luck with your technical analysis journey! 📈**
