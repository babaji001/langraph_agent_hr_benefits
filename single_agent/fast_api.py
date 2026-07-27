from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Enterprise HR APIs")

DATABASE = "data/employee.db"


#########################################################
# Helper Function
#########################################################

def execute_query(query, params=()):

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute(query, params)

    rows = cur.fetchall()

    conn.close()

    return [dict(row) for row in rows]


#########################################################
# Employee
#########################################################

@app.get("/employee/{emp_id}")

def employee(emp_id: int):

    return execute_query(

        "SELECT * FROM employees WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Leave Balance
#########################################################

@app.get("/leave/{emp_id}")

def leave(emp_id: int):

    return execute_query(

        "SELECT * FROM leave_balance WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Leave History
#########################################################

@app.get("/leave/history/{emp_id}")

def leave_history(emp_id: int):

    return execute_query(

        "SELECT * FROM leave_history WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Payroll
#########################################################

@app.get("/payroll/{emp_id}")

def payroll(emp_id: int):

    return execute_query(

        "SELECT * FROM payroll WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Benefits
#########################################################

@app.get("/benefits/{emp_id}")

def benefits(emp_id: int):

    return execute_query(

        "SELECT * FROM benefits WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Claims
#########################################################

@app.get("/claims/{emp_id}")

def claims(emp_id: int):

    return execute_query(

        "SELECT * FROM claims WHERE emp_id=?",

        (emp_id,)
    )


#########################################################
# Dependents
#########################################################

@app.get("/dependents/{emp_id}")

def dependents(emp_id: int):

    return execute_query(

        "SELECT * FROM dependents WHERE emp_id=?",

        (emp_id,)
    )
