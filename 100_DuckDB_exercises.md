


# 100+ DuckDB exercises

This is a collection of DuckDB exercises covering SQL fundamentals, advanced queries, window functions,
DuckDB-specific features, and file operations. The goal of this collection is to offer a quick reference
for both old and new users but also to provide a set of exercises for those who teach.

If you find an error or think you've a better way to solve some of them, feel
free to open an issue at <https://github.com/pranamg/duckdb-100>.
File automatically generated. See the documentation to update questions/answers/hints programmatically.

#### 1. Import DuckDB and check the version (★☆☆)

#### 2. Create an in-memory DuckDB connection and run a simple SELECT (★☆☆)

#### 3. Generate a sequence of numbers from 1 to 10 using DuckDB (★☆☆)

#### 4. Select specific columns from a generated sequence (★☆☆)

#### 5. Use SELECT with literal values to create a simple result set (★☆☆)

#### 6. Create a table from a VALUES clause and query it (★☆☆)

#### 7. Sort results by a column in descending order (★☆☆)

#### 8. Limit the result set to the first 3 rows (★☆☆)

#### 9. Skip the first 2 rows and return the next 3 (★☆☆)

#### 10. Select distinct values from a column (★☆☆)

#### 11. Count the total number of rows in a table (★☆☆)

#### 12. Use column aliases to rename output columns (★☆☆)

#### 13. Combine two columns into one with string concatenation (★☆☆)

#### 14. Use CASE expression to categorize salary levels (★☆☆)

#### 15. Use COALESCE to handle NULL values (★☆☆)

#### 16. Filter rows where salary is greater than 65000 (★☆☆)

#### 17. Filter rows using multiple conditions with AND (★☆☆)

#### 18. Filter rows using OR for alternative conditions (★☆☆)

#### 19. Use IN clause to match multiple values (★☆☆)

#### 20. Use BETWEEN to filter a range of values (★☆☆)

#### 21. Use LIKE for pattern matching with wildcards (★☆☆)

#### 22. Use ILIKE for case-insensitive pattern matching (★☆☆)

#### 23. Filter rows where a value is NOT in a list (★☆☆)

#### 24. Use IS NULL and IS NOT NULL to filter null values (★☆☆)

#### 25. Use regular expression matching with SIMILAR TO (★☆☆)

#### 26. Calculate the sum of all salaries (★☆☆)

#### 27. Calculate the average salary (★☆☆)

#### 28. Find the minimum and maximum salaries (★☆☆)

#### 29. Count employees per department using GROUP BY (★☆☆)

#### 30. Calculate total and average salary per department (★☆☆)

#### 31. Filter grouped results using HAVING (★☆☆)

#### 32. Use GROUP BY with ORDER BY on aggregated column (★☆☆)

#### 33. Calculate multiple statistics in one query (★☆☆)

#### 34. Use FILTER clause with aggregates (DuckDB feature) (★☆☆)

#### 35. Calculate running statistics with GROUP BY ALL (★☆☆)

#### 36. Use string aggregation with STRING_AGG or LIST (★☆☆)

#### 37. Calculate percentile values (★☆☆)

#### 38. Create two tables and perform an INNER JOIN (★★☆)

#### 39. Perform a LEFT JOIN to include unmatched rows (★★☆)

#### 40. Perform a RIGHT JOIN (★★☆)

#### 41. Perform a FULL OUTER JOIN (★★☆)

#### 42. Use CROSS JOIN to generate all combinations (★★☆)

#### 43. Perform a self-join to compare rows within the same table (★★☆)

#### 44. Join multiple tables in a single query (★★☆)

#### 45. Use USING clause for joins on same-named columns (★★☆)

#### 46. Perform a NATURAL JOIN (★★☆)

#### 47. Use anti-join pattern to find non-matching rows (★★☆)

#### 48. Use semi-join pattern with EXISTS (★★☆)

#### 49. Combine results with UNION (★★☆)

#### 50. Use INTERSECT to find common values (★★☆)

#### 51. Use EXCEPT to find differences between sets (★★☆)

#### 52. Write a simple subquery in the WHERE clause (★★☆)

#### 53. Use a subquery in the FROM clause (derived table) (★★☆)

#### 54. Use a correlated subquery (★★☆)

#### 55. Use subquery with IN clause (★★☆)

#### 56. Use subquery with ANY/ALL (★★☆)

#### 57. Write a Common Table Expression (CTE) (★★☆)

#### 58. Use multiple CTEs in a single query (★★☆)

#### 59. Use a CTE that references another CTE (★★☆)

#### 60. Use scalar subquery in SELECT (★★☆)

#### 61. Use LATERAL join for row-by-row subquery evaluation (★★☆)

#### 62. Add row numbers to results using ROW_NUMBER() (★★☆)

#### 63. Partition row numbers by a column (★★☆)

#### 64. Use RANK() and DENSE_RANK() for ranking with ties (★★☆)

#### 65. Calculate running totals with SUM() window function (★★☆)

#### 66. Calculate moving average using window frame (★★☆)

#### 67. Use LAG() to access previous row's value (★★☆)

#### 68. Use LEAD() to access next row's value (★★☆)

#### 69. Use FIRST_VALUE() and LAST_VALUE() (★★☆)

#### 70. Use NTH_VALUE() to get a specific row's value (★★☆)

#### 71. Use NTILE() to divide rows into buckets (★★☆)

#### 72. Calculate cumulative distribution with CUME_DIST() (★★☆)

#### 73. Use window function with FILTER clause (★★☆)

#### 74. Calculate difference from partition average (★★☆)

#### 75. Use multiple window functions with named windows (★★☆)

#### 76. Filter window function results using QUALIFY (★★☆)

#### 77. Create and query a LIST column (★★☆)

#### 78. Use LIST functions for manipulation (★★☆)

#### 79. Use list_transform to apply function to each element (★★☆)

#### 80. Use list_filter to select elements (★★☆)

#### 81. Use list_reduce for aggregation (★★☆)

#### 82. Flatten nested lists with flatten() (★★☆)

#### 83. Create and query STRUCT columns (★★☆)

#### 84. Use STRUCT functions (★★☆)

#### 85. Create and use MAP type (★★☆)

#### 86. Use MAP functions (★★☆)

#### 87. Use UNNEST to expand arrays/lists into rows (★★☆)

#### 88. Create a table with nested types (★★☆)

#### 89. Use UNION type for heterogeneous data (★★☆)

#### 90. Use ASOF JOIN for time-series data (★★★)

#### 91. Use PIVOT to transform rows to columns (★★★)

#### 92. Use UNPIVOT to transform columns to rows (★★★)

#### 93. Use QUALIFY to filter window function results (★★★)

#### 94. Use EXCLUDE and REPLACE in SELECT * (★★★)

#### 95. Use COLUMNS expression for dynamic column selection (★★★)

#### 96. Use GROUPING SETS for multiple groupings (★★★)

#### 97. Use ROLLUP for hierarchical aggregation (★★★)

#### 98. Use CUBE for all combination aggregations (★★★)

#### 99. Write a recursive CTE (★★★)

#### 100. Read a CSV file with DuckDB (★★☆)

#### 101. Write query results to a CSV file (★★☆)

#### 102. Read and write Parquet files (★★☆)

#### 103. Read JSON data (★★☆)

#### 104. Query remote files using httpfs extension (★★☆)

#### 105. Use glob patterns to read multiple files (★★☆)

#### 106. Create a view over external files (★★☆)

#### 107. Export database or tables (★★☆)

#### 108. Use DuckDB with partitioned data (★★☆)

#### 109. Insert data from external files (★★☆)

#### 110. Write a simple macro (user-defined function) (★★★)

#### 111. Use the json extension for JSON processing (★★★)

#### 112. Use full-text search extension (★★★)

#### 113. Use window functions with complex frames (★★★)

#### 114. Use SAMPLE to randomly sample data (★★★)

#### 115. Use EXPLAIN and EXPLAIN ANALYZE (★★★)

#### 116. Create and use sequences (★★★)

#### 117. Use transactions for data integrity (★★★)

#### 118. Use COPY with advanced options (★★★)

#### 119. Use prepared statements (★★★)

#### 120. Combine multiple advanced features in a complex query (★★★)
