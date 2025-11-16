# SQL Fundamentals - Quick Reference Cheat Sheet

A comprehensive reference guide for SQL commands and syntax covered in this course.

---

## Table of Contents
1. [SELECT Basics](#select-basics)
2. [Filtering](#filtering)
3. [Sorting & Limiting](#sorting--limiting)
4. [Joins](#joins)
5. [Aggregation](#aggregation)
6. [Subqueries & CTEs](#subqueries--ctes)
7. [Data Modification](#data-modification)
8. [Database Design](#database-design)
9. [Advanced Queries](#advanced-queries)
10. [Performance](#performance)

---

## SELECT Basics

### Select All Columns
```sql
SELECT * FROM table_name;
```

### Select Specific Columns
```sql
SELECT column1, column2 FROM table_name;
```

### Column Aliases
```sql
SELECT
    column1 AS alias1,
    column2 AS "Alias with Spaces"
FROM table_name;
```

### Calculated Columns
```sql
SELECT
    price,
    quantity,
    price * quantity AS total
FROM table_name;
```

### DISTINCT Values
```sql
SELECT DISTINCT column_name FROM table_name;
```

---

## Filtering

### WHERE Clause
```sql
SELECT * FROM table_name
WHERE condition;
```

### Comparison Operators
```sql
WHERE price = 100        -- Equal
WHERE price != 100       -- Not equal
WHERE price <> 100       -- Not equal (alternative)
WHERE price > 100        -- Greater than
WHERE price < 100        -- Less than
WHERE price >= 100       -- Greater than or equal
WHERE price <= 100       -- Less than or equal
```

### Logical Operators
```sql
-- AND (all conditions must be true)
WHERE price > 50 AND stock > 0

-- OR (at least one condition must be true)
WHERE category = 'Books' OR category = 'Electronics'

-- NOT (negates a condition)
WHERE NOT category = 'Books'
```

### IN Operator
```sql
WHERE category_id IN (1, 3, 5)
WHERE country IN ('USA', 'Canada', 'UK')
WHERE category_id NOT IN (1, 2)
```

### BETWEEN
```sql
WHERE price BETWEEN 50 AND 100
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
WHERE price NOT BETWEEN 20 AND 80
```

### NULL Values
```sql
WHERE column IS NULL
WHERE column IS NOT NULL
```

### Pattern Matching (LIKE)
```sql
WHERE name LIKE 'A%'        -- Starts with A
WHERE name LIKE '%book%'    -- Contains 'book'
WHERE name LIKE '%er'       -- Ends with 'er'
WHERE name LIKE '_a%'       -- Second character is 'a'
```

**Wildcards:**
- `%` - Matches any sequence of characters
- `_` - Matches exactly one character

---

## Sorting & Limiting

### ORDER BY
```sql
-- Ascending (default)
SELECT * FROM products ORDER BY price;
SELECT * FROM products ORDER BY price ASC;

-- Descending
SELECT * FROM products ORDER BY price DESC;

-- Multiple columns
SELECT * FROM products
ORDER BY category_id ASC, price DESC;
```

### LIMIT
```sql
-- First 10 rows
SELECT * FROM products LIMIT 10;

-- Rows 11-20 (pagination)
SELECT * FROM products LIMIT 10 OFFSET 10;
```

---

## Joins

### INNER JOIN
```sql
SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### LEFT JOIN
```sql
SELECT *
FROM table1 t1
LEFT JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### Multiple Joins
```sql
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```

### Self Join
```sql
SELECT
    e1.name AS employee,
    e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

---

## Aggregation

### Aggregate Functions
```sql
COUNT(*)                    -- Count all rows
COUNT(column)               -- Count non-NULL values
COUNT(DISTINCT column)      -- Count unique values
SUM(column)                 -- Sum of values
AVG(column)                 -- Average
MIN(column)                 -- Minimum value
MAX(column)                 -- Maximum value
```

### GROUP BY
```sql
SELECT
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM products
GROUP BY category;
```

### GROUP BY with Multiple Columns
```sql
SELECT
    category,
    brand,
    COUNT(*) AS count
FROM products
GROUP BY category, brand;
```

### HAVING (Filter Grouped Results)
```sql
SELECT
    category,
    COUNT(*) AS count
FROM products
GROUP BY category
HAVING COUNT(*) > 10;
```

### GROUP BY with JOIN
```sql
SELECT
    c.category_name,
    COUNT(p.product_id) AS product_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name;
```

---

## Subqueries & CTEs

### Subquery in WHERE
```sql
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

### Subquery in FROM
```sql
SELECT *
FROM (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
) AS category_avg
WHERE avg_price > 100;
```

### EXISTS
```sql
SELECT product_name
FROM products p
WHERE EXISTS (
    SELECT 1 FROM order_items oi
    WHERE oi.product_id = p.product_id
);
```

### Common Table Expressions (CTE)
```sql
WITH expensive_products AS (
    SELECT product_id, product_name, price
    FROM products
    WHERE price > 100
)
SELECT * FROM expensive_products
ORDER BY price DESC;
```

### Multiple CTEs
```sql
WITH
cte1 AS (SELECT ...),
cte2 AS (SELECT ...)
SELECT * FROM cte1
JOIN cte2 ON ...;
```

---

## Data Modification

### INSERT
```sql
-- Insert single row
INSERT INTO table_name (col1, col2)
VALUES (value1, value2);

-- Insert multiple rows
INSERT INTO table_name (col1, col2)
VALUES
    (value1a, value2a),
    (value1b, value2b);

-- Insert from SELECT
INSERT INTO table_name (col1, col2)
SELECT col1, col2 FROM other_table;
```

### UPDATE
```sql
-- Update with WHERE
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

-- Update all rows (dangerous!)
UPDATE table_name
SET column1 = value1;
```

### DELETE
```sql
-- Delete specific rows
DELETE FROM table_name
WHERE condition;

-- Delete all rows (dangerous!)
DELETE FROM table_name;
```

### Transactions
```sql
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Or rollback on error
ROLLBACK;
```

---

## Database Design

### CREATE TABLE
```sql
CREATE TABLE table_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    column1 TEXT NOT NULL,
    column2 INTEGER DEFAULT 0,
    column3 REAL CHECK (column3 >= 0),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (column1) REFERENCES other_table(id)
);
```

### Constraints
```sql
PRIMARY KEY             -- Unique identifier
FOREIGN KEY            -- Link to another table
NOT NULL               -- Cannot be null
UNIQUE                 -- All values must be unique
CHECK (condition)      -- Custom validation
DEFAULT value          -- Default value
AUTOINCREMENT          -- Auto-incrementing number
```

### CREATE INDEX
```sql
-- Single column index
CREATE INDEX idx_name ON table_name(column);

-- Composite index
CREATE INDEX idx_name ON table_name(col1, col2);

-- Unique index
CREATE UNIQUE INDEX idx_name ON table_name(column);
```

### DROP TABLE/INDEX
```sql
DROP TABLE IF EXISTS table_name;
DROP INDEX IF EXISTS index_name;
```

---

## Advanced Queries

### CASE Statements
```sql
SELECT
    product_name,
    price,
    CASE
        WHEN price < 30 THEN 'Budget'
        WHEN price BETWEEN 30 AND 100 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_tier
FROM products;
```

### Window Functions
```sql
-- ROW_NUMBER
SELECT
    product_name,
    price,
    ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products;

-- RANK
SELECT
    product_name,
    category_id,
    price,
    RANK() OVER (PARTITION BY category_id ORDER BY price DESC) AS rank
FROM products;

-- Running Total
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;
```

### UNION
```sql
-- UNION (removes duplicates)
SELECT column FROM table1
UNION
SELECT column FROM table2;

-- UNION ALL (keeps duplicates, faster)
SELECT column FROM table1
UNION ALL
SELECT column FROM table2;
```

---

## Performance

### EXPLAIN Query Plan
```sql
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price > 100;
```

### Index Best Practices
- Index foreign keys
- Index columns frequently used in WHERE
- Index columns frequently used in JOIN
- Index columns frequently used in ORDER BY
- Don't over-index (slows INSERT/UPDATE/DELETE)

### Query Optimization Tips
1. **Avoid SELECT *** - Select only needed columns
2. **Use LIMIT** when testing queries
3. **Use EXISTS** instead of IN for subqueries
4. **Use JOINs** instead of subqueries when possible
5. **Filter early** in subqueries and CTEs
6. **Avoid functions** on indexed columns in WHERE
7. **Use indexes** on frequently queried columns
8. **Analyze with EXPLAIN** QUERY PLAN

---

## Common Patterns

### Top N Per Group
```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY price DESC) AS rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 3;
```

### Pivot (Rows to Columns)
```sql
SELECT
    month,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending
FROM orders
GROUP BY month;
```

### Running Calculations
```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS cumulative_total,
    AVG(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3
FROM orders;
```

### Deduplication
```sql
-- Find duplicates
SELECT email, COUNT(*) AS count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- Delete duplicates (keep first)
DELETE FROM customers
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM customers
    GROUP BY email
);
```

---

## String Functions

```sql
-- Concatenation
column1 || ' ' || column2
CONCAT(column1, ' ', column2)

-- Case conversion
UPPER(column)
LOWER(column)

-- Trimming
TRIM(column)
LTRIM(column)
RTRIM(column)

-- Substring
SUBSTR(column, start, length)

-- Length
LENGTH(column)
```

---

## Date Functions (SQLite)

```sql
-- Current date/time
DATE('now')
DATETIME('now')
TIME('now')

-- Format dates
strftime('%Y-%m', date_column)     -- 2024-01
strftime('%Y-%m-%d', date_column)  -- 2024-01-15

-- Date arithmetic
DATE('now', '+7 days')
DATE('now', '-1 month')
DATE('now', 'start of month')
DATE('now', 'start of year')
```

---

## Helpful Shortcuts

### Quick Table Info
```sql
-- List all tables
SELECT name FROM sqlite_master WHERE type='table';

-- Show table schema
PRAGMA table_info(table_name);

-- List indexes
SELECT name FROM sqlite_master WHERE type='index';
```

### Quick Stats
```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT column) AS unique_values,
    MIN(column) AS min_value,
    MAX(column) AS max_value,
    AVG(column) AS avg_value
FROM table_name;
```

---

## Quick Reference: Execution Order

SQL statements are executed in this order:

1. **FROM** / **JOIN** - Get the data
2. **WHERE** - Filter rows
3. **GROUP BY** - Group rows
4. **HAVING** - Filter groups
5. **SELECT** - Choose columns
6. **ORDER BY** - Sort results
7. **LIMIT** / **OFFSET** - Limit results

---

## Need More Help?

- **Glossary**: See `SQL_GLOSSARY.md` for term definitions
- **FAQ**: Check `FAQ.md` for common questions
- **Notebooks**: Review module notebooks for detailed examples

**Happy Querying!**
