"""
Download Sample Datasets for Data Visualization Fundamentals

This script downloads sample datasets used throughout the course modules.
Run this script once after installation to prepare your data directory.

Usage:
    python scripts/download_datasets.py
"""

import os
from pathlib import Path

import numpy as np
import pandas as pd

# Define data directory
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("Data Visualization Fundamentals - Dataset Generator")
print("=" * 60)
print()


def generate_stock_data():
    """Generate synthetic stock price data"""
    print("Generating stock price data...")

    np.random.seed(42)
    dates = pd.date_range("2023-01-01", "2024-01-01", freq="D")

    # Generate multiple stocks with random walk
    stocks = ["TECH", "FINANCE", "ENERGY", "HEALTH", "RETAIL"]
    data = {}

    for stock in stocks:
        base_price = np.random.uniform(50, 200)
        returns = np.random.randn(len(dates)) * 0.02
        prices = base_price * np.exp(np.cumsum(returns))
        data[stock] = prices

    df = pd.DataFrame(data, index=dates)
    df.index.name = "Date"

    output_file = DATA_DIR / "stock_prices.csv"
    df.to_csv(output_file)
    print(f"  ✓ Saved: {output_file}")
    return df


def generate_climate_data():
    """Generate synthetic climate data"""
    print("Generating climate data...")

    np.random.seed(42)
    dates = pd.date_range("1990-01-01", "2024-01-01", freq="M")

    # Temperature with trend and seasonality
    trend = np.linspace(14, 15.5, len(dates))
    seasonal = 3 * np.sin(2 * np.pi * np.arange(len(dates)) / 12)
    noise = np.random.randn(len(dates)) * 0.5
    temperature = trend + seasonal + noise

    # CO2 levels with increasing trend
    co2_base = 350
    co2_trend = np.linspace(0, 70, len(dates))
    co2_seasonal = 3 * np.sin(2 * np.pi * np.arange(len(dates)) / 12)
    co2 = co2_base + co2_trend + co2_seasonal + np.random.randn(len(dates)) * 2

    # Sea level
    sea_level_base = 0
    sea_level_trend = np.linspace(0, 100, len(dates))  # mm
    sea_level = sea_level_base + sea_level_trend + np.random.randn(len(dates)) * 5

    df = pd.DataFrame(
        {"Date": dates, "Temperature_C": temperature, "CO2_ppm": co2, "SeaLevel_mm": sea_level}
    )

    output_file = DATA_DIR / "climate_data.csv"
    df.to_csv(output_file, index=False)
    print(f"  ✓ Saved: {output_file}")
    return df


def generate_sales_data():
    """Generate synthetic sales data"""
    print("Generating sales data...")

    np.random.seed(42)

    # Generate sales data for different products and regions
    dates = pd.date_range("2023-01-01", "2023-12-31", freq="D")
    products = ["Product A", "Product B", "Product C", "Product D"]
    regions = ["North", "South", "East", "West"]

    data = []
    for date in dates:
        for product in products:
            for region in regions:
                # Add seasonality and randomness
                base_sales = np.random.randint(50, 200)
                seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.dayofyear / 365)
                sales = int(base_sales * seasonal_factor)
                revenue = sales * np.random.uniform(10, 50)

                data.append(
                    {
                        "Date": date,
                        "Product": product,
                        "Region": region,
                        "Units_Sold": sales,
                        "Revenue": round(revenue, 2),
                    }
                )

    df = pd.DataFrame(data)

    output_file = DATA_DIR / "sales_data.csv"
    df.to_csv(output_file, index=False)
    print(f"  ✓ Saved: {output_file}")
    return df


def generate_survey_data():
    """Generate synthetic survey data"""
    print("Generating survey data...")

    np.random.seed(42)
    n_samples = 500

    # Generate realistic survey responses
    age_groups = np.random.choice(["18-25", "26-35", "36-45", "46-55", "56+"], n_samples)
    education = np.random.choice(
        ["High School", "Bachelor", "Master", "PhD"], n_samples, p=[0.3, 0.4, 0.2, 0.1]
    )
    income = np.random.normal(60000, 25000, n_samples).clip(20000, 200000)
    satisfaction = np.random.randint(1, 11, n_samples)

    df = pd.DataFrame(
        {
            "Age_Group": age_groups,
            "Education": education,
            "Income": income.round(0),
            "Satisfaction": satisfaction,
            "Hours_Per_Week": np.random.randint(0, 60, n_samples),
            "Recommend": np.random.choice(["Yes", "No"], n_samples, p=[0.7, 0.3]),
        }
    )

    output_file = DATA_DIR / "survey_data.csv"
    df.to_csv(output_file, index=False)
    print(f"  ✓ Saved: {output_file}")
    return df


def generate_experiment_data():
    """Generate synthetic experiment data for scientific plots"""
    print("Generating experiment data...")

    np.random.seed(42)

    # Control vs Treatment groups
    control = np.random.normal(100, 15, 100)
    treatment_a = np.random.normal(110, 15, 100)
    treatment_b = np.random.normal(105, 12, 100)

    data = []
    for group, values in [
        ("Control", control),
        ("Treatment A", treatment_a),
        ("Treatment B", treatment_b),
    ]:
        for value in values:
            data.append({"Group": group, "Measurement": value})

    df = pd.DataFrame(data)

    output_file = DATA_DIR / "experiment_data.csv"
    df.to_csv(output_file, index=False)
    print(f"  ✓ Saved: {output_file}")
    return df


def generate_correlation_data():
    """Generate data with various correlation patterns"""
    print("Generating correlation data...")

    np.random.seed(42)
    n_samples = 200

    # Create correlated variables
    x1 = np.random.randn(n_samples)
    x2 = 0.8 * x1 + 0.2 * np.random.randn(n_samples)  # Strong positive
    x3 = -0.6 * x1 + 0.4 * np.random.randn(n_samples)  # Moderate negative
    x4 = np.random.randn(n_samples)  # No correlation
    x5 = 0.5 * x1 + 0.5 * x2 + 0.2 * np.random.randn(n_samples)  # Mixed

    df = pd.DataFrame(
        {"Variable_1": x1, "Variable_2": x2, "Variable_3": x3, "Variable_4": x4, "Variable_5": x5}
    )

    output_file = DATA_DIR / "correlation_data.csv"
    df.to_csv(output_file, index=False)
    print(f"  ✓ Saved: {output_file}")
    return df


def main():
    """Generate all datasets"""

    print("Generating sample datasets for course modules...\n")

    try:
        generate_stock_data()
        generate_climate_data()
        generate_sales_data()
        generate_survey_data()
        generate_experiment_data()
        generate_correlation_data()

        print()
        print("=" * 60)
        print("✓ All datasets generated successfully!")
        print("=" * 60)
        print(f"\nDatasets saved to: {DATA_DIR.absolute()}")
        print("\nGenerated files:")
        print("  - stock_prices.csv (366 days × 5 stocks)")
        print("  - climate_data.csv (408 months of climate data)")
        print("  - sales_data.csv (365 days × 4 products × 4 regions)")
        print("  - survey_data.csv (500 survey responses)")
        print("  - experiment_data.csv (300 experimental measurements)")
        print("  - correlation_data.csv (200 samples × 5 variables)")
        print()
        print("You're ready to start learning data visualization!")
        print()

    except Exception as e:
        print(f"\n❌ Error generating datasets: {e}")
        raise


if __name__ == "__main__":
    main()
