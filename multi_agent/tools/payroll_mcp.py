"""
Payroll MCP Server

Exposes payroll capabilities as tools
for the Payroll AI Agent.

Architecture Layer:
MCP Integration Layer

Flow:

Payroll Agent
      |
      |
 MCP Tools
      |
      |
 Payroll Service
      |
      |
 Payroll System
"""

from typing import Dict, Any

from services.payroll_service import PayrollService


class PayrollMCP:
    """
    MCP interface for Payroll operations.
    """

    def __init__(self):

        self.payroll_service = PayrollService()


    # -------------------------------------------------
    # Tool 1:
    # Retrieve employee payroll summary
    # -------------------------------------------------

    def get_payroll_summary(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        """
        Returns payroll summary.

        Example:
        - Gross salary
        - Tax deductions
        - Net pay
        - Pay period
        """

        return self.payroll_service.get_payroll_summary(
            employee_id
        )


    # -------------------------------------------------
    # Tool 2:
    # Retrieve payslip
    # -------------------------------------------------

    def get_pay_slip(
            self,
            employee_id: str,
            month: str
    ) -> Dict[str, Any]:

        """
        Retrieve monthly payslip.
        """

        return self.payroll_service.get_pay_slip(
            employee_id,
            month
        )


    # -------------------------------------------------
    # Tool 3:
    # Tax calculation
    # -------------------------------------------------

    def calculate_tax(
            self,
            employee_id: str,
            income: float
    ) -> Dict[str, Any]:

        """
        Calculate employee tax.
        """

        return self.payroll_service.calculate_tax(
            employee_id,
            income
        )


    # -------------------------------------------------
    # Tool 4:
    # Bonus details
    # -------------------------------------------------

    def get_bonus_details(
            self,
            employee_id: str
    ) -> Dict[str, Any]:

        """
        Retrieve bonus information.
        """

        return self.payroll_service.get_bonus_details(
            employee_id
        )


# -----------------------------------------------------
# MCP Tool Registration
# -----------------------------------------------------

payroll_tools = PayrollMCP()


TOOLS = {

    "get_payroll_summary":
        payroll_tools.get_payroll_summary,

    "get_pay_slip":
        payroll_tools.get_pay_slip,

    "calculate_tax":
        payroll_tools.calculate_tax,

    "get_bonus_details":
        payroll_tools.get_bonus_details
}
