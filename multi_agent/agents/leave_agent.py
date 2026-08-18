
# agents/leave_agent.py

from tools.hr_mcp import hr_mcp


class LeaveAgent:

    def __init__(self):

        self.name = "leave"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_leave_balance",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "leave_balance",

            "data": result

        }


leave_agent = LeaveAgent()
