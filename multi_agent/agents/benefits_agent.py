
# agents/benefits_agent.py

from tools.hr_mcp import hr_mcp


class BenefitsAgent:

    def __init__(self):

        self.name = "benefits"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_benefits",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "benefits_information",

            "data": result

        }


benefits_agent = BenefitsAgent()
