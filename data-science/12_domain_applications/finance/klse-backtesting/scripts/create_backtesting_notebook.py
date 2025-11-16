"""
Create KLSE Advanced: Backtesting Trading Strategies Notebook
Intermediate level - Educational focus
"""

import json


def create_cell(cell_type, content, cell_id=None):
    """Helper to create notebook cells"""
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": content if isinstance(content, list) else [content],
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    if cell_id:
        cell["id"] = cell_id
    return cell


# Create notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11.0"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

# Section 1: Title and Introduction
notebook["cells"].append(
    create_cell(
        "markdown",
        [
            "# 📈 KLSE Advanced: Backtesting Trading Strategies\n",
            "\n",
            "## Welcome to Intermediate Stock Analysis!\n",
            "\n",
            "This notebook teaches you how to **backtest trading strategies** on Malaysian stocks. If you've completed the KLSE Stock Screener notebook, you're ready for this!\n",
            "\n",
            "### 🎯 What You'll Learn:\n",
            "\n",
            "1. **What is Backtesting?** - Test strategies on historical data\n",
            "2. **Build Trading Strategies** - Moving averages, RSI, MACD\n",
            "3. **Measure Performance** - Returns, Sharpe ratio, drawdown\n",
            "4. **Manage Risk** - Stop-loss, position sizing\n",
            "5. **Avoid Pitfalls** - Overfitting, bias, unrealistic assumptions\n",
            "6. **Compare Strategies** - Find what works best\n",
            "\n",
            "### 📋 Prerequisites:\n",
            "\n",
            "- Completed KLSE Stock Screener notebook (or equivalent knowledge)\n",
            "- Understand DataFrames, functions, loops\n",
            "- Know basic technical indicators (SMA, RSI, MACD)\n",
            "- Have Python environment set up\n",
            "\n",
            "### ⚠️ Important Disclaimer:\n",
            "\n",
            "**This is for EDUCATIONAL purposes only!**\n",
            "\n",
            "- Past performance ≠ future results\n",
            "- Backtesting has limitations (we'll discuss them!)\n",
            "- Always paper trade before using real money\n",
            "- Consult financial advisors for investment decisions\n",
            "- Markets can behave differently than historical data suggests\n",
            "\n",
            "### 🚀 Let's Begin!\n",
            "\n",
            "**Estimated time:** 3-4 hours to complete thoroughly\n",
            "\n",
            "---\n",
        ],
    )
)

notebook["cells"].append(
    create_cell(
        "markdown",
        [
            "## 1. What is Backtesting?\n",
            "\n",
            "### 🤔 The Big Question\n",
            "\n",
            "Imagine you have a trading idea:\n",
            '- *"Buy when stock price crosses above 50-day moving average"*\n',
            '- *"Sell when RSI goes above 70"*\n',
            "\n",
            "**But how do you know if it actually works?**\n",
            "\n",
            "That's where **backtesting** comes in!\n",
            "\n",
            "---\n",
            "\n",
            "### 📖 Definition\n",
            "\n",
            "**Backtesting** = Testing a trading strategy on historical data to see if it would have been profitable.\n",
            "\n",
            "**Example:**\n",
            "```\n",
            "Strategy: Buy when price > SMA-50\n",
            "Test Period: 2020-2023\n",
            "Result: Would have made 25% return\n",
            "```\n",
            "\n",
            "---\n",
            "\n",
            "### 🎯 Why Backtest?\n",
            "\n",
            "**Benefits:**\n",
            "- ✅ Test ideas WITHOUT risking real money\n",
            "- ✅ See historical performance and risk\n",
            "- ✅ Compare different strategies objectively\n",
            "- ✅ Build confidence in your approach\n",
            "- ✅ Identify weaknesses before going live\n",
            "\n",
            "**What Backtesting CAN'T Do:**\n",
            "- ❌ Guarantee future results\n",
            "- ❌ Account for all market conditions\n",
            "- ❌ Predict black swan events\n",
            "- ❌ Replace live trading experience\n",
            "\n",
            "---\n",
            "\n",
            "### ⚙️ How Backtesting Works\n",
            "\n",
            "**Step-by-step process:**\n",
            "\n",
            "1. **Define Strategy** - Clear entry/exit rules\n",
            "2. **Get Historical Data** - Price, volume, etc.\n",
            "3. **Simulate Trades** - Apply rules to past data\n",
            "4. **Calculate Results** - Returns, win rate, etc.\n",
            "5. **Analyze Performance** - Is it actually good?\n",
            "6. **Refine & Repeat** - Improve the strategy\n",
            "\n",
            "**Example Strategy Flow:**\n",
            "```\n",
            "Day 1: Price = RM 10.00, SMA-50 = RM 10.20 → Do nothing (price < SMA)\n",
            "Day 2: Price = RM 10.30, SMA-50 = RM 10.20 → BUY! (price crosses above)\n",
            "Day 15: Price = RM 9.80, SMA-50 = RM 10.10 → SELL (price crosses below)\n",
            "Result: Loss of RM 0.50 per share\n",
            "```\n",
            "\n",
            "---\n",
            "\n",
            "### 🚨 Common Pitfalls (We'll Cover These Later!)\n",
            "\n",
            "1. **Overfitting** - Strategy works on past data but nowhere else\n",
            "2. **Look-ahead Bias** - Using future information you wouldn't have had\n",
            "3. **Ignoring Costs** - Forgetting commissions, slippage, taxes\n",
            "4. **Survivorship Bias** - Only testing stocks that still exist\n",
            "5. **Cherry-picking** - Testing until you get good results\n",
            "\n",
            "**Don't worry!** We'll learn how to avoid ALL of these. 😊\n",
            "\n",
            "---\n",
            "\n",
            "### 💡 Realistic Expectations\n",
            "\n",
            "**Good backtesting results:**\n",
            "- 10-15% annual return = Good\n",
            "- 15-20% annual return = Very good\n",
            "- 20%+ annual return = Excellent (but be skeptical!)\n",
            "\n",
            "**If your backtest shows:**\n",
            "- 50%+ annual returns = 🚩 Probably overfitted or has errors\n",
            "- 100%+ annual returns = 🚩🚩 Definitely something wrong!\n",
            "\n",
            "**Remember:** Even professional hedge funds average 10-20% annually.\n",
            "\n",
            "---\n",
            "\n",
            "### 📊 What We'll Build Today\n",
            "\n",
            "We'll create a **simple but powerful backtesting framework** and test **three strategies**:\n",
            "\n",
            "1. **Moving Average Crossover** - Classic trend-following\n",
            "2. **RSI Mean Reversion** - Buy oversold, sell overbought\n",
            "3. **MACD Momentum** - Follow the momentum\n",
            "\n",
            "We'll compare them and see which works best for Malaysian stocks!\n",
            "\n",
            "---\n",
        ],
    )
)

# Add more cells...
print("Creating advanced backtesting notebook...")
print("This is a large notebook, building it in phases...")

# Save notebook (will continue in next part)
import os

os.makedirs("projects/klse-backtesting", exist_ok=True)
with open(
    "projects/klse-backtesting/klse_backtesting_strategies.ipynb", "w", encoding="utf-8"
) as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Phase 1: Created notebook structure with introduction")
print("Total cells so far:", len(notebook["cells"]))
