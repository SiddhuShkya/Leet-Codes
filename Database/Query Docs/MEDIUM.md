## Database | Medium 

This readme file contains solved SQL problems from LeetCode,from the Medium category.

Each problem includes:

- ✅ Table Schema
- ✅ Problem Description
- ✅ Input example
- ✅ Correct SQL solution
- ✅ Output example
- ✅ SQL Keywords Used

---

### <div align="center">Consecutive Numbers</div>

> Table 

```text
Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
```

> Problem 

In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
Find all numbers that appear at least three times consecutively.
Return the result table in any order.

> Input Example

```text
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
```

> SQL Query **Solution**

```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM logs l1
JOIN logs l2 ON l1.id = l2.id - 1
JOIN logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num AND l2.num = l3.num;
```

> Output Example

```text
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, JOIN, ON, AS, DISTINCT, AND

---


### <div align="center">Customers Who Bought All Products</div>

> Table 

```text
Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
 
Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
```

> Problem 

This table may contain duplicates rows. 
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.
product_key is the primary key (column with unique values) for this table.
Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.
Return the result table in any order.

> Input Example

```text
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
```

> SQL Query **Solution**

```sql
SELECT customer_id 
FROM (
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) AS num_products_bought,
        (SELECT COUNT(*) FROM Product) AS total_products
    FROM Customer
    GROUP BY customer_id
)t
WHERE num_products_bought = total_products;
```

> Output Example

```text
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, GROUP BY, AS, DISTINCT, COUNT

---


### <div align="center">Department Highest Salary</div>

> Table 

```text
Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
 
Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
```

> Problem 

id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.

> Input Example

```text
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
```

> SQL Query **Solution**

```sql
SELECT Department.name AS Department, Employee.name as Employee, salary FROM Employee
JOIN Department ON Employee.departmentId = Department.Id
WHERE (departmentId, salary) IN
(SELECT departmentId, MAX(salary) 
FROM Employee
GROUP BY departmentId);
```

> Output Example

```text
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, JOIN, ON, GROUP BY, AS, IN, MAX

---


### <div align="center">Friend Requests II: Who Has the Most Friends</div>

> Table 

```text
Table: RequestAccepted
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
```

> Problem 

(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
Write a solution to find the people who have the most friends and the most friends number.
The test cases are generated so that only one person has the most friends.

> Input Example

```text
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
```

> SQL Query **Solution**

```sql
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```

> Output Example

```text
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
```

> `SQL Keywords Used:` SELECT, FROM, GROUP BY, ORDER BY, LIMIT, UNION, ALL, AS, ALL, COUNT

---


### <div align="center">Investments In 2016</div>

> Table 

```text
Table: Insurance
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
```

> Problem 

pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholder's policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.
Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.

> Input Example

```text
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
```

> SQL Query **Solution**

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
```

> Output Example

```text
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, GROUP BY, HAVING, AS, AND, IN, COUNT, SUM, ROUND

---


### <div align="center">Managers with at Least 5 Direct Reports</div>

> Table 

```text
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
```

> Problem 

id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
Write a solution to find managers with at least five direct reports.
Return the result table in any order.

> Input Example

```text
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
```

> SQL Query **Solution**

```sql
SELECT name
FROM (
    SELECT name, COUNT(*)
    FROM (
        SELECT e1.name, e2.managerId
        FROM employee e1
        RIGHT JOIN employee e2
        ON e1.id = e2.managerId
        WHERE e1.id IS NOT NULL
    ) t
    GROUP BY name, managerId
    HAVING COUNT(*) >= 5
) t1;
```

> Output Example

```text
+------+
| name |
+------+
| John |
+------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, JOIN, RIGHT JOIN, ON, GROUP BY, HAVING, IS NOT NULL, COUNT

---


### <div align="center">Nth Highest Salary</div>

> Table 

```text
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
```

> Problem 

id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

> Input Example

```text
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
```

> SQL Query **Solution**

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE offset_val INT;
    SET offset_val = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET offset_val
    );
END
```

> Output Example

```text
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```

> `SQL Keywords Used:` SELECT, FROM, ORDER BY, LIMIT, DISTINCT, END

---


### <div align="center">Product Price at a Given Date</div>

> Table 

```text
Table: Products
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
```

> Problem 

(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
Initially, all products have price 10.
Write a solution to find the prices of all products on the date 2019-08-16.
Return the result table in any order.

> Input Example

```text
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
```

> SQL Query **Solution**

```sql
SELECT product_id, new_price AS price
FROM products
WHERE change_date <= '2019-08-16'
  AND (product_id, change_date) IN (
        SELECT product_id, MAX(change_date)
        FROM products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
  )
UNION ALL
SELECT DISTINCT product_id, 10 AS price
FROM products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id
    FROM products
    WHERE change_date <= '2019-08-16'
);
```

> Output Example

```text
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, GROUP BY, UNION, ALL, AS, DISTINCT, AND, IN, ALL, MAX

---


### <div align="center">Rank Scores</div>

> Table 

```text
Table: Scores
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
```

> Problem 

id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

> Input Example

```text
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```

> SQL Query **Solution**

```sql
SELECT s1.Score, (SELECT COUNT(DISTINCT Score) FROM Scores s2 WHERE s2.Score >= s1.Score) AS 'Rank'
FROM Scores s1
ORDER BY s1.Score Desc
```

> Output Example

```text
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

> `SQL Keywords Used:` SELECT, FROM, WHERE, ORDER BY, AS, DISTINCT, COUNT

---


### <div align="center">Second Highest Salary</div>

> Table 

```text
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
```

> Problem 

id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

> Input Example

```text
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
```

> SQL Query **Solution**

```sql
SELECT (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

> Output Example

```text
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```

> `SQL Keywords Used:` SELECT, FROM, ORDER BY, LIMIT, AS, DISTINCT

---
