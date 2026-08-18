
# agents/payroll_agent.py

from tools.hr_mcp import hr_mcp


class PayrollAgent:

    def __init__(self):

        self.name = "payroll"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_payroll_summary",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "payroll_summary",

            "data": result

        }


payroll_agent = PayrollAgent()
