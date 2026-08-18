# tools/hr_mcp.py

from services.payroll_service import PayrollService
from services.employee_service import EmployeeService
from services.leave_service import LeaveService
from services.benefits_service import BenefitsService
from services.claims_service import ClaimsService
from services.retirement_service import RetirementService
from services.policy_service import PolicyService
from services.hr_service import HRService


class HRMCP:

    def __init__(self):

        self.payroll = PayrollService()

        self.employee = EmployeeService()

        self.leave = LeaveService()

        self.benefits = BenefitsService()

        self.claims = ClaimsService()

        self.retirement = RetirementService()

        self.policy = PolicyService()

        self.hr = HRService()


    def execute(
        self,
        tool_name,
        params
    ):


        if tool_name == "get_payroll_summary":

            return self.payroll.get_summary(
                params["employee_id"]
            )


        elif tool_name == "get_employee_profile":

            return self.employee.get_profile(
                params["employee_id"]
            )


        elif tool_name == "get_leave_balance":

            return self.leave.get_balance(
                params["employee_id"]
            )


        elif tool_name == "get_benefits":

            return self.benefits.get_details(
                params["employee_id"]
            )


        elif tool_name == "get_claim_status":

            return self.claims.get_status(
                params["employee_id"]
            )


        elif tool_name == "get_retirement_summary":

            return self.retirement.get_summary(
                params["employee_id"]
            )


        elif tool_name == "search_policy":

            return self.policy.search(
                params["query"]
            )


        elif tool_name == "create_hr_case":

            return self.hr.create_case(
                params
            )


        return {

            "error": "Unknown HR MCP tool"

        }



hr_mcp = HRMCP()
