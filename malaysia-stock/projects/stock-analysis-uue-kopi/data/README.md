# Data Folder

This folder contains all data files for the Stock Analysis Project.

## Directory Structure

```
data/
├── raw/                      # Original, unmodified data
│   ├── 0310_KL_*.csv        # UUE historical price data
│   ├── 0338_KL_*.csv        # Oriental Kopi price data
│   └── benchmarks_*.csv     # FBMKLCI, FBMACE data
│
├── processed/                # Cleaned and calculated data
│   ├── uue_with_indicators.csv
│   └── kopi_with_indicators.csv
│
├── financial_statements/     # Company financial reports
│   ├── uue/
│   │   ├── annual_report_2023.pdf
│   │   └── quarterly_*.pdf
│   └── kopi/
│       ├── annual_report_2023.pdf
│       └── quarterly_*.pdf
│
├── news/                     # Scraped news articles
│   ├── uue_news.json
│   ├── kopi_news.json
│   └── sentiment_scores.csv
│
└── analysis_reports/         # Generated analysis outputs
    ├── fundamental_analysis_uue.xlsx
    ├── technical_analysis_kopi.xlsx
    └── valuation_models/
```

## Data Management Rules

### Raw Data
- **NEVER modify** files in `raw/`
- All transformations happen in `processed/`
- Raw data is the source of truth

### File Naming
- Format: `{ticker}_{date}.csv`
- Example: `0310_KL_20250118.csv`
- Latest version: `0310_KL_latest.csv`

### Data Formats
- **CSV**: Human-readable, good for small files
- **Parquet**: Compressed, fast for large files
- **JSON**: For structured data (news, sentiment)

### Size Limits
- Files > 10MB: Do NOT commit to git
- Use `.gitignore` to exclude large files
- Store large files locally or in cloud storage

## Data Sources

### Price Data
- **Source**: Yahoo Finance (yfinance)
- **Frequency**: Daily
- **Update**: Automated via `scripts/fetch_stock_data.py`

### Financial Statements
- **Source**: Bursa Malaysia, company websites
- **Frequency**: Quarterly + Annual
- **Update**: Manual download

### News Data
- **Sources**: The Edge, Bursa, i3investor
- **Frequency**: Daily scraping
- **Update**: Automated via `scripts/fetch_news.py`

## Data Quality Checks

Before using data, verify:
- [ ] No missing dates in price data
- [ ] No null values in critical columns (Close, Volume)
- [ ] Dates are in correct format
- [ ] Prices are reasonable (no outliers)
- [ ] Corporate actions handled (splits, dividends)

## Backup Strategy

- **Local backup**: Weekly export to external drive
- **Cloud backup**: (Optional) Sync to Google Drive / AWS S3
- **Version control**: Git tracks schema changes, not data files

## Security

- **No sensitive data**: Do NOT store API keys, passwords here
- **Public data only**: All data should be publicly available
- **Verify sources**: Always cross-check critical financial data

## Getting Started

1. Run data collection script:
   ```bash
   python scripts/fetch_stock_data.py
   ```

2. Verify data downloaded:
   ```bash
   ls -lh data/raw/
   ```

3. Check data quality:
   ```python
   import pandas as pd
   df = pd.read_csv('data/raw/0310_KL_latest.csv')
   print(df.info())
   print(df.describe())
   ```
