
# services/hr_service.py

import sqlite3
from config import DATABASE

class HRService:

    def __init__(self):

        self.database = DATABASE


    def create_case(
        self,
        request
    ):

        connection = sqlite3.connect(
            self.database
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO hr_cases
            (
                employee_id,
                issue,
                status
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                request.get("employee_id"),

                request.get("question"),

                "OPEN"
            )
        )


        connection.commit()


        case_id = cursor.lastrowid


        connection.close()


        return {

            "employee_id":
                request.get("employee_id"),

            "case_id":
                case_id,

            "status":
                "OPEN",

            "message":
                "HR case created successfully"

        }


    def get_case_status(
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
                case_id,
                issue,
                status
            FROM hr_cases
            WHERE employee_id = ?
            ORDER BY case_id DESC
            """,
            (
                employee_id,
            )
        )


        rows = cursor.fetchall()

        connection.close()


        cases = []


        for row in rows:

            cases.append(

                {

                    "case_id": row[0],

                    "issue": row[1],

                    "status": row[2]

                }

            )


        return {

            "employee_id": employee_id,

            "cases": cases

        }
