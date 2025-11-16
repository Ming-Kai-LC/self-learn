"""
Phase 3: Add comments to remaining cells and break down complex operations
"""

import json

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


# Enhanced version of get_fundamentals function
enhanced_get_fundamentals = create_code_cell(
    [
        "# ========================================\n",
        "# FUNCTION TO GET FUNDAMENTAL DATA\n",
        "# ========================================\n",
        "# Fundamental data = financial metrics like PE ratio, market cap, etc.\n",
        "\n",
        "def get_fundamentals(ticker):\n",
        '    """\n',
        "    Fetch fundamental data for a Malaysian stock.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    ticker : str\n",
        "        Malaysian stock ticker\n",
        "    \n",
        "    Returns:\n",
        "    --------\n",
        "    dict\n",
        "        Dictionary containing fundamental metrics\n",
        '    """\n',
        "    try:\n",
        "        # Create a ticker object\n",
        "        stock = yf.Ticker(ticker)\n",
        "        \n",
        "        # Get all company information (this is a big dictionary with LOTS of data)\n",
        "        info = stock.info\n",
        "        \n",
        "        # Create our own organized dictionary with just the metrics we want\n",
        "        fundamentals = {\n",
        "            'Ticker': ticker,  # The stock code\n",
        "            \n",
        "            # Get company name, or use ticker if name not available\n",
        "            'Name': info.get('longName', ticker),\n",
        "            \n",
        "            # Sector and industry classification\n",
        "            'Sector': info.get('sector', 'N/A'),  # e.g., \"Financial Services\"\n",
        "            'Industry': info.get('industry', 'N/A'),  # e.g., \"Banks - Regional\"\n",
        "            \n",
        "            # Market Cap in billions (divide by 1e9 = 1,000,000,000)\n",
        "            'Market Cap (B)': info.get('marketCap', 0) / 1e9 if info.get('marketCap') else None,\n",
        "            \n",
        "            # Valuation metrics\n",
        "            'PE Ratio': info.get('trailingPE'),  # Price-to-Earnings (current)\n",
        "            'Forward PE': info.get('forwardPE'),  # Expected future PE\n",
        "            'EPS': info.get('trailingEps'),  # Earnings Per Share\n",
        "            \n",
        "            # Dividend yield as percentage (multiply by 100)\n",
        "            'Dividend Yield (%)': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else None,\n",
        "            \n",
        "            # Risk metric (how volatile vs market)\n",
        "            'Beta': info.get('beta'),\n",
        "            \n",
        "            # Current price (try two different fields)\n",
        "            'Current Price': info.get('currentPrice') or info.get('regularMarketPrice'),\n",
        "            \n",
        "            # 52-week high and low prices\n",
        "            '52W High': info.get('fiftyTwoWeekHigh'),\n",
        "            '52W Low': info.get('fiftyTwoWeekLow')\n",
        "        }\n",
        "        \n",
        "        return fundamentals\n",
        "    \n",
        "    except Exception as e:\n",
        '        print(f"❌ Error fetching fundamentals for {ticker}: {e}")\n',
        "        return None\n",
        "\n",
        'print("✅ get_fundamentals() function created!")\n',
        "\n",
        "# 💡 TIP: .get(key, default) safely gets a value from a dictionary\n",
        "#         If the key doesn't exist, it returns the default instead of crashing\n",
    ]
)

# Find and replace get_fundamentals function
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if (
            "def get_fundamentals(ticker)" in source_text
            and "get_fundamentals() function created" in source_text
        ):
            nb["cells"][i] = enhanced_get_fundamentals
            print(f"[OK] Enhanced get_fundamentals function with detailed comments")
            break

# Add explanation for screening function
enhanced_screen_stocks = create_code_cell(
    [
        "# ========================================\n",
        "# STOCK SCREENING FUNCTION\n",
        "# ========================================\n",
        "# This function filters stocks based on criteria you specify\n",
        "# Think of it like Amazon filters: price range, brand, rating, etc.\n",
        "\n",
        "def screen_stocks(df, \n",
        "                  min_market_cap=None, \n",
        "                  max_pe=None,\n",
        "                  min_dividend_yield=None,\n",
        "                  sectors=None):\n",
        '    """\n',
        "    Screen stocks based on fundamental criteria.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    df : pd.DataFrame\n",
        "        DataFrame with stock fundamental data\n",
        "    min_market_cap : float\n",
        "        Minimum market cap in billions (e.g., 5 for RM 5B)\n",
        "    max_pe : float\n",
        "        Maximum PE ratio (e.g., 15 for value stocks)\n",
        "    min_dividend_yield : float\n",
        "        Minimum dividend yield in % (e.g., 3 for 3%)\n",
        "    sectors : list\n",
        "        List of sectors to include (e.g., ['Financial Services', 'Technology'])\n",
        "    \n",
        "    Returns:\n",
        "    --------\n",
        "    pd.DataFrame\n",
        "        Filtered stocks meeting the criteria\n",
        '    """\n',
        "    # Start with a copy of all stocks\n",
        "    filtered = df.copy()\n",
        "    \n",
        "    # ========================================\n",
        "    # APPLY FILTERS ONE BY ONE\n",
        "    # ========================================\n",
        "    # Each filter narrows down the list\n",
        "    \n",
        "    # FILTER 1: Minimum market cap\n",
        "    if min_market_cap is not None:  # Only if user specified this filter\n",
        "        # Keep only rows where Market Cap >= minimum\n",
        "        filtered = filtered[filtered['Market Cap (B)'] >= min_market_cap]\n",
        "    \n",
        "    # FILTER 2: Maximum PE ratio\n",
        "    if max_pe is not None:\n",
        "        # First, remove rows with missing PE data\n",
        "        filtered = filtered[filtered['PE Ratio'].notna()]  # notna() = not NaN\n",
        "        \n",
        "        # Keep only rows where PE <= maximum\n",
        "        filtered = filtered[filtered['PE Ratio'] <= max_pe]\n",
        "        \n",
        "        # Exclude negative PE (means company is losing money)\n",
        "        filtered = filtered[filtered['PE Ratio'] > 0]\n",
        "    \n",
        "    # FILTER 3: Minimum dividend yield\n",
        "    if min_dividend_yield is not None:\n",
        "        # Remove rows with missing dividend data\n",
        "        filtered = filtered[filtered['Dividend Yield (%)'].notna()]\n",
        "        \n",
        "        # Keep only rows where dividend >= minimum\n",
        "        filtered = filtered[filtered['Dividend Yield (%)'] >= min_dividend_yield]\n",
        "    \n",
        "    # FILTER 4: Specific sectors only\n",
        "    if sectors is not None:\n",
        "        # Keep only rows where Sector is in the list\n",
        "        # .isin() checks if value is in a list\n",
        "        filtered = filtered[filtered['Sector'].isin(sectors)]\n",
        "    \n",
        "    return filtered  # Return the filtered DataFrame\n",
        "\n",
        'print("✅ screen_stocks() function created!")\n',
        "\n",
        "# 💡 TIP: You can combine multiple filters:\n",
        "#    screen_stocks(df, min_market_cap=10, max_pe=15, min_dividend_yield=3)\n",
        "#    This finds large, cheap, dividend-paying stocks!\n",
    ]
)

# Find and replace screen_stocks function
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if (
            "def screen_stocks(df" in source_text
            and "screen_stocks() function created" in source_text
        ):
            nb["cells"][i] = enhanced_screen_stocks
            print(f"[OK] Enhanced screen_stocks function with detailed comments")
            break

# Add beginner tip on DataFrames before first usage
tip_dataframe = create_markdown_cell(
    [
        "---\n",
        "### 📊 Quick Guide: Working with DataFrames\n",
        "\n",
        "DataFrames are like Excel spreadsheets in Python. Here are the basics:\n",
        "\n",
        "**Getting Data:**\n",
        "```python\n",
        "df['Close']          # Get entire Close column\n",
        "df['Close'][0]       # Get first value\n",
        "df['Close'][-1]      # Get last value\n",
        "df[['Close', 'Open']] # Get multiple columns\n",
        "```\n",
        "\n",
        "**Viewing Data:**\n",
        "```python\n",
        "df.head()            # First 5 rows\n",
        "df.tail(10)          # Last 10 rows\n",
        "df.info()            # Summary info\n",
        "df.describe()        # Statistics\n",
        "len(df)              # Number of rows\n",
        "df.columns           # Column names\n",
        "```\n",
        "\n",
        "**Filtering Data:**\n",
        "```python\n",
        "df[df['Close'] > 10]              # Rows where Close > 10\n",
        "df[df['Volume'] > 1000000]        # High volume days\n",
        "df[(df['Close'] > 9) & (df['Close'] < 11)]  # Between 9 and 11\n",
        "```\n",
        "Note: Use `&` for AND, `|` for OR, `~` for NOT\n",
        "\n",
        "**Calculations:**\n",
        "```python\n",
        "df['Close'].mean()    # Average\n",
        "df['Close'].max()     # Maximum\n",
        "df['Close'].min()     # Minimum\n",
        "df['Volume'].sum()    # Total\n",
        "```\n",
        "\n",
        "**Creating New Columns:**\n",
        "```python\n",
        "df['Price_Change'] = df['Close'] - df['Open']  # Calculate difference\n",
        "df['Change_%'] = (df['Close'] / df['Open'] - 1) * 100  # Percentage\n",
        "```\n",
        "\n",
        "**⚠️ COMMON MISTAKES:**\n",
        "- ❌ `df[Close]` - Wrong! Need quotes: `df['Close']`\n",
        "- ❌ `df.Close[-1]` - Use `df['Close'][-1]` instead\n",
        "- ❌ Using `and`/`or` - Use `&`/`|` instead for DataFrames\n",
        "\n",
        "---\n",
    ]
)

# Insert DataFrame guide early in notebook
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "### Understanding OHLCV Data" in source_text:
            nb["cells"].insert(i, tip_dataframe)
            print("[OK] Added DataFrame quick guide")
            break

# Add final beginner exercises at the end
final_exercises = create_markdown_cell(
    [
        "---\n",
        "---\n",
        "\n",
        "## 🎓 Final Challenge: Put It All Together!\n",
        "\n",
        "Congratulations on making it this far! Now test your knowledge with these comprehensive challenges:\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 1: Find the Best Banking Stock** ⭐\n",
        "\n",
        "**Your task:**\n",
        "1. Screen for banking stocks (Financial Services sector)\n",
        "2. Filter for PE ratio < 12 and dividend yield > 4%\n",
        "3. Add 6-month technical indicators\n",
        "4. Find which one has the highest RSI\n",
        "5. Check if it's in an uptrend (price > SMA-50)\n",
        "\n",
        "**Hint:** Combine screening, technical analysis, and data filtering\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 2: Build a Balanced Portfolio** ⭐⭐\n",
        "\n",
        "**Your task:**\n",
        "Create a diversified portfolio with:\n",
        "- 2 banking stocks\n",
        "- 1 telecommunications stock\n",
        "- 1 utilities stock\n",
        "- 1 consumer stock\n",
        "\n",
        "Requirements:\n",
        "- Total investment: RM 50,000\n",
        "- No stock more than 25% of portfolio\n",
        "- Track it for current value and returns\n",
        "\n",
        "**Hint:** Use the portfolio tracking code from Section 8\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 3: Create a Custom Screener** ⭐⭐\n",
        "\n",
        "**Your task:**\n",
        "Build a screener that finds:\n",
        "- Large cap stocks (market cap > RM 20B)\n",
        "- Reasonable valuation (PE ratio between 10 and 20)\n",
        "- Decent dividend (dividend yield > 3%)\n",
        "- Strong momentum (RSI between 50 and 70)\n",
        "\n",
        "**Hint:** You'll need to combine fundamental screening with technical analysis\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 4: Analyze Sector Performance** ⭐⭐⭐\n",
        "\n",
        "**Your task:**\n",
        "1. Calculate the average 6-month return for each sector\n",
        "2. Find which sector performed best\n",
        "3. Create a bar chart comparing sector returns\n",
        "4. Identify the top stock in the winning sector\n",
        "\n",
        "**Hint:** Use groupby() and visualization tools\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 5: Build a Trading Signal** ⭐⭐⭐\n",
        "\n",
        "**Your task:**\n",
        "Create a function that generates BUY/SELL/HOLD signals based on:\n",
        "\n",
        "**BUY Signal:**\n",
        "- Price > SMA-50 (uptrend)\n",
        "- RSI < 70 (not overbought)\n",
        "- MACD > Signal line (momentum)\n",
        "- Volume > 20-day average (confirmation)\n",
        "\n",
        "**SELL Signal:**\n",
        "- Price < SMA-50 (downtrend)\n",
        "- RSI > 70 (overbought)\n",
        "\n",
        "**Otherwise:** HOLD\n",
        "\n",
        "Test it on 5 different stocks!\n",
        "\n",
        "---\n",
        "\n",
        "### **Challenge 6: Research Deep Dive** ⭐⭐⭐⭐\n",
        "\n",
        "**Your task:**\n",
        "Pick one Malaysian stock and perform a complete analysis:\n",
        "\n",
        "1. **Fundamental Analysis:**\n",
        "   - What's the PE ratio? Is it cheap or expensive?\n",
        "   - How's the dividend yield?\n",
        "   - What sector is it in?\n",
        "\n",
        "2. **Technical Analysis:**\n",
        "   - What's the current trend?\n",
        "   - Where are support/resistance levels?\n",
        "   - What do RSI and MACD say?\n",
        "\n",
        "3. **Comparative Analysis:**\n",
        "   - How does it compare to sector peers?\n",
        "   - Performance vs KLSE index?\n",
        "\n",
        "4. **Conclusion:**\n",
        "   - Would you buy, sell, or hold?\n",
        "   - What's your reasoning?\n",
        "\n",
        "Write your analysis as if presenting to an investor!\n",
        "\n",
        "---\n",
        "\n",
        "## 🎉 You Did It!\n",
        "\n",
        "If you completed even a few of these challenges, you're well on your way to becoming a quantitative analyst!\n",
        "\n",
        "**Next Steps:**\n",
        "1. Practice with real stocks daily\n",
        "2. Keep learning - read about new indicators and strategies\n",
        "3. Join investing communities (Reddit r/BursaBets, i3investor forums)\n",
        "4. Paper trade (practice without real money) before investing\n",
        "5. Always keep learning!\n",
        "\n",
        "**Remember:**\n",
        "- Knowledge is power, but practice makes perfect\n",
        "- Start small when investing real money\n",
        "- Never invest more than you can afford to lose\n",
        "- Keep emotions in check - stick to your strategy\n",
        "\n",
        "**Happy analyzing! 📊📈🚀**\n",
        "\n",
        "---\n",
    ]
)

# Insert final challenges before summary
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 11. Summary & Next Steps" in source_text:
            nb["cells"].insert(i, final_exercises)
            print("[OK] Added final comprehensive challenges")
            break

# Save Phase 3 enhancements
with open("projects/klse-stock-screener/klse_stock_screener.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\n" + "=" * 80)
print("[OK] PHASE 3 COMPLETE: Enhanced notebook with:")
print("   • Enhanced get_fundamentals() with detailed comments")
print("   • Enhanced screen_stocks() with step-by-step explanations")
print("   • DataFrame quick reference guide")
print("   • Final comprehensive challenges")
print("=" * 80)
print("\n[OK] ALL ENHANCEMENTS COMPLETE!")
print("     The notebook is now MUCH more beginner-friendly!")
