
# agents/claims_agent.py

from tools.hr_mcp import hr_mcp


class ClaimsAgent:

    def __init__(self):

        self.name = "claims"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "get_claim_status",

            {
                "employee_id": employee_id
            }

        )


        return {

            "agent": self.name,

            "intent": "claims_status",

            "data": result

        }


claims_agent = ClaimsAgent()
