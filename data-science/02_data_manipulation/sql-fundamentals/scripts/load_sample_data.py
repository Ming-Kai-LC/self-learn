"""
Load Sample Data into SQL Databases

This utility script helps load CSV files or custom datasets into the sample databases.
Useful for adding your own data or extending the existing databases.

Usage:
    python scripts/load_sample_data.py

Author: SQL Fundamentals Course
Last Updated: 2025-01
"""

import csv
import sqlite3
from pathlib import Path

import pandas as pd

# Set up paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
DB_DIR = DATA_DIR / "databases"
RAW_DIR = DATA_DIR / "raw"


def load_csv_to_database(csv_path, db_path, table_name, if_exists="append"):
    """
    Load a CSV file into a SQLite database table.

    Parameters:
    -----------
    csv_path : Path or str
        Path to the CSV file
    db_path : Path or str
        Path to the SQLite database
    table_name : str
        Name of the table to create/append to
    if_exists : str, default 'append'
        How to behave if the table already exists:
        - 'fail': Raise a ValueError
        - 'replace': Drop the table before inserting new values
        - 'append': Insert new values to the existing table
    """
    try:
        # Read CSV file
        df = pd.read_csv(csv_path)

        # Connect to database
        conn = sqlite3.connect(db_path)

        # Load data into table
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)

        conn.close()

        print(f"✓ Loaded {len(df)} rows from {csv_path.name} into {table_name} table")
        return True

    except Exception as e:
        print(f"✗ Error loading {csv_path.name}: {e}")
        return False


def inspect_database(db_path):
    """
    Display information about tables in a database.

    Parameters:
    -----------
    db_path : Path or str
        Path to the SQLite database
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    print(f"\nDatabase: {db_path.name}")
    print("=" * 70)

    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        print("-" * 70)

        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        print(f"Rows: {row_count}")

        # Get column info
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        print("\nColumns:")
        for col in columns:
            col_id, name, col_type, not_null, default, pk = col
            pk_str = " [PRIMARY KEY]" if pk else ""
            not_null_str = " NOT NULL" if not_null else ""
            print(f"  - {name}: {col_type}{not_null_str}{pk_str}")

    conn.close()
    print("\n" + "=" * 70)


def export_table_to_csv(db_path, table_name, output_path=None):
    """
    Export a database table to a CSV file.

    Parameters:
    -----------
    db_path : Path or str
        Path to the SQLite database
    table_name : str
        Name of the table to export
    output_path : Path or str, optional
        Path for the output CSV file. If None, saves to data/raw/
    """
    if output_path is None:
        output_path = RAW_DIR / f"{table_name}.csv"

    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()

        df.to_csv(output_path, index=False)
        print(f"✓ Exported {len(df)} rows from {table_name} to {output_path.name}")
        return True

    except Exception as e:
        print(f"✗ Error exporting {table_name}: {e}")
        return False


def create_custom_table_example():
    """
    Example: Create a custom table in the ecommerce database.
    Demonstrates how to add your own tables to existing databases.
    """
    db_path = DB_DIR / "ecommerce.db"

    if not db_path.exists():
        print(f"✗ Database not found: {db_path}")
        print("  Please run setup_databases.py first")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a product reviews table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product_reviews (
            review_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            customer_id INTEGER,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            review_text TEXT,
            review_date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """
    )

    # Insert sample reviews
    sample_reviews = [
        (1, 1, 5, 5, "Excellent laptop! Fast and reliable.", "2024-09-15"),
        (2, 1, 12, 4, "Great performance but a bit pricey.", "2024-09-20"),
        (3, 6, 8, 5, "Best SQL book I have read!", "2024-10-01"),
        (4, 9, 15, 4, "Comfortable and good quality.", "2024-10-10"),
        (5, 15, 3, 5, "Perfect yoga mat for beginners.", "2024-10-15"),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO product_reviews
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        sample_reviews,
    )

    conn.commit()
    conn.close()

    print("✓ Created product_reviews table with sample data")


def main():
    """Main function demonstrating data loading utilities."""
    print("=" * 70)
    print("SQL Fundamentals - Data Loading Utilities")
    print("=" * 70)
    print()

    # Check if databases exist
    if not (DB_DIR / "ecommerce.db").exists():
        print("✗ Databases not found!")
        print("  Please run setup_databases.py first:")
        print("  python scripts/setup_databases.py")
        return

    print("Available functions:")
    print("  1. Inspect databases")
    print("  2. Create custom table (example)")
    print("  3. Export table to CSV (example)")
    print()

    # Inspect all databases
    print("\n1. INSPECTING DATABASES")
    print("=" * 70)
    for db_file in ["ecommerce.db", "employees.db", "sales.db"]:
        db_path = DB_DIR / db_file
        if db_path.exists():
            inspect_database(db_path)

    # Create custom table example
    print("\n2. CREATING CUSTOM TABLE (Example)")
    print("=" * 70)
    create_custom_table_example()

    # Export example
    print("\n3. EXPORTING TABLE TO CSV (Example)")
    print("=" * 70)
    export_table_to_csv(DB_DIR / "ecommerce.db", "categories")

    print()
    print("=" * 70)
    print("Examples completed!")
    print("=" * 70)
    print()
    print("To use these functions in your own scripts:")
    print("  from scripts.load_sample_data import load_csv_to_database")
    print("  load_csv_to_database('mydata.csv', 'database.db', 'table_name')")
    print()


if __name__ == "__main__":
    main()
