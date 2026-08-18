"""
Retirement MCP Server

Exposes retirement tools
for Retirement AI Agent.
"""


from typing import Dict, Any

from services.retirement_service import RetirementService



class RetirementMCP:


    def __init__(self):

        self.retirement_service = RetirementService()



    def get_retirement_balance(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        return self.retirement_service.get_retirement_balance(
            employee_id
        )



    def get_contribution_details(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        return self.retirement_service.get_contribution_details(
            employee_id
        )



    def get_retirement_projection(
            self,
            employee_id: str,
            years: int
    ) -> Dict[str, Any]:

        return self.retirement_service.get_retirement_projection(
            employee_id,
            years
        )



    def get_retirement_advice(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        return self.retirement_service.get_retirement_advice(
            employee_id
        )



retirement_tools = RetirementMCP()


TOOLS = {

    "get_retirement_balance":
        retirement_tools.get_retirement_balance,

    "get_contribution_details":
        retirement_tools.get_contribution_details,

    "get_retirement_projection":
        retirement_tools.get_retirement_projection,

    "get_retirement_advice":
        retirement_tools.get_retirement_advice

}
