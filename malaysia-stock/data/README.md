# Data Directory Structure

This directory is organized to support the Malaysian Stock Technical Analysis educational project.

## Directory Layout

```
data/
├── raw/            # Original, unmodified data
├── processed/      # Cleaned and transformed data
├── sample/         # Small example datasets for testing
└── README.md       # This file
```

## Data Sources

All notebooks in this project use **yfinance** to download Malaysian stock data dynamically:

```python
import yfinance as yf

# Download Malaysian stock data (note the .KL suffix)
data = yf.download('1155.KL', start='2023-01-01', end='2024-12-31')
```

## Why No Static Data Files?

This project intentionally **does not include static CSV or JSON data files** for several reasons:

1. **Always Current**: Stock market data changes daily. Dynamic downloads ensure you always work with up-to-date information.

2. **Educational Value**: Learning to fetch data from APIs (like yfinance) is a crucial skill for real-world data science and trading.

3. **Storage Efficiency**: Stock data can be large. Not storing it in git keeps the repository lean.

4. **Reproducibility**: Anyone can run the notebooks and get the same data for the specified date ranges.

## Malaysian Stock Code Format

Malaysian stocks on Bursa Malaysia use the format: `XXXX.KL`

Examples:
- `1155.KL` - Maybank
- `1295.KL` - Public Bank
- `5398.KL` - Gamuda
- `5285.KL` - Sime Darby Plantation

The `.KL` suffix indicates **K**uala **L**umpur Stock Exchange listing.

## Using the Data Directories

### raw/

Store original, unmodified data here if you download datasets for offline analysis:

```python
# Save raw data
data.to_csv('data/raw/maybank_2023_2024.csv')
```

**Important**: Files in this directory should **never be modified**. Treat them as read-only archives.

### processed/

Store cleaned, transformed, or feature-engineered data here:

```python
# After cleaning and adding indicators
processed_data.to_csv('data/processed/maybank_with_indicators.csv')
```

### sample/

Store small example datasets (< 10MB) for testing or demonstration:

```python
# Save a small sample for quick testing
sample = data.head(100)
sample.to_csv('data/sample/maybank_sample_100days.csv')
```

## Data Persistence vs Dynamic Downloads

### When to Save Data Locally

Save data to these directories when:
- ✅ You need offline access
- ✅ You're doing extensive backtesting (avoid re-downloading)
- ✅ You've performed expensive computations
- ✅ You're creating reproducible research

### When to Use Dynamic Downloads

Use `yfinance` directly when:
- ✅ Following educational notebooks (learning experience)
- ✅ Needing most recent data
- ✅ Doing quick explorations
- ✅ Working with small datasets (< 5 years of daily data)

## Example Workflow

```python
import yfinance as yf
import pandas as pd
from pathlib import Path

# 1. Download data
ticker = '1155.KL'
data = yf.download(ticker, start='2020-01-01', end='2024-12-31')

# 2. Save raw data
raw_path = Path('data/raw')
raw_path.mkdir(exist_ok=True)
data.to_csv(raw_path / f'{ticker}_raw.csv')

# 3. Process data (add indicators, clean, etc.)
# ... your processing code ...

# 4. Save processed data
processed_path = Path('data/processed')
processed_path.mkdir(exist_ok=True)
processed_data.to_csv(processed_path / f'{ticker}_processed.csv')
```

## Data Not in Git

**Note**: The `.gitignore` file excludes `*.csv`, `*.json`, and other data files from version control. This means:

- Data you save locally stays local
- The repository remains lightweight
- Everyone generates their own datasets

## Need Help?

- **yfinance documentation**: https://pypi.org/project/yfinance/
- **Bursa Malaysia**: https://www.bursamalaysia.com/
- **Stock code lookup**: https://www.bursamalaysia.com/trade/trading_resources/listing_directory

---

**Remember**: Stock data is for educational purposes only. Always verify data quality before making any investment decisions.
