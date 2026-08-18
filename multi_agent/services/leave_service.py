
# services/leave_service.py

import sqlite3

from config import DATABASE


class LeaveService:

    def __init__(self):

        self.database = DATABASE



    def get_balance(
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
                pto,
                sick_leave,
                floating_holiday,
                personal_leave,
                last_updated

            FROM leave_balance

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

                    "Leave balance not found",

                "employee_id":

                    employee_id

            }



        return {

            "employee_id":

                row[0],

            "pto":

                row[1],

            "sick_leave":

                row[2],

            "floating_holiday":

                row[3],

            "personal_leave":

                row[4],

            "last_updated":

                row[5]

        }
