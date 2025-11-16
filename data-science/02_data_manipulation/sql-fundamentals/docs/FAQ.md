# SQL Fundamentals - Frequently Asked Questions

Common questions and answers about SQL, databases, and this course.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [SQL Basics](#sql-basics)
3. [Common Errors](#common-errors)
4. [Performance & Optimization](#performance--optimization)
5. [Database Design](#database-design)
6. [Course-Specific](#course-specific)

---

## Getting Started

### Q: Do I need to install a database server?
**A:** No! This course uses SQLite, which is file-based and requires no server installation. Everything you need is included in Python.

### Q: What if I'm completely new to SQL?
**A:** This course is designed for intermediate learners, so basic SQL knowledge is helpful. If you're brand new:
1. Start with Module 00 (Setup & Introduction)
2. Complete Modules 01-02 slowly
3. Practice the exercises
4. Review the glossary for unfamiliar terms

### Q: Can I use PostgreSQL or MySQL instead of SQLite?
**A:** Yes, but:
- SQLite is recommended for learning (simpler, no setup)
- PostgreSQL examples are included in some notebooks
- Syntax is 95% the same across databases
- Some advanced features differ between databases

### Q: How long will it take to complete the course?
**A:** Estimated 10-12 hours total:
- Setup: 30 min
- Core modules (01-09): 8-10 hours
- Final project: 90 min
- At your own pace: 2-4 weeks is typical

---

## SQL Basics

### Q: What's the difference between WHERE and HAVING?
**A:**
- **WHERE** filters rows BEFORE grouping
- **HAVING** filters groups AFTER grouping

```sql
-- WHERE: Filter individual products
SELECT category, COUNT(*)
FROM products
WHERE price > 50  -- Filter rows first
GROUP BY category;

-- HAVING: Filter groups
SELECT category, COUNT(*) AS count
FROM products
GROUP BY category
HAVING COUNT(*) > 10;  -- Filter groups after aggregation
```

### Q: When should I use JOIN vs subquery?
**A:** Use JOIN when:
- Combining related data from multiple tables
- Need data from both tables in results
- Performance is important (usually faster)

Use subquery when:
- Need a calculation for filtering
- Checking existence (EXISTS)
- Query logic is clearer with nesting

```sql
-- JOIN (preferred for combining data)
SELECT p.product_name, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id;

-- Subquery (good for filtering)
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

### Q: What's the difference between UNION and UNION ALL?
**A:**
- **UNION**: Removes duplicate rows (slower)
- **UNION ALL**: Keeps all rows including duplicates (faster)

Use UNION ALL when you know there are no duplicates or duplicates don't matter.

### Q: Why do I get different results with LEFT JOIN vs INNER JOIN?
**A:**
- **INNER JOIN**: Only rows with matches in BOTH tables
- **LEFT JOIN**: All rows from left table, even without matches

```sql
-- INNER JOIN: Only customers with orders
SELECT c.name, o.order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT JOIN: All customers, even without orders
SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
-- Result includes customers with NULL order_id
```

### Q: What does NULL mean and how do I work with it?
**A:** NULL represents missing or unknown data.

**Important rules:**
- NULL ≠ empty string
- NULL ≠ zero
- NULL = NULL is NOT true (NULL means unknown!)
- Use `IS NULL` and `IS NOT NULL`

```sql
-- Wrong
SELECT * FROM products WHERE description = NULL;  -- Returns nothing!

-- Correct
SELECT * FROM products WHERE description IS NULL;

-- NULL in calculations
SELECT 5 + NULL;  -- Result: NULL (any operation with NULL = NULL)
```

### Q: What's the difference between DELETE and TRUNCATE?
**A:**
- **DELETE**: Removes specific rows, can use WHERE, slower, can be rolled back
- **TRUNCATE**: Removes ALL rows, faster, cannot use WHERE, harder to rollback

```sql
-- DELETE specific rows
DELETE FROM orders WHERE order_date < '2020-01-01';

-- TRUNCATE removes everything
TRUNCATE TABLE temp_data;  -- Fast but removes ALL rows!
```

---

## Common Errors

### Q: Why do I get "no such table" error?
**A:** Common causes:
1. **Wrong database**: Check you're connected to the correct database
2. **Typo**: Table name is misspelled
3. **Case sensitivity**: Some databases are case-sensitive
4. **Database not created**: Run `setup_databases.py` first

```python
# Check connected database
conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
```

### Q: Why does my query return no results?
**A:** Check:
1. **WHERE conditions**: Are they too restrictive?
2. **JOIN conditions**: Are they correct?
3. **Data exists**: Does the table have data?
4. **NULL handling**: Are you comparing with NULL correctly?

```sql
-- Debug step-by-step
SELECT COUNT(*) FROM table_name;  -- Does table have data?
SELECT * FROM table_name LIMIT 5;  -- See sample data
SELECT * FROM table_name WHERE condition;  -- Test condition
```

### Q: "Ambiguous column name" error - what does this mean?
**A:** The column appears in multiple tables in your join. Specify which table:

```sql
-- Error: ambiguous
SELECT customer_id, name
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;

-- Fixed: specify table
SELECT
    customers.customer_id,  -- or c.customer_id with alias
    customers.name
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

### Q: Why does my INSERT fail?
**A:** Common reasons:
1. **Primary key violation**: Inserting duplicate primary key
2. **Foreign key violation**: Referenced row doesn't exist
3. **NOT NULL violation**: Missing required field
4. **CHECK constraint**: Value doesn't meet condition
5. **Wrong data type**: Inserting text into numeric column

```sql
-- Check constraints
PRAGMA table_info(table_name);  -- See NOT NULL, data types
SELECT name FROM sqlite_master WHERE type='index';  -- See indexes/keys
```

### Q: "Database is locked" error?
**A:** SQLite allows only one write at a time.

**Solutions:**
1. Close other connections to the database
2. Restart Jupyter kernel
3. Check if another program has the file open
4. Wait a moment and retry

---

## Performance & Optimization

### Q: How do I know if my query is slow?
**A:** Benchmark it:

```python
import time

start = time.time()
cursor.execute("SELECT * FROM large_table WHERE condition")
results = cursor.fetchall()
end = time.time()

print(f"Query took {(end-start)*1000:.2f}ms")
```

**Generally:**
- < 100ms: Good
- 100-500ms: Acceptable
- > 500ms: Needs optimization
- > 1000ms: Definitely needs optimization

### Q: When should I create an index?
**A:** Create indexes on:
- Primary keys (automatic)
- Foreign keys
- Columns frequently used in WHERE
- Columns frequently used in JOIN
- Columns frequently used in ORDER BY

**Don't index:**
- Small tables (< 1000 rows)
- Columns rarely queried
- Columns with low cardinality (few unique values like boolean)
- Tables with heavy INSERT/UPDATE activity

### Q: Why isn't my index being used?
**A:** Common reasons:
1. **Function in WHERE**: `WHERE UPPER(name) = 'JOHN'` prevents index use
2. **Type mismatch**: Comparing string column to number
3. **Leading wildcard**: `WHERE name LIKE '%test'` (can't use index)
4. **OR conditions**: Often prevents index use
5. **Small table**: Optimizer decides full scan is faster

Check with EXPLAIN QUERY PLAN

### Q: What's better: IN or EXISTS?
**A:** Generally:
- **EXISTS**: Better for correlated subqueries
- **IN**: Fine for small, non-correlated lists

```sql
-- EXISTS (better for large subqueries)
SELECT product_name FROM products p
WHERE EXISTS (
    SELECT 1 FROM order_items oi
    WHERE oi.product_id = p.product_id
);

-- IN (fine for small lists)
SELECT product_name FROM products
WHERE category_id IN (1, 2, 3);
```

### Q: Should I use SELECT * or list columns?
**A:** Always list specific columns in production code:

**Reasons:**
- Faster (less data transferred)
- Clearer intent
- Prevents breaking changes if columns are added
- Better for optimization

```sql
-- Bad (production)
SELECT * FROM products;

-- Good
SELECT product_id, product_name, price FROM products;

-- OK for quick testing
SELECT * FROM products LIMIT 5;
```

---

## Database Design

### Q: How do I choose a primary key?
**A:** Options:
1. **Auto-incrementing integer**: Most common, simple
2. **UUID/GUID**: Good for distributed systems
3. **Natural key**: Existing unique value (email, SSN)
4. **Composite key**: Multiple columns (for junction tables)

**Best practice:** Use auto-incrementing integer for most tables

### Q: When should I normalize vs denormalize?
**A:**

**Normalize (separate tables) when:**
- Building transactional systems (OLTP)
- Data integrity is critical
- Data changes frequently
- Reducing redundancy matters

**Denormalize (combine data) when:**
- Building analytics systems (OLAP)
- Query performance is critical
- Data is read-heavy
- Redundancy is acceptable

### Q: What's the difference between one-to-many and many-to-many?
**A:**

**One-to-Many**: One record relates to many records
```sql
-- One customer, many orders
customers (1) ----< (many) orders
```

**Many-to-Many**: Many records relate to many records
```sql
-- Many students, many courses
-- Requires junction table
students >----< enrollments >----< courses
```

### Q: Do I need an index on every foreign key?
**A:** Usually yes:
- Speeds up JOIN operations
- Small overhead
- Critical for referential integrity checks

```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

---

## Course-Specific

### Q: The setup script fails - what do I do?
**A:** Troubleshooting steps:
1. Ensure Python 3.8+ is installed: `python --version`
2. Activate virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Check file permissions
5. Try running with full path:
   ```bash
   python D:/Users/USER/.../scripts/setup_databases.py
   ```

### Q: Can I skip modules?
**A:** Not recommended, but:
- **Can skip**: Modules 06-07 if you only want querying (not design/modification)
- **Don't skip**: Modules 00-05 (core foundation)
- **Should do**: Module 10 (final project - brings everything together)

### Q: How do I reset the sample databases?
**A:** Simply re-run the setup script:
```bash
python scripts/setup_databases.py
```
This deletes and recreates all sample databases.

### Q: Can I add my own data to the sample databases?
**A:** Yes! Use the load_sample_data.py utilities:

```python
from scripts.load_sample_data import load_csv_to_database

load_csv_to_database('mydata.csv', 'path/to/db.db', 'table_name')
```

### Q: SQL magic commands (%sql, %%sql) don't work
**A:** Make sure you loaded the extension:
```python
%load_ext sql
```

If still not working:
1. Restart Jupyter kernel
2. Reinstall ipython-sql: `pip install ipython-sql`
3. Use pandas alternative:
   ```python
   pd.read_sql_query("SELECT * FROM table", conn)
   ```

### Q: Where can I practice more?
**A:** Resources:
1. **LeetCode**: SQL problems (interview prep)
2. **HackerRank**: SQL challenges
3. **SQLZoo**: Interactive tutorials
4. **Kaggle**: Real datasets to analyze
5. **Mode Analytics**: SQL tutorials with real data

### Q: What should I learn after this course?
**A:** Next steps:
1. **Advanced SQL**: Recursive CTEs, advanced window functions
2. **Database Administration**: Backup, security, user management
3. **BI Tools**: Tableau, Power BI, Looker
4. **Data Warehousing**: Snowflake, Redshift, BigQuery
5. **ETL/ELT**: Apache Airflow, dbt
6. **NoSQL**: MongoDB, Redis (different paradigm)

### Q: How do I get help if I'm stuck?
**A:** Resources in order:
1. **Course docs**: Check FAQ, Glossary, Cheat Sheet
2. **Error messages**: Read them carefully (often say exactly what's wrong)
3. **EXPLAIN**: Use EXPLAIN QUERY PLAN to understand query execution
4. **Print/Debug**: Add LIMIT, break complex queries into steps
5. **Search**: Google the error message
6. **Ask**: Stack Overflow (with sample data and expected output)

---

## Still Have Questions?

**Additional Resources:**
- **SQL Cheat Sheet**: `docs/SQL_CHEAT_SHEET.md`
- **Glossary**: `docs/SQL_GLOSSARY.md`
- **Course Notebooks**: Review modules for detailed explanations

**External Resources:**
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [Stack Overflow - SQL Tag](https://stackoverflow.com/questions/tagged/sql)
- [SQL Style Guide](https://www.sqlstyle.guide/)

---

**Happy Learning!**
