import duckdb
import random

import generators as ge

# Create a global DuckDB connection
con = duckdb.connect()

def setup_sample_tables():
    """Create sample tables used in exercises"""
    con.execute("""
        CREATE OR REPLACE TABLE employees AS 
        SELECT * FROM (VALUES 
            (1, 'Alice', 'Engineering', 75000),
            (2, 'Bob', 'Sales', 65000),
            (3, 'Charlie', 'Engineering', 80000),
            (4, 'Diana', 'HR', 60000),
            (5, 'Eve', 'Sales', 70000)
        ) AS t(id, name, department, salary)
    """)
    
    con.execute("""
        CREATE OR REPLACE TABLE departments AS 
        SELECT * FROM (VALUES 
            ('Engineering', 'Building A'),
            ('Sales', 'Building B'),
            ('HR', 'Building C'),
            ('Marketing', 'Building D')
        ) AS t(name, location)
    """)
    
    con.execute("""
        CREATE OR REPLACE TABLE projects AS 
        SELECT * FROM (VALUES 
            (1, 'Project Alpha', 'Engineering'),
            (2, 'Project Beta', 'Sales'),
            (3, 'Project Gamma', 'Engineering')
        ) AS t(id, name, department)
    """)
    
    print("Sample tables created: employees, departments, projects")

def question(n):
    """Display question n"""
    print(f'{n}. ' + ge.QHA[f'q{n}'])

def hint(n):
    """Display hint for question n"""
    print(ge.QHA[f'h{n}'])

def answer(n):
    """Display answer for question n"""
    print(ge.QHA[f'a{n}'])

def pick():
    """Pick a random question"""
    n = random.randint(1, ge.NUM_EXERCISES)
    question(n)
    return n

def sql(query):
    """Execute a SQL query and return results"""
    return con.sql(query)

def run(query):
    """Execute a SQL query and print results"""
    result = con.sql(query)
    print(result)
    return result

# Setup sample tables on import
setup_sample_tables()

print(f"\nDuckDB Exercises initialized!")
print(f"Total exercises: {ge.NUM_EXERCISES}")
print(f"\nAvailable functions:")
print(f"  question(n) - Display question n")
print(f"  hint(n)     - Display hint for question n")
print(f"  answer(n)   - Display answer for question n")
print(f"  pick()      - Pick a random question")
print(f"  sql(query)  - Execute SQL and return result")
print(f"  run(query)  - Execute SQL and print result")
print(f"\nGlobal connection available as 'con'")
