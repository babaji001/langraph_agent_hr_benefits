"""
Policy MCP Server

Exposes policy tools
for Policy AI Agent.
"""


from typing import Dict, Any

from services.policy_service import PolicyService



class PolicyMCP:


    def __init__(self):

        self.policy_service = PolicyService()



    def search_policy(
            self,
            policy_type: str
    ) -> Dict[str, Any]:

        return self.policy_service.search_policy(
            policy_type
        )



    def get_policy_details(
            self,
            policy_id: str
    ) -> Dict[str, Any]:

        return self.policy_service.get_policy_details(
            policy_id
        )



    def get_policy_summary(
            self,
            policy_type: str
    ) -> Dict[str, Any]:

        return self.policy_service.get_policy_summary(
            policy_type
        )



policy_tools = PolicyMCP()


TOOLS = {

    "search_policy":
        policy_tools.search_policy,

    "get_policy_details":
        policy_tools.get_policy_details,

    "get_policy_summary":
        policy_tools.get_policy_summary

}
