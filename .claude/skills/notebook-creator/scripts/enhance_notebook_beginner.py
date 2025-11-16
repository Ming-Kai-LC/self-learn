"""
Enhance KLSE Stock Screener Notebook for Complete Beginners
Adds:
1. Inline comments to all code
2. Python Basics Refresher section
3. Try It Yourself exercises
4. Tips and warnings throughout
5. Troubleshooting section
6. Breaks down complex cells
"""

import json

# Read the original notebook
with open("projects/klse-stock-screener/klse_stock_screener.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)


# Helper function to create cells
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


# Insert Python Basics Refresher after cell 2 (after imports)
python_basics_markdown = create_markdown_cell(
    [
        "## 🎓 Python Basics Quick Refresher\n",
        "\n",
        "Before we dive in, let's review some Python concepts you'll see in this notebook:\n",
        "\n",
        "### 1. **Variables**\n",
        "Variables store data that we can use later:\n",
        "```python\n",
        'ticker = "1155.KL"  # Stores the stock ticker as text (string)\n',
        "price = 9.50        # Stores a number (float)\n",
        "shares = 100        # Stores a whole number (integer)\n",
        "```\n",
        "\n",
        "### 2. **DataFrames (Spreadsheet-like Tables)**\n",
        "Think of DataFrames as Excel spreadsheets in Python:\n",
        "```python\n",
        "df['Close']         # Gets the 'Close' column (like column B in Excel)\n",
        "df.head()           # Shows first 5 rows\n",
        "df['Close'][-1]     # Gets the last value in Close column\n",
        "```\n",
        "\n",
        "### 3. **Functions**\n",
        "Functions are reusable blocks of code:\n",
        "```python\n",
        "def get_stock_data(ticker):  # Define a function\n",
        "    # Code goes here\n",
        "    return data              # Give back the result\n",
        "\n",
        'result = get_stock_data("1155.KL")  # Use the function\n',
        "```\n",
        "\n",
        "### 4. **Dictionaries (Key-Value Pairs)**\n",
        "Dictionaries store data with labels:\n",
        "```python\n",
        "stock = {'name': 'Maybank', 'price': 9.50}\n",
        "print(stock['name'])  # Output: Maybank\n",
        "```\n",
        "\n",
        "### 5. **Loops**\n",
        "Loops repeat actions:\n",
        "```python\n",
        "for ticker in ['1155.KL', '1295.KL']:  # Do this for each ticker\n",
        "    print(ticker)                       # Print each one\n",
        "```\n",
        "\n",
        "### 6. **Lists**\n",
        "Lists store multiple items:\n",
        "```python\n",
        "stocks = ['1155.KL', '1295.KL', '1023.KL']  # A list of 3 tickers\n",
        "stocks[0]  # Gets first item: '1155.KL'\n",
        "```\n",
        "\n",
        "### 7. **Conditional Statements (If/Else)**\n",
        "Make decisions in code:\n",
        "```python\n",
        "if price > 10:           # If condition is true\n",
        '    print("Expensive")\n',
        "else:                     # Otherwise\n",
        '    print("Affordable")\n',
        "```\n",
        "\n",
        "**💡 TIP:** Don't worry if you don't understand everything yet! The concepts will become clearer as you see them used in real examples.\n",
        "\n",
        "---\n",
    ],
    "basics-refresher",
)

nb["cells"].insert(3, python_basics_markdown)

print("[OK] Added Python Basics Refresher section")

# Enhanced cell 2 (imports) with detailed comments
enhanced_imports = create_code_cell(
    [
        "# ========================================\n",
        "# IMPORT REQUIRED LIBRARIES\n",
        "# ========================================\n",
        "# These are pre-written code packages that add functionality\n",
        "\n",
        "# yfinance: Downloads stock market data from Yahoo Finance (FREE!)\n",
        "import yfinance as yf\n",
        "\n",
        "# pandas: Works with data in tables (like Excel spreadsheets)\n",
        "import pandas as pd\n",
        "\n",
        "# pandas_ta: Calculates technical indicators (RSI, MACD, etc.)\n",
        "import pandas_ta as ta\n",
        "\n",
        "# matplotlib & seaborn: Create charts and graphs\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# plotly: Creates interactive charts you can zoom and explore\n",
        "import plotly.graph_objects as go\n",
        "import plotly.express as px\n",
        "from plotly.subplots import make_subplots\n",
        "\n",
        "# datetime: Works with dates and times\n",
        "from datetime import datetime, timedelta\n",
        "\n",
        "# warnings: Controls warning messages\n",
        "import warnings\n",
        "\n",
        "# os: Interacts with your computer's file system\n",
        "import os\n",
        "\n",
        "# ========================================\n",
        "# CONFIGURE SETTINGS\n",
        "# ========================================\n",
        "\n",
        "# Turn off warning messages to keep output clean\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "# Set the default style for charts (makes them look nice)\n",
        "sns.set_style('whitegrid')\n",
        "\n",
        "# Set default chart size (width=14 inches, height=7 inches)\n",
        "plt.rcParams['figure.figsize'] = (14, 7)\n",
        "\n",
        "# Print success message with emoji checkmark\n",
        'print("✅ All libraries imported successfully!")\n',
        "print(f\"📅 Today's date: {datetime.now().strftime('%Y-%m-%d')}\")\n",
        'print(f"📊 yfinance version: {yf.__version__}")\n',
        "\n",
        "# 💡 TIP: If you get an error here, make sure you've installed all packages:\n",
        "#    pip install yfinance pandas pandas-ta matplotlib seaborn plotly\n",
    ],
    "cell-2-enhanced",
)

# Replace cell 2 with enhanced version
nb["cells"][2] = enhanced_imports

print("[OK] Enhanced imports cell with detailed comments")

# Add tips and exercises throughout
# After cell on basic fetching (around cell 8), add Try It Yourself
try_it_cell_basic = create_markdown_cell(
    [
        "---\n",
        "## 🎯 Try It Yourself!\n",
        "\n",
        "Now that you've seen how to fetch stock data, practice with these exercises:\n",
        "\n",
        "### **Exercise 1: Fetch Different Stocks**\n",
        "Modify the code above to fetch data for:\n",
        "- Public Bank: `1295.KL`\n",
        "- CIMB Group: `1023.KL`\n",
        "\n",
        "**Hint:** Change the ticker variable\n",
        "\n",
        "### **Exercise 2: Try Different Time Periods**\n",
        "Experiment with different periods:\n",
        '- Last 1 month: `period="1mo"`\n',
        '- Last 5 years: `period="5y"`\n',
        '- All available data: `period="max"`\n',
        "\n",
        "### **Exercise 3: Calculate Price Change**\n",
        "Can you calculate the percentage change over different periods?\n",
        "\n",
        "**Formula:** `((latest_price / first_price) - 1) * 100`\n",
        "\n",
        "---\n",
        "\n",
        "**⚠️ COMMON MISTAKE:** Make sure to use `.KL` suffix for Malaysian stocks!\n",
        '- ✅ Correct: `"1155.KL"`\n',
        '- ❌ Wrong: `"1155"` or `"1155.MY"`\n',
        "\n",
        "---\n",
    ],
    "try-it-basic",
)

# Find cell 8 and insert after it
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "get_stock_data" in source_text and "def get_stock_data" in source_text:
            nb["cells"].insert(i + 1, try_it_cell_basic)
            print(f"[OK] Added 'Try It Yourself' exercise after cell {i}")
            break

# Add tips throughout
tip_fundamental = create_markdown_cell(
    [
        "---\n",
        "### 💡 Understanding PE Ratio\n",
        "\n",
        "**PE Ratio = Price-to-Earnings Ratio**\n",
        "\n",
        'Think of it as "How many years of earnings would it take to pay back the stock price?"\n',
        "\n",
        "**Example:**\n",
        "- Stock price: RM 10\n",
        "- Earnings per share: RM 1\n",
        "- PE Ratio = 10 / 1 = 10\n",
        "\n",
        "**What's a good PE Ratio?**\n",
        '- PE < 15: Usually considered "cheap" or "value" stock\n',
        "- PE 15-25: Average\n",
        '- PE > 25: Might be "expensive" or high-growth stock\n',
        "\n",
        '**⚠️ WARNING:** Low PE doesn\'t always mean "good deal"! The company might be struggling.\n',
        "\n",
        "---\n",
    ],
    "tip-pe-ratio",
)

# Insert tip before fundamentals section
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 3. Fundamental Data Analysis" in source_text:
            nb["cells"].insert(i + 1, tip_fundamental)
            print(f"[OK] Added PE Ratio explanation tip")
            break

# Add comprehensive troubleshooting section at the end (before summary)
troubleshooting_section = create_markdown_cell(
    [
        "---\n",
        "---\n",
        "\n",
        "## 🔧 Common Mistakes & Troubleshooting\n",
        "\n",
        "Running into errors? Here are solutions to common problems:\n",
        "\n",
        "---\n",
        "\n",
        "### **Problem 1: \"ModuleNotFoundError: No module named 'yfinance'\"**\n",
        "\n",
        "**What it means:** The required package isn't installed\n",
        "\n",
        "**Solution:**\n",
        "```bash\n",
        "pip install yfinance pandas pandas-ta matplotlib seaborn plotly\n",
        "```\n",
        "\n",
        "**💡 TIP:** Make sure you're using the same Python environment where you installed packages!\n",
        "\n",
        "---\n",
        "\n",
        '### **Problem 2: "No data found for ticker"**\n',
        "\n",
        "**What it means:** The stock ticker doesn't exist or is incorrect\n",
        "\n",
        "**Common causes:**\n",
        "- Missing `.KL` suffix for Malaysian stocks\n",
        "- Wrong ticker symbol\n",
        "- Stock has been delisted\n",
        "\n",
        "**Solution:**\n",
        '- Always use `.KL` for Malaysian stocks: `"1155.KL"`\n',
        "- Verify ticker on Yahoo Finance website first\n",
        "\n",
        "---\n",
        "\n",
        '### **Problem 3: "KeyError: \'SMA_20\'" or "Column not found"**\n',
        "\n",
        "**What it means:** You're trying to access a column that doesn't exist\n",
        "\n",
        "**Common causes:**\n",
        "- Forgot to run `add_technical_indicators()` function\n",
        "- Not enough data points to calculate indicator\n",
        "\n",
        "**Solution:**\n",
        "```python\n",
        "# Check what columns exist:\n",
        "print(df.columns)\n",
        "\n",
        "# Make sure to add indicators first:\n",
        "df = add_technical_indicators(df)\n",
        "```\n",
        "\n",
        "---\n",
        "\n",
        '### **Problem 4: "ValueError: Cannot set a DataFrame with multiple columns..."**\n',
        "\n",
        "**What it means:** pandas_ta returned unexpected format\n",
        "\n",
        "**Solution:** This notebook already uses `safe_add_indicator()` helper function to handle this. If you see this error:\n",
        "- Make sure you're using the `add_technical_indicators()` function from cell 16\n",
        "- Ensure you have enough data (at least 200 days for SMA-200)\n",
        "\n",
        "---\n",
        "\n",
        "### **Problem 5: Charts not showing up**\n",
        "\n",
        "**Solution:**\n",
        "- For Jupyter Notebook: Make sure you ran the imports cell\n",
        "- For VS Code: Install the Jupyter extension\n",
        "- Try restarting the kernel: `Kernel > Restart`\n",
        "\n",
        "---\n",
        "\n",
        '### **Problem 6: "HTTP Error 429: Too Many Requests"**\n',
        "\n",
        "**What it means:** You've made too many requests to Yahoo Finance\n",
        "\n",
        "**Solution:**\n",
        "- Wait 1-2 minutes before trying again\n",
        "- Use the caching functions in Section 10 to avoid repeated requests\n",
        "- Don't run the screening function too frequently\n",
        "\n",
        "---\n",
        "\n",
        "### **Problem 7: Slow performance / notebook hanging**\n",
        "\n",
        "**Common causes:**\n",
        "- Fetching too many stocks at once\n",
        "- Downloading large amounts of historical data\n",
        "\n",
        "**Solution:**\n",
        "- Start with fewer stocks (3-5) when testing\n",
        '- Use shorter time periods (`"1mo"` instead of `"max"`)\n',
        "- Clear outputs regularly: `Cell > All Output > Clear`\n",
        "\n",
        "---\n",
        "\n",
        "### **Problem 8: Dividend Yield shows very high percentage (600%+)**\n",
        "\n",
        "**What it means:** This is likely a data issue with Yahoo Finance API\n",
        "\n",
        "**Explanation:** Sometimes Yahoo Finance provides incorrect dividend yield data. Always verify high values against official sources like Bursa Malaysia.\n",
        "\n",
        "**Real typical dividend yields:**\n",
        "- Banks: 3-6%\n",
        "- REITs: 5-8%\n",
        "- Growth stocks: 0-2%\n",
        "\n",
        "---\n",
        "\n",
        '### **Problem 9: Getting "NaN" (Not a Number) in results**\n',
        "\n",
        "**What it means:** Data is missing or can't be calculated\n",
        "\n",
        "**Common causes:**\n",
        "- Not enough historical data\n",
        "- Stock is newly listed\n",
        "- Market was closed\n",
        "\n",
        "**Check for NaN values:**\n",
        "```python\n",
        "# See which values are missing:\n",
        "print(df.isna().sum())\n",
        "\n",
        "# Remove rows with NaN:\n",
        "df = df.dropna()\n",
        "```\n",
        "\n",
        "---\n",
        "\n",
        "### 🆘 Still Having Issues?\n",
        "\n",
        "**Debugging checklist:**\n",
        "1. ✅ Did you run ALL cells from top to bottom?\n",
        "2. ✅ Are you using the correct ticker format (`.KL`)?\n",
        "3. ✅ Did you install all required packages?\n",
        "4. ✅ Is your internet connection working?\n",
        "5. ✅ Have you checked the error message carefully?\n",
        "\n",
        "**Getting help:**\n",
        "- Read the error message from bottom to top\n",
        '- Search the error on Google with "yfinance" keyword\n',
        "- Check yfinance GitHub issues: https://github.com/ranaroussi/yfinance/issues\n",
        "\n",
        "---\n",
    ],
    "troubleshooting-section",
)

# Find the summary section and insert troubleshooting before it
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "markdown":
        source_text = (
            "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        )
        if "## 11. Summary & Next Steps" in source_text:
            nb["cells"].insert(i, troubleshooting_section)
            print(f"[OK] Added comprehensive troubleshooting section")
            break

# Save enhanced notebook
with open("projects/klse-stock-screener/klse_stock_screener.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\n" + "=" * 80)
print("[OK] PHASE 1 COMPLETE: Enhanced notebook with:")
print("   • Python Basics Refresher section")
print("   • Detailed inline comments in imports")
print("   • Try It Yourself exercises")
print("   • Tips and explanations")
print("   • Comprehensive troubleshooting section")
print("=" * 80)
