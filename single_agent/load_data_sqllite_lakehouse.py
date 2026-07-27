import sqlite3
import pandas as pd

DATABASE = "data/employee.db"

# Read CSV
df = pd.read_csv("data/employees.csv")

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Optional: Clear existing data if you rerun
cursor.execute("DELETE FROM Employee")
cursor.execute("DELETE FROM LeaveBalance")
cursor.execute("DELETE FROM Payroll")

# Load records
for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO Employee
        VALUES (?,?,?,?,?)
    """, (
        int(row.employee_id),
        row.employee_name,
        row.department,
        row.designation,
        row.location
    ))

    cursor.execute("""
        INSERT INTO LeaveBalance
        VALUES (?,?,?,?)
    """, (
        int(row.employee_id),
        int(row.annual_leave),
        int(row.sick_leave),
        row.fmla_eligible
    ))

    cursor.execute("""
        INSERT INTO Payroll
        VALUES (?,?,?,?)
    """, (
        int(row.employee_id),
        float(row.salary),
        float(row.bonus),
        row.last_payment
    ))

conn.commit()

print("Sample data loaded successfully!")

conn.close()
