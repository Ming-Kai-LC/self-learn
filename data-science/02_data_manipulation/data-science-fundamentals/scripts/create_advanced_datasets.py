"""
Script to create advanced datasets for intermediate modules.
Generates realistic datasets for ML, DL, time series, NLP, and recommendation systems.
"""

import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def create_sales_timeseries():
    """Create 2 years of daily sales data for time series forecasting (Module 20)."""

    np.random.seed(42)

    # Generate 2 years of dates
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(730)]

    # Base sales with trend and seasonality
    trend = np.linspace(1000, 1500, 730)

    # Weekly seasonality (higher on weekends)
    weekly_pattern = np.array([1.0, 1.0, 1.0, 1.0, 1.1, 1.3, 1.2])
    seasonality = np.tile(weekly_pattern, 730 // 7 + 1)[:730]

    # Monthly seasonality (holiday season)
    monthly_effect = [1.0 + 0.3 * np.sin(2 * np.pi * i / 365) for i in range(730)]

    # Random noise
    noise = np.random.normal(0, 50, 730)

    # Combine components
    sales = trend * seasonality * monthly_effect + noise
    sales = np.maximum(sales, 0)  # No negative sales

    df = pd.DataFrame(
        {
            "date": dates,
            "sales": sales.round(2),
            "day_of_week": [d.strftime("%A") for d in dates],
            "month": [d.month for d in dates],
            "year": [d.year for d in dates],
            "is_weekend": [(d.weekday() >= 5) * 1 for d in dates],
            "is_holiday": [
                ((d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 5)) * 1
                for d in dates
            ],
        }
    )

    return df


def create_customer_reviews():
    """Create customer reviews dataset for NLP (Module 18)."""

    np.random.seed(42)

    # Positive reviews
    positive_reviews = [
        "This product is amazing! Highly recommend it.",
        "Excellent quality and fast shipping. Very satisfied!",
        "Best purchase I've made this year. Love it!",
        "Great value for money. Exceeded my expectations.",
        "Fantastic product! Will definitely buy again.",
        "Outstanding quality. Very happy with this purchase.",
        "Perfect! Exactly what I was looking for.",
        "Superb product. Delivery was quick too.",
        "Absolutely love it! Worth every penny.",
        "Incredible quality. Highly recommended!",
    ]

    # Negative reviews
    negative_reviews = [
        "Terrible product. Complete waste of money.",
        "Very disappointed. Does not work as advertised.",
        "Poor quality. Broke after one use.",
        "Worst purchase ever. Do not recommend.",
        "Horrible experience. Item arrived damaged.",
        "Not worth the price. Very dissatisfied.",
        "Cheaply made. Fell apart immediately.",
        "Awful product. Returning it.",
        "Complete garbage. Save your money.",
        "Disappointing quality. Not as described.",
    ]

    # Neutral reviews
    neutral_reviews = [
        "It's okay. Nothing special but works.",
        "Average product. Gets the job done.",
        "Fair quality for the price.",
        "Not bad, not great. Just okay.",
        "Decent product. Could be better.",
        "It works as expected. Nothing more.",
        "Acceptable quality. No complaints.",
        "Standard product. Does what it says.",
        "Okay for the price. Nothing extraordinary.",
        "It's fine. Meets basic needs.",
    ]

    # Create dataset with 1000 reviews
    reviews = []
    sentiments = []
    ratings = []

    for _ in range(400):  # Positive
        reviews.append(np.random.choice(positive_reviews))
        sentiments.append("positive")
        ratings.append(np.random.choice([4, 5]))

    for _ in range(300):  # Negative
        reviews.append(np.random.choice(negative_reviews))
        sentiments.append("negative")
        ratings.append(np.random.choice([1, 2]))

    for _ in range(300):  # Neutral
        reviews.append(np.random.choice(neutral_reviews))
        sentiments.append("neutral")
        ratings.append(3)

    df = pd.DataFrame(
        {
            "review_id": range(1, 1001),
            "product_id": np.random.randint(100, 200, 1000),
            "customer_id": np.random.randint(1000, 2000, 1000),
            "review_text": reviews,
            "rating": ratings,
            "sentiment": sentiments,
            "helpful_count": np.random.randint(0, 50, 1000),
        }
    )

    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return df


def create_movie_ratings():
    """Create movie ratings for recommendation system (Module 21)."""

    np.random.seed(42)

    # Movies
    movies = [
        "The Matrix",
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Pulp Fiction",
        "Fight Club",
        "Forrest Gump",
        "The Shawshank Redemption",
        "The Godfather",
        "Star Wars",
        "Jurassic Park",
        "Avatar",
        "Titanic",
        "The Avengers",
        "Iron Man",
        "Black Panther",
        "Toy Story",
        "Finding Nemo",
        "The Lion King",
        "Frozen",
        "Harry Potter",
        "Lord of the Rings",
        "The Hobbit",
        "Spider-Man",
        "Batman Begins",
        "Gladiator",
        "Braveheart",
        "Saving Private Ryan",
        "The Terminator",
        "Alien",
        "Blade Runner",
        "The Social Network",
        "Whiplash",
        "La La Land",
        "Parasite",
        "Joker",
        "Get Out",
        "A Quiet Place",
        "Us",
        "Hereditary",
    ]

    # Generate ratings (5000 user-movie interactions)
    n_ratings = 5000
    user_ids = np.random.randint(1, 501, n_ratings)  # 500 users
    movie_indices = np.random.randint(0, len(movies), n_ratings)
    movie_titles = [movies[i] for i in movie_indices]

    # Ratings from 1-5 with realistic distribution
    ratings = np.random.choice([1, 2, 3, 4, 5], n_ratings, p=[0.05, 0.10, 0.20, 0.35, 0.30])

    # Timestamps (last 2 years)
    start_timestamp = int(datetime(2022, 1, 1).timestamp())
    end_timestamp = int(datetime.now().timestamp())
    timestamps = np.random.randint(start_timestamp, end_timestamp, n_ratings)
    dates = [datetime.fromtimestamp(ts).strftime("%Y-%m-%d") for ts in timestamps]

    df = pd.DataFrame(
        {
            "user_id": user_ids,
            "movie_id": movie_indices + 1,
            "movie_title": movie_titles,
            "rating": ratings,
            "timestamp": timestamps,
            "date": dates,
        }
    )

    # Remove duplicates (same user rating same movie twice)
    df = df.drop_duplicates(subset=["user_id", "movie_id"], keep="first")

    return df


def create_sensor_data():
    """Create sensor data for anomaly detection (Module 15)."""

    np.random.seed(42)

    # Generate 10,000 sensor readings
    n_readings = 10000
    timestamps = pd.date_range("2023-01-01", periods=n_readings, freq="1min")

    # Normal sensor readings (temperature in Celsius)
    normal_temp = np.random.normal(25, 2, n_readings)

    # Inject anomalies (about 2% of data)
    anomaly_indices = np.random.choice(n_readings, size=int(n_readings * 0.02), replace=False)

    temperatures = normal_temp.copy()
    is_anomaly = np.zeros(n_readings, dtype=int)

    for idx in anomaly_indices:
        # Spike anomaly or drop anomaly
        if np.random.random() > 0.5:
            temperatures[idx] = np.random.uniform(35, 45)  # Hot spike
        else:
            temperatures[idx] = np.random.uniform(10, 15)  # Cold drop
        is_anomaly[idx] = 1

    # Other sensor readings
    humidity = np.random.normal(60, 5, n_readings)
    pressure = np.random.normal(1013, 10, n_readings)

    df = pd.DataFrame(
        {
            "timestamp": timestamps,
            "temperature": temperatures.round(2),
            "humidity": humidity.round(2),
            "pressure": pressure.round(2),
            "sensor_id": np.random.choice(["A", "B", "C"], n_readings),
            "is_anomaly": is_anomaly,
        }
    )

    return df


def create_feature_engineering_data():
    """Create dataset for feature engineering module (Module 12)."""

    np.random.seed(42)

    n_samples = 1000

    df = pd.DataFrame(
        {
            "age": np.random.randint(18, 80, n_samples),
            "income": np.random.normal(50000, 20000, n_samples).clip(20000, 200000),
            "education_years": np.random.randint(8, 20, n_samples),
            "experience_years": np.random.randint(0, 40, n_samples),
            "num_dependents": np.random.randint(0, 6, n_samples),
            "city": np.random.choice(
                ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"], n_samples
            ),
            "job_category": np.random.choice(
                ["Tech", "Finance", "Healthcare", "Education", "Other"], n_samples
            ),
            "purchase_amount": np.random.normal(500, 200, n_samples).clip(50, 2000),
        }
    )

    # Add target variable (loan approved: yes/no)
    # Higher income, education, and experience increase probability
    prob = (df["income"] / 100000 + df["education_years"] / 20 + df["experience_years"] / 40) / 3
    prob = prob.clip(0, 1)
    df["loan_approved"] = (np.random.random(n_samples) < prob).astype(int)

    return df


def main():
    """Generate all advanced datasets."""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(project_dir, "data_advanced")

    print("Creating Advanced Datasets")
    print("=" * 60)

    # Create datasets
    datasets = {
        "sales_timeseries.csv": create_sales_timeseries(),
        "customer_reviews.csv": create_customer_reviews(),
        "movie_ratings.csv": create_movie_ratings(),
        "sensor_data.csv": create_sensor_data(),
        "feature_engineering.csv": create_feature_engineering_data(),
    }

    # Save datasets
    for filename, df in datasets.items():
        filepath = os.path.join(data_dir, filename)
        df.to_csv(filepath, index=False)
        print(f"[OK] Created {filename} - {len(df)} rows x {len(df.columns)} columns")

    print("=" * 60)
    print("All advanced datasets created successfully!")
    print(f"\nDatasets saved to: {data_dir}")


if __name__ == "__main__":
    main()
