"""
Setup Sample Databases for SQL Fundamentals Course

This script creates three SQLite databases with realistic sample data:
1. ecommerce.db - Online store (products, orders, customers)
2. employees.db - Company database (departments, employees, salaries)
3. sales.db - Sales tracking (transactions, regions, performance)

Usage:
    python scripts/setup_databases.py

Author: SQL Fundamentals Course
Last Updated: 2025-01
"""

import os
import random
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# Set up paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "databases"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Random seed for reproducibility
random.seed(42)


def create_ecommerce_database():
    """Create e-commerce database with products, customers, and orders."""
    db_path = DATA_DIR / "ecommerce.db"

    # Remove existing database
    if db_path.exists():
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT NOT NULL,
            description TEXT
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category_id INTEGER,
            price REAL NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            created_date TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT,
            country TEXT,
            signup_date TEXT
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT NOT NULL,
            total_amount REAL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """
    )

    # Insert sample data - Categories
    categories = [
        (1, "Electronics", "Electronic devices and accessories"),
        (2, "Books", "Physical and digital books"),
        (3, "Clothing", "Apparel and fashion items"),
        (4, "Home & Garden", "Home improvement and garden supplies"),
        (5, "Sports", "Sports equipment and accessories"),
    ]
    cursor.executemany("INSERT INTO categories VALUES (?, ?, ?)", categories)

    # Insert sample data - Products
    products = [
        # Electronics
        (1, "Laptop Pro 15", 1, 1299.99, 25, "2024-01-15"),
        (2, "Wireless Mouse", 1, 29.99, 150, "2024-02-01"),
        (3, "USB-C Hub", 1, 49.99, 80, "2024-02-10"),
        (4, "Mechanical Keyboard", 1, 129.99, 45, "2024-01-20"),
        (5, '27" Monitor', 1, 349.99, 30, "2024-03-01"),
        # Books
        (6, "SQL Mastery", 2, 39.99, 200, "2024-01-05"),
        (7, "Python Data Science", 2, 45.99, 150, "2024-01-10"),
        (8, "Web Development Guide", 2, 34.99, 180, "2024-02-15"),
        # Clothing
        (9, "Cotton T-Shirt", 3, 19.99, 500, "2024-01-25"),
        (10, "Denim Jeans", 3, 59.99, 200, "2024-02-05"),
        (11, "Running Shoes", 3, 89.99, 120, "2024-03-10"),
        # Home & Garden
        (12, "Coffee Maker", 4, 79.99, 60, "2024-01-30"),
        (13, "Garden Tool Set", 4, 45.99, 75, "2024-02-20"),
        (14, "LED Desk Lamp", 4, 34.99, 100, "2024-03-05"),
        # Sports
        (15, "Yoga Mat", 5, 29.99, 180, "2024-01-12"),
        (16, "Dumbbell Set", 5, 119.99, 40, "2024-02-25"),
        (17, "Tennis Racket", 5, 79.99, 55, "2024-03-15"),
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", products)

    # Insert sample data - Customers
    first_names = [
        "John",
        "Jane",
        "Michael",
        "Emily",
        "David",
        "Sarah",
        "James",
        "Emma",
        "Robert",
        "Olivia",
        "William",
        "Sophia",
        "Richard",
        "Isabella",
        "Thomas",
    ]
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
    ]
    cities = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
        "Dallas",
        "Austin",
    ]
    countries = ["USA", "Canada", "UK", "Australia", "Germany"]

    customers = []
    for i in range(1, 51):  # 50 customers
        first = random.choice(first_names)
        last = random.choice(last_names)
        email = f"{first.lower()}.{last.lower()}{i}@email.com"
        city = random.choice(cities)
        country = random.choice(countries)
        days_ago = random.randint(30, 365)
        signup_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        customers.append((i, first, last, email, city, country, signup_date))

    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", customers)

    # Insert sample data - Orders and Order Items
    order_id = 1
    order_item_id = 1
    statuses = ["completed", "completed", "completed", "pending", "shipped"]

    for customer_id in range(1, 51):
        # Each customer has 1-5 orders
        num_orders = random.randint(1, 5)
        for _ in range(num_orders):
            days_ago = random.randint(1, 180)
            order_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
            status = random.choice(statuses)

            # Each order has 1-4 items
            num_items = random.randint(1, 4)
            total_amount = 0
            order_items = []

            for _ in range(num_items):
                product_id = random.randint(1, 17)
                quantity = random.randint(1, 3)
                # Get product price (using the products list above)
                product_price = [p[3] for p in products if p[0] == product_id][0]
                item_total = product_price * quantity
                total_amount += item_total

                order_items.append((order_item_id, order_id, product_id, quantity, product_price))
                order_item_id += 1

            # Insert order
            cursor.execute(
                "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
                (order_id, customer_id, order_date, round(total_amount, 2), status),
            )

            # Insert order items
            cursor.executemany("INSERT INTO order_items VALUES (?, ?, ?, ?, ?)", order_items)

            order_id += 1

    conn.commit()
    conn.close()
    print(f"✓ Created ecommerce.db at {db_path}")


def create_employees_database():
    """Create employees database with departments, employees, and salaries."""
    db_path = DATA_DIR / "employees.db"

    # Remove existing database
    if db_path.exists():
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT NOT NULL,
            location TEXT
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            hire_date TEXT NOT NULL,
            job_title TEXT NOT NULL,
            department_id INTEGER,
            manager_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(department_id),
            FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE salaries (
            salary_id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            salary_amount REAL NOT NULL,
            effective_date TEXT NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        )
    """
    )

    # Insert sample data - Departments
    departments = [
        (1, "Engineering", "San Francisco"),
        (2, "Sales", "New York"),
        (3, "Marketing", "Los Angeles"),
        (4, "Human Resources", "Chicago"),
        (5, "Finance", "Boston"),
    ]
    cursor.executemany("INSERT INTO departments VALUES (?, ?, ?)", departments)

    # Insert sample data - Employees
    first_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Edward",
        "Fiona",
        "George",
        "Hannah",
        "Isaac",
        "Julia",
        "Kevin",
        "Laura",
        "Mark",
        "Nina",
        "Oscar",
    ]
    last_names = [
        "Anderson",
        "Baker",
        "Clark",
        "Davis",
        "Evans",
        "Foster",
        "Green",
        "Harris",
        "Jackson",
        "King",
        "Lewis",
        "Moore",
        "Nelson",
        "Owens",
        "Parker",
    ]

    job_titles = {
        1: [
            "Software Engineer",
            "Senior Engineer",
            "Engineering Manager",
            "Tech Lead",
            "DevOps Engineer",
        ],
        2: ["Sales Representative", "Sales Manager", "Account Executive", "Business Development"],
        3: ["Marketing Specialist", "Marketing Manager", "Content Creator", "SEO Specialist"],
        4: ["HR Specialist", "HR Manager", "Recruiter", "HR Coordinator"],
        5: ["Financial Analyst", "Finance Manager", "Accountant", "Controller"],
    }

    employees = []
    employee_id = 1

    # Create employees for each department
    for dept_id in range(1, 6):
        num_employees = random.randint(8, 12)
        for i in range(num_employees):
            first = random.choice(first_names)
            last = random.choice(last_names)
            email = f"{first.lower()}.{last.lower()}{employee_id}@company.com"
            phone = f"555-{random.randint(1000, 9999)}"
            days_ago = random.randint(30, 2000)
            hire_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
            job_title = random.choice(job_titles[dept_id])
            manager_id = (
                None if i == 0 else random.randint(max(1, employee_id - 5), employee_id - 1)
            )

            employees.append(
                (employee_id, first, last, email, phone, hire_date, job_title, dept_id, manager_id)
            )
            employee_id += 1

    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", employees)

    # Insert sample data - Salaries
    salaries = []
    salary_id = 1
    base_salaries = {
        "Software Engineer": 95000,
        "Senior Engineer": 130000,
        "Engineering Manager": 150000,
        "Tech Lead": 140000,
        "DevOps Engineer": 110000,
        "Sales Representative": 60000,
        "Sales Manager": 95000,
        "Account Executive": 75000,
        "Business Development": 70000,
        "Marketing Specialist": 65000,
        "Marketing Manager": 90000,
        "Content Creator": 60000,
        "SEO Specialist": 68000,
        "HR Specialist": 60000,
        "HR Manager": 85000,
        "Recruiter": 65000,
        "HR Coordinator": 55000,
        "Financial Analyst": 75000,
        "Finance Manager": 100000,
        "Accountant": 70000,
        "Controller": 120000,
    }

    for emp in employees:
        emp_id, _, _, _, _, hire_date, job_title, _, _ = emp
        base_salary = base_salaries.get(job_title, 60000)

        # Add some variation
        salary_amount = base_salary + random.randint(-5000, 15000)

        # Initial salary
        salaries.append((salary_id, emp_id, salary_amount, hire_date))
        salary_id += 1

        # Maybe a raise after 1 year
        if random.random() > 0.5:
            hire_datetime = datetime.strptime(hire_date, "%Y-%m-%d")
            raise_date = (hire_datetime + timedelta(days=365)).strftime("%Y-%m-%d")
            if datetime.strptime(raise_date, "%Y-%m-%d") < datetime.now():
                raise_amount = salary_amount + random.randint(3000, 10000)
                salaries.append((salary_id, emp_id, raise_amount, raise_date))
                salary_id += 1

    cursor.executemany("INSERT INTO salaries VALUES (?, ?, ?, ?)", salaries)

    conn.commit()
    conn.close()
    print(f"✓ Created employees.db at {db_path}")


def create_sales_database():
    """Create sales database with transactions, regions, and performance metrics."""
    db_path = DATA_DIR / "sales.db"

    # Remove existing database
    if db_path.exists():
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """
        CREATE TABLE regions (
            region_id INTEGER PRIMARY KEY,
            region_name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE sales_reps (
            rep_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            region_id INTEGER,
            hire_date TEXT NOT NULL,
            FOREIGN KEY (region_id) REFERENCES regions(region_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE transactions (
            transaction_id INTEGER PRIMARY KEY,
            rep_id INTEGER,
            transaction_date TEXT NOT NULL,
            amount REAL NOT NULL,
            product_category TEXT,
            payment_method TEXT,
            FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE monthly_targets (
            target_id INTEGER PRIMARY KEY,
            rep_id INTEGER,
            month TEXT NOT NULL,
            target_amount REAL NOT NULL,
            achieved_amount REAL DEFAULT 0,
            FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
        )
    """
    )

    # Insert sample data - Regions
    regions = [
        (1, "North America", "USA"),
        (2, "Europe", "UK"),
        (3, "Asia Pacific", "Singapore"),
        (4, "Latin America", "Brazil"),
        (5, "Middle East", "UAE"),
    ]
    cursor.executemany("INSERT INTO regions VALUES (?, ?, ?)", regions)

    # Insert sample data - Sales Reps
    first_names = ["Alex", "Beth", "Chris", "Dana", "Eric", "Faith", "Greg", "Hope"]
    last_names = ["Taylor", "White", "Black", "Blue", "Gray", "Brown", "Silver", "Gold"]

    reps = []
    rep_id = 1
    for region_id in range(1, 6):
        for i in range(random.randint(3, 6)):
            first = random.choice(first_names)
            last = random.choice(last_names)
            email = f"{first.lower()}.{last.lower()}{rep_id}@sales.com"
            days_ago = random.randint(100, 1500)
            hire_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
            reps.append((rep_id, first, last, email, region_id, hire_date))
            rep_id += 1

    cursor.executemany("INSERT INTO sales_reps VALUES (?, ?, ?, ?, ?, ?)", reps)

    # Insert sample data - Transactions
    categories = ["Software", "Hardware", "Services", "Consulting", "Training"]
    payment_methods = ["Credit Card", "Bank Transfer", "PayPal", "Check"]

    transactions = []
    transaction_id = 1

    for rep in reps:
        rep_id = rep[0]
        # Each rep has 20-50 transactions
        num_transactions = random.randint(20, 50)
        for _ in range(num_transactions):
            days_ago = random.randint(1, 365)
            transaction_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
            amount = round(random.uniform(100, 10000), 2)
            category = random.choice(categories)
            payment = random.choice(payment_methods)
            transactions.append(
                (transaction_id, rep_id, transaction_date, amount, category, payment)
            )
            transaction_id += 1

    cursor.executemany("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?)", transactions)

    # Insert sample data - Monthly Targets
    targets = []
    target_id = 1
    months = [
        "2024-01",
        "2024-02",
        "2024-03",
        "2024-04",
        "2024-05",
        "2024-06",
        "2024-07",
        "2024-08",
        "2024-09",
        "2024-10",
        "2024-11",
        "2024-12",
    ]

    for rep in reps:
        rep_id = rep[0]
        for month in months:
            target_amount = round(random.uniform(30000, 100000), 2)
            # Calculate achieved from transactions
            cursor.execute(
                """
                SELECT COALESCE(SUM(amount), 0)
                FROM transactions
                WHERE rep_id = ? AND strftime('%Y-%m', transaction_date) = ?
            """,
                (rep_id, month),
            )
            achieved = cursor.fetchone()[0]
            targets.append((target_id, rep_id, month, target_amount, achieved))
            target_id += 1

    cursor.executemany("INSERT INTO monthly_targets VALUES (?, ?, ?, ?, ?)", targets)

    conn.commit()
    conn.close()
    print(f"✓ Created sales.db at {db_path}")


def main():
    """Main function to create all databases."""
    print("=" * 70)
    print("SQL Fundamentals - Database Setup")
    print("=" * 70)
    print()
    print("Creating sample databases with realistic data...")
    print()

    try:
        create_ecommerce_database()
        create_employees_database()
        create_sales_database()

        print()
        print("=" * 70)
        print("✓ All databases created successfully!")
        print("=" * 70)
        print()
        print("Databases created:")
        print(f"  1. {DATA_DIR / 'ecommerce.db'}")
        print(f"  2. {DATA_DIR / 'employees.db'}")
        print(f"  3. {DATA_DIR / 'sales.db'}")
        print()
        print("You can now start with the Jupyter notebooks!")
        print("Begin with: notebooks/00_setup_introduction.ipynb")
        print()

    except Exception as e:
        print(f"\n✗ Error creating databases: {e}")
        raise


if __name__ == "__main__":
    main()
