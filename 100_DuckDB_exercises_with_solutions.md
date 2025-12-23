


# 100+ DuckDB exercises

This is a collection of DuckDB exercises covering SQL fundamentals, advanced queries, window functions,
DuckDB-specific features, and file operations. The goal of this collection is to offer a quick reference
for both old and new users but also to provide a set of exercises for those who teach.

If you find an error or think you've a better way to solve some of them, feel
free to open an issue at <https://github.com/pranamg/duckdb-100>.
File automatically generated. See the documentation to update questions/answers/hints programmatically.

#### 1. Import DuckDB and check the version (★☆☆)


```sql
import duckdb
print(duckdb.__version__)
```
#### 2. Create an in-memory DuckDB connection and run a simple SELECT (★☆☆)


```sql
import duckdb
con = duckdb.connect()
result = con.sql("SELECT 'Hello, DuckDB!' AS greeting")
print(result)
```
#### 3. Generate a sequence of numbers from 1 to 10 using DuckDB (★☆☆)


```sql
SELECT * FROM generate_series(1, 10);

-- Alternative using range()
SELECT * FROM range(1, 11);
```
#### 4. Select specific columns from a generated sequence (★☆☆)


```sql
SELECT generate_series AS num, generate_series * 2 AS doubled
FROM generate_series(1, 5);
```
#### 5. Use SELECT with literal values to create a simple result set (★☆☆)


```sql
SELECT 1 AS id, 'Alice' AS name, 30 AS age
UNION ALL
SELECT 2, 'Bob', 25
UNION ALL
SELECT 3, 'Charlie', 35;

-- Alternative using VALUES
SELECT * FROM (VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)) AS t(id, name, age);
```
#### 6. Create a table from a VALUES clause and query it (★☆☆)


```sql
CREATE TABLE employees AS 
SELECT * FROM (VALUES 
    (1, 'Alice', 'Engineering', 75000),
    (2, 'Bob', 'Sales', 65000),
    (3, 'Charlie', 'Engineering', 80000),
    (4, 'Diana', 'HR', 60000),
    (5, 'Eve', 'Sales', 70000)
) AS t(id, name, department, salary);

SELECT * FROM employees;
```
#### 7. Sort results by a column in descending order (★☆☆)


```sql
SELECT * FROM employees ORDER BY salary DESC;
```
#### 8. Limit the result set to the first 3 rows (★☆☆)


```sql
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;
```
#### 9. Skip the first 2 rows and return the next 3 (★☆☆)


```sql
SELECT * FROM employees ORDER BY id LIMIT 3 OFFSET 2;
```
#### 10. Select distinct values from a column (★☆☆)


```sql
SELECT DISTINCT department FROM employees;
```
#### 11. Count the total number of rows in a table (★☆☆)


```sql
SELECT COUNT(*) AS total_employees FROM employees;
```
#### 12. Use column aliases to rename output columns (★☆☆)


```sql
SELECT 
    name AS employee_name, 
    salary AS annual_salary,
    salary / 12 AS monthly_salary
FROM employees;
```
#### 13. Combine two columns into one with string concatenation (★☆☆)


```sql
SELECT name || ' - ' || department AS employee_info FROM employees;

-- Alternative using concat()
SELECT concat(name, ' works in ', department) AS description FROM employees;
```
#### 14. Use CASE expression to categorize salary levels (★☆☆)


```sql
SELECT 
    name,
    salary,
    CASE 
        WHEN salary >= 75000 THEN 'High'
        WHEN salary >= 65000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees;
```
#### 15. Use COALESCE to handle NULL values (★☆☆)


```sql
SELECT 
    name,
    COALESCE(department, 'Unassigned') AS department
FROM (VALUES ('Frank', NULL), ('Grace', 'IT')) AS t(name, department);
```
#### 16. Filter rows where salary is greater than 65000 (★☆☆)


```sql
SELECT * FROM employees WHERE salary > 65000;
```
#### 17. Filter rows using multiple conditions with AND (★☆☆)


```sql
SELECT * FROM employees 
WHERE department = 'Engineering' AND salary > 70000;
```
#### 18. Filter rows using OR for alternative conditions (★☆☆)


```sql
SELECT * FROM employees 
WHERE department = 'Sales' OR department = 'HR';
```
#### 19. Use IN clause to match multiple values (★☆☆)


```sql
SELECT * FROM employees 
WHERE department IN ('Engineering', 'Sales');
```
#### 20. Use BETWEEN to filter a range of values (★☆☆)


```sql
SELECT * FROM employees 
WHERE salary BETWEEN 65000 AND 75000;
```
#### 21. Use LIKE for pattern matching with wildcards (★☆☆)


```sql
SELECT * FROM employees WHERE name LIKE 'A%';

-- Names containing 'i'
SELECT * FROM employees WHERE name LIKE '%i%';

-- Names with exactly 3 characters
SELECT * FROM employees WHERE name LIKE '___';
```
#### 22. Use ILIKE for case-insensitive pattern matching (★☆☆)


```sql
SELECT * FROM employees WHERE name ILIKE 'a%';
```
#### 23. Filter rows where a value is NOT in a list (★☆☆)


```sql
SELECT * FROM employees 
WHERE department NOT IN ('HR', 'Sales');
```
#### 24. Use IS NULL and IS NOT NULL to filter null values (★☆☆)


```sql
-- Create sample with NULLs
SELECT * FROM (VALUES 
    (1, 'Alice', 100),
    (2, 'Bob', NULL),
    (3, 'Charlie', 150)
) AS t(id, name, bonus)
WHERE bonus IS NOT NULL;
```
#### 25. Use regular expression matching with SIMILAR TO (★☆☆)


```sql
-- Names starting with A or B
SELECT * FROM employees WHERE name SIMILAR TO '(A|B)%';

-- Alternative using regexp_matches
SELECT * FROM employees WHERE regexp_matches(name, '^[AB]');
```
#### 26. Calculate the sum of all salaries (★☆☆)


```sql
SELECT SUM(salary) AS total_salary FROM employees;
```
#### 27. Calculate the average salary (★☆☆)


```sql
SELECT AVG(salary) AS average_salary FROM employees;
```
#### 28. Find the minimum and maximum salaries (★☆☆)


```sql
SELECT 
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;
```
#### 29. Count employees per department using GROUP BY (★☆☆)


```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```
#### 30. Calculate total and average salary per department (★☆☆)


```sql
SELECT 
    department,
    COUNT(*) AS num_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```
#### 31. Filter grouped results using HAVING (★☆☆)


```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 67000;
```
#### 32. Use GROUP BY with ORDER BY on aggregated column (★☆☆)


```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;
```
#### 33. Calculate multiple statistics in one query (★☆☆)


```sql
SELECT 
    COUNT(*) AS count,
    SUM(salary) AS sum,
    AVG(salary) AS avg,
    MIN(salary) AS min,
    MAX(salary) AS max,
    STDDEV(salary) AS stddev
FROM employees;
```
#### 34. Use FILTER clause with aggregates (DuckDB feature) (★☆☆)


```sql
SELECT 
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE department = 'Engineering') AS engineering_count,
    AVG(salary) FILTER (WHERE department = 'Sales') AS sales_avg_salary
FROM employees;
```
#### 35. Calculate running statistics with GROUP BY ALL (★☆☆)


```sql
SELECT department, name, AVG(salary) AS avg_salary
FROM employees
GROUP BY ALL;
```
#### 36. Use string aggregation with STRING_AGG or LIST (★☆☆)


```sql
SELECT 
    department,
    STRING_AGG(name, ', ' ORDER BY name) AS employee_names
FROM employees
GROUP BY department;

-- Alternative using LIST
SELECT 
    department,
    LIST(name ORDER BY name) AS employee_list
FROM employees
GROUP BY department;
```
#### 37. Calculate percentile values (★☆☆)


```sql
SELECT 
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary,
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1_salary,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3_salary
FROM employees;
```
#### 38. Create two tables and perform an INNER JOIN (★★☆)


```sql
CREATE TABLE departments AS 
SELECT * FROM (VALUES 
    ('Engineering', 'Building A'),
    ('Sales', 'Building B'),
    ('HR', 'Building C'),
    ('Marketing', 'Building D')
) AS t(name, location);

SELECT e.name, e.salary, d.location
FROM employees e
INNER JOIN departments d ON e.department = d.name;
```
#### 39. Perform a LEFT JOIN to include unmatched rows (★★☆)


```sql
-- Add an employee with department not in departments table
INSERT INTO employees VALUES (6, 'Frank', 'IT', 72000);

SELECT e.name, e.department, d.location
FROM employees e
LEFT JOIN departments d ON e.department = d.name;
```
#### 40. Perform a RIGHT JOIN (★★☆)


```sql
SELECT e.name, d.name AS dept_name, d.location
FROM employees e
RIGHT JOIN departments d ON e.department = d.name;
```
#### 41. Perform a FULL OUTER JOIN (★★☆)


```sql
SELECT e.name, e.department, d.name AS dept_name, d.location
FROM employees e
FULL OUTER JOIN departments d ON e.department = d.name;
```
#### 42. Use CROSS JOIN to generate all combinations (★★☆)


```sql
SELECT a.x, b.y, a.x * b.y AS product
FROM (SELECT generate_series AS x FROM generate_series(1, 3)) a
CROSS JOIN (SELECT generate_series AS y FROM generate_series(1, 3)) b;
```
#### 43. Perform a self-join to compare rows within the same table (★★☆)


```sql
-- Find employees who earn more than others in the same department
SELECT 
    e1.name AS employee, 
    e2.name AS earns_less_than,
    e1.department
FROM employees e1
JOIN employees e2 ON e1.department = e2.department AND e1.salary > e2.salary;
```
#### 44. Join multiple tables in a single query (★★☆)


```sql
CREATE TABLE projects AS 
SELECT * FROM (VALUES 
    (1, 'Project Alpha', 'Engineering'),
    (2, 'Project Beta', 'Sales'),
    (3, 'Project Gamma', 'Engineering')
) AS t(id, name, department);

SELECT e.name AS employee, p.name AS project, d.location
FROM employees e
JOIN departments d ON e.department = d.name
JOIN projects p ON e.department = p.department;
```
#### 45. Use USING clause for joins on same-named columns (★★☆)


```sql
-- Rename department column for demonstration
SELECT e.name, e.salary, d.location
FROM employees e
JOIN (SELECT name AS department, location FROM departments) d 
USING (department);
```
#### 46. Perform a NATURAL JOIN (★★☆)


```sql
CREATE TABLE emp_dept AS 
SELECT id, name AS emp_name, department AS dept_name, salary FROM employees;

CREATE TABLE dept_info AS 
SELECT name AS dept_name, location FROM departments;

SELECT * FROM emp_dept NATURAL JOIN dept_info;
```
#### 47. Use anti-join pattern to find non-matching rows (★★☆)


```sql
-- Find employees in departments without a location
SELECT e.name, e.department
FROM employees e
LEFT JOIN departments d ON e.department = d.name
WHERE d.name IS NULL;
```
#### 48. Use semi-join pattern with EXISTS (★★☆)


```sql
-- Find employees who work on projects
SELECT e.name, e.department
FROM employees e
WHERE EXISTS (
    SELECT 1 FROM projects p WHERE p.department = e.department
);
```
#### 49. Combine results with UNION (★★☆)


```sql
SELECT name, 'employee' AS type FROM employees
UNION
SELECT name, 'department' AS type FROM departments;

-- UNION ALL keeps duplicates
SELECT department FROM employees
UNION ALL
SELECT name FROM departments;
```
#### 50. Use INTERSECT to find common values (★★☆)


```sql
SELECT department FROM employees
INTERSECT
SELECT name FROM departments;
```
#### 51. Use EXCEPT to find differences between sets (★★☆)


```sql
-- Departments with no employees
SELECT name FROM departments
EXCEPT
SELECT department FROM employees;
```
#### 52. Write a simple subquery in the WHERE clause (★★☆)


```sql
-- Find employees with above-average salary
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
#### 53. Use a subquery in the FROM clause (derived table) (★★☆)


```sql
SELECT dept_stats.department, dept_stats.avg_salary
FROM (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE dept_stats.avg_salary > 67000;
```
#### 54. Use a correlated subquery (★★☆)


```sql
-- Find employees who earn more than their department average
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary) 
    FROM employees e2 
    WHERE e2.department = e1.department
);
```
#### 55. Use subquery with IN clause (★★☆)


```sql
-- Find employees in departments that have projects
SELECT * FROM employees
WHERE department IN (SELECT department FROM projects);
```
#### 56. Use subquery with ANY/ALL (★★☆)


```sql
-- Salary greater than any Sales employee
SELECT * FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales');

-- Salary greater than all Sales employees
SELECT * FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE department = 'Sales');
```
#### 57. Write a Common Table Expression (CTE) (★★☆)


```sql
WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT e.name, e.salary, d.avg_salary
FROM employees e
JOIN dept_avg d ON e.department = d.department
WHERE e.salary > d.avg_salary;
```
#### 58. Use multiple CTEs in a single query (★★☆)


```sql
WITH 
dept_stats AS (
    SELECT department, AVG(salary) AS avg_sal, COUNT(*) AS cnt
    FROM employees GROUP BY department
),
high_avg_depts AS (
    SELECT department FROM dept_stats WHERE avg_sal > 67000
)
SELECT e.* FROM employees e
WHERE e.department IN (SELECT department FROM high_avg_depts);
```
#### 59. Use a CTE that references another CTE (★★☆)


```sql
WITH 
all_salaries AS (
    SELECT salary FROM employees
),
salary_stats AS (
    SELECT 
        AVG(salary) AS avg_sal,
        STDDEV(salary) AS std_sal
    FROM all_salaries
)
SELECT e.name, e.salary,
    (e.salary - s.avg_sal) / s.std_sal AS z_score
FROM employees e, salary_stats s;
```
#### 60. Use scalar subquery in SELECT (★★☆)


```sql
SELECT 
    name,
    salary,
    (SELECT AVG(salary) FROM employees) AS company_avg,
    salary - (SELECT AVG(salary) FROM employees) AS diff_from_avg
FROM employees;
```
#### 61. Use LATERAL join for row-by-row subquery evaluation (★★☆)


```sql
SELECT e.name, e.department, top_earner.max_salary
FROM employees e,
LATERAL (
    SELECT MAX(salary) AS max_salary 
    FROM employees e2 
    WHERE e2.department = e.department
) AS top_earner;
```
#### 62. Add row numbers to results using ROW_NUMBER() (★★☆)


```sql
SELECT 
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank,
    name,
    salary
FROM employees;
```
#### 63. Partition row numbers by a column (★★☆)


```sql
SELECT 
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    name,
    department,
    salary
FROM employees;
```
#### 64. Use RANK() and DENSE_RANK() for ranking with ties (★★☆)


```sql
SELECT 
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```
#### 65. Calculate running totals with SUM() window function (★★☆)


```sql
SELECT 
    name,
    salary,
    SUM(salary) OVER (ORDER BY id) AS running_total
FROM employees;
```
#### 66. Calculate moving average using window frame (★★☆)


```sql
SELECT 
    id,
    salary,
    AVG(salary) OVER (
        ORDER BY id 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_avg
FROM employees;
```
#### 67. Use LAG() to access previous row's value (★★☆)


```sql
SELECT 
    name,
    salary,
    LAG(salary, 1) OVER (ORDER BY id) AS prev_salary,
    salary - LAG(salary, 1, salary) OVER (ORDER BY id) AS salary_diff
FROM employees;
```
#### 68. Use LEAD() to access next row's value (★★☆)


```sql
SELECT 
    name,
    salary,
    LEAD(salary, 1) OVER (ORDER BY id) AS next_salary
FROM employees;
```
#### 69. Use FIRST_VALUE() and LAST_VALUE() (★★☆)


```sql
SELECT 
    name,
    department,
    salary,
    FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) AS highest_earner,
    LAST_VALUE(name) OVER (
        PARTITION BY department ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS lowest_earner
FROM employees;
```
#### 70. Use NTH_VALUE() to get a specific row's value (★★☆)


```sql
SELECT 
    name,
    department,
    salary,
    NTH_VALUE(name, 2) OVER (
        PARTITION BY department ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS second_highest_earner
FROM employees;
```
#### 71. Use NTILE() to divide rows into buckets (★★☆)


```sql
SELECT 
    name,
    salary,
    NTILE(3) OVER (ORDER BY salary) AS salary_tercile
FROM employees;
```
#### 72. Calculate cumulative distribution with CUME_DIST() (★★☆)


```sql
SELECT 
    name,
    salary,
    CUME_DIST() OVER (ORDER BY salary) AS cumulative_dist,
    PERCENT_RANK() OVER (ORDER BY salary) AS percent_rank
FROM employees;
```
#### 73. Use window function with FILTER clause (★★☆)


```sql
SELECT 
    name,
    department,
    salary,
    COUNT(*) FILTER (WHERE salary > 65000) OVER (PARTITION BY department) AS high_earners_in_dept
FROM employees;
```
#### 74. Calculate difference from partition average (★★☆)


```sql
SELECT 
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg,
    salary - AVG(salary) OVER (PARTITION BY department) AS diff_from_dept_avg
FROM employees;
```
#### 75. Use multiple window functions with named windows (★★☆)


```sql
SELECT 
    name,
    department,
    salary,
    ROW_NUMBER() OVER w AS row_num,
    SUM(salary) OVER w AS running_total,
    AVG(salary) OVER w AS running_avg
FROM employees
WINDOW w AS (PARTITION BY department ORDER BY salary);
```
#### 76. Filter window function results using QUALIFY (★★☆)


```sql
-- Get only the highest paid employee per department
SELECT 
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
FROM employees
QUALIFY rn = 1;
```
#### 77. Create and query a LIST column (★★☆)


```sql
SELECT 
    [1, 2, 3, 4, 5] AS my_list,
    LIST_VALUE(10, 20, 30) AS another_list;

-- Access elements (1-indexed)
SELECT 
    [1, 2, 3, 4, 5][1] AS first,
    [1, 2, 3, 4, 5][-1] AS last;
```
#### 78. Use LIST functions for manipulation (★★☆)


```sql
SELECT 
    list_append([1, 2, 3], 4) AS appended,
    list_concat([1, 2], [3, 4]) AS concatenated,
    list_contains([1, 2, 3], 2) AS contains_2,
    list_distinct([1, 2, 2, 3, 3, 3]) AS distinct_list,
    list_sort([3, 1, 4, 1, 5]) AS sorted;
```
#### 79. Use list_transform to apply function to each element (★★☆)


```sql
SELECT 
    list_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled,
    list_transform(['hello', 'world'], s -> upper(s)) AS uppercased;
```
#### 80. Use list_filter to select elements (★★☆)


```sql
SELECT 
    list_filter([1, 2, 3, 4, 5, 6], x -> x % 2 = 0) AS evens,
    list_filter([1, 2, 3, 4, 5], x -> x > 2) AS greater_than_2;
```
#### 81. Use list_reduce for aggregation (★★☆)


```sql
SELECT 
    list_reduce([1, 2, 3, 4, 5], (a, b) -> a + b) AS sum,
    list_reduce([1, 2, 3, 4, 5], (a, b) -> a * b) AS product;
```
#### 82. Flatten nested lists with flatten() (★★☆)


```sql
SELECT 
    flatten([[1, 2], [3, 4], [5]]) AS flattened,
    unnest([[1, 2], [3, 4]]) AS unnested;
```
#### 83. Create and query STRUCT columns (★★☆)


```sql
SELECT 
    {'name': 'Alice', 'age': 30, 'city': 'NYC'} AS person,
    STRUCT_PACK(x := 1, y := 2, z := 3) AS point;

-- Access fields
SELECT 
    {'name': 'Alice', 'age': 30}.name AS name,
    {'name': 'Alice', 'age': 30}['age'] AS age;
```
#### 84. Use STRUCT functions (★★☆)


```sql
WITH data AS (
    SELECT {'a': 1, 'b': 2, 'c': 3} AS s
)
SELECT 
    struct_extract(s, 'a') AS extract_a,
    struct_keys(s) AS keys,
    struct_values(s) AS values
FROM data;
```
#### 85. Create and use MAP type (★★☆)


```sql
SELECT 
    MAP {'a': 1, 'b': 2, 'c': 3} AS my_map,
    map_from_entries([('x', 10), ('y', 20)]) AS from_entries;

-- Access values
SELECT 
    MAP {'a': 1, 'b': 2}['a'] AS value_a,
    element_at(MAP {'a': 1, 'b': 2}, 'b') AS value_b;
```
#### 86. Use MAP functions (★★☆)


```sql
WITH data AS (
    SELECT MAP {'x': 1, 'y': 2, 'z': 3} AS m
)
SELECT 
    map_keys(m) AS keys,
    map_values(m) AS values,
    map_entries(m) AS entries,
    cardinality(m) AS size
FROM data;
```
#### 87. Use UNNEST to expand arrays/lists into rows (★★☆)


```sql
SELECT unnest([1, 2, 3, 4, 5]) AS num;

-- Unnest multiple arrays in parallel
SELECT 
    unnest(['a', 'b', 'c']) AS letter,
    unnest([1, 2, 3]) AS number;

-- Unnest with ordinality
SELECT * FROM unnest(['a', 'b', 'c']) WITH ORDINALITY AS t(val, idx);
```
#### 88. Create a table with nested types (★★☆)


```sql
CREATE TABLE orders AS 
SELECT * FROM (VALUES 
    (1, 'Alice', [{'product': 'laptop', 'qty': 1}, {'product': 'mouse', 'qty': 2}]),
    (2, 'Bob', [{'product': 'keyboard', 'qty': 1}]),
    (3, 'Charlie', [{'product': 'monitor', 'qty': 2}, {'product': 'cable', 'qty': 5}])
) AS t(order_id, customer, items);

SELECT order_id, customer, unnest(items) AS item FROM orders;
```
#### 89. Use UNION type for heterogeneous data (★★☆)


```sql
CREATE TABLE events (
    id INTEGER,
    data UNION(num INTEGER, str VARCHAR, flag BOOLEAN)
);

INSERT INTO events VALUES 
    (1, 42),
    (2, 'hello'),
    (3, true);

SELECT 
    id, 
    data,
    union_tag(data) AS type_tag
FROM events;
```
#### 90. Use ASOF JOIN for time-series data (★★★)


```sql
CREATE TABLE stock_prices AS 
SELECT * FROM (VALUES 
    ('2024-01-01 09:00:00'::TIMESTAMP, 100.0),
    ('2024-01-01 10:00:00'::TIMESTAMP, 101.5),
    ('2024-01-01 11:00:00'::TIMESTAMP, 99.0)
) AS t(ts, price);

CREATE TABLE trades AS 
SELECT * FROM (VALUES 
    ('2024-01-01 09:30:00'::TIMESTAMP, 10),
    ('2024-01-01 10:15:00'::TIMESTAMP, 20),
    ('2024-01-01 11:30:00'::TIMESTAMP, 15)
) AS t(ts, quantity);

SELECT t.ts AS trade_time, t.quantity, s.price AS price_at_trade
FROM trades t
ASOF JOIN stock_prices s ON t.ts >= s.ts;
```
#### 91. Use PIVOT to transform rows to columns (★★★)


```sql
CREATE TABLE sales AS 
SELECT * FROM (VALUES 
    ('Q1', 'ProductA', 100),
    ('Q1', 'ProductB', 150),
    ('Q2', 'ProductA', 120),
    ('Q2', 'ProductB', 180),
    ('Q3', 'ProductA', 110),
    ('Q3', 'ProductB', 200)
) AS t(quarter, product, amount);

PIVOT sales ON product USING SUM(amount);
```
#### 92. Use UNPIVOT to transform columns to rows (★★★)


```sql
CREATE TABLE quarterly_sales AS 
SELECT * FROM (VALUES 
    ('ProductA', 100, 120, 110),
    ('ProductB', 150, 180, 200)
) AS t(product, Q1, Q2, Q3);

UNPIVOT quarterly_sales ON Q1, Q2, Q3 INTO NAME quarter VALUE amount;
```
#### 93. Use QUALIFY to filter window function results (★★★)


```sql
-- Top 2 earners per department
SELECT name, department, salary
FROM employees
QUALIFY ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) <= 2;

-- Employees earning above their department median
SELECT name, department, salary
FROM employees
QUALIFY salary > PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) 
    OVER (PARTITION BY department);
```
#### 94. Use EXCLUDE and REPLACE in SELECT * (★★★)


```sql
-- Exclude specific columns
SELECT * EXCLUDE (id) FROM employees;

-- Replace column with expression
SELECT * REPLACE (salary * 1.1 AS salary) FROM employees;

-- Combine both
SELECT * EXCLUDE (id) REPLACE (upper(name) AS name) FROM employees;
```
#### 95. Use COLUMNS expression for dynamic column selection (★★★)


```sql
-- Sum all numeric columns
SELECT SUM(COLUMNS(* EXCLUDE (id, name, department))) FROM employees;

-- Apply function to columns matching pattern
SELECT COLUMNS('salary|id')::VARCHAR FROM employees;
```
#### 96. Use GROUPING SETS for multiple groupings (★★★)


```sql
SELECT 
    department,
    CASE WHEN GROUPING(department) = 1 THEN 'All Departments' ELSE department END AS dept_label,
    SUM(salary) AS total_salary,
    COUNT(*) AS count
FROM employees
GROUP BY GROUPING SETS ((department), ());
```
#### 97. Use ROLLUP for hierarchical aggregation (★★★)


```sql
CREATE TABLE sales_data AS 
SELECT * FROM (VALUES 
    (2023, 'Q1', 'ProductA', 100),
    (2023, 'Q1', 'ProductB', 150),
    (2023, 'Q2', 'ProductA', 120),
    (2024, 'Q1', 'ProductA', 200)
) AS t(year, quarter, product, amount);

SELECT year, quarter, SUM(amount) AS total
FROM sales_data
GROUP BY ROLLUP (year, quarter)
ORDER BY year NULLS LAST, quarter NULLS LAST;
```
#### 98. Use CUBE for all combination aggregations (★★★)


```sql
SELECT year, quarter, SUM(amount) AS total
FROM sales_data
GROUP BY CUBE (year, quarter)
ORDER BY year NULLS LAST, quarter NULLS LAST;
```
#### 99. Write a recursive CTE (★★★)


```sql
-- Generate Fibonacci sequence
WITH RECURSIVE fib(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b FROM fib WHERE n < 10
)
SELECT n, a AS fib_number FROM fib;

-- Hierarchical query (org chart)
CREATE TABLE org AS 
SELECT * FROM (VALUES 
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Dev Lead', 2),
    (5, 'Accountant', 3)
) AS t(id, title, manager_id);

WITH RECURSIVE hierarchy AS (
    SELECT id, title, manager_id, 0 AS level, title AS path
    FROM org WHERE manager_id IS NULL
    UNION ALL
    SELECT o.id, o.title, o.manager_id, h.level + 1, h.path || ' > ' || o.title
    FROM org o JOIN hierarchy h ON o.manager_id = h.id
)
SELECT * FROM hierarchy ORDER BY level, id;
```
#### 100. Read a CSV file with DuckDB (★★☆)


```sql
-- Auto-detect CSV format
SELECT * FROM read_csv_auto('data.csv');

-- With explicit options
SELECT * FROM read_csv('data.csv', 
    delim = ',',
    header = true,
    columns = {'id': 'INTEGER', 'name': 'VARCHAR', 'value': 'DOUBLE'}
);

-- Read from URL (requires httpfs extension)
-- INSTALL httpfs; LOAD httpfs;
-- SELECT * FROM read_csv_auto('https://example.com/data.csv');
```
#### 101. Write query results to a CSV file (★★☆)


```sql
-- Using COPY
COPY (SELECT * FROM employees) TO 'employees.csv' (HEADER, DELIMITER ',');

-- Using write_csv function (DuckDB 0.9+)
COPY (SELECT * FROM employees) TO 'employees.csv' WITH (FORMAT CSV, HEADER TRUE);
```
#### 102. Read and write Parquet files (★★☆)


```sql
-- Read Parquet file
SELECT * FROM read_parquet('data.parquet');

-- Read multiple Parquet files with glob
SELECT * FROM read_parquet('data/*.parquet');

-- Write to Parquet
COPY (SELECT * FROM employees) TO 'employees.parquet' (FORMAT PARQUET);

-- With compression
COPY (SELECT * FROM employees) TO 'employees.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
```
#### 103. Read JSON data (★★☆)


```sql
-- Read JSON file
SELECT * FROM read_json_auto('data.json');

-- Read JSON with explicit schema
SELECT * FROM read_json('data.json',
    columns = {'id': 'INTEGER', 'name': 'VARCHAR', 'tags': 'VARCHAR[]'}
);

-- Read newline-delimited JSON
SELECT * FROM read_ndjson_auto('data.ndjson');
```
#### 104. Query remote files using httpfs extension (★★☆)


```sql
-- Install and load httpfs
INSTALL httpfs;
LOAD httpfs;

-- Query CSV from URL
SELECT * FROM read_csv_auto('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv') LIMIT 10;

-- Query Parquet from S3 (with credentials)
-- SET s3_region='us-east-1';
-- SET s3_access_key_id='your_key';
-- SET s3_secret_access_key='your_secret';
-- SELECT * FROM read_parquet('s3://bucket/path/file.parquet');
```
#### 105. Use glob patterns to read multiple files (★★☆)


```sql
-- Read all CSV files in directory
SELECT * FROM read_csv_auto('data/*.csv');

-- Read all Parquet files recursively
SELECT * FROM read_parquet('data/**/*.parquet');

-- Add filename column
SELECT *, filename FROM read_csv_auto('data/*.csv', filename=true);
```
#### 106. Create a view over external files (★★☆)


```sql
-- Create view over CSV file
CREATE VIEW external_data AS 
SELECT * FROM read_csv_auto('data.csv');

-- Query the view
SELECT * FROM external_data WHERE id > 5;

-- Create view over Parquet with filter pushdown
CREATE VIEW parquet_data AS 
SELECT * FROM read_parquet('data.parquet');
```
#### 107. Export database or tables (★★☆)


```sql
-- Export entire database to directory
EXPORT DATABASE 'backup_dir';

-- Export specific table to Parquet
COPY employees TO 'employees_backup.parquet' (FORMAT PARQUET);

-- Import database
-- IMPORT DATABASE 'backup_dir';
```
#### 108. Use DuckDB with partitioned data (★★☆)


```sql
-- Read hive-partitioned data
SELECT * FROM read_parquet('data/*/*.parquet', hive_partitioning=true);

-- Write partitioned data
COPY (SELECT * FROM employees) 
TO 'output' (FORMAT PARQUET, PARTITION_BY (department));
```
#### 109. Insert data from external files (★★☆)


```sql
-- Insert from CSV
CREATE TABLE imported_data (id INTEGER, name VARCHAR, value DOUBLE);
INSERT INTO imported_data SELECT * FROM read_csv_auto('data.csv');

-- Insert from Parquet with transformation
INSERT INTO employees 
SELECT id, name, dept, salary * 1.05 
FROM read_parquet('new_employees.parquet');
```
#### 110. Write a simple macro (user-defined function) (★★★)


```sql
-- Simple expression macro
CREATE MACRO double(x) AS x * 2;
SELECT double(5);

-- Macro with multiple arguments
CREATE MACRO full_name(first, last) AS first || ' ' || last;
SELECT full_name('John', 'Doe');

-- Table macro
CREATE MACRO high_earners(min_salary) AS TABLE 
    SELECT * FROM employees WHERE salary > min_salary;
SELECT * FROM high_earners(70000);
```
#### 111. Use the json extension for JSON processing (★★★)


```sql
-- Extract JSON fields
SELECT 
    json_extract('{"name": "Alice", "age": 30}', '$.name') AS name_json,
    json_extract_string('{"name": "Alice", "age": 30}', '$.name') AS name_str,
    '{"name": "Alice", "age": 30}'::JSON ->> 'name' AS name_arrow;

-- Extract nested JSON
SELECT 
    json_extract('{"person": {"name": "Alice", "city": "NYC"}}', '$.person.name') AS nested_name;

-- JSON array handling
SELECT 
    json_extract('[1, 2, 3, 4, 5]', '$[0]') AS first,
    json_array_length('[1, 2, 3, 4, 5]') AS len;
```
#### 112. Use full-text search extension (★★★)


```sql
INSTALL fts;
LOAD fts;

-- Create table with text
CREATE TABLE documents AS 
SELECT * FROM (VALUES 
    (1, 'DuckDB is an in-process SQL OLAP database'),
    (2, 'Python is a popular programming language'),
    (3, 'SQL databases store structured data')
) AS t(id, content);

-- Create full-text search index
PRAGMA create_fts_index('documents', 'id', 'content');

-- Search using FTS
SELECT id, content, score
FROM (
    SELECT *, fts_main_documents.match_bm25(id, 'SQL database') AS score
    FROM documents
) sq
WHERE score IS NOT NULL
ORDER BY score DESC;
```
#### 113. Use window functions with complex frames (★★★)


```sql
-- Rows-based frame: specific number of rows
SELECT 
    id,
    salary,
    AVG(salary) OVER (ORDER BY id ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS avg_5_rows
FROM employees;

-- Range-based frame: value range
SELECT 
    id,
    salary,
    COUNT(*) OVER (ORDER BY salary RANGE BETWEEN 5000 PRECEDING AND 5000 FOLLOWING) AS similar_salary_count
FROM employees;

-- Exclude current row
SELECT 
    id,
    salary,
    AVG(salary) OVER (ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING EXCLUDE CURRENT ROW) AS avg_others
FROM employees;
```
#### 114. Use SAMPLE to randomly sample data (★★★)


```sql
-- Sample fixed number of rows
SELECT * FROM employees USING SAMPLE 3;

-- Sample percentage
SELECT * FROM employees USING SAMPLE 50%;

-- Reproducible sampling with seed
SELECT * FROM employees USING SAMPLE 50% (bernoulli, 42);

-- Reservoir sampling
SELECT * FROM generate_series(1, 1000) USING SAMPLE reservoir(10 ROWS);
```
#### 115. Use EXPLAIN and EXPLAIN ANALYZE (★★★)


```sql
-- Show query plan
EXPLAIN SELECT * FROM employees WHERE department = 'Engineering';

-- Show query plan with execution stats
EXPLAIN ANALYZE SELECT * FROM employees e
JOIN departments d ON e.department = d.name;

-- Analyze specific optimization
PRAGMA explain_output = 'all';
EXPLAIN SELECT * FROM employees WHERE salary > 70000;
```
#### 116. Create and use sequences (★★★)


```sql
-- Create sequence
CREATE SEQUENCE emp_id_seq START 100;

-- Use sequence
SELECT nextval('emp_id_seq') AS next_id;
SELECT nextval('emp_id_seq') AS next_id;

-- Use in INSERT
CREATE TABLE new_employees (
    id INTEGER DEFAULT nextval('emp_id_seq'),
    name VARCHAR
);
INSERT INTO new_employees (name) VALUES ('Grace');
SELECT * FROM new_employees;
```
#### 117. Use transactions for data integrity (★★★)


```sql
-- Start transaction
BEGIN TRANSACTION;

-- Make changes
UPDATE employees SET salary = salary * 1.1 WHERE department = 'Engineering';

-- Check results
SELECT * FROM employees WHERE department = 'Engineering';

-- Commit or rollback
COMMIT;
-- or ROLLBACK; to undo changes
```
#### 118. Use COPY with advanced options (★★★)


```sql
-- Copy with all options
COPY (
    SELECT * FROM employees WHERE salary > 60000
) TO 'high_earners.parquet' (
    FORMAT PARQUET,
    COMPRESSION ZSTD,
    ROW_GROUP_SIZE 100000
);

-- Copy to stdout as CSV
COPY (SELECT * FROM employees LIMIT 3) TO '/dev/stdout' WITH (FORMAT CSV, HEADER);

-- Copy with partitioning
COPY employees TO 'by_dept' (FORMAT PARQUET, PARTITION_BY department);
```
#### 119. Use prepared statements (★★★)


```sql
-- Prepare a statement
PREPARE emp_by_dept AS 
SELECT * FROM employees WHERE department = $1 AND salary > $2;

-- Execute with parameters
EXECUTE emp_by_dept('Engineering', 70000);
EXECUTE emp_by_dept('Sales', 60000);

-- Deallocate when done
DEALLOCATE emp_by_dept;
```
#### 120. Combine multiple advanced features in a complex query (★★★)


```sql
WITH 
-- Calculate department statistics
dept_stats AS (
    SELECT 
        department,
        AVG(salary) AS avg_salary,
        STDDEV(salary) AS std_salary,
        LIST(name ORDER BY salary DESC) AS employees_by_salary
    FROM employees
    GROUP BY department
),
-- Rank employees within departments
ranked_employees AS (
    SELECT 
        e.*,
        ds.avg_salary AS dept_avg,
        ds.employees_by_salary,
        ROW_NUMBER() OVER (PARTITION BY e.department ORDER BY e.salary DESC) AS dept_rank,
        PERCENT_RANK() OVER (ORDER BY e.salary) AS company_percentile
    FROM employees e
    JOIN dept_stats ds ON e.department = ds.department
)
SELECT 
    name,
    department,
    salary,
    dept_avg,
    ROUND(company_percentile * 100, 1) AS percentile,
    dept_rank,
    CASE 
        WHEN dept_rank = 1 THEN 'Top Earner'
        WHEN company_percentile > 0.75 THEN 'High Performer'
        ELSE 'Standard'
    END AS classification,
    employees_by_salary[1] AS dept_top_earner
FROM ranked_employees
QUALIFY dept_rank <= 2
ORDER BY department, dept_rank;
```