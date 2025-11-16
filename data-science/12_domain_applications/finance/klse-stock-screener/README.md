# KLSE Stock Screener & Analyzer

A comprehensive Jupyter notebook for analyzing Malaysian stocks (Bursa Malaysia / KLSE) with fundamental analysis, technical indicators, portfolio tracking, and stock screening capabilities.

## Overview

This project provides a complete toolkit for analyzing Malaysian stock market data. It uses **yfinance** (Yahoo Finance API) to fetch free, legal, and reliable data for Malaysian stocks, making it perfect for both learning and practical investment analysis.

## Features

### 1. Data Acquisition
- Fetch real-time and historical stock prices for Malaysian stocks
- Access fundamental data (PE ratio, market cap, EPS, dividend yield)
- Get company information (sector, industry, business description)
- All data from Yahoo Finance - **completely free and legal!**

### 2. Fundamental Analysis
- Compare key metrics across multiple stocks
- Filter stocks by fundamental criteria
- Sector-wise analysis and comparisons
- Financial ratios and valuations

### 3. Technical Analysis
- **Moving Averages**: SMA 20, 50, 200 and EMA
- **RSI**: Relative Strength Index for momentum
- **MACD**: Moving Average Convergence Divergence
- **Bollinger Bands**: Volatility indicators
- **ATR**: Average True Range
- Volume analysis with moving averages

### 4. Stock Screening
- Build custom filters for investment opportunities
- Value investing screens (low PE, high dividend)
- Large-cap / mid-cap / small-cap filters
- Sector-specific screening
- Growth stock identification

### 5. Portfolio Tracking
- Track multiple stock positions
- Calculate individual and portfolio returns
- Visualize portfolio allocation
- Monitor profit/loss in real-time

### 6. Comparative Analysis
- Compare stocks within the same sector
- Benchmark against KLSE index (^KLSE)
- Sector performance analysis
- Identify outperformers and underperformers

### 7. Interactive Visualizations
- Candlestick charts with moving averages
- Technical analysis dashboards (RSI, MACD, Bollinger Bands)
- Portfolio allocation pie charts
- Sector performance comparisons
- All charts are interactive using Plotly!

### 8. Data Caching
- Save fetched data locally to avoid repeated API calls
- Load cached data for offline analysis
- Respectful API usage with proper rate limiting

## Malaysian Stock Ticker Format

Malaysian stocks on Yahoo Finance use the `.KL` suffix:

| Company | Stock Code | Yahoo Finance Ticker |
|---------|------------|----------------------|
| Maybank | 1155 | `1155.KL` |
| Public Bank | 1295 | `1295.KL` |
| Tenaga Nasional | 5296 | `5296.KL` |
| CIMB Group | 1023 | `1023.KL` |
| Petronas Chemicals | 5183 | `5183.KL` |

The **KLSE index** ticker: `^KLSE`

## What You'll Learn

### Data Science Skills
- Using APIs for data acquisition (yfinance)
- Data manipulation with pandas
- Time series analysis
- Statistical calculations and aggregations
- Data visualization with matplotlib, seaborn, and plotly

### Finance Skills
- Reading and interpreting financial statements
- Understanding fundamental metrics (PE ratio, market cap, EPS)
- Technical analysis and chart patterns
- Portfolio management basics
- Risk assessment and diversification

### Python Programming
- Working with external libraries
- Creating reusable functions
- Data caching and file I/O
- Error handling and data validation

## Prerequisites

- Basic Python knowledge
- Understanding of pandas DataFrames (recommended)
- Basic stock market concepts (helpful but not required)
- Curiosity to learn! 🚀

## Files

- **`klse_stock_screener.ipynb`** - Main Jupyter notebook with complete tutorial
- **`data/`** - Directory for cached stock data (gitignored)

## Installation & Setup

### 1. Activate Virtual Environment

From the project root directory:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

If you haven't installed the required packages:

```bash
pip install yfinance pandas pandas-ta matplotlib seaborn plotly jupyter
```

Or install from requirements.txt:

```bash
cd ../..  # Go to project root
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

Navigate to `projects/klse-stock-screener/` and open `klse_stock_screener.ipynb`

## Usage Guide

### Basic Stock Data Fetching

```python
import yfinance as yf

# Fetch Maybank data
maybank = yf.Ticker("1155.KL")

# Get historical prices (1 year)
hist = maybank.history(period="1y")

# Get fundamental data
info = maybank.info
pe_ratio = info.get('trailingPE')
market_cap = info.get('marketCap')
```

### Adding Technical Indicators

```python
import pandas_ta as ta

# Add moving averages
df['SMA_20'] = df.ta.sma(length=20)
df['SMA_50'] = df.ta.sma(length=50)

# Add RSI
df['RSI'] = df.ta.rsi(length=14)

# Add MACD
macd = df.ta.macd()
df = pd.concat([df, macd], axis=1)
```

### Stock Screening Example

```python
# Screen for value stocks
value_stocks = stocks_df[
    (stocks_df['PE Ratio'] < 15) &
    (stocks_df['Dividend Yield (%)'] > 3)
]

# Screen for large caps
large_caps = stocks_df[stocks_df['Market Cap (B)'] > 10]
```

### Portfolio Tracking

```python
portfolio = {
    '1155.KL': {'name': 'Maybank', 'shares': 1000, 'buy_price': 9.00},
    '1295.KL': {'name': 'Public Bank', 'shares': 500, 'buy_price': 4.50}
}

# Calculate current value and returns
# (See notebook for complete implementation)
```

## Sample Stocks Covered

The notebook includes analysis of major Malaysian stocks across various sectors:

### Banking & Finance
- Maybank (1155.KL)
- Public Bank (1295.KL)
- CIMB Group (1023.KL)
- RHB Bank (6947.KL)
- Hong Leong Bank (1066.KL)

### Utilities
- Tenaga Nasional (5296.KL)

### Oil & Gas
- Petronas Chemicals (5183.KL)
- Petronas Gas (5225.KL)
- Dialog Group (2445.KL)

### Telecommunications
- Maxis (4197.KL)
- Axiata Group (6012.KL)
- DiGi.Com (4863.KL)

### Healthcare
- IHH Healthcare (3816.KL)

### And more sectors: Plantation, Construction, Consumer Goods, Technology

## Notebook Structure

The notebook is organized into 11 comprehensive sections:

1. **Setup and Imports** - Library installation and configuration
2. **Basic Stock Data Fetching** - Understanding OHLCV data
3. **Fundamental Data Analysis** - Financial metrics and company info
4. **Technical Indicators** - RSI, MACD, Moving Averages, Bollinger Bands
5. **Stock Screener Functionality** - Custom filters and screening
6. **Price Trend Visualization** - Candlestick and line charts
7. **Technical Analysis Visualization** - Interactive dashboards
8. **Portfolio Tracking** - Multi-stock portfolio management
9. **Sector & Comparative Analysis** - Sector comparisons and benchmarking
10. **Data Export & Caching** - Save and load data locally
11. **Summary & Next Steps** - Ideas for further development

## Data Sources

### Primary: Yahoo Finance (via yfinance)
- **Status**: ✅ Free, legal, and reliable
- **Coverage**: Excellent for KLSE stocks
- **Data**: Prices, fundamentals, company info
- **Rate Limits**: Generous (no API key needed)
- **Best For**: Beginners and production use

### Why Yahoo Finance?
- No API keys or authentication required
- Comprehensive data for Malaysian stocks
- Historical data goes back 10+ years
- Active maintenance and community support
- Legal and ethical data usage

## Legal & Ethical Considerations

✅ **This project uses publicly available data ethically**

- All stock prices and financial data are public information
- No Terms of Service violations
- No authentication bypass or paywall circumvention
- Respectful API usage with proper delays
- For educational and personal use only

⚠️ **Important Notes**:
- Do not redistribute or sell the data
- Add delays between API requests (already implemented in notebook)
- Data is typically 15-minute delayed (free tier)
- Always verify critical data against official sources

## Extending the Project

### Ideas for Enhancement

1. **Advanced Screening**
   - Add earnings growth filters
   - Implement debt-to-equity ratio checks
   - Create multi-factor scoring system

2. **Machine Learning**
   - Predict stock prices using LSTM
   - Build classification models for buy/sell signals
   - Sentiment analysis from news articles

3. **Automation**
   - Set price alerts
   - Create daily/weekly reports
   - Email notifications for screener results

4. **Web Dashboard**
   - Build Streamlit app for interactive analysis
   - Deploy to cloud (Heroku, AWS)
   - Add user authentication

5. **More Analysis**
   - Options pricing and Greeks
   - Earnings calendar tracking
   - Institutional ownership data
   - Insider trading activity

## Troubleshooting

### Common Issues

**Issue**: "No data found for ticker"
- **Solution**: Verify ticker format uses `.KL` suffix (e.g., `1155.KL` not `1155`)

**Issue**: "yfinance not found"
- **Solution**: Install with `pip install yfinance`

**Issue**: Slow data fetching
- **Solution**: Use caching feature in notebook section 10

**Issue**: Charts not displaying
- **Solution**: Ensure `%matplotlib inline` is run and Jupyter is properly configured

**Issue**: Old data being displayed
- **Solution**: Clear cache in `data/` directory and re-fetch

## Resources

### Learning Materials
- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [pandas-ta GitHub](https://github.com/twopirllc/pandas-ta)
- [Investopedia - Technical Analysis](https://www.investopedia.com/technical-analysis-4689657)
- [Plotly Python Documentation](https://plotly.com/python/)

### Malaysian Market Info
- [Bursa Malaysia](https://www.bursamalaysia.com/)
- [The Edge Markets](https://www.theedgemarkets.com/)
- [i3investor](https://klse.i3investor.com/)
- [KLSE Screener](https://www.klsescreener.com/)

### Data Science
- [Kaggle Learn](https://www.kaggle.com/learn)
- [DataCamp](https://www.datacamp.com/)
- [Python for Finance](https://www.python.org/community/sigs/current/finance-sig/)

## Disclaimer

⚠️ **IMPORTANT**: This project is for **educational purposes only**.

- **NOT financial advice**: Always consult licensed financial advisors
- **No guarantees**: Past performance ≠ future results
- **Risk warning**: Stock investing carries risk of loss
- **Your responsibility**: Do your own research (DYOR)
- **Data accuracy**: Verify critical data with official sources

## License

MIT License - Feel free to use, modify, and learn from this project!

## Contributing

Suggestions and improvements are welcome! This is a learning project, so feel free to:
- Report issues or bugs
- Suggest new features
- Share your own analysis ideas
- Improve documentation

## Acknowledgments

- **yfinance** by Ran Aroussi for providing free Yahoo Finance API access
- **pandas-ta** by Kevin Johnson for comprehensive technical analysis library
- **Plotly** team for amazing visualization capabilities
- Bursa Malaysia for maintaining a transparent market
- The Python data science community

---

**Happy Analyzing! 📈🚀**

Remember: Knowledge + Discipline + Patience = Success in investing!
