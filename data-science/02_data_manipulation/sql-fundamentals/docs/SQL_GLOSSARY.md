# SQL Fundamentals - Glossary of Terms

A comprehensive glossary of database and SQL terms used in this course.

---

## How to Use This Glossary

Terms are organized alphabetically. Each term includes:
- **Definition**: Clear explanation of the term
- **Why It Matters**: Practical importance
- **Example**: Real-world usage

---

## A

### Aggregate Function
**Definition**: A function that performs a calculation on multiple rows and returns a single value.

**Why It Matters**: Essential for data analysis - calculating totals, averages, counts, etc.

**Example**:
```sql
SELECT COUNT(*) AS total_products, AVG(price) AS average_price
FROM products;
```

**Common aggregate functions**: COUNT(), SUM(), AVG(), MIN(), MAX()

---

### Alias
**Definition**: A temporary name assigned to a table or column in a query.

**Why It Matters**: Makes queries more readable and allows shorter names for complex expressions.

**Example**:
```sql
SELECT
    product_name AS name,
    price * 1.1 AS price_with_tax
FROM products AS p;
```

---

### AND
**Definition**: Logical operator that combines two or more conditions; all must be true.

**Why It Matters**: Allows precise filtering of data.

**Example**:
```sql
SELECT * FROM products
WHERE price > 50 AND stock_quantity > 0;
```

---

### AUTOINCREMENT
**Definition**: Automatically generates a unique number for each new row.

**Why It Matters**: Simplifies primary key generation.

**Example**:
```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT
);
```

---

## B

### BETWEEN
**Definition**: Operator that selects values within a specified range (inclusive).

**Why It Matters**: Cleaner syntax than using >= AND <=.

**Example**:
```sql
SELECT * FROM products
WHERE price BETWEEN 50 AND 100;
```

---

## C

### Cardinality
**Definition**: The uniqueness of data values in a column. High cardinality means many unique values; low cardinality means few.

**Why It Matters**: Affects index effectiveness - high cardinality columns benefit more from indexes.

**Example**:
- High cardinality: email addresses (mostly unique)
- Low cardinality: gender (few values)

---

### CASE Statement
**Definition**: Adds conditional logic to SQL queries (similar to if/else).

**Why It Matters**: Enables data categorization and transformation within queries.

**Example**:
```sql
SELECT
    product_name,
    CASE
        WHEN price < 30 THEN 'Budget'
        WHEN price < 100 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_tier
FROM products;
```

---

### Cartesian Product
**Definition**: Result when tables are joined without a condition - every row from the first table is combined with every row from the second.

**Why It Matters**: Usually an error that produces massive, meaningless result sets.

**Example** (avoid this):
```sql
SELECT * FROM table1, table2;  -- Missing JOIN condition!
```

---

### Column
**Definition**: A vertical structure in a table that stores a specific type of data.

**Why It Matters**: Fundamental building block of relational databases.

**Example**: In a `customers` table: customer_id, first_name, last_name, email

---

### Composite Key
**Definition**: A primary key composed of multiple columns.

**Why It Matters**: Used when no single column uniquely identifies a row.

**Example**:
```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    PRIMARY KEY (student_id, course_id)
);
```

---

### Constraint
**Definition**: A rule enforced on data in a table.

**Why It Matters**: Ensures data integrity and validity.

**Example**:
```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    price REAL CHECK (price > 0),
    email TEXT UNIQUE NOT NULL
);
```

**Types**: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT

---

### Correlated Subquery
**Definition**: A subquery that references columns from the outer query.

**Why It Matters**: Enables row-by-row comparison between tables.

**Example**:
```sql
SELECT product_name, price
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE category_id = p.category_id
);
```

---

### CTE (Common Table Expression)
**Definition**: A temporary named result set defined with the WITH clause.

**Why It Matters**: Makes complex queries more readable and maintainable.

**Example**:
```sql
WITH expensive_products AS (
    SELECT * FROM products WHERE price > 100
)
SELECT * FROM expensive_products ORDER BY price DESC;
```

---

## D

### Database
**Definition**: An organized collection of structured data stored electronically.

**Why It Matters**: Foundation for storing and retrieving information in applications.

---

### DDL (Data Definition Language)
**Definition**: SQL commands that define database structure.

**Why It Matters**: Used to create, modify, and delete database objects.

**Commands**: CREATE, ALTER, DROP, TRUNCATE

---

### DELETE
**Definition**: SQL command to remove rows from a table.

**Why It Matters**: Permanently removes data (use with caution!).

**Example**:
```sql
DELETE FROM customers WHERE last_login < '2020-01-01';
```

---

### DENSE_RANK()
**Definition**: Window function that assigns ranks without gaps.

**Why It Matters**: Useful for rankings where tied values should have the same rank.

**Example**:
```sql
SELECT
    product_name,
    price,
    DENSE_RANK() OVER (ORDER BY price DESC) AS rank
FROM products;
```

---

### DML (Data Manipulation Language)
**Definition**: SQL commands that manipulate data within tables.

**Why It Matters**: Core operations for working with data.

**Commands**: SELECT, INSERT, UPDATE, DELETE

---

### DISTINCT
**Definition**: Keyword that removes duplicate rows from query results.

**Why It Matters**: Shows only unique values.

**Example**:
```sql
SELECT DISTINCT country FROM customers;
```

---

## E

### Entity
**Definition**: A real-world object or concept represented by a table.

**Why It Matters**: Foundation of database design.

**Example**: Customer, Product, Order are entities

---

### EXISTS
**Definition**: Operator that tests for the existence of rows in a subquery.

**Why It Matters**: More efficient than IN for correlated subqueries.

**Example**:
```sql
SELECT product_name FROM products p
WHERE EXISTS (
    SELECT 1 FROM order_items oi
    WHERE oi.product_id = p.product_id
);
```

---

### EXPLAIN
**Definition**: Command that shows how SQLite will execute a query.

**Why It Matters**: Essential for query optimization.

**Example**:
```sql
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price > 100;
```

---

## F

### Foreign Key
**Definition**: A column (or columns) that references the primary key of another table.

**Why It Matters**: Maintains referential integrity between related tables.

**Example**:
```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

---

### Full Table Scan
**Definition**: Reading every row in a table to find matching records.

**Why It Matters**: Slow operation that can be improved with indexes.

---

## G

### GROUP BY
**Definition**: Clause that groups rows with the same values into summary rows.

**Why It Matters**: Essential for aggregating data by category.

**Example**:
```sql
SELECT category, COUNT(*) AS count
FROM products
GROUP BY category;
```

---

## H

### HAVING
**Definition**: Clause that filters grouped results (like WHERE for groups).

**Why It Matters**: Allows filtering after aggregation.

**Example**:
```sql
SELECT category, COUNT(*) AS count
FROM products
GROUP BY category
HAVING COUNT(*) > 10;
```

---

## I

### IN
**Definition**: Operator that matches any value in a list.

**Why It Matters**: Cleaner than multiple OR conditions.

**Example**:
```sql
SELECT * FROM products
WHERE category_id IN (1, 3, 5);
```

---

### Index
**Definition**: A database structure that speeds up data retrieval.

**Why It Matters**: Dramatically improves query performance on large tables.

**Example**:
```sql
CREATE INDEX idx_price ON products(price);
```

**Trade-off**: Faster queries but slower INSERT/UPDATE/DELETE

---

### INNER JOIN
**Definition**: Returns rows when there's a match in both tables.

**Why It Matters**: Most common join type.

**Example**:
```sql
SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id;
```

---

### INSERT
**Definition**: SQL command to add new rows to a table.

**Why It Matters**: Primary way to add data.

**Example**:
```sql
INSERT INTO customers (first_name, last_name, email)
VALUES ('John', 'Doe', 'john@example.com');
```

---

## J

### JOIN
**Definition**: Combines rows from two or more tables based on a related column.

**Why It Matters**: Core feature of relational databases.

**Types**: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN

---

## K

### Key
**Definition**: A column or set of columns used to identify rows.

**Types**:
- **Primary Key**: Unique identifier for rows
- **Foreign Key**: References another table
- **Composite Key**: Multiple columns forming a key

---

## L

### LEFT JOIN
**Definition**: Returns all rows from the left table and matching rows from the right table.

**Why It Matters**: Shows all records from one table, even without matches.

**Example**:
```sql
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

---

### LIKE
**Definition**: Operator for pattern matching with wildcards.

**Why It Matters**: Enables flexible text searching.

**Example**:
```sql
SELECT * FROM customers
WHERE email LIKE '%@gmail.com';
```

**Wildcards**:
- `%` - any characters
- `_` - single character

---

### LIMIT
**Definition**: Restricts the number of rows returned.

**Why It Matters**: Controls result set size and enables pagination.

**Example**:
```sql
SELECT * FROM products
ORDER BY price DESC
LIMIT 10;
```

---

## N

### Normalization
**Definition**: Process of organizing data to reduce redundancy.

**Why It Matters**: Improves data integrity and reduces storage.

**Forms**:
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies
- **3NF**: 2NF + no transitive dependencies

---

### NOT NULL
**Definition**: Constraint that prevents NULL values in a column.

**Why It Matters**: Ensures required data is always present.

**Example**:
```sql
CREATE TABLE users (
    email TEXT NOT NULL
);
```

---

### NULL
**Definition**: Special value representing missing or unknown data.

**Why It Matters**: Different from empty string or zero - requires special handling.

**Example**:
```sql
SELECT * FROM products
WHERE description IS NULL;
```

**Important**: Use `IS NULL` and `IS NOT NULL`, not `= NULL`

---

## O

### OFFSET
**Definition**: Skips a specified number of rows before returning results.

**Why It Matters**: Enables pagination.

**Example**:
```sql
-- Get rows 11-20
SELECT * FROM products
LIMIT 10 OFFSET 10;
```

---

### OR
**Definition**: Logical operator where at least one condition must be true.

**Why It Matters**: Allows flexible filtering.

**Example**:
```sql
SELECT * FROM products
WHERE category = 'Books' OR category = 'Electronics';
```

---

### ORDER BY
**Definition**: Sorts query results by one or more columns.

**Why It Matters**: Controls result ordering.

**Example**:
```sql
SELECT * FROM products
ORDER BY price DESC, product_name ASC;
```

**Options**: ASC (ascending, default), DESC (descending)

---

## P

### PARTITION BY
**Definition**: Divides rows into groups for window function calculations.

**Why It Matters**: Enables group-wise calculations without GROUP BY.

**Example**:
```sql
SELECT
    product_name,
    category_id,
    price,
    RANK() OVER (PARTITION BY category_id ORDER BY price DESC) AS rank
FROM products;
```

---

### Primary Key
**Definition**: Column(s) that uniquely identifies each row in a table.

**Why It Matters**: Ensures every row can be uniquely identified.

**Properties**: Must be unique, cannot be NULL, one per table

**Example**:
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE
);
```

---

## Q

### Query
**Definition**: A request for data from a database.

**Why It Matters**: Fundamental way to retrieve and manipulate data.

---

### Query Execution Plan
**Definition**: Step-by-step process of how database executes a query.

**Why It Matters**: Shows if indexes are used and helps optimize performance.

**View with**: `EXPLAIN QUERY PLAN`

---

## R

### RANK()
**Definition**: Window function that assigns ranks with gaps for ties.

**Why It Matters**: Creates rankings where tied values skip subsequent ranks.

**Example**:
```sql
SELECT
    product_name,
    price,
    RANK() OVER (ORDER BY price DESC) AS rank
FROM products;
```

**Difference from DENSE_RANK**: Creates gaps (1, 2, 2, 4 vs 1, 2, 2, 3)

---

### Referential Integrity
**Definition**: Ensures relationships between tables remain consistent.

**Why It Matters**: Prevents orphaned records.

**Enforced by**: Foreign keys

---

### Row
**Definition**: A single record in a table (horizontal).

**Why It Matters**: Represents one instance of an entity.

**Example**: One row in `customers` = one customer

---

### ROW_NUMBER()
**Definition**: Window function that assigns a unique sequential number to rows.

**Why It Matters**: Useful for pagination and removing duplicates.

**Example**:
```sql
SELECT
    product_name,
    ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products;
```

---

## S

### Schema
**Definition**: The structure of a database - tables, columns, data types, relationships.

**Why It Matters**: Blueprint for how data is organized.

---

### SELECT
**Definition**: SQL command to retrieve data from tables.

**Why It Matters**: Most commonly used SQL command.

**Example**:
```sql
SELECT column1, column2 FROM table_name WHERE condition;
```

---

### Self-Join
**Definition**: A table joined with itself.

**Why It Matters**: Enables comparing rows within the same table.

**Example**:
```sql
SELECT
    e1.name AS employee,
    e2.name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

---

### Subquery
**Definition**: A query nested inside another query.

**Why It Matters**: Enables complex multi-step operations.

**Example**:
```sql
SELECT product_name FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

---

## T

### Table
**Definition**: A collection of related data organized in rows and columns.

**Why It Matters**: Fundamental structure for storing data.

---

### Transaction
**Definition**: A sequence of operations treated as a single unit of work.

**Why It Matters**: Ensures data consistency (all succeed or all fail).

**Example**:
```sql
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

## U

### UNION
**Definition**: Combines results from multiple SELECT statements (removes duplicates).

**Why It Matters**: Merges data from different sources.

**Example**:
```sql
SELECT name FROM customers
UNION
SELECT name FROM suppliers;
```

**UNION vs UNION ALL**: UNION removes duplicates, UNION ALL keeps them (faster)

---

### UNIQUE
**Definition**: Constraint ensuring all values in a column are different.

**Why It Matters**: Prevents duplicate values.

**Example**:
```sql
CREATE TABLE users (
    email TEXT UNIQUE
);
```

---

### UPDATE
**Definition**: SQL command to modify existing rows.

**Why It Matters**: Changes data without re-inserting.

**Example**:
```sql
UPDATE products
SET price = price * 1.1
WHERE category = 'Electronics';
```

---

## W

### WHERE
**Definition**: Clause that filters rows based on conditions.

**Why It Matters**: Essential for querying specific data.

**Example**:
```sql
SELECT * FROM products
WHERE price > 50 AND stock_quantity > 0;
```

---

### Window Function
**Definition**: Function that performs calculations across rows related to the current row.

**Why It Matters**: Enables advanced analytics without grouping.

**Common functions**: ROW_NUMBER(), RANK(), DENSE_RANK(), SUM() OVER(), AVG() OVER()

**Example**:
```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

---

### WITH
**Definition**: Keyword that defines a Common Table Expression (CTE).

**Why It Matters**: Makes complex queries readable.

**Example**:
```sql
WITH high_value_customers AS (
    SELECT customer_id, SUM(total_amount) AS total
    FROM orders
    GROUP BY customer_id
    HAVING total > 1000
)
SELECT * FROM high_value_customers;
```

---

## Need More Help?

- **Cheat Sheet**: See `SQL_CHEAT_SHEET.md` for syntax reference
- **FAQ**: Check `FAQ.md` for common questions
- **Notebooks**: Review course modules for detailed explanations

---

**Happy Learning!**
