
# agents/hr_agent.py

from tools.hr_mcp import hr_mcp


class HRAgent:

    def __init__(self):

        self.name = "hr"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "create_hr_case",

            {
                "employee_id": employee_id,

                "question": question

            }

        )


        return {

            "agent": self.name,

            "intent": "hr_case_creation",

            "data": result

        }


hr_agent = HRAgent()
