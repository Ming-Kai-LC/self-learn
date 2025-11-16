# SQL Fundamentals - Master Intermediate SQL Skills

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Database](https://img.shields.io/badge/database-SQLite%20%7C%20PostgreSQL%20%7C%20MySQL-orange)

## About This Project

Welcome to **SQL Fundamentals**, a comprehensive, hands-on learning project designed to take you from basic SQL knowledge to intermediate proficiency. This project focuses on real-world database scenarios using interactive Jupyter notebooks with practical examples and exercises.

**Who This Project Is For:**
- Developers with basic SQL knowledge looking to advance their skills
- Data analysts wanting to write more complex queries
- Anyone preparing for technical interviews involving SQL
- Students transitioning from beginner to intermediate SQL concepts

**Why Learn SQL?**
SQL (Structured Query Language) is the universal language for working with relational databases. Whether you're analyzing data, building applications, or managing databases, SQL proficiency is essential. This project emphasizes intermediate concepts that are crucial for real-world data manipulation and analysis.

**What Makes This Project Unique:**
- **Multi-Database Support**: Learn SQL with SQLite, PostgreSQL, and MySQL examples
- **Real-World Datasets**: Practice with realistic e-commerce, employee, and sales data
- **Interactive Learning**: Jupyter notebooks combine theory with hands-on coding
- **Progressive Difficulty**: Each module builds upon previous concepts
- **Interview-Ready**: Covers common SQL interview topics and patterns

## What You'll Learn

By completing this project, you will master:

- **Complex Queries**: Write sophisticated SELECT statements with multiple conditions
- **JOINs**: Master INNER, LEFT, RIGHT, and FULL OUTER joins to combine data
- **Aggregations**: Use GROUP BY, HAVING, and aggregate functions for data analysis
- **Subqueries & CTEs**: Write maintainable queries using Common Table Expressions
- **Data Modification**: Safely INSERT, UPDATE, and DELETE records
- **Database Design**: Understand normalization and schema design principles
- **Performance Optimization**: Create indexes and optimize query performance
- **Advanced SQL**: Use window functions, CASE statements, and complex joins
- **Best Practices**: Write clean, efficient, and maintainable SQL code

## Project Structure

```
sql-fundamentals/
├── README.md                                    # This file
├── requirements.txt                             # Python dependencies
├── notebooks/
│   ├── 00_setup_introduction.ipynb             # Environment setup & SQL basics (30 min)
│   ├── 01_select_from_where.ipynb              # Basic queries (45 min)
│   ├── 02_filtering_sorting.ipynb              # WHERE, ORDER BY, LIMIT (45 min)
│   ├── 03_joins_relationships.ipynb            # INNER, LEFT, RIGHT, FULL JOINs (75 min)
│   ├── 04_aggregation_grouping.ipynb           # COUNT, SUM, AVG, GROUP BY, HAVING (60 min)
│   ├── 05_subqueries_cte.ipynb                 # Subqueries and CTEs (60 min)
│   ├── 06_data_modification.ipynb              # INSERT, UPDATE, DELETE (45 min)
│   ├── 07_database_design.ipynb                # Schema design & normalization (60 min)
│   ├── 08_advanced_queries.ipynb               # Window functions, CASE, complex joins (75 min)
│   ├── 09_performance_optimization.ipynb       # Indexes, query optimization (60 min)
│   ├── 10_final_project.ipynb                  # Complete database project (90 min)
│   └── outputs/                                # Generated files
├── data/
│   ├── databases/                              # Sample SQLite databases
│   │   ├── ecommerce.db
│   │   ├── employees.db
│   │   └── sales.db
│   └── raw/                                    # CSV files for data loading
├── scripts/
│   ├── setup_databases.py                      # Create sample databases
│   └── load_sample_data.py                     # Load datasets into databases
└── docs/
    ├── SQL_CHEAT_SHEET.md                      # Quick reference guide
    ├── SQL_GLOSSARY.md                         # Database terms & definitions
    └── FAQ.md                                  # Common SQL questions
```

## Prerequisites

**Knowledge Requirements:**
- Basic understanding of databases (tables, rows, columns)
- Familiarity with simple SELECT statements
- Basic Python knowledge (helpful but not required)
- Understanding of data types

**Software Requirements:**
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- 500 MB free disk space
- (Optional) PostgreSQL 12+ for PostgreSQL examples
- (Optional) MySQL 8.0+ for MySQL examples

**System Requirements:**
- Windows, macOS, or Linux
- 4 GB RAM minimum (8 GB recommended)
- Internet connection for initial setup

## Installation

### Step 1: Clone or Navigate to This Project

```bash
# If you have the full portfolio
cd projects/sql-fundamentals

# Or clone just this project
git clone <repository-url>
cd sql-fundamentals
```

### Step 2: Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Set Up Sample Databases

```bash
python scripts/setup_databases.py
```

This script will create three sample databases in the `data/databases/` directory:
- `ecommerce.db` - Online store with products, orders, and customers
- `employees.db` - Company database with departments, employees, and salaries
- `sales.db` - Sales tracking with transactions, regions, and performance metrics

### Step 5: Launch Jupyter Notebook

```bash
jupyter notebook
```

Navigate to the `notebooks/` folder and start with `00_setup_introduction.ipynb`.

### Step 6: Verify Installation

Open `00_setup_introduction.ipynb` and run all cells. You should see:
- Successful database connections
- Sample query results
- Confirmation that all libraries are installed

## Learning Path

### Module 00: Setup & Introduction (30 min)
**File**: `00_setup_introduction.ipynb`

**What You'll Learn:**
- Setting up your SQL environment
- Connecting to SQLite databases
- Running your first queries
- Understanding the sample databases

**Topics Covered:**
- Database connections with SQLAlchemy
- SQL magic commands in Jupyter
- Exploring database schema
- Basic SELECT statements review

### Module 01: SELECT, FROM, WHERE (45 min)
**File**: `01_select_from_where.ipynb`

**What You'll Learn:**
- Selecting specific columns
- Filtering rows with WHERE
- Working with comparison operators
- Combining conditions with AND/OR

**Topics Covered:**
- Column selection and aliases
- WHERE clause operators (=, !=, <, >, <=, >=)
- Logical operators (AND, OR, NOT)
- Pattern matching with LIKE
- NULL handling (IS NULL, IS NOT NULL)

**Real-World Applications:**
- Finding specific customer orders
- Filtering product inventory
- Searching employee records

### Module 02: Filtering & Sorting (45 min)
**File**: `02_filtering_sorting.ipynb`

**What You'll Learn:**
- Advanced filtering techniques
- Sorting query results
- Limiting and paginating results
- Using IN and BETWEEN operators

**Topics Covered:**
- ORDER BY (ASC, DESC)
- LIMIT and OFFSET
- IN operator for multiple values
- BETWEEN for ranges
- DISTINCT for unique values

**Real-World Applications:**
- Top 10 customers by revenue
- Recent orders within a date range
- Paginated product listings

### Module 03: JOINs & Relationships (75 min)
**File**: `03_joins_relationships.ipynb`

**What You'll Learn:**
- Understanding table relationships
- INNER JOIN to combine related data
- LEFT JOIN to include all rows from left table
- RIGHT JOIN and FULL OUTER JOIN
- Self-joins and multiple joins

**Topics Covered:**
- Foreign key relationships
- INNER JOIN syntax and logic
- LEFT JOIN vs RIGHT JOIN
- FULL OUTER JOIN (when supported)
- Multi-table joins
- Self-joins for hierarchical data

**Real-World Applications:**
- Customer orders with product details
- Employee manager relationships
- Sales data with regional information

### Module 04: Aggregation & Grouping (60 min)
**File**: `04_aggregation_grouping.ipynb`

**What You'll Learn:**
- Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- Grouping data with GROUP BY
- Filtering groups with HAVING
- Combining aggregations with JOINs

**Topics Covered:**
- COUNT(*) vs COUNT(column)
- SUM and AVG for calculations
- MIN and MAX for extremes
- GROUP BY single and multiple columns
- HAVING for filtered aggregations
- Aggregate functions with JOINs

**Real-World Applications:**
- Total sales by region
- Average order value per customer
- Product category performance
- Monthly revenue reports

### Module 05: Subqueries & CTEs (60 min)
**File**: `05_subqueries_cte.ipynb`

**What You'll Learn:**
- Writing subqueries in WHERE and FROM clauses
- Correlated vs non-correlated subqueries
- Common Table Expressions (CTEs) with WITH
- Recursive CTEs for hierarchical data

**Topics Covered:**
- Subqueries in WHERE clause
- Subqueries in FROM clause (derived tables)
- Subqueries in SELECT clause
- EXISTS and NOT EXISTS
- WITH clause for CTEs
- Multiple CTEs in a single query
- Recursive CTEs

**Real-World Applications:**
- Finding above-average performers
- Comparing values to aggregates
- Breaking complex queries into readable parts
- Organizational hierarchy traversal

### Module 06: Data Modification (45 min)
**File**: `06_data_modification.ipynb`

**What You'll Learn:**
- Inserting new records with INSERT
- Updating existing data with UPDATE
- Deleting records with DELETE
- Transaction safety and best practices

**Topics Covered:**
- INSERT single and multiple rows
- INSERT with SELECT (bulk insert)
- UPDATE with WHERE conditions
- UPDATE with JOINs
- DELETE safely with WHERE
- TRUNCATE vs DELETE
- Transaction basics (BEGIN, COMMIT, ROLLBACK)

**Real-World Applications:**
- Adding new customers and orders
- Updating product prices
- Removing inactive accounts
- Bulk data migrations

### Module 07: Database Design (60 min)
**File**: `07_database_design.ipynb`

**What You'll Learn:**
- Database normalization (1NF, 2NF, 3NF)
- Primary and foreign keys
- Constraints and data integrity
- Schema design best practices

**Topics Covered:**
- Normalization forms
- Primary key design
- Foreign key relationships
- UNIQUE, NOT NULL, CHECK constraints
- Default values
- Entity-relationship diagrams

**Real-World Applications:**
- Designing a customer database
- Creating normalized order tables
- Enforcing data integrity
- Schema optimization

### Module 08: Advanced Queries (75 min)
**File**: `08_advanced_queries.ipynb`

**What You'll Learn:**
- Window functions (ROW_NUMBER, RANK, DENSE_RANK)
- CASE statements for conditional logic
- Complex multi-table joins
- UNION and UNION ALL

**Topics Covered:**
- Window functions and OVER clause
- PARTITION BY for grouped calculations
- Running totals and moving averages
- CASE WHEN for conditional columns
- UNION for combining result sets
- Cross joins and complex join patterns

**Real-World Applications:**
- Ranking products by sales
- Running totals for cumulative metrics
- Conditional data categorization
- Combining data from multiple sources

### Module 09: Performance & Optimization (60 min)
**File**: `09_performance_optimization.ipynb`

**What You'll Learn:**
- Creating and using indexes
- Query execution plans (EXPLAIN)
- Optimization techniques
- Common performance pitfalls

**Topics Covered:**
- Index types (single-column, composite)
- When to use indexes
- EXPLAIN and query analysis
- Query optimization strategies
- Avoiding SELECT *
- Efficient WHERE clauses
- Index maintenance

**Real-World Applications:**
- Speeding up slow queries
- Optimizing report generation
- Database performance tuning
- Identifying bottlenecks

### Module 10: Final Project (90 min)
**File**: `10_final_project.ipynb`

**What You'll Build:**
A complete e-commerce analytics system that combines all learned skills:
- Customer segmentation analysis
- Product recommendation queries
- Sales performance dashboard
- Revenue forecasting queries
- Inventory management system

**Skills Applied:**
- Complex multi-table JOINs
- Advanced aggregations
- Window functions
- CTEs for readable queries
- Performance optimization
- Real-world business logic

**Deliverables:**
- Set of analytical queries
- Documentation of approach
- Performance benchmarks
- Recommendations for improvements

## How to Use This Project

### For Self-Paced Learning:
1. Start with Module 00 to set up your environment
2. Complete one module at a time in order
3. Run all code cells and experiment with variations
4. Complete exercises at the end of each notebook
5. Reference the cheat sheet and glossary as needed
6. Aim for 2-3 modules per week

### For Study Groups:
- Each module is ~45-75 minutes (perfect for sessions)
- Discuss exercises and solutions together
- Share different approaches to problems
- Use the final project for group collaboration

### For Instructors:
- Each module is self-contained with objectives
- Exercises range from basic to challenging
- Final project can be used as assessment
- Datasets can be replaced with domain-specific data

### Recommended Study Schedule:
- **Intensive**: 2 weeks (4-5 modules per week)
- **Standard**: 4 weeks (2-3 modules per week)
- **Relaxed**: 6-8 weeks (1-2 modules per week)

## Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Programming environment |
| Jupyter | 1.0+ | Interactive notebooks |
| SQLite | 3.x | Primary database (no server needed) |
| SQLAlchemy | 2.0+ | Database connectivity |
| pandas | 2.0+ | Data manipulation and analysis |
| ipython-sql | 0.5+ | SQL magic commands |
| PostgreSQL | 12+ | Optional: Advanced features |
| MySQL | 8.0+ | Optional: Alternative database |

## Tips for Success

**1. Practice Regularly:**
- SQL is a hands-on skill - write queries daily
- Try to solve exercises before looking at solutions
- Experiment with variations of example queries

**2. Understand the "Why":**
- Don't just memorize syntax
- Understand when to use each technique
- Think about query efficiency

**3. Use Real Data:**
- The sample databases mirror real-world scenarios
- Try applying concepts to your own data
- Experiment with larger datasets

**4. Read Error Messages:**
- SQL errors are usually informative
- Learn to debug your queries
- Use EXPLAIN to understand execution

**5. Build Projects:**
- Apply SQL to real problems
- Create your own databases
- Combine SQL with other tools (Python, BI tools)

**6. Reference Documentation:**
- Use the cheat sheet for quick syntax lookup
- Consult the glossary for term definitions
- Check the FAQ for common issues

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'sqlalchemy'"
**Solution**: Ensure you've activated your virtual environment and run `pip install -r requirements.txt`

### Issue: "Database is locked"
**Solution**: Close other connections to the database or restart Jupyter kernel

### Issue: "PostgreSQL/MySQL connection failed"
**Solution**: PostgreSQL and MySQL are optional. You can complete the course using SQLite only. For advanced examples, ensure the database server is running.

### Issue: "Kernel keeps dying when running queries"
**Solution**: Large result sets may cause memory issues. Use LIMIT to reduce result size.

### Issue: Slow query performance
**Solution**:
- Check indexes with Module 09
- Use EXPLAIN to analyze queries
- Avoid SELECT * with large tables

### Need More Help?
- Check the FAQ in `docs/FAQ.md`
- Review the SQL Cheat Sheet in `docs/SQL_CHEAT_SHEET.md`
- Consult the Glossary in `docs/SQL_GLOSSARY.md`
- Search for error messages online (Stack Overflow is your friend!)

## Next Steps

After completing this project, you'll be ready for:

**Advanced SQL Topics:**
- Advanced window functions and analytics
- Query optimization at scale
- Database administration and tuning
- Stored procedures and triggers
- Database security and permissions

**Related Technologies:**
- **NoSQL Databases**: MongoDB, Redis, Cassandra
- **Data Warehousing**: Snowflake, Redshift, BigQuery
- **ETL Tools**: Apache Airflow, dbt
- **BI Tools**: Tableau, Power BI, Looker
- **ORMs**: SQLAlchemy (advanced), Django ORM

**Project Ideas:**
1. Build a personal finance tracker with SQL backend
2. Create a movie recommendation system database
3. Analyze public datasets (COVID-19, weather, sports)
4. Build a blog or CMS with SQL database
5. Create an inventory management system

**Recommended Resources:**
- **Books**:
  - "SQL Performance Explained" by Markus Winand
  - "Learning SQL" by Alan Beaulieu
  - "SQL Cookbook" by Anthony Molinaro
- **Websites**:
  - SQLZoo (interactive tutorials)
  - LeetCode SQL problems
  - HackerRank SQL challenges
- **Documentation**:
  - SQLite official docs
  - PostgreSQL documentation
  - MySQL reference manual

## Contributing

Found a bug or have a suggestion? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of a personal learning portfolio. Feel free to use it for educational purposes.

## Acknowledgments

- Sample datasets inspired by real-world e-commerce and business scenarios
- SQL examples follow industry best practices
- Built with feedback from data professionals and educators

---

**Ready to master SQL?** Start with `notebooks/00_setup_introduction.ipynb` and begin your journey!

**Estimated completion time**: 10-12 hours
**Difficulty**: Intermediate
**Prerequisites**: Basic SQL knowledge

Happy querying!
