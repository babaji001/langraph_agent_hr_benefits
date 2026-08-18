"""
Claims MCP Server

Exposes claims capabilities as tools
for the Claims AI Agent.

Architecture Layer:
MCP Integration Layer


Flow:

Claims Agent

      |
      v

Claims MCP Tools

      |
      v

Claims Service

      |
      v

Claims System
"""


from typing import Dict, Any

from services.claims_service import ClaimsService



class ClaimsMCP:
    """
    MCP interface for Claims operations.
    """


    def __init__(self):

        self.claims_service = ClaimsService()



    # -------------------------------------------------
    # Tool 1:
    # Retrieve claim status
    # -------------------------------------------------

    def get_claim_status(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        """
        Retrieve current claim status
        for an employee.
        """

        return self.claims_service.get_claim_status(
            employee_id
        )



    # -------------------------------------------------
    # Tool 2:
    # Claim History
    # -------------------------------------------------

    def get_claim_history(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        """
        Retrieve previous claims.
        """

        return self.claims_service.get_claim_history(
            employee_id
        )



    # -------------------------------------------------
    # Tool 3:
    # Claim Eligibility
    # -------------------------------------------------

    def check_claim_eligibility(
            self,
            employee_id: str,
            claim_type: str
    ) -> Dict[str, Any]:

        """
        Check whether employee
        can submit a specific claim.
        """

        return self.claims_service.check_claim_eligibility(
            employee_id,
            claim_type
        )



    # -------------------------------------------------
    # Tool 4:
    # Claim Explanation
    # -------------------------------------------------

    def explain_claim(
            self,
            claim_id: str
    ) -> Dict[str, Any]:

        """
        Explain claim decision.
        """

        return self.claims_service.explain_claim(
            claim_id
        )



# -----------------------------------------------------
# MCP Tool Registry
# -----------------------------------------------------

claims_tools = ClaimsMCP()



TOOLS = {

    "get_claim_status":
        claims_tools.get_claim_status,


    "get_claim_history":
        claims_tools.get_claim_history,


    "check_claim_eligibility":
        claims_tools.check_claim_eligibility,


    "explain_claim":
        claims_tools.explain_claim

}
