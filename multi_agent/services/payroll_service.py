
# services/payroll_service.py

import sqlite3
from config import DATABASE

class PayrollService:

    def __init__(self):

        self.database = DATABASE


    def get_summary(
        self,
        employee_id
    ):

        connection = sqlite3.connect(
            self.database
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                employee_id,
                pay_period,
                gross_pay,
                deductions,
                net_pay,
                pay_date
            FROM payroll
            WHERE employee_id = ?
            ORDER BY pay_date DESC
            LIMIT 1
            """,
            (
                employee_id,
            )
        )


        row = cursor.fetchone()

        connection.close()


        if not row:

            return {

                "employee_id": employee_id,

                "message": "Payroll record not found"

            }


        return {

            "employee_id": row[0],

            "pay_period": row[1],

            "gross_pay": row[2],

            "deductions": row[3],

            "net_pay": row[4],

            "pay_date": row[5]

        }
