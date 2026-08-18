import sqlite3
import os

DB_FOLDER = "database"
DB_NAME = "employee.db"

os.makedirs(DB_FOLDER, exist_ok=True)

db_path = os.path.join(DB_FOLDER, DB_NAME)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# =====================================================
# DROP TABLES
# =====================================================

tables = [
    "employees",
    "leave_balance",
    "payroll",
    "benefits",
    "claims",
    "retirement"
]

for table in tables:
    cur.execute(f"DROP TABLE IF EXISTS {table}")

# =====================================================
# EMPLOYEES
# =====================================================

cur.execute("""
CREATE TABLE employees(
employee_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
department TEXT,
manager TEXT,
email TEXT,
country TEXT,
hire_date TEXT,
employment_type TEXT
)
""")

employees = [

(1001,"John","Smith","IT","David Brown","john.smith@company.com","USA","2018-01-12","Full Time"),
(1002,"Mary","Jones","Finance","David Brown","mary.jones@company.com","USA","2019-03-15","Full Time"),
(1003,"Kevin","Lee","HR","Susan White","kevin.lee@company.com","USA","2021-07-10","Full Time"),
(1004,"Lisa","Green","Sales","Mark Taylor","lisa.green@company.com","Canada","2020-09-14","Full Time"),
(1005,"Robert","Hall","IT","David Brown","robert.hall@company.com","USA","2017-05-22","Contractor")

]

cur.executemany("""
INSERT INTO employees VALUES (?,?,?,?,?,?,?,?,?)
""",employees)

# =====================================================
# LEAVE
# =====================================================

cur.execute("""
CREATE TABLE leave_balance(

employee_id INTEGER,

pto REAL,

sick_leave REAL,

floating_holiday REAL,

personal_leave REAL,

last_updated TEXT

)
""")

leave = [

(1001,120,40,8,16,"2026-01-01"),
(1002,96,32,8,8,"2026-01-01"),
(1003,140,40,8,16,"2026-01-01"),
(1004,88,24,8,8,"2026-01-01"),
(1005,60,16,0,0,"2026-01-01")

]

cur.executemany("""
INSERT INTO leave_balance VALUES (?,?,?,?,?,?)
""",leave)

# =====================================================
# PAYROLL
# =====================================================

cur.execute("""

CREATE TABLE payroll(

employee_id INTEGER,

annual_salary REAL,

bonus REAL,

pay_frequency TEXT,

last_pay_date TEXT

)

""")

payroll=[

(1001,125000,12000,"Biweekly","2026-01-15"),
(1002,115000,8000,"Biweekly","2026-01-15"),
(1003,98000,5000,"Biweekly","2026-01-15"),
(1004,89000,6000,"Biweekly","2026-01-15"),
(1005,78000,0,"Monthly","2026-01-31")

]

cur.executemany("""
INSERT INTO payroll VALUES (?,?,?,?,?)
""",payroll)

# =====================================================
# BENEFITS
# =====================================================

cur.execute("""

CREATE TABLE benefits(

employee_id INTEGER,

medical_plan TEXT,

dental_plan TEXT,

vision_plan TEXT,

life_insurance TEXT,

hsa_balance REAL,

fsa_balance REAL

)

""")

benefits=[

(1001,"PPO Gold","Premium Dental","Vision Plus","500000",3400,1500),
(1002,"PPO Silver","Standard Dental","Vision Basic","250000",2200,800),
(1003,"HDHP","Premium Dental","Vision Plus","500000",5400,2200),
(1004,"PPO Gold","Premium Dental","Vision Basic","250000",1800,700),
(1005,"HDHP","Standard Dental","Vision Basic","100000",500,0)

]

cur.executemany("""
INSERT INTO benefits VALUES (?,?,?,?,?,?,?)
""",benefits)

# =====================================================
# CLAIMS
# =====================================================

cur.execute("""

CREATE TABLE claims(

claim_id INTEGER PRIMARY KEY,

employee_id INTEGER,

claim_type TEXT,

amount REAL,

status TEXT,

submitted_date TEXT

)

""")

claims=[

(1,1001,"Medical",800,"Approved","2026-01-10"),
(2,1001,"Dental",200,"Processing","2026-01-12"),
(3,1002,"Vision",150,"Approved","2026-01-05"),
(4,1003,"Medical",1200,"Denied","2026-01-08"),
(5,1004,"Medical",450,"Processing","2026-01-11"),
(6,1005,"Dental",350,"Approved","2026-01-13")

]

cur.executemany("""
INSERT INTO claims VALUES (?,?,?,?,?,?)
""",claims)

# =====================================================
# RETIREMENT
# =====================================================

cur.execute("""

CREATE TABLE retirement(

employee_id INTEGER,

plan_type TEXT,

employee_contribution REAL,

employer_match REAL,

balance REAL

)

""")

retirement=[

(1001,"401K",6,6,180000),
(1002,"401K",5,5,150000),
(1003,"401K",8,6,85000),
(1004,"401K",6,4,62000),
(1005,"401K",4,3,45000)

]

cur.executemany("""
INSERT INTO retirement VALUES (?,?,?,?,?)
""",retirement)

conn.commit()

print("="*60)
print("Enterprise HR Database Created Successfully")
print("="*60)
print("Location :",db_path)

conn.close()
