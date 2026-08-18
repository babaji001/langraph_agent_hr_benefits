
# services/claims_service.py

import sqlite3
from config import DATABASE
class ClaimsService:

    def __init__(self):

        self.database = DATABASE


    def get_status(
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
                claim_id,
                claim_type,
                claim_status,
                submitted_date,
                approved_amount
            FROM claims
            WHERE employee_id = ?
            ORDER BY submitted_date DESC
            """,
            (
                employee_id,
            )
        )


        rows = cursor.fetchall()

        connection.close()


        if not rows:

            return {

                "employee_id": employee_id,

                "message": "Claims record not found"

            }


        claims = []


        for row in rows:

            claims.append(

                {

                    "claim_id": row[1],

                    "claim_type": row[2],

                    "claim_status": row[3],

                    "submitted_date": row[4],

                    "approved_amount": row[5]

                }

            )


        return {

            "employee_id": employee_id,

            "claims": claims

        }
