"""
COMPLETE KLSE Backtesting Notebook Builder
Generates full educational notebook with all 12 sections
"""

import json


def create_notebook():
    """Build complete notebook"""

    nb = {
        "cells": [],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    def add_md(text):
        """Add markdown cell"""
        nb["cells"].append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [text] if isinstance(text, list) else [text],
            }
        )

    def add_code(code):
        """Add code cell"""
        nb["cells"].append(
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [code] if isinstance(code, list) else [code],
            }
        )

    print("Building notebook with all sections...")

    # SECTION 1: TITLE & INTRO
    add_md(
        "# KLSE Advanced: Backtesting Trading Strategies\n\n## Welcome!\n\nThis intermediate notebook teaches **backtesting** - testing trading strategies on historical Malaysian stock data.\n\n### What You'll Learn:\n1. Build backtesting framework\n2. Test 3 trading strategies (MA Crossover, RSI, MACD)\n3. Calculate performance metrics\n4. Manage risk properly\n5. Avoid common pitfalls\n\n**Time:** 3-4 hours | **Level:** Intermediate | **Prerequisites:** KLSE Stock Screener notebook\n\n**Disclaimer:** Educational purposes only. Past performance does not guarantee future results.\n\n---"
    )

    add_md(
        "## 1. What is Backtesting?\n\n**Backtesting** = Testing a trading strategy on past data to see if it would have worked.\n\n### Why Backtest?\n- Test ideas risk-free\n- Compare strategies\n- Build confidence\n- Find weaknesses\n\n### How It Works:\n1. Define strategy rules\n2. Get historical data\n3. Simulate trades\n4. Calculate results\n5. Analyze performance\n\n### Realistic Expectations:\n- 10-15% annual: Good\n- 15-20% annual: Very good\n- 20%+: Excellent (but verify!)\n- 50%+: Likely overfitted\n\n### We'll Build:\n1. MA Crossover Strategy\n2. RSI Mean Reversion\n3. MACD Momentum\n\n---"
    )

    # SECTION 2: SETUP
    add_md("## 2. Setup & Imports\n\nImport libraries (same as beginner notebook):")

    add_code(
        "# Data & Analysis\nimport yfinance as yf\nimport pandas as pd\nimport numpy as np\nimport pandas_ta as ta\n\n# Visualization\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport plotly.graph_objects as go\nimport plotly.express as px\n\n# Utilities\nfrom datetime import datetime, timedelta\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Config\nsns.set_style('whitegrid')\nplt.rcParams['figure.figsize'] = (14, 7)\nnp.random.seed(42)\n\nprint('[OK] Libraries imported')\nprint(f'Today: {datetime.now().strftime(\"%Y-%m-%d\")}')"
    )

    # SECTION 3: DATA FUNCTIONS
    add_md("## 3. Data & Framework\n\nBuild our backtesting foundation:")

    add_code(
        "def get_data(ticker, start, end):\n    '''Fetch historical data'''\n    try:\n        df = yf.download(ticker, start=start, end=end, progress=False)\n        if df.empty:\n            print(f'No data for {ticker}')\n            return None\n        print(f'[OK] {len(df)} days for {ticker}')\n        return df\n    except Exception as e:\n        print(f'Error: {e}')\n        return None\n\n# Test\ntest_df = get_data('1155.KL', '2021-01-01', '2023-12-31')\nif test_df is not None:\n    print(f'\\nData: {test_df.index[0].date()} to {test_df.index[-1].date()}')\n    print(f'Columns: {list(test_df.columns)}')"
    )

    add_code(
        "def add_indicators(df):\n    '''Add technical indicators'''\n    df = df.copy()\n    \n    def safe(result):\n        if result is None:\n            return None\n        if isinstance(result, pd.Series):\n            return result\n        if isinstance(result, pd.DataFrame):\n            return result.iloc[:, 0] if len(result.columns) > 0 else None\n        return result\n    \n    df['SMA_20'] = safe(df.ta.sma(20))\n    df['SMA_50'] = safe(df.ta.sma(50))\n    df['SMA_200'] = safe(df.ta.sma(200))\n    df['RSI'] = safe(df.ta.rsi(14))\n    \n    macd = df.ta.macd()\n    if macd is not None:\n        df = pd.concat([df, macd], axis=1)\n    \n    return df\n\nprint('[OK] add_indicators() ready')"
    )

    # SECTION 4: MA CROSSOVER STRATEGY
    add_md(
        "## 4. Strategy #1: Moving Average Crossover\n\n### Concept:\n**BUY:** SMA-50 crosses above SMA-200 (Golden Cross)\n**SELL:** SMA-50 crosses below SMA-200 (Death Cross)\n\n### When it works:\n- Strong trending markets\n- Clear directional moves\n\n### When it fails:\n- Sideways/choppy markets\n- Too many false signals\n\n---"
    )

    add_code(
        "def ma_crossover(df):\n    '''Generate MA crossover signals'''\n    df = df.copy()\n    df['Signal'] = 0\n    df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1\n    df['Position'] = df['Signal'].diff()\n    return df\n\nprint('[OK] ma_crossover() strategy ready')"
    )

    add_code(
        "def backtest(df, capital=100000, commission=0.001):\n    '''Backtest strategy'''\n    df = df.copy()\n    \n    # Returns\n    df['Returns'] = df['Close'].pct_change()\n    df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)\n    \n    # Commission\n    df['Commission'] = abs(df['Position']) * commission\n    df['Strategy_Returns'] -= df['Commission']\n    \n    # Cumulative\n    df['Cum_Market'] = (1 + df['Returns']).cumprod()\n    df['Cum_Strategy'] = (1 + df['Strategy_Returns']).cumprod()\n    \n    # Portfolio value\n    df['Portfolio'] = capital * df['Cum_Strategy']\n    df['BuyHold'] = capital * df['Cum_Market']\n    \n    return df\n\nprint('[OK] backtest() engine ready')"
    )

    # Test the strategy
    add_md("### Test MA Crossover on Maybank:")

    add_code(
        "# Run backtest\ndf_may = get_data('1155.KL', '2021-01-01', '2023-12-31')\n\nif df_may is not None:\n    df_may = add_indicators(df_may)\n    df_may = df_may.dropna()\n    df_may = ma_crossover(df_may)\n    df_may = backtest(df_may)\n    \n    buys = (df_may['Position'] == 1).sum()\n    sells = (df_may['Position'] == -1).sum()\n    \n    final = df_may['Portfolio'].iloc[-1]\n    bh = df_may['BuyHold'].iloc[-1]\n    \n    strat_ret = ((final / 100000) - 1) * 100\n    bh_ret = ((bh / 100000) - 1) * 100\n    \n    print('='*60)\n    print('MA CROSSOVER BACKTEST - MAYBANK')\n    print('='*60)\n    print(f'BUY signals: {buys}')\n    print(f'SELL signals: {sells}')\n    print(f'\\nInitial: RM 100,000')\n    print(f'Final: RM {final:,.2f}')\n    print(f'Strategy Return: {strat_ret:+.2f}%')\n    print(f'\\nBuy & Hold: RM {bh:,.2f}')\n    print(f'B&H Return: {bh_ret:+.2f}%')\n    print(f'\\nDifference: {strat_ret - bh_ret:+.2f}%')\n    print('='*60)"
    )

    # Visualization
    add_code(
        "# Visualize results\nif df_may is not None:\n    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))\n    \n    # Price & signals\n    ax1.plot(df_may.index, df_may['Close'], 'k-', label='Price', lw=1.5)\n    ax1.plot(df_may.index, df_may['SMA_50'], 'orange', label='SMA-50', alpha=0.7)\n    ax1.plot(df_may.index, df_may['SMA_200'], 'blue', label='SMA-200', alpha=0.7)\n    \n    buys = df_may[df_may['Position'] == 1]\n    sells = df_may[df_may['Position'] == -1]\n    ax1.scatter(buys.index, buys['Close'], marker='^', c='g', s=100, label='BUY', zorder=5)\n    ax1.scatter(sells.index, sells['Close'], marker='v', c='r', s=100, label='SELL', zorder=5)\n    \n    ax1.set_ylabel('Price (RM)')\n    ax1.set_title('MA Crossover Strategy - Maybank', fontweight='bold')\n    ax1.legend()\n    ax1.grid(alpha=0.3)\n    \n    # Portfolio value\n    ax2.plot(df_may.index, df_may['Portfolio'], 'g-', label='Strategy', lw=2)\n    ax2.plot(df_may.index, df_may['BuyHold'], 'b--', label='Buy & Hold', lw=2)\n    ax2.axhline(100000, color='gray', ls=':', alpha=0.5)\n    \n    ax2.set_ylabel('Portfolio Value (RM)')\n    ax2.set_xlabel('Date')\n    ax2.legend()\n    ax2.grid(alpha=0.3)\n    \n    plt.tight_layout()\n    plt.show()\n    \n    print('Green triangles = BUY | Red triangles = SELL')"
    )

    # SECTION 5: PERFORMANCE METRICS
    add_md("## 5. Performance Metrics\n\nLet's calculate proper performance metrics:")

    add_code(
        "def calc_metrics(df, capital=100000):\n    '''Calculate performance metrics'''\n    returns = df['Strategy_Returns'].dropna()\n    \n    # Total return\n    total_ret = ((df['Portfolio'].iloc[-1] / capital) - 1) * 100\n    \n    # CAGR\n    days = (df.index[-1] - df.index[0]).days\n    years = days / 365.25\n    cagr = ((df['Portfolio'].iloc[-1] / capital) ** (1/years) - 1) * 100\n    \n    # Sharpe (assuming 3% risk-free)\n    excess = returns - (0.03/252)\n    sharpe = np.sqrt(252) * excess.mean() / returns.std()\n    \n    # Max Drawdown\n    cummax = df['Portfolio'].cummax()\n    dd = (df['Portfolio'] - cummax) / cummax\n    max_dd = dd.min() * 100\n    \n    # Win rate\n    wins = (returns > 0).sum()\n    total = len(returns[returns != 0])\n    win_rate = (wins / total * 100) if total > 0 else 0\n    \n    return {\n        'Total Return (%)': round(total_ret, 2),\n        'CAGR (%)': round(cagr, 2),\n        'Sharpe Ratio': round(sharpe, 2),\n        'Max Drawdown (%)': round(max_dd, 2),\n        'Win Rate (%)': round(win_rate, 2),\n        'Total Trades': int(total)\n    }\n\nprint('[OK] calc_metrics() ready')"
    )

    add_code(
        "# Calculate metrics for Maybank MA strategy\nif df_may is not None:\n    metrics = calc_metrics(df_may)\n    \n    print('='*50)\n    print('PERFORMANCE METRICS - MA CROSSOVER')\n    print('='*50)\n    for key, val in metrics.items():\n        print(f'{key:<25}: {val}')\n    print('='*50)\n    \n    print('\\nInterpretation:')\n    if metrics['Sharpe Ratio'] > 1:\n        print('[OK] Sharpe > 1: Good risk-adjusted returns')\n    else:\n        print('[WARNING] Sharpe < 1: Poor risk-adjusted returns')\n    \n    if abs(metrics['Max Drawdown (%)']) < 20:\n        print('[OK] Drawdown < 20%: Acceptable risk')\n    else:\n        print('[WARNING] Drawdown > 20%: High risk')"
    )

    # SECTION 6: RSI STRATEGY
    add_md(
        "## 6. Strategy #2: RSI Mean Reversion\n\n### Concept:\n**BUY:** RSI < 30 (oversold)\n**SELL:** RSI > 70 (overbought)\n\n### Logic:\nWhen price drops too much (RSI < 30), it tends to bounce back.\nWhen price rises too much (RSI > 70), it tends to pull back.\n\n---"
    )

    add_code(
        "def rsi_strategy(df):\n    '''RSI mean reversion strategy'''\n    df = df.copy()\n    df['Signal'] = 0\n    \n    # Buy when oversold, sell when overbought\n    df.loc[df['RSI'] < 30, 'Signal'] = 1\n    df.loc[df['RSI'] > 70, 'Signal'] = 0\n    \n    # Forward fill (hold position until next signal)\n    df['Signal'] = df['Signal'].replace(0, np.nan).ffill().fillna(0)\n    df['Position'] = df['Signal'].diff()\n    \n    return df\n\nprint('[OK] rsi_strategy() ready')"
    )

    add_code(
        "# Test RSI strategy on Maybank\ndf_rsi = get_data('1155.KL', '2021-01-01', '2023-12-31')\n\nif df_rsi is not None:\n    df_rsi = add_indicators(df_rsi)\n    df_rsi = df_rsi.dropna()\n    df_rsi = rsi_strategy(df_rsi)\n    df_rsi = backtest(df_rsi)\n    \n    metrics_rsi = calc_metrics(df_rsi)\n    \n    print('='*50)\n    print('RSI MEAN REVERSION - MAYBANK')\n    print('='*50)\n    for k, v in metrics_rsi.items():\n        print(f'{k:<25}: {v}')\n    print('='*50)"
    )

    # SECTION 7: MACD STRATEGY
    add_md(
        "## 7. Strategy #3: MACD Momentum\n\n### Concept:\n**BUY:** MACD crosses above signal line\n**SELL:** MACD crosses below signal line\n\n---"
    )

    add_code(
        "def macd_strategy(df):\n    '''MACD momentum strategy'''\n    df = df.copy()\n    df['Signal'] = 0\n    \n    if 'MACD_12_26_9' in df.columns and 'MACDs_12_26_9' in df.columns:\n        df.loc[df['MACD_12_26_9'] > df['MACDs_12_26_9'], 'Signal'] = 1\n        df['Position'] = df['Signal'].diff()\n    \n    return df\n\nprint('[OK] macd_strategy() ready')"
    )

    add_code(
        "# Test MACD strategy\ndf_macd = get_data('1155.KL', '2021-01-01', '2023-12-31')\n\nif df_macd is not None:\n    df_macd = add_indicators(df_macd)\n    df_macd = df_macd.dropna()\n    df_macd = macd_strategy(df_macd)\n    df_macd = backtest(df_macd)\n    \n    metrics_macd = calc_metrics(df_macd)\n    \n    print('='*50)\n    print('MACD MOMENTUM - MAYBANK')\n    print('='*50)\n    for k, v in metrics_macd.items():\n        print(f'{k:<25}: {v}')\n    print('='*50)"
    )

    # SECTION 8: RISK MANAGEMENT
    add_md(
        "## 8. Risk Management\n\n### Stop-Loss Implementation\nLimit losses by exiting when price drops X%:\n\n---"
    )

    add_code(
        "def add_stop_loss(df, stop_pct=0.05):\n    '''Add stop-loss (5% default)'''\n    df = df.copy()\n    entry_price = None\n    \n    for i in range(len(df)):\n        if df['Position'].iloc[i] == 1:  # Entry\n            entry_price = df['Close'].iloc[i]\n        elif entry_price is not None and df['Signal'].iloc[i] == 1:\n            # Check stop-loss\n            if df['Close'].iloc[i] < entry_price * (1 - stop_pct):\n                df.loc[df.index[i], 'Signal'] = 0\n                df.loc[df.index[i], 'Position'] = -1\n                entry_price = None\n        elif df['Position'].iloc[i] == -1:\n            entry_price = None\n    \n    return df\n\nprint('[OK] add_stop_loss() ready')\nprint('Adds 5% stop-loss to protect capital')"
    )

    # SECTION 9: PORTFOLIO BACKTEST
    add_md("## 9. Multi-Stock Portfolio\n\nTest strategy across multiple Malaysian stocks:\n\n---")

    add_code(
        "# Test MA Crossover on 5 stocks\nstocks = ['1155.KL', '1295.KL', '1023.KL', '5296.KL', '4197.KL']\nnames = ['Maybank', 'PublicBank', 'CIMB', 'Tenaga', 'Maxis']\n\nresults = []\n\nfor ticker, name in zip(stocks, names):\n    print(f'Testing {name}...')\n    df = get_data(ticker, '2021-01-01', '2023-12-31')\n    if df is not None:\n        df = add_indicators(df)\n        df = df.dropna()\n        df = ma_crossover(df)\n        df = backtest(df)\n        m = calc_metrics(df)\n        m['Stock'] = name\n        results.append(m)\n\n# Show results\nimport pandas as pd\nresults_df = pd.DataFrame(results)\nprint('\\n' + '='*70)\nprint('MA CROSSOVER - PORTFOLIO RESULTS')\nprint('='*70)\nprint(results_df.to_string(index=False))\nprint('='*70)"
    )

    # SECTION 10: PITFALLS
    add_md(
        "## 10. Common Pitfalls\n\n### 1. Overfitting\nMaking strategy work TOO well on past data\n\n### 2. Look-ahead Bias\nUsing future information\n\n### 3. Ignoring Costs\nForgetting commissions and slippage\n\n### 4. Survivorship Bias\nOnly testing stocks that still exist\n\n**How to avoid:** Use out-of-sample testing, realistic costs, and diverse data\n\n---"
    )

    # SECTION 11: COMPARISON
    add_md("## 11. Strategy Comparison\n\nCompare all 3 strategies:\n\n---")

    add_code(
        "# Compare strategies on Maybank\ncomparison = [\n    {'Strategy': 'MA Crossover', **metrics},\n    {'Strategy': 'RSI Mean Reversion', **metrics_rsi},\n    {'Strategy': 'MACD Momentum', **metrics_macd}\n]\n\ncomp_df = pd.DataFrame(comparison)\nprint('='*70)\nprint('STRATEGY COMPARISON - MAYBANK (2021-2023)')\nprint('='*70)\nprint(comp_df.to_string(index=False))\nprint('='*70)\n\n# Find best\nbest_idx = comp_df['CAGR (%)'].idxmax()\nprint(f'\\n[WINNER] {comp_df.loc[best_idx, \"Strategy\"]}')\nprint(f'Best CAGR: {comp_df.loc[best_idx, \"CAGR (%)\"]:.2f}%')"
    )

    # SECTION 12: NEXT STEPS
    add_md(
        '## 12. Next Steps\n\n### Congratulations!\n\nYou\'ve learned:\n- How to backtest strategies\n- Build MA, RSI, and MACD strategies\n- Calculate performance metrics\n- Manage risk\n- Avoid common mistakes\n\n### Advanced Topics:\n1. **Machine Learning** - Use ML to optimize strategies\n2. **Walk-Forward Testing** - More robust validation\n3. **Portfolio Optimization** - Modern Portfolio Theory\n4. **Options Strategies** - Hedging and income\n5. **Live Trading** - Deploy with proper risk management\n\n### Practice Exercises:\n1. Test strategies on different timeframes\n2. Combine multiple indicators\n3. Optimize parameters (MA lengths, RSI levels)\n4. Add position sizing rules\n5. Test on different market conditions\n\n### Resources:\n- "Evidence-Based Technical Analysis" - David Aronson\n- "Algorithmic Trading" - Ernest Chan\n- QuantStart.com - Free education\n- Backtrader library - Advanced backtesting\n\n**Remember:** Always paper trade before using real money!\n\n---\n\n## Thank You!\n\nHappy backtesting! May your strategies be profitable and your drawdowns minimal. 📈'
    )

    # Save notebook
    with open("klse_backtesting_strategies.ipynb", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"\\n[COMPLETE] Generated {len(nb['cells'])} cells across 12 sections")
    return nb


if __name__ == "__main__":
    nb = create_notebook()
    print(f"[OK] Notebook saved: klse_backtesting_strategies.ipynb")
    print(f"[OK] Total cells: {len(nb['cells'])}")
