# Stock Analysis Project Plan: 1000-Hour Roadmap

**Project**: Real-World Analysis of UUE Holdings (0310.KL) & Oriental Kopi (0338.KL)
**Total Time**: 1000 hours
**Duration**: 6-12 months
**Difficulty**: ⭐⭐⭐ (Advanced, Professional-Grade)

---

## Executive Summary

This plan breaks down 1000 hours of learning into a structured curriculum that transforms you from a stock market learner into a competent analyst capable of making informed investment decisions. The project focuses on two real ACE Market stocks, requiring deep fundamental analysis, technical analysis, and automated monitoring systems.

---

## Phase Breakdown

| Phase | Module | Hours | Focus Area | Deliverable |
|-------|--------|-------|------------|-------------|
| 1 | 00-01 | 100 | Foundation & Data | Data Pipeline |
| 2 | 02-04 | 300 | Fundamental Analysis | Investment Thesis |
| 3 | 05-07 | 250 | Technical Analysis | Entry Points |
| 4 | 08 | 150 | News & Intelligence | Alert System |
| 5 | 09 | 100 | Risk Management | Risk Framework |
| 6 | 10 | 100 | Dashboard & Automation | Live Monitor |
| **TOTAL** | | **1000** | | **Complete System** |

---

## Phase 1: Foundation & Data Collection (100 Hours)

### Module 00: Project Setup and Objectives (20 Hours)

#### Week 1: Personal Investment Framework (10 hours)
- [ ] Define your investment goals (capital growth, dividend income, learning)
- [ ] Establish risk tolerance (questionnaire, past experience)
- [ ] Determine time horizon (short-term trader vs long-term investor)
- [ ] Set capital allocation limits (% of portfolio per stock)
- [ ] Document investment philosophy

**Activities**:
- Complete risk tolerance assessment
- Research Warren Buffett's investment principles
- Read about ACE Market characteristics
- Define personal success criteria

**Deliverables**:
- Personal Investment Policy Statement (IPS)
- Risk tolerance scorecard
- Investment goals document

#### Week 2: Company Research (10 hours)
- [ ] UUE Holdings business model understanding
  - Watch YouTube videos about HDD (Horizontal Directional Drilling)
  - Research infrastructure projects in Malaysia
  - Understand competitive landscape
- [ ] Oriental Kopi business understanding
  - Visit Oriental Kopi outlets (if possible)
  - Study F&B industry trends in Malaysia
  - Analyze café chain business models
- [ ] ACE Market mechanics
  - Trading rules and restrictions
  - Liquidity considerations
  - Disclosure requirements

**Activities**:
- Read latest annual reports (both companies)
- Review Bursa Malaysia ACE Market guidelines
- Study competitor analysis

**Deliverables**:
- Business model summaries (2-page each)
- Competitive landscape maps
- Initial hypothesis about stock quality

---

### Module 01: Data Collection Systems (80 Hours)

#### Week 3-4: Historical Price Data (20 hours)
- [ ] Set up yfinance for Malaysian stocks
- [ ] Download 5+ years of historical data (0310.KL, 0338.KL)
- [ ] Download benchmark data (FBMKLCI, FBMACE)
- [ ] Create data validation scripts
- [ ] Handle missing data and corporate actions
- [ ] Store data in efficient formats (Parquet, CSV)

**Technical Skills**:
```python
import yfinance as yf
import pandas as pd

# Download data with proper error handling
def fetch_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        # Validation checks
        assert len(data) > 0, f"No data for {ticker}"
        assert data['Close'].notna().sum() > 0, "Missing price data"
        return data
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None
```

**Deliverables**:
- `fetch_stock_data.py` script
- Historical data files in `data/raw/`
- Data quality report

#### Week 5-6: Fundamental Data Collection (30 hours)
- [ ] Extract financial statements (5 years)
  - Income statements
  - Balance sheets
  - Cash flow statements
- [ ] Collect quarterly earnings data
- [ ] Download dividend history
- [ ] Get insider trading data (if available)
- [ ] Collect peer comparison data

**Data Sources**:
- Bursa Malaysia company announcements
- Annual reports (PDF parsing)
- KLSE Screener
- i3investor data
- Manual data entry from financial statements

**Tools to Learn**:
- PDF text extraction (PyPDF2, pdfplumber)
- Web scraping (BeautifulSoup, Selenium)
- Data cleaning (pandas)

**Deliverables**:
- `data/financial_statements/` populated
- Quarterly earnings spreadsheet
- Dividend history database

#### Week 7-8: Data Pipeline Automation (30 hours)
- [ ] Create automated update scripts
- [ ] Schedule daily price updates
- [ ] Set up data versioning
- [ ] Build data quality checks
- [ ] Create data documentation
- [ ] Test pipeline robustness

**Advanced Topics**:
- cron jobs / Task Scheduler
- Database setup (SQLite or PostgreSQL)
- Error handling and retry logic
- Logging and monitoring

**Deliverables**:
- Automated data pipeline
- Data dictionary
- Pipeline documentation

---

## Phase 2: Fundamental Analysis (300 Hours)

### Module 02: UUE Holdings Fundamental Analysis (100 Hours)

#### Week 9-10: Revenue & Business Analysis (25 hours)
- [ ] Revenue breakdown by segment
- [ ] Historical revenue growth analysis (5 years)
- [ ] Customer concentration risk
- [ ] Contract win analysis
- [ ] Project pipeline visibility
- [ ] Market share estimation

**Key Questions**:
- What drives UUE's revenue growth?
- Is revenue recurring or project-based?
- Who are the main customers (government, private)?
- What is the competitive moat?

**Analysis Techniques**:
- Time series analysis
- Growth rate calculations
- Trend decomposition
- Seasonality identification

**Deliverables**:
- Revenue analysis report (10 pages)
- Growth drivers identified
- Risk factors documented

#### Week 11-12: Profitability Analysis (25 hours)
- [ ] Gross margin trends
- [ ] Operating margin analysis
- [ ] Net profit margin trends
- [ ] ROE (Return on Equity) calculation
- [ ] ROA (Return on Assets) calculation
- [ ] ROIC (Return on Invested Capital)
- [ ] Compare to industry averages

**Financial Ratios**:
```python
# Calculate key profitability metrics
gross_margin = (revenue - cogs) / revenue * 100
operating_margin = operating_income / revenue * 100
net_margin = net_income / revenue * 100
roe = net_income / shareholders_equity * 100
roa = net_income / total_assets * 100
```

**Deliverables**:
- Profitability dashboard
- 5-year trend analysis
- Peer comparison charts

#### Week 13-14: Balance Sheet & Debt Analysis (25 hours)
- [ ] Asset composition analysis
- [ ] Liability structure
- [ ] Working capital trends
- [ ] Debt-to-equity ratio
- [ ] Interest coverage ratio
- [ ] Current ratio and quick ratio
- [ ] Asset turnover ratios

**Solvency Assessment**:
- Can UUE pay its debts?
- Is leverage too high?
- What is the debt maturity profile?
- Are there covenant risks?

**Deliverables**:
- Balance sheet health scorecard
- Debt sustainability report
- Liquidity analysis

#### Week 15-16: Cash Flow Analysis (25 hours)
- [ ] Operating cash flow trends
- [ ] Free cash flow calculation
- [ ] Capital expenditure analysis
- [ ] Cash conversion cycle
- [ ] Dividend sustainability
- [ ] Cash flow to debt ratio

**Critical Analysis**:
```python
# Free Cash Flow calculation
fcf = operating_cash_flow - capital_expenditures

# Cash flow quality
cf_quality = operating_cash_flow / net_income

# Dividend coverage
dividend_coverage = fcf / dividends_paid
```

**Deliverables**:
- Cash flow statement analysis (15 pages)
- FCF projections
- Dividend sustainability assessment

---

### Module 03: Oriental Kopi Fundamental Analysis (100 Hours)

#### Week 17-18: F&B Industry Analysis (25 hours)
- [ ] Malaysian F&B market size and growth
- [ ] Café industry trends
- [ ] Consumer spending patterns
- [ ] Competitive landscape mapping
- [ ] Market positioning analysis
- [ ] Brand strength assessment

**Industry Research**:
- Euromonitor data (if accessible)
- Department of Statistics Malaysia
- Industry reports
- Competitor analysis (OldTown, Starbucks, local cafés)

**Deliverables**:
- Industry analysis report (20 pages)
- Competitive positioning map
- Market opportunity assessment

#### Week 19-20: Unit Economics & Growth (25 hours)
- [ ] Revenue per store analysis
- [ ] Same-store sales growth (SSSG)
- [ ] Store expansion analysis
- [ ] Average transaction value
- [ ] Customer frequency analysis
- [ ] Menu pricing analysis

**Key Metrics for F&B**:
```python
# Store-level economics
revenue_per_store = total_revenue / number_of_stores
sssg = (current_store_revenue - prior_store_revenue) / prior_store_revenue * 100
avg_transaction_value = total_revenue / transaction_count
```

**Deliverables**:
- Unit economics model
- Store expansion projection
- Growth scenario analysis

#### Week 21-22: Profitability & Efficiency (25 hours)
- [ ] Food cost percentage
- [ ] Labor cost analysis
- [ ] Rent and occupancy costs
- [ ] EBITDA margin trends
- [ ] Efficiency ratios
- [ ] Scalability analysis

**F&B Specific Ratios**:
- Food cost % (ideal: 25-35%)
- Labor cost % (ideal: 25-35%)
- Prime cost (food + labor, ideal: <60%)
- Rent as % of sales (ideal: <10%)

**Deliverables**:
- Profitability breakdown
- Cost structure analysis
- Margin improvement opportunities

#### Week 23-24: Financial Health & Valuation (25 hours)
- [ ] Balance sheet analysis
- [ ] Cash flow assessment
- [ ] Growth capital requirements
- [ ] Franchise model analysis (if applicable)
- [ ] Preliminary valuation

**Deliverables**:
- Financial health report
- Capital requirements forecast
- Initial valuation range

---

### Module 04: Comparative Fundamental Analysis (100 Hours)

#### Week 25-26: Financial Metrics Comparison (30 hours)
- [ ] Side-by-side P&L comparison
- [ ] Balance sheet comparison
- [ ] Cash flow comparison
- [ ] Ratio comparison (ROE, margins, etc.)
- [ ] Growth rates comparison
- [ ] Valuation multiples comparison

**Comparison Framework**:
| Metric | UUE (0310.KL) | KOPI (0338.KL) | Industry Avg | Winner |
|--------|---------------|----------------|--------------|--------|
| Revenue Growth (5Y CAGR) | | | | |
| Net Margin | | | | |
| ROE | | | | |
| Debt/Equity | | | | |
| P/E Ratio | | | | |

**Deliverables**:
- Comprehensive comparison spreadsheet
- Visual dashboards
- Strengths/weaknesses matrix

#### Week 27-28: Valuation Analysis (40 hours)
- [ ] Discounted Cash Flow (DCF) models
  - UUE DCF model
  - Oriental Kopi DCF model
- [ ] Relative valuation
  - P/E ratio analysis
  - P/B ratio analysis
  - EV/EBITDA analysis
- [ ] Sensitivity analysis
- [ ] Scenario modeling (bull/base/bear)

**Valuation Techniques**:
```python
# DCF Model Components
wacc = calculate_wacc(risk_free_rate, beta, market_return, cost_of_debt)
fcf_projections = project_free_cash_flows(years=5)
terminal_value = fcf_terminal / (wacc - growth_rate)
enterprise_value = npv(fcf_projections) + terminal_value
equity_value = enterprise_value - net_debt
fair_value_per_share = equity_value / shares_outstanding
```

**Deliverables**:
- DCF models (Excel + Python)
- Valuation reports
- Fair value estimates with ranges

#### Week 29-30: Investment Thesis Development (30 hours)
- [ ] Bull case for UUE
- [ ] Bear case for UUE
- [ ] Bull case for Oriental Kopi
- [ ] Bear case for Oriental Kopi
- [ ] Risk assessment for each
- [ ] Portfolio allocation decision
- [ ] **Final recommendation: BUY / HOLD / AVOID**

**Investment Thesis Template**:
1. **Executive Summary** (1 page)
2. **Business Overview** (2 pages)
3. **Financial Analysis** (5 pages)
4. **Valuation** (3 pages)
5. **Risks** (2 pages)
6. **Recommendation** (1 page)

**Critical Question**:
**"Are these stocks truly good investments, or have I been wrong?"**

**Deliverables**:
- Investment thesis documents (2 x 15-page reports)
- Risk/reward scorecards
- Final BUY/HOLD/AVOID decision with supporting evidence

---

## Phase 3: Technical Analysis (250 Hours)

### Module 05: Technical Analysis - UUE Holdings (80 Hours)

#### Week 31-32: Chart Analysis Foundations (20 hours)
- [ ] Daily, weekly, monthly chart review
- [ ] Trend identification (uptrend, downtrend, sideways)
- [ ] Support and resistance levels
- [ ] Chart patterns (triangles, head & shoulders, etc.)
- [ ] Volume analysis
- [ ] Price action analysis

**Chart Reading Skills**:
- Candlestick patterns
- Trend lines drawing
- Breakout identification
- Volume confirmation

**Tools**:
- TradingView for charting
- mplfinance for Python charting
- Plotly for interactive charts

**Deliverables**:
- Annotated charts with key levels
- Support/resistance database
- Pattern recognition log

#### Week 33-34: Moving Averages & Trends (20 hours)
- [ ] Calculate SMA 20, 50, 100, 200
- [ ] Calculate EMA 12, 26
- [ ] Moving average crossovers
- [ ] Price vs MA analysis
- [ ] Trend strength assessment
- [ ] Backtest MA strategies

**Moving Average Analysis**:
```python
import pandas as pd

# Calculate moving averages
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# Golden cross / Death cross
df['Golden_Cross'] = (df['SMA_50'] > df['SMA_200']) & (df['SMA_50'].shift(1) <= df['SMA_200'].shift(1))
df['Death_Cross'] = (df['SMA_50'] < df['SMA_200']) & (df['SMA_50'].shift(1) >= df['SMA_200'].shift(1))
```

**Deliverables**:
- MA analysis report
- Trend classification system
- Historical signal backtest

#### Week 35-36: Oscillators & Indicators (20 hours)
- [ ] RSI (Relative Strength Index)
- [ ] MACD (Moving Average Convergence Divergence)
- [ ] Stochastic Oscillator
- [ ] Bollinger Bands
- [ ] ATR (Average True Range)
- [ ] Indicator divergences

**Oscillator Implementation**:
```python
import pandas_ta as ta

# RSI
df['RSI'] = ta.rsi(df['Close'], length=14)

# MACD
macd = ta.macd(df['Close'])
df = pd.concat([df, macd], axis=1)

# Bollinger Bands
bbands = ta.bbands(df['Close'], length=20, std=2)
df = pd.concat([df, bbands], axis=1)

# Identify overbought/oversold
df['RSI_Overbought'] = df['RSI'] > 70
df['RSI_Oversold'] = df['RSI'] < 30
```

**Deliverables**:
- Indicator dashboard
- Signal accuracy backtest
- Optimal parameter tuning results

#### Week 37-38: Multi-Timeframe Analysis (20 hours)
- [ ] Daily timeframe analysis
- [ ] Weekly timeframe analysis
- [ ] Monthly timeframe analysis
- [ ] Timeframe alignment strategy
- [ ] Confluence identification
- [ ] Entry timing optimization

**Multi-Timeframe Framework**:
1. **Monthly**: Determine overall trend
2. **Weekly**: Identify intermediate support/resistance
3. **Daily**: Find precise entry points

**Deliverables**:
- Multi-timeframe analysis template
- Alignment indicator
- Entry confidence scoring

---

### Module 06: Technical Analysis - Oriental Kopi (80 Hours)

#### Week 39-42: Complete Technical Analysis (80 hours)
- [ ] Repeat all Module 05 analyses for Oriental Kopi
- [ ] ACE Market liquidity considerations
- [ ] Volatility analysis (higher expected for ACE stocks)
- [ ] Bid-ask spread analysis
- [ ] Volume profile analysis
- [ ] Sector comparison (vs other F&B stocks)

**Additional ACE Market Considerations**:
- Lower trading volumes = harder to enter/exit
- Wider spreads = higher trading costs
- More volatility = larger position risk
- Less institutional coverage = less information

**Deliverables**:
- Complete technical analysis report for KOPI
- Liquidity risk assessment
- Volatility-adjusted position sizing

---

### Module 07: Finding Entry Points (90 Hours)

#### Week 43-44: Buy Zone Identification (30 hours)
- [ ] Current price level assessment (UUE)
- [ ] Current price level assessment (KOPI)
- [ ] Identify technical support levels
- [ ] Calculate risk/reward ratios
- [ ] Define buy zones (price ranges)
- [ ] Set up price alerts

**Buy Zone Framework**:
1. **Optimal Zone** (highest conviction)
   - Multiple support confluences
   - RSI oversold
   - Positive fundamental backdrop
2. **Good Zone** (moderate conviction)
   - Single support level
   - Neutral indicators
3. **Acceptable Zone** (lower conviction)
   - Near current price
   - Minimal technical support

**Example for UUE**:
- **Optimal Buy Zone**: RM 0.75 - 0.78 (strong support + RSI<30)
- **Good Buy Zone**: RM 0.82 - 0.85 (moderate support)
- **Acceptable Zone**: RM 0.88 - 0.90 (weak support)

**Deliverables**:
- Buy zone charts (annotated)
- Alert system setup
- Entry checklist

#### Week 45-46: Entry Strategy Development (30 hours)
- [ ] Scale-in strategy design
- [ ] Lump-sum vs DCA analysis
- [ ] Trigger conditions definition
- [ ] Multi-indicator confirmation
- [ ] Entry timing optimization
- [ ] Test on historical data

**Entry Strategies**:
1. **All-in entry**: Single purchase when all conditions met
2. **Scaled entry**: 3-4 purchases as price falls into buy zone
3. **DCA (Dollar Cost Averaging)**: Regular purchases regardless of price

**Confirmation Checklist**:
- [ ] Price in buy zone ✓
- [ ] RSI < 40 ✓
- [ ] MACD bullish crossover ✓
- [ ] Volume increasing ✓
- [ ] No negative news ✓
- [ ] Fundamental thesis intact ✓

**Deliverables**:
- Entry strategy playbook
- Historical backtest results
- Entry decision tree

#### Week 47-48: Exit Strategy & Stops (30 hours)
- [ ] Stop-loss placement strategies
- [ ] Trailing stop implementation
- [ ] Profit target definition
- [ ] Exit indicator selection
- [ ] Scenario planning
- [ ] Exit discipline framework

**Stop-Loss Strategies**:
1. **Technical stops**: Below support levels
2. **Percentage stops**: Fixed % below entry (e.g., 15%)
3. **Volatility stops**: Based on ATR
4. **Time stops**: Exit if no progress in X months
5. **Fundamental stops**: Exit if thesis breaks

**Profit Targets**:
- **Target 1**: +20% (take 1/3 position off)
- **Target 2**: +50% (take another 1/3 off)
- **Target 3**: +100% (trailing stop on remaining)

**Deliverables**:
- Exit strategy document
- Stop-loss calculator
- Profit target roadmap

---

## Phase 4: News & Market Intelligence (150 Hours)

### Module 08: News Monitoring & Sentiment Analysis (150 Hours)

#### Week 49-50: Web Scraping Setup (30 hours)
- [ ] Identify target news sources
- [ ] Build web scrapers (BeautifulSoup/Selenium)
- [ ] Set up RSS feed readers
- [ ] Create Bursa announcement scraper
- [ ] Build i3investor forum scraper
- [ ] Schedule automated scraping

**News Sources to Scrape**:
1. **The Edge Markets**: Malaysian financial news
2. **Bursa Malaysia**: Official announcements
3. **The Star Biz**: Business news
4. **i3investor**: Forum discussions
5. **Google News**: Keyword alerts

**Scraping Code Example**:
```python
import requests
from bs4 import BeautifulSoup
import schedule
import time

def scrape_the_edge(keyword):
    url = f"https://theedgemalaysia.com/search?keywords={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        date = article.find('time')['datetime']

        # Save to database
        save_article(title, link, date, keyword)

# Schedule daily scraping
schedule.every().day.at("08:00").do(lambda: scrape_the_edge("UUE Holdings"))
schedule.every().day.at("08:00").do(lambda: scrape_the_edge("Oriental Kopi"))

while True:
    schedule.run_pending()
    time.sleep(60)
```

**Deliverables**:
- Web scraping scripts (`scripts/fetch_news.py`)
- News database schema
- Automated scraping scheduler

#### Week 51-52: Sentiment Analysis Implementation (30 hours)
- [ ] NLP preprocessing pipeline
- [ ] Sentiment analysis model selection
- [ ] Train custom sentiment model
- [ ] Apply to news articles
- [ ] Forum sentiment analysis
- [ ] Sentiment scoring system

**Sentiment Analysis Techniques**:
```python
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# TextBlob for general sentiment
def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 to 1
    subjectivity = blob.sentiment.subjectivity  # 0 to 1
    return polarity, subjectivity

# VADER for financial text
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text):
    scores = analyzer.polarity_scores(text)
    return scores['compound']  # -1 to 1

# Classify sentiment
def classify_sentiment(score):
    if score > 0.2:
        return "POSITIVE"
    elif score < -0.2:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
```

**Deliverables**:
- Sentiment analysis pipeline
- Historical sentiment database
- Sentiment scoring dashboard

#### Week 53-54: Event Detection System (30 hours)
- [ ] Define critical events
  - Earnings releases
  - Dividend announcements
  - Contract wins/losses
  - Management changes
  - Regulatory announcements
- [ ] Build event detection rules
- [ ] Create event classification system
- [ ] Historical event impact analysis
- [ ] Event-driven trading signals

**Critical Events to Monitor**:
1. **Quarterly earnings** (forecast vs actual)
2. **Dividend announcements** (amount, ex-date, payment date)
3. **Major contracts** (>RM10M for UUE, new store openings for KOPI)
4. **Management changes** (CEO, CFO, directors)
5. **Regulatory actions** (SC investigations, trading suspensions)
6. **Analyst coverage** (research reports, target prices)

**Deliverables**:
- Event detection rules engine
- Historical event database
- Event impact correlation analysis

#### Week 55-56: Alert System Development (30 hours)
- [ ] Email alert system
- [ ] SMS/Telegram alerts (optional)
- [ ] Alert priority levels
- [ ] Alert templates
- [ ] Alert testing
- [ ] Alert logs and tracking

**Alert Types**:
1. **CRITICAL**: Earnings surprise, regulatory action
2. **HIGH**: Dividend announcement, major contract
3. **MEDIUM**: News mentions, analyst reports
4. **LOW**: Forum discussions, general news

**Alert System Code**:
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject, body, priority="MEDIUM"):
    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    password = "your_app_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"[{priority}] {subject}"

    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Example usage
if new_earnings_detected:
    send_email_alert(
        subject="UUE Q4 2024 Earnings Released",
        body=f"<h3>Earnings Alert</h3><p>EPS: RM0.05 (Beat by 10%)</p>",
        priority="CRITICAL"
    )
```

**Deliverables**:
- Alert system implementation
- Alert configuration file
- Alert response playbook

#### Week 57-58: News Database & Analysis (30 hours)
- [ ] Build comprehensive news database
- [ ] Historical news backfill
- [ ] News impact analysis
- [ ] Correlation: news sentiment vs stock price
- [ ] Topic modeling
- [ ] Trend identification

**News Analysis**:
- How do earnings surprises affect stock price?
- What % move occurs after major news?
- How long does news impact last?
- Which news sources are most predictive?

**Deliverables**:
- News database (SQLite/PostgreSQL)
- News impact study report
- Predictive news signals

---

## Phase 5: Risk Management & Portfolio (100 Hours)

### Module 09: Risk Management & Position Sizing (100 Hours)

#### Week 59-60: Portfolio Allocation Framework (25 hours)
- [ ] Define total portfolio size
- [ ] Sector allocation limits
- [ ] Single stock limits
- [ ] ACE Market exposure limits
- [ ] Correlation analysis (UUE vs KOPI)
- [ ] Diversification strategy

**Portfolio Allocation Rules** (Example):
- **Total ACE Market exposure**: Max 20% of portfolio
- **Single stock limit**: Max 10% of portfolio
- **Sector limits**: Max 30% in any single sector
- **Cash reserve**: Min 20% in cash

**Allocation Example** (RM100,000 portfolio):
- UUE Holdings: RM 8,000 (8%)
- Oriental Kopi: RM 7,000 (7%)
- Other stocks: RM 65,000 (65%)
- Cash: RM 20,000 (20%)

**Deliverables**:
- Portfolio allocation policy
- Correlation analysis
- Rebalancing rules

#### Week 61-62: Position Sizing Calculations (25 hours)
- [ ] Fixed fractional position sizing
- [ ] Volatility-based sizing
- [ ] Kelly Criterion application
- [ ] Risk-based position sizing
- [ ] Position size calculator tool
- [ ] Backtesting position sizing strategies

**Position Sizing Methods**:

1. **Fixed Fractional** (Simplest):
   ```python
   position_size = portfolio_value * allocation_percentage
   shares = position_size / stock_price
   ```

2. **Volatility-Adjusted**:
   ```python
   # Adjust for stock volatility
   target_volatility = 0.02  # 2% daily volatility target
   stock_volatility = df['Returns'].std()
   adjustment_factor = target_volatility / stock_volatility
   position_size = base_position * adjustment_factor
   ```

3. **Risk-Based** (Most sophisticated):
   ```python
   # Risk 1% of portfolio per trade
   portfolio_value = 100000
   risk_per_trade = portfolio_value * 0.01  # RM1000
   entry_price = 0.85
   stop_loss = 0.75
   risk_per_share = entry_price - stop_loss  # RM0.10
   shares_to_buy = risk_per_trade / risk_per_share  # 10,000 shares
   position_size = shares_to_buy * entry_price  # RM8500
   ```

4. **Kelly Criterion**:
   ```python
   # Kelly % = (Win% * Avg Win - Loss% * Avg Loss) / Avg Win
   win_rate = 0.55  # 55% of trades win
   avg_win = 0.15  # Average 15% gain
   avg_loss = 0.08  # Average 8% loss
   kelly_pct = (win_rate * avg_win - (1 - win_rate) * avg_loss) / avg_win
   # Use half-Kelly for safety
   position_pct = kelly_pct * 0.5
   ```

**Deliverables**:
- Position sizing calculator (Excel + Python)
- Backtested sizing strategies
- Position sizing playbook

#### Week 63-64: Stop-Loss & Risk Controls (25 hours)
- [ ] Stop-loss methodology selection
- [ ] Initial stop placement
- [ ] Trailing stop strategies
- [ ] Time-based stops
- [ ] Fundamental stops
- [ ] Emergency exit protocols

**Stop-Loss Strategies**:

1. **Technical Stops**:
   - Below recent support: Entry - (Entry - Support) = Stop
   - Below moving average: Stop at 200-day MA
   - Volatility stops: Entry - (2 × ATR) = Stop

2. **Percentage Stops**:
   - Fixed %: 10%, 15%, 20% below entry
   - ACE Market: Consider wider stops (20-25%) due to volatility

3. **Trailing Stops**:
   - Fixed trailing: Trail by 15% below peak
   - ATR trailing: Trail by 2.5 × ATR below peak
   - MA trailing: Trail at 50-day SMA

**Emergency Protocols**:
- **Circuit breaker**: Exit all positions if portfolio down >10% in 1 week
- **Thesis break**: Exit immediately if fundamental thesis invalidated
- **Liquidity crisis**: Exit if trading volume drops >50% for 5 consecutive days

**Deliverables**:
- Stop-loss decision tree
- Trailing stop calculator
- Risk control checklist

#### Week 65-66: Profit Taking & Exit Strategies (25 hours)
- [ ] Profit target framework
- [ ] Scaled exit strategy
- [ ] Trailing profit stops
- [ ] Rebalancing rules
- [ ] Tax considerations (Malaysian CGT)
- [ ] Exit decision framework

**Profit Taking Strategy**:
```
Entry: RM 0.85
├─ Target 1 (+20%): RM 1.02 → Sell 25% of position
├─ Target 2 (+50%): RM 1.28 → Sell 25% of position
├─ Target 3 (+100%): RM 1.70 → Sell 25% of position
└─ Let final 25% run with trailing stop
```

**Exit Reasons**:
1. **Profit target reached**
2. **Stop-loss triggered**
3. **Time stop** (no progress in 12 months)
4. **Thesis invalidated** (fundamentals deteriorated)
5. **Better opportunity** (reallocation)
6. **Regulatory concerns**

**Tax Notes for Malaysia**:
- **No capital gains tax** on listed stocks (as of 2024)
- Dividend income: Subject to income tax
- Trading frequency: Could be classified as "business income" if excessive

**Deliverables**:
- Profit-taking playbook
- Exit strategy flowchart
- Tax tracking spreadsheet

---

## Phase 6: Dashboard & Automation (100 Hours)

### Module 10: Investment Decision Dashboard (100 Hours)

#### Week 67-68: Dashboard Design & Setup (20 hours)
- [ ] Choose technology stack (Streamlit vs Plotly Dash)
- [ ] Design dashboard layout
- [ ] Define key metrics to display
- [ ] Create wireframes
- [ ] Set up development environment
- [ ] Initialize dashboard project

**Dashboard Sections**:
1. **Overview**: Portfolio summary, daily P&L
2. **Stock Monitors**: Real-time prices, indicators
3. **News Feed**: Latest news with sentiment
4. **Signals**: Buy/sell/hold recommendations
5. **Analytics**: Performance charts, backtests
6. **Alerts**: Recent alerts and notifications

**Technology Choice**:
- **Streamlit**: Easier, faster development (Recommended)
- **Plotly Dash**: More customizable, professional

**Deliverables**:
- Dashboard wireframes
- Technology stack selection
- Initial dashboard skeleton

#### Week 69-70: Real-Time Data Integration (20 hours)
- [ ] Connect to yfinance for live prices
- [ ] Implement price update mechanism
- [ ] Calculate technical indicators in real-time
- [ ] Display fundamental metrics
- [ ] Add benchmark comparisons (FBMKLCI)
- [ ] Performance optimization

**Streamlit Dashboard Code**:
```python
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Stock Selection")
selected_stock = st.sidebar.radio("Choose Stock", ["UUE (0310.KL)", "KOPI (0338.KL)"])

# Map selection
ticker = "0310.KL" if "UUE" in selected_stock else "0338.KL"

# Fetch real-time data
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    info = stock.info
    return hist, info

hist, info = get_stock_data(ticker)

# Main dashboard
st.title(f"{info.get('longName', ticker)} Analysis Dashboard")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Current Price", f"RM {info.get('currentPrice', 'N/A')}")
with col2:
    change_pct = ((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100)
    st.metric("Daily Change", f"{change_pct:.2f}%", delta=change_pct)
with col3:
    st.metric("P/E Ratio", f"{info.get('trailingPE', 'N/A'):.2f}")
with col4:
    st.metric("Market Cap", f"RM {info.get('marketCap', 0)/1e6:.1f}M")

# Price chart
fig = go.Figure(data=[go.Candlestick(
    x=hist.index,
    open=hist['Open'],
    high=hist['High'],
    low=hist['Low'],
    close=hist['Close']
)])
fig.update_layout(title="Price Chart", xaxis_title="Date", yaxis_title="Price (RM)")
st.plotly_chart(fig, use_container_width=True)
```

**Deliverables**:
- Real-time data integration
- Performance-optimized dashboard
- Caching strategy

#### Week 71-72: Visualization & Charts (20 hours)
- [ ] Price chart with indicators overlay
- [ ] Technical indicator panels (RSI, MACD)
- [ ] Volume analysis charts
- [ ] Fundamental scorecards
- [ ] Comparison charts (UUE vs KOPI)
- [ ] Interactive features (zoom, tooltips)

**Advanced Visualizations**:
1. **Multi-indicator chart**: Price + SMA + Bollinger Bands
2. **RSI panel**: With overbought/oversold zones
3. **MACD panel**: Histogram + signal line
4. **Volume profile**: Cumulative volume by price
5. **Heatmap**: Correlation matrix
6. **Sentiment gauge**: News sentiment meter

**Deliverables**:
- Comprehensive chart library
- Interactive visualizations
- Mobile-responsive design

#### Week 73-74: Signal Generation System (20 hours)
- [ ] Define buy/sell/hold logic
- [ ] Implement signal algorithms
- [ ] Backtesting signal accuracy
- [ ] Display signals on dashboard
- [ ] Signal confidence scoring
- [ ] Historical signal tracking

**Signal Logic Example**:
```python
def generate_signal(df, fundamentals):
    # Technical score (0-100)
    tech_score = 0

    # Price vs moving averages
    if df['Close'].iloc[-1] > df['SMA_50'].iloc[-1]:
        tech_score += 20
    if df['Close'].iloc[-1] > df['SMA_200'].iloc[-1]:
        tech_score += 20

    # RSI
    if 30 < df['RSI'].iloc[-1] < 40:  # Mildly oversold
        tech_score += 20

    # MACD
    if df['MACD'].iloc[-1] > df['MACD_signal'].iloc[-1]:
        tech_score += 20

    # Volume
    if df['Volume'].iloc[-1] > df['Volume'].rolling(20).mean().iloc[-1]:
        tech_score += 20

    # Fundamental score (0-100)
    fund_score = fundamentals['total_score']  # From Module 04

    # Combined score
    combined_score = (tech_score * 0.4) + (fund_score * 0.6)

    # Signal generation
    if combined_score >= 70:
        return "STRONG BUY", combined_score
    elif combined_score >= 55:
        return "BUY", combined_score
    elif combined_score >= 45:
        return "HOLD", combined_score
    elif combined_score >= 30:
        return "SELL", combined_score
    else:
        return "STRONG SELL", combined_score
```

**Deliverables**:
- Signal generation engine
- Signal backtest results
- Signal display in dashboard

#### Week 75-76: Automation & Deployment (20 hours)
- [ ] Automated daily data updates
- [ ] Scheduled signal generation
- [ ] Automated alert sending
- [ ] Dashboard deployment (local or cloud)
- [ ] Monitoring and logging
- [ ] Documentation and user guide

**Automation with APScheduler**:
```python
from apscheduler.schedulers.background import BackgroundScheduler

def update_data_job():
    # Fetch latest stock data
    fetch_stock_data()
    # Update news
    fetch_news()
    # Recalculate signals
    generate_signals()
    # Send alerts if needed
    check_and_send_alerts()

scheduler = BackgroundScheduler()
scheduler.add_job(update_data_job, 'cron', hour=18, minute=0)  # 6 PM daily
scheduler.start()
```

**Deployment Options**:
1. **Local**: Run on your computer (simplest)
2. **Cloud**: Deploy to Streamlit Cloud (free tier available)
3. **VPS**: Deploy to DigitalOcean/AWS (more control)

**Deliverables**:
- Fully automated system
- Deployed dashboard (accessible via URL)
- User documentation

---

## Project Deliverables Summary

By the end of 1000 hours, you will have:

### Documentation
- [ ] Personal Investment Policy Statement
- [ ] UUE Holdings Investment Thesis (15 pages)
- [ ] Oriental Kopi Investment Thesis (15 pages)
- [ ] Technical Analysis Reports (2 × 20 pages)
- [ ] Risk Management Playbook
- [ ] Exit Strategy Manual
- [ ] User Guide for Dashboard

### Code & Tools
- [ ] Data collection scripts (automated)
- [ ] Financial analysis notebooks (10 modules)
- [ ] Technical indicator library
- [ ] News scraping system
- [ ] Sentiment analysis engine
- [ ] Position sizing calculator
- [ ] Risk management tool
- [ ] Interactive dashboard (Streamlit)

### Data Assets
- [ ] 5+ years historical price data
- [ ] Financial statements database
- [ ] News and sentiment database
- [ ] Technical indicator database
- [ ] Backtesting results database

### Decisions & Actions
- [ ] **Clear answer**: Are UUE and Oriental Kopi good investments?
- [ ] **Specific buy zones**: Exact prices to enter positions
- [ ] **Risk parameters**: Stop-losses and position sizes defined
- [ ] **Monitoring system**: Automated alerts operational
- [ ] **Track record**: Paper trading results documented

---

## Success Metrics

### Knowledge Metrics
- [ ] Can explain UUE's business model in 5 minutes
- [ ] Can explain Oriental Kopi's business model in 5 minutes
- [ ] Can calculate and interpret key financial ratios
- [ ] Can read technical charts with confidence
- [ ] Can identify buy/sell signals independently
- [ ] Understand risk management principles

### Skill Metrics
- [ ] Built functional data pipeline
- [ ] Created comprehensive financial models
- [ ] Developed working trading system
- [ ] Deployed interactive dashboard
- [ ] Automated news monitoring

### Decision Metrics
- [ ] Made informed BUY/HOLD/AVOID decision on UUE
- [ ] Made informed BUY/HOLD/AVOID decision on Oriental Kopi
- [ ] Defined exact entry prices with supporting evidence
- [ ] Set up automated alerts for opportunities
- [ ] Documented complete risk management plan

---

## Weekly Time Allocation

For a **1000-hour project over 76 weeks** (~18 months):
- **Average**: 13-14 hours/week
- **Intensive periods**: 20-30 hours/week (during analysis phases)
- **Lighter periods**: 5-10 hours/week (during automation setup)

**Recommended Weekly Schedule**:
- **Weekdays**: 1-2 hours/day (reading, coding, analysis)
- **Weekends**: 5-10 hours (deep work, financial modeling, dashboard development)

---

## Adjustment & Flexibility

This plan is **comprehensive but adaptable**:

- **If you finish modules faster**: Add more stocks to analyze
- **If modules take longer**: Extend timeline, don't compromise quality
- **If you find gaps**: Circle back to earlier modules
- **If priorities change**: Adjust focus (e.g., more fundamental, less technical)

---

## Next Steps

**Immediate Actions** (This Week):
1. Review this plan thoroughly
2. Set up development environment
3. Create GitHub repository (optional)
4. Download and read latest UUE annual report
5. Download and read latest Oriental Kopi annual report
6. Begin Module 00: Project Setup and Objectives

**Week 1 Goals**:
- [ ] Complete personal investment framework
- [ ] Read both companies' annual reports
- [ ] Set up Python environment
- [ ] Install required libraries
- [ ] Start notebook 00

---

## Tracking Progress

Use the `ANALYSIS_CHECKLIST.md` to track completed items weekly.

**Monthly Reviews**:
- End of each month: Review progress
- Adjust timeline if needed
- Celebrate completed modules
- Identify blockers and solutions

---

**Let's begin your 1000-hour journey to becoming a competent stock analyst!**

**Current Status**: Plan created, ready to start Module 00
**Next Notebook**: `00_project_setup_and_objectives.ipynb`
