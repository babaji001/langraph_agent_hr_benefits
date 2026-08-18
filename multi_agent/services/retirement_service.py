
# services/retirement_service.py

import sqlite3
from config import DATABASE

class RetirementService:

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
            *
            FROM retirement
            WHERE employee_id = ?
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

                "message": "Retirement record not found"

            }


        return {

            "employee_id": row[0],

            "plan_type": row[1],

            "employee_contribution": row[2],

            "employer_match": row[3],

            "balance": row[4],

        }
