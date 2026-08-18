
# agents/employee_agent.py

from tools.hr_mcp import hr_mcp


class EmployeeAgent:

    def __init__(self):

        self.name = "employee"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_employee_profile",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "employee_profile",

            "data": result

        }


employee_agent = EmployeeAgent()
