
# services/benefits_service.py

import sqlite3
from config import DATABASE

class BenefitsService:

    def __init__(self):

        self.database = DATABASE

    def get_details(
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
                health_plan,
                dental_plan,
                vision_plan,
                retirement_plan,
                effective_date
            FROM benefits
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

                "message": "Benefits record not found"

            }


        return {

            "employee_id": row[0],

            "health_plan": row[1],

            "dental_plan": row[2],

            "vision_plan": row[3],

            "retirement_plan": row[4],

            "effective_date": row[5]

        }
