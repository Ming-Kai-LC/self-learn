# Malaysian Stock Technical Analysis - Educational Project

**A comprehensive educational portfolio for learning stock market technical analysis with focus on Bursa Malaysia.**

## Project Overview

This project provides a structured learning path from beginner to proficient trader in the Malaysian stock market. It follows the educational notebook standards defined in the repository's CLAUDE.md guidelines.

## Learning Objectives

By completing this educational series, you will:

1. **Understand Bursa Malaysia mechanics** - Trading hours, settlement (T+2), order types, and CDS system
2. **Master fundamental analysis** - Financial statements, valuation methods (P/E, ROE, debt ratios)
3. **Apply technical analysis** - Moving averages, RSI, MACD, chart patterns
4. **Develop trading strategies** - Swing trading, position sizing, risk management
5. **Build practical skills** - Using yfinance for data, implementing indicators, backtesting strategies

## Project Structure

```
malaysia-stock/
├── notebooks/           # Educational Jupyter notebooks (numbered 00-10)
│   ├── 00_setup_introduction.ipynb
│   ├── 01_bursa_malaysia_fundamentals.ipynb
│   ├── 02_data_collection_with_yfinance.ipynb
│   ├── ...
│   └── 10_final_trading_project.ipynb
├── data/
│   ├── raw/            # Original data (never modified)
│   ├── processed/      # Cleaned and prepared data
│   └── sample/         # Small example datasets (<10MB for repo)
├── docs/
│   └── Stock-SelfLearn.md  # Complete learning roadmap (5 stages)
├── tests/              # Notebook validation and testing
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Basic understanding of Python and pandas
- Interest in stock market investing
- **Recommended**: Complete "Data Science Fundamentals" project first

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   cd /home/user/self-learn/malaysia-stock
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Start with notebook 00** and progress sequentially

## Malaysian Market Specifics

### Key Advantages

- **Zero capital gains tax** on listed stocks
- Competitive brokerage fees (as low as RM2.88 per trade)
- Strong regulatory oversight by Securities Commission Malaysia
- T+2 settlement system (implemented 2019)

### Trading Hours

- **Morning Session**: 9:00 AM - 12:30 PM MYT
- **Afternoon Session**: 2:30 PM - 5:00 PM MYT

### Popular Stocks for Examples

- **Banking**: Maybank (1155.KL), Public Bank (1295.KL), CIMB (1023.KL)
- **Plantation**: Sime Darby Plantation (5285.KL), IOI Corp (1961.KL)
- **Consumer**: Nestle Malaysia (4707.KL), 99 Speed Mart (5304.KL)
- **Construction**: Gamuda (5398.KL), Sunway (5211.KL)

## Learning Path

### Stage 1: Foundation (Notebooks 00-02)
- Market mechanics and structure
- Account setup and paper trading
- Data collection with yfinance

### Stage 2: Technical Analysis (Notebooks 03-05)
- Moving averages and trend analysis
- RSI and MACD indicators
- Chart patterns and volume analysis

### Stage 3: Trading Strategies (Notebooks 06-08)
- Entry and exit strategies
- Position sizing and risk management
- Backtesting frameworks

### Stage 4: Advanced Topics (Notebooks 09-10)
- Multi-timeframe analysis
- Portfolio optimization
- Final trading project

## Data Sources

All notebooks use **yfinance** for data collection:

```python
import yfinance as yf

# Example: Download Maybank stock data
maybank = yf.download('1155.KL', start='2020-01-01', end='2024-12-31')
```

**Note**: Malaysian stock codes use `.KL` suffix (e.g., `1155.KL` for Maybank)

## Quality Standards

This project follows strict educational quality standards:

- ✅ **Markdown Ratio**: ≥30% explanatory content
- ✅ **Exercise Count**: ≥3 exercises per major concept
- ✅ **Execution**: All notebooks pass "Restart and Run All"
- ✅ **Code Quality**: PEP 8 compliant with educational exceptions
- ✅ **Learning Objectives**: Clearly stated in each notebook
- ✅ **Prerequisites**: Explicitly documented

## Testing Your Knowledge

Each notebook includes:

1. **Guided Examples** - Step-by-step demonstrations
2. **Practice Exercises** - Apply concepts independently
3. **Challenge Problems** - Test mastery
4. **Self-Assessment** - Validate understanding before progressing

## Additional Resources

### Recommended Reading

- *The Intelligent Investor* by Benjamin Graham
- *How to Make Money from the Malaysian Stock Market*
- *Rich Dad Poor Dad* by Robert Kiyosaki

### Online Resources

- [Bursa Malaysia Academy](https://bursamarketplace.com) - Free courses
- [i3investor](https://klse.i3investor.com) - Largest Malaysian stock forum
- [The Edge Malaysia](https://theedgemalaysia.com) - Financial news
- [KLSE Screener](https://klsescreener.com) - Stock filtering tools

### YouTube Channels

- **Mr Money TV** (207K subscribers) - Malaysian investing
- **CF Lieu** (22K subscribers) - Technical analysis

## Contributing

This is an educational project. Improvements welcome:

1. Enhanced explanations in notebooks
2. Additional exercises with solutions
3. New visualizations or examples
4. Bug fixes or corrections

## Risk Disclaimer

**IMPORTANT**: This is an educational project for learning purposes only.

- Past performance does not guarantee future results
- Stock trading involves substantial risk of loss
- Always use paper trading before real money
- Consult licensed financial advisors before investing
- The materials provided are for educational purposes and should not be considered as financial advice

## License

Educational use only. See repository root for license details.

## Support

For questions or issues:

1. Check the comprehensive learning roadmap in `docs/Stock-SelfLearn.md`
2. Review notebook comments and markdown explanations
3. Refer to the main project CLAUDE.md for standards
4. Join i3investor forum for community support

---

**Start Date**: 2024
**Target Audience**: Beginners to intermediate learners
**Estimated Completion**: 3-6 months (at 5-10 hours/week)
**Difficulty**: ⭐⭐ (Progressive from ⭐ to ⭐⭐⭐)

**Remember**: "The stock market is a device for transferring money from the impatient to the patient." - Warren Buffett
