


# 100+ DuckDB exercises

This is a collection of DuckDB exercises covering SQL fundamentals, advanced queries, window functions,
DuckDB-specific features, and file operations. The goal of this collection is to offer a quick reference
for both old and new users but also to provide a set of exercises for those who teach.

If you find an error or think you've a better way to solve some of them, feel
free to open an issue at <https://github.com/pranamg/duckdb-100>.
File automatically generated. See the documentation to update questions/answers/hints programmatically.

#### 1. Import DuckDB and check the version (★☆☆)
`hint: import duckdb, duckdb.__version__`
#### 2. Create an in-memory DuckDB connection and run a simple SELECT (★☆☆)
`hint: duckdb.connect(), .sql() or .execute()`
#### 3. Generate a sequence of numbers from 1 to 10 using DuckDB (★☆☆)
`hint: generate_series() or range()`
#### 4. Select specific columns from a generated sequence (★☆☆)
`hint: generate_series with column alias`
#### 5. Use SELECT with literal values to create a simple result set (★☆☆)
`hint: SELECT without FROM, or VALUES clause`
#### 6. Create a table from a VALUES clause and query it (★☆☆)
`hint: CREATE TABLE ... AS SELECT ... FROM (VALUES ...)`
#### 7. Sort results by a column in descending order (★☆☆)
`hint: ORDER BY ... DESC`
#### 8. Limit the result set to the first 3 rows (★☆☆)
`hint: LIMIT`
#### 9. Skip the first 2 rows and return the next 3 (★☆☆)
`hint: LIMIT ... OFFSET`
#### 10. Select distinct values from a column (★☆☆)
`hint: SELECT DISTINCT`
#### 11. Count the total number of rows in a table (★☆☆)
`hint: COUNT(*)`
#### 12. Use column aliases to rename output columns (★☆☆)
`hint: AS keyword`
#### 13. Combine two columns into one with string concatenation (★☆☆)
`hint: || or concat()`
#### 14. Use CASE expression to categorize salary levels (★☆☆)
`hint: CASE WHEN ... THEN ... ELSE ... END`
#### 15. Use COALESCE to handle NULL values (★☆☆)
`hint: COALESCE(column, default_value)`
#### 16. Filter rows where salary is greater than 65000 (★☆☆)
`hint: WHERE clause with comparison operator`
#### 17. Filter rows using multiple conditions with AND (★☆☆)
`hint: WHERE ... AND ...`
#### 18. Filter rows using OR for alternative conditions (★☆☆)
`hint: WHERE ... OR ...`
#### 19. Use IN clause to match multiple values (★☆☆)
`hint: WHERE column IN (value1, value2, ...)`
#### 20. Use BETWEEN to filter a range of values (★☆☆)
`hint: WHERE column BETWEEN low AND high`
#### 21. Use LIKE for pattern matching with wildcards (★☆☆)
`hint: LIKE '%pattern%', _ for single char`
#### 22. Use ILIKE for case-insensitive pattern matching (★☆☆)
`hint: ILIKE (DuckDB-specific case-insensitive LIKE)`
#### 23. Filter rows where a value is NOT in a list (★☆☆)
`hint: NOT IN`
#### 24. Use IS NULL and IS NOT NULL to filter null values (★☆☆)
`hint: IS NULL, IS NOT NULL`
#### 25. Use regular expression matching with SIMILAR TO (★☆☆)
`hint: SIMILAR TO or regexp_matches()`
#### 26. Calculate the sum of all salaries (★☆☆)
`hint: SUM()`
#### 27. Calculate the average salary (★☆☆)
`hint: AVG()`
#### 28. Find the minimum and maximum salaries (★☆☆)
`hint: MIN(), MAX()`
#### 29. Count employees per department using GROUP BY (★☆☆)
`hint: GROUP BY, COUNT()`
#### 30. Calculate total and average salary per department (★☆☆)
`hint: GROUP BY with multiple aggregates`
#### 31. Filter grouped results using HAVING (★☆☆)
`hint: HAVING (filters after GROUP BY)`
#### 32. Use GROUP BY with ORDER BY on aggregated column (★☆☆)
`hint: ORDER BY can use aggregate or alias`
#### 33. Calculate multiple statistics in one query (★☆☆)
`hint: Multiple aggregate functions`
#### 34. Use FILTER clause with aggregates (DuckDB feature) (★☆☆)
`hint: aggregate() FILTER (WHERE condition)`
#### 35. Calculate running statistics with GROUP BY ALL (★☆☆)
`hint: GROUP BY ALL (groups by all non-aggregated columns)`
#### 36. Use string aggregation with STRING_AGG or LIST (★☆☆)
`hint: STRING_AGG() or LIST()`
#### 37. Calculate percentile values (★☆☆)
`hint: PERCENTILE_CONT, PERCENTILE_DISC`
#### 38. Create two tables and perform an INNER JOIN (★★☆)
`hint: JOIN ... ON`
#### 39. Perform a LEFT JOIN to include unmatched rows (★★☆)
`hint: LEFT JOIN`
#### 40. Perform a RIGHT JOIN (★★☆)
`hint: RIGHT JOIN`
#### 41. Perform a FULL OUTER JOIN (★★☆)
`hint: FULL OUTER JOIN or FULL JOIN`
#### 42. Use CROSS JOIN to generate all combinations (★★☆)
`hint: CROSS JOIN`
#### 43. Perform a self-join to compare rows within the same table (★★☆)
`hint: Join table to itself with different aliases`
#### 44. Join multiple tables in a single query (★★☆)
`hint: Chain multiple JOINs`
#### 45. Use USING clause for joins on same-named columns (★★☆)
`hint: JOIN ... USING (column_name)`
#### 46. Perform a NATURAL JOIN (★★☆)
`hint: NATURAL JOIN (joins on all matching column names)`
#### 47. Use anti-join pattern to find non-matching rows (★★☆)
`hint: LEFT JOIN ... WHERE ... IS NULL`
#### 48. Use semi-join pattern with EXISTS (★★☆)
`hint: WHERE EXISTS (subquery)`
#### 49. Combine results with UNION (★★☆)
`hint: UNION removes duplicates, UNION ALL keeps all`
#### 50. Use INTERSECT to find common values (★★☆)
`hint: INTERSECT`
#### 51. Use EXCEPT to find differences between sets (★★☆)
`hint: EXCEPT`
#### 52. Write a simple subquery in the WHERE clause (★★☆)
`hint: WHERE column = (SELECT ...)`
#### 53. Use a subquery in the FROM clause (derived table) (★★☆)
`hint: FROM (subquery) AS alias`
#### 54. Use a correlated subquery (★★☆)
`hint: Subquery references outer query`
#### 55. Use subquery with IN clause (★★☆)
`hint: WHERE column IN (SELECT ...)`
#### 56. Use subquery with ANY/ALL (★★☆)
`hint: > ANY (subquery), > ALL (subquery)`
#### 57. Write a Common Table Expression (CTE) (★★☆)
`hint: WITH cte_name AS (query)`
#### 58. Use multiple CTEs in a single query (★★☆)
`hint: WITH cte1 AS (...), cte2 AS (...)`
#### 59. Use a CTE that references another CTE (★★☆)
`hint: CTEs can reference previously defined CTEs`
#### 60. Use scalar subquery in SELECT (★★☆)
`hint: SELECT (SELECT ... ) AS column`
#### 61. Use LATERAL join for row-by-row subquery evaluation (★★☆)
`hint: LATERAL or , LATERAL`
#### 62. Add row numbers to results using ROW_NUMBER() (★★☆)
`hint: ROW_NUMBER() OVER (ORDER BY ...)`
#### 63. Partition row numbers by a column (★★☆)
`hint: ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`
#### 64. Use RANK() and DENSE_RANK() for ranking with ties (★★☆)
`hint: RANK() skips numbers after ties, DENSE_RANK() doesn't`
#### 65. Calculate running totals with SUM() window function (★★☆)
`hint: SUM() OVER (ORDER BY ...)`
#### 66. Calculate moving average using window frame (★★☆)
`hint: AVG() OVER (ORDER BY ... ROWS BETWEEN ... AND ...)`
#### 67. Use LAG() to access previous row's value (★★☆)
`hint: LAG(column, offset, default) OVER (...)`
#### 68. Use LEAD() to access next row's value (★★☆)
`hint: LEAD(column, offset, default) OVER (...)`
#### 69. Use FIRST_VALUE() and LAST_VALUE() (★★☆)
`hint: FIRST_VALUE(), LAST_VALUE() with proper frame`
#### 70. Use NTH_VALUE() to get a specific row's value (★★☆)
`hint: NTH_VALUE(column, n) OVER (...)`
#### 71. Use NTILE() to divide rows into buckets (★★☆)
`hint: NTILE(n) OVER (ORDER BY ...)`
#### 72. Calculate cumulative distribution with CUME_DIST() (★★☆)
`hint: CUME_DIST() OVER (ORDER BY ...)`
#### 73. Use window function with FILTER clause (★★☆)
`hint: aggregate FILTER (WHERE ...) OVER (...)`
#### 74. Calculate difference from partition average (★★☆)
`hint: value - AVG() OVER (PARTITION BY ...)`
#### 75. Use multiple window functions with named windows (★★☆)
`hint: WINDOW w AS (...)`
#### 76. Filter window function results using QUALIFY (★★☆)
`hint: QUALIFY (DuckDB-specific, filters window results)`
#### 77. Create and query a LIST column (★★☆)
`hint: LIST, array syntax [1, 2, 3]`
#### 78. Use LIST functions for manipulation (★★☆)
`hint: list_append, list_concat, list_contains, etc.`
#### 79. Use list_transform to apply function to each element (★★☆)
`hint: list_transform(list, lambda)`
#### 80. Use list_filter to select elements (★★☆)
`hint: list_filter(list, lambda)`
#### 81. Use list_reduce for aggregation (★★☆)
`hint: list_reduce(list, lambda)`
#### 82. Flatten nested lists with flatten() (★★☆)
`hint: flatten()`
#### 83. Create and query STRUCT columns (★★☆)
`hint: STRUCT, {'key': value} syntax`
#### 84. Use STRUCT functions (★★☆)
`hint: struct_extract, struct_keys, struct_values`
#### 85. Create and use MAP type (★★☆)
`hint: MAP {key: value}, map_from_entries`
#### 86. Use MAP functions (★★☆)
`hint: map_keys, map_values, map_entries`
#### 87. Use UNNEST to expand arrays/lists into rows (★★☆)
`hint: UNNEST(list), FROM unnest(list)`
#### 88. Create a table with nested types (★★☆)
`hint: Combine STRUCT, LIST in table definition`
#### 89. Use UNION type for heterogeneous data (★★☆)
`hint: UNION(type1, type2, ...)`
#### 90. Use ASOF JOIN for time-series data (★★★)
`hint: ASOF JOIN matches nearest preceding value`
#### 91. Use PIVOT to transform rows to columns (★★★)
`hint: PIVOT ... ON ... USING ...`
#### 92. Use UNPIVOT to transform columns to rows (★★★)
`hint: UNPIVOT ... ON ...`
#### 93. Use QUALIFY to filter window function results (★★★)
`hint: QUALIFY filters after window functions`
#### 94. Use EXCLUDE and REPLACE in SELECT * (★★★)
`hint: SELECT * EXCLUDE (cols), SELECT * REPLACE (expr AS col)`
#### 95. Use COLUMNS expression for dynamic column selection (★★★)
`hint: COLUMNS('pattern'), COLUMNS(*)`
#### 96. Use GROUPING SETS for multiple groupings (★★★)
`hint: GROUP BY GROUPING SETS ((cols), (cols), ...)`
#### 97. Use ROLLUP for hierarchical aggregation (★★★)
`hint: GROUP BY ROLLUP (col1, col2)`
#### 98. Use CUBE for all combination aggregations (★★★)
`hint: GROUP BY CUBE (col1, col2)`
#### 99. Write a recursive CTE (★★★)
`hint: WITH RECURSIVE cte AS (base UNION ALL recursive)`
#### 100. Read a CSV file with DuckDB (★★☆)
`hint: read_csv_auto(), read_csv()`
#### 101. Write query results to a CSV file (★★☆)
`hint: COPY ... TO ..., or write_csv()`
#### 102. Read and write Parquet files (★★☆)
`hint: read_parquet(), COPY TO ... (FORMAT PARQUET)`
#### 103. Read JSON data (★★☆)
`hint: read_json_auto(), read_json()`
#### 104. Query remote files using httpfs extension (★★☆)
`hint: INSTALL httpfs; LOAD httpfs;`
#### 105. Use glob patterns to read multiple files (★★☆)
`hint: read_csv_auto('path/*.csv'), read_parquet('path/**/*.parquet')`
#### 106. Create a view over external files (★★☆)
`hint: CREATE VIEW ... AS SELECT FROM read_...`
#### 107. Export database or tables (★★☆)
`hint: EXPORT DATABASE, COPY`
#### 108. Use DuckDB with partitioned data (★★☆)
`hint: hive_partitioning, write partitioned data`
#### 109. Insert data from external files (★★☆)
`hint: INSERT INTO ... SELECT FROM read_...`
#### 110. Write a simple macro (user-defined function) (★★★)
`hint: CREATE MACRO name(args) AS expression`
#### 111. Use the json extension for JSON processing (★★★)
`hint: json_extract, json_extract_string, ->>, etc.`
#### 112. Use full-text search extension (★★★)
`hint: INSTALL fts; LOAD fts; PRAGMA create_fts_index`
#### 113. Use window functions with complex frames (★★★)
`hint: ROWS/RANGE BETWEEN ... AND ...`
#### 114. Use SAMPLE to randomly sample data (★★★)
`hint: USING SAMPLE n, USING SAMPLE n%`
#### 115. Use EXPLAIN and EXPLAIN ANALYZE (★★★)
`hint: EXPLAIN query, EXPLAIN ANALYZE query`
#### 116. Create and use sequences (★★★)
`hint: CREATE SEQUENCE, nextval()`
#### 117. Use transactions for data integrity (★★★)
`hint: BEGIN TRANSACTION, COMMIT, ROLLBACK`
#### 118. Use COPY with advanced options (★★★)
`hint: COPY with FORMAT, COMPRESSION, PARTITION_BY`
#### 119. Use prepared statements (★★★)
`hint: PREPARE, EXECUTE, DEALLOCATE`
#### 120. Combine multiple advanced features in a complex query (★★★)
`hint: CTEs, window functions, QUALIFY, complex types`