import sqlite3
import os

DB = "data/employee.db"

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS dependents")
cur.execute("DROP TABLE IF EXISTS claims")
cur.execute("DROP TABLE IF EXISTS benefits")
cur.execute("DROP TABLE IF EXISTS payroll")
cur.execute("DROP TABLE IF EXISTS leave_history")
cur.execute("DROP TABLE IF EXISTS leave_balance")
cur.execute("DROP TABLE IF EXISTS employees")

##########################################################
# Employees
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(

emp_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT,
department TEXT,
manager TEXT,
location TEXT,
hire_date TEXT

)
""")

##########################################################
# Leave Balance
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS leave_balance(

emp_id INTEGER,
pto INTEGER,
sick_leave INTEGER,
floating_holiday INTEGER,
personal_leave INTEGER

)
""")

##########################################################
# Leave History
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS leave_history(

leave_id INTEGER PRIMARY KEY AUTOINCREMENT,
emp_id INTEGER,
leave_type TEXT,
start_date TEXT,
end_date TEXT,
status TEXT

)
""")

##########################################################
# Payroll
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS payroll(

emp_id INTEGER,
salary INTEGER,
bonus INTEGER,
tax INTEGER,
net_pay INTEGER

)
""")

##########################################################
# Benefits
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS benefits(

emp_id INTEGER,
medical_plan TEXT,
dental_plan TEXT,
vision_plan TEXT,
life_insurance TEXT,
std TEXT,
ltd TEXT,
hsa TEXT,
fsa TEXT,
retirement TEXT

)
""")

##########################################################
# Claims
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS claims(

claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
emp_id INTEGER,
claim_type TEXT,
provider TEXT,
claim_amount INTEGER,
status TEXT

)
""")

##########################################################
# Dependents
##########################################################

cur.execute("""
CREATE TABLE IF NOT EXISTS dependents(

dependent_id INTEGER PRIMARY KEY AUTOINCREMENT,
emp_id INTEGER,
name TEXT,
relationship TEXT,
covered TEXT

)
""")

##########################################################
# Employees
##########################################################

employees = [

(1001,"John","Smith","john.smith@alight.com","IT","David Miller","Chicago","2019-03-12"),
(1002,"Alice","Johnson","alice.johnson@alight.com","HR","Sarah Adams","Chicago","2021-01-10"),
(1003,"Robert","Brown","robert.brown@alight.com","Finance","Kevin Lee","Dallas","2018-08-21"),
(1004,"Emily","Wilson","emily.wilson@alight.com","Operations","David Miller","Atlanta","2020-05-15"),
(1005,"Michael","Taylor","michael.taylor@alight.com","IT","David Miller","Remote","2017-09-30")

]

cur.executemany("INSERT OR REPLACE INTO employees VALUES (?,?,?,?,?,?,?,?)",employees)

##########################################################
# Leave Balance
##########################################################

leave = [

(1001,18,8,2,1),
(1002,10,6,1,0),
(1003,25,9,2,2),
(1004,14,7,1,1),
(1005,22,10,2,2)

]

cur.executemany("INSERT INTO leave_balance VALUES (?,?,?,?,?)",leave)

##########################################################
# Leave History
##########################################################

history = [

(1001,"Vacation","2026-02-10","2026-02-15","Approved"),
(1001,"Sick","2026-05-12","2026-05-13","Approved"),
(1002,"Vacation","2026-04-01","2026-04-05","Approved"),
(1003,"FMLA","2026-01-10","2026-03-01","Approved"),
(1004,"Personal","2026-06-01","2026-06-02","Pending")

]

cur.executemany("""

INSERT INTO leave_history
(emp_id,leave_type,start_date,end_date,status)

VALUES (?,?,?,?,?)

""",history)

##########################################################
# Payroll
##########################################################

payroll = [

(1001,120000,10000,28000,8500),
(1002,90000,5000,19000,6200),
(1003,130000,15000,33000,9300),
(1004,85000,4000,17000,5800),
(1005,140000,18000,35000,9900)

]

cur.executemany("INSERT INTO payroll VALUES (?,?,?,?,?)",payroll)

##########################################################
# Benefits
##########################################################

benefits = [

(1001,"PPO Gold","Delta Dental","VSP","2x Salary","Yes","Yes","Yes","Yes","401K"),
(1002,"HMO Silver","Delta Dental","VSP","2x Salary","Yes","No","Yes","No","401K"),
(1003,"PPO Platinum","MetLife","EyeMed","3x Salary","Yes","Yes","Yes","Yes","401K"),
(1004,"PPO Gold","MetLife","EyeMed","2x Salary","No","No","Yes","Yes","401K"),
(1005,"PPO Gold","Delta Dental","VSP","3x Salary","Yes","Yes","Yes","Yes","401K")

]

cur.executemany("INSERT INTO benefits VALUES (?,?,?,?,?,?,?,?,?,?)",benefits)

##########################################################
# Claims
##########################################################

claims = [

(1001,"Medical","Mayo Clinic",1800,"Approved"),
(1001,"Dental","Smile Dental",450,"Approved"),
(1002,"Vision","LensCrafters",220,"Pending"),
(1003,"Medical","Cleveland Clinic",5200,"Approved"),
(1004,"Medical","Northwestern",900,"Rejected"),
(1005,"Dental","Aspen Dental",350,"Approved")

]

cur.executemany("""

INSERT INTO claims
(emp_id,claim_type,provider,claim_amount,status)

VALUES (?,?,?,?,?)

""",claims)

##########################################################
# Dependents
##########################################################

dependents = [

(1001,"Jennifer Smith","Spouse","Yes"),
(1001,"Emma Smith","Child","Yes"),
(1002,"Tom Johnson","Spouse","Yes"),
(1003,"Sophia Brown","Child","Yes"),
(1005,"Olivia Taylor","Spouse","Yes")

]

cur.executemany("""

INSERT INTO dependents
(emp_id,name,relationship,covered)

VALUES (?,?,?,?)

""",dependents)

conn.commit()
conn.close()

print("Enterprise Employee Database Created Successfully.")
