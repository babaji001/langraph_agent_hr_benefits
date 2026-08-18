
# services/employee_service.py

import sqlite3

from config import DATABASE


class EmployeeService:

    def __init__(self):

        self.database = DATABASE



    def get_profile(
        self,
        employee_id
    ):

        conn = sqlite3.connect(

            self.database

        )


        cursor = conn.cursor()


        cursor.execute(

            """
            SELECT
                employee_id,
                first_name,
                last_name,
                department,
                manager,
                email,
                country,
                hire_date,
                employment_type
            FROM employees
            WHERE employee_id = ?
            """,

            (
                employee_id,
            )

        )


        row = cursor.fetchone()


        conn.close()



        if not row:

            return {

                "message":
                    "Employee not found",

                "employee_id":
                    employee_id

            }



        return {

            "employee_id":
                row[0],

            "first_name":
                row[1],

            "last_name":
                row[2],

            "department":
                row[3],

            "manager":
                row[4],

            "email":
                row[5],

            "country":
                row[6],

            "hire_date":
                row[7],

            "employment_type":
                row[8]

        }
