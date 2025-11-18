# Scripts Folder

Automation and utility scripts for the Stock Analysis Project.

## Available Scripts

### Data Collection

- **fetch_stock_data.py**: Download historical price data for UUE and Oriental Kopi
  ```bash
  python scripts/fetch_stock_data.py
  ```

### News Monitoring (To be created)

- **fetch_news.py**: Scrape news from The Edge, Bursa, i3investor
- **sentiment_analysis.py**: Analyze sentiment of news articles
- **send_alerts.py**: Send email/Telegram alerts for important events

### Technical Analysis (To be created)

- **calculate_indicators.py**: Compute technical indicators
- **generate_signals.py**: Generate buy/sell/hold signals
- **backtest_strategy.py**: Backtest trading strategies

### Dashboard (To be created)

- **update_dashboard.py**: Refresh dashboard data
- **run_dashboard.sh**: Launch Streamlit dashboard

## Usage

Each script includes:
- Detailed docstrings
- Command-line arguments (when applicable)
- Error handling and logging
- Configuration via config/stock_config.yaml

## Testing

Run tests for scripts:
```bash
pytest tests/test_scripts.py
```

## Scheduling

Use cron (Linux/Mac) or Task Scheduler (Windows) to run scripts automatically.

Example cron entry (daily at 6 PM):
```
0 18 * * * cd /home/user/self-learn/malaysia-stock/projects/stock-analysis-uue-kopi && python scripts/fetch_stock_data.py
```
