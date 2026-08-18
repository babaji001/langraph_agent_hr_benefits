
# agents/policy_agent.py

from tools.hr_mcp import hr_mcp


class PolicyAgent:

    def __init__(self):

        self.name = "policy"


    def process(
        self,
        question,
        employee_id
    ):

        result = hr_mcp.execute(

            "search_policy",

            {
                "query": question
            }

        )


        return {

            "agent": self.name,

            "intent": "policy_search",

            "data": result

        }


policy_agent = PolicyAgent()
