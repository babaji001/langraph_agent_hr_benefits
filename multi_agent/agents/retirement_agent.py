
# agents/retirement_agent.py

from tools.hr_mcp import hr_mcp


class RetirementAgent:

    def __init__(self):

        self.name = "retirement"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_retirement_summary",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "retirement_summary",

            "data": result

        }


retirement_agent = RetirementAgent()
