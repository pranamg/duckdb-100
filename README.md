# 100+ DuckDB Exercises

This is a collection of DuckDB exercises covering SQL fundamentals, advanced queries, window functions, DuckDB-specific features, and file operations. Inspired by [numpy-100](https://github.com/rougier/numpy-100).

## Exercise Categories

| Category | Count | Difficulty |
|----------|-------|------------|
| SQL Basics | 15 | ★☆☆ |
| Filtering & Conditions | 10 | ★☆☆ |
| Aggregations | 12 | ★☆☆ |
| JOINs | 14 | ★★☆ |
| Subqueries & CTEs | 10 | ★★☆ |
| Window Functions | 15 | ★★☆ |
| DuckDB Types (LIST, STRUCT, MAP) | 13 | ★★☆ |
| DuckDB-Specific Features | 10 | ★★★ |
| File Operations | 10 | ★★☆ |
| Advanced Queries | 11 | ★★★ |

**Total: 120 exercises**

## Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Interactive Mode (Jupyter)

1. Open `100_DuckDB_exercises.ipynb` in Jupyter
2. Run the first cell to initialize
3. Use `hint(n)` and `answer(n)` to get help

```python
%run initialise.py

# Get a random question
pick()

# Get hint for question 5
hint(5)

# Get answer for question 5
answer(5)

# Execute SQL directly
sql("SELECT * FROM employees")
```

### Random Practice

Open `100_DuckDB_random.ipynb` for random question practice mode.

### Read on GitHub

- [Questions only](100_DuckDB_exercises.md)
- [Questions with hints](100_DuckDB_exercises_with_hints.md)
- [Questions with solutions](100_DuckDB_exercises_with_solutions.md)
- [Questions with hints and solutions](100_DuckDB_exercises_with_hints_with_solutions.md)

## File Structure

```
duckdb-100/
├── source/
│   ├── headers.ktx           # Header text (keyed text format)
│   └── exercises.ktx         # All exercises (q/h/a format)
├── .github/
│   └── workflows/
│       └── generate.yml      # Auto-generate on push
├── generators.py             # Generate notebooks/markdown
├── initialise.py             # Helper functions
├── requirements.txt          # Python dependencies
├── 100_DuckDB_exercises.ipynb
├── 100_DuckDB_exercises.md
├── 100_DuckDB_exercises_with_hints.md
├── 100_DuckDB_exercises_with_solutions.md
├── 100_DuckDB_exercises_with_hints_with_solutions.md
└── 100_DuckDB_random.ipynb
```

## Contributing

1. Edit exercises in `source/exercises.ktx`
2. Run `python generators.py` to regenerate files
3. Or push changes and GitHub Actions will auto-generate

### KTX Format

```
< q1
Question text here (★☆☆)

< h1
hint: relevant functions

< a1
-- SQL solution
SELECT * FROM table;
```

## Sample Tables

The following tables are automatically created when you run `initialise.py`:

**employees**
| id | name | department | salary |
|----|------|------------|--------|
| 1 | Alice | Engineering | 75000 |
| 2 | Bob | Sales | 65000 |
| 3 | Charlie | Engineering | 80000 |
| 4 | Diana | HR | 60000 |
| 5 | Eve | Sales | 70000 |

**departments**
| name | location |
|------|----------|
| Engineering | Building A |
| Sales | Building B |
| HR | Building C |
| Marketing | Building D |

**projects**
| id | name | department |
|----|------|------------|
| 1 | Project Alpha | Engineering |
| 2 | Project Beta | Sales |
| 3 | Project Gamma | Engineering |

## License

This work is licensed under the MIT license.
