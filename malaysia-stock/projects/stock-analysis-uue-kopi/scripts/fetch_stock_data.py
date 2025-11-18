"""
Stock Data Fetcher

This script fetches historical stock price data for UUE Holdings (0310.KL)
and Oriental Kopi (0338.KL) using yfinance.

Usage:
    python scripts/fetch_stock_data.py

Author: Stock Analysis Project
Date: 2025-11-18
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import logging
from typing import Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
DATA_DIR = Path(__file__).parent.parent / 'data' / 'raw'
STOCKS = {
    'UUE': '0310.KL',
    'KOPI': '0338.KL',
    'FBMKLCI': '^KLSE',  # Benchmark
    'FBMACE': '^ACEMD'   # ACE Market Index (if available)
}


def fetch_stock_data(
    ticker: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    period: str = '5y'
) -> Optional[pd.DataFrame]:
    """
    Fetch historical stock data from yfinance.

    Args:
        ticker: Stock ticker symbol (e.g., '0310.KL')
        start_date: Start date in 'YYYY-MM-DD' format (optional)
        end_date: End date in 'YYYY-MM-DD' format (optional)
        period: Period to download (default: '5y' for 5 years)

    Returns:
        DataFrame with stock data, or None if error occurs
    """
    try:
        logger.info(f"Fetching data for {ticker}...")

        if start_date and end_date:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        else:
            data = yf.download(ticker, period=period, progress=False)

        # Validation checks
        if data.empty:
            logger.error(f"No data retrieved for {ticker}")
            return None

        if len(data) == 0:
            logger.error(f"Empty dataset for {ticker}")
            return None

        # Check for missing data
        missing_count = data['Close'].isna().sum()
        if missing_count > 0:
            logger.warning(f"{ticker}: Found {missing_count} missing price data points")

        logger.info(f"Successfully fetched {len(data)} rows for {ticker}")
        logger.info(f"Date range: {data.index[0]} to {data.index[-1]}")

        return data

    except Exception as e:
        logger.error(f"Error fetching {ticker}: {e}")
        return None


def save_stock_data(data: pd.DataFrame, ticker: str, format: str = 'csv') -> bool:
    """
    Save stock data to file.

    Args:
        data: DataFrame with stock data
        ticker: Stock ticker for filename
        format: File format ('csv' or 'parquet')

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create data directory if it doesn't exist
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        # Clean ticker for filename (remove special characters)
        clean_ticker = ticker.replace('.', '_').replace('^', '')
        timestamp = datetime.now().strftime('%Y%m%d')

        if format == 'csv':
            filepath = DATA_DIR / f"{clean_ticker}_{timestamp}.csv"
            data.to_csv(filepath)
            logger.info(f"Saved to {filepath}")
        elif format == 'parquet':
            filepath = DATA_DIR / f"{clean_ticker}_{timestamp}.parquet"
            data.to_parquet(filepath)
            logger.info(f"Saved to {filepath}")
        else:
            logger.error(f"Unsupported format: {format}")
            return False

        # Also save as "latest" version
        latest_filepath = DATA_DIR / f"{clean_ticker}_latest.{format}"
        if format == 'csv':
            data.to_csv(latest_filepath)
        else:
            data.to_parquet(latest_filepath)
        logger.info(f"Saved latest version to {latest_filepath}")

        return True

    except Exception as e:
        logger.error(f"Error saving {ticker}: {e}")
        return False


def fetch_all_stocks(save_format: str = 'csv') -> dict:
    """
    Fetch data for all stocks in the project.

    Args:
        save_format: File format to save ('csv' or 'parquet')

    Returns:
        Dictionary with ticker as key and DataFrame as value
    """
    results = {}

    for name, ticker in STOCKS.items():
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing {name} ({ticker})")
        logger.info(f"{'='*60}")

        data = fetch_stock_data(ticker, period='5y')

        if data is not None:
            # Save data
            save_stock_data(data, ticker, format=save_format)
            results[ticker] = data

            # Print summary
            print(f"\n{name} ({ticker}) Summary:")
            print(f"  Start Date: {data.index[0].strftime('%Y-%m-%d')}")
            print(f"  End Date: {data.index[-1].strftime('%Y-%m-%d')}")
            print(f"  Total Days: {len(data)}")
            print(f"  Latest Close: RM {data['Close'].iloc[-1]:.3f}")
            print(f"  52-Week High: RM {data['Close'].tail(252).max():.3f}")
            print(f"  52-Week Low: RM {data['Close'].tail(252).min():.3f}")
        else:
            logger.error(f"Failed to fetch {name} ({ticker})")

    return results


def get_stock_info(ticker: str) -> dict:
    """
    Get detailed stock information.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary with stock info
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        print(f"\nDetailed Info for {ticker}:")
        print(f"  Company Name: {info.get('longName', 'N/A')}")
        print(f"  Sector: {info.get('sector', 'N/A')}")
        print(f"  Industry: {info.get('industry', 'N/A')}")
        print(f"  Market Cap: RM {info.get('marketCap', 0):,.0f}")
        print(f"  P/E Ratio: {info.get('trailingPE', 'N/A')}")
        print(f"  Dividend Yield: {info.get('dividendYield', 'N/A')}")
        print(f"  52 Week High: RM {info.get('fiftyTwoWeekHigh', 'N/A')}")
        print(f"  52 Week Low: RM {info.get('fiftyTwoWeekLow', 'N/A')}")

        return info

    except Exception as e:
        logger.error(f"Error getting info for {ticker}: {e}")
        return {}


if __name__ == "__main__":
    print("="*60)
    print("Stock Data Fetcher")
    print("UUE Holdings & Oriental Kopi Analysis Project")
    print("="*60)
    print()

    # Fetch all stock data
    results = fetch_all_stocks(save_format='csv')

    # Get detailed info for main stocks
    if results:
        print("\n" + "="*60)
        print("Fetching Detailed Stock Information")
        print("="*60)

        for name, ticker in [('UUE', '0310.KL'), ('KOPI', '0338.KL')]:
            get_stock_info(ticker)

    print("\n" + "="*60)
    print("Data fetching complete!")
    print(f"Files saved to: {DATA_DIR}")
    print("="*60)
