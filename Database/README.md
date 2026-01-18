## Database

A database is an organized collection of data stored electronically so it can be easily accessed, managed, and updated. This database stores information in a structured way, allowing computers and applications to save, retrieve, filter, and modify data efficiently.

In SQL terms, a database is a logical container that holds structured data organized into tables, and is managed using SQL (Structured Query Language) 🗄️📄.

A database is a collection of:

- Tables (rows + columns)
- Views
- Indexes
- Constraints
- Stored procedures & functions

All of these are accessed and controlled using SQL commands

--- 

### Core SQL concepts

1. `Database` -> Top-level container
2. `Table` -> Stores actual data in rows and columns
3. `Row (Record)` -> One entry in a table
4. `Column (Attribute)` -> Defines the type of data stored
5. `Primary Key` -> Uniquely identifies a row
6. `Foreign Key` -> Links to the primary key of another table
7. `Query` -> A request to retrieve or manipulate data

---

### How SQL sees a database

```text
Database
 ├── Table: students
 │    ├── Rows (records)
 │    └── Columns (fields)
 ├── Table: courses
 └── Views / Indexes
```

---

### Why SQL databases matter

- Data is normalized (less duplication)
- ACID properties ensure reliability
- Perfect for analytics, transactions, and data engineering

---

### What is an SQL Query

An SQL query is a command written in SQL (Structured Query Language) used to ask the database for information or to perform actions on data. Query helps to

- Retrieve data (SELECT)
- Insert new data (INSERT)
- Update existing data (UPDATE)
- Delete data (DELETE)
- Create or modify database structures (CREATE, ALTER, DROP)

---

### SQL Clauses

A SQL query is built using clauses, and each clause starts with one or more SQL keywords. 

- A keyword is a reserved word in SQL used to write queries. 
- A clause is a section of a SQL query that performs a specific task.

| Clause Category             | Keyword           | What it does                                              | Key points                                                                           | Clause Example                                                    |
| --------------------------- | ---------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Projection**              | `SELECT`         | Chooses which columns or expressions appear in the result | Can include columns, expressions, aliases, aggregates. Does not filter rows          | `SELECT name, salary * 12 AS annual_salary FROM Employee;` |
| **Source**                  | `FROM`           | Specifies where the data comes from                       | Tables, views, subqueries. Defines joins and join conditions                         | `FROM Employee e JOIN Department d ON e.dept_id = d.id;`   |
| **Filtering (Row-level)**   | `WHERE`          | Filters individual rows before grouping                   | Cannot use aggregate functions. Executes before `GROUP BY`                           | `WHERE salary > 50000;`                                    |
| **Grouping**                | `GROUP BY`       | Groups rows into sets so aggregates can be applied        | Required when mixing aggregates and non-aggregates. Creates one result row per group | `GROUP BY department;`                                     |
| **Filtering (Group-level)** | `HAVING`         | Filters groups after aggregation                          | Used with aggregate functions. Executes after `GROUP BY`                             | `HAVING COUNT(*) > 5;`                                     |
| **Sorting**                 | `ORDER BY`       | Sorts the final result set                                | Can sort by column name, alias, or position. Executed after `SELECT`                 | `ORDER BY salary DESC;`                                    |
| **Limiting / Pagination**   | `LIMIT / OFFSET` | Restricts number of rows returned                         | Used for pagination                                                                  | `LIMIT 10 OFFSET 20;`                                      |

---

### SQL Keywords & SQL Clauses

Here is the difference between SQL Keywords and SQL Clauses:

| **Concept**                      | **Definition**                                           | **Example**                                                            | **Notes**                         |
| -------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------- |
| **SQL Keyword**                  | A reserved word in SQL used to write queries             | `SELECT`, `FROM`, `WHERE`, `JOIN`                                      | Keywords are parts of clauses     |
| **SQL Clause**                   | A part of an SQL statement that performs a specific role | `SELECT name FROM Employee`                                            | Each clause starts with a keyword |
| **Keyword that is not a clause** | A keyword used inside a clause but not a clause itself   | `INNER`, `ASC`, `DESC`, `ON`                                           | Used to modify or define behavior |
| **Clause example**               | A full clause using a keyword                            | `WHERE salary > 50000`                                                 | Filters rows                      |
| **Query example**                | Full SQL statement using multiple clauses                | `SELECT name FROM Employee WHERE salary > 50000 ORDER BY salary DESC;` | Combines clauses                  |

Quick Example:

```sql
SELECT name, salary           -- SELECT clause (keyword: SELECT)
FROM Employee                 -- FROM clause (keyword: FROM)
WHERE salary > 50000          -- WHERE clause (keyword: WHERE)
ORDER BY salary DESC;         -- ORDER BY clause (keywords: ORDER BY, DESC)
```

> In the above example, we have 4 Clauses and 5 keywords.

---

### 📌 Important Note

-> **Clauses ≤ Keywords** 

✅ Because:
- Clauses start with keywords
- But some keywords do not start a new clause

--- 
