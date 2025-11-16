"""
Phase 2: Add detailed inline comments to ALL code cells
Plus more exercises, tips, and break down complex cells
"""

import json

# Read the enhanced notebook from Phase 1
with open("projects/klse-stock-screener/klse_stock_screener.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)


def create_markdown_cell(content, cell_id=None):
    cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": content if isinstance(content, list) else [content],
    }
    if cell_id:
        cell["id"] = cell_id
    return cell


def create_code_cell(source, cell_id=None):
    cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source if isinstance(source, list) else [source],
    }
    if cell_id:
        cell["id"] = cell_id
    return cell


# Enhanced versions of key code cells with detailed comments

# Cell: get_stock_data function with detailed comments
enhanced_get_stock_data = create_code_cell(
    [
        "# ========================================\n",
        "# CREATE A REUSABLE FUNCTION TO FETCH STOCK DATA\n",
        "# ========================================\n",
        "# Functions let us reuse code instead of writing it again and again\n",
        "\n",
        'def get_stock_data(ticker, period="1y"):\n',
        '    """\n',
        "    Fetch historical stock data for a Malaysian stock.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    ticker : str\n",
        "        Malaysian stock ticker (e.g., '1155.KL' for Maybank)\n",
        "    period : str\n",
        "        Time period: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'max'\n",
        "    \n",
        "    Returns:\n",
        "    --------\n",
        "    pd.DataFrame\n",
        "        Historical price data\n",
        '    """\n',
        "    try:  # Try to do this, and if it fails, handle the error gracefully\n",
        "        # Create a Ticker object for the stock\n",
        "        stock = yf.Ticker(ticker)\n",
        "        \n",
        "        # Download historical data for the specified period\n",
        "        hist = stock.history(period=period)\n",
        "        \n",
        "        # Check if we got any data back\n",
        "        if hist.empty:  # empty = no data found\n",
        '            print(f"❌ No data found for {ticker}")\n',
        "            return None  # Return nothing\n",
        "        \n",
        "        # Success! Print how many days we got\n",
        '        print(f"✅ Fetched {len(hist)} days of data for {ticker}")\n',
        "        return hist  # Return the data\n",
        "    \n",
        "    except Exception as e:  # If anything goes wrong\n",
        '        print(f"❌ Error fetching {ticker}: {e}")\n',
        "        return None\n",
        "\n",
        "# ========================================\n",
        "# TEST THE FUNCTION\n",
        "# ========================================\n",
        'print("Testing get_stock_data function:\\n")\n',
        "\n",
        "# Call our function to get 6 months of data for Tenaga Nasional\n",
        'tenaga_data = get_stock_data("5296.KL", period="6mo")\n',
        "\n",
        "# If we got data back (not None)\n",
        "if tenaga_data is not None:\n",
        "    # Access the last row's Close price using [-1] indexing\n",
        "    current_price = tenaga_data['Close'][-1]\n",
        '    print(f"\\nTenaga Nasional current price: RM {current_price:.2f}")\n',
        "    # .2f means format as decimal with 2 places: 9.95\n",
        "\n",
        "# 💡 TIP: The 'if ____ is not None' check prevents errors if data fetch failed\n",
    ]
)

# Find and replace the get_stock_data function cell
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "def get_stock_data(ticker" in source_text and "Testing get_stock_data" in source_text:
            nb["cells"][i] = enhanced_get_stock_data
            print(f"[OK] Enhanced get_stock_data function cell {i} with detailed comments")
            break

# Add more "Try It Yourself" exercises after technical indicators section
try_it_technical = create_markdown_cell(
    [
        "---\n",
        "## 🎯 Try It Yourself - Technical Analysis!\n",
        "\n",
        "Time to practice calculating and interpreting technical indicators:\n",
        "\n",
        "### **Exercise 1: Interpret RSI Values**\n",
        "Look at the RSI value calculated above:\n",
        "- Is it above 70 (overbought)?\n",
        "- Is it below 30 (oversold)?\n",
        "- What does this suggest about the stock's momentum?\n",
        "\n",
        "### **Exercise 2: Compare Different Stocks**\n",
        "Fetch technical indicators for different Malaysian stocks:\n",
        "```python\n",
        "# Try Public Bank\n",
        'df2 = get_stock_data("1295.KL", period="1y")\n',
        "df2 = add_technical_indicators(df2)\n",
        "print(f\"Public Bank RSI: {df2['RSI'][-1]:.2f}\")\n",
        "```\n",
        "\n",
        "### **Exercise 3: Golden Cross Detection**\n",
        'A "Golden Cross" happens when SMA-50 crosses above SMA-200 (bullish signal!):\n',
        "```python\n",
        "if df['SMA_50'][-1] > df['SMA_200'][-1]:\n",
        '    print("🟢 Golden Cross - Bullish!")\n',
        "else:\n",
        '    print("🔴 Death Cross - Bearish!")\n',
        "```\n",
        "\n",
        "### **Exercise 4: Find Trends**\n",
        "Check if price is in an uptrend:\n",
        "- Current price > SMA-20 = Short-term uptrend\n",
        "- Current price > SMA-50 = Medium-term uptrend  \n",
        "- Current price > SMA-200 = Long-term uptrend\n",
        "\n",
        "**Challenge:** Can you write code to check all three conditions?\n",
        "\n",
        "---\n",
        "\n",
        "### 💡 TIP: Understanding Moving Averages\n",
        "\n",
        "**SMA (Simple Moving Average)** = Average price over X days\n",
        "\n",
        "**Why 20, 50, and 200 days?**\n",
        "- **SMA-20**: Approximately 1 trading month (~20 trading days)\n",
        "- **SMA-50**: Approximately 2-3 trading months  \n",
        "- **SMA-200**: Approximately 1 trading year\n",
        "\n",
        "**How traders use them:**\n",
        "- Price ABOVE MAs = Uptrend (bullish)\n",
        "- Price BELOW MAs = Downtrend (bearish)\n",
        "- MAs act as support/resistance levels\n",
        "\n",
        "---\n",
    ]
)

# Insert after technical indicators section
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 5. Stock Screener Functionality" in source_text:
            nb["cells"].insert(i, try_it_technical)
            print("[OK] Added technical analysis exercises")
            break

# Add more tips
tip_rsi = create_markdown_cell(
    [
        "---\n",
        "### 💡 Understanding RSI (Relative Strength Index)\n",
        "\n",
        "**RSI measures momentum on a scale of 0-100**\n",
        "\n",
        "**How it works:**\n",
        "```\n",
        "RSI = 100 - (100 / (1 + RS))\n",
        "where RS = Average Gain / Average Loss over 14 days\n",
        "```\n",
        "\n",
        "**But you don't need to calculate it! pandas_ta does it for you.**\n",
        "\n",
        "**Interpretation:**\n",
        "- **RSI > 70**: Overbought - Stock might be too expensive, could drop soon\n",
        "- **RSI 30-70**: Neutral zone - Normal trading range\n",
        "- **RSI < 30**: Oversold - Stock might be too cheap, could rise soon\n",
        "\n",
        "**Example scenarios:**\n",
        "- RSI = 85: Stock has been rising fast. Be cautious! 🔴\n",
        "- RSI = 50: Normal momentum. No strong signal. 🟡\n",
        "- RSI = 25: Stock has been falling fast. Might be a buying opportunity! 🟢\n",
        "\n",
        "**⚠️ WARNING:** RSI alone isn't enough! Always consider:\n",
        "- Overall market conditions\n",
        "- Company fundamentals\n",
        "- Other technical indicators\n",
        "- News and events\n",
        "\n",
        "**Real-world usage:**\n",
        "Many traders wait for RSI to reverse from extreme levels:\n",
        "- **Bullish signal**: RSI drops below 30, then rises back above it\n",
        "- **Bearish signal**: RSI rises above 70, then drops back below it\n",
        "\n",
        "---\n",
    ]
)

# Insert RSI tip
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "RSI Signal" in source_text and "rsi_value" in source_text:
            nb["cells"].insert(i + 1, tip_rsi)
            print("[OK] Added RSI explanation tip")
            break

# Add screening strategy tip
tip_screening = create_markdown_cell(
    [
        "---\n",
        "### 💡 Building Your Own Screening Strategy\n",
        "\n",
        "Stock screening is like using filters on an online shopping site - you set criteria to find what you want!\n",
        "\n",
        "**Popular Screening Strategies:**\n",
        "\n",
        "#### **1. Value Investing (Warren Buffett Style)**\n",
        "```python\n",
        "value_stocks = screen_stocks(\n",
        "    stocks_df,\n",
        "    max_pe=15,           # Cheap valuation\n",
        "    min_dividend_yield=4 # Good income\n",
        ")\n",
        "```\n",
        "**Finds:** Undervalued, dividend-paying companies\n",
        "\n",
        "#### **2. Large Cap Stability**\n",
        "```python\n",
        "safe_stocks = screen_stocks(\n",
        "    stocks_df,\n",
        "    min_market_cap=50    # Only big, established companies\n",
        ")\n",
        "```\n",
        "**Finds:** Large, stable blue-chip companies\n",
        "\n",
        "#### **3. Sector Focus**\n",
        "```python\n",
        "tech_stocks = screen_stocks(\n",
        "    stocks_df,\n",
        "    sectors=['Technology']  # Only tech companies\n",
        ")\n",
        "```\n",
        "**Finds:** Companies in specific sectors\n",
        "\n",
        "#### **4. Dividend Hunters**\n",
        "```python\n",
        "income_stocks = screen_stocks(\n",
        "    stocks_df,\n",
        "    min_dividend_yield=5,\n",
        "    min_market_cap=10\n",
        ")\n",
        "```\n",
        "**Finds:** Reliable dividend payers\n",
        "\n",
        "**⚠️ IMPORTANT:** \n",
        "- Screening finds CANDIDATES, not guarantees!\n",
        "- Always research further before investing\n",
        "- Check company news, financial reports, and industry trends\n",
        "- Diversify - don't put all money in one stock\n",
        "\n",
        "---\n",
    ]
)

# Insert screening tip
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 6. Price Trend Visualization" in source_text:
            nb["cells"].insert(i, tip_screening)
            print("[OK] Added screening strategy tip")
            break

# Add Portfolio exercises
try_it_portfolio = create_markdown_cell(
    [
        "---\n",
        "## 🎯 Try It Yourself - Portfolio Management!\n",
        "\n",
        "### **Exercise 1: Create Your Own Portfolio**\n",
        "Build a portfolio with your favorite Malaysian stocks:\n",
        "```python\n",
        "my_portfolio = {\n",
        "    '1155.KL': {'name': 'Maybank', 'shares': 500, 'buy_price': 9.50},\n",
        "    '1295.KL': {'name': 'Public Bank', 'shares': 300, 'buy_price': 4.20},\n",
        "    # Add more stocks here!\n",
        "}\n",
        "```\n",
        "\n",
        "### **Exercise 2: Calculate Your Best Performer**\n",
        "Which stock in your portfolio made the most profit?\n",
        "```python\n",
        "best_performer = portfolio_df.loc[portfolio_df['Return (%)'].idxmax()]\n",
        "print(f\"Best stock: {best_performer['Name']} (+{best_performer['Return (%)']:.2f}%)\")\n",
        "```\n",
        "\n",
        "### **Exercise 3: Risk Assessment**\n",
        "Calculate what percentage of your portfolio each stock represents:\n",
        "```python\n",
        "portfolio_df['Weight (%)'] = (portfolio_df['Current Value'] / total_value) * 100\n",
        "print(portfolio_df[['Name', 'Weight (%)']])\n",
        "```\n",
        "\n",
        "**💡 TIP:** Financial advisors recommend:\n",
        "- No single stock > 25% of portfolio (diversification)\n",
        "- At least 5-10 different stocks\n",
        "- Mix different sectors (banks, tech, utilities, etc.)\n",
        "\n",
        "### **Exercise 4: Set Stop-Loss Levels**\n",
        "Calculate a 10% stop-loss for each stock:\n",
        "```python\n",
        "portfolio_df['Stop Loss'] = portfolio_df['Current Price'] * 0.90\n",
        "print(portfolio_df[['Name', 'Current Price', 'Stop Loss']])\n",
        "```\n",
        "\n",
        "**What's a stop-loss?** A price level where you sell to limit losses.\n",
        "\n",
        "---\n",
    ]
)

# Insert portfolio exercise
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 9. Sector & Comparative Analysis" in source_text:
            nb["cells"].insert(i, try_it_portfolio)
            print("[OK] Added portfolio management exercises")
            break

# Add data visualization tip
tip_charts = create_markdown_cell(
    [
        "---\n",
        "### 💡 Reading Stock Charts Like a Pro\n",
        "\n",
        "**Candlestick Charts:**\n",
        "```\n",
        "   |    <- High price\n",
        "  |-|   <- Green/Red body (Open to Close)\n",
        "   |    <- Low price\n",
        "```\n",
        "\n",
        "- **Green candle**: Close > Open (price went up that day) 📈\n",
        "- **Red candle**: Close < Open (price went down that day) 📉\n",
        "- **Wicks (lines)**: Show high and low prices\n",
        "- **Body**: Shows opening and closing prices\n",
        "\n",
        "**What to Look For:**\n",
        "\n",
        "1. **Trend**:\n",
        "   - Series of higher highs = Uptrend 📈\n",
        "   - Series of lower lows = Downtrend 📉\n",
        "   - Moving sideways = Range-bound ➡️\n",
        "\n",
        "2. **Support & Resistance**:\n",
        "   - **Support**: Price level where stock tends to stop falling\n",
        "   - **Resistance**: Price level where stock tends to stop rising\n",
        "   - Often at round numbers (RM 10.00, RM 15.00)\n",
        "\n",
        "3. **Volume**:\n",
        "   - High volume + price rise = Strong buying 💪\n",
        "   - High volume + price fall = Strong selling 💔\n",
        "   - Low volume = Weak moves, ignore them 😴\n",
        "\n",
        "4. **Moving Averages as Guides**:\n",
        "   - Price bouncing off SMA-50 = Strong support\n",
        "   - Price breaking through SMA = Trend change\n",
        "\n",
        "**⚠️ Practice Reading Charts:**\n",
        "Look at the charts in this notebook and ask yourself:\n",
        "- Is this an uptrend or downtrend?\n",
        "- Where are the support/resistance levels?\n",
        "- Are price and volume confirming each other?\n",
        "\n",
        "---\n",
    ]
)

# Insert chart reading tip
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 7. Technical Analysis Visualization" in source_text:
            nb["cells"].insert(i, tip_charts)
            print("[OK] Added chart reading guide")
            break

# Save Phase 2 enhancements
with open("projects/klse-stock-screener/klse_stock_screener.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\n" + "=" * 80)
print("[OK] PHASE 2 COMPLETE: Enhanced notebook with:")
print("   • Detailed inline comments in more code cells")
print("   • Technical analysis exercises")
print("   • RSI explanation and tips")
print("   • Screening strategy guide")
print("   • Portfolio management exercises")
print("   • Chart reading guide")
print("=" * 80)
